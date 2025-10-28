# Amazon DynamoDB controls

###### Topics

- [[CT.DYNAMODB.PR.1] Require that point-in-time recovery for an Amazon DynamoDB table is activated](#ct-dynamodb-pr-1-description "#ct-dynamodb-pr-1-description")
- [[CT.DYNAMODB.PR.2] Require an Amazon DynamoDB table to be encrypted at rest using an AWS KMS key](#ct-dynamodb-pr-2-description "#ct-dynamodb-pr-2-description")

## [CT.DYNAMODB.PR.1] Require that point-in-time recovery for an Amazon DynamoDB table is activated

This control checks whether point-in-time recovery (PITR) is enabled for an Amazon DynamoDB table.

- **Control objective:** Improve resiliency
- **Implementation:** AWS CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DynamoDB::Table`
- **AWS CloudFormation guard rule:**
  [CT.DYNAMODB.PR.1 rule specification](#ct-dynamodb-pr-1-rule "#ct-dynamodb-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DYNAMODB.PR.1 rule specification](#ct-dynamodb-pr-1-rule "#ct-dynamodb-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.DYNAMODB.PR.1 example templates](#ct-dynamodb-pr-1-templates "#ct-dynamodb-pr-1-templates")

**Explanation**

Backups help you to recover more quickly from a security incident. They also strengthen the resilience of your systems. Amazon DynamoDB point-in-time recovery (PITR) automates backups for DynamoDB tables, which can reduce the time required to recover from accidental delete or write operations. DynamoDB tables that have PITR enabled can be restored to any point in time within the last 35 days.

### Remediation for rule failure

Provide a `PointInTimeRecoverySpecification` configuration and set `PointInTimeRecoveryEnabled` to `true`.

The examples that follow show how to implement this remediation.

#### Amazon DynamoDB Table - Example

Amazon DynamoDB table configured with point-in-time recovery activated. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DynamoDBTable": {
        "Type": "AWS::DynamoDB::Table",
        "Properties": {
            "AttributeDefinitions": [
                {
                    "AttributeName": "PK",
                    "AttributeType": "S"
                }
            ],
            "BillingMode": "PAY_PER_REQUEST",
            "KeySchema": [
                {
                    "AttributeName": "PK",
                    "KeyType": "HASH"
                }
            ],
            "PointInTimeRecoverySpecification": {
                "PointInTimeRecoveryEnabled": true
            }
        }
    }
}

```

**YAML example**

```

DynamoDBTable:
  Type: AWS::DynamoDB::Table
  Properties:
    AttributeDefinitions:
      - AttributeName: PK
        AttributeType: S
    BillingMode: PAY_PER_REQUEST
    KeySchema:
      - AttributeName: PK
        KeyType: HASH
    PointInTimeRecoverySpecification:
      PointInTimeRecoveryEnabled: true


```

### CT.DYNAMODB.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
# Rule Identifier:
#   dynamodb_table_pitr_enabled_check
#
# Description:
#   This control checks whether point-in-time recovery (PITR) is enabled for an Amazon DynamoDB table.
#
# Reports on:
#   AWS::DynamoDB::Table
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Paramaeters:
#   None
#
# Scenarios:
#   Scenario: 1
#      Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#        And: The input document does not contain any DynamoDB table resources
#       Then: SKIP
#   Scenario: 2
#      Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#        And: The input document does not contains a DynamoDB table resource
#        And: 'PointInTimeRecoverySpecification' is not present on the DynamoDB table resource
#       Then: FAIL
#   Scenario: 3
#      Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#        And: The input document does not contains a DynamoDB table resource
#        And: 'PointInTimeRecoverySpecification' is present on the DynamoDB table resource
#        And: 'PointInTimeRecoveryEnabled' in 'PointInTimeRecoverySpecification' is missing or is a value
#              other than bool(true)
#       Then: FAIL
#   Scenario: 4
#      Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#        And: The input document does not contains a DynamoDB table resource
#        And: 'PointInTimeRecoverySpecification' is present on the DynamoDB table resource
#        And: 'PointInTimeRecoveryEnabled' in 'PointInTimeRecoverySpecification' is present and set to bool(true)
#       Then: PASS

#
# Constants
#
let DYNAMODB_TABLE_TYPE = "AWS::DynamoDB::Table"
let INPUT_DOCUMENT = this

#
# Assignments
#
let dynamodb_tables = Resources.*[ Type == %DYNAMODB_TABLE_TYPE ]

#
# Primary Rules
#
rule dynamodb_table_pitr_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                            %dynamodb_tables not empty {
    check(%dynamodb_tables.Properties)
        <<
        [CT.DYNAMODB.PR.1]: Require that point-in-time recovery for an Amazon DynamoDB table is activated
            [FIX]: Provide a 'PointInTimeRecoverySpecification' configuration and set 'PointInTimeRecoveryEnabled' to 'true'.
        >>
}

rule dynamodb_table_pitr_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %DYNAMODB_TABLE_TYPE) {
    check(%INPUT_DOCUMENT.%DYNAMODB_TABLE_TYPE.resourceProperties)
        <<
        [CT.DYNAMODB.PR.1]: Require that point-in-time recovery for an Amazon DynamoDB table is activated
            [FIX]: Provide a 'PointInTimeRecoverySpecification' configuration and set 'PointInTimeRecoveryEnabled' to 'true'.
        >>
}

rule check(dynamodb_table) {
    %dynamodb_table {
        # Scenario 2
        PointInTimeRecoverySpecification exists
        PointInTimeRecoverySpecification is_struct

        # Scenario 3 and 4
        PointInTimeRecoverySpecification {
            PointInTimeRecoveryEnabled exists
            PointInTimeRecoveryEnabled == true
        }
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, DYNAMODB_TABLE_TYPE) {
    %doc.%DYNAMODB_TABLE_TYPE.resourceProperties exists
}


```

### CT.DYNAMODB.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: "PK"
          AttributeType: "S"
      BillingMode: "PAY_PER_REQUEST"
      KeySchema:
        - AttributeName: "PK"
          KeyType: "HASH"
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: "PK"
          AttributeType: "S"
      BillingMode: "PAY_PER_REQUEST"
      KeySchema:
        - AttributeName: "PK"
          KeyType: "HASH"
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: false


```

## [CT.DYNAMODB.PR.2] Require an Amazon DynamoDB table to be encrypted at rest using an AWS KMS key

This control checks whether your Amazon DynamoDB table is encrypted with an AWS Key Management Service (KMS) key.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DynamoDB::Table`
- **AWS CloudFormation guard rule:**
  [CT.DYNAMODB.PR.2 rule specification](#ct-dynamodb-pr-2-rule "#ct-dynamodb-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DYNAMODB.PR.2 rule specification](#ct-dynamodb-pr-2-rule "#ct-dynamodb-pr-2-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.DYNAMODB.PR.2 example templates](#ct-dynamodb-pr-2-templates "#ct-dynamodb-pr-2-templates")

**Explanation**

Amazon DynamoDB encryption at rest provides an additional layer of data protection, because it always secures your data in an encrypted table - including its primary key, local and global secondary indexes, streams, global tables, backups, and DynamoDB Accelerator (DAX) clusters, whenever the data is stored in durable media.

Encryption at rest integrates with AWS KMS for managing the encryption keys that are used to encrypt your tables.

###### Usage considerations

- This control requires only that KMS keys are used for server-side encryption. It does not check the properties of the KMS key used, such as whether the KMS key is customer-managed or service-managed.

### Remediation for rule failure

Provide a `SSESpecification` configuration and set `SSEEnabled` to `true`.

The examples that follow show how to implement this remediation.

#### Amazon DynamoDB Table - Example

An Amazon DynamoDB table configured to encrypt data at rest with AWS Key Management Service (KMS) keys. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DynamoDBTable": {
        "Type": "AWS::DynamoDB::Table",
        "Properties": {
            "AttributeDefinitions": [
                {
                    "AttributeName": "PK",
                    "AttributeType": "S"
                }
            ],
            "BillingMode": "PAY_PER_REQUEST",
            "KeySchema": [
                {
                    "AttributeName": "PK",
                    "KeyType": "HASH"
                }
            ],
            "SSESpecification": {
                "SSEEnabled": true
            }
        }
    }
}

```

**YAML example**

```

DynamoDBTable:
  Type: AWS::DynamoDB::Table
  Properties:
    AttributeDefinitions:
      - AttributeName: PK
        AttributeType: S
    BillingMode: PAY_PER_REQUEST
    KeySchema:
      - AttributeName: PK
        KeyType: HASH
    SSESpecification:
      SSEEnabled: true


```

### CT.DYNAMODB.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   dynamodb_table_encrypted_kms_check
#
# Description:
#   This control checks whether your Amazon DynamoDB table is encrypted with an AWS Key Management Service (KMS) key.
#
# Reports on:
#   AWS::DynamoDB::Table
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any DynamoDB table resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DynamoDB table resources
#       And: 'SSEEnabled' in 'SSESpecification' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DynamoDB table resources
#       And: 'SSEEnabled' in 'SSESpecification' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DynamoDB table resources
#       And: 'SSEEnabled' in 'SSESpecification' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let DYNAMODB_TABLE_TYPE = "AWS::DynamoDB::Table"
let INPUT_DOCUMENT = this

#
# Assignments
#
let dynamodb_tables = Resources.*[ Type == %DYNAMODB_TABLE_TYPE ]

#
# Primary Rules
#
rule dynamodb_table_encrypted_kms_check when is_cfn_template(%INPUT_DOCUMENT)
                                             %dynamodb_tables not empty {
    check(%dynamodb_tables.Properties)
        <<
        [CT.DYNAMODB.PR.2]: Require an Amazon DynamoDB table to be encrypted at rest using an AWS KMS key
        [FIX]: Provide a 'SSESpecification' configuration and set 'SSEEnabled' to 'true'.
        >>
}

rule dynamodb_table_encrypted_kms_check when is_cfn_hook(%INPUT_DOCUMENT, %DYNAMODB_TABLE_TYPE) {
    check(%INPUT_DOCUMENT.%DYNAMODB_TABLE_TYPE.resourceProperties)
        <<
        [CT.DYNAMODB.PR.2]: Require an Amazon DynamoDB table to be encrypted at rest using an AWS KMS key
        [FIX]: Provide a 'SSESpecification' configuration and set 'SSEEnabled' to 'true'.
        >>
}

rule check(dynamodb_table) {
    %dynamodb_table {
        # Scenario 2
        SSESpecification exists
        SSESpecification is_struct

        # Scenarios 3 and 4
        SSESpecification {
            SSEEnabled exists
            SSEEnabled == true
        }
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, DYNAMODB_TABLE_TYPE) {
    %doc.%DYNAMODB_TABLE_TYPE.resourceProperties exists
}


```

### CT.DYNAMODB.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
      - AttributeName: PK
        AttributeType: S
      BillingMode: PAY_PER_REQUEST
      KeySchema:
      - AttributeName: PK
        KeyType: HASH
      SSESpecification:
        SSEEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
      - AttributeName: PK
        AttributeType: S
      BillingMode: PAY_PER_REQUEST
      KeySchema:
      - AttributeName: PK
        KeyType: HASH
      SSESpecification:
        SSEEnabled: false


```
