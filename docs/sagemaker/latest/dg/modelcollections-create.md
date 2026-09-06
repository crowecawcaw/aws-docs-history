

# Create a Collection
<a name="modelcollections-create"></a>

**Important**  
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).  
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

You can create a Collection in the Amazon SageMaker Studio console. To create a Collection, complete the following steps based on whether you use Studio or Studio Classic.

------
#### [ Studio ]

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models**.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Collections**.

1. (Optional) To create a Collection inside another Collection, navigate to the hierarchy where you want to add your Collection. Otherwise, your Collection is created at the root level.

1. In the **Actions** dropdown menu in the top right, choose **Create new collection**.

1. Enter a name for your Collection in the **Name** field of the dialog box.
**Note**  
If you plan to create multiple hierarchies in this Collection, keep your Collection names short. The absolute path, which is a string representing the location of your Collections from the root level, must be 256 characters or less. For additional details, see [Collection and Model Group tagging](modelcollections-limitations.md#modelcollections-tagging).

1. (Optional) To add Model Groups to your Collection, complete the following steps:

   1. Choose **Select model groups**.

   1. Select the Model Groups that you want to add. You can select up to 10.

1. Choose **Create**.

1. Check to make sure your Collection was created in the current hierarchy. If you do not immediately see your new Collection, choose **Refresh**.

------
#### [ Studio Classic ]

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. Choose the **Collections** tab.

1. (Optional) To create a Collection inside another Collection, navigate to the hierarchy where you want to add your Collection. Otherwise, your Collection is created at the root level.

1. In the **Actions** dropdown menu in the top right, choose **Create new collection**.

1. Enter a name for your Collection in the **Name** field of the dialog box.
**Note**  
If you plan to create multiple hierarchies in this Collection, keep your Collection names short. The absolute path, which is a string representing the location of your Collections from the root level, must be 256 characters or less. For additional details, see [Collection and Model Group tagging](modelcollections-limitations.md#modelcollections-tagging).

1. (Optional) To add Model Groups to your Collection, complete the following steps:

   1. Choose **Select model groups**.

   1. Select the Model Groups that you want to add. You can select up to 10.

1. Choose **Create**.

1. Check to make sure your Collection was created in the current hierarchy. If you do not immediately see your new Collection, choose **Refresh**.

------