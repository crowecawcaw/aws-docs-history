# appmesh-virtual-node-service-backends-tls-enforced

Checks if service backends for AWS App Mesh virtual nodes require the virtual nodes to communicate with all ports using TLS. The rule is NON_COMPLIANT if any configuration.Spec.Backends[].ClientPolicy.Tls.Enforce is false.

**Identifier:** APPMESH_VIRTUAL_NODE_SERVICE_BACKENDS_TLS_ENFORCED

**Resource Types:** AWS::AppMesh::VirtualNode

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
