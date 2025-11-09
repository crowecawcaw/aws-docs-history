# eks-endpoint-no-public-access

Checks if the Amazon Elastic Kubernetes Service (Amazon EKS) endpoint is not publicly accessible. The rule is NON_COMPLIANT if the endpoint is publicly accessible.

**Identifier:** EKS_ENDPOINT_NO_PUBLIC_ACCESS

**Resource Types:** AWS::EKS::Cluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
