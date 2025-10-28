# Setting up your anomaly detection

The overviews in this section describe how to get started with AWS Cost Anomaly Detection in
AWS Billing and Cost Management.

###### Topics

- [Enabling Cost Explorer](#enable-ce-ad "#enable-ce-ad")
- [Controlling access using IAM](#access-iam-ad "#access-iam-ad")
- [Accessing the console](#access-ad "#access-ad")
- [Quotas](#limits-ad-section "#limits-ad-section")

## Enabling Cost Explorer

AWS Cost Anomaly Detection is a feature within Cost Explorer. To access AWS Cost Anomaly Detection, enable
Cost Explorer. For instructions on how to enable Cost Explorer using the console,
see [Enabling Cost Explorer](ce-enable.md "ce-enable.md").

## Controlling access using IAM

After you enable Cost Explorer at the management account level, you can use
AWS Identity and Access Management (IAM) to manage access to your billing data for individual users. You
can then grant or revoke access on an individual level for each user role, rather
than granting access to all users.

A user must be granted explicit permission to view pages in the Billing and Cost Management console. With
the appropriate permissions, the user can view costs for the AWS account that the
user belongs to. For the policy that grants the necessary permissions to a user, see
[Billing and Cost Management actions policies](billing-permissions-ref.md#user-permissions "billing-permissions-ref.md#user-permissions").

For more information about using resource-level access and attribute-based access
control (ABAC) for Cost Anomaly Detection, see [Controlling access for Cost Anomaly Detection](accesscontrol-ad.md "accesscontrol-ad.md").

## Accessing the console

When your setup is complete, access AWS Cost Anomaly Detection.

###### To access AWS Cost Anomaly Detection

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Anomaly Detection**.

## Quotas

For the default quotas, see [AWS Cost Anomaly Detection](management-limits.md#limits-ad "management-limits.md#limits-ad").
