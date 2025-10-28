# AWS Glue controls

###### Topics

- [[CT.GLUE.PR.1] Require an AWS Glue job to have an associated
  security configuration](#ct-glue-pr-1-description "#ct-glue-pr-1-description")

## [CT.GLUE.PR.1] Require an AWS Glue job to have an associated

security configuration

This control checks whether an AWS Glue job has an associated security configuration.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Glue::Job`
- **AWS CloudFormation guard rule:**
  [CT.GLUE.PR.1 rule specification](#ct-glue-pr-1-rule "#ct-glue-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.GLUE.PR.1 rule specification](#ct-glue-pr-1-rule "#ct-glue-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.GLUE.PR.1 example templates](#ct-glue-pr-1-templates "#ct-glue-pr-1-templates")

**Explanation**

In AWS Glue, a security configuration contains the properties that are needed when you write
encrypted data. Security configurations for an AWS Glue job must be configured to specify how the data is encrypted at the Amazon S3 target.
Encryption helps protect the data from unauthorized access and exposure.

### Remediation for rule failure

Set the `SecurityConfiguration` parameter to the name of an AWS Glue security configuration.

The examples that follow show how to implement this remediation.

#### AWS Glue job - Example

An AWS Glue job configured with an associated security configuration. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "GlueJob": {
        "Type": "AWS::Glue::Job",
        "Properties": {
            "Command": {
                "Name": "glueetl",
                "ScriptLocation": "s3://example-glue-script-bucket/scripts"
            },
            "Name": "sample-glue-job",
            "Role": {
                "Ref": "IAMRole"
            },
            "GlueVersion": "2.0",
            "SecurityConfiguration": {
                "Ref": "GlueSecurityConfig"
            }
        }
    }
}

```

**YAML example**

```

GlueJob:
  Type: AWS::Glue::Job
  Properties:
    Command:
      Name: glueetl
      ScriptLocation: s3://example-glue-script-bucket/scripts
    Name: sample-glue-job
    Role: !Ref 'IAMRole'
    GlueVersion: '2.0'
    SecurityConfiguration: !Ref 'GlueSecurityConfig'


```

### CT.GLUE.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   glue_job_security_config_check
#
# Description:
#   This control checks whether an AWS Glue job has an associated security configuration.
#
# Reports on:
#   AWS::Glue::Job
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
#       And: The input document does not contain any AWS Glue job resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an AWS Glue job resource
#       And: 'SecurityConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an AWS Glue job resource
#       And: 'SecurityConfiguration 'has been provided as an empty string or invalid local
#            reference
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation Hook Document
#       And: The input document contains an AWS Glue job resource
#       And: 'SecurityConfiguration' has been provided as a non-empty string or valid
#            local reference to an AWS Glue security configuration resource
#      Then: PASS

#
# Constants
#
let INPUT_DOCUMENT = this
let GLUE_JOB_TYPE = "AWS::Glue::Job"

#
# Assignments
#
let glue_jobs = Resources.*[ Type == %GLUE_JOB_TYPE ]

#
# Primary Rules
#
rule glue_job_security_config_check when is_cfn_template(%INPUT_DOCUMENT)
                                         %glue_jobs not empty {
    check(%glue_jobs.Properties)
        <<
        [CT.GLUE.PR.1]: Require an AWS Glue job to have an associated security configuration
        [FIX]: Set the 'SecurityConfiguration' parameter to the name of an AWS Glue security configuration.
        >>
}

rule glue_job_security_config_check when is_cfn_hook(%INPUT_DOCUMENT, %GLUE_JOB_TYPE) {
    check(%INPUT_DOCUMENT.%GLUE_JOB_TYPE.resourceProperties)
        <<
        [CT.GLUE.PR.1]: Require an AWS Glue job to have an associated security configuration
        [FIX]: Set the 'SecurityConfiguration' parameter to the name of an AWS Glue security configuration.
        >>
}

#
# Parameterized Rules
#
rule check(glue_job) {
    %glue_job{
        # Scenario 2
        SecurityConfiguration exists
         # Scenario 3 and 4
        check_is_string_and_not_empty(SecurityConfiguration) or
        check_local_references(%INPUT_DOCUMENT, SecurityConfiguration, "AWS::Glue::SecurityConfiguration")
    }
}

#
# Utility Rules
#
rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}

rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}

rule check_local_references(doc, reference_properties, referenced_RESOURCE_TYPE) {
    %reference_properties {
        'Fn::GetAtt' {
            query_for_resource(%doc, this[0], %referenced_RESOURCE_TYPE)
                <<Local Stack reference was invalid>>
        } or Ref {
            query_for_resource(%doc, this, %referenced_RESOURCE_TYPE)
                <<Local Stack reference was invalid>>
        }
    }
}

rule query_for_resource(doc, resource_key, referenced_RESOURCE_TYPE) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
    %referenced_resource {
        Type == %referenced_RESOURCE_TYPE
    }
}


```

### CT.GLUE.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  IAMRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
        - Effect: "Allow"
          Principal:
            Service:
            - "glue.amazonaws.com"
          Action:
          - "sts:AssumeRole"
      Path: "/"
  Key:
    Type: AWS::KMS::Key
    Properties:
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
      KeySpec: SYMMETRIC_DEFAULT
      EnableKeyRotation: true
  GlueSecurityConfig:
    Type: AWS::Glue::SecurityConfiguration
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      EncryptionConfiguration:
        S3Encryptions:
        - KmsKeyArn:
            Fn::GetAtt: [Key, Arn]
          S3EncryptionMode: SSE-KMS
  GlueJob:
    Type: AWS::Glue::Job
    Properties:
      Command:
        Name: glueetl
        ScriptLocation: "s3://example-glue-script-bucket/scripts"
      Name:
        Fn::Sub: ${AWS::StackName}-example
      Role:
        Ref: IAMRole
      GlueVersion: "2.0"
      SecurityConfiguration:
        Ref: GlueSecurityConfig


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  IAMRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
        - Effect: "Allow"
          Principal:
            Service:
            - "glue.amazonaws.com"
          Action:
          - "sts:AssumeRole"
      Path: "/"
  GlueJob:
    Type: AWS::Glue::Job
    Properties:
      Command:
        Name: glueetl
        ScriptLocation: "s3://example-glue-script-bucket/scripts"
      Name:
        Fn::Sub: ${AWS::StackName}-example
      Role:
        Ref: IAMRole
      GlueVersion: "2.0"


```
