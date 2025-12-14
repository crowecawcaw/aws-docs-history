# Working with the configuration recorder

The _configuration recorder_ stores the configuration changes to the
resource types in scope as [configuration items
(CIs)](config-item-table.md "config-item-table.md").

There are two types of configuration recorders.

| **Type**                                | **Description**                                                                                                                                                                                                                   |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer managed configuration recorder | A configuration recorder that you managed. The resource types in scope are set by<br>you. By default, a customer managed configuration recorder records all supported<br>resources in the AWS Region where AWS Config is running. |
| Service-linked configuration recorder   | A configuration recorder that is linked to a specific AWS service. The resource<br>types in scope are set by the linked service.                                                                                                  |

###### Topics

- [Considerations for the customer managed
  configuration recorder](#stop-start-recorder-considerations "#stop-start-recorder-considerations")
- [Considerations for
  service-linked configuration recorders](#stop-start-recorder-considerations-service-linked "#stop-start-recorder-considerations-service-linked")
- [Drift detection for the configuration recorder](#drift-detection "#drift-detection")
- [Starting the customer managed configuration
  recorder](managing-recorder_console-start.md "managing-recorder_console-start.md")
- [Stopping the customer managed configuration
  recorder](managing-recorder_console-stop.md "managing-recorder_console-stop.md")
- [Changing the recording
  frequency for the customer managed configuration recorder](managing-recorder_console-change-recording-frequency.md "managing-recorder_console-change-recording-frequency.md")
- [Renaming the customer managed configuration
  recorder](managing-recorder_console-rename.md "managing-recorder_console-rename.md")
- [Viewing your configuration recorders](configuration-recorder-view.md "configuration-recorder-view.md")
- [Deleting your configuration
  recorders](managing-recorder_console-delete.md "managing-recorder_console-delete.md")

## Considerations for the customer managed

configuration recorder

**One customer managed configuration recorder per account per
Region**

You can have only one customer managed configuration recorder for each AWS account for
each AWS Region.

**Default is to record all supported resource types, excluding the global IAM
resource types**

The default for a customer managed configuration recorder is to record all supported
resource types, excluding the following global IAM resource types:
`AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`,
and `AWS::IAM::User` You can specify which resource types you want to include or
exclude from recording.

For more information, see [Recording AWS Resources with AWS Config](select-resources.md "select-resources.md").

**You are charged service usage fees for using the customer managed configuration
recorder**

You are charged service usage fees when AWS Config starts recording configurations with the
customer managed configuration recorder.

For pricing information, see [AWS Config
Pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/").

**Use AWS Systems Manager to create a customer managed configuration recorder across an
organization**

You can use AWS Systems Manager Quick Setup to create a customer managed configuration recorder
across multiple organizational units (OUs) and AWS Regions using AWS best
practices.

For more information, see [Create an AWS Config configuration
recorder using Quick Setup](../../../systems-manager/latest/userguide/quick-setup-config.md "../../../systems-manager/latest/userguide/quick-setup-config.md") in the _Systems Manager User Guide_.

###### Important

**Policies and compliance results**

[IAM
policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") and [other policies managed in
AWS Organizations](../../../organizations/latest/userguide/orgs_manage_policies.md "../../../organizations/latest/userguide/orgs_manage_policies.md") can impact whether AWS Config has permissions to record configuration changes
for your resources. Additionally, rules directly evaluate the configuration of a resource
and rules don't take into account these policies when running evaluations. Make sure that
the policies in effect align with how you intend to use AWS Config.

**Stale evaluation results for deleted resources can persist if the
configuration recorder is turned off**

If the customer managed configuration recorder is turned off, it disables the ability of
AWS Config Config to track changes to the configuration of the resources you specified, including
their deletions. This means you might see stale evaluation results for resources that are
deleted when the customer managed configuration recorder is turned off since AWS Config cannot
capture deletion events if recording is not on.

## Considerations for

service-linked configuration recorders

**The AWS Config service-linked role must be used**

The AWS Config service-linked role is required for service-linked configuration
recorders.

For more information, see [Using
Service-Linked Roles for AWS Config](using-service-linked-roles.md "using-service-linked-roles.md").

**Service-linked configuration recorders are always recording**

Service-linked recorders are fixed. You can't directly change the settings in a
service-linked recorder. To modify recorder settings such as starting, stopping, or updating
the recorder, make these changes through the associated AWS service that uses the
service-linked recorder.

For more information, see [Deleting the Configuration Recorder](managing-recorder_console-delete.md "managing-recorder_console-delete.md").

**The recording scope determines if you receive configuration
items**

The recording scope is set by the AWS service that is linked to the configuration
recorder and determines whether you receive configuration items (CIs) in the delivery channel.
If the recording scope is INTERNAL, you will not receive CIs in the delivery channel.

**The recording scope determines if you are charged a service
fee**

The recording scope is set by the AWS service that is linked to the configuration
recorder and determines whether the configuration items (CIs) in scope are recorded for free
(INTERNAL) or if it impacts the costs of your bill (PAID).

**Recording frequency precedence between recorders**

When you have both a customer managed configuration recorder and a service-linked configuration recorder with a recording scope of 'PAID' that record the same resource types, the recorder with the higher recording frequency takes precedence. For example, if your customer managed recorder is set to daily recording, but you enable an AWS service that uses a service-linked recorder with a recording scope of 'PAID' and continuous recording, the affected resource types will be recorded continuously.

This means that even though your customer managed recorder settings still show "Daily recording," you will be charged for continuous recording for the resource types that are in scope for both recorders. This only affects resource types that are being recorded by both recorders.

###### Note

You are charged only once per configuration item, regardless of the number of
configuration items generated by a customer managed configuration recorder or service-linked
configuration recorders that you pay for.

###### Example: Recording frequency precedence

You have configured your customer managed recorder to record Amazon EC2 instances with daily
recording frequency. Later, you enable an AWS service feature that uses a service-linked
recorder with a recording scope of 'PAID' and continuous recording that also records Amazon EC2
instances. In this scenario:

- Your customer managed recorder settings will still show "Daily recording"
- Amazon EC2 instances will be recorded continuously and provides additional CIs because the
  service-linked recorder with a recording scope of 'PAID' has a higher recording
  frequency
- You will be charged for continuous recording of Amazon EC2 instances
- Other resource types that are only recorded by your customer managed recorder will continue to
  be recorded in a daily recording frequency

### Supported services

Service-linked configuration recorders are supported for the following services:

| **AWS service**       | **Service principal**                                                                        | **Benefits of using with AWS Config**                                                                                                                                                                                                                                                        | **Learn more**                                                                                                                                                                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon CloudWatch     | `observabilityadmin.amazonaws.com,<br>telemetry-enablement.observabilityadmin.amazonaws.com` | You can use Amazon CloudWatch Observability Admin to discover and understand the state of telemetry configuration in CloudWatch for your AWS Organization or account.                                                                                                                        | For more information, see [Auditing CloudWatch telemetry configurations](../../../AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.md") in the _CloudWatch User Guide_. |
| AWS Security Hub CSPM | `securityhub.amazonaws.com`                                                                  | You can use AWS Security Hub CSPM to centrally manage security findings and perform<br>security assessments across your AWS accounts. The service-linked recorder enables<br>an event-driven approach for obtaining resource configuration items required for<br>exposure analysis coverage. | For more information, see [Enabling Security Hub](../../../securityhub/latest/userguide/security-hub-adv-getting-started-enable.md "../../../securityhub/latest/userguide/security-hub-adv-getting-started-enable.md") in the _Security Hub CSPM User<br>Guide_.  |

## Drift detection for the configuration recorder

The `AWS::Config::ConfigurationRecorder` resource type is a
_configuration item_ (CI) for the configuration recorder that tracks all
changes to the state of configuration recorder. You can use this CI to check if the state of
the configuration recorder differs, or has _drifted_, from its previous
state.

For example, this CI tracks if there are updates to resource types that you have enabled
AWS Config to track, if you have stopped or started the configuration recorder, or if you have
deleted or uninstalled the configuration recorder. A drifted configuration recorder indicates
that you are not accurately detecting changes to your intended resource types. If your
configuration recorder has been drifted, this can result in false negative or false positive
compliance results.

The `AWS::Config::ConfigurationRecorder` resource type is a system resource
type of AWS Config and recording of this resource type is enabled by default in all supported
Regions. Recording for the `AWS::Config::ConfigurationRecorder` resource type comes
with no additional charge.
