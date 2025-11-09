# Delete a Provisioned Throughput or cancel auto renew

Your Provisioned Throughput will automatically renew at the end of each commitment term, maintaining your current input and output tokens configurations.

If you don't want to keep your Provisioned Throughput, you can delete it or, for Provisioned Throughput by Tokens, cancel auto renew to prevent it renewing when the current term ends.

## Deleting a Provisioned Throughput

When you delete a Provisioned Throughput, you'll no longer be able to invoke the model at the throughput level that you purchased it for. If you delete a Provisioned Throughput associated with a custom model,
the custom model isn't deleted. To learn how to delete a custom model, see [Delete a custom model](model-customization-delete.md "model-customization-delete.md").

###### Note

You can't delete a Provisioned Throughput by Model Units with commitment before the commitment term is complete.

To learn how to delete a Provisioned Throughput, choose the tab for your preferred method, and then follow the steps:

Console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Provisioned Throughput** from the left navigation pane.
3. From the **Provisioned Throughput** section, select a Provisioned Throughput.
4. Choose **Delete** from the **Actions** dropdown menu.
5. The console displays a modal form to warn you that deletion is permanent. Choose
   **Confirm** to proceed.
6. The Provisioned Throughput is immediately deleted.

API
To delete a Provisioned Throughput, send a [DeleteProvisionedModelThroughput](../APIReference/API_DeleteProvisionedModelThroughput.md "../APIReference/API_DeleteProvisionedModelThroughput.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). Specify either the name of the Provisioned Throughput or its ARN as the `provisionedModelId`. If deletion is successful, the response returns an HTTP 200 status code.

[See code examples](prov-thru-code-examples.md "prov-thru-code-examples.md")

## Canceling auto renew for a Provisioned Throughput

For Provisioned Throughput by Tokens, you can cancel auto renew at any point before your commitment term ends to prevent a Provisioned Throughput from automatically renewing.

If you cancel auto renew, your Provisioned Throughput will remain in service until the end of your commitment term. You will still be charged the full provision fee for your current term, whether you
run inference or not.

After you cancel auto renew for a Provisioned Throughput, you can't make any further modifications to your Provisioned Throughput for the remainder of the commitment term.

###### Note

Auto renew cannot be re-enabled once cancelled. If you need Provisioned Throughput after your current term expires, you will need to purchase a new Provisioned Throughput.

To learn how to cancel auto renew for a Provisioned Throughput by Tokens, choose the tab for your preferred method, and then follow the steps:

Console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Provisioned Throughput** from the left navigation pane.
3. From the **Provisioned Throughput** section, select a Provisioned Throughput.
4. Choose **Cancel auto renew** from the **Actions** dropdown menu.
5. The console displays a modal form to warn you that this action cannot be undone. Choose
   **Confirm** to proceed.
6. The Provisioned Throughput will remain active until the end of the current commitment term, after which it will be automatically deleted.

API
To cancel auto renew for a Provisioned Throughput, send an [UpdateProvisionedModelThroughput](../APIReference/API_UpdateProvisionedModelThroughput.md "../APIReference/API_UpdateProvisionedModelThroughput.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") with the `disableAutoRenew` parameter set to `true`. The Provisioned Throughput will remain active until the end of the current commitment term.

[See code examples](prov-thru-code-examples.md "prov-thru-code-examples.md")
