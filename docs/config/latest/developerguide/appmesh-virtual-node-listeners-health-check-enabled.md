# appmesh-virtual-node-listeners-health-check-enabled

Checks if listeners for AWS App Mesh virtual nodes have health check enabled. The rule is NON_COMPLIANT if configuration.Spec.Listeners[].HealthCheck does not exist in one or more listeners.

**Identifier:** APPMESH_VIRTUAL_NODE_LISTENERS_HEALTH_CHECK_ENABLED

**Resource Types:** AWS::AppMesh::VirtualNode

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
