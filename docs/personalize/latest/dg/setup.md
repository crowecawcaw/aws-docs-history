# Setting up Amazon Personalize

Before using Amazon Personalize, you must have an Amazon Web Services (AWS) account with an administrative user. After you set up the required permissions, you can access Amazon Personalize
through the Amazon Personalize console, the AWS Command Line Interface (AWS CLI), or the AWS SDKs.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Regions and endpoints](#endpoints "#endpoints")
- [Setting up permissions](aws-personalize-set-up-permissions.md "aws-personalize-set-up-permissions.md")
- [Setting up the AWS CLI](aws-personalize-set-up-aws-cli.md "aws-personalize-set-up-aws-cli.md")
- [Setting up the AWS SDKs](aws-personalize-set-up-sdks.md "aws-personalize-set-up-sdks.md")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Regions and endpoints

An endpoint is a URL that is the entry point for a web service. Each endpoint is associated with a specific AWS
region. Pay attention to the default regions of the Amazon Personalize console, the AWS CLI, and the Amazon Personalize SDKs, as all Amazon Personalize components
of a given campaign (dataset, solution, campaign, event tracker) must be created in the same region. For the regions and
endpoints supported by Amazon Personalize, see [Regions and endpoints](../../../general/latest/gr/rande.md#personalize_region "../../../general/latest/gr/rande.md#personalize_region").
