# Copyright 2020 The Merlin Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import asyncio
import logging
import traceback

import kfserving
import uvloop
from prometheus_client import CollectorRegistry, multiprocess

from pyfuncserver import PyFuncModel
from pyfuncserver.server import PyFuncServer

DEFAULT_MODEL_NAME = "model"
DEFAULT_LOCAL_MODEL_DIR = "/tmp/model"

parser = argparse.ArgumentParser(parents=[kfserving.kfserver.parser])
parser.add_argument('--model_dir', required=True,
                    help='A URI pointer to the model binary')
parser.add_argument('--model_name', default=DEFAULT_MODEL_NAME,
                    help='The name that the model is served under.')
parser.add_argument('--dry_run', default=False, action='store_true', required=False,
                    help="Dry run pyfunc server by loading the specified model "
                         "in --model_dir without starting webserver")
args, _ = parser.parse_known_args()

logging.getLogger('tornado.access').disabled = True

if __name__ == "__main__":
    # initialize prometheus
    # register to MultiProcessCollector as PyFuncServer will run in multiple process
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)

    # use uvloop as the event loop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    # load model
    model = PyFuncModel(args.model_name, args.model_dir)
    try:
        model.load()
    except Exception as e:
        logging.error(f"Unable to initalize model")
        logging.error(traceback.format_exc())
        logging.error(
            """
            Some module might be missing from your pyfunc model.
            If the module is part of your code, 
            you can specify it as 'code' argument when calling log_pyfunc, e.g.:
            
            merlin.log_pyfunc_model(model_instance=MyModel(), 
                    conda_env="env.yaml",
                    code=["path/to/your/package"])
                    
            If the module is a python package, then you should add it in the
            conda env.yaml that you pass to log_pyfunc method, e.g.:
            
            dependencies:
            - python=3.7
            - pip:
              - my-missing-package==1.0
              
            OR if the package is not available in PyPI distribution
            
            dependencies:
            - python=3.7
            - my-missing-package=1.0
            
            See: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
            """)
        exit(1)

    if args.dry_run:
        logging.info("dry run success")
        exit(0)
        

    PyFuncServer(registry).start([model])
