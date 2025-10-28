# Perform scaling updates

Scaling updates adjust the capacity of your compute environment by adding or removing
instances. This is the fastest update strategy and doesn't require replacing existing instances.
Scaling updates work with any service role type and allocation strategy, making them the most
flexible update option.

## Changes that trigger a scaling update

When you modify only the following settings,
AWS Batch performs a scaling update. If you modify any of these settings along with other
compute environment settings, AWS Batch performs an [infrastructure update](infrastructure-updates.md#infrastructure-updates.title "infrastructure-updates.md#infrastructure-updates.title")
instead.

The following settings trigger scaling updates when modified exclusively:

- `desiredvCpus` – Sets the target number of vCPUs for the
  environment.
- `maxvCpus` – Defines the maximum number of vCPUs that can be
  launched.
- `minvCpus` – Specifies the minimum number of vCPUs to maintain.

For Fargate compute environments, you can also modify these settings for scaling updates:

- `securityGroupIds` – Security group IDs for the compute environment.
- `subnets` – Subnets for the compute environment.

###### Note

We recommend not using `desiredvCpus` to initiate a scaling update as AWS Batch will dynamically adjust `desiredvCpus`. Instead you should update `minvCpus`.

When updating `desiredvCpus`, the value must be between
`minvCpus` and `maxvCpus`. The new value must be greater than or
equal to the current `desiredvCpus`. For more information, see [Error message when you update the
desiredvCpus setting](error-desired-vcpus-update.md "error-desired-vcpus-update.md").

###### Important

If you modify any of these scaling settings together with other compute environment settings (such as instance types, AMI IDs, or launch templates), AWS Batch performs an infrastructure update instead of a scaling update. Infrastructure updates take longer and may replace existing instances.

Performing scaling updates using the AWS Management Console

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. In the navigation pane, choose **Environments** and then the
   **Compute environments** tab.
3. Select the compute environment to update.
4. Choose **Actions** and then **Edit**.
5. Modify one or more of the [settings that
   support scaling updates](#scaling-updates-triggers "#scaling-updates-triggers"). For example:
   - For **Minimum vCPUs**, enter the minimum number of
     vCPUs.
   - For **Desired vCPUs**, enter the desired number of
     vCPUs.
   - For **Maximum vCPUs**, enter the maximum number of
     vCPUs.

6. Choose **Save changes**.
7. Monitor the compute environment status. The update should complete quickly since
   it only involves scaling operations.

Performing scaling updates using the AWS CLI
Use the **update-compute-environment** command to perform scaling
updates. The following two examples demonstrate common scaling operations. You can modify
one or more of the following [settings that
support scaling updates](#scaling-updates-triggers "#scaling-updates-triggers")

- This example updates the desired, minimum, and maximum vCPUs:

```
aws batch update-compute-environment \
    --compute-environment `your-compute-environment-name` \
    --compute-resources minvCpus=`2`,maxvCpus=`8`
```

## Monitoring scaling updates

Monitor your scaling updates using the AWS Batch console to view the compute environment
status and check instance count and vCPU metrics. You can also use the AWS CLI with the
**describe-compute-environments** command to check status and monitor
instance counts and vCPU values.
