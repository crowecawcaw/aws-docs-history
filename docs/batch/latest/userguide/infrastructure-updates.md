# Perform infrastructure updates

Infrastructure updates replace the instances in your compute environment with new instances
that have updated settings. This update strategy takes longer than scaling updates and requires
specific service role and allocation strategy settings. Infrastructure updates provide a way to
modify fundamental compute environment configurations while maintaining service
availability.

###### Important

Infrastructure updates require the _AWSServiceRoleForBatch_
service-linked role and an allocation strategy of `BEST_FIT_PROGRESSIVE`,
`SPOT_CAPACITY_OPTIMIZED`, or `SPOT_PRICE_CAPACITY_OPTIMIZED`. If your
environment doesn't meet these requirements, use blue/green updates instead.

## Changes that trigger infrastructure

updates

When you modify any of the following settings, AWS Batch performs an infrastructure update.
Infrastructure updates also occur when you modify these settings together with scaling update
settings.

The following settings trigger infrastructure updates:

**Compute configuration**

- `allocationStrategy` – Determines how AWS Batch selects instance
  types.
- `instanceTypes` – Specifies which EC2 instance types to use.
- `bidPercentage` – Maximum percentage of On-Demand price for Spot
  instances.
- `type` – Compute environment type (`EC2` or
  `SPOT`).

**AMI and launch configuration**

- `imageId` – Specific AMI to use for instances.
- `ec2Configuration` – EC2 configuration including
  `imageIdOverride`.
- `launchTemplate` – EC2 launch template settings.
- `ec2KeyPair` – SSH key pair for instance access.
- `updateToLatestImageVersion` – Automatic AMI updates setting.

**Networking and security**

- `subnets` – VPC subnets where instances are launched (for EC2 compute
  environments).
- `securityGroupIds` – Security groups for instances (for EC2 compute
  environments).
- `placementGroup` – EC2 placement group configuration.

**Other settings**

- `instanceRole` – IAM role for EC2 instances.
- `tags` – Tags applied to EC2 instances.

###### Important

If you modify any infrastructure update settings together with scaling update settings
(such as `desiredvCpus`, `maxvCpus`, or `minvCpus`),
AWS Batch performs an infrastructure update. Infrastructure updates take longer than scaling
updates.

## AMI selection during infrastructure updates

During an infrastructure update, the compute environment's AMI ID might change, depending on
whether AMIs are specified in any of these three settings. AMIs are specified in the
`imageId` (in `computeResources`), `imageIdOverride` (in
`ec2Configuration`), or the launch template specified in `launchTemplate`.
Suppose that no AMI IDs are specified in any of those settings and the
`updateToLatestImageVersion` setting is `true`. Then, the latest Amazon ECS
optimized AMI supported by AWS Batch is used for any infrastructure update.

If an AMI ID is specified in at least one of these settings, the update depends on which
setting provided the AMI ID used before the update. When you create a compute environment, the
priority for selecting an AMI ID is first the launch template, then the `imageId`
setting, and finally the `imageIdOverride` setting. However, if the AMI ID that's
used came from the launch template, updating either the `imageId` or
`imageIdOverride` settings doesn't update the AMI ID. The only way to update an
AMI ID selected from the launch template is to update the launch template. If the version
parameter of the launch template is `$Default` or `$Latest`, the default
or latest version of the specified launch template is evaluated. If a different AMI ID is
selected by the default or the latest version of the launch template is selected, that AMI
ID is used in the update.

If the launch template was not used to select the AMI ID, the AMI ID that's specified in the
`imageId` or `imageIdOverride` parameters is used. If both are specified,
the AMI ID specified in the `imageIdOverride` parameter is used.

Suppose that the compute environment uses an AMI ID specified by the `imageId`,
`imageIdOverride`, or `launchTemplate` parameters, and you want to use the
latest Amazon ECS optimized AMI supported by AWS Batch. Then, the update must remove the settings that
provided AMI IDs. For `imageId`, this requires specifying an empty string for that
parameter. For `imageIdOverride`, this requires specifying an empty string for the
`ec2Configuration` parameter.

If the AMI ID came from the launch template, you can change to the latest Amazon ECS optimized
AMI that's supported by AWS Batch by either one of the following ways:

- Remove the launch template by specifying an empty string for the
  `launchTemplateId` or `launchTemplateName` parameter. This removes the
  entire launch template, rather than the AMI ID alone.
- If the updated version of the launch template doesn't specify an AMI ID, the
  `updateToLatestImageVersion` parameter must be set to `true`.

## Job handling during updates

Configure how running jobs are handled during an infrastructure update using the update
policy. When you set `terminateJobsOnUpdate=true`, running jobs are terminated
immediately, the `jobExecutionTimeoutMinutes` setting is ignored, and the update
proceeds as soon as instances can be replaced. When you set
`terminateJobsOnUpdate=false`, running jobs continue for the specified timeout
period with a default timeout of 30 minutes, and jobs are terminated if they exceed the
timeout.

###### Note

To retry jobs that are terminated during an update, configure a job retry strategy. For
more information, see [Automated job retries](job_retries.md "job_retries.md").

Performing infrastructure updates using the AWS Management Console

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. In the navigation pane, choose **Environments** then the
   **Compute environments** tab.
3. Select the compute environment to update.
4. Choose **Actions** and then **Edit**.
5. In the **Update behavior** section, configure how running jobs
   are handled:
   - Choose **Update AMI to latest version** to update the AMI to
     the latest version.
   - Choose **Terminate jobs immediately on update** to terminate
     jobs when the update process is run.
   - For **Job execution timeout** enter the number of minutes to
     wait before starting the update process.

6. Modify one or more of the [settings
   that require an infrastructure updates](#infrastructure-updates-triggers "#infrastructure-updates-triggers"). For example:
   - **Instance role**
   - **Use EC2 Spot instances**
   - **Allowed instance types**
   - **Placement group**
   - **EC2 key pair**
   - **EC2 configuration**
   - **Launch templates**
   - **Subnets**
   - **Security groups**

7. Choose **Save changes**.
8. Monitor the compute environment status. The environment will show
   `UPDATING` during the update process.

Performing infrastructure updates using the AWS CLI
Use the **update-compute-environment** command with an change to one or
more of the [settings that require an
infrastructure updates](#infrastructure-updates-triggers "#infrastructure-updates-triggers"). The following three examples are common infrastructure
operations.

- This example updates the instance types and configures the update policy:

```
aws batch update-compute-environment \
    --compute-environment `your-compute-environment-name` \
    --compute-resources instanceTypes=`default_x86_64` \
    --update-policy terminateJobsOnUpdate=`false`,jobExecutionTimeoutMinutes=`30`
```

- This example updates the VPC subnets and security groups:

```
aws batch update-compute-environment \
    --compute-environment `your-compute-environment-name` \
    --compute-resources subnets=`subnet-abcd1234`,`subnet-efgh5678` securityGroupIds=`sg-abcd1234` \
    --update-policy terminateJobsOnUpdate=`true`
```

- This example enables automatic updates to the latest Amazon ECS optimized AMI:

```
aws batch update-compute-environment \
    --compute-environment `your-compute-environment-name` \
    --compute-resources updateToLatestImageVersion=`true` \
    --update-policy terminateJobsOnUpdate=`false`,jobExecutionTimeoutMinutes=`60`
```

## Monitoring infrastructure updates

Monitor your infrastructure updates using the AWS Batch console to watch the compute
environment status change to `UPDATING`, monitor instance replacement progress, and
check for any failed updates. The update is successful once the compute environment state is
`VAILD`. You can also use CloudWatch to track instance termination events and monitor
job states during the update. With the AWS CLI, use the
**describe-compute-environments** command to check status and monitor
instance lifecycle events.
