# appmesh-virtual-node-cloud-map-ip-pref-check

Checks if an AWS App Mesh virtual node is configured with the specified IP preference for AWS Cloud Map service discovery. The rule is NON_COMPLIANT if the virtual node is not configured with the IP preference specified in the required rule parameter.

**Identifier:** APPMESH_VIRTUAL_NODE_CLOUD_MAP_IP_PREF_CHECK

**Resource Types:** AWS::AppMesh::VirtualNode

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

ipPreference
Type: String

The IP preference value for AWS Cloud Map service discovery. The rule is NON_COMPLIANT if a virtual node is configured with a value that does not match this value. Valid values include: 'IPv6_PREFERRED', 'IPv4_PREFERRED', 'IPv4_ONLY', and 'IPv6_ONLY'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
