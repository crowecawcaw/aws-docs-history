# How readiness rules

determine readiness status

ARC readiness checks determine readiness status based on the predefined rules for each resource type and the way those rules are defined.
ARC includes one group of rules for each type of resource that it supports. For example, ARC has groups of readiness rules for Amazon Aurora clusters,
Amazon EC2 Auto Scaling groups, and so on. Some readiness rules compare resources in a set to each other, and some look at specific information about each resource
in the resource set.

You can't add, edit, or remove readiness rules, or groups of rules. However, you can create an Amazon CloudWatch alarm
and create a readiness check to monitor the state of the alarm. For example, you can create a custom CloudWatch alarm to monitor Amazon EKS container
services, and create a readiness check to audit the readiness status of the alarm.

You can view all the readiness rules for each resource type in the AWS Management Console when you create a resource set, or
you can view the readiness rules later by navigating to the details page for a resource set. You can also view
readiness rules in the following section: [Readiness rules in ARC](recovery-readiness.md#recovery-readiness.list-rules "recovery-readiness.md#recovery-readiness.list-rules").

When a readiness check audits a set of resources with a set of rules, the way each rule is defined determines whether the result will be
`READY` or `NOT READY` for all the resources or if the result will be different for different resources. In addition, you can view
readiness status in multiple ways. For example, you can view the readiness status of a group of resources in a resource set or view a summary of readiness
status for a recovery group or a cell (that is, an AWS Region or Availability Zone, depending on how you've set up your recovery group).

The wording in each rule description explains how it evaluates the resources to determine the readiness status when that
rule is applied. A rule is defined to inspect _each resource_ or to inspect _all resources_ in a resource set to
determine readiness. Specifically, the rules work as follows:

- The rule inspects _each resource_ in the resource set to ensure a condition.

      + If all resources succeed, all resources are set as `READY`.
      + If one resource fails, that resource is set as `NOT READY`, and the other cells remain `READY`.

  For example: **MskClusterState:** Inspects each Amazon MSK cluster to ensure that it is in an
  `ACTIVE` state.

- The rule inspects _all resources_ in the resource set to ensure a condition.
  - If the condition is ensured, all resources are set as `READY`.
  - If any fails to meet the condition, all resources are set as `NOT READY`.For example: **VpcSubnetCount:** Inspects all VPC subnets to ensure that they have the same
    number of subnets.

- Non-critical rule: The rule inspects all resources in the resource set to ensure a condition.

      + If any fails, the readiness status is unchanged. A rule with this behavior has a note in its description.For example: **ElbV2CheckAzCount:** Inspects each Network Load Balancer to ensure that it is attached to only one Availability Zone.

  Note: This rule does not affect readiness status.
  In addition, ARC takes an extra step for quotas. If a readiness check detects a mismatch across cells for service
  quotas (the maximum value for resource creation and operations) for any supported resource, ARC automatically raises the quota
  for the resource with the lower quota. This applies only to quotas (limits). For capacity, you should add additional capacity
  as required for your application needs.

You can also set up an Amazon EventBridge notification for readiness checks, for example, when any readiness check status changes to `NOT READY`.
Then when a configuration mismatch is detected, EventBridge sends you a notification and you can take corrective action to make
sure that your application replicas are aligned and prepared for recovery. For more information, see [Using readiness check in ARC with Amazon EventBridge](eventbridge-readiness.md "eventbridge-readiness.md").
