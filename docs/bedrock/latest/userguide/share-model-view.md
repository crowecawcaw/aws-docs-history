# View information about shared models

To learn how to view information about models that you've shared with other accounts or models that have been shared with you, choose the tab for your preferred method, and then follow the steps:

Console

###### To view models that you've shared with other accounts

1. Sign in to the AWS Management Console and open the AWS RAM console at [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. Follow the steps at [Viewing resource shares you created in AWS Resource Access Manager](../../../ram/latest/userguide/working-with-sharing-view-rs.md "../../../ram/latest/userguide/working-with-sharing-view-rs.md").

###### To view models shared with you by other accounts

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. Models that have been shared with you by other accounts will be shown in the following ways, depending on whether you've [copied them to a Region](copy-model.md "copy-model.md"):
   1. Shared models that you haven't copied to a Region yet are listed in the **Models shared with you** section.
   2. Shared models that have been copied to the current Region are listed in the **Models** section with a **Share status** of `Shared`.

API
To view information about models that you've shared, send a [GetResourceShares](../../../ram/latest/APIReference/API_GetResourceShares.md "../../../ram/latest/APIReference/API_GetResourceShares.md") request with an [AWS Resource Access Manager endpoint](../../../general/latest/gr/ram.md "../../../general/latest/gr/ram.md") and specify `SELF` in the `resourceOwner` field. You can use the optional fields to filter for specific models or resource shares.

To view information about models that have been shared with you, send a [ListCustomModels](../APIReference/API_ListCustomModels.md "../APIReference/API_ListCustomModels.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") and specify `false` with the `isOwned` filter.
