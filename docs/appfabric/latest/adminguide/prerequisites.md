# Prerequisites and recommendations to use AWS AppFabric

If you're a new AWS customer, complete the setup prerequisites that are listed on this
page before you start using AWS AppFabric for security. For these setup procedures, you use the
AWS Identity and Access Management (IAM) service. For complete information about IAM, see the
[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [(Required) Complete application prerequisites](#application-prerequisites "#application-prerequisites")
- [(Optional) Create an output location](#create-output-location "#create-output-location")
- [(Optional) Create an AWS KMS key](#create-kms-keys "#create-kms-keys")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## (Required) Complete application prerequisites

To use AppFabric for security to receive user information and audit logs from applications,
many applications require that you have specific role and plan types. Ensure that you
have reviewed the prerequisites for each application that you want to authorize with
AppFabric for security, and that you have the proper plans and roles. For more information about
the application-specific prerequisites, see [Supported Applications](supported-applications.md "supported-applications.md"), or choose one of the following application-specific
topics.

- [Configure 1Password for AppFabric](1password.md "1password.md")
- [Configure Asana for AppFabric](asana.md "asana.md")
- [Configure Azure Monitor for AppFabric](azure-monitor.md "azure-monitor.md")
- [Configure Atlassian Confluence for AppFabric](confluence.md "confluence.md")
- [Configure Atlassian Jira suite for AppFabric](jira.md "jira.md")
- [Configure Box for AppFabric](box.md "box.md")
- [Configure Cisco Duo for AppFabric](cisco-duo.md "cisco-duo.md")
- [Configure Dropbox for AppFabric](dropbox.md "dropbox.md")
- [Configure Genesys Cloud for AppFabric](genesys.md "genesys.md")
- [Configure GitHub for AppFabric](github.md "github.md")
- [Configure Google Analytics for AppFabric](google-analytics.md "google-analytics.md")
- [Configure Google Workspace for AppFabric](google-workspace.md "google-workspace.md")
- [Configure HubSpot for AppFabric](hubspot.md "hubspot.md")
- [Configure IBM Security® Verify for AppFabric](ibm-security.md "ibm-security.md")
- [Configure JumpCloud for AppFabric](jumpcloud.md "jumpcloud.md")
- [Configure Microsoft 365 for AppFabric](microsoft-365.md "microsoft-365.md")
- [Configure Miro for AppFabric](miro.md "miro.md")
- [Configure Okta for AppFabric](okta.md "okta.md")
- [Configure OneLogin by One Identity for AppFabric](onelogin.md "onelogin.md")
- [Configure PagerDuty for AppFabric](pagerduty.md "pagerduty.md")
- [Configure Ping Identity for AppFabric](pingidentity.md "pingidentity.md")
- [Configure Salesforce for AppFabric](salesforce.md "salesforce.md")
- [Configure ServiceNow for AppFabric](servicenow.md "servicenow.md")
- [Configure Singularity Cloud for AppFabric](singularity-cloud.md "singularity-cloud.md")
- [Configure Slack for AppFabric](slack.md "slack.md")
- [Configure Smartsheet for AppFabric](smartsheet.md "smartsheet.md")
- [Configure Terraform Cloud for AppFabric](terraform.md "terraform.md")
- [Configure Webex by Cisco for AppFabric](webex.md "webex.md")
- [Configure Zendesk for AppFabric](zendesk.md "zendesk.md")
- [Configure Zoom for AppFabric](zoom.md "zoom.md")

## (Optional) Create an output location

AppFabric for security supports Amazon Simple Storage Service (Amazon S3) and Amazon Data Firehose as audit log ingestion
destinations.

### Amazon S3

You can create a new Amazon S3 bucket using the AppFabric console when you create an
ingestion destination. You can also create a bucket using the Amazon S3 service. If you
choose to create your bucket using the Amazon S3 service, you must create the bucket
before creating the AppFabric ingestion destination, and then select the bucket when you
create the ingestion destination. You can choose to use an existing Amazon S3 bucket in
your AWS account, as long as it meets the following requirements for existing
buckets:

- AppFabric for security requires that your Amazon S3 bucket be in the same AWS Region
  as your Amazon S3 resources.
- Your can encrypt your bucket using one of the following:
  - Server-side encryption with Amazon S3 managed keys (SSE-S3)
  - Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) using
    the default AWS managed key (`aws/s3`).

### Amazon Data Firehose

You can choose to use Amazon Data Firehose as your ingestion destination for AppFabric for
security data. To use Firehose, you can create the Firehose delivery stream in your
AWS account before creating an ingestion or while you're creating an ingestion
destination in AppFabric. You can create a Firehose delivery stream using the AWS Management Console,
AWS CLI, or the AWS APIs or SDKs. For stream configuration instructions, see the
following topics:

- AWS Management Console instructions – [Creating an Amazon Data Firehose
  Delivery Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the _Amazon Data Firehose Developer
  Guide_
- AWS CLI instructions – [create-delivery-stream](../../../index.md "../../../index.md") in the _AWS CLI Command Reference_
- AWS APIs and SDKs instructions – [CreateDeliveryStream](../../../firehose/latest/APIReference/API_CreateDeliveryStream.md "../../../firehose/latest/APIReference/API_CreateDeliveryStream.md") in the _Amazon Data Firehose
  API Reference_

The requirements when using Amazon Data Firehose as the AppFabric for security output destination are
as follows:

- You must create the stream in the same AWS Region as your AppFabric for
  security resources.
- You must select **Direct PUT** as the source.
- Attach **AmazonKinesisFirehoseFullAccess**
  AWS managed policy to your user, or attach the following permissions to
  your user:

```
{
    "Sid": "TagFirehoseDeliveryStream",
    "Effect": "Allow",
    "Action": ["firehose:TagDeliveryStream"],
    "Condition": {
        "ForAllValues:StringEquals": {"aws:TagKeys": "AWSAppFabricManaged"}
    },
    "Resource": "arn:aws:firehose:*:*:deliverystream/*"
}
```

Firehose supports integration with a variety of third-party security tools, such as
Splunk and Logz.io. For information about how to
properly configure Amazon Kinesis so that it outputs data to these tools, see [Destination Settings](../../../firehose/latest/dev/create-destination.md "../../../firehose/latest/dev/create-destination.md") in the _Amazon Data Firehose Developer
Guide_.

## (Optional) Create an AWS KMS key

In the process of creating an AppFabric for security app bundle, you will select or set up an
encryption key to securely protect your data from all authorized applications. This key
will be used to encrypt your data within the AppFabric service.

AppFabric for security encrypts data by default. AppFabric for security can use an AWS owned key
created and managed by AppFabric on your behalf or a customer managed key that you create and manage
in AWS Key Management Service (AWS KMS). AWS owned keys are a collection of AWS KMS keys that an
AWS service owns and manages for use in multiple AWS accounts. Customer managed keys are
AWS KMS keys in your AWS account that you create, own, and manage. For more information
about AWS owned keys and customer managed keys, see [Customer keys and AWS
keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the _AWS Key Management Service Developer Guide_.

If you want to use a customer managed key to encrypt your data, such as authorization tokens,
within AppFabric for security, you can create one with [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). For more information about the permissions policy that grants access
to your customer managed key in AWS KMS, see the [Key policy](data-protection.md#key-policy "data-protection.md#key-policy")
section of this guide.
