

# eks-cluster-log-enabled
<a name="eks-cluster-log-enabled"></a>

Checks if an Amazon Elastic Kubernetes Service (Amazon EKS) cluster is configured with logging enabled. The rule is NON\_COMPLIANT if logging for Amazon EKS clusters is not enabled or if logging is not enabled with the log type mentioned. 



**Identifier:** EKS\_CLUSTER\_LOG\_ENABLED

**Resource Types:** AWS::EKS::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

logTypes (Optional)Type: CSV  
Comma-separated list of EKS Cluster control plane log types for the rule to check. Valid values: "api", "audit", "authenticator", "controllerManager", "scheduler

## AWS CloudFormation template
<a name="w2aac20c16c17b7d721c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).