# AWS Step Functions controls

###### Topics

- [[CT.STEPFUNCTIONS.PR.1] Require an AWS Step Functions state machine to have logging activated](#ct-stepfunctions-pr-1-description "#ct-stepfunctions-pr-1-description")
- [[CT.STEPFUNCTIONS.PR.2] Require an AWS Step Functions state machine to have AWS X-Ray tracing activated](#ct-stepfunctions-pr-2-description "#ct-stepfunctions-pr-2-description")

## [CT.STEPFUNCTIONS.PR.1] Require an AWS Step Functions state machine to have logging activated

This control checks whether an AWS Step Functions state machine has logging enabled.

- **Control objective:** Establish logging and monitoring
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::StepFunctions::StateMachine`
- **AWS CloudFormation guard rule:**
  [CT.STEPFUNCTIONS.PR.1 rule specification](#ct-stepfunctions-pr-1-rule "#ct-stepfunctions-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.STEPFUNCTIONS.PR.1 rule specification](#ct-stepfunctions-pr-1-rule "#ct-stepfunctions-pr-1-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.STEPFUNCTIONS.PR.1 example templates](#ct-stepfunctions-pr-1-templates "#ct-stepfunctions-pr-1-templates")

**Explanation**

Defining a logging configuration for your state machines allows you to track their execution history and results. This configuration allows you to track failed events that occur on a state machine, and this insight into errors can assist you when you're troubleshooting issues.

### Remediation for rule failure

In `LoggingConfiguration`, set `Level` to `ERROR` or `ALL`, and set `Destinations` to a list with one or more valid Amazon CloudWatch Logs log group ARNs.

The examples that follow show how to implement this remediation.

#### AWS Step Functions State Machine - Example

AWS Step Functions state machine configured to send logs to Amazon CloudWatch Logs. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "StateMachine": {
        "Type": "AWS::StepFunctions::StateMachine",
        "Properties": {
            "StateMachineType": "STANDARD",
            "DefinitionString": "{\"StartAt\": \"Sample\",\"States\": {\"Sample\": {\"Type\": \"Task\", \"Resource\":\"arn:aws:lambda:us-east-1:111122223333:function:SampleFunction\", \"End\": true}}}",
            "RoleArn": {
                "Fn::GetAtt": [
                    "StepFunctionExecutionRole",
                    "Arn"
                ]
            },
            "LoggingConfiguration": {
                "Level": "ALL",
                "Destinations": [
                    {
                        "CloudWatchLogsLogGroup": {
                            "LogGroupArn": {
                                "Fn::GetAtt": [
                                    "LogGroup",
                                    "Arn"
                                ]
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

StateMachine:
  Type: AWS::StepFunctions::StateMachine
  Properties:
    StateMachineType: STANDARD
    DefinitionString: '{"StartAt": "Sample","States": {"Sample": {"Type": "Task",
      "Resource":"arn:aws:lambda:us-east-1:111122223333:function:SampleFunction",
      "End": true}}}'
    RoleArn: !GetAtt 'StepFunctionExecutionRole.Arn'
    LoggingConfiguration:
      Level: ALL
      Destinations:
        - CloudWatchLogsLogGroup:
            LogGroupArn: !GetAtt 'LogGroup.Arn'


```

### CT.STEPFUNCTIONS.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   step_functions_state_machine_logging_enabled_check
#
# Description:
#   This control checks whether an AWS Step Functions state machine has logging enabled.
#
# Reports on:
#   AWS::StepFunctions::StateMachine
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
#       And: The input document does not contain any StepFunctions state machine resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'LoggingConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'LoggingConfiguration' has been provided
#       And: In 'LoggingConfiguration', 'Level' has not been provided or provided and set to a value other than
#            'ERROR' or 'ALL'
#       And: In 'LoggingConfiguration', 'Destinations' has not been provided or provided as an empty list or list
#            containing empty strings or non-valid local references
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'LoggingConfiguration' has been provided
#       And: In 'LoggingConfiguration', 'Level' has not been provided or provided and set to a value other than
#            'ERROR' or 'ALL'
#       And: In 'LoggingConfiguration', 'Destinations' has not been provided or provided as an empty list or list
#            containing empty strings or non-valid local references
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'LoggingConfiguration' has been provided
#       And: In 'LoggingConfiguration', 'Level' has not been provided or provided and set to a value other than
#            'ERROR' or 'ALL'
#       And: In 'LoggingConfiguration', 'Destinations' has been provided as a list containing non-empty strings or
#            valid local references
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'LoggingConfiguration' has been provided
#       And: In 'LoggingConfiguration', 'Level' has been provided and set to 'ERROR' or 'ALL'
#       And: In 'LoggingConfiguration', 'Destinations' has been provided as a list containing non-empty strings or
#            valid local references
#      Then: PASS

#
# Constants
#
let STEP_FUNCTIONS_STATE_MACHINE_TYPE = "AWS::StepFunctions::StateMachine"
let ALLOWED_LOGGING_LEVELS = [ "ERROR", "ALL" ]
let INPUT_DOCUMENT = this

#
# Assignments
#
let step_functions_state_machines = Resources.*[ Type == %STEP_FUNCTIONS_STATE_MACHINE_TYPE ]

#
# Primary Rules
#
rule step_functions_state_machine_logging_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                             %step_functions_state_machines not empty {
    check(%step_functions_state_machines.Properties)
        <<
        [CT.STEPFUNCTIONS.PR.1]: Require an AWS Step Functions state machine to have logging activated
        [FIX]: In 'LoggingConfiguration', set 'Level' to 'ERROR' or 'ALL', and set 'Destinations' to a list with one or more valid Amazon CloudWatch Logs log group ARNs.
        >>
}

rule step_functions_state_machine_logging_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %STEP_FUNCTIONS_STATE_MACHINE_TYPE) {
    check(%INPUT_DOCUMENT.%STEP_FUNCTIONS_STATE_MACHINE_TYPE.resourceProperties)
        <<
        [CT.STEPFUNCTIONS.PR.1]: Require an AWS Step Functions state machine to have logging activated
        [FIX]: In 'LoggingConfiguration', set 'Level' to 'ERROR' or 'ALL', and set 'Destinations' to a list with one or more valid Amazon CloudWatch Logs log group ARNs.
        >>
}

rule check(step_functions_state_machine) {
    %step_functions_state_machine {
        # Scenario 2
        LoggingConfiguration exists
        LoggingConfiguration is_struct

        LoggingConfiguration {
            # Scenarios 3, 4, 5 and 6
            Level exists
            Level in %ALLOWED_LOGGING_LEVELS

            Destinations exists
            Destinations is_list
            Destinations not empty

            Destinations[*] {
                CloudWatchLogsLogGroup exists
                CloudWatchLogsLogGroup is_struct

                CloudWatchLogsLogGroup {
                    LogGroupArn exists

                    check_is_string_and_not_empty(LogGroupArn) or
                    check_local_references(%INPUT_DOCUMENT, LogGroupArn, "AWS::Logs::LogGroup")
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

### CT.STEPFUNCTIONS.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  StepFunctionExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - states.amazonaws.com
          Action:
          - sts:AssumeRole
          Condition:
            ArnLike:
              aws:SourceArn:
                Fn::Sub: arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:*
            StringEquals:
              aws:SourceAccount:
                Ref: AWS::AccountId
      Path: /
      Policies:
      - PolicyName: StepFunctionLoggingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogDelivery
            - logs:GetLogDelivery
            - logs:UpdateLogDelivery
            - logs:DeleteLogDelivery
            - logs:ListLogDeliveries
            - logs:PutLogEvents
            - logs:PutResourcePolicy
            - logs:DescribeResourcePolicies
            - logs:DescribeLogGroups
            Resource: '*'
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties: {}
  StateMachine:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      StateMachineType: STANDARD
      DefinitionString: '{"StartAt": "Example","States": {"Example": {"Type": "Task", "Resource":"arn:aws:lambda:us-east-1:111122223333:function:ExampleFunction",
        "End": true}}}'
      RoleArn:
        Fn::GetAtt:
        - StepFunctionExecutionRole
        - Arn
      LoggingConfiguration:
        Level: ALL
        Destinations:
        - CloudWatchLogsLogGroup:
            LogGroupArn:
              Fn::GetAtt:
              - LogGroup
              - Arn


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  StepFunctionExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - states.amazonaws.com
          Action:
          - sts:AssumeRole
          Condition:
            ArnLike:
              aws:SourceArn:
                Fn::Sub: arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:*
            StringEquals:
              aws:SourceAccount:
                Ref: AWS::AccountId
      Path: /
      Policies:
      - PolicyName: StepFunctionLoggingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogDelivery
            - logs:GetLogDelivery
            - logs:UpdateLogDelivery
            - logs:DeleteLogDelivery
            - logs:ListLogDeliveries
            - logs:PutLogEvents
            - logs:PutResourcePolicy
            - logs:DescribeResourcePolicies
            - logs:DescribeLogGroups
            Resource: '*'
  StateMachine:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      StateMachineType: STANDARD
      DefinitionString: '{"StartAt": "Example","States": {"Example": {"Type": "Task", "Resource":"arn:aws:lambda:us-east-1:111122223333:function:ExampleFunction",
        "End": true}}}'
      RoleArn:
        Fn::GetAtt:
        - StepFunctionExecutionRole
        - Arn


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  StepFunctionExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - states.amazonaws.com
          Action:
          - sts:AssumeRole
          Condition:
            ArnLike:
              aws:SourceArn:
                Fn::Sub: arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:*
            StringEquals:
              aws:SourceAccount:
                Ref: AWS::AccountId
      Path: /
      Policies:
      - PolicyName: StepFunctionLoggingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogDelivery
            - logs:GetLogDelivery
            - logs:UpdateLogDelivery
            - logs:DeleteLogDelivery
            - logs:ListLogDeliveries
            - logs:PutLogEvents
            - logs:PutResourcePolicy
            - logs:DescribeResourcePolicies
            - logs:DescribeLogGroups
            Resource: '*'
  StateMachine:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      StateMachineType: STANDARD
      DefinitionString: '{"StartAt": "Example","States": {"Example": {"Type": "Task", "Resource":"arn:aws:lambda:us-east-1:111122223333:function:ExampleFunction",
        "End": true}}}'
      RoleArn:
        Fn::GetAtt:
        - StepFunctionExecutionRole
        - Arn
      LoggingConfiguration:
        Level: 'OFF'


```

## [CT.STEPFUNCTIONS.PR.2] Require an AWS Step Functions state machine to have AWS X-Ray tracing activated

This control checks whether an AWS Step Functions state machine has AWS X-Ray tracing enabled.

- **Control objective:** Establish logging and monitoring
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::StepFunctions::StateMachine`
- **AWS CloudFormation guard rule:**
  [CT.STEPFUNCTIONS.PR.2 rule specification](#ct-stepfunctions-pr-2-rule "#ct-stepfunctions-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.STEPFUNCTIONS.PR.2 rule specification](#ct-stepfunctions-pr-2-rule "#ct-stepfunctions-pr-2-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.STEPFUNCTIONS.PR.2 example templates](#ct-stepfunctions-pr-2-templates "#ct-stepfunctions-pr-2-templates")

**Explanation**

A tracing configuration allows your state machine to send tracing data to AWS X-Ray, so you can visualize the components of your state machine, identify performance bottlenecks, and troubleshoot requests that resulted in errors.

### Remediation for rule failure

In the `TracingConfiguration` property, set the value of `Enabled` to true.

The examples that follow show how to implement this remediation.

#### AWS Step Functions State Machine - Example

An AWS Step Functions state machine configured to send trace data to AWS X-Ray. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "StateMachine": {
        "Type": "AWS::StepFunctions::StateMachine",
        "Properties": {
            "StateMachineType": "STANDARD",
            "DefinitionString": "{\"StartAt\": \"Sample\",\"States\": {\"Sample\": {\"Type\": \"Task\", \"Resource\":\"arn:aws:lambda:us-east-1:111122223333:function:SampleFunction\", \"End\": true}}}",
            "RoleArn": {
                "Fn::GetAtt": [
                    "StepFunctionExecutionRole",
                    "Arn"
                ]
            },
            "LoggingConfiguration": {
                "Level": "ALL",
                "Destinations": [
                    {
                        "CloudWatchLogsLogGroup": {
                            "LogGroupArn": {
                                "Fn::GetAtt": [
                                    "LogGroup",
                                    "Arn"
                                ]
                            }
                        }
                    }
                ]
            },
            "TracingConfiguration": {
                "Enabled": true
            }
        }
    }
}

```

**YAML example**

```

StateMachine:
  Type: AWS::StepFunctions::StateMachine
  Properties:
    StateMachineType: STANDARD
    DefinitionString: '{"StartAt": "Sample","States": {"Sample": {"Type": "Task",
      "Resource":"arn:aws:lambda:us-east-1:111122223333:function:SampleFunction",
      "End": true}}}'
    RoleArn: !GetAtt 'StepFunctionExecutionRole.Arn'
    LoggingConfiguration:
      Level: ALL
      Destinations:
        - CloudWatchLogsLogGroup:
            LogGroupArn: !GetAtt 'LogGroup.Arn'
    TracingConfiguration:
      Enabled: true


```

### CT.STEPFUNCTIONS.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   step_functions_state_machine_tracing_enabled_check
#
# Description:
#   This control checks whether an AWS Step Functions state machine has AWS X-Ray tracing enabled.
#
# Reports on:
#   AWS::StepFunctions::StateMachine
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
#       And: The input document does not contain any StepFunctions state machine resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'TracingConfiguration' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'TracingConfiguration' has been provided
#       And: In 'TracingConfiguration', 'Enabled' has not been provided or provided and set to a value other
#            than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a StepFunctions state machine resource
#       And: 'TracingConfiguration' has been provided
#       And: In 'TracingConfiguration', 'Enabled' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let STEP_FUNCTIONS_STATE_MACHINE_TYPE = "AWS::StepFunctions::StateMachine"
let INPUT_DOCUMENT = this

#
# Assignments
#
let step_functions_state_machines = Resources.*[ Type == %STEP_FUNCTIONS_STATE_MACHINE_TYPE ]

#
# Primary Rules
#
rule step_functions_state_machine_tracing_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                             %step_functions_state_machines not empty {
    check(%step_functions_state_machines.Properties)
        <<
        [CT.STEPFUNCTIONS.PR.2]: Require an AWS Step Functions state machine to have AWS X-Ray tracing activated
        [FIX]: In the 'TracingConfiguration' property, set the value of 'Enabled' to true.
        >>
}

rule step_functions_state_machine_tracing_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %STEP_FUNCTIONS_STATE_MACHINE_TYPE) {
    check(%INPUT_DOCUMENT.%STEP_FUNCTIONS_STATE_MACHINE_TYPE.resourceProperties)
        <<
        [CT.STEPFUNCTIONS.PR.2]: Require an AWS Step Functions state machine to have AWS X-Ray tracing activated
        [FIX]: In the 'TracingConfiguration' property, set the value of 'Enabled' to true.
        >>
}

rule check(step_functions_state_machine) {
    %step_functions_state_machine {
        # Scenario 2
        TracingConfiguration exists
        TracingConfiguration is_struct

        TracingConfiguration {
            # Scenarios 3 and 4
            Enabled exists
            Enabled == true
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

### CT.STEPFUNCTIONS.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  StepFunctionExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - states.amazonaws.com
          Action:
          - sts:AssumeRole
          Condition:
            ArnLike:
              aws:SourceArn:
                Fn::Sub: arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:*
            StringEquals:
              aws:SourceAccount:
                Ref: AWS::AccountId
      Path: /
      Policies:
      - PolicyName: StepFunctionLoggingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogDelivery
            - logs:GetLogDelivery
            - logs:UpdateLogDelivery
            - logs:DeleteLogDelivery
            - logs:ListLogDeliveries
            - logs:PutLogEvents
            - logs:PutResourcePolicy
            - logs:DescribeResourcePolicies
            - logs:DescribeLogGroups
            Resource: '*'
      - PolicyName: StepFunctionTracingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - xray:PutTraceSegments
            - xray:PutTelemetryRecords
            - xray:GetSamplingRules
            - xray:GetSamplingTargets
            Resource: '*'
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties: {}
  StateMachine:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      StateMachineName:
        Fn::Sub: Example-StateMachine-${AWS::StackName}
      StateMachineType: STANDARD
      DefinitionString: '{"StartAt": "Example","States": {"Example": {"Type": "Task", "Resource":"arn:aws:lambda:us-east-1:111122223333:function:ExampleFunction",
        "End": true}}}'
      RoleArn:
        Fn::GetAtt:
        - StepFunctionExecutionRole
        - Arn
      LoggingConfiguration:
        Level: ALL
        Destinations:
        - CloudWatchLogsLogGroup:
            LogGroupArn:
              Fn::GetAtt:
              - LogGroup
              - Arn
      TracingConfiguration:
        Enabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  StepFunctionExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - states.amazonaws.com
          Action:
          - sts:AssumeRole
          Condition:
            ArnLike:
              aws:SourceArn:
                Fn::Sub: arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:*
            StringEquals:
              aws:SourceAccount:
                Ref: AWS::AccountId
      Path: /
      Policies:
      - PolicyName: StepFunctionLoggingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogDelivery
            - logs:GetLogDelivery
            - logs:UpdateLogDelivery
            - logs:DeleteLogDelivery
            - logs:ListLogDeliveries
            - logs:PutLogEvents
            - logs:PutResourcePolicy
            - logs:DescribeResourcePolicies
            - logs:DescribeLogGroups
            Resource: '*'
      - PolicyName: StepFunctionTracingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - xray:PutTraceSegments
            - xray:PutTelemetryRecords
            - xray:GetSamplingRules
            - xray:GetSamplingTargets
            Resource: '*'
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties: {}
  StateMachine:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      StateMachineName:
        Fn::Sub: Example-StateMachine-${AWS::StackName}
      StateMachineType: STANDARD
      DefinitionString: '{"StartAt": "Example","States": {"Example": {"Type": "Task", "Resource":"arn:aws:lambda:us-east-1:111122223333:function:ExampleFunction",
        "End": true}}}'
      RoleArn:
        Fn::GetAtt:
        - StepFunctionExecutionRole
        - Arn
      LoggingConfiguration:
        Level: ALL
        Destinations:
        - CloudWatchLogsLogGroup:
            LogGroupArn:
              Fn::GetAtt:
              - LogGroup
              - Arn
      TracingConfiguration:
        Enabled: false


```
