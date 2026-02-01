Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing Amazon Redshift Advisor recommendations

You can access Amazon Redshift Advisor recommendations using the Amazon Redshift console, Amazon Redshift API, or AWS CLI.
To access recommendations you must have permission `redshift:ListRecommendations` attached to your IAM role or identity.

## Viewing Amazon Redshift Advisor recommendations on the Amazon Redshift provisioned console

You can view Amazon Redshift Advisor recommendations on the AWS Management Console.

###### To view Amazon Redshift Advisor recommendations for Amazon Redshift clusters on the console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Advisor**.
3. Expand each recommendation to see more details.
   On this page, you can sort and group recommendations.

## Viewing Amazon Redshift Advisor recommendations using Amazon Redshift API operations

You can list Amazon Redshift Advisor recommendations for Amazon Redshift clusters using the Amazon Redshift API.
Typically, you develop and application in your programming language of your choice to call the `redshift:ListRecommendations` API using an AWS SDK.
For more information, see
[ListRecommendations](../APIReference/API_ListRecommendations.md "../APIReference/API_ListRecommendations.md") in the _Amazon Redshift API Reference_.

## Viewing Amazon Redshift Advisor recommendations using AWS Command Line Interface operations

You can list Amazon Redshift Advisor recommendations for Amazon Redshift clusters using the AWS Command Line Interface.
For more information, see
[list-recommendations](../../../cli/latest/reference/redshift/list-recommendations.md "../../../cli/latest/reference/redshift/list-recommendations.md") in the _AWS CLI Command Reference_.
