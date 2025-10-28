# Data and control planes for routing control

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that
you make sure that the mechanisms that you depend on during failover are highly available,
so that you can use them when you need them in a disaster scenario. Typically, you should use data plane
functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind, it's important to understand how the
functionality of a service is divided between control planes and data planes, and when you can rely on an expectation of extreme reliability with a
service's data plane.

As with most AWS services,
the functionality for the routing control capability is supported by control planes and data planes. While both of these are built to be reliable,
a control plane is optimized for data consistency, while a data plane is optimized for availability. A data plane is designed
for resilience so that it can maintain availability even during disruptive events, when a control plane might become unavailable.

In general, a _control plane_ enables you to do basic management functions, such as create, update,
and delete resources in the service. A _data plane_ provides a service's core functionality. Because of this,
we recommend that you use data plane operations when availability is important, for example, when you
need to reroute traffic to a standby replica during an outage.

For routing control, the control planes and data planes are divided as follows:

- The control plane API for routing control is the
  [Recovery Control Configuration API](../../../recovery-cluster/latest/api/what-is-recovery-control.md "../../../recovery-cluster/latest/api/what-is-recovery-control.md"), supported in
  the US West (Oregon) Region (us-west-2). You use these API operations or the AWS Management Console to create or delete clusters,
  control panels, and routing controls, to help prepare for a disaster recovery event when you might need to reroute
  traffic for your application.
  _The routing control configuration control plane is not highly available._
- The routing control data plane is a dedicated cluster across five geographically-isolated AWS
  Regions. Each customer creates one or more clusters using the routing control control plane. The cluster hosts control
  panels and routing controls. Then you use the [Routing Control (Recovery Cluster) API](../../../routing-control/latest/APIReference/Welcome.md "../../../routing-control/latest/APIReference/Welcome.md")
  to get, list, and update routing control states when you want to reroute traffic for your application. _The routing
  control data plane IS highly available._
  Because the routing control data plane is highly available, we recommend that you plan to use the AWS Command Line Interface to
  make API calls to work with routing control states when you want to fail over to recover from an event. For more
  information about key considerations when you prepare for and complete a recovery operation with routing control,
  see [Best practices for routing control in ARC](route53-arc-best-practices.md "route53-arc-best-practices.md").

For more information about data planes, control planes, and how AWS builds services to meet high availability targets,
see the [Static
stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ "https://aws.amazon.com/builders-library/static-stability-using-availability-zones/") in the Amazon Builders' Library.
