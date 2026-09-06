

# eks-cluster-supported-version
<a name="eks-cluster-supported-version"></a>

Checks if an Amazon Elastic Kubernetes Service (EKS) cluster is running a supported Kubernetes version. This rule is NON\_COMPLIANT if an EKS cluster is running an unsupported version (less than the parameter '`oldestVersionSupported`'). 



**Identifier:** EKS\_CLUSTER\_SUPPORTED\_VERSION

**Resource Types:** AWS::EKS::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

oldestVersionSupportedType: String  
Value of the oldest version of Kubernetes supported on AWS.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d727c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).