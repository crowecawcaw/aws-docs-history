# Managed license settings in License Manager

The following settings are available for managed licenses.

## Account details

You can review your account details to see information such as the account type, whether
accounts in AWS Organizations are linked, the account's License Manager S3 bucket ARN, and the AWS Resource Access Manager share ARN.
This section also enables you to link your AWS Organizations accounts.

To distribute managed entitlements or self-managed licenses within your organization, choose
**Link AWS Organizations accounts**. The distributed grants for managed entitlements are
auto-accepted by all of your member accounts. When you select this option, we add a
service-linked role to the [management](management-role.md "management-role.md") and [member](member-role.md "member-role.md") accounts.

###### Note

To enable this option, you must be signed in to your management account and all features
must be enabled in AWS Organizations. For more information, see [Enabling all
features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the _AWS Organizations User Guide_.

This selection also creates an AWS Resource Access Manager resource share in your management account, which
allows you to seamlessly share self-managed licenses. For more information, see the [AWS Resource Access Manager User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md").

To disable this option, call the [UpdateServiceSettings](../APIReference/API_UpdateServiceSettings.md "../APIReference/API_UpdateServiceSettings.md") API.

## Cross-account resource discovery

You can turn on cross-account resource discovery in order to manage license usage across all
of your accounts in AWS Organizations.

To enable cross-account resource discovery in your organization, choose **Turn
on** for cross-account resource discovery. When you turn on the cross-account resource
discovery, AWS Organizations will automatically be linked to perform resource discovery across all of your
accounts.

License Manager uses [Systems Manager inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md")
to discover software usage. Verify that you have configured Systems Manager inventory on all of your
resources. Querying Systems Manager inventory requires the following:

- [Resource data
  sync](../../../systems-manager/latest/userguide/sysman-inventory-datasync.md "../../../systems-manager/latest/userguide/sysman-inventory-datasync.md") to store inventory in an Amazon S3 bucket.
- [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md") to aggregate inventory data from your accounts in
  AWS Organizations.
- [AWS Glue](../../../glue.md "../../../glue.md") to provide a fast query
  experience.

###### Note

The following AWS Regions don't require Amazon Athena or AWS Glue to query or
aggregate inventory data for Systems Manager inventory to discover software usage:

- Asia Pacific (Jakarta)
- Israel (Tel Aviv)

## Simple Notification Service (SNS)

You can configure an Amazon SNS to receive notifications and alerts from License Manager.

###### To configure an Amazon SNS topic

1. Choose **Edit** next to **Simple Notification Service
   (SNS)**.
2. Specify an SNS topic ARN in the following format:

`arn:`<aws_partition>`:sns:`<region>`:`<account_id>`:aws-license-manager-service-*` 3. Choose **Save changes**.
