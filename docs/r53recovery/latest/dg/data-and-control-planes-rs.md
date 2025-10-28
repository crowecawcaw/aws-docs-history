# Data and control planes for Region switch

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that
you make sure that the mechanisms that you depend on during failover are highly available,
so that you can use them when you need them in a disaster scenario. Typically, you should use data plane
functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind,
it's important to understand how the functionality of a service is divided between control planes and data planes,
and when you can rely on an expectation of extreme reliability with a service's data plane.

As with many AWS services,
the functionality for the Region switch capability is supported by a control plane and data planes. While both types
built to be reliable, a control plane is optimized for data consistency, while a data plane is optimized
for availability. A data plane is designed for resilience so that it can maintain availability even during
disruptive events, when a control plane might become unavailable.

In general, a _control plane_ enables you to do basic management functions, such as create, update,
and delete resources in the service. A _data plane_ provides a service's core functionality. Because of this,
we recommend that you use data plane operations when availability is important, for example, when you
need to get information about a Region switch plan during an outage.

For Region switch, the control planes and data planes are divided as follows:

- The control plane for Region switch is located in US East (N. Virginia) Region (us-east-1) and is
  meant to only be used for service management, that is, creating and updating plans, not for recovery,
  that is, executing plans. _The Region switch configuration control plane API operations are not highly available._
- Region switch has independent data planes in each AWS Region. You should use the data plane
  for recovery actions, that is, for executing Region switch plans. For a list of the data
  plan operations, see [Region switch API operations](actions.md "actions.md").
  _These Region switch data plane operations are highly available._
  Region switch provides an independent console in each AWS Region, which calls data plane API operations for
  recovery tasks, so you can use the console in the Region that you're activating to execute plans for application
  recovery. For more information about key considerations when you prepare for and complete a recovery operation with Region switch,
  see [Best practices for Region switch in ARC](best-practices.md "best-practices.md").

For more information about data planes, control planes, and how AWS builds services to meet high availability targets,
see the [Static
stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ "https://aws.amazon.com/builders-library/static-stability-using-availability-zones/") in the Amazon Builders' Library.
