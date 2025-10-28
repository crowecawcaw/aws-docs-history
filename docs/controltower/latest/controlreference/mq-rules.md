# Amazon MQ controls

###### Topics

- [[CT.MQ.PR.1] Require an Amazon MQ ActiveMQ broker to use use active/standby deployment mode for high availability](#ct-mq-pr-1-description "#ct-mq-pr-1-description")
- [[CT.MQ.PR.2] Require an Amazon MQ Rabbit MQ broker to use Multi-AZ cluster mode for high availability](#ct-mq-pr-2-description "#ct-mq-pr-2-description")

## [CT.MQ.PR.1] Require an Amazon MQ ActiveMQ broker to use use active/standby deployment mode for high availability

This control checks whether an Amazon MQ ActiveMQ broker is configured in an active/standby deployment mode.

- **Control objective:** Improve resiliency, Improve availability
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AmazonMQ::Broker`
- **AWS CloudFormation guard rule:**
  [CT.MQ.PR.1 rule specification](#ct-mq-pr-1-rule "#ct-mq-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.MQ.PR.1 rule specification](#ct-mq-pr-1-rule "#ct-mq-pr-1-rule")
- For examples of PASS and FAIL AWS CloudFormation Templates related to
  this control, see:
  [CT.MQ.PR.1 example templates](#ct-mq-pr-1-templates "#ct-mq-pr-1-templates")

**Explanation**

Amazon MQ ActiveMQ active/standby deployment mode helps you achieve high availability for your Amazon MQ brokers across a single region. The Amazon MQ
active/standby deployment mode includes two broker instances, which are configured in a redundant pair across different availability zones.

###### Usage considerations

- This control applies only to Amazon MQ brokers with an engine type of ACTIVEMQ.

### Remediation for rule failure

For Amazon MQ brokers with an engine type of ACTIVEMQ, set the DeploymentMode property to ACTIVE_STANDBY_MULTI_AZ.

The examples that follow show how to implement this remediation.

#### Amazon MQ ActiveMQ Broker - Example

An Amazon MQ ActiveMQ broker configured in active/standby deployment mode. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "MQBroker": {
        "Type": "AWS::AmazonMQ::Broker",
        "Properties": {
            "AutoMinorVersionUpgrade": true,
            "BrokerName": "sample-broker",
            "EngineVersion": "5.17.2",
            "HostInstanceType": "mq.m5.large",
            "PubliclyAccessible": false,
            "Users": [
                {
                    "ConsoleAccess": true,
                    "Username": {
                        "Fn::Sub": "{{resolve:secretsmanager:${MQBrokerSecret}::username}}"
                    },
                    "Password": {
                        "Fn::Sub": "{{resolve:secretsmanager:${MQBrokerSecret}::password}}"
                    }
                }
            ],
            "EngineType": "ACTIVEMQ",
            "DeploymentMode": "ACTIVE_STANDBY_MULTI_AZ"
        }
    }
}

```

**YAML example**

```

MQBroker:
  Type: AWS::AmazonMQ::Broker
  Properties:
    AutoMinorVersionUpgrade: true
    BrokerName: sample-broker
    EngineVersion: 5.17.2
    HostInstanceType: mq.m5.large
    PubliclyAccessible: false
    Users:
      - ConsoleAccess: true
        Username: !Sub '{{resolve:secretsmanager:${MQBrokerSecret}::username}}'
        Password: !Sub '{{resolve:secretsmanager:${MQBrokerSecret}::password}}'
    EngineType: ACTIVEMQ
    DeploymentMode: ACTIVE_STANDBY_MULTI_AZ


```

### CT.MQ.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   mq_active_deployment_mode_check
#
# Description:
#   This control checks whether an Amazon MQ ActiveMQ broker is configured in an active/standby deployment mode.
#
# Reports on:
#   AWS::AmazonMQ::Broker
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
#       And: The input document does not contain any Amazon MQ broker resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon MQ broker resource
#       And: 'EngineType' has been provided and is equal to a value other than 'ACTIVEMQ'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon MQ broker resource
#       And: 'EngineType' has been provided and set to 'ACTIVEMQ'
#       And: 'DeploymentMode' has not been provided or has been provided and set to a value other
#            than 'ACTIVE_STANDBY_MULTI_AZ'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon MQ broker resource
#       And: 'EngineType' has been provided and set to 'ACTIVEMQ'
#       And: 'DeploymentMode' has been provided and set to 'ACTIVE_STANDBY_MULTI_AZ'
#      Then: PASS

#
# Constants
#
let MQ_BROKER_TYPE = "AWS::AmazonMQ::Broker"
let ENGINES_WITH_CLUSTER_DEPLOYMENT_SUPPORT = ["ACTIVEMQ"]
let ALLOWED_DEPLOYMENT_MODES = ["ACTIVE_STANDBY_MULTI_AZ"]
let INPUT_DOCUMENT = this

#
# Assignments
#
let mq_brokers = Resources.*[ Type == %MQ_BROKER_TYPE ]

#
# Primary Rules
#
rule mq_active_deployment_mode_check when is_cfn_template(%INPUT_DOCUMENT)
                                          %mq_brokers not empty {
    check(%mq_brokers.Properties)
        <<
        [CT.MQ.PR.1]: Require an Amazon MQ ActiveMQ broker to use use active/standby deployment mode for high availability
        [FIX]: For Amazon MQ brokers with an engine type of ACTIVEMQ, set the DeploymentMode property to ACTIVE_STANDBY_MULTI_AZ.
        >>
}

rule mq_active_deployment_mode_check when is_cfn_hook(%INPUT_DOCUMENT, %MQ_BROKER_TYPE) {
    check(%INPUT_DOCUMENT.%MQ_BROKER_TYPE.resourceProperties)
        <<
        [CT.MQ.PR.1]: Require an Amazon MQ ActiveMQ broker to use use active/standby deployment mode for high availability
        [FIX]: For Amazon MQ brokers with an engine type of ACTIVEMQ, set the DeploymentMode property to ACTIVE_STANDBY_MULTI_AZ.
        >>
}

#
# Parameterized Rules
#
rule check(mq_broker) {
    %mq_broker [
        # Scenario 2
        filter_engine(this)
    ] {
        # Scenarios 3 and 4
        DeploymentMode exists
        DeploymentMode in %ALLOWED_DEPLOYMENT_MODES
    }
}

rule filter_engine(mq_broker) {
    %mq_broker {
        EngineType exists
        EngineType in %ENGINES_WITH_CLUSTER_DEPLOYMENT_SUPPORT
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

### CT.MQ.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  MQBrokerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: MQ broker secret
      GenerateSecretString:
        SecretStringTemplate: '{"username": "examplemqusername"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: ',:='
  MQBroker:
    Type: AWS::AmazonMQ::Broker
    Properties:
      AutoMinorVersionUpgrade: true
      BrokerName:
        Ref: AWS::StackName
      EngineVersion: 5.17.2
      HostInstanceType: mq.m5.large
      PubliclyAccessible: false
      Users:
      - ConsoleAccess: true
        Username:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::username}}'
        Password:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::password}}'
      EngineType: ACTIVEMQ
      DeploymentMode: ACTIVE_STANDBY_MULTI_AZ


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  MQBrokerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: MQ broker secret
      GenerateSecretString:
        SecretStringTemplate: '{"username": "examplemqusername"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: ',:='
  MQBroker:
    Type: AWS::AmazonMQ::Broker
    Properties:
      AutoMinorVersionUpgrade: true
      BrokerName:
        Ref: AWS::StackName
      EngineVersion: 5.17.2
      HostInstanceType: mq.m5.large
      PubliclyAccessible: false
      Users:
      - ConsoleAccess: true
        Username:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::username}}'
        Password:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::password}}'
      EngineType: ACTIVEMQ
      DeploymentMode: SINGLE_INSTANCE


```

## [CT.MQ.PR.2] Require an Amazon MQ Rabbit MQ broker to use Multi-AZ cluster mode for high availability

This control checks whether an Amazon MQ RabbitMQ broker is configured in a cluster deployment mode, to allow for high availability.

- **Control objective:** Improve resiliency, Improve availability
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AmazonMQ::Broker`
- **AWS CloudFormation guard rule:**
  [CT.MQ.PR.2 rule specification](#ct-mq-pr-2-rule "#ct-mq-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.MQ.PR.2 rule specification](#ct-mq-pr-2-rule "#ct-mq-pr-2-rule")
- For examples of PASS and FAIL AWS CloudFormation Templates related to
  this control, see:
  [CT.MQ.PR.2 example templates](#ct-mq-pr-2-templates "#ct-mq-pr-2-templates")

**Explanation**

Amazon MQ cluster deployments for RabbitMQ help you achieve high availability for your Amazon MQ brokers across a single region. RabbitMQ clusters include three broker instances,
which are configured in a cluster across different availability zones.

###### Usage considerations

- This control applies only to Amazon MQ brokers with an engine type of RABBITMQ.

### Remediation for rule failure

For Amazon MQ brokers with an engine type of RABBITMQ, set the DeploymentMode property to CLUSTER_MULTI_AZ.

The examples that follow show how to implement this remediation.

#### Amazon MQ RabbitMQ Broker - Example

An Amazon MQ RabbitMQ broker configured in a cluster deployment mode. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "MQBroker": {
        "Type": "AWS::AmazonMQ::Broker",
        "Properties": {
            "AutoMinorVersionUpgrade": true,
            "BrokerName": "sample-mq-broker",
            "EngineVersion": "3.10.10",
            "HostInstanceType": "mq.m5.large",
            "PubliclyAccessible": false,
            "Users": [
                {
                    "ConsoleAccess": true,
                    "Username": {
                        "Fn::Sub": "{{resolve:secretsmanager:${MQBrokerSecret}::username}}"
                    },
                    "Password": {
                        "Fn::Sub": "{{resolve:secretsmanager:${MQBrokerSecret}::password}}"
                    }
                }
            ],
            "EngineType": "RABBITMQ",
            "DeploymentMode": "CLUSTER_MULTI_AZ"
        }
    }
}

```

**YAML example**

```

MQBroker:
  Type: AWS::AmazonMQ::Broker
  Properties:
    AutoMinorVersionUpgrade: true
    BrokerName: sample-mq-broker
    EngineVersion: 3.10.10
    HostInstanceType: mq.m5.large
    PubliclyAccessible: false
    Users:
      - ConsoleAccess: true
        Username: !Sub '{{resolve:secretsmanager:${MQBrokerSecret}::username}}'
        Password: !Sub '{{resolve:secretsmanager:${MQBrokerSecret}::password}}'
    EngineType: RABBITMQ
    DeploymentMode: CLUSTER_MULTI_AZ


```

### CT.MQ.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   mq_rabbit_deployment_mode_check
#
# Description:
#   This control checks whether an Amazon MQ RabbitMQ broker is configured in a cluster deployment mode, to allow for high availability.
#
# Reports on:
#   AWS::AmazonMQ::Broker
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
#       And: The input document does not contain any Amazon MQ broker resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon MQ broker resource
#       And: 'EngineType' been provided and is equal to a value other than 'RABBITMQ'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon MQ broker resource
#       And: 'EngineType' been provided and is equal to 'RABBITMQ'
#       And: 'DeploymentMode' has not been provided or has been provided and set to a value other
#            than 'CLUSTER_MULTI_AZ'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon MQ broker resource
#       And: 'EngineType' been provided and is equal to 'RABBITMQ'
#       And: 'DeploymentMode' has been provided and set to 'CLUSTER_MULTI_AZ'
#      Then: PASS

#
# Constants
#
let MQ_BROKER_TYPE = "AWS::AmazonMQ::Broker"
let ENGINES_WITH_CLUSTER_DEPLOYMENT_SUPPORT = ["RABBITMQ"]
let ALLOWED_DEPLOYMENT_MODES = ["CLUSTER_MULTI_AZ"]
let INPUT_DOCUMENT = this

#
# Assignments
#
let mq_brokers = Resources.*[ Type == %MQ_BROKER_TYPE ]

#
# Primary Rules
#
rule mq_rabbit_deployment_mode_check when is_cfn_template(%INPUT_DOCUMENT)
                                          %mq_brokers not empty {
    check(%mq_brokers.Properties)
        <<
        [CT.MQ.PR.2]: Require an Amazon MQ Rabbit MQ broker to use Multi-AZ cluster mode for high availability
        [FIX]: For Amazon MQ brokers with an engine type of RABBITMQ, set the DeploymentMode property to CLUSTER_MULTI_AZ.
        >>
}

rule mq_rabbit_deployment_mode_check when is_cfn_hook(%INPUT_DOCUMENT, %MQ_BROKER_TYPE) {
    check(%INPUT_DOCUMENT.%MQ_BROKER_TYPE.resourceProperties)
        <<
        [CT.MQ.PR.2]: Require an Amazon MQ Rabbit MQ broker to use Multi-AZ cluster mode for high availability
        [FIX]: For Amazon MQ brokers with an engine type of RABBITMQ, set the DeploymentMode property to CLUSTER_MULTI_AZ.
        >>
}

#
# Parameterized Rules
#
rule check(mq_broker) {
    %mq_broker [
        # Scenario 2
        filter_engine(this)
    ] {
        # Scenarios 3 and 4
        DeploymentMode exists
        DeploymentMode in %ALLOWED_DEPLOYMENT_MODES
    }
}

rule filter_engine(mq_broker) {
    %mq_broker {
        EngineType exists
        EngineType in %ENGINES_WITH_CLUSTER_DEPLOYMENT_SUPPORT
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

### CT.MQ.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  MQBrokerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: MQ broker secret
      GenerateSecretString:
        SecretStringTemplate: '{"username": "examplemqusername"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: ',:='
  MQBroker:
    Type: AWS::AmazonMQ::Broker
    Properties:
      AutoMinorVersionUpgrade: true
      BrokerName:
        Ref: AWS::StackName
      EngineVersion: 3.10.10
      HostInstanceType: mq.m5.large
      PubliclyAccessible: false
      Users:
      - ConsoleAccess: true
        Username:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::username}}'
        Password:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::password}}'
      EngineType: RABBITMQ
      DeploymentMode: CLUSTER_MULTI_AZ


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  MQBrokerSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: MQ broker secret
      GenerateSecretString:
        SecretStringTemplate: '{"username": "examplemqusername"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: ',:='
  MQBroker:
    Type: AWS::AmazonMQ::Broker
    Properties:
      AutoMinorVersionUpgrade: true
      BrokerName:
        Ref: AWS::StackName
      EngineVersion: 3.10.10
      HostInstanceType: mq.m5.large
      PubliclyAccessible: false
      Users:
      - ConsoleAccess: true
        Username:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::username}}'
        Password:
          Fn::Sub: '{{resolve:secretsmanager:${MQBrokerSecret}::password}}'
      EngineType: RABBITMQ
      DeploymentMode: SINGLE_INSTANCE


```
