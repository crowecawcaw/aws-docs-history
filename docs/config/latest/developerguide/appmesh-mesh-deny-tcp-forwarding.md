

# appmesh-mesh-deny-tcp-forwarding
<a name="appmesh-mesh-deny-tcp-forwarding"></a>

Checks if proxies for AWS App Mesh service meshes do not forward TCP traffic directly to services that aren't deployed with a proxy that is defined in the mesh. The rule is NON\_COMPLIANT if configuration.Spec.EgressFilter.Type is set to 'ALLOW\_ALL'. 



**Identifier:** APPMESH\_MESH\_DENY\_TCP\_FORWARDING

**Resource Types:** AWS::AppMesh::Mesh

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d129c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).