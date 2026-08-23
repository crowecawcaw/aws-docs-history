# Application status checks

Application status checks help you monitor the performance and health of your
applications running on Amazon EC2. With application status checks, you can detect and
respond to application health impairments by monitoring your applications through
configurable paths and ports. For example, you can use application status checks
to confirm that your web server is listening on its expected port and accepting new
connections.

Application status checks monitor the HTTP and HTTPS responses of your applications at configurable paths and ports. They run every 60 seconds and integrate with Amazon EC2 Auto Scaling, so you can automate replacement of instances whose applications are impaired.

###### Contents

- [How application status checks work](#how-application-status-checks-work "#how-application-status-checks-work")
- [Get started with application status checks](#get-started-application-status-checks "#get-started-application-status-checks")
- [Configuration options](#asc-configuration-options "#asc-configuration-options")
- [Default settings](#asc-default-settings "#asc-default-settings")
- [Amazon EC2 Auto Scaling integration](#asc-auto-scaling-integration "#asc-auto-scaling-integration")
- [Handling deployment, in-place patching, and replacements](#asc-handling-deployment-and-patching "#asc-handling-deployment-and-patching")
- [Testing a new application status check](#asc-testing-a-new-check "#asc-testing-a-new-check")
- [Advanced networking](#asc-advanced-networking "#asc-advanced-networking")
- [Best practices](#asc-best-practices "#asc-best-practices")
- [Troubleshooting](#asc-troubleshooting "#asc-troubleshooting")
- [Monitor application status checks](#asc-monitoring "#asc-monitoring")
- [Security and permissions](#asc-security-and-permissions "#asc-security-and-permissions")
- [Pricing](#asc-pricing "#asc-pricing")
- [Quotas](#asc-quotas "#asc-quotas")

## How application status checks work

Application status checks send HTTP or HTTPS requests to an endpoint listening
at a network port on your instance every 60 seconds. AWS compares the response code against the status code matcher you configured. The check is marked impaired after a number of consecutive failed requests, and healthy again after a number of consecutive successful requests. Both counts default to 2 and are configurable. For more information, see [Evaluation thresholds](#asc-config-evaluation "#asc-config-evaluation").

###### Note

Application status checks send the health check request over HTTP/2.

The HTTPS protocol check does not validate the server certificate.

During a reboot, application status checks report a failure until the
instance becomes available again because the application cannot respond to
health check requests while the operating system is restarting.

### Network architecture

Application status checks originate from the Amazon EC2 application
status checks service. To reach your instances, AWS creates a managed
elastic network interface (ENI) in your VPC. AWS creates one ENI per combination of source subnet and security group that has associated instances. AWS creates the managed
ENI when an application status check first requires that combination, and
removes it when no remaining application status check requires it. The
managed ENI does not count against your instance ENI limit, but does count
against the _Network interfaces per Region_ quota for your
account, which is enforced per Availability Zone. For more information, see
[Amazon VPC
quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md").

By default, Amazon EC2 hides these managed network interfaces from the console
and API list operations for accounts that did not have managed resources before
this setting became available. To change their visibility, see [Managed resource visibility settings](amazon-ec2-managed-instances.md#managed-resource-visibility-settings "amazon-ec2-managed-instances.md#managed-resource-visibility-settings").

AWS creates one managed network interface for each combination of source
subnet and security group among your associated instances. The number of
managed interfaces grows with the number of distinct subnet and security group
combinations your monitored instances use. Consolidating monitored instances
into fewer subnet and security group combinations reduces the number of managed
interfaces. For example, 200 instances spread across 2 subnets that all use a
single security group produce 2 managed interfaces. The same 200 instances using
3 security groups across those 2 subnets produce up to 6 managed interfaces. Each
interface corresponds to one subnet and security group combination.

Application status checks reach your instances from a private vantage
point within your VPC. The scope describes where the check originates, not
a property of your instance's IP address. AWS creates the managed ENI in
a subnet within your VPC and reaches the instance over the private network
path.

With AWS managed network paths, health check traffic originates from AWS
managed Amazon EC2 instances in the same Availability Zone as the target instance (or
the parent Availability Zone for Local Zone targets). The traffic travels over
the AWS internal network and does not traverse the public internet. For more
information, see [Amazon VPC
FAQs](https://aws.amazon.com/vpc/faqs/ "https://aws.amazon.com/vpc/faqs/") on the Amazon Web Services website.

With customer-managed network paths, you choose the source subnets, so you
can run checks from a different Availability Zone than the target. For more
information, see [Cross-Availability Zone monitoring](#asc-cross-az "#asc-cross-az").

### AWS managed and customer-managed network paths

Application status checks support two onboarding modes that determine
who selects the source subnets and security groups for the health check
ENI and the destination subnets and security groups for the target
instances.

AWS managed network paths

AWS selects the source subnets and security groups for the
health check ENI and the destination subnets and security
groups for the target instances.

Customer-managed network paths

You specify the source subnets and security groups for the
health check ENI and the destination subnets and security
groups for the target instances.

Use customer-managed network paths when you need to control
which subnets and security groups health check traffic
originates from, such as when your VPC has strict network
segmentation, firewall rules, or compliance requirements that
restrict which sources can reach your application
endpoints.

You choose the mode by including or omitting the `--health-check-paths` parameter in the create command. If you
omit the `--health-check-paths` parameter, AWS selects source
and destination subnets and security groups (AWS managed network paths).
If you include the `--health-check-paths` parameter, you manage
them (customer-managed network paths).

### IP version

Each application status check is associated with a single IP version
(IPv4 or IPv6). To monitor an instance over both IPv4 and IPv6, create two
separate application status checks and associate both with the
instance.

Checks reach your instance from within your VPC for both IPv4 and
IPv6.

### Check status values

Each individual check reports one of the following statuses:

- `passed`: the check completed successfully
- `failed`: the check failed. The response includes
  the HTTP status code returned by your application. For
  interpretation and remediation guidance, see [Troubleshooting](#asc-troubleshooting "#asc-troubleshooting").
- `initializing`: the check has not yet completed its
  first evaluation
- `insufficient-data`: the check did not receive enough
  data to determine a result
- `not-applicable`: the check is not associated with the
  instance

The overall application status reported for the instance aggregates all
individual check results. The overall status is one of the following:

- `ok`: all checks passed
- `impaired`: one or more checks failed
- `initializing`: one or more checks have not yet
  completed their first evaluation
- `insufficient-data`: one or more checks report
  insufficient data
- `not-applicable`: all associated application status checks are excluded from aggregation
- `suppressed`: application status check evaluation is
  suppressed for the instance

### Aggregation

You can mark each application status check as included in or excluded from the overall status for the instance. By default, a check is
`included`.

`included`

The check contributes to the overall status for the instance and Amazon EC2 Auto Scaling uses it.

`excluded`

The check reports its individual status but does not contribute to the overall status for the instance and Amazon EC2 Auto Scaling does not use it. Use this setting to validate a new check in
production without affecting the overall status or triggering
Amazon EC2 Auto Scaling replacements. This is the recommended workflow when
adding a check to an existing production workload; see [Testing a new application status check](#asc-testing-a-new-check "#asc-testing-a-new-check").

## Get started with application status checks

###### Prerequisites

Before you create an application status check, make sure you have the
following:

- A VPC with the instances you want to monitor.
- An application endpoint on each instance that can respond to HTTP or
  HTTPS requests on the port and HTTP path you will configure.
- A security group on each destination instance that allows inbound
  traffic on the check port from the source security group used by the
  application status check. See [Security and permissions](#asc-security-and-permissions "#asc-security-and-permissions").

###### Step 1: Configure your application

Configure your application endpoint to respond to HTTP or HTTPS requests
on the port and HTTP path you will specify when you create the check.
Return a response code included in your status code matcher to indicate
the application is healthy.

Make sure the destination instance's security group allows inbound traffic
on the check port from the source security group used by the application
status check. For managed network paths, AWS provides the source security
group at check creation. For customer-managed network paths, you specify the
source security group when you create the check.

###### Step 2: Create a check definition

Use the AWS CLI to create an application status
check.

Console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under
   **Instances**, choose **Application
   status checks**.
3. Choose **Create application status
   check**.
4. Under **Health check logic**, configure the
   following:

   - **Protocol**: choose
     **HTTP** or
     **HTTPS**.
   - **Port**: enter the port on which
     your application listens.
   - **Path** (optional): enter the HTTP
     path to request, for example
     `/healthcheck`.
   - **IP version**: choose
     **IPv4** or
     **IPv6**.
   - **Device index**: the network
     interface device index to check. Default is
     `0`.

5. Under **Controls and thresholds**, set the
   **Timeout**, and optionally the **Status
   code matcher**, **Failure threshold**,
   **Success threshold**, and
   **Initialization grace period**. The check
   interval is fixed at 60 seconds.
6. Under **Aggregation**, choose
   **Included** for the check to contribute to the
   overall application status and drive Amazon EC2 Auto Scaling, or
   **Excluded** to report the check without
   affecting the overall status.
7. Under **Health check paths**, keep
   **Do not specify network paths
   (recommended/default)** to let Amazon EC2 place the health
   check network interfaces in your instance's subnets, or choose
   **Specify network paths (advanced)** to define
   the source subnet, security group, and destinations
   yourself.
8. (Optional) Add a **Name tag** and other
   **Tags**.
9. Choose **Create application status
   check**.

AWS CLI
To use AWS managed network paths, omit the
`--health-check-paths` parameter and let AWS select
source and destination subnets and security groups.

```
aws ec2 create-application-status-check \
        --protocol https \
        --port 443 \
        --path "/health" \
        --status-code-matcher "200"
```

To use customer-managed network paths, include the
`--health-check-paths` parameter. Each health check path
contains a source (subnet and security group for the health check
ENI) and one or more destinations (subnet and security group for the
target instances).

```
aws ec2 create-application-status-check \
        --protocol https \
        --port 443 \
        --path "/health" \
        --status-code-matcher "200" \
        --health-check-paths '[{"Source":{"SubnetId":"subnet-111","SecurityGroupId":"sg-aaa"},"Destinations":[{"SubnetId":"subnet-222","SecurityGroupId":"sg-bbb"}]}]'
```

###### Step 3: Associate the check with instances

Associate the check with the instances you want to monitor, either by
instance ID or by tag.

Console

1. In the navigation pane, under
   **Instances**, choose **Application
   status checks**, and select the check.
2. Choose **Manage status check
   associations**, then choose **Manage
   associations by resource ID** or **Manage
   associations by tags**.
3. To associate with all instances in an Auto Scaling group, choose
   **Manage associations by tags** and enter
   `aws:autoscaling:groupName` as the tag key and your
   Auto Scaling group name as the value.
4. Choose **Associate**.

AWS CLI
By instance ID:

```
aws ec2 associate-application-status-check \
        --application-status-check-id asc-1234567890abcdef0 \
        --instance-ids i-0123456789abcdef0
```

By tag:

```
aws ec2 associate-application-status-check \
        --application-status-check-id asc-1234567890abcdef0 \
        --target-tag-associations Key=Environment,Value=production
```

To associate with all instances in an Auto Scaling group, use the
`aws:autoscaling:groupName` system tag:

```
aws ec2 associate-application-status-check \
        --application-status-check-id asc-1234567890abcdef0 \
        --target-tag-associations Key=aws:autoscaling:groupName,Value=`my-asg`
```

Associate and disassociate operations return per-instance success and
failure results. If some instances cannot be associated (for example, because
the check is already associated), those instances appear in the unsuccessful
results with a reason.

###### Step 4: View results

View the per-instance application health status.

Console

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance, and then choose the **Status
   and alarms** tab.
4. Under **Application status checks**, review
   the overall status and each associated check's individual
   status.

AWS CLI

```
aws ec2 describe-application-status \
        --instance-ids i-0123456789abcdef0
```

The response includes the overall application status and, for each
associated check, the check status and, for failed checks, the HTTP
status code returned by your application.

Example response:

```
{
        "ApplicationStatuses": [
            {
                "InstanceId": "i-0123456789abcdef0",
                "ApplicationStatus": {
                    "Status": "ok",
                    "Details": [
                        {
                            "ApplicationStatusCheckId": "asc-1234567890abcdef0",
                            "Status": "passed",
                            "Reason": {
                                "Code": "ResponseCodeMatched",
                                "StatusCode": 200,
                                "Protocol": "HTTP"
                            }
                        }
                    ]
                }
            }
        ]
    }
```

To view check definitions (not per-instance status), use [describe-application-status-checks](../../../cli/latest/reference/ec2/describe-application-status-checks.md "../../../cli/latest/reference/ec2/describe-application-status-checks.md"). This command returns
the configuration of your application status checks, including
protocol, port, HTTP path, and status code matcher settings.

## Configuration options

Application status checks accept several configuration parameters. This
section explains the parameters where the behavior isn't self-evident from
the parameter name. For the complete list of parameters and validation
rules, see [CreateApplicationStatusCheck](../APIReference/API_CreateApplicationStatusCheck.md "../APIReference/API_CreateApplicationStatusCheck.md") and [AssociateApplicationStatusCheck](../APIReference/API_AssociateApplicationStatusCheck.md "../APIReference/API_AssociateApplicationStatusCheck.md") in the
_Amazon EC2 API Reference_.

### Evaluation thresholds

`FailureThreshold`

The number of consecutive failed requests before the
check is marked impaired. Default: 2.

`SuccessThreshold`

The number of consecutive successful requests before the
check is marked healthy again. Default: 2.

`Timeout`

The number of seconds to wait for a response before the
request is recorded as failed. Enforced as a forced
timeout; if your application does not respond within this
window, the request is recorded as a failure regardless of
eventual response. Default: 6. Valid range: 1-30.

### Startup grace period

`InitializationGracePeriodSeconds`

The number of seconds to wait after an instance launches before AWS starts evaluating the check. Use this
parameter to give applications time to start listening
before checks begin. If the grace period is too short,
Amazon EC2 Auto Scaling might replace new instances before their
application is ready. Default: 300. Valid range: 1 to 600.

### IP scope

`IpScope`

Application status checks use `private` scope; the
check runs from within your VPC. For IPv4, this corresponds to
the instance's private IP address. For IPv6, AWS does not
classify the address as public or private; the check accepts
any IPv6 address and evaluates it from within your VPC.

### Device index

`DeviceIndex`

The index of the network device on your instance that
AWS evaluates for the health check. Change this when
your instance's primary network device is not the one you
want checked. Default: 0.

Aggregation, IP version, and health check paths (source and destination
subnets and security groups) are covered in their own sections earlier on
this page.

## Default settings

With AWS managed network paths, application status checks use the
following defaults.

| Setting                            | Default                              |
| ---------------------------------- | ------------------------------------ |
| Check interval                     | 60 seconds (fixed; not configurable) |
| Failure threshold                  | 2 consecutive failures               |
| Success threshold                  | 2 consecutive successes              |
| Timeout                            | 6 seconds                            |
| Status code matcher                | 200                                  |
| HTTP path                          | /                                    |
| IP version                         | ipv4                                 |
| IP scope                           | private                              |
| Device index                       | 0                                    |
| Initialization grace period        | 300 seconds                          |
| Aggregation                        | included                             |
| Source subnets and security groups | Managed by AWS                       |

## Amazon EC2 Auto Scaling integration

Amazon EC2 Auto Scaling automatically terminates and replaces instances whose overall
application status reports `impaired`, as long as the check is
included in aggregation. No Auto Scaling group configuration is required beyond
associating the application status check with the instances in the
group.

Amazon EC2 Auto Scaling uses the overall status for the instance, not individual check
status. Checks marked `excluded` do not drive Amazon EC2 Auto Scaling actions.
Checks in the `suppressed` state do not drive Amazon EC2 Auto Scaling
actions.

Use the `InitializationGracePeriodSeconds` parameter on the check
to allow new instances time to start up before application status checks
begin. If the grace period is too short, new instances might be terminated and
replaced by Amazon EC2 Auto Scaling before their application is ready to serve traffic.

The check's `InitializationGracePeriodSeconds` sets how long after an
instance launches before the check starts evaluating the application. Set it to
cover your application's startup time, so the check does not report
`impaired` while the application is still starting up. The Auto Scaling group's
health check grace period is separate. It sets how long after an instance enters
service before Amazon EC2 Auto Scaling terminates it for a failed health check.

For more information about how Amazon EC2 Auto Scaling uses health checks, see [Health checks for instances in an Auto Scaling group](../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md") and [Use application status checks with an Auto Scaling group](../../../autoscaling/ec2/userguide/use-application-status-checks-auto-scaling-group.md "../../../autoscaling/ec2/userguide/use-application-status-checks-auto-scaling-group.md") in the
_Amazon EC2 Auto Scaling User Guide_.

## Handling deployment, in-place patching, and replacements

Deployments, in-place patching, and other maintenance operations can
temporarily stop or restart your application. During that time,
application status checks report a failure because the application cannot
respond to health check requests. If your instances are in an Auto Scaling group
with application status checks included in aggregation, Amazon EC2 Auto Scaling might
terminate and replace these instances even though the disruption is
expected.

### Option A: Suppress the check

Use suppression for bounded maintenance windows where you know the
duration. Suppression is enforced at the instance level. You specify a duration, or omit it to suppress the check until you disable the suppression.

AWS CLI

```
aws ec2 enable-application-status-check-suppression \
        --instance-ids i-0123456789abcdef0 \
        --duration-seconds 3600
```

The response returns, for each instance, when suppression started
and when it will end. Partial success is possible; some instances
may fail to be suppressed and appear in the response with a
reason.

To resume checks before the suppression window expires:

```
aws ec2 disable-application-status-check-suppression \
        --instance-ids i-0123456789abcdef0
```

While suppressed, the overall application status for the instance
reports `suppressed`. Amazon EC2 Auto Scaling does not act on
`suppressed` instances.

### Option B: Exclude the check from aggregation

If you want the check to keep evaluating and reporting its individual
status but not affect the overall status or trigger Amazon EC2 Auto Scaling actions, set
the check's aggregation setting to `excluded`. This is useful
for longer-lived scenarios such as rolling out a new check version or
validating a change without risking replacement, and for cases where
you want telemetry to continue without operational impact.

For more information, see [Aggregation](#asc-aggregation "#asc-aggregation").

### Option C: Disassociate the check

Use disassociation for longer-lived or indefinite removal.

```
aws ec2 disassociate-application-status-check \
        --application-status-check-id asc-1234567890abcdef0 \
        --instance-ids i-0123456789abcdef0
```

If you associated by tag, remove the tag from the instance to
disassociate. After disassociation, the overall application status for
the instance reports `not-applicable`.

### Deployment guidance

Deployments are the most common maintenance scenario that requires
suppression. Use suppression when your deployment tool has a
pre-deployment hook and a post-deployment hook so that you can suppress
the check before the deployment starts and disable suppression after the
deployment completes.

The general pattern is:

1. In the pre-deployment hook, call [enable-application-status-check-suppression](../../../cli/latest/reference/ec2/enable-application-status-check-suppression.md "../../../cli/latest/reference/ec2/enable-application-status-check-suppression.md") for the
   instance, with a duration that covers the expected deployment
   window.
2. Perform the deployment.
3. In the post-deployment hook, call [disable-application-status-check-suppression](../../../cli/latest/reference/ec2/disable-application-status-check-suppression.md "../../../cli/latest/reference/ec2/disable-application-status-check-suppression.md") for the
   instance.

If your deployment tool does not have hooks, drive suppression from the
CI/CD pipeline that invokes the deployment.

## Testing a new application status check

You can validate a new application status check in production before it
starts contributing to your instance-level monitoring. Set the aggregation
setting to `excluded` when you create the check, then confirm it
reports the expected status and HTTP response codes. When you're ready,
change the setting to `included` so the check contributes to the
overall status for the instance and integrates with Amazon EC2 Auto Scaling.

1. Create the check with the aggregation setting set to
   `excluded`.

```
aws ec2 create-application-status-check \
        --protocol https \
        --port 443 \
        --path "/health" \
        --status-code-matcher "200" \
        --aggregation excluded
```

2. Associate the check with a test instance or a subset of your
   production fleet.
3. Wait for at least two check intervals (approximately two minutes) to
   allow the check to complete an initial evaluation.
4. Use [describe-application-status](../../../cli/latest/reference/ec2/describe-application-status.md "../../../cli/latest/reference/ec2/describe-application-status.md") to verify the check is
   reporting the expected status and HTTP response code.

```
aws ec2 describe-application-status \
        --instance-ids i-0123456789abcdef0
```

5. If the check reports as expected, update the aggregation setting to
   `included` to make the check contribute to the overall
   status for the instance and drive Amazon EC2 Auto Scaling actions.

```
aws ec2 modify-application-status-check \
        --application-status-check-id asc-1234567890abcdef0 \
        --aggregation included
```

## Advanced networking

Application status checks originate from a managed ENI in the source subnet
and security group you specify (or that AWS selects for you). For workloads
that require higher availability than a single-source configuration provides,
or for workloads that run in Local Zones or Outposts, consider the following
patterns.

### Cross-Availability Zone monitoring

For Availability Zone redundancy, you can run health checks from more than
one Availability Zone. With customer-managed network paths, you define health
check paths whose sources are in two different Availability Zones that reach
the same destination instances, using the `--health-check-paths`
parameter. Monitoring from two Availability Zones keeps health reporting for
your instances continuous even if one Availability Zone becomes
unavailable.

The following example creates a check with two health check paths whose
sources are in different Availability Zones, both reaching the same
destination instances.

```
aws ec2 create-application-status-check \
        --protocol https \
        --port 443 \
        --path "/health" \
        --status-code-matcher "200" \
        --health-check-paths '[{"Source":{"SubnetId":"subnet-source-az1","SecurityGroupId":"sg-healthcheck"},"Destinations":[{"SubnetId":"subnet-app-az1","SecurityGroupId":"sg-app"}]},{"Source":{"SubnetId":"subnet-source-az2","SecurityGroupId":"sg-healthcheck"},"Destinations":[{"SubnetId":"subnet-app-az2","SecurityGroupId":"sg-app"}]}]'
```

### Local Zones

For instances running in AWS Local Zones, the managed elastic network
interface (ENI) resides in the parent AWS Region, not in the Local Zone.
Health check traffic between the parent Region and your Local Zone
instances traverses the Local Zone service link, which may incur additional data transfer charges.

## Best practices

- **Design your health endpoint to reflect the health of
  the application running on that instance.** When your endpoint returns health based
  on the application itself, Amazon EC2 Auto Scaling replaces
  only the instances that are genuinely impaired. If the endpoint's response
  also depends on a shared resource such as a database or a downstream
  service, a problem with that resource can fail the check across many
  instances at once. This can trigger a fleet-wide replacement. For guidance on
  writing health check endpoints, see [Implementing health checks](https://aws.amazon.com/builders-library/implementing-health-checks/ "https://aws.amazon.com/builders-library/implementing-health-checks/") in the Amazon Builders' Library.
- **Protect against correlated failures.**
  An included check drives Amazon EC2 Auto Scaling replacement. A check that fails
  across many instances at once can trigger a wave of replacements. Set an
  instance maintenance policy on your Auto Scaling group to limit how
  many instances are replaced at the same time. For more information, see
  [Instance maintenance policy](../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.md") in the Amazon EC2 Auto Scaling User
  Guide.
- **Alarm on the count of impaired instances.**
  Create an Amazon CloudWatch alarm on the
  `StatusCheckFailed_Application` metric across your fleet. A sudden
  rise across many instances indicates a shared dependency rather than
  individual instance faults, and gives you time to respond before
  replacements cascade. For more information, see [Monitor application status checks](#asc-monitoring "#asc-monitoring").
- **Stay within your network interface quota.**
  Application status checks create managed network interfaces that count
  against the _Network interfaces per Region_ quota. AWS
  enforces this quota per Availability Zone. Monitor your usage so a growing
  fleet does not reach the quota. If it does, AWS cannot create new
  interfaces. For related quota alarm guidance, see [Quotas](#asc-quotas "#asc-quotas").
- **Treat status check permissions as
  change-controlled.** The IAM actions that create, modify, delete,
  associate, disassociate, and suppress application status checks can affect
  instance availability. These actions determine what drives Amazon EC2 Auto
  Scaling replacement. Treat actions such as
  `ec2:CreateApplicationStatusCheck`,
  `ec2:AssociateApplicationStatusCheck`,
  `ec2:ModifyApplicationStatusCheck`, and
  `ec2:EnableApplicationStatusCheckSuppression` as
  change-controlled rather than granting them as part of general Amazon EC2 access.
  For the full list of actions, see the Amazon EC2 API Reference.

## Troubleshooting

When an application status check reports impaired but you expect your
application to be healthy, verify each of the following:

1. _Instance reachability._ Confirm that the
   instance's Instance and System status checks are
   `ok`.
2. _Security group inbound rule._ The
   destination instance's security group must allow inbound traffic
   on the check port from the source security group used by the
   application status check. For AWS managed network paths, AWS
   provides the source security group; for customer-managed network
   paths, use the security group you specified as the
   source.
3. _Host firewall._ Any host-level firewall
   (iptables, Windows Firewall, third-party host firewall) on the
   instance must allow inbound traffic on the check port.
4. _Application endpoint._ The application must
   be listening on the port and path you configured. Confirm with a
   local request from the instance
   (`curl http://localhost:PORT/PATH`).
5. _Protocol mismatch._ If the check is
   configured as HTTPS but the endpoint serves HTTP only (or vice
   versa), all calls will fail.
6. _Status code matcher._ Confirm that your
   application's actual response code is included in the status code
   matcher you configured.
7. _Network path._ If you configured
   customer-managed network paths, confirm the source subnet and
   security group have connectivity to the destination subnet. Use
   [VPC Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") to trace the network
   path.
8. _Available ENI quota._ AWS creates a
   managed elastic network interface (ENI) in your account for each
   source subnet and security group combination. Confirm your account
   has not reached its _Network interfaces per Region_
   quota, which is enforced per Availability Zone. If your account has
   reached this quota, AWS cannot create the managed ENI
   and the check cannot run. For more information, see [Amazon VPC quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md").

### Reason codes

The [describe-application-status](../../../cli/latest/reference/ec2/describe-application-status.md "../../../cli/latest/reference/ec2/describe-application-status.md") response includes a reason for
each check. The reason contains the HTTP status code returned by your
application (as a number), along with the protocol used for the check.
A check is marked `passed` if the returned status code is
included in your status code matcher, and `failed`
otherwise.

The reason also includes a reason code and, for HTTP-level results, the
protocol and the returned HTTP status code. The reason contains the
following fields:

`Code`

The reason code for the application status check result. One
of the following values:

- `ResponseCodeMatched`: the HTTP status
  code returned by the health check matched the
  configured `StatusCodeMatcher`.
- `ResponseCodeMismatch`: the HTTP status
  code returned by the health check did not match the
  configured `StatusCodeMatcher`.
- `ConnectionTimeout`: the connection to
  the target timed out.
- `ResponseTimeout`: the health check timed
  out while waiting for a response from the
  target.
- `ConnectionRefused`: the target refused
  the health check connection.
- `ConnectionReset`: the health check
  connection was reset before a response was
  received.

For `ResponseCodeMatched` and
`ResponseCodeMismatch`, the `StatusCode`
field contains the returned HTTP status code and the
`Protocol` field contains the protocol used for the health check. For connection errors, such as `ConnectionTimeout`, `ResponseTimeout`, `ConnectionRefused`, and `ConnectionReset`, the `StatusCode` and `Protocol` fields are not present.

`Protocol`

The protocol used for the health check. One of `HTTP` or `HTTPS`.

`StatusCode`

The HTTP status code returned by the health check.

Use the returned HTTP status code to identify why a check failed. Some
common examples:

| HTTP status code       | Typical meaning                                                                          | Common remediation                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`                  | Application returned a successful<br>response.                                           | None. This is typically a healthy<br>status.                                                                                                                              |
| `301`, `302`           | Application returned a redirect. Health check<br>calls do not follow redirects.          | Point the health check path at the destination<br>of the redirect, or add the redirect code to your<br>status code matcher if you consider it<br>healthy.                 |
| `401`,<br>`403`        | The application requires authentication or<br>denied access to the health check<br>path. | Configure the health check path to be<br>unauthenticated, or serve health checks on a path<br>that does not require credentials.                                          |
| `404`                  | The configured health check path was not found<br>on the application.                    | Confirm the path matches a route your<br>application serves.                                                                                                              |
| `500`                  | Application returned an internal server<br>error.                                        | Investigate application logs on the<br>instance.                                                                                                                          |
| `502`, `503`,<br>`504` | Application is reachable but reports upstream<br>or capacity issues.                     | Investigate application health, dependencies,<br>and capacity. If your application returns these<br>codes during startup, increase<br>`InitializationGracePeriodSeconds`. |

For the complete `ApplicationStatusReason` structure, see
[ApplicationStatusReason](../APIReference/API_ApplicationStatusReason.md "../APIReference/API_ApplicationStatusReason.md") in the
_Amazon EC2 API Reference_.

### Common mistakes

- The security group does not allow inbound traffic from the
  health check source on the check port.
- The application is bound to `127.0.0.1` and not
  listening on the network interface.
- The health check path returns a redirect (301, 302) rather than
  a success response, and the status code matcher does not include
  the redirect code.
- The check is configured for HTTPS but the application only
  serves HTTP, or vice versa.
- The application takes longer to start than the
  `InitializationGracePeriodSeconds` value, and Amazon EC2 Auto Scaling
  replaces the instance before it is ready.

## Monitor application status checks

You can monitor application status checks in three ways:

- **Amazon CloudWatch**. The
  `StatusCheckFailed_Application` metric reflects the
  overall application status for the instance and can drive alarms.
  The metric is aggregated per instance across associated checks
  whose aggregation setting is `included`. CloudWatch also publishes a per-check metric for each associated check, named `StatusCheckFailed_Application_`application-status-check-id``.
- **[describe-instance-status](../../../cli/latest/reference/ec2/describe-instance-status.md "../../../cli/latest/reference/ec2/describe-instance-status.md")**. Returns the
  overall application status alongside your instance's other status
  information.
- **[describe-application-status](../../../cli/latest/reference/ec2/describe-application-status.md "../../../cli/latest/reference/ec2/describe-application-status.md")**. Returns
  detailed per-instance results, including each associated check's
  individual status and the HTTP status code returned by your
  application.

Use the CloudWatch metric for alarm-driven automation. Use
`describe-instance-status` when you already query it for
instance status. Use `describe-application-status` for detailed
per-check visibility.

## Security and permissions

AWS creates and manages the network interfaces used for application status
checks through a service-linked role. No IAM setup is required for the
service to create these ENIs. The service-linked role uses the [`EC2ApplicationStatusChecksServiceRolePolicy`](../../../aws-managed-policy/latest/reference/EC2ApplicationStatusChecksServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/EC2ApplicationStatusChecksServiceRolePolicy.md") AWS
managed policy.

To create, associate, describe, delete, and suppress application status
checks yourself, your IAM user or role needs the corresponding Amazon EC2
permissions. See the _Amazon EC2 API Reference_ for the full list of
actions.

Your instance's security group must allow inbound traffic from the health
check source security group on the port you configured. With AWS managed
network paths, AWS provides the source security group; with customer-managed
network paths, use the security group you specified as the source.

## Pricing

Application status checks are billed on the following components:

- An hourly charge of $0.01 for each managed elastic network interface
  (ENI), per Availability Zone.
- Standard Amazon CloudWatch pricing applies to application status check
  metrics.

## Quotas

Application status checks are subject to AWS service quotas. For the quota
names, default values, and descriptions, see [Amazon
EC2 endpoints and quotas](../../../general/latest/gr/ec2-service.md "../../../general/latest/gr/ec2-service.md") in the _AWS General
Reference_.

In addition to the AWS service quotas that affect the managed network
interfaces, application status checks have the following service quotas. You
can view your usage and request increases from the Service Quotas
console.

In these quotas, a _target_ is a single instance that one
health check monitors. If more than one health check monitors an instance, each
instance and health check pairing counts as a separate target. An
_association_ is a single tag rule or a single instance ID
that you associate with a health check. Each rule or instance ID counts as one
association, regardless of how many instances it resolves to.

| Quota                         | Default | Adjustable         |
| ----------------------------- | ------- | ------------------ |
| Health checks per account     | 50      | Yes, automatically |
| Associations per health check | 50      | Yes, automatically |
| Associations per account      | 200     | Yes, automatically |
| Targets per account           | 5,000   | Yes, by request    |

Most quota increases are approved automatically. An increase to
_Targets per account_ requires a request and manual
approval.

###### Important

If the number of targets in your account exceeds the _Targets
per account_ quota, the targets over the limit are not
monitored and do not report an application status. To avoid gaps in
monitoring, keep your target count within the quota or request an
increase.

We recommend that you create a Amazon CloudWatch alarm on your application status
checks quota usage so that you are notified before you reach a quota. Service
Quotas publishes usage metrics to the `AWS/Usage` namespace in
CloudWatch, which you can use to create the alarm.
