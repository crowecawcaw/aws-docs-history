

# appmesh-virtual-node-listeners-outlier-detect-enabled
<a name="appmesh-virtual-node-listeners-outlier-detect-enabled"></a>

Checks if listeners for AWS App Mesh virtual nodes have outlier detection enabled. The rule is NON\_COMPLIANT if configuration.Spec.Listeners[].OutlierDetection does not exist in one or more listeners. 



**Identifier:** APPMESH\_VIRTUAL\_NODE\_LISTENERS\_OUTLIER\_DETECT\_ENABLED

**Resource Types:** AWS::AppMesh::VirtualNode

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d153c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).