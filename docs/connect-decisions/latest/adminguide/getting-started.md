

# Getting Started
<a name="getting-started"></a>

In this section, you can learn to create an Amazon Connect Decisions instance, grant user permission roles, and log into the Amazon Connect Decisions web application.

## Prerequisites to use Amazon Connect Decisions
<a name="getting-started-prerequisites"></a>

Before you create an Amazon Connect Decisions instance, make sure that you complete the following steps:
+ You have an AWS account. To create an AWS account, see [Setting up an AWS account](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/setting-up-an-aws-account.html).
+ Make sure IAM Identity Center is enabled. To enable IAM Identity Center, see [Enabling IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html).
+ An IAM Identity Center instance must be activated in the same region where you want to create your Amazon Connect Decisions instance. Amazon Connect Decisions is only supported in US East (N. Virginia) and Europe (Ireland) Region.
+ If the Amazon Connect Decisions instance is not in the same region as your existing IAM Identity Center region, [contact us](https://aws.amazon.com/contact-us/) for further assistance.
+ You must have at least one user in the IAM Identity Center instance to assign as the Amazon Connect Decisions administrator. You can connect your active directory to IAM Identity Center. For more information, see [Connect to a Microsoft AD directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html).
+ Add any additional users who need access to Amazon Connect Decisions to IAM Identity Center.
+ You need AWS Key Management Service (AWS KMS) to create an instance. Amazon Connect Decisions uses this AWS KMS key to encrypt all the data that comes into Amazon Connect Decisions. For information about AWS KMS Keys, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).
+ If you intend to enable the actions feature, you will need to configure a connection to the system you use to maintain the relevant data, and provide credentials for Amazon Connect Decisions to use. Please [contact us](https://aws.amazon.com/contact-us/) for further assistance.

## Browsers supported by Amazon Connect Decisions
<a name="getting-started-supported-browsers"></a>

Before you work with Amazon Connect Decisions, verify that your browser is supported using the following table.


| Browser | Supported Versions | 
| --- | --- | 
| Google Chrome | Latest three versions. | 
| Mozilla Firefox ESR | Versions are supported until their Firefox [end-of-life date](https://support.mozilla.org/en-US/kb/firefox-esr-release-cycle). For details, see the [Firefox ESR release calendar](https://wiki.mozilla.org/Release_Management/Calendar). | 
| Mozilla Firefox | Latest three versions. | 
| Microsoft Edge and Edge Chromium | Version 84 and later. | 
| Safari | Safari 10 or later on macOS. | 

## Languages supported by Amazon Connect Decisions
<a name="getting-started-supported-languages"></a>

Amazon Connect Decisions supports the following languages:
+ English (US)