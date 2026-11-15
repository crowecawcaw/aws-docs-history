

# Prerequisites
<a name="cloud-connector-gcp-prerequisites"></a>

Before you create a Cloud Connector, complete the following prerequisites on both the AWS side and the GCP side. These steps establish OIDC-based workload identity federation between AWS and GCP.

**Note**  
The manual GCP prerequisites in [GCP prerequisites](cloud-connector-gcp-prereqs-gcp.md) apply to the AWS CLI path only. If you create a Cloud Connector in the AWS Management Console, the wizard generates a setup script that performs this GCP-side setup for you. For more information, see [Create a Cloud Connector (AWS Management Console)](cloud-connector-gcp-create-console.md).

**Important**  
Make sure your AWS account is not in any service control policy (SCP) that restricts the `sts:GetWebIdentityToken` action.

**Topics**
+ [AWS prerequisites](cloud-connector-gcp-prereqs-aws.md)
+ [GCP prerequisites](cloud-connector-gcp-prereqs-gcp.md)