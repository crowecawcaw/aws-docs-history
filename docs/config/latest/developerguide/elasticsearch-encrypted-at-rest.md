# elasticsearch-encrypted-at-rest

Checks if Amazon OpenSearch Service (previously called Elasticsearch) domains have encryption at rest configuration enabled. The rule is NON_COMPLIANT if the EncryptionAtRestOptions field is not enabled.

**Identifier:** ELASTICSEARCH_ENCRYPTED_AT_REST

**Resource Types:** AWS::Elasticsearch::Domain

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
