# docdb-cluster-encrypted-in-transit

Checks if connections to Amazon DocumentDB clusters are configured to use encryption in transit. The rule is NON_COMPLIANT if the parameter group is not "in-sync", or the TLS parameter is set to either "disabled" or a value in `excludeTlsParameters`.

**Identifier:** DOCDB_CLUSTER_ENCRYPTED_IN_TRANSIT

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe (Stockholm), Middle East (Bahrain), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), US West (N. California), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

excludeTlsParameters (Optional)
Type: CSV

Comma-separated list of TLS cluster parameters for the rule to NOT check. Default value: 'disabled'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
