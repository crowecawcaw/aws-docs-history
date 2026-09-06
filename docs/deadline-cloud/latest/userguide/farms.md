

# Deadline Cloud farms
<a name="farms"></a>

With a Deadline Cloud farm, you can manage users and project resources. A *farm* is a where your project resources are located. Your farm consists of queues and fleets. A *queue* is where submitted jobs are located and scheduled to be rendered. A * fleet* is a group of worker nodes that run tasks to complete jobs. After you create a farm, you can create queues and fleets to meet your project's needs.

## Create a farm
<a name="create-farm"></a>

1. From the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home), choose **Go to Dashboard**. 

1. In the Farms section of the Deadline Cloud dashboard, choose **Actions** → **Create farm**.

   1.  Alternatively, in the left side panel choose **Farms and other resources**, then choose **Create Farm**.

1. Add a **Name** for your farm.

1. For **Description**, enter the farm description. A clear description can help you quickly identify your farm's purpose.

1. (Optional) By default, your data is encrypted with a key that AWS owns and manages for your security. You can choose **Customize encryption settings (advanced)** to use an existing key or to create a new one that you manage.

   If you choose to customize encryption settings using the checkbox, enter a AWS KMS ARN, or create a new AWS KMS by choosing **Create new KMS key**.

1. (Optional) For **Cost scale factor**, enter a value to adjust how costs are displayed in the usage explorer and budget manager. Values less than 1 represent discounts, values greater than 1 represent premiums, and 1 (the default) leaves costs unchanged. For more information, see [Cost scale factor](manage-costs.md#cost-scale-factor).

1. (Optional) Choose **Add new tag** to add one or more tags to your farm.

1. Choose **Create farm**. After creation, your farm displays.