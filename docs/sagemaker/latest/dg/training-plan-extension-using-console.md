

# Extend a training plan using the SageMaker AI console
<a name="training-plan-extension-using-console"></a>

SageMaker training plans offer a convenient way to extend your existing training plans through the SageMaker AI console UI. This guide walks you through the process of extending a training plan for SageMaker training jobs and SageMaker HyperPod clusters using the SageMaker AI console.

To extend a training plan using the console:

1. Navigate to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Choose **Training Plans** in the left navigation pane.

1. Select the training plan you want to extend from the list.

1. Choose the **Extend** button.

1. Enter the desired end date for your extension and choose **Search** to find available extension offerings.

1. Review the list of extension offerings, which includes details such as duration, availability zone, upfront fee, and start and end times.

1. Select the extension offering that best meets your requirements.

1. Review the extension details in the confirmation dialog, then choose **Submit** to confirm your purchase.

After the extension is purchased, the training plan's end date is updated to reflect the new extended duration.

## View extension history
<a name="training-plan-extension-history-console"></a>

To view the extension history for a training plan:

1. Navigate to the **Training Plans** page in the SageMaker AI console.

1. Select the training plan you want to view.

1. In the training plan details page, view the **Extensions** section to see all past extensions, including extension offering ID, start and end dates, status, and when the extension was created.

## Extension status values
<a name="training-plan-extension-status-values-console"></a>

Extensions can have the following status values:
+ `Pending`: The extension has been requested and is awaiting payment processing.
+ `Active`: The extension has been successfully purchased and is active.
+ `Scheduled`: The extension is scheduled to start at a future time.
+ `Failed`: The extension purchase failed (for example, due to payment issues).
+ `Expired`: The extension period has ended.