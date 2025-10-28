# Amazon CloudWatch controls

###### Topics

- [[CT.CLOUDWATCH.PR.1] Require an Amazon CloudWatch alarm to have an action configured for the alarm state](#ct-cloudwatch-pr-1-description "#ct-cloudwatch-pr-1-description")
- [[CT.CLOUDWATCH.PR.2] Require an Amazon CloudWatch log group to be retained for at least one year](#ct-cloudwatch-pr-2-description "#ct-cloudwatch-pr-2-description")
- [[CT.CLOUDWATCH.PR.3] Require an Amazon CloudWatch log group to be encrypted at rest with an AWS KMS key](#ct-cloudwatch-pr-3-description "#ct-cloudwatch-pr-3-description")
- [[CT.CLOUDWATCH.PR.4] Require an Amazon CloudWatch alarm to have actions activated](#ct-cloudwatch-pr-4-description "#ct-cloudwatch-pr-4-description")

## [CT.CLOUDWATCH.PR.1] Require an Amazon CloudWatch alarm to have an action configured for the alarm state

This control checks whether an Amazon CloudWatch alarm has at least one action configured for the alarm state.

- **Control objective:** Establish logging and monitoring
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::CloudWatch::Alarm`
- **AWS CloudFormation guard rule:**
  [CT.CLOUDWATCH.PR.1 rule specification](#ct-cloudwatch-pr-1-rule "#ct-cloudwatch-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.CLOUDWATCH.PR.1 rule specification](#ct-cloudwatch-pr-1-rule "#ct-cloudwatch-pr-1-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.CLOUDWATCH.PR.1 example templates](#ct-cloudwatch-pr-1-templates "#ct-cloudwatch-pr-1-templates")

**Explanation**

AWS Control Tower recommends configuring actions for alarms to alert you automatically when an alarm is in the alarm state and the monitored metric is outside the defined threshold. This configuration ensures that alarms are monitored, and that necessary actions are taken when the alarm is triggered. Monitoring alarms help you identify unusual activities and respond quickly to security and operational issues. You can specify the actions an alarm should take when it goes into OK, ALARM, and INSUFFICIENT_DATA states. The most common CloudWatch alarm action in the alarm state is to notify one or more users by sending a message to an Amazon Simple Notification Service (Amazon SNS) topic.

### Remediation for rule failure

Set `AlarmActions` to a list with one or more alarm action values.

The examples that follow show how to implement this remediation.

#### Amazon CloudWatch Alarm - Example

An Amazon CloudWatch alarm configured to notify an SNS topic when the CloudWatch alarm is in the alarm state. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "Alarm": {
        "Type": "AWS::CloudWatch::Alarm",
        "Properties": {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 1,
            "Period": 300,
            "Threshold": 1.0,
            "Namespace": "AWS/Lambda",
            "MetricName": "Errors",
            "TreatMissingData": "missing",
            "Statistic": "Sum",
            "DatapointsToAlarm": 1,
            "ActionsEnabled": true,
            "AlarmActions": [
                {
                    "Ref": "Topic"
                }
            ]
        }
    }
}

```

**YAML example**

```

Alarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    ComparisonOperator: GreaterThanOrEqualToThreshold
    EvaluationPeriods: 1
    Period: 300
    Threshold: 1.0
    Namespace: AWS/Lambda
    MetricName: Errors
    TreatMissingData: missing
    Statistic: Sum
    DatapointsToAlarm: 1
    ActionsEnabled: true
    AlarmActions:
      - !Ref 'Topic'


```

### CT.CLOUDWATCH.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   cloudwatch_alarm_action_check
#
# Description:
#   This control checks whether an Amazon CloudWatch alarm has at least one action configured for the alarm state.
#
# Reports on:
#   AWS::CloudWatch::Alarm
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
#       And: The input document does not contain any CloudWatch alarm resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch alarm resource
#       And: 'AlarmActions' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch alarm resource
#       And: 'AlarmActions' has been provided as an empty list
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation Hook Document
#       And: The input document contains a CloudWatch alarm resource
#       And: 'AlarmActions' has been provided as a non-empty list
#      Then: PASS

#
# Constants
#
let CLOUDWATCH_ALARM_TYPE = "AWS::CloudWatch::Alarm"
let INPUT_DOCUMENT = this

#
# Assignments
#
let cloudwatch_alarms = Resources.*[ Type == %CLOUDWATCH_ALARM_TYPE ]

#
# Primary Rules
#
rule cloudwatch_alarm_action_check when is_cfn_template(%INPUT_DOCUMENT)
                                        %cloudwatch_alarms not empty {
    check(%cloudwatch_alarms.Properties)
        <<
        [CT.CLOUDWATCH.PR.1]: Require an Amazon CloudWatch alarm to have an action configured for the alarm state
        [FIX]: Set 'AlarmActions' to a list with one or more alarm action values.
        >>
}

rule cloudwatch_alarm_action_check when is_cfn_hook(%INPUT_DOCUMENT, %CLOUDWATCH_ALARM_TYPE) {
    check(%INPUT_DOCUMENT.%CLOUDWATCH_ALARM_TYPE.resourceProperties)
        <<
        [CT.CLOUDWATCH.PR.1]: Require an Amazon CloudWatch alarm to have an action configured for the alarm state
        [FIX]: Set 'AlarmActions' to a list with one or more alarm action values.
        >>
}

#
# Parameterized Rules
#
rule check(cloudwatch_alarm){
    %cloudwatch_alarm {
        # Scenario 2
        AlarmActions exists
        # Scenarios 3 and 4
        AlarmActions is_list
        AlarmActions not empty
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

### CT.CLOUDWATCH.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  Topic:
    Type: AWS::SNS::Topic
    Properties: {}
  Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Threshold: 1.0
      Namespace: AWS/Lambda
      MetricName: Errors
      TreatMissingData: missing
      Statistic: Sum
      DatapointsToAlarm: 1
      ActionsEnabled: true
      AlarmActions:
      - Ref: Topic


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Threshold: 1.0
      Namespace: AWS/Lambda
      MetricName: Errors
      TreatMissingData: missing
      Statistic: Sum
      DatapointsToAlarm: 1
      ActionsEnabled: true


```

## [CT.CLOUDWATCH.PR.2] Require an Amazon CloudWatch log group to be retained for at least one year

This control checks whether an Amazon CloudWatch Log Group retention period is set to a value greater than or equal to 365 days.

- **Control objective:** Establish logging and monitoring
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Logs::LogGroup`
- **AWS CloudFormation guard rule:**
  [CT.CLOUDWATCH.PR.2 rule specification](#ct-cloudwatch-pr-2-rule "#ct-cloudwatch-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.CLOUDWATCH.PR.2 rule specification](#ct-cloudwatch-pr-2-rule "#ct-cloudwatch-pr-2-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.CLOUDWATCH.PR.2 example templates](#ct-cloudwatch-pr-2-templates "#ct-cloudwatch-pr-2-templates")

**Explanation**

Amazon CloudWatch Logs centralizes the logs from all of your systems, applications, and AWS services in a single, highly scalable service. You can use Amazon CloudWatch Logs to monitor, store, and retrieve your log files from Amazon EC2 instances, CloudTrail, Route 53, and other sources. Retaining your logs for at least one year can help you comply with log retention standards.

### Remediation for rule failure

Omit the field value of `RetentionInDays` to adopt the default retention setting of `Never expire`, or set `RetentionInDays` to an integer value greater than or equal to 365.

The examples that follow show how to implement this remediation.

#### Amazon CloudWatch Log Group - Example

An Amazon CloudWatch log group configured to retain logs for one year (365 days). The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LogGroup": {
        "Type": "AWS::Logs::LogGroup",
        "Properties": {
            "RetentionInDays": 365
        }
    }
}

```

**YAML example**

```

LogGroup:
  Type: AWS::Logs::LogGroup
  Properties:
    RetentionInDays: 365


```

### CT.CLOUDWATCH.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   cloudwatch_log_group_retention_period_check
#
# Description:
#   This control checks whether an Amazon CloudWatch Log Group retention period is set to a value greater than or equal to 365 days.
#
# Reports on:
#   AWS::Logs::LogGroup
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
#       And: The input document does not contain any CloudWatch log group resources
#     Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch log group resource
#       And: 'RetentionInDays' has been provided and set to a non integer value or
#            integer value less than 365
#     Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch log group resource
#       And: 'RetentionInDays' has not been provided
#     Then: PASS
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation Hook Document
#       And: The input document contains a CloudWatch log group resource
#       And: 'RetentionInDays' has been provided and set to an integer value greater than or equal to 365
#     Then: PASS

#
# Constants
#
let CLOUDWATCH_LOGS_TYPE = "AWS::Logs::LogGroup"
let MINIMUM_RETENTION_IN_DAYS = 365
let INPUT_DOCUMENT = this

#
# Assignments
#
let cloudwatch_log_groups = Resources.*[ Type == %CLOUDWATCH_LOGS_TYPE ]

#
# Primary Rules
#
rule cloudwatch_log_group_retention_period_check when is_cfn_template(%INPUT_DOCUMENT)
                                                      %cloudwatch_log_groups not empty {
    check(%cloudwatch_log_groups.Properties)
        <<
        [CT.CLOUDWATCH.PR.2]: Require an Amazon CloudWatch log group to be retained for at least one year
        [FIX]: Omit the field value of 'RetentionInDays' to adopt the default retention setting of 'Never expire', or set 'RetentionInDays' to an integer value greater than or equal to 365.
        >>
}

rule cloudwatch_log_group_retention_period_check when is_cfn_hook(%INPUT_DOCUMENT, %CLOUDWATCH_LOGS_TYPE) {
    check(%INPUT_DOCUMENT.%CLOUDWATCH_LOGS_TYPE.resourceProperties)
        <<
        [CT.CLOUDWATCH.PR.2]: Require an Amazon CloudWatch log group to be retained for at least one year
        [FIX]: Omit the field value of 'RetentionInDays' to adopt the default retention setting of 'Never expire', or set 'RetentionInDays' to an integer value greater than or equal to 365.
        >>
}

#
# Parameterized Rules
#
rule check(cloudwatch_log_group){
    %cloudwatch_log_group {
        # Scenario 3
        RetentionInDays not exists or

        # Scenarios 2 and 4
        RetentionInDays >= %MINIMUM_RETENTION_IN_DAYS
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

### CT.CLOUDWATCH.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      RetentionInDays: 365


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      RetentionInDays: 1


```

## [CT.CLOUDWATCH.PR.3] Require an Amazon CloudWatch log group to be encrypted at rest with an AWS KMS key

This control checks whether an Amazon CloudWatch Logs log group is encrypted at rest with an AWS KMS key

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Logs::LogGroup`
- **AWS CloudFormation guard rule:**
  [CT.CLOUDWATCH.PR.3 rule specification](#ct-cloudwatch-pr-3-rule "#ct-cloudwatch-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.CLOUDWATCH.PR.3 rule specification](#ct-cloudwatch-pr-3-rule "#ct-cloudwatch-pr-3-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.CLOUDWATCH.PR.3 example templates](#ct-cloudwatch-pr-3-templates "#ct-cloudwatch-pr-3-templates")

**Explanation**

Amazon CloudWatch Logs log groups are encrypted by default using server-side encryption. For added control over encryption keys, you can use customer-managed keys from AWS KMS. You have full control over these KMS keys, including establishing and maintaining their key policies, IAM policies, and grants, enabling and disabling the keys, rotating their cryptographic material, adding tags, creating aliases that refer to the KMS keys, and scheduling the KMS keys for deletion.

### Remediation for rule failure

Set `KmsKeyId` to the ARN of an AWS KMS customer-managed key configured with permissions that allow the CloudWatch service principal to use the key.

The examples that follow show how to implement this remediation.

#### Amazon CloudWatch Logs Group - Example

An Amazon CloudWatch log group configured to encrypt logs with an AWS KMS customer-managed key. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LogGroup": {
        "Type": "AWS::Logs::LogGroup",
        "Properties": {
            "KmsKeyId": {
                "Fn::GetAtt": [
                    "KMSKey",
                    "Arn"
                ]
            }
        }
    }
}

```

**YAML example**

```

LogGroup:
  Type: AWS::Logs::LogGroup
  Properties:
    KmsKeyId: !GetAtt 'KMSKey.Arn'


```

### CT.CLOUDWATCH.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   cloudwatch_log_group_encrypted_check
#
# Description:
#   This control checks whether an Amazon CloudWatch log group is encrypted at rest with an AWS KMS key
#
# Reports on:
#   AWS::Logs::LogGroup
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
#       And: The input document does not contain any CloudWatch log group resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch log group resource
#       And: 'KmsKeyId' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch log group resource
#       And: 'KmsKeyId' has been provided as an empty string or invalid local reference to a KMS Key
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch log group resource
#       And: 'KmsKeyId' has been provided as a non-empty string or valid local reference to a KMS Key
#      Then: PASS

#
# Constants
#
let CLOUDWATCH_LOGS_TYPE = "AWS::Logs::LogGroup"
let INPUT_DOCUMENT = this

#
# Assignments
#
let cloudwatch_log_groups = Resources.*[ Type == %CLOUDWATCH_LOGS_TYPE ]

#
# Primary Rules
#
rule cloudwatch_log_group_encrypted_check when is_cfn_template(%INPUT_DOCUMENT)
                                               %cloudwatch_log_groups not empty {
    check(%cloudwatch_log_groups.Properties)
        <<
        [CT.CLOUDWATCH.PR.3]: Require an Amazon CloudWatch log group to be encrypted at rest with an AWS KMS key
        [FIX]: Set 'KmsKeyId' to the ARN of an AWS KMS customer managed key configured with permissions that allow the CloudWatch service principal to use the key.
        >>
}

rule cloudwatch_log_group_encrypted_check when is_cfn_hook(%INPUT_DOCUMENT, %CLOUDWATCH_LOGS_TYPE) {
    check(%INPUT_DOCUMENT.%CLOUDWATCH_LOGS_TYPE.resourceProperties)
        <<
        [CT.CLOUDWATCH.PR.3]: Require an Amazon CloudWatch log group to be encrypted at rest with an AWS KMS key
        [FIX]: Set 'KmsKeyId' to the ARN of an AWS KMS customer managed key configured with permissions that allow the CloudWatch service principal to use the key.
        >>
}

#
# Parameterized Rules
#
rule check(cloudwatch_log_group){
    %cloudwatch_log_group {
        # Scenario 2
        KmsKeyId exists
        # Scenario 3 and 4
        check_is_string_and_not_empty(KmsKeyId) or
        check_local_references(%INPUT_DOCUMENT, KmsKeyId, "AWS::KMS::Key")
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

rule query_for_resource(doc, resource_key, resource_type) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
    %referenced_resource {
        Type == %resource_type
    }
}


```

### CT.CLOUDWATCH.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  KMSKey:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: 2012-10-17
        Id: example-cloudwatch-logs-key-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: "*"
        - Sid: Enable Logs
          Effect: Allow
          Principal:
            Service:
              Fn::Sub: logs.${AWS::Region}.amazonaws.com
          Action:
          - kms:Encrypt*
          - kms:Decrypt*
          - kms:ReEncrypt*
          - kms:GenerateDataKey*
          - kms:Describe
          Resource: "*"
          Condition:
            ArnEquals:
              kms:EncryptionContext:aws:logs:arn:
                Fn::Sub: arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      KmsKeyId:
        Fn::GetAtt:
        - KMSKey
        - Arn


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties: {}


```

## [CT.CLOUDWATCH.PR.4] Require an Amazon CloudWatch alarm to have actions activated

This control checks whether an Amazon CloudWatch alarm has actions enabled.

- **Control objective:** Establish logging and monitoring
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::CloudWatch::Alarm`
- **AWS CloudFormation guard rule:**
  [CT.CLOUDWATCH.PR.4 rule specification](#ct-cloudwatch-pr-4-rule "#ct-cloudwatch-pr-4-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.CLOUDWATCH.PR.4 rule specification](#ct-cloudwatch-pr-4-rule "#ct-cloudwatch-pr-4-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.CLOUDWATCH.PR.4 example templates](#ct-cloudwatch-pr-4-templates "#ct-cloudwatch-pr-4-templates")

**Explanation**

Alarm actions automatically alert you when a monitored metric is outside the defined threshold. If the alarm action is deactivated, no actions are executed when the alarm changes state, so you won't be alerted to changes in monitored metrics. AWS Control Tower recommends activating CloudWatch alarm actions to help you respond quickly to security and operational issues.

### Remediation for rule failure

Set `ActionsEnabled` to `true` or do not provide the `ActionsEnabled` property.

The examples that follow show how to implement this remediation.

#### Amazon CloudWatch Alarm - Example

An Amazon CloudWatch alarm configured with alarm actions enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "Alarm": {
        "Type": "AWS::CloudWatch::Alarm",
        "Properties": {
            "AlarmActions": [
                {
                    "Ref": "Topic"
                }
            ],
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 1,
            "Period": 300,
            "Threshold": 1.0,
            "Namespace": "AWS/Lambda",
            "MetricName": "Errors",
            "TreatMissingData": "missing",
            "Statistic": "Sum",
            "DatapointsToAlarm": 1,
            "ActionsEnabled": true
        }
    }
}

```

**YAML example**

```

Alarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmActions:
      - !Ref 'Topic'
    ComparisonOperator: GreaterThanOrEqualToThreshold
    EvaluationPeriods: 1
    Period: 300
    Threshold: 1.0
    Namespace: AWS/Lambda
    MetricName: Errors
    TreatMissingData: missing
    Statistic: Sum
    DatapointsToAlarm: 1
    ActionsEnabled: true


```

### CT.CLOUDWATCH.PR.4 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   cloudwatch_alarm_action_enabled_check
#
# Description:
#   This control checks whether an Amazon CloudWatch alarm has actions enabled.
#
# Reports on:
#   AWS::CloudWatch::Alarm
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
#       And: The input document does not contain any CloudWatch alarm resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch alarm resource
#       And: 'ActionsEnabled' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a CloudWatch alarm resource
#       And: 'ActionsEnabled' has not been provided
#      Then: PASS
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation Hook Document
#       And: The input document contains a CloudWatch alarm resource
#       And: 'ActionsEnabled' has been provided with a value of bool(true)
#      Then: PASS

#
# Constants
#
let CLOUDWATCH_ALARM_TYPE = "AWS::CloudWatch::Alarm"
let INPUT_DOCUMENT = this

#
# Assignments
#
let cloudwatch_alarms = Resources.*[ Type == %CLOUDWATCH_ALARM_TYPE ]

#
# Primary Rules
#
rule cloudwatch_alarm_action_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                %cloudwatch_alarms not empty {
    check(%cloudwatch_alarms.Properties)
        <<
        [CT.CLOUDWATCH.PR.4]: Require an Amazon CloudWatch alarm to have actions activated
        [FIX]: Set 'ActionsEnabled' to 'true' or do not provide the 'ActionsEnabled' property.
        >>
}

rule cloudwatch_alarm_action_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %CLOUDWATCH_ALARM_TYPE) {
    check(%INPUT_DOCUMENT.%CLOUDWATCH_ALARM_TYPE.resourceProperties)
        <<
        [CT.CLOUDWATCH.PR.4]: Require an Amazon CloudWatch alarm to have actions activated
        [FIX]: Set 'ActionsEnabled' to 'true' or do not provide the 'ActionsEnabled' property.
        >>
}

#
# Parameterized Rules
#
rule check(cloudwatch_alarm){
    %cloudwatch_alarm {
        # Scenario 3
        ActionsEnabled not exists or
        # Scenarios 2 and 4
        ActionsEnabled == true
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

### CT.CLOUDWATCH.PR.4 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  Topic:
    Type: AWS::SNS::Topic
    Properties: {}
  Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmActions:
      - Ref: Topic
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Threshold: 1.0
      Namespace: AWS/Lambda
      MetricName: Errors
      TreatMissingData: missing
      Statistic: Sum
      DatapointsToAlarm: 1
      ActionsEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  Topic:
    Type: AWS::SNS::Topic
    Properties: {}
  Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmActions:
      - Ref: Topic
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Threshold: 1.0
      Namespace: AWS/Lambda
      MetricName: Errors
      TreatMissingData: missing
      Statistic: Sum
      DatapointsToAlarm: 1
      ActionsEnabled: false


```
