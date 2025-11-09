# Share a model with another account

After you [fulfill the prerequisites](share-model-prereq.md "share-model-prereq.md"), you can share a model. Choose the tab for your preferred method, and then follow the steps:

Console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. Select the button next to the model that you want to share. Then, choose the three dots (

![Vertical ellipsis icon representing a menu or more options.](images/icons/vertical-ellipsis.png)

) and select **Share**. 4. In the **Model sharing details** section, do the following:

    1. In the **Name for shared model** field, give the shared model a name.
    2. In the **Recipient account ID** field, specify the ID of the account that will receive the model.
    3. (Optional) To add tags, expand the **Tags** section. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").

5. Choose **Share model**. After the recipient accepts the model in [Resource Access Manager](../../../ram/latest/userguide/getting-started-shared.md "../../../ram/latest/userguide/getting-started-shared.md"), the model appears in their list of custom models.

API
To share a model, send a [CreateResourceShare](../../../ram/latest/APIReference/API_CreateResourceShare.md "../../../ram/latest/APIReference/API_CreateResourceShare.md") request with an [AWS Resource Access Manager endpoint](../../../general/latest/gr/ram.md "../../../general/latest/gr/ram.md"). Minimally, provide the following fields:

| Field        | Use case                                           |
| ------------ | -------------------------------------------------- |
| Name         | To provide a name for the resource share.          |
| resourceArns | To specify the ARNs of each model to share.        |
| principals   | To specify the principals to share the model with. |

The [CreateResourceShare](../../../ram/latest/APIReference/API_CreateResourceShare.md "../../../ram/latest/APIReference/API_CreateResourceShare.md") response returns a `resourceShareArn` that you can use to manage the resource share.

The account receiving a model can check whether a model has been shared by sending a [ListCustomModels](../APIReference/API_ListCustomModels.md "../APIReference/API_ListCustomModels.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). Models that have been shared will show up with a `shared` status of `true`.

After sharing the model, the recipient of the model must copy it into a Region in order to use it. For more information, see [Copy a customized or shared model to use in a Region](copy-model.md "copy-model.md").
