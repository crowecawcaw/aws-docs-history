# Amazon Athena controls

###### Topics

- [[CT.ATHENA.PR.2] Require an Amazon Athena workgroup to encrypt Athena query results at rest with an AWS Key Management Service (KMS) key](#ct-athena-pr-2-description "#ct-athena-pr-2-description")

## [CT.ATHENA.PR.2] Require an Amazon Athena workgroup to encrypt Athena query results at rest with an AWS Key Management Service (KMS) key

This control checks whether an Amazon Athena workgroup is configured to encrypt query results at rest with an AWS KMS key.

- **Control objective:** Encrypt data at rest
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Athena::WorkGroup`
- **CloudFormation guard rule:**
  [CT.ATHENA.PR.2 rule specification](#ct-athena-pr-2-rule "#ct-athena-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ATHENA.PR.2 rule specification](#ct-athena-pr-2-rule "#ct-athena-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.ATHENA.PR.2 example templates](#ct-athena-pr-2-templates "#ct-athena-pr-2-templates")

**Explanation**

For an added layer of security, you can encrypt the results of Athena queries in the workgroup with AWS Key Management Service (KMS).

###### Usage considerations

- This control requires an Athena workgroup to override client settings by requiring the `EnforceWorkGroupConfiguration` property to be provided and set to true, or omitted to adopt the default value of true.

### Remediation for rule failure

In the `WorkGroupConfiguration.ResultConfiguration` parameter, provide an `EncryptionConfiguration` configuration with an `EncryptionOption` set to a KMS-based encryption option, and with `KmsKey` set to the identifier or ARN of an AWS KMS key, or the name of an AWS KMS key alias.

The examples that follow show how to implement this remediation.

#### Amazon Athena workgroup - Example

Amazon Athena workgroup configured to encrypt Athena query results with AWS KMS (SSE_KMS). The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AthenaWorkGroup": {
        "Type": "AWS::Athena::WorkGroup",
        "Properties": {
            "Name": {
                "Fn::Sub": "${AWS::StackName}-example"
            },
            "Description": "Example workgroup",
            "State": "ENABLED",
            "WorkGroupConfiguration": {
                "EnforceWorkGroupConfiguration": true,
                "ResultConfiguration": {
                    "EncryptionConfiguration": {
                        "KmsKey": {
                            "Ref": "Key"
                        },
                        "EncryptionOption": "SSE_KMS"
                    }
                }
            }
        }
    }
}

```

**YAML example**

```

AthenaWorkGroup:
  Type: AWS::Athena::WorkGroup
  Properties:
    Name: !Sub '${AWS::StackName}-example'
    Description: Example workgroup
    State: ENABLED
    WorkGroupConfiguration:
      EnforceWorkGroupConfiguration: true
      ResultConfiguration:
        EncryptionConfiguration:
          KmsKey: !Ref 'Key'
          EncryptionOption: SSE_KMS


```

### CT.ATHENA.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   athena_workgroup_results_encrypted_at_rest_kms_check
#
# Description:
#   This control checks whether an Amazon Athena workgroup is configured to encrypt query results at rest with an AWS KMS key.
#
# Reports on:
#   AWS::Athena::WorkGroup
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any Athena workgroup resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Athena workgroup resource
#       And: 'EnforceWorkGroupConfiguration' in 'WorkGroupConfiguration' has been provided and
#            set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Athena workgroup resource
#       And: 'EnforceWorkGroupConfiguration' in 'WorkGroupConfiguration' has not been provided or provided
#            and set to bool(true)
#       And: 'EncryptionConfiguration' in 'WorkGroupConfiguration.ResultConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Athena workgroup resource
#       And: 'EnforceWorkGroupConfiguration' in 'WorkGroupConfiguration' has not been provided or provided
#            and set to bool(true)
#       And: 'EncryptionConfiguration' in 'WorkGroupConfiguration.ResultConfiguration' has been provided
#       And: 'EncryptionOption' in 'EncryptionConfiguration' has not been provided or provided as an empty string
#       And: 'KmsKey' in 'EncryptionConfiguration' has not been provided or provided as an empty string or
#            invalid local reference
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Athena workgroup resource
#       And: 'EnforceWorkGroupConfiguration' in 'WorkGroupConfiguration' has not been provided or provided
#            and set to bool(true)
#       And: 'EncryptionConfiguration' in 'WorkGroupConfiguration.ResultConfiguration' has been provided
#       And: 'EncryptionOption' in 'EncryptionConfiguration' has been provided as a non-empty string
#       And: 'KmsKey' in 'EncryptionConfiguration' has not been provided or provided as an empty string or
#            invalid local reference
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Athena workgroup resource
#       And: 'EnforceWorkGroupConfiguration' in 'WorkGroupConfiguration' has not been provided or provided
#            and set to bool(true)
#       And: 'EncryptionConfiguration' in 'WorkGroupConfiguration.ResultConfiguration' has been provided
#       And: 'EncryptionOption' in 'EncryptionConfiguration' has not been provided or provided as an empty string
#       And: 'KmsKey' in 'EncryptionConfiguration' has been provided as a non-empty string or valid local reference to
#            a KMS key or key alias
#      Then: FAIL
#   Scenario: 7
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Athena workgroup resource
#       And: 'EnforceWorkGroupConfiguration' in 'WorkGroupConfiguration' has not been provided or provided
#            and set to bool(true)
#       And: 'EncryptionConfiguration' in 'WorkGroupConfiguration.ResultConfiguration' has been provided
#       And: 'EncryptionOption' in 'EncryptionConfiguration' has been provided as a non-empty string
#       And: 'KmsKey' in 'EncryptionConfiguration' has been provided as a non-empty string or valid local reference to
#            a KMS key or key alias
#      Then: PASS

#
# Constants
#
let ATHENA_WORKGROUP_TYPE = "AWS::Athena::WorkGroup"
let INPUT_DOCUMENT = this

#
# Assignments
#
let athena_workgroups = Resources.*[ Type == %ATHENA_WORKGROUP_TYPE ]

#
# Primary Rules
#
rule athena_workgroup_results_encrypted_at_rest_kms_check when is_cfn_template(%INPUT_DOCUMENT)
                                                               %athena_workgroups not empty {
    check(%athena_workgroups.Properties)
        <<
        [CT.ATHENA.PR.2]: Require an Amazon Athena workgroup to encrypt Athena query results at rest with an AWS Key Management Service (KMS) key
        [FIX]: In the 'WorkGroupConfiguration.ResultConfiguration' parameter, provide an 'EncryptionConfiguration' configuration with an 'EncryptionOption' set to a KMS-based encryption option, and with 'KmsKey' set to the identifier or ARN of an AWS KMS key, or the name of an AWS KMS key alias.
        >>
}

rule athena_workgroup_results_encrypted_at_rest_kms_check when is_cfn_hook(%INPUT_DOCUMENT, %ATHENA_WORKGROUP_TYPE) {
    check(%INPUT_DOCUMENT.%ATHENA_WORKGROUP_TYPE.resourceProperties)
        <<
        [CT.ATHENA.PR.2]: Require an Amazon Athena workgroup to encrypt Athena query results at rest with an AWS Key Management Service (KMS) key
        [FIX]: In the 'WorkGroupConfiguration.ResultConfiguration' parameter, provide an 'EncryptionConfiguration' configuration with an 'EncryptionOption' set to a KMS-based encryption option, and with 'KmsKey' set to the identifier or ARN of an AWS KMS key, or the name of an AWS KMS key alias.
        >>
}

#
# Parameterized Rules
#
rule check(athena_workgroup) {
    %athena_workgroup {
        WorkGroupConfiguration exists
        WorkGroupConfiguration is_struct

        WorkGroupConfiguration {
            # Scenario 2
            EnforceWorkGroupConfiguration not exists or
            EnforceWorkGroupConfiguration == true

            ResultConfiguration exists
            ResultConfiguration is_struct
            ResultConfiguration {
                # Scenario 3
                EncryptionConfiguration exists
                EncryptionConfiguration is_struct

                EncryptionConfiguration {
                    # Scenarios 4, 5, 6 and 7
                    EncryptionOption exists
                    check_is_string_and_not_empty(EncryptionOption)

                    KmsKey exists
                    check_is_string_and_not_empty(KmsKey) or
                    check_local_references(%INPUT_DOCUMENT, KmsKey, "AWS::KMS::Key") or
                    check_local_references(%INPUT_DOCUMENT, KmsKey, "AWS::KMS::Alias")
                }
            }
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

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}

rule check_local_references(doc, reference_properties, referenced_resource_type) {
    %reference_properties {
        'Fn::GetAtt' {
            query_for_resource(%doc, this[0], %referenced_resource_type)
                <<Local Stack reference was invalid>>
        } or Ref {
            query_for_resource(%doc, this, %referenced_resource_type)
                <<Local Stack reference was invalid>>
        }
    }
}

rule query_for_resource(doc, resource_key, referenced_resource_type) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
    %referenced_resource {
        Type == %referenced_resource_type
    }
}


```

### CT.ATHENA.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  Key:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: 2012-10-17
        Id: example-policy
        Statement:
        - Sid: Enable IAM user permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'
      KeySpec: SYMMETRIC_DEFAULT
  AthenaWorkGroup:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      Description: Example workgroup
      State: ENABLED
      WorkGroupConfiguration:
        EnforceWorkGroupConfiguration: true
        ResultConfiguration:
          EncryptionConfiguration:
            KmsKey:
              Ref: Key
            EncryptionOption: SSE_KMS


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  AthenaWorkGroup:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      Description: Example workgroup
      State: ENABLED
      WorkGroupConfiguration:
        ResultConfiguration:
          EncryptionConfiguration:
            EncryptionOption: SSE_S3


```
