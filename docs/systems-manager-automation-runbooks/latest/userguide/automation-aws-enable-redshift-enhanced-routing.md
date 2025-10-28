# `AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting`

**Description**

The `AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting`
runbook enables enhanced virtual private cloud (VPC) routing for the Amazon Redshift cluster
you specify. For information about enhanced VPC routing, see [Amazon Redshift enhanced VPC routing](../../../redshift/latest/gsg/enhanced-vpc-routing.md "../../../redshift/latest/gsg/enhanced-vpc-routing.md") in
the _Amazon Redshift Management Guide_ .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- ClusterIdentifier

Type: String

Description: (Required) The unique identifier of the cluster you want to
enable enhanced VPC routing on.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `redshift:DescribeClusters`
- `redshift:ModifyCluster`

**Document Steps**

- `aws:executeAwsApi` - Enables enhanced VPC routing on the cluster
  specified in the `ClusterIdentifier` parameter.
- `assertAwsResourceProperty` - Confirms enhanced VPC routing was
  enabled on the cluster.
