On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Viewing your ingestion history

To view your ingestion history:

1. Go to the main page for your dataset. (Amazon Lookout for Equipment -> Projects -> [asset name] -> Dataset
2. Select the **Ingestion history** tab.
   For each ingestion job that succeeded, you may also view the associated logs in Amazon CloudWatch. The log group for your Lookout for Equipment logs will be `/aws/lookoutequipment/ingestion`. The logstream name will be the ingestion job ID.

For more information, see [Publishing information about ingestion validation to Amazon CloudWatch Logs](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-publish-to-CW "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-publish-to-CW").
