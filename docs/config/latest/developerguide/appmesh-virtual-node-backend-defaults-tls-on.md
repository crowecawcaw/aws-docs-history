

# appmesh-virtual-node-backend-defaults-tls-on
<a name="appmesh-virtual-node-backend-defaults-tls-on"></a>

Checks if backend defaults for AWS App Mesh virtual nodes require the virtual nodes to communicate with all ports using TLS. The rule is NON\_COMPLIANT if configuration.Spec.BackendDefaults.ClientPolicy.Tls.Enforce is false. 



**Identifier:** APPMESH\_VIRTUAL\_NODE\_BACKEND\_DEFAULTS\_TLS\_ON

**Resource Types:** AWS::AppMesh::VirtualNode

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d145c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).