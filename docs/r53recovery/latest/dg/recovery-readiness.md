# Readiness check in ARC

With readiness check in Amazon Application Recovery Controller (ARC), you can gain insights into whether your applications
and resources are prepared for recovery. After you model your AWS application in ARC and
create readiness checks, the checks continually monitor information about your application, such
as AWS resource quotas, capacity, and network routing policies. Then, you can choose to be
notified about changes that would affect your ability to fail over to a replica of your application,
to recover from an event. Readiness checks help make sure, on an ongoing basis, that you can maintain
your multi-Region applications in a state that is scaled and configured to handle failover traffic.

This chapter explains how to model your application in ARC to set up the structure that
enables readiness checks to work, by creating a recovery group and cells that describe your application.
Then, you can follow the steps to add readiness checks and readiness scopes so that ARC can audit
readiness for your application.

After you create readiness checks, you can monitor the readiness status of your resources.
Readiness checks help you to ensure that a standby application replica and its resources match your production
replica on an ongoing basis, reflecting the capacity, routing policies, and other configuration details of your production
application. If the replica doesn't match, you can add capacity or change a configuration so that your application
replicas are aligned again.

###### Important

Readiness checks are most useful for verifying, on an ongoing basis, that application replica
configurations and runtime states are aligned. Readiness checks shouldn't be used to indicate whether your
production replica is healthy, nor should you rely on readiness checks as a primary trigger for failover
during a disaster event.

## Set up a resilient recovery process for your application

To use Amazon Application Recovery Controller (ARC) with AWS applications that are in multiple AWS Regions, there are guidelines
to follow to set up your applications for resilience, so that you can support recovery readiness effectively.
Then, you can create readiness checks for your application and set up routing controls to reroute traffic
for failover. You can also review the recommendations ARC provides to about your application's architecture
that can improve resiliency.

###### Note

If you have an application that is siloed by Availability Zones, consider using zonal shift or
zonal autoshift for failover recovery. No setup is required to use zonal shift or zonal autoshift to reliably
recover applications from Availability Zone impairments.

To move traffic away from an Availability Zone for load balancer resources, start a zonal shift in
the ARC console or in the ELB console. Or, you can use the AWS Command Line Interface or AWS SDK with zonal shift
API actions. For more information, see [Zonal shift in ARC](arc-zonal-shift.md "arc-zonal-shift.md").

To learn more about getting started with resilient failover configurations, see [Getting started with multi-Region recovery in Amazon Application Recovery Controller (ARC)](getting-started.md "getting-started.md").
