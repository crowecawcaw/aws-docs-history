# `AWS-UpdateEKSCluster`

**Description**

The `AWS-UpdateEKSCluster` runbook helps you update your Amazon Elastic Kubernetes Service
(Amazon EKS) cluster to the Kubernetes version that you want to use.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateEKSCluster "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateEKSCluster")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- ClusterName

Type: String

Description: (Required) The name of your Amazon EKS cluster.

- Version

Type: String

Description: (Required) The Kubernetes version that you want to update
your cluster to.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `eks:DescribeUpdate`
- `eks:UpdateClusterVersion`

**Document Steps**

- `aws:executeAwsApi` - Updates the Kubernetes version that is used
  by your Amazon EKS cluster.
- `aws:waitForAwsResourceProperty` - Waits for the update status to
  be `Successful`.
