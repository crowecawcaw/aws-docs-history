# Data and control planes for zonal autoshift

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that
you make sure that the mechanisms that you depend on during failover are highly available,
so that you can use them when you need them in a disaster scenario. Typically, you should use data plane
functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind, it's important to understand how the
functionality of a service is divided between control planes and data planes, and when you can rely on an expectation of extreme reliability with a
service's data plane.

In general, a _control plane_ enables you to do basic management functions, such as create, update,
and delete resources in the service. A _data plane_ provides a service's core functionality.

For more information about data planes, control planes, and how AWS builds services to meet high availability targets,
see the [Static
stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ "https://aws.amazon.com/builders-library/static-stability-using-availability-zones/") in the Amazon Builders' Library.
