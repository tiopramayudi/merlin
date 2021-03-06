# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
    overload as typing___overload,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ResultType(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'ResultType': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['ResultType']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'ResultType']]: ...
    DOUBLE = typing___cast('ResultType', 0)
    FLOAT = typing___cast('ResultType', 1)
    INTEGER = typing___cast('ResultType', 2)
    LONG = typing___cast('ResultType', 3)
    STRING = typing___cast('ResultType', 4)
    ARRAY = typing___cast('ResultType', 10)
DOUBLE = typing___cast('ResultType', 0)
FLOAT = typing___cast('ResultType', 1)
INTEGER = typing___cast('ResultType', 2)
LONG = typing___cast('ResultType', 3)
STRING = typing___cast('ResultType', 4)
ARRAY = typing___cast('ResultType', 10)

class ModelType(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'ModelType': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['ModelType']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'ModelType']]: ...
    INVALID_MODEL_TYPE = typing___cast('ModelType', 0)
    XGBOOST = typing___cast('ModelType', 1)
    TENSORFLOW = typing___cast('ModelType', 2)
    SKLEARN = typing___cast('ModelType', 3)
    PYTORCH = typing___cast('ModelType', 4)
    ONNX = typing___cast('ModelType', 5)
    PYFUNC = typing___cast('ModelType', 6)
    PYFUNC_V2 = typing___cast('ModelType', 7)
INVALID_MODEL_TYPE = typing___cast('ModelType', 0)
XGBOOST = typing___cast('ModelType', 1)
TENSORFLOW = typing___cast('ModelType', 2)
SKLEARN = typing___cast('ModelType', 3)
PYTORCH = typing___cast('ModelType', 4)
ONNX = typing___cast('ModelType', 5)
PYFUNC = typing___cast('ModelType', 6)
PYFUNC_V2 = typing___cast('ModelType', 7)

class FileFormat(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'FileFormat': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['FileFormat']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'FileFormat']]: ...
    INVALID_FILE_FORMAT = typing___cast('FileFormat', 0)
    CSV = typing___cast('FileFormat', 1)
    PARQUET = typing___cast('FileFormat', 2)
    AVRO = typing___cast('FileFormat', 3)
    JSON = typing___cast('FileFormat', 4)
INVALID_FILE_FORMAT = typing___cast('FileFormat', 0)
CSV = typing___cast('FileFormat', 1)
PARQUET = typing___cast('FileFormat', 2)
AVRO = typing___cast('FileFormat', 3)
JSON = typing___cast('FileFormat', 4)

class SaveMode(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'SaveMode': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['SaveMode']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SaveMode']]: ...
    ERRORIFEXISTS = typing___cast('SaveMode', 0)
    OVERWRITE = typing___cast('SaveMode', 1)
    APPEND = typing___cast('SaveMode', 2)
    IGNORE = typing___cast('SaveMode', 3)
    ERROR = typing___cast('SaveMode', 4)
ERRORIFEXISTS = typing___cast('SaveMode', 0)
OVERWRITE = typing___cast('SaveMode', 1)
APPEND = typing___cast('SaveMode', 2)
IGNORE = typing___cast('SaveMode', 3)
ERROR = typing___cast('SaveMode', 4)

class PredictionJob(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version = ... # type: typing___Text
    kind = ... # type: typing___Text
    name = ... # type: typing___Text

    @property
    def bigquery_source(self) -> BigQuerySource: ...

    @property
    def gcs_source(self) -> GcsSource: ...

    @property
    def model(self) -> Model: ...

    @property
    def bigquery_sink(self) -> BigQuerySink: ...

    @property
    def gcs_sink(self) -> GcsSink: ...

    def __init__(self,
        *,
        version : typing___Optional[typing___Text] = None,
        kind : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        bigquery_source : typing___Optional[BigQuerySource] = None,
        gcs_source : typing___Optional[GcsSource] = None,
        model : typing___Optional[Model] = None,
        bigquery_sink : typing___Optional[BigQuerySink] = None,
        gcs_sink : typing___Optional[GcsSink] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PredictionJob: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PredictionJob: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bigquery_sink",b"bigquery_sink",u"bigquery_source",b"bigquery_source",u"gcs_sink",b"gcs_sink",u"gcs_source",b"gcs_source",u"model",b"model",u"sink",b"sink",u"source",b"source"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bigquery_sink",b"bigquery_sink",u"bigquery_source",b"bigquery_source",u"gcs_sink",b"gcs_sink",u"gcs_source",b"gcs_source",u"kind",b"kind",u"model",b"model",u"name",b"name",u"sink",b"sink",u"source",b"source",u"version",b"version"]) -> None: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"sink",b"sink"]) -> typing_extensions___Literal["bigquery_sink","gcs_sink"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"source",b"source"]) -> typing_extensions___Literal["bigquery_source","gcs_source"]: ...

class BigQuerySource(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OptionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> BigQuerySource.OptionsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BigQuerySource.OptionsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    table = ... # type: typing___Text
    features = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def options(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        table : typing___Optional[typing___Text] = None,
        features : typing___Optional[typing___Iterable[typing___Text]] = None,
        options : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BigQuerySource: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BigQuerySource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"features",b"features",u"options",b"options",u"table",b"table"]) -> None: ...

class GcsSource(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OptionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GcsSource.OptionsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GcsSource.OptionsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    format = ... # type: FileFormat
    uri = ... # type: typing___Text
    features = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def options(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        format : typing___Optional[FileFormat] = None,
        uri : typing___Optional[typing___Text] = None,
        features : typing___Optional[typing___Iterable[typing___Text]] = None,
        options : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GcsSource: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GcsSource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"features",b"features",u"format",b"format",u"options",b"options",u"uri",b"uri"]) -> None: ...

class Model(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OptionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Model.OptionsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Model.OptionsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ModelResult(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: ResultType
        item_type = ... # type: ResultType

        def __init__(self,
            *,
            type : typing___Optional[ResultType] = None,
            item_type : typing___Optional[ResultType] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Model.ModelResult: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Model.ModelResult: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"item_type",b"item_type",u"type",b"type"]) -> None: ...

    type = ... # type: ModelType
    uri = ... # type: typing___Text

    @property
    def result(self) -> Model.ModelResult: ...

    @property
    def options(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        type : typing___Optional[ModelType] = None,
        uri : typing___Optional[typing___Text] = None,
        result : typing___Optional[Model.ModelResult] = None,
        options : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Model: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Model: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"options",b"options",u"result",b"result",u"type",b"type",u"uri",b"uri"]) -> None: ...

class BigQuerySink(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OptionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> BigQuerySink.OptionsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BigQuerySink.OptionsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    table = ... # type: typing___Text
    staging_bucket = ... # type: typing___Text
    result_column = ... # type: typing___Text
    save_mode = ... # type: SaveMode

    @property
    def options(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        table : typing___Optional[typing___Text] = None,
        staging_bucket : typing___Optional[typing___Text] = None,
        result_column : typing___Optional[typing___Text] = None,
        save_mode : typing___Optional[SaveMode] = None,
        options : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BigQuerySink: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BigQuerySink: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"options",b"options",u"result_column",b"result_column",u"save_mode",b"save_mode",u"staging_bucket",b"staging_bucket",u"table",b"table"]) -> None: ...

class GcsSink(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OptionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GcsSink.OptionsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GcsSink.OptionsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    format = ... # type: FileFormat
    uri = ... # type: typing___Text
    result_column = ... # type: typing___Text
    save_mode = ... # type: SaveMode

    @property
    def options(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        format : typing___Optional[FileFormat] = None,
        uri : typing___Optional[typing___Text] = None,
        result_column : typing___Optional[typing___Text] = None,
        save_mode : typing___Optional[SaveMode] = None,
        options : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GcsSink: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GcsSink: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"format",b"format",u"options",b"options",u"result_column",b"result_column",u"save_mode",b"save_mode",u"uri",b"uri"]) -> None: ...
