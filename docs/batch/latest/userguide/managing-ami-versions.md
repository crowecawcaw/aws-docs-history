

# Managing AMI versions in compute environments
<a name="managing-ami-versions"></a>

AWS Batch provides visibility into the Amazon Machine Images (AMIs) that your compute environments use.

## Viewing AMI status
<a name="viewing-ami-status"></a>

You can view the status of AMIs used in your compute environments through the AWS Batch console or by using [describe-compute-environments](https://docs.aws.amazon.com/cli/latest/reference/batch/describe-compute-environments.html) command.

------
#### [ Console ]

In the AWS Batch console, AMI status information appears in two locations with the following status values:
+ **Latest** – Using the most recent AMI supported by AWS Batch.
+ **Update available** – An update is available.

**Note**  
AMI status information appears only for AWS Batch-managed AMIs. The status does not appear when images are specified in `imageId` (deprecated), `imageIdOverride`, or in the default launch template. The status does not appear when the compute environment has a launch template override. For more information on AMI selection, see [AMI selection order](ami-selection-order.md).

The compute environments page displays a **Batch image status** column that shows the overall `batchImageStatus` for each compute environment. If a compute environment has multiple AMIs and any one AMI has **Update available**, the console shows **Update available** for the entire compute environment.

**Note**  
The status appears after the compute environment has started scaling for any **Image type**.

On the compute environment detail page, the **Ec2 configuration** section of the **Compute resources** tab shows the **Batch image status** for each **Image type** in the compute environment. If an **Image type** has multiple AMIs and any one AMI has **Update available**, the console shows **Update available** for that **Image type**.

**Note**  
The status appears for each **Image type** only after the compute environment has begun scaling instances for that specific **Image type**.

------
#### [ CLI ]

When you call [describe-compute-environments](https://docs.aws.amazon.com/cli/latest/reference/batch/describe-compute-environments.html), the response includes the `batchImageStatus` field that provides AMI visibility with the following values:
+ `LATEST` – Using the most recent AMI supported by AWS Batch.
+ `UPDATE_AVAILABLE` – An update is available.

**Note**  
The `batchImageStatus` field appears only for AWS Batch-managed AMIs. It does not appear when custom AMIs are specified in `imageId` (deprecated), `imageIdOverride`, or in the default launch template. The status does not appear when the compute environment has a launch template override. For more information about how AWS Batch selects AMIs, see [AMI selection order](ami-selection-order.md).  
The field appears independently for each `Ec2Configuration` and only after the compute environment has begun scaling instances using that `imageType`.

```
{
    "computeEnvironments": [
        {
            "computeEnvironmentName": "my-compute-environment",
            "computeResources": {
                "ec2Configuration": [
                    {
                        "imageType": "ECS_AL2023"
                    },
                    {
                        "imageType": "ECS_AL2023_NVIDIA",
                        "batchImageStatus": "UPDATE_AVAILABLE"
                    }
                ]
            }
        }
    ]
}
```

------

## Updating AMI versions
<a name="updating-ami-versions"></a>

When AWS Batch indicates that an AMI update is available, you can update your compute environment to use the newer AMIs by updating the compute environment with **Update AMI to latest version** set to true.

You don't need to specify new AMI IDs – AWS Batch automatically selects the latest supported AMIs when you set **Update AMI to latest version**.

**Important**  
Updating AMIs triggers an [infrastructure update](infrastructure-updates.md), not a scaling update. This means AWS Batch replaces existing instances with new instances that use the updated AMI. The update process takes longer than a scaling update and may interrupt running jobs depending on your update policy configuration.

**Important**  
If your allocation strategy is `BEST_FIT` then you have to perform a [blue/green update](blue-green-updates.md).

------
#### [ Console ]

To update AMIs using the AWS Batch console:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane, choose **Environments**.

1. Select the option next to the compute environment that shows an AMI status with an update. You must select a compute environment before the **Actions** menu options become available.

1. Choose **Update now** (by the AMI status) or **Actions** > **Edit** to open the update modal.

1. In the AMI update modal, review the current AMI versions and their statuses.

1. Choose **Confirm** or **Save** to begin the infrastructure update.

The compute environment status changes to `UPDATING` during the infrastructure update. You can monitor the progress in the console.

------
#### [ CLI ]

To update AMIs using the AWS CLI, use the `update-compute-environment` command.

```
aws batch update-compute-environment \
    --compute-environment my-compute-environment \
    --compute-resources updateToLatestImageVersion=true
```

This command triggers an infrastructure update that replaces instances with new instances using the latest AWS Batch-supported AMIs.

------

## Custom AMI considerations
<a name="custom-ami-considerations"></a>

If your compute environment uses custom AMIs, i.e. AMIs specified in `ComputeResources.imageId` (deprecated), `Ec2Configuration.imageIdOverride`, the default launch template or the launch template overrides, AWS Batch cannot provide status information for these AMIs.
+ **Status visibility** – Custom AMIs show "**-**" for their **Batch image status** in the console and do not include the `batchImageStatus` field in API responses.
+ **Manual management** – You are responsible for maintaining and updating custom AMIs. Stay informed of security and software patches from your AMI provider and update your custom AMIs accordingly.
+ **EC2 management** – Use the Amazon EC2 console or APIs to manage custom AMI lifecycle, including creating new versions and deprecating old ones.

For more information about managing custom AMIs, see [Compute resource AMIs](compute_resource_AMIs.md).

## Best practices for AMI updates
<a name="ami-update-best-practices"></a>

This section applies to both custom and default AMIs.
+ **Regular monitoring** – Regularly check the AMI status of your compute environments to identify when updates are available. For default AMIs, the `batchImageStatus` will show when an update is available. For custom AMIs, you'll need to use other resources like AWS security bulletins.
+ **Maintenance windows** – Schedule AMI updates during maintenance windows when job interruption is acceptable, as infrastructure updates replace existing instances.
+ **Job retry strategy** – Configure job retry strategies to handle jobs that may be interrupted during infrastructure updates. For more information, see [Automated job retries](job_retries.md).
+ **Update policy configuration** – Configure appropriate update policies to control how running jobs are handled during infrastructure updates. For more information, see [Perform infrastructure updates](infrastructure-updates.md).
+ **Testing** – Test AMI updates in development environments before applying them to production compute environments.