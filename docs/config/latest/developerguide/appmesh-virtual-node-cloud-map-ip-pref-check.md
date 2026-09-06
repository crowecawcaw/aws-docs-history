

# appmesh-virtual-node-cloud-map-ip-pref-check
<a name="appmesh-virtual-node-cloud-map-ip-pref-check"></a>

Checks if an AWS App Mesh virtual node is configured with the specified IP preference for AWS Cloud Map service discovery. The rule is NON\_COMPLIANT if the virtual node is not configured with the IP preference specified in the required rule parameter. 



**Identifier:** APPMESH\_VIRTUAL\_NODE\_CLOUD\_MAP\_IP\_PREF\_CHECK

**Resource Types:** AWS::AppMesh::VirtualNode

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

ipPreferenceType: String  
The IP preference value for AWS Cloud Map service discovery. The rule is NON\_COMPLIANT if a virtual node is configured with a value that does not match this value. Valid values include: 'IPv6\_PREFERRED', 'IPv4\_PREFERRED', 'IPv4\_ONLY', and 'IPv6\_ONLY'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d147c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).