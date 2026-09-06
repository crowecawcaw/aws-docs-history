

# Setting up your anomaly detection
<a name="settingup-ad"></a>

The overviews in this section describe how to get started with AWS Cost Anomaly Detection in AWS Billing and Cost Management.

**Topics**
+ [Enabling Cost Explorer](#enable-ce-ad)
+ [Controlling access using IAM](#access-iam-ad)
+ [Accessing the console](#access-ad)
+ [Quotas](#limits-ad-section)

## Enabling Cost Explorer
<a name="enable-ce-ad"></a>

AWS Cost Anomaly Detection is a feature within Cost Explorer. To access AWS Cost Anomaly Detection, enable Cost Explorer. For instructions on how to enable Cost Explorer using the console, see [Enabling Cost Explorer](ce-enable.md).

## Controlling access using IAM
<a name="access-iam-ad"></a>

After you enable Cost Explorer at the management account level, you can use AWS Identity and Access Management (IAM) to manage access to your billing data for individual users. You can then grant or revoke access on an individual level for each user role, rather than granting access to all users.

A user must be granted explicit permission to view pages in the Billing and Cost Management console. With the appropriate permissions, the user can view costs for the AWS account that the user belongs to. For the policy that grants the necessary permissions to a user, see [Billing and Cost Management actions policies](billing-permissions-ref.md#user-permissions). 

For more information about using resource-level access and attribute-based access control (ABAC) for Cost Anomaly Detection, see [Controlling access for Cost Anomaly Detection](accesscontrol-ad.md).

## Accessing the console
<a name="access-ad"></a>

When your setup is complete, access AWS Cost Anomaly Detection.<a name="access-ad-process"></a>

**To access AWS Cost Anomaly Detection**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Anomaly Detection**.

## Quotas
<a name="limits-ad-section"></a>

For the default quotas, see [AWS Cost Anomaly Detection](management-limits.md#limits-ad).