# AWS Key Management Service (AWS KMS) controls

###### Topics

- [[CT.KMS.PR.1] Require any AWS KMS key to have rotation configured](#ct-kms-pr-1-description "#ct-kms-pr-1-description")
- [[CT.KMS.PR.2] Require that an AWS Key Management Service asymmetric key with RSA key material used for encryption has a key length greater than 2048 bits](#ct-kms-pr-2-description "#ct-kms-pr-2-description")
- [[CT.KMS.PR.3] Require an AWS Key Management Service key policy to have a statement that limits
  creation of AWS KMS grants to AWS services](#ct-kms-pr-3-description "#ct-kms-pr-3-description")

## [CT.KMS.PR.1] Require any AWS KMS key to have rotation configured

This control checks whether key rotation is enabled for AWS KMS customer managed keys.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::KMS::Key`
- **AWS CloudFormation guard rule:**
  [CT.KMS.PR.1 rule specification](#ct-kms-pr-1-rule "#ct-kms-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.KMS.PR.1 rule specification](#ct-kms-pr-1-rule "#ct-kms-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.KMS.PR.1 example templates](#ct-kms-pr-1-templates "#ct-kms-pr-1-templates")

**Explanation**

Key rotation minimizes the possibility of key exposure to malicious users. Cryptographic best practices discourage extensive reuse of encryption keys. Rotation of keys on regular basis helps you meet organizational security and compliance requirements.

###### Usage considerations

- This control applies only to AWS KMS symmetric-encryption, customer managed keys.

### Remediation for rule failure

Set `EnableKeyRotation` to `true` for AWS KMS symmetric-encryption keys.

The examples that follow show how to implement this remediation.

#### AWS KMS key - Example

AWS KMS customer managed key configured with key rotation activated. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "KMSKey": {
        "Type": "AWS::KMS::Key",
        "Properties": {
            "PendingWindowInDays": 7,
            "KeyPolicy": {
                "Version": "2012-10-17",
                "Id": "sample-policy",
                "Statement": [
                    {
                        "Sid": "Enable IAM User Permissions",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": {
                                "Fn::Sub": "arn:${AWS::Partition}:iam::${AWS::AccountId}:root"
                            }
                        },
                        "Action": "kms:*",
                        "Resource": "*"
                    }
                ]
            },
            "EnableKeyRotation": true
        }
    }
}

```

**YAML example**

```

KMSKey:
  Type: AWS::KMS::Key
  Properties:
    PendingWindowInDays: 7
    KeyPolicy:
      Version: 2012-10-17
      Id: sample-policy
      Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS: !Sub 'arn:${AWS::Partition}:iam::${AWS::AccountId}:root'
          Action: kms:*
          Resource: '*'
    EnableKeyRotation: true


```

### CT.KMS.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   kms_key_rotation_enabled_check
#
# Description:
#   This control checks whether key rotation is enabled for AWS KMS customer managed keys.
#
# Reports on:
#   AWS::KMS::Key
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
#       And: The input document does not contain any KMS key resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeySpec' is provided and is a value other than 'SYMMETRIC_DEFAULT'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeySpec' is not provided or is provided and is set to 'SYMMETRIC_DEFAULT'
#       And: 'EnableKeyRotation' is not provided
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeySpec' is not provided or is provided and is set to 'SYMMETRIC_DEFAULT'
#       And: 'EnableKeyRotation' is provided and is set to bool(false)
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeySpec' is not provided or is provided and is set to 'SYMMETRIC_DEFAULT'
#       And: 'EnableKeyRotation' is provided and is set to bool(true)
#      Then: PASS

#
# Constants
#
let KMS_KEY_TYPE = "AWS::KMS::Key"
let INPUT_DOCUMENT = this

#
# Assignments
#
let kms_keys = Resources.*[ Type == %KMS_KEY_TYPE ]

#
# Primary Rules
#
rule kms_key_rotation_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                         %kms_keys not empty {
    check(%kms_keys.Properties)
        <<
        [CT.KMS.PR.1]: Require any AWS KMS key to have rotation configured
        [FIX]: Set 'EnableKeyRotation' to 'true' for AWS KMS symmetric-encryption keys.
        >>
}

rule kms_key_rotation_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %KMS_KEY_TYPE) {
    check(%INPUT_DOCUMENT.%KMS_KEY_TYPE.resourceProperties)
        <<
        [CT.KMS.PR.1]: Require any AWS KMS key to have rotation configured
        [FIX]: Set 'EnableKeyRotation' to 'true' for AWS KMS symmetric-encryption keys.
        >>
}

#
# Parameterized Rules
#
rule check(kms_keys) {
    %kms_keys[
        # Scenario 2
        filter_is_kms_cmk_symmetric_key(this)
    ] {
        # Scenario 3, 4 and 5
        EnableKeyRotation exists
        EnableKeyRotation == true
    }
}

rule filter_is_kms_cmk_symmetric_key(kms_key) {
    %kms_key {
        KeySpec not exists or
        KeySpec == "SYMMETRIC_DEFAULT"
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


```

### CT.KMS.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  Key:
    Type: AWS::KMS::Key
    Properties:
      PendingWindowInDays: 7
      KeyPolicy:
        Version: 2012-10-17
        Id: example-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'
      EnableKeyRotation: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  Key:
    Type: AWS::KMS::Key
    Properties:
      PendingWindowInDays: 7
      KeyPolicy:
        Version: 2012-10-17
        Id: example-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'
      EnableKeyRotation: false


```

## [CT.KMS.PR.2] Require that an AWS Key Management Service asymmetric key with RSA key material used for encryption has a key length greater than 2048 bits

This control checks whether an AWS KMS asymmetric key with RSA key material, which is used for encryption and decryption, to use a key spec with a key length greater than 2048 bits (that is, a key spec other than `RSA_2048`).

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::KMS::Key`
- **AWS CloudFormation guard rule:**
  [CT.KMS.PR.2 rule specification](#ct-kms-pr-2-rule "#ct-kms-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.KMS.PR.2 rule specification](#ct-kms-pr-2-rule "#ct-kms-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.KMS.PR.2 example templates](#ct-kms-pr-2-templates "#ct-kms-pr-2-templates")

**Explanation**

AWS Control Tower recommends using an RSA key spec with a key length greater than 2048 bits, when you are using such keys for encryption and decryption. The key spec determines whether the KMS key is symmetric or asymmetric.
It also determines the type of key material, and the algorithms it supports. AWS KMS supports asymmetric KMS keys that represent a mathematically-related RSA or elliptic curve (ECC)
public and private key pair. A KMS key with an RSA key pair can be used for encryption and decryption, or for signing and verification (but not both). AWS KMS supports several key
lengths for different security requirements.

###### Usage considerations

- This control applies only to a KMS key with an RSA key spec, which is configured for encryption and decryption.

### Remediation for rule failure

For KMS keys with an RSA keyspec, which are configured for encryption and decryption (`KeyUsage` of `ENCRYPT_DECRYPT`), set the `KeySpec` parameter to a key spec other than `RSA_2048`.

The examples that follow show how to implement this remediation.

#### AWS KMS key - Example

An AWS KMS asymmetric key configured for encryption and decryption, with an `RSA_4096` key spec. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "Key": {
        "Type": "AWS::KMS::Key",
        "Properties": {
            "KeyPolicy": {
                "Version": "2012-10-17",
                "Id": "example-policy",
                "Statement": [
                    {
                        "Sid": "Enable IAM User Permissions",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": {
                                "Fn::Sub": "arn:${AWS::Partition}:iam::${AWS::AccountId}:root"
                            }
                        },
                        "Action": "kms:*",
                        "Resource": "*"
                    }
                ]
            },
            "KeyUsage": "ENCRYPT_DECRYPT",
            "KeySpec": "RSA_4096"
        }
    }
}

```

**YAML example**

```

Key:
  Type: AWS::KMS::Key
  Properties:
    KeyPolicy:
      Version: '2012-10-17		 	 	 '
      Id: example-policy
      Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS: !Sub 'arn:${AWS::Partition}:iam::${AWS::AccountId}:root'
          Action: kms:*
          Resource: '*'
    KeyUsage: ENCRYPT_DECRYPT
    KeySpec: RSA_4096


```

### CT.KMS.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Name:
#   kms_asymmetric_rsa_keyspec_check
#
# Description:
#   This control checks whether an AWS KMS asymmetric key with RSA key material, which is used for encryption and decryption, to use a key spec with a key length greater than 2048 bits (that is, a key spec other than 'RSA_2048').
#
# Reports on:
#   AWS::KMS::Key
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
#       And: The input document does not contain any KMS key resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeyUsage' has been provided and is a value other than 'ENCRYPT_DECRYPT'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeyUsage' has not been provided or has been provided and is set to 'ENCRYPT_DECRYPT'
#       And: 'KeySpec' has not been provided or has been provided and is set to a
#            key spec other than an RSA key spec (does not begin with 'RSA_')
#      Then: SKIP
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeyUsage' has not been provided or has been provided and is set to 'ENCRYPT_DECRYPT'
#       And: 'KeySpec' has been provided and is set to an RSA key spec (begins with 'RSA_')
#       And: 'KeySpec' has been set to a disallowed RSA key spec ('RSA_2048')
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'KeyUsage' has not been provided or has been provided and is set to 'ENCRYPT_DECRYPT'
#       And: 'KeySpec' has been provided and is set to an RSA key spec (begins with 'RSA_')
#       And: 'KeySpec' has not been set to a disallowed RSA key spec ('RSA_2048')
#      Then: PASS

#
# Constants
#
let KMS_KEY_TYPE = "AWS::KMS::Key"
let RSA_KEYSPEC_PATTERN = /^RSA_/
let ENCRYPTION_KEY_USAGE = "ENCRYPT_DECRYPT"
let DISALLOWED_RSA_KEYSPECS = [ "RSA_2048" ]
let INPUT_DOCUMENT = this

#
# Assignments
#
let kms_keys = Resources.*[ Type == %KMS_KEY_TYPE ]

#
# Primary Rules
#
rule kms_asymmetric_rsa_keyspec_check when is_cfn_template(%INPUT_DOCUMENT)
                                           %kms_keys not empty {
    check(%kms_keys.Properties)
        <<
        [CT.KMS.PR.2]: Require that an AWS KMS asymmetric key with RSA key material used for encryption has a key length greater than 2048 bits
        [FIX]: For KMS keys with an RSA keyspec, which are configured for encryption and decryption ('KeyUsage' of 'ENCRYPT_DECRYPT'), set the 'KeySpec' parameter to a key spec other than 'RSA_2048'.
        >>
}

rule kms_asymmetric_rsa_keyspec_check when is_cfn_hook(%INPUT_DOCUMENT, %KMS_KEY_TYPE) {
    check(%INPUT_DOCUMENT.%KMS_KEY_TYPE.resourceProperties)
        <<
        [CT.KMS.PR.2]: Require that an AWS KMS asymmetric key with RSA key material used for encryption has a key length greater than 2048 bits
        [FIX]: For KMS keys with an RSA keyspec, which are configured for encryption and decryption ('KeyUsage' of 'ENCRYPT_DECRYPT'), set the 'KeySpec' parameter to a key spec other than 'RSA_2048'.
        >>
}

#
# Parameterized Rules
#
rule check(kms_keys) {
    %kms_keys[
        # Scenarios 2 and 3
        filter_is_kms_rsa_asymmetric_encryption_key(this)
    ] {
        # Scenario 4 and 5
        KeySpec exists
        KeySpec not in %DISALLOWED_RSA_KEYSPECS
    }
}

rule filter_is_kms_rsa_asymmetric_encryption_key(kms_key) {
    %kms_key {
        KeyUsage not exists or
        KeyUsage == %ENCRYPTION_KEY_USAGE

        KeySpec exists
        KeySpec == %RSA_KEYSPEC_PATTERN
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


```

### CT.KMS.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  Key:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: '2012-10-17		 	 	 '
        Id: example-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'
      KeyUsage: ENCRYPT_DECRYPT
      KeySpec: RSA_4096


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  Key:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: '2012-10-17		 	 	 '
        Id: example-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'
      KeyUsage: ENCRYPT_DECRYPT
      KeySpec: RSA_2048


```

## [CT.KMS.PR.3] Require an AWS Key Management Service key policy to have a statement that limits

creation of AWS KMS grants to AWS services

This control checks whether an AWS KMS key has an associated key policy statement that limits creation of
AWS KMS grants to AWS services only.

- **Control objective:** Enforce least privilege
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::KMS::Key`
- **AWS CloudFormation guard rule:**
  [CT.KMS.PR.3 rule specification](#ct-kms-pr-3-rule "#ct-kms-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.KMS.PR.3 rule specification](#ct-kms-pr-3-rule "#ct-kms-pr-3-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.KMS.PR.3 example templates](#ct-kms-pr-3-templates "#ct-kms-pr-3-templates")

**Explanation**

Users with permission to create grants for a KMS key (`kms:CreateGrant`) can use a grant to allow other users and roles, including AWS services, to use the KMS key (grantee principals). Grantee principals can be identities in your own AWS account, or identities from a different account or organization.

By denying creation of AWS KMS grants unless the request originates from an AWS service, you prevent grants from being assigned directly to principals other than AWS service principals, and you reduce the opportunities for grant misuse. The `kms:GrantIsForAWSResource` condition helps check whether the `CreateGrant` operation is being called by an AWS service integrated with AWS KMS, on behalf of another principal. The `aws:PrincipalIsAWSService` condition helps check whether the `CreateGrant` operation is being called directly by an AWS service principal.

###### Usage considerations

- If you must use additional conditions on your grants, or if you must issue AWS KMS grants directly to your IAM principals for a customer-managed key, **do not** enable this control.
  This control requires a policy statement that denies the creation of AWS KMS grants for your customer-managed KMS keys, if the request does not originate from an AWS service that's integrated with AWS KMS,
  or from an AWS service principal.

### Remediation for rule failure

Configure an AWS KMS policy statement that denies access to the `kms:CreateGrant` operation for all principals when the `kms:GrantIsForAWSResource` and `aws:PrincipalIsAWSService` conditions are both false, using the `BoolIfExists` condition operator.

The examples that follow show how to implement this remediation.

#### AWS KMS key - Example

An AWS KMS key, configured to deny creation of AWS KMS grants where the `CreateGrant` request does not originate from an AWS service principal. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "Key": {
        "Type": "AWS::KMS::Key",
        "Properties": {
            "KeyUsage": "ENCRYPT_DECRYPT",
            "KeySpec": "SYMMETRIC_DEFAULT",
            "KeyPolicy": {
                "Version": "2012-10-17",
                "Id": "sample-policy",
                "Statement": [
                    {
                        "Sid": "Enable IAM User Permissions",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": {
                                "Fn::Sub": "arn:${AWS::Partition}:iam::${AWS::AccountId}:root"
                            }
                        },
                        "Action": "kms:*",
                        "Resource": "*"
                    },
                    {
                        "Effect": "Deny",
                        "Action": "kms:CreateGrant",
                        "Resource": "*",
                        "Principal": "*",
                        "Condition": {
                            "BoolIfExists": {
                                "kms:GrantIsForAWSResource": "false",
                                "aws:PrincipalIsAWSService": "false"
                            }
                        }
                    }
                ]
            }
        }
    }
}

```

**YAML example**

```

Key:
  Type: AWS::KMS::Key
  Properties:
    KeyUsage: ENCRYPT_DECRYPT
    KeySpec: SYMMETRIC_DEFAULT
    KeyPolicy:
      Version: '2012-10-17		 	 	 '
      Id: sample-policy
      Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS: !Sub 'arn:${AWS::Partition}:iam::${AWS::AccountId}:root'
          Action: kms:*
          Resource: '*'
        - Effect: Deny
          Action: kms:CreateGrant
          Resource: '*'
          Principal: '*'
          Condition:
            BoolIfExists:
              kms:GrantIsForAWSResource: 'false'
              aws:PrincipalIsAWSService: 'false'


```

### CT.KMS.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Name:
#   kms_create_grant_aws_service_check
#
# Description:
#   This control checks whether an AWS KMS key has an associated key policy statement that limits creation of AWS KMS grants to AWS services only.
#
# Reports on:
#   AWS::KMS::Key
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
#       And: The input document does not contain any KMS key resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'Statement' in 'KeyPolicy' has not been provided or has been provided as an empty list
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'Statement' in 'KeyPolicy' has been provided as a non-empty list
#       And: 'Statement' in 'KeyPolicy' does not include a statement that denies all Principals ('*', AWS: '*')
#            create grant permissions ('kms:CreateGrant') on the KMS key (resource of '*')
#            when the conditions 'kms:GrantIsForAWSResource' and 'aws:PrincipalIsAWSService'
#            are both 'false' ('BoolIfExists' condition operator)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a KMS key resource
#       And: 'Statement' in 'KeyPolicy' has been provided as a non-empty list
#       And: 'Statement' in 'KeyPolicy' includes a statement that denies all Principals ('*', AWS: '*')
#            create grant permissions ('kms:CreateGrant') on the KMS key (resource of '*')
#            when the conditions 'kms:GrantIsForAWSResource' and 'aws:PrincipalIsAWSService'
#            are both 'false' ('BoolIfExists' condition operator)
#      Then: PASS

#
# Constants
#
let INPUT_DOCUMENT = this
let KMS_KEY_TYPE = "AWS::KMS::Key"
let KMS_GRANT_IS_FOR_AWS_RESOURCE_KEY_PATTERN = /^(?i)kms:GrantIsForAWSResource$/
let AWS_PRINCIPAL_IS_AWS_SERVICE_KEY_PATTERN = /^(?i)aws:PrincipalIsAWSService$/
let ALLOWED_KEY_PATTERNS = [/^(?i)kms:GrantIsForAWSResource$/, /^(?i)aws:PrincipalIsAWSService$/]
#
# Assignments
#
let kms_keys = Resources.*[ Type == %KMS_KEY_TYPE ]

#
# Primary Rules
#
rule kms_create_grant_aws_service_check when is_cfn_template(%INPUT_DOCUMENT)
                                             %kms_keys not empty {
    check(%kms_keys.Properties)
        <<
        [CT.KMS.PR.3]: Require an AWS KMS key policy to have a statement that limits creation of AWS KMS grants to AWS services
        [FIX]: Configure a KMS keys policy statement that denies access to the 'kms:CreateGrant' operation for all principals when the 'kms:GrantIsForAWSResource' and 'aws:PrincipalIsAWSService' conditions are both false, using the 'BoolIfExists' condition operator.
        >>
}

rule kms_create_grant_aws_service_check when is_cfn_hook(%INPUT_DOCUMENT, %KMS_KEY_TYPE) {
    check(%INPUT_DOCUMENT.%KMS_KEY_TYPE.resourceProperties)
        <<
        [CT.KMS.PR.3]: Require an AWS KMS key policy to have a statement that limits creation of AWS KMS grants to AWS services
        [FIX]: Configure a KMS key policy statement that denies access to the 'kms:CreateGrant' operation for all principals when the 'kms:GrantIsForAWSResource' and 'aws:PrincipalIsAWSService' conditions are both false, using the 'BoolIfExists' condition operator.
        >>
}

#
# Parameterized Rules
#
rule check(kms_keys) {
    %kms_keys {
        # Scenario 2
        KeyPolicy exists
        KeyPolicy is_struct

        KeyPolicy {
            Statement exists
            Statement is_list
            Statement not empty

            #Scenario 3 and 4
            some Statement[*] {
                check_statement_create_grant_aws_services_only(this)
            }
        }
    }
}

rule check_statement_create_grant_aws_services_only(statement) {
    %statement{
        check_all_required_statement_properties(this)

        Effect == "Deny"
        Action[*] in ["kms:CreateGrant"]

        Principal == "*" or
        Principal {
            AWS exists
            AWS == "*"
        }

        Resource[*] == "*"

        Condition is_struct
        struct_contains_only_allowed_keys(Condition, ["BoolIfExists"])

        Condition {
            BoolIfExists exists
            BoolIfExists is_struct

            struct_contains_only_allowed_keys(BoolIfExists, %ALLOWED_KEY_PATTERNS)
            struct_contains_key_with_value(BoolIfExists, %KMS_GRANT_IS_FOR_AWS_RESOURCE_KEY_PATTERN, "false")
            struct_contains_key_with_value(BoolIfExists, %AWS_PRINCIPAL_IS_AWS_SERVICE_KEY_PATTERN, "false")
        }
    }
}

rule check_all_required_statement_properties(statement) {
    %statement {
        Effect exists
        Action exists
        Principal exists
        Condition exists
        Resource exists
    }
}

rule struct_contains_only_allowed_keys(struct, allowed_keys) {
    let disallowed_keys = %struct[
        keys not in %allowed_keys
    ]
    %disallowed_keys empty
}

rule struct_contains_key_with_value(struct, key, value) {
    let key_present = %struct[
        keys == %key
    ]
    %key_present not empty
    %key_present == %value
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


```

### CT.KMS.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  Key:
    Type: AWS::KMS::Key
    Properties:
      KeyUsage: ENCRYPT_DECRYPT
      KeySpec: SYMMETRIC_DEFAULT
      KeyPolicy:
        Version: '2012-10-17		 	 	 '
        Id: example-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'
        - Effect: Deny
          Action: kms:CreateGrant
          Resource: '*'
          Principal: '*'
          Condition:
            BoolIfExists:
              kms:GrantIsForAWSResource: 'false'
              aws:PrincipalIsAWSService: 'false'


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  Key:
    Type: AWS::KMS::Key
    Properties:
      KeyUsage: ENCRYPT_DECRYPT
      KeySpec: SYMMETRIC_DEFAULT
      KeyPolicy:
        Version: '2012-10-17		 	 	 '
        Id: example-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'


```
