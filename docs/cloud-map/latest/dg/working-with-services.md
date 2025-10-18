# AWS Cloud Map services

An AWS Cloud Map service is a template for registering service instances that consists of the
 service name and DNS configuration, if applicable, for the service. You can also set up a
 health check to determine the health status of instances in the service and filter out
 unhealthy resources. A service can represent a component of your application. For example,
 you can create a service for resources that handle payments on your application and another
 for resources that manage users.

A service allows you to locate the resources for an application by getting back one or
 more endpoints that can be used to connect to the resource. The location of resources is
 done using DNS queries or the AWS Cloud Map [`DiscoverInstances`](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html") API
 action, depending on how you've configured the namespace. You can use the AWS Cloud Map console to
 scope instance discovery at the service level.

You can also specify custom metadata as atttributes at the service level using the
 `UpdateServiceAttributes` API. You can set service attributes to avoid duplicating attributes across
 instances and modify these attributes
 without needing to make any changes to instance attributes. Information you can specify as
 attributes at the service level includes, but isn't limited to, the following:


* Endpoint weights for shifting traffic during progressive deployments.
* Service preferences such as API timeouts and suggested retry policies.
For more information, see [UpdateServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateServiceAttributes.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateServiceAttributes.html") in the *AWS Cloud Map API reference*.

The following topics describe health check and DNS configurations for services and include
 instructions for creating, listing, updating, and deleting a service.

###### Topics

* [AWS Cloud Map service health check
 configuration](services-health-checks.md "services-health-checks.md")
* [AWS Cloud Map service DNS configuration](services-route53.md "services-route53.md")
* [Creating an AWS Cloud Map service for an application
 component](creating-services.md "creating-services.md")
* [Updating an AWS Cloud Map service](editing-services.md "editing-services.md")
* [Listing AWS Cloud Map services in a namespace](listing-services.md "listing-services.md")
* [Deleting an AWS Cloud Map service](deleting-services.md "deleting-services.md")
