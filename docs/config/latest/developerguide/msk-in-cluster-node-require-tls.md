

# msk-in-cluster-node-require-tls
<a name="msk-in-cluster-node-require-tls"></a>

Checks if an Amazon MSK cluster enforces encryption in transit using HTTPS (TLS) with the broker nodes of the cluster. The rule is NON\_COMPLIANT if plain text communication is enabled for in-cluster broker node connections. 



**Identifier:** MSK\_IN\_CLUSTER\_NODE\_REQUIRE\_TLS

**Resource Types:** AWS::MSK::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1131c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).