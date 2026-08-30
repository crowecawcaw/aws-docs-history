# Reliability of Region switch as a recovery platform

A recovery mechanism is only useful if it works when you need it most, during an actual
Regional impairment. Region switch is designed with reliability as a core principle, so that you
can depend on it to orchestrate recovery even when parts of your infrastructure are unavailable.
The following factors contribute to the reliability of Region switch as a recovery platform.

## 1. Data and control plane API decoupling

As with many AWS services, the functionality for Region switch is divided between a
_control plane_ and _data planes_. A control plane
enables management functions such as creating, updating, and deleting resources. A data plane
provides a service's core functionality and is optimized for availability. It is designed to
maintain operations even during disruptive events when a control plane might become unavailable.

Region switch decouples these two planes so that all critical recovery capabilities are highly
reliable data plane operations. Plan creation and plan updates are control plane operations
located in US East (N. Virginia) (us-east-1) and AWS GovCloud (US-West) (us-gov-west-1).
Recovery-critical APIs, including plan execution, update execution, pause, cancel, and
retrieving open plan evaluation warnings, are all data plane operations.

The best practice is to create your Region switch recovery plan in advance of an actual recovery,
and to test it regularly as part of game days and after new deployments. This way, when a
real impairment occurs, your recovery depends only on the highly available data plane. For a
list of data plane operations, see [Region switch API operations](actions.region-switch.md "actions.region-switch.md").

## 2. Plan execution from healthy Region

When executing a Region switch plan to recover your application, you need to execute from the
Region you are activating. This ensures your recovery does not take a dependency on the
Region that is experiencing issues. Region switch provides an independent console in each
AWS Region that calls data plane API operations for recovery tasks, so you can use the
console in the Region that you're activating to execute plans for application recovery.
This design ensures that recovery remains highly reliable and available regardless of the
state of the impaired Region.

## 3. Declarative recovery plans and cross-Region replication

You can declare Region switch recovery plans as code using Terraform or
CloudFormation. This allows you to integrate your recovery plans into the same testing and deployment
rigor as your application. Changes go through code review, version control, and CI/CD
pipelines, which reduces the risk of configuration drift and untested recovery paths.

Additionally, Region switch allows failover and failback workflows to live in the same plan, and
automatically replicates the plan in both Regions. This means a single plan contains
everything needed to recover in either direction, and both Regions always have the latest
configuration. You don't need to manually synchronize plan configurations across Regions,
which eliminates a class of failures where a stale or missing plan in the target Region
blocks recovery.

Together, these design choices ensure that Region switch can reliably orchestrate your application
recovery during a Regional impairment. For more information about how AWS builds services to
meet high availability targets, see the [Static stability using
Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ "https://aws.amazon.com/builders-library/static-stability-using-availability-zones/") in the Amazon Builders' Library.
