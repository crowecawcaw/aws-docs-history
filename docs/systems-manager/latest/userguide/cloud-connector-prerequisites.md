

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Prerequisites
<a name="cloud-connector-prerequisites"></a>

Before you create a Cloud Connector, complete the following prerequisites on both the AWS side and the Azure side. These steps establish OIDC-based federated authentication between AWS and Microsoft Azure.

**Note**  
The manual Azure prerequisites in [Azure prerequisites](cloud-connector-prereqs-azure.md) apply to the AWS CLI path only. If you create a Cloud Connector in the AWS Management Console, the wizard generates a setup script that performs this Azure-side setup for you. For more information, see [Create a Cloud Connector (AWS Management Console)](cloud-connector-create-console.md).

**Important**  
Make sure your AWS account is not in any service control policy (SCP) that restricts the `sts:GetWebIdentityToken` action.

**Topics**
+ [AWS prerequisites](cloud-connector-prereqs-aws.md)
+ [Azure prerequisites](cloud-connector-prereqs-azure.md)