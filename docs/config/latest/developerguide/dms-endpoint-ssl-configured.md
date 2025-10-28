# dms-endpoint-ssl-configured

Checks if AWS Database Migration Service (AWS DMS) endpoints are configured with an SSL connection. The rule is NON_COMPLIANT if AWS DMS does not have an SSL connection configured.

**Context**:
SSL/TLS connections provide one layer of security by encrypting data that moves between your client and a DB instance.
Using server certificate provides an extra layer of security by validating that the connection is being made to an Amazon RDS DB instance.
It does so by checking the server certificate that is automatically installed on all DB instances that you provision.
By enabling SSL connection on AWS DMS, you protect the confidentiality of the data during the migration.

To configure SSL connection for AWS DMS, see [Using SSL/TLS to encrypt a connection to a DB instance or cluster](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") in the
_Amazon Relational Database Service User Guide_.

**Identifier:** DMS_ENDPOINT_SSL_CONFIGURED

**Resource Types:** AWS::DMS::Endpoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
