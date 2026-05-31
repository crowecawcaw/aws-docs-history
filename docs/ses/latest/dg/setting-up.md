# Setting up Amazon Simple Email Service

Before you start using Amazon SES, you must complete the following tasks.

###### Tasks

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Set up your SES account](#quick-start-verify-email-addresses "#quick-start-verify-email-addresses")
- [Download an AWS SDK (For using the SES APIs)](#download-aws-sdk "#download-aws-sdk")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Set up your SES account

Get started with SES by verifying an email address and sending domain so that you can
start sending email through SES and request production access for your account by using
the _SES account set up_ wizard.

###### Using the _SES account set up_ wizard to set up your account

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Select **Get started** from the SES console home page and the
   wizard will walk you through the steps of setting up your SES account.

_The_ SES account set up _wizard will only be presented
if you have not yet created any identities (email address or domain) in SES._

## Download an AWS SDK (For using the SES APIs)

To call the SES APIs without having to handle low-level details like assembling raw
HTTP requests, you can use an AWS SDK. The AWS SDKs provide functions and data types that
encapsulate the functionality of SES and other AWS services. To download an AWS SDK,
go to [SDKs](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk"). After you download the SDK, [create a shared
credentials file](../../../credref/latest/refdocs/creds-config-files.md "../../../credref/latest/refdocs/creds-config-files.md") and specify your AWS access keys.
