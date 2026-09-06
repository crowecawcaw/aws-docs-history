

# docdb-cluster-encrypted-in-transit
<a name="docdb-cluster-encrypted-in-transit"></a>

Checks if connections to Amazon DocumentDB clusters are configured to use encryption in transit. The rule is NON\_COMPLIANT if the parameter group is not "in-sync", or the TLS parameter is set to either "disabled" or a value in `excludeTlsParameters`. 



**Identifier:** DOCDB\_CLUSTER\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Europe (Stockholm), Middle East (Bahrain), Asia Pacific (Jakarta), Africa (Cape Town), Asia Pacific (Osaka), Asia Pacific (Melbourne), US West (N. California), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

excludeTlsParameters (Optional)Type: CSV  
Comma-separated list of TLS cluster parameters for the rule to NOT check. Default value: 'disabled'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d493c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).