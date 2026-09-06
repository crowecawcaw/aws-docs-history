

# eks-cluster-secrets-encrypted
<a name="eks-cluster-secrets-encrypted"></a>

Checks if Amazon EKS clusters are configured to have Kubernetes secrets encrypted using AWS KMS. The rule is NON\_COMPLIANT if an EKS cluster does not have an encryptionConfig resource or if encryptionConfig does not name secrets as a resource. 



**Identifier:** EKS\_CLUSTER\_SECRETS\_ENCRYPTED

**Resource Types:** AWS::EKS::Cluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV  
Comma-separated list of KMS key Amazon Resource Names (ARNs) that are approved for EKS usage.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d725c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).