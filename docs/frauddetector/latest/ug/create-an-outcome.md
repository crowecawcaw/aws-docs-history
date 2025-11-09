Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create an outcome

You can create outcomes in the Amazon Fraud Detector console, using the [put-outcome](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-outcome.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-outcome.html") command,
using the [PutOutcome](../api/API_PutOutcome.md "../api/API_PutOutcome.md") API, or using the AWS SDK for Python (Boto3).

## Create an outcome using the Amazon Fraud Detector console

###### To create one or more outcomes,

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose **Outcomes**.
3. In the **Outcomes** page, choose **Create**.
4. In your **New outcome** page, enter the following:
   1. In the **Outcome name**, enter a name for your outcome.
   2. In the **Outcome description**, optionally, enter a description.

5. Choose **Save outcome**.
6. Repeat steps 2 to 5 for creating additional outcomes.

## Create an outcome using the AWS SDK for Python (Boto3)

The following example uses the `PutOutcome` API to create three outcomes. They are `verify_customer`, `review`, and `approve`.
After the outcomes are created, you can assign them to rules.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_outcome(
name = 'verify_customer',
description = 'this outcome initiates a verification workflow'
)

fraudDetector.put_outcome(
name = 'review',
description = 'this outcome sidelines event for review'
)

fraudDetector.put_outcome(
name = 'approve',
description = 'this outcome approves the event'
)

```
