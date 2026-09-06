

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Viewing Amazon Redshift Advisor recommendations
<a name="access-advisor"></a>

You can access Amazon Redshift Advisor recommendations using the Amazon Redshift console, Amazon Redshift API, or AWS CLI. To access recommendations you must have permission `redshift:ListRecommendations` attached to your IAM role or identity.

## Viewing Amazon Redshift Advisor recommendations on the Amazon Redshift provisioned console
<a name="access-advisor-console"></a>

You can view Amazon Redshift Advisor recommendations on the AWS Management Console. 

**To view Amazon Redshift Advisor recommendations for Amazon Redshift clusters on the console**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Advisor**.

1. Expand each recommendation to see more details. On this page, you can sort and group recommendations. 

## Viewing Amazon Redshift Advisor recommendations using Amazon Redshift API operations
<a name="access-advisor-api"></a>

You can list Amazon Redshift Advisor recommendations for Amazon Redshift clusters using the Amazon Redshift API. Typically, you develop and application in your programming language of your choice to call the `redshift:ListRecommendations` API using an AWS SDK. For more information, see [ListRecommendations](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ListRecommendations.html) in the *Amazon Redshift API Reference*.

## Viewing Amazon Redshift Advisor recommendations using AWS Command Line Interface operations
<a name="access-advisor-cli"></a>

You can list Amazon Redshift Advisor recommendations for Amazon Redshift clusters using the AWS Command Line Interface. For more information, see [list-recommendations](https://docs.aws.amazon.com/cli/latest/reference/redshift/list-recommendations.html) in the *AWS CLI Command Reference*.