# Amazon Elastic Map Reduce (Amazon EMR) controls

###### Topics

- [[CT.EMR.PR.1] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3](#ct-emr-pr-1-description "#ct-emr-pr-1-description")
- [[CT.EMR.PR.2] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3 with an AWS KMS key](#ct-emr-pr-2-description "#ct-emr-pr-2-description")
- [[CT.EMR.PR.3] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured with EBS volume local disk encryption using an AWS KMS key](#ct-emr-pr-3-description "#ct-emr-pr-3-description")
- [[CT.EMR.PR.4] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data in transit](#ct-emr-pr-4-description "#ct-emr-pr-4-description")

## [CT.EMR.PR.1] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3

This control checks whether an Amazon EMR security configuration is configured to encrypt EMR File System (EMRFS) objects at rest in Amazon S3.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::EMR::SecurityConfiguration`
- **AWS CloudFormation guard rule:**
  [CT.EMR.PR.1 rule specification](#ct-emr-pr-1-rule "#ct-emr-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.EMR.PR.1 rule specification](#ct-emr-pr-1-rule "#ct-emr-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.EMR.PR.1 example templates](#ct-emr-pr-1-templates "#ct-emr-pr-1-templates")

**Explanation**

Amazon S3 encryption works with EMR File System (EMRFS) objects that are read from and written to Amazon S3. When you enable encryption at rest, you specify Amazon S3 server-side encryption (SSE) or client-side encryption (CSE) as the default encryption mode. Optionally, you can specify different encryption methods for individual buckets by using per bucket encryption overrides.

### Remediation for rule failure

In the `EncryptionConfiguration` parameter, set the value of `EnableAtRestEncryption` to true, and provide an `AtRestEncryptionConfiguration` configuration.

The examples that follow show how to implement this remediation.

#### Amazon EMR security configuration - Example

An Amazon EMR security configuration configured to encrypt EMR File System (EMRFS) objects at rest in Amazon S3. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "SecurityConfiguration": {
        "Type": "AWS::EMR::SecurityConfiguration",
        "Properties": {
            "SecurityConfiguration": {
                "EncryptionConfiguration": {
                    "EnableInTransitEncryption": false,
                    "EnableAtRestEncryption": true,
                    "AtRestEncryptionConfiguration": {
                        "S3EncryptionConfiguration": {
                            "EncryptionMode": "SSE-S3"
                        }
                    }
                }
            }
        }
    }
}

```

**YAML example**

```

SecurityConfiguration:
  Type: AWS::EMR::SecurityConfiguration
  Properties:
    SecurityConfiguration:
      EncryptionConfiguration:
        EnableInTransitEncryption: false
        EnableAtRestEncryption: true
        AtRestEncryptionConfiguration:
          S3EncryptionConfiguration:
            EncryptionMode: SSE-S3


```

### CT.EMR.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   emr_sec_config_encryption_at_rest_s3_check
#
# Description:
#   This control checks whether an Amazon EMR security configuration is configured to encrypt EMR File System (EMRFS) objects at rest in Amazon S3.
#
# Reports on:
#   AWS::EMR::SecurityConfiguration
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1`
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any EMR security configuration resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has not been provided
#            or has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has been provided as a struct
#       And: 'EncryptionMode' in 'AtRestEncryptionConfiguration.S3EncryptionConfiguration'
#            has not been provided or has been provided as an empty string
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has been provided as a struct
#       And: 'EncryptionMode' in 'AtRestEncryptionConfiguration.S3EncryptionConfiguration'
#            has been provided as a non-empty string
#      Then: PASS

#
# Constants
#
let EMR_SECURITY_CONFIGURATION_TYPE = "AWS::EMR::SecurityConfiguration"
let INPUT_DOCUMENT = this

#
# Assignments
#
let emr_security_configurations = Resources.*[ Type == %EMR_SECURITY_CONFIGURATION_TYPE ]

#
# Primary Rules
#
rule emr_sec_config_encryption_at_rest_s3_check when is_cfn_template(%INPUT_DOCUMENT)
                                                     %emr_security_configurations not empty {
    check(%emr_security_configurations.Properties)
        <<
        [CT.EMR.PR.1]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3
        [FIX]: In the 'EncryptionConfiguration' parameter, set the value of 'EnableAtRestEncryption' to true, and provide an 'AtRestEncryptionConfiguration' configuration.
        >>
}

rule emr_sec_config_encryption_at_rest_s3_check when is_cfn_hook(%INPUT_DOCUMENT, %EMR_SECURITY_CONFIGURATION_TYPE) {
    check(%INPUT_DOCUMENT.%EMR_SECURITY_CONFIGURATION_TYPE.resourceProperties)
        <<
        [CT.EMR.PR.1]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3
        [FIX]: In the 'EncryptionConfiguration' parameter, set the value of 'EnableAtRestEncryption' to true, and provide an 'AtRestEncryptionConfiguration' configuration.
        >>
}

#
# Parameterized Rules
#
rule check(emr_security_configuration) {
    %emr_security_configuration {
        SecurityConfiguration exists
        SecurityConfiguration is_struct

        SecurityConfiguration {
            # Scenario 2
            EncryptionConfiguration exists
            EncryptionConfiguration is_struct

            EncryptionConfiguration {
                # Scenario 3
                EnableAtRestEncryption exists
                EnableAtRestEncryption == true

                # Scenario 4
                AtRestEncryptionConfiguration exists
                AtRestEncryptionConfiguration is_struct

                # Scenarios 5 and 6
                AtRestEncryptionConfiguration {
                    S3EncryptionConfiguration exists
                    S3EncryptionConfiguration is_struct

                    S3EncryptionConfiguration {
                        EncryptionMode exists
                        check_is_string_and_not_empty(EncryptionMode)
                    }
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


```

### CT.EMR.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableInTransitEncryption: false
          EnableAtRestEncryption: true
          AtRestEncryptionConfiguration:
            S3EncryptionConfiguration:
              EncryptionMode: SSE-S3


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableAtRestEncryption: false
          EnableInTransitEncryption: false


```

## [CT.EMR.PR.2] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3 with an AWS KMS key

This control checks whether an Amazon EMR security configuration is configured to encrypt EMR File System (EMRFS) objects at rest in Amazon S3 with an AWS KMS key.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::EMR::SecurityConfiguration`
- **AWS CloudFormation guard rule:**
  [CT.EMR.PR.2 rule specification](#ct-emr-pr-2-rule "#ct-emr-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.EMR.PR.2 rule specification](#ct-emr-pr-2-rule "#ct-emr-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.EMR.PR.2 example templates](#ct-emr-pr-2-templates "#ct-emr-pr-2-templates")

**Explanation**

Amazon S3 encryption works with EMR File System (EMRFS) objects that are read from and written to Amazon S3. When you enable encyption at rest, you specify Amazon S3 server-side encryption (SSE) or client-side encryption (CSE) as the default encryption mode. Optionally, you can specify different encryption methods for individual buckets using per bucket encryption overrides.

### Remediation for rule failure

In the `EncryptionConfiguration` parameter, set `EnableAtRestEncryption` to true, and provide an `AtRestEncryptionConfiguration` configuration, with `EncryptionMode` set to `SSE-KMS` or `CSE-KMS`.

The examples that follow show how to implement this remediation.

#### Amazon EMR security configuration - Example

An Amazon EMR security configuration configured to encrypt EMR File System (EMRFS) objects at rest in Amazon S3 with AWS KMS. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "SecurityConfiguration": {
        "Type": "AWS::EMR::SecurityConfiguration",
        "Properties": {
            "SecurityConfiguration": {
                "EncryptionConfiguration": {
                    "EnableInTransitEncryption": false,
                    "EnableAtRestEncryption": true,
                    "AtRestEncryptionConfiguration": {
                        "S3EncryptionConfiguration": {
                            "EncryptionMode": "SSE-KMS",
                            "AwsKmsKey": {
                                "Fn::GetAtt": [
                                    "KmsKey",
                                    "Arn"
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
}

```

**YAML example**

```

SecurityConfiguration:
  Type: AWS::EMR::SecurityConfiguration
  Properties:
    SecurityConfiguration:
      EncryptionConfiguration:
        EnableInTransitEncryption: false
        EnableAtRestEncryption: true
        AtRestEncryptionConfiguration:
          S3EncryptionConfiguration:
            EncryptionMode: SSE-KMS
            AwsKmsKey: !GetAtt 'KmsKey.Arn'


```

### CT.EMR.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   emr_sec_config_encryption_at_rest_s3_kms_check
#
# Description:
#   This control checks whether an Amazon EMR security configuration is configured to encrypt EMR File System (EMRFS) objects at rest in Amazon S3 with an AWS KMS key.
#
# Reports on:
#   AWS::EMR::SecurityConfiguration
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
#       And: The input document does not contain any EMR security configuration resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has not been provided
#            or has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has been provided as a struct
#       And: 'EncryptionMode' in 'AtRestEncryptionConfiguration.S3EncryptionConfiguration'
#            has not been provided or has been provided and set to a value other than
#            a KMS-based encryption mode ('SSE-KMS', 'CSE-KMS')
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has been provided as a struct
#       And: 'EncryptionMode' in 'AtRestEncryptionConfiguration.S3EncryptionConfiguration'
#            has been provided and set to a KMS-based encryption mode ('SSE-KMS', 'CSE-KMS')
#       And: 'Overrides' in 'AtRestEncryptionConfiguration.S3EncryptionConfiguration' has been
#            provided as a non-empty list where one or more entries does not contain 'EncryptionMode',
#            or contains 'EncryptionMode' set to a value other than a KMS-based encryption mode
#            ('SSE-KMS', 'CSE-KMS')
#      Then: FAIL
#   Scenario: 7
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has been provided as a struct
#       And: 'EncryptionMode' in 'AtRestEncryptionConfiguration.S3EncryptionConfiguration'
#            has been provided and set to a KMS-based encryption mode ('SSE-KMS', 'CSE-KMS')
#       And: 'Overrides' in 'AtRestEncryptionConfiguration.S3EncryptionConfiguration' has not
#            been provided, or has been provided as an empty list, or list where every entry
#            contains 'EncryptionMode' set to a KMS-based encryption mode ('SSE-KMS', 'CSE-KMS')
#      Then: PASS

#
# Constants
#
let EMR_SECURITY_CONFIGURATION_TYPE = "AWS::EMR::SecurityConfiguration"
let S3_KMS_ENCRYPTION_MODES = [ "SSE-KMS", "CSE-KMS" ]
let INPUT_DOCUMENT = this

#
# Assignments
#
let emr_security_configurations = Resources.*[ Type == %EMR_SECURITY_CONFIGURATION_TYPE ]

#
# Primary Rules
#
rule emr_sec_config_encryption_at_rest_s3_kms_check when is_cfn_template(%INPUT_DOCUMENT)
                                                         %emr_security_configurations not empty {
    check(%emr_security_configurations.Properties)
        <<
        [CT.EMR.PR.2]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3 with an AWS KMS key
        [FIX]: In the 'EncryptionConfiguration' parameter, set 'EnableAtRestEncryption' to true, and provide an 'AtRestEncryptionConfiguration' configuration, with 'EncryptionMode' set to 'SSE-KMS' or 'CSE-KMS'.
        >>
}

rule emr_sec_config_encryption_at_rest_s3_kms_check when is_cfn_hook(%INPUT_DOCUMENT, %EMR_SECURITY_CONFIGURATION_TYPE) {
    check(%INPUT_DOCUMENT.%EMR_SECURITY_CONFIGURATION_TYPE.resourceProperties)
        <<
        [CT.EMR.PR.2]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data at rest in Amazon S3 with an AWS KMS key
        [FIX]: In the 'EncryptionConfiguration' parameter, set 'EnableAtRestEncryption' to true, and provide an 'AtRestEncryptionConfiguration' configuration, with 'EncryptionMode' set to 'SSE-KMS' or 'CSE-KMS'.
        >>
}

#
# Parameterized Rules
#
rule check(emr_security_configuration) {
    %emr_security_configuration {
        SecurityConfiguration exists
        SecurityConfiguration is_struct

        SecurityConfiguration {
            # Scenario 2
            EncryptionConfiguration exists
            EncryptionConfiguration is_struct

            EncryptionConfiguration {
                # Scenario 3
                EnableAtRestEncryption exists
                EnableAtRestEncryption == true

                # Scenario 4
                AtRestEncryptionConfiguration exists
                AtRestEncryptionConfiguration is_struct

                # Scenarios 5, 6 and 7
                AtRestEncryptionConfiguration {
                    S3EncryptionConfiguration exists
                    S3EncryptionConfiguration is_struct

                    let s3_encryption_configuration = S3EncryptionConfiguration

                    %s3_encryption_configuration {
                        check_kms_key_configuration(this)
                    }

                    %s3_encryption_configuration [
                        Overrides exists
                        Overrides is_list
                        Overrides not empty
                    ] {
                        Overrides[*] {
                            check_kms_key_configuration(this)
                        }
                    }
                }
            }
        }
    }
}

rule check_kms_key_configuration(s3_encryption_config) {
    %s3_encryption_config {
        EncryptionMode exists
        EncryptionMode in %S3_KMS_ENCRYPTION_MODES
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

### CT.EMR.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  KmsKey:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: 2012-10-17
        Id: example-key-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: "*"
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableInTransitEncryption: false
          EnableAtRestEncryption: true
          AtRestEncryptionConfiguration:
            S3EncryptionConfiguration:
              EncryptionMode: SSE-KMS
              AwsKmsKey:
                Fn::GetAtt:
                - KmsKey
                - Arn


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableInTransitEncryption: false
          EnableAtRestEncryption: false


```

## [CT.EMR.PR.3] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured with EBS volume local disk encryption using an AWS KMS key

This control checks whether Amazon EMR security configurations are configured with local disk encryption enabled, using EBS volume encryption and AWS KMS.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::EMR::SecurityConfiguration`
- **AWS CloudFormation guard rule:**
  [CT.EMR.PR.3 rule specification](#ct-emr-pr-3-rule "#ct-emr-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.EMR.PR.3 rule specification](#ct-emr-pr-3-rule "#ct-emr-pr-3-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.EMR.PR.3 example templates](#ct-emr-pr-3-templates "#ct-emr-pr-3-templates")

**Explanation**

For data at rest, EMR provides the option to encrypt local disk storage. The local storage consists of EC2 instance store volumes and the attached Amazon Elastic Block Store (EBS) storage, which are provisioned with your cluster. The EBS encryption option encrypts the EBS root device volume and its attached storage volumes. The EBS encryption option is available only when you specify AWS Key Management Service as your key provider. AWS Control Tower recommends using EBS encryption.

###### Usage considerations

- If you create a cluster in a Region where Amazon EC2 encryption of EBS volumes is enabled by default for your account, an EBS volume is encrypted even when local disk encryption is not enabled.
- With local disk encryption enabled in a security configuration, the Amazon EMR settings take precedence over the Amazon EC2 encryption-by-default settings for cluster EC2 instances.

### Remediation for rule failure

In the `EncryptionConfiguration` parameter, set the value of `EnableAtRestEncryption` to true, and provide an `AtRestEncryptionConfiguration` configuration, containing an `LocalDiskEncryptionConfiguration` configuration that sets `EnableEbsEncryption` to true.

The examples that follow show how to implement this remediation.

#### Amazon EMR security configuration - Example

An Amazon EMR security configuration configured with EBS encryption using AWS KMS. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "SecurityConfiguration": {
        "Type": "AWS::EMR::SecurityConfiguration",
        "Properties": {
            "SecurityConfiguration": {
                "EncryptionConfiguration": {
                    "EnableInTransitEncryption": false,
                    "EnableAtRestEncryption": true,
                    "AtRestEncryptionConfiguration": {
                        "LocalDiskEncryptionConfiguration": {
                            "EnableEbsEncryption": true,
                            "EncryptionKeyProviderType": "AwsKms",
                            "AwsKmsKey": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
                        }
                    }
                }
            }
        }
    }
}

```

**YAML example**

```

SecurityConfiguration:
  Type: AWS::EMR::SecurityConfiguration
  Properties:
    SecurityConfiguration:
      EncryptionConfiguration:
        EnableInTransitEncryption: false
        EnableAtRestEncryption: true
        AtRestEncryptionConfiguration:
          LocalDiskEncryptionConfiguration:
            EnableEbsEncryption: true
            EncryptionKeyProviderType: AwsKms
            AwsKmsKey: arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab


```

### CT.EMR.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   emr_sec_config_ebs_encryption_check
#
# Description:
#   This control checks whether Amazon EMR security configurations are configured with local disk encryption enabled, using EBS volume encryption and AWS KMS.
#
# Reports on:
#   AWS::EMR::SecurityConfiguration
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
#       And: The input document does not contain any EMR security configuration resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has not been provided
#            or has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has been provided as a struct
#       And: 'EnableEbsEncryption' in 'AtRestEncryptionConfiguration.LocalDiskEncryptionConfiguration'
#            has not been provided or has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableAtRestEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'AtRestEncryptionConfiguration' has been provided as a struct
#       And: 'EnableEbsEncryption' in 'AtRestEncryptionConfiguration.LocalDiskEncryptionConfiguration'
#            has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let EMR_SECURITY_CONFIGURATION_TYPE = "AWS::EMR::SecurityConfiguration"
let INPUT_DOCUMENT = this

#
# Assignments
#
let emr_security_configurations = Resources.*[ Type == %EMR_SECURITY_CONFIGURATION_TYPE ]

#
# Primary Rules
#
rule emr_sec_config_ebs_encryption_check when is_cfn_template(%INPUT_DOCUMENT)
                                              %emr_security_configurations not empty {
    check(%emr_security_configurations.Properties)
        <<
        [CT.EMR.PR.3]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured with EBS volume local disk encryption using an AWS KMS key
        [FIX]: In the 'EncryptionConfiguration' parameter, set the value of 'EnableAtRestEncryption' to true, and provide an 'AtRestEncryptionConfiguration' configuration, containing an 'LocalDiskEncryptionConfiguration' configuration that sets 'EnableEbsEncryption' to true.
        >>
}

rule emr_sec_config_ebs_encryption_check when is_cfn_hook(%INPUT_DOCUMENT, %EMR_SECURITY_CONFIGURATION_TYPE) {
    check(%INPUT_DOCUMENT.%EMR_SECURITY_CONFIGURATION_TYPE.resourceProperties)
        <<
        [CT.EMR.PR.3]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured with EBS volume local disk encryption using an AWS KMS key
        [FIX]: In the 'EncryptionConfiguration' parameter, set the value of 'EnableAtRestEncryption' to true, and provide an 'AtRestEncryptionConfiguration' configuration, containing an 'LocalDiskEncryptionConfiguration' configuration that sets 'EnableEbsEncryption' to true.
        >>
}

#
# Parameterized Rules
#
rule check(emr_security_configuration) {
    %emr_security_configuration {
        SecurityConfiguration exists
        SecurityConfiguration is_struct

        SecurityConfiguration {
            # Scenario 2
            EncryptionConfiguration exists
            EncryptionConfiguration is_struct

            EncryptionConfiguration {
                # Scenario 3
                EnableAtRestEncryption exists
                EnableAtRestEncryption == true

                # Scenario 4
                AtRestEncryptionConfiguration exists
                AtRestEncryptionConfiguration is_struct

                # Scenarios 5 and 6
                AtRestEncryptionConfiguration {
                    LocalDiskEncryptionConfiguration exists
                    LocalDiskEncryptionConfiguration is_struct

                    LocalDiskEncryptionConfiguration {
                        EnableEbsEncryption exists
                        EnableEbsEncryption == true
                    }
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


```

### CT.EMR.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  KmsKey:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: 2012-10-17
        Id: example-key-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: "*"
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableInTransitEncryption: false
          EnableAtRestEncryption: true
          AtRestEncryptionConfiguration:
            LocalDiskEncryptionConfiguration:
              EnableEbsEncryption: true
              EncryptionKeyProviderType: AwsKms
              AwsKmsKey:
                Fn::GetAtt:
                - KmsKey
                - Arn


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableInTransitEncryption: false
          EnableAtRestEncryption: false


```

## [CT.EMR.PR.4] Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data in transit

This control checks whether an Amazon EMR security configuration is configured to require encryption in transit.

- **Control objective:** Encrypt data in transit
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::EMR::SecurityConfiguration`
- **AWS CloudFormation guard rule:**
  [CT.EMR.PR.4 rule specification](#ct-emr-pr-4-rule "#ct-emr-pr-4-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.EMR.PR.4 rule specification](#ct-emr-pr-4-rule "#ct-emr-pr-4-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.EMR.PR.4 example templates](#ct-emr-pr-4-templates "#ct-emr-pr-4-templates")

**Explanation**

For data in transit, EMR security configurations provide you two options. You can create PEM certificates, zip them in a file, and reference them from Amazon S3, or you can implement a certificate custom provider in Java and specify the S3 path to the JAR. In either case, EMR downloads artifacts to each node in the cluster automatically, and later uses them to implement open-source, in-transit encryption features. For more information on how these certificates are used with different big data technologies, see Amazon EMR documentation.

###### Usage considerations

- Several encryption mechanisms are associated with in-transit encryption. These mechanisms are open-source features, they are application-specific, and they may vary by Amazon EMR release. For more information, see [Encryption in transit](../../../emr/latest/ManagementGuide/emr-data-encryption-options.md#emr-encryption-intransit "../../../emr/latest/ManagementGuide/emr-data-encryption-options.md#emr-encryption-intransit") in the _Amazon EMR Management Guide_.

### Remediation for rule failure

In the `EncryptionConfiguration` parameter, set the `EnableInTransitEncryption` parameter to true, and provide an `InTransitEncryptionConfiguration` configuration.

The examples that follow show how to implement this remediation.

#### Amazon EMR security configuration - Example

An Amazon EMR security configuration configured to require encryption of data in transit. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "SecurityConfiguration": {
        "Type": "AWS::EMR::SecurityConfiguration",
        "Properties": {
            "SecurityConfiguration": {
                "EncryptionConfiguration": {
                    "EnableAtRestEncryption": false,
                    "EnableInTransitEncryption": true,
                    "InTransitEncryptionConfiguration": {
                        "TLSCertificateConfiguration": {
                            "CertificateProviderType": "PEM",
                            "S3Object": "s3://MyConfigStore/artifacts/MyCerts.zip"
                        }
                    }
                }
            }
        }
    }
}

```

**YAML example**

```

SecurityConfiguration:
  Type: AWS::EMR::SecurityConfiguration
  Properties:
    SecurityConfiguration:
      EncryptionConfiguration:
        EnableAtRestEncryption: false
        EnableInTransitEncryption: true
        InTransitEncryptionConfiguration:
          TLSCertificateConfiguration:
            CertificateProviderType: PEM
            S3Object: s3://MyConfigStore/artifacts/MyCerts.zip


```

### CT.EMR.PR.4 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   emr_sec_config_encryption_in_transit_check
#
# Description:
#   This control checks whether an Amazon EMR security configuration is configured to require encryption in transit.
#
# Reports on:
#   AWS::EMR::SecurityConfiguration
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
#       And: The input document does not contain any EMR security configuration resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableInTransitEncryption' in 'EncryptionConfiguration' has not been provided
#            or has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableInTransitEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'InTransitEncryptionConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableInTransitEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'InTransitEncryptionConfiguration' has been provided as a struct
#       And: 'CertificateProviderType' in 'InTransitEncryptionConfiguration.TLSCertificateConfiguration'
#            has not been provided or has been provided and set to an empty string
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an EMR security configuration resource
#       And: 'EncryptionConfiguration' in 'SecurityConfiguration' has been provided as a struct
#       And: 'EnableInTransitEncryption' in 'EncryptionConfiguration' has been provided and
#            set to bool(true)
#       And: 'InTransitEncryptionConfiguration' has been provided as a struct
#       And: 'CertificateProviderType' in 'InTransitEncryptionConfiguration.TLSCertificateConfiguration'
#            has been provided and set to a non-empty string
#      Then: PASS

#
# Constants
#
let EMR_SECURITY_CONFIGURATION_TYPE = "AWS::EMR::SecurityConfiguration"
let INPUT_DOCUMENT = this

#
# Assignments
#
let emr_security_configurations = Resources.*[ Type == %EMR_SECURITY_CONFIGURATION_TYPE ]

#
# Primary Rules
#
rule emr_sec_config_encryption_in_transit_check when is_cfn_template(%INPUT_DOCUMENT)
                                                     %emr_security_configurations not empty {
    check(%emr_security_configurations.Properties)
        <<
        [CT.EMR.PR.4]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data in transit
        [FIX]: In the 'EncryptionConfiguration' parameter, set the 'EnableInTransitEncryption' parameter to true, and provide an 'InTransitEncryptionConfiguration' configuration.
        >>
}

rule emr_sec_config_encryption_in_transit_check when is_cfn_hook(%INPUT_DOCUMENT, %EMR_SECURITY_CONFIGURATION_TYPE) {
    check(%INPUT_DOCUMENT.%EMR_SECURITY_CONFIGURATION_TYPE.resourceProperties)
        <<
        [CT.EMR.PR.4]: Require that an Amazon Elastic MapReduce (EMR) security configuration is configured to encrypt data in transit
        [FIX]: In the 'EncryptionConfiguration' parameter, set the 'EnableInTransitEncryption' parameter to true, and provide an 'InTransitEncryptionConfiguration' configuration.
        >>
}

#
# Parameterized Rules
#
rule check(emr_security_configuration) {
    %emr_security_configuration {
        SecurityConfiguration exists
        SecurityConfiguration is_struct

        SecurityConfiguration {
            # Scenario 2
            EncryptionConfiguration exists
            EncryptionConfiguration is_struct

            EncryptionConfiguration {
                # Scenario 3
                EnableInTransitEncryption exists
                EnableInTransitEncryption == true

                # Scenario 4
                InTransitEncryptionConfiguration exists
                InTransitEncryptionConfiguration is_struct

                # Scenarios 5 and 6
                InTransitEncryptionConfiguration {
                    TLSCertificateConfiguration exists
                    TLSCertificateConfiguration is_struct

                    TLSCertificateConfiguration {
                        CertificateProviderType exists
                        check_is_string_and_not_empty(CertificateProviderType)
                    }
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


```

### CT.EMR.PR.4 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableAtRestEncryption: false
          EnableInTransitEncryption: true
          InTransitEncryptionConfiguration:
            TLSCertificateConfiguration:
              CertificateProviderType: PEM
              S3Object: s3://MyConfigStore/artifacts/MyCerts.zip


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  SecurityConfiguration:
    Type: AWS::EMR::SecurityConfiguration
    Properties:
      SecurityConfiguration:
        EncryptionConfiguration:
          EnableInTransitEncryption: false
          EnableAtRestEncryption: false


```
