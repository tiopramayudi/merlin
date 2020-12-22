// Code generated by client-gen. DO NOT EDIT.

package v1alpha3

import (
	v1alpha3 "github.com/gojek/merlin/istio/client-go/pkg/apis/networking/v1alpha3"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	types "k8s.io/apimachinery/pkg/types"
	rest "k8s.io/client-go/rest"
)

// VirtualServicesGetter has a method to return a VirtualServiceInterface.
// A group's client should implement this interface.
type VirtualServicesGetter interface {
	VirtualServices(namespace string) VirtualServiceInterface
}

// VirtualServiceInterface has methods to work with VirtualService resources.
type VirtualServiceInterface interface {
	Create(*v1alpha3.VirtualService) (*v1alpha3.VirtualService, error)
	Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1alpha3.VirtualService, err error)
	Delete(name string, options *v1.DeleteOptions) error
	VirtualServiceExpansion
}

// virtualServices implements VirtualServiceInterface
type virtualServices struct {
	client rest.Interface
	ns     string
}

// newVirtualServices returns a VirtualServices
func newVirtualServices(c *NetworkingV1alpha3Client, namespace string) *virtualServices {
	return &virtualServices{
		client: c.RESTClient(),
		ns:     namespace,
	}
}

// Create takes the representation of a virtualService and creates it.  Returns the server's representation of the virtualService, and an error, if there is any.
func (c *virtualServices) Create(virtualService *v1alpha3.VirtualService) (result *v1alpha3.VirtualService, err error) {
	result = &v1alpha3.VirtualService{}
	err = c.client.Post().
		Namespace(c.ns).
		Resource("virtualservices").
		Body(virtualService).
		Do().
		Into(result)
	return
}

// Patch applies the patch and returns the patched virtualService.
func (c *virtualServices) Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1alpha3.VirtualService, err error) {
	result = &v1alpha3.VirtualService{}
	err = c.client.Patch(pt).
		Namespace(c.ns).
		Resource("virtualservices").
		SubResource(subresources...).
		Name(name).
		Body(data).
		Do().
		Into(result)
	return
}

// Delete takes name of the virtualService and deletes it. Returns an error if one occurs.
func (c *virtualServices) Delete(name string, options *v1.DeleteOptions) error {
	return c.client.Delete().
		Namespace(c.ns).
		Resource("virtualservices").
		Name(name).
		Body(options).
		Do().
		Error()
}