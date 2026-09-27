

# Working with service quota checks
<a name="working-with-rs-service-quota-checks"></a>

In a multi-Region application, your standby Region often runs at reduced capacity until you need to recover into it. As demand grows in your active Region, you might raise service quotas there to keep up, but forget to request matching increases in your standby Region. This gap can cause a healthy-looking plan to fail during execution, because the standby Region can't launch enough resources to take over. To help you catch these gaps, Region switch performs service quota checks on the compute and database resources in your plan's execution blocks.

## Configuration
<a name="working-with-rs-service-quota-checks-configuration"></a>

Service quota checks are controlled by the `serviceQuotaChecksEnabled` setting on a plan. New plans have service quota checks enabled by default; plans that you created before service quota checks were available have them disabled by default.

To change the setting, set `serviceQuotaChecksEnabled` to `true` or `false` with the Region switch API, the AWS CLI, or AWS CloudFormation. In the console, select **Enable service quota warnings** or **Disable service quota warnings** on the **Edit plan details** page. When you update a plan without specifying the field, Region switch keeps the plan's current setting.

## How it works
<a name="working-with-rs-service-quota-checks-how"></a>

Region switch service quota checks compare the applied quota limits for resources defined in the plan, in each Region and account, to identify and attempt to remediate mismatches which could prevent recovery operations.

When Region switch finds a Region or account whose applied quota is lower than the matching one, it can request an increase to raise the lower quota to match the higher one. This helps ensure that either Region can provision the capacity that the plan requires, preventing constraints during failover.

Frequency of checks: Quota checks run automatically within 30 minutes of plan creation or update, and then every 24 hours. This cadence is independent of plan evaluation.

Request limits: To avoid exhausting the account-level limit on open quota increase requests, Region switch uses at most half of the allowed open requests, reserving the rest for your own submissions. In practice:
+ Commercial Regions: Up to 5 concurrent requests per account per Region
+ Opt-in Regions: Up to 1 concurrent request per account

When this limit is reached, additional mismatches are surfaced as warnings. Once open requests are approved or resolved, Region switch submits the remaining increases on the next check cycle.

**Note**  
Quota checks enforce parity between Regions only. They do not adjust quotas based on current resource consumption.

## Service quotas that Region switch checks
<a name="working-with-rs-service-quota-checks-quotas"></a>

Region switch determines which service quotas are relevant to a plan based on the compute and database resources in the plan's execution blocks. For example, on a compute execution block, Region switch identifies the resource to scale (an Amazon EC2 Auto Scaling group, an Amazon ECS service, or an Amazon EKS cluster). It describes the resource to determine the instance families and configuration it uses, and then maps that configuration to the service quotas the resource consumes.

### Permissions
<a name="working-with-rs-service-quota-checks-permissions"></a>

For Region switch to perform service quota checks, grant the required permissions to the IAM role that Region switch uses to access your resources. Region switch performs service quota checks only for plans whose execution role, and any cross-account roles that the plan uses, include these permissions.
+ `servicequotas:GetServiceQuota` allows Region switch to read applied quota values and generate warnings when it finds a mismatch.
+ `servicequotas:RequestServiceQuotaIncrease` and `servicequotas:GetRequestedServiceQuotaChange` allow Region switch to automatically submit quota increase requests on your behalf.

To determine which quotas to check, Region switch also needs `Describe` and `List` permissions for the resources in the plan. Grant the permissions for the execution block types that the plan uses.

An Amazon EC2 Auto Scaling group sometimes has no running instances, such as in a standby Region that is scaled to zero. In this case, Region switch determines the instance families from the group's launch template or launch configuration. This way, Region switch can still perform a parity check. When the group has running instances, Region switch uses those instances as the source of truth instead.

If a role is missing a required permission, plan evaluation surfaces a warning that identifies the missing permission instead of the quota result. Review these plan evaluation warnings to learn which permissions to grant. For cross-account resources, grant these permissions to the cross-account role for each account that contains resources in the plan. For more information about the permissions that Region switch requires, see [Identity and Access Management for Region switch in ARC](security-iam-region-switch.md).

**Note**  
Service Quotas requires a service-linked role in each account where quota increase requests are made, in order to create support cases. Quota increase requests fail if the service-linked role has never been created in an account. To create a service-linked role, submit a service quota increase request in your account. To let Region switch submit the first quota increase request in an account, grant `iam:CreateServiceLinkedRole` at the account level. This permission is needed only until the service-linked role exists.

**Note**  
Submitting a service quota increase request doesn't create any resources and doesn't change the resources in your account. Service quota increase requests can take several hours, or in some cases days, to be applied.

#### Service quotas that Region switch checks by execution block
<a name="working-with-rs-service-quota-checks-by-block"></a>


| Execution block | Service quotas checked | Permissions required in the execution role | 
| --- | --- | --- | 
| Amazon EC2 Auto Scaling | On-Demand and Spot instance vCPUs per instance family; Amazon EBS storage and IOPS per volume type; network interfaces per Region (when applicable). | autoscaling:DescribeAutoScalingGroups, autoscaling:DescribeLaunchConfigurations, ec2:DescribeInstances, and ec2:DescribeLaunchTemplateVersions | 
| Amazon ECS service scaling | On-Demand and Spot instance vCPUs per instance family (Amazon ECS on Amazon EC2); Fargate vCPUs for On-Demand and Spot (Amazon ECS on Fargate); Amazon EBS storage and IOPS per volume type; network interfaces per Region (when applicable). | ecs:DescribeServices, ecs:DescribeTaskDefinition, ecs:DescribeClusters, and ecs:DescribeCapacityProviders | 
| Amazon EKS resource scaling | On-Demand and Spot instance vCPUs per instance family (Amazon EC2 managed node groups); Fargate vCPUs for On-Demand and Spot (Fargate profiles); Amazon EBS storage and IOPS per volume type; network interfaces per Region (when applicable). | eks:ListNodegroups, eks:DescribeNodegroup, and eks:ListFargateProfiles | 
| Amazon RDS create cross-Region replica and Aurora provisioned scaling | Amazon RDS DB instances per Region; total storage for all DB instances per Region. | rds:DescribeDBInstances | 

## Remediating service quota warnings
<a name="working-with-rs-service-quota-checks-remediating"></a>

Service quota warnings identify quotas in your recovery plan where one Region's applied value is lower than the matching Region's. You can view these warnings on the Service quota warnings tab under the Plan evaluation tab in the console, or retrieve them programmatically using the [ListServiceQuotaWarnings](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListServiceQuotaWarnings.html) API.

### Retrieving warnings
<a name="working-with-rs-service-quota-checks-retrieving"></a>

The `ListServiceQuotaWarnings` API returns warnings for all plans accessible to the caller, including plans you own and plans shared with your account through AWS Resource Access Manager. To narrow the results, provide a list of plan Amazon Resource Names (ARNs). Region switch ignores any plan ARN that the caller cannot access. If no plan ARNs are specified, Region switch returns warnings for all accessible plans.

**Note**  
Service quota warnings are separate from plan evaluation warnings retrieved with [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html). Plan evaluation reports whether the plan's execution role is missing IAM permissions required by service quota checks. It does not report quota mismatches or the status of quota increase requests. Those details appear only in the service quota warnings returned by `ListServiceQuotaWarnings`. For more information, see the [Region Switch API Reference Guide](https://docs.aws.amazon.com/arc-region-switch/latest/api/Welcome.html) for Amazon Application Recovery Controller (ARC). For an overview of service quota checks, see [Service quota checks](region-switch-plans.md#region-switch-plans.service-quota-checks).

### Warning details
<a name="working-with-rs-service-quota-checks-warning-details"></a>

Each service quota warning includes the following information:
+ The affected service and quota
+ The Region and account where the quota is insufficient
+ If Region switch submitted an increase request, the request ID and support case ID

Because service quotas are scoped to the account and Region level, a single quota mismatch can affect more than one plan.

### Warning lifecycle
<a name="working-with-rs-service-quota-checks-warning-lifecycle"></a>

A service quota warning follows this lifecycle:
+ Increase request submitted: When Region switch submits a quota increase request, the warning remains on the plan while the request is open. After the request is approved and the new quota value is applied, Region switch removes the warning on the next check cycle.
+ Increase request denied: If the request is denied, the warning persists. Region switch submits a new request after a cooldown period, provided the mismatch still exists.
+ Increase request not submitted: When Region switch cannot submit an increase request, the warning remains until the mismatch is resolved. This can occur when Region switch has reached its limit on open requests, or when the account has reached the maximum number of open requests.

The mismatch resolves when one of the following occurs:
+ You request the increase yourself.
+ The resources in the plan change such that the existing quota is sufficient.
+ You remove the affected execution block from the plan.

**Canceling a service quota increase request**  
Service quota increase requests submitted by Region switch cannot be canceled through the Region switch API. To cancel a request, respond to the associated AWS Support case.

**Service quota warnings don't block plan execution**  
A service quota warning doesn't prevent you from executing a plan. Executing a plan while a service quota warning is active carries the same risk as executing any plan whose recovery Region has a lower quota than the matching Region: the execution can fail. Service quota warnings appear in the console when you start a plan execution, and in plan execution reports, so that you can decide whether to proceed.