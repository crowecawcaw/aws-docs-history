# CloudFormation template Rules

syntax

The `Rules` section is an optional part of a CloudFormation template that enables
custom validation logic. When included, this section contains rule functions that validate
parameter values before CloudFormation creates or updates any resources.

Rules are useful when standard parameter constraints are insufficient. For example, when SSL
is enabled, both a certificate and domain name must be provided. A rule can ensure that these
dependencies are met.

## Syntax

The `Rules` section uses the following syntax:

### JSON

The `Rules` section of a template consists of the key name
`Rules`, followed by a single colon. You must use braces to enclose all rule
declarations. If you declare multiple rules, they're delimited by commas. For each rule, you
declare a logical name in quotation marks followed by a colon and braces that enclose the
rule condition and assertions.

```
{
    "Rules": {
        "`LogicalRuleName1`": {
            "RuleCondition": {
                "`rule-specific intrinsic function`": "`Value`"
            },
            "Assertions": [
                {
                    "Assert": {
                        "`rule-specific intrinsic function`": "`Value`"
                    },
                    "AssertDescription": "`Information about this assert`"
                },
                {
                    "Assert": {
                        "`rule-specific intrinsic function`": "`Value`"
                    },
                    "AssertDescription": "`Information about this assert`"
                }
            ]
        },
        "`LogicalRuleName2`": {
            "Assertions": [
                {
                    "Assert": {
                        "`rule-specific intrinsic function`": "`Value`"
                    },
                    "AssertDescription": "`Information about this assert`"
                }
            ]
        }
    }
}
```

### YAML

```
Rules:
  `LogicalRuleName1`:
    RuleCondition:
      `rule-specific intrinsic function`: `Value`
    Assertions:
      - Assert:
          `rule-specific intrinsic function`: `Value`
        AssertDescription: `Information about this assert`
      - Assert:
          `rule-specific intrinsic function`: `Value`
        AssertDescription: `Information about this assert`
  `LogicalRuleName2`:
    Assertions:
      - Assert:
          `rule-specific intrinsic function`: `Value`
        AssertDescription: `Information about this assert`
```

### Rules fields

The `Rules` section can include the following fields.

**Logical ID (also called _logical name_)**

A unique identifier for each rule.

**`RuleCondition` (optional)**

A property that determines when a rule takes effect. If you don't define a rule
condition, the rule's assertions always take effect. For each rule, you can define
only one rule condition.

**`Assertions` (required)**

One or more statements that specify the acceptable values for a particular
parameter.

**`Assert`**

A condition that must evaluate to `true`.

**`AssertDescription`**

A message displayed when an assertion fails.

## Rule-specific intrinsic

functions

To define your rules, you must use _rule-specific functions_, which are
functions that can only be used in the `Rules` section of a template. While these
functions can be nested, the final result of a rule condition or assertion must be either
`true` or `false`.

The following rule functions are available:

- [Fn::And](../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and "../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and")
- [Fn::Contains](../TemplateReference/intrinsic-function-reference-rules.md#fn-contains "../TemplateReference/intrinsic-function-reference-rules.md#fn-contains")
- [Fn::EachMemberEquals](../TemplateReference/intrinsic-function-reference-rules.md#fn-eachmemberequals "../TemplateReference/intrinsic-function-reference-rules.md#fn-eachmemberequals")
- [Fn::EachMemberIn](../TemplateReference/intrinsic-function-reference-rules.md#fn-eachmemberin "../TemplateReference/intrinsic-function-reference-rules.md#fn-eachmemberin")
- [Fn::Equals](../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-equals "../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-equals")
- [Fn::If](../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if "../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if")
- [Fn::Not](../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not "../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not")
- [Fn::Or](../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or "../TemplateReference/intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or")
- [Fn::RefAll](../TemplateReference/intrinsic-function-reference-rules.md#fn-refall "../TemplateReference/intrinsic-function-reference-rules.md#fn-refall")
- [Fn::ValueOf](../TemplateReference/intrinsic-function-reference-rules.md#fn-valueof "../TemplateReference/intrinsic-function-reference-rules.md#fn-valueof")
- [Fn::ValueOfAll](../TemplateReference/intrinsic-function-reference-rules.md#fn-valueofall "../TemplateReference/intrinsic-function-reference-rules.md#fn-valueofall")

These functions are used in the condition or assertions of a rule. The condition property
determines if CloudFormation applies the assertions. If the condition evaluates to
`true`, CloudFormation evaluates the assertions to verify whether a parameter value
is valid when a provisioned product is created or updated. If a parameter value is invalid,
CloudFormation does not create or update the stack. If the condition evaluates to
`false`, CloudFormation doesn't check the parameter value and proceeds with the stack
operation.

## Examples

###### Topics

- [Conditionally verify a parameter
  value](#template-constraint-rules-example-verify "#template-constraint-rules-example-verify")
- [Cross-parameter validation](#template-cross-parameter-rules-example "#template-cross-parameter-rules-example")

### Conditionally verify a parameter

value

In the following example, the two rules check the value of the `InstanceType`
parameter. Depending on the value of the environment parameter (`test` or
`prod`), the user must specify `t3.medium` or `t3.large`
for the `InstanceType` parameter. The `InstanceType` and
`Environment` parameters must be declared in the `Parameters`
section of the same template.

#### JSON

```
{
  "Rules": {
    "testInstanceType": {
      "RuleCondition": {
        "Fn::Equals": [
          {"Ref": "Environment"},
          "test"
        ]
      },
      "Assertions": [
        {
          "Assert": {
            "Fn::Contains": [
              ["t3.medium"],
              {"Ref": "InstanceType"}
            ]
          },
          "AssertDescription": "For a test environment, the instance type must be t3.medium"
        }
      ]
    },
    "prodInstanceType": {
      "RuleCondition": {
        "Fn::Equals": [
          {"Ref": "Environment"},
          "prod"
        ]
      },
      "Assertions": [
        {
          "Assert": {
            "Fn::Contains": [
              ["t3.large"],
              {"Ref": "InstanceType"}
            ]
          },
          "AssertDescription": "For a production environment, the instance type must be t3.large"
        }
      ]
    }
  }
}

```

#### YAML

```
Rules:
  testInstanceType:
    RuleCondition: !Equals
      - !Ref Environment
      - test
    Assertions:
      - Assert:
          'Fn::Contains':
            - - t3.medium
            - !Ref InstanceType
        AssertDescription: 'For a test environment, the instance type must be t3.medium'
  prodInstanceType:
    RuleCondition: !Equals
      - !Ref Environment
      - prod
    Assertions:
      - Assert:
          'Fn::Contains':
            - - t3.large
            - !Ref InstanceType
        AssertDescription: 'For a production environment, the instance type must be t3.large'
```

### Cross-parameter validation

The following sample templates demonstrate the use of rules for cross-parameter
validations. They create a sample website running on an Amazon EC2 Auto Scaling group behind a load balancer.
The website is available on port 80 or 443 depending on input parameters. The instances in
the Amazon EC2 Auto Scaling group can be configured to listen on any port (with 8888 as the default).

The rules in this template validate input parameters before stack creation. They verify
that all subnets belong to the specified VPC and ensure that when the `UseSSL`
parameter is set to `Yes`, both an SSL certificate ARN and hosted zone name are
provided.

###### Note

You will be billed for the AWS resources used if you create a stack from this
template.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "VpcId": {
      "Type": "AWS::EC2::VPC::Id",
      "Description": "VpcId of your existing Virtual Private Cloud (VPC)",
      "ConstraintDescription": "must be the VPC Id of an existing Virtual Private Cloud."
    },
    "Subnets": {
      "Type": "List<AWS::EC2::Subnet::Id>",
      "Description": "The list of SubnetIds in your Virtual Private Cloud (VPC)",
      "ConstraintDescription": "must be a list of at least two existing subnets associated with at least two different availability zones."
    },
    "InstanceType": {
      "Description": "WebServer EC2 instance type",
      "Type": "String",
      "Default": "t2.micro",
      "AllowedValues": ["t2.micro", "t3.micro"],
      "ConstraintDescription": "must be a valid EC2 instance type."
    },
    "KeyName": {
      "Description": "Name of an existing EC2 KeyPair to enable SSH access to the instances",
      "Type": "AWS::EC2::KeyPair::KeyName",
      "ConstraintDescription": "must be the name of an existing EC2 KeyPair."
    },
    "SSHLocation": {
      "Description": "The IP address range that can be used to SSH to the EC2 instances",
      "Type": "String",
      "MinLength": "9",
      "MaxLength": "18",
      "Default": "0.0.0.0/0",
      "AllowedPattern": "(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})",
      "ConstraintDescription": "must be a valid IP CIDR range of the form x.x.x.x/x."
    },
    "UseSSL": {
      "AllowedValues": ["Yes", "No"],
      "Default": "No",
      "Description": "Select \"Yes\" to implement SSL, \"No\" to skip (default).",
      "Type": "String"
    },
    "ALBSSLCertificateARN": {
      "Default": "",
      "Description": "[Optional] The ARN of the SSL certificate to be used for the Application Load Balancer",
      "Type": "String"
    },
    "HostedZoneName": {
      "AllowedPattern": "^$|(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])$",
      "Default": "",
      "Description": "[Optional] The domain name of a valid Hosted Zone on AWS.",
      "Type": "String"
    }
  },
  "Conditions": {
    "UseALBSSL": {"Fn::Equals": [{"Ref": "UseSSL"}, "Yes"]}
  },
  "Rules": {
    "SubnetsInVPC": {
      "Assertions": [
        {
          "Assert": {"Fn::EachMemberEquals": [{"Fn::ValueOf": ["Subnets", "VpcId"]}, {"Ref": "VpcId"}]},
          "AssertDescription": "All subnets must be in the VPC"
        }
      ]
    },
    "ValidateHostedZone": {
      "RuleCondition": {"Fn::Equals": [{"Ref": "UseSSL"}, "Yes"]},
      "Assertions": [
        {
          "Assert": {"Fn::Not": [{"Fn::Equals": [{"Ref": "ALBSSLCertificateARN"}, ""]}]},
          "AssertDescription": "ACM Certificate value cannot be empty if SSL is required"
        },
        {
          "Assert": {"Fn::Not": [{"Fn::Equals": [{"Ref": "HostedZoneName"}, ""]}]},
          "AssertDescription": "Route53 Hosted Zone Name is mandatory when SSL is required"
        }
      ]
    }
  },
  "Resources": {
    "WebServerGroup": {
      "Type": "AWS::AutoScaling::AutoScalingGroup",
      "Properties": {
        "VPCZoneIdentifier": {"Ref": "Subnets"},
        "LaunchTemplate": {
          "LaunchTemplateId": {"Ref": "LaunchTemplate"},
          "Version": {"Fn::GetAtt": ["LaunchTemplate","LatestVersionNumber"]}
        },
        "MinSize": "2",
        "MaxSize": "2",
        "TargetGroupARNs": [{"Ref": "ALBTargetGroup"}]
      },
      "CreationPolicy": {
        "ResourceSignal": {"Timeout": "PT15M"}
      },
      "UpdatePolicy": {
        "AutoScalingRollingUpdate": {
          "MinInstancesInService": "1",
          "MaxBatchSize": "1",
          "PauseTime": "PT15M",
          "WaitOnResourceSignals": true
        }
      }
    },
    "LaunchTemplate": {
      "Type": "AWS::EC2::LaunchTemplate",
      "Metadata": {
        "Comment": "Install a simple application",
        "AWS::CloudFormation::Init": {
          "config": {
            "packages": {"yum": {"httpd": []}},
            "files": {
              "/var/www/html/index.html": {
                "content": {"Fn::Join": ["\n", ["<h1>Congratulations, you have successfully launched the AWS CloudFormation sample.</h1>"]]},
                "mode": "000644",
                "owner": "root",
                "group": "root"
              },
              "/etc/cfn/cfn-hup.conf": {
                "content": {"Fn::Join": ["", [
                  "[main]\n",
                  "stack=", {"Ref": "AWS::StackId"}, "\n",
                  "region=", {"Ref": "AWS::Region"}, "\n"
                ]]},
                "mode": "000400",
                "owner": "root",
                "group": "root"
              },
              "/etc/cfn/hooks.d/cfn-auto-reloader.conf": {
                "content": {"Fn::Join": ["", [
                  "[cfn-auto-reloader-hook]\n",
                  "triggers=post.update\n",
                  "path=Resources.LaunchTemplate.Metadata.AWS::CloudFormation::Init\n",
                  "action=/opt/aws/bin/cfn-init -v ",
                  "         --stack ", {"Ref": "AWS::StackName"},
                  "         --resource LaunchTemplate ",
                  "         --region ", {"Ref": "AWS::Region"}, "\n",
                  "runas=root\n"
                ]]},
                "mode": "000400",
                "owner": "root",
                "group": "root"
              }
            },
            "services": {
              "sysvinit": {
                "httpd": {
                  "enabled": "true",
                  "ensureRunning": "true"
                },
                "cfn-hup": {
                  "enabled": "true",
                  "ensureRunning": "true",
                  "files": [
                    "/etc/cfn/cfn-hup.conf",
                    "/etc/cfn/hooks.d/cfn-auto-reloader.conf"
                  ]
                }
              }
            }
          }
        }
      },
      "Properties": {
        "LaunchTemplateName": {"Fn::Sub": "${AWS::StackName}-launch-template"},
        "LaunchTemplateData": {
          "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}",
          "SecurityGroupIds": [{"Ref": "InstanceSecurityGroup"}],
          "InstanceType": {"Ref": "InstanceType"},
          "KeyName": {"Ref": "KeyName"},
          "UserData": {
            "Fn::Base64": {"Fn::Join": ["", [
              "#!/bin/bash\n",
              "yum install -y aws-cfn-bootstrap\n",
              "/opt/aws/bin/cfn-init -v ",
              "         --stack ", {"Ref": "AWS::StackName"},
              "         --resource LaunchTemplate ",
              "         --region ", {"Ref": "AWS::Region"}, "\n",
              "/opt/aws/bin/cfn-signal -e $? ",
              "         --stack ", {"Ref": "AWS::StackName"},
              "         --resource WebServerGroup ",
              "         --region ", {"Ref": "AWS::Region"}, "\n"
            ]]}
          }
        }
      }
    },
    "ELBSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Allow access to the ELB",
        "VpcId": {"Ref": "VpcId"},
        "SecurityGroupIngress": [{
          "Fn::If": [
            "UseALBSSL",
            {
              "IpProtocol": "tcp",
              "FromPort": 443,
              "ToPort": 443,
              "CidrIp": "0.0.0.0/0"
            },
            {
              "IpProtocol": "tcp",
              "FromPort": 80,
              "ToPort": 80,
              "CidrIp": "0.0.0.0/0"
            }
          ]
        }]
      }
    },
    "ApplicationLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
      "Properties": {
        "Subnets": {"Ref": "Subnets"},
        "SecurityGroups": [{"Ref": "ELBSecurityGroup"}]
      }
    },
    "ALBListener": {
      "Type": "AWS::ElasticLoadBalancingV2::Listener",
      "Properties": {
        "DefaultActions": [{
          "Type": "forward",
          "TargetGroupArn": {"Ref": "ALBTargetGroup"}
        }],
        "LoadBalancerArn": {"Ref": "ApplicationLoadBalancer"},
        "Port": {"Fn::If": ["UseALBSSL", 443, 80]},
        "Protocol": {"Fn::If": ["UseALBSSL", "HTTPS", "HTTP"]},
        "Certificates": [{
          "Fn::If": [
            "UseALBSSL",
            {"CertificateArn": {"Ref": "ALBSSLCertificateARN"}},
            {"Ref": "AWS::NoValue"}
          ]
        }]
      }
    },
    "ALBTargetGroup": {
      "Type": "AWS::ElasticLoadBalancingV2::TargetGroup",
      "Properties": {
        "HealthCheckIntervalSeconds": 30,
        "HealthCheckTimeoutSeconds": 5,
        "HealthyThresholdCount": 3,
        "Port": 80,
        "Protocol": "HTTP",
        "UnhealthyThresholdCount": 5,
        "VpcId": {"Ref": "VpcId"}
      }
    },
    "InstanceSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Enable SSH access and HTTP access on the inbound port",
        "SecurityGroupIngress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "SourceSecurityGroupId": {"Fn::Select": [0, {"Fn::GetAtt": ["ApplicationLoadBalancer", "SecurityGroups"]}]}
          },
          {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "CidrIp": {"Ref": "SSHLocation"}
          }
        ],
        "VpcId": {"Ref": "VpcId"}
      }
    },
    "RecordSet": {
      "Type": "AWS::Route53::RecordSetGroup",
      "Condition": "UseALBSSL",
      "Properties": {
        "HostedZoneName": {"Fn::Join": ["", [{"Ref": "HostedZoneName"}, "."]]},
        "RecordSets": [{
          "Name": {"Fn::Join": ["", [
            {"Fn::Select": ["0", {"Fn::Split": [".", {"Fn::GetAtt": ["ApplicationLoadBalancer", "DNSName"]}]}]},
            ".",
            {"Ref": "HostedZoneName"},
            "."
          ]]},
          "Type": "A",
          "AliasTarget": {
            "DNSName": {"Fn::GetAtt": ["ApplicationLoadBalancer", "DNSName"]},
            "EvaluateTargetHealth": true,
            "HostedZoneId": {"Fn::GetAtt": ["ApplicationLoadBalancer", "CanonicalHostedZoneID"]}
          }
        }]
      }
    }
  },
  "Outputs": {
    "URL": {
      "Description": "URL of the website",
      "Value": {"Fn::Join": ["", [
        {"Fn::If": [
          "UseALBSSL",
          {"Fn::Join": ["", [
            "https://",
            {"Fn::Join": ["", [
              {"Fn::Select": ["0", {"Fn::Split": [".", {"Fn::GetAtt": ["ApplicationLoadBalancer", "DNSName"]}]}]},
              ".",
              {"Ref": "HostedZoneName"},
              "."
            ]]}
          ]]},
          {"Fn::Join": ["", [
            "http://",
            {"Fn::GetAtt": ["ApplicationLoadBalancer", "DNSName"]}
          ]]}
        ]}
      ]]}
    }
  }
}

```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: VpcId of your existing Virtual Private Cloud (VPC)
    ConstraintDescription: must be the VPC Id of an existing Virtual Private Cloud.
  Subnets:
    Type: List<AWS::EC2::Subnet::Id>
    Description: The list of SubnetIds in your Virtual Private Cloud (VPC)
    ConstraintDescription: >-
      must be a list of at least two existing subnets associated with at least
      two different availability zones. They should be residing in the selected
      Virtual Private Cloud.
  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - t3.micro
    ConstraintDescription: must be a valid EC2 instance type.
  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instances
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.
  SSHLocation:
    Description: The IP address range that can be used to SSH to the EC2 instances
    Type: String
    MinLength: '9'
    MaxLength: '18'
    Default: 0.0.0.0/0
    AllowedPattern: '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
  UseSSL:
    AllowedValues:
      - 'Yes'
      - 'No'
    ConstraintDescription: Select Yes to create a HTTPS Listener
    Default: 'No'
    Description: 'Select "Yes" to implement SSL, "No" to skip (default).'
    Type: String
  ALBSSLCertificateARN:
    Default: ''
    Description: >-
      [Optional] The ARN of the SSL certificate to be used for the Application
      Load Balancer
    Type: String
  HostedZoneName:
    AllowedPattern: >-
      ^$|(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$
    Default: ''
    Description: '[Optional] The domain name of a valid Hosted Zone on AWS.'
    Type: String
Conditions:
  UseALBSSL: !Equals
    - !Ref UseSSL
    - 'Yes'
Rules:
  SubnetsInVPC:
    Assertions:
      - Assert:
          'Fn::EachMemberEquals':
            - 'Fn::ValueOf':
                - Subnets
                - VpcId
            - Ref: VpcId
        AssertDescription: All subnets must be in the VPC
  ValidateHostedZone:
    RuleCondition: !Equals
      - !Ref UseSSL
      - 'Yes'
    Assertions:
      - Assert: !Not
          - !Equals
            - !Ref ALBSSLCertificateARN
            - ''
        AssertDescription: ACM Certificate value cannot be empty if SSL is required
      - Assert: !Not
          - !Equals
            - !Ref HostedZoneName
            - ''
        AssertDescription: Route53 Hosted Zone Name is mandatory when SSL is required
Resources:
  WebServerGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier: !Ref Subnets
      LaunchTemplate:
        LaunchTemplateId: !Ref LaunchTemplate
        Version: !GetAtt LaunchTemplate.LatestVersionNumber
      MinSize: '2'
      MaxSize: '2'
      TargetGroupARNs:
        - !Ref ALBTargetGroup
    CreationPolicy:
      ResourceSignal:
        Timeout: PT15M
    UpdatePolicy:
      AutoScalingRollingUpdate:
        MinInstancesInService: '1'
        MaxBatchSize: '1'
        PauseTime: PT15M
        WaitOnResourceSignals: 'true'
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Metadata:
      Comment: Install a simple application
      AWS::CloudFormation::Init:
        config:
          packages:
            yum:
              httpd: []
          files:
            /var/www/html/index.html:
              content: !Join
                - |+
                - - >-
                    <h1>Congratulations, you have successfully launched the AWS
                    CloudFormation sample.</h1>
              mode: '000644'
              owner: root
              group: root
            /etc/cfn/cfn-hup.conf:
              content: !Sub |
                [main]
                stack=${AWS::StackId}
                region=${AWS::Region}
              mode: '000400'
              owner: root
              group: root
            /etc/cfn/hooks.d/cfn-auto-reloader.conf:
              content: !Sub |-
                [cfn-auto-reloader-hook]
                triggers=post.update
                path=Resources.LaunchTemplate.Metadata.AWS::CloudFormation::Init
                action=/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate --region ${AWS::Region}
                runas=root
              mode: '000400'
              owner: root
              group: root
          services:
            sysvinit:
              httpd:
                enabled: 'true'
                ensureRunning: 'true'
              cfn-hup:
                enabled: 'true'
                ensureRunning: 'true'
                files:
                  - /etc/cfn/cfn-hup.conf
                  - /etc/cfn/hooks.d/cfn-auto-reloader.conf
    Properties:
      LaunchTemplateName: !Sub ${AWS::StackName}-launch-template
      LaunchTemplateData:
        ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}'
        SecurityGroupIds:
        - !Ref InstanceSecurityGroup
        InstanceType: !Ref InstanceType
        KeyName: !Ref KeyName
        UserData: !Base64
          Fn::Sub: |
            #!/bin/bash
            yum install -y aws-cfn-bootstrap
            /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate --region ${AWS::Region}
            /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
  ELBSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow access to the ELB
      VpcId: !Ref VpcId
      SecurityGroupIngress:
        - !If
          - UseALBSSL
          - IpProtocol: tcp
            FromPort: 443
            ToPort: 443
            CidrIp: 0.0.0.0/0
          - IpProtocol: tcp
            FromPort: 80
            ToPort: 80
            CidrIp: 0.0.0.0/0
  ApplicationLoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Subnets: !Ref Subnets
      SecurityGroups:
        - !Ref ELBSecurityGroup
  ALBListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref ALBTargetGroup
      LoadBalancerArn: !Ref ApplicationLoadBalancer
      Port: !If
        - UseALBSSL
        - 443
        - 80
      Protocol: !If
        - UseALBSSL
        - HTTPS
        - HTTP
      Certificates:
        - !If
          - UseALBSSL
          - CertificateArn: !Ref ALBSSLCertificateARN
          - !Ref 'AWS::NoValue'
  ALBTargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      HealthCheckIntervalSeconds: 30
      HealthCheckTimeoutSeconds: 5
      HealthyThresholdCount: 3
      Port: 80
      Protocol: HTTP
      UnhealthyThresholdCount: 5
      VpcId: !Ref VpcId
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access and HTTP access on the inbound port
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          SourceSecurityGroupId: !Select
            - 0
            - !GetAtt
              - ApplicationLoadBalancer
              - SecurityGroups
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: !Ref SSHLocation
      VpcId: !Ref VpcId
  RecordSet:
    Type: AWS::Route53::RecordSetGroup
    Condition: UseALBSSL
    Properties:
      HostedZoneName: !Join
        - ''
        - - !Ref HostedZoneName
          - .
      RecordSets:
        - Name: !Join
            - ''
            - - !Select
                - '0'
                - !Split
                  - .
                  - !GetAtt
                    - ApplicationLoadBalancer
                    - DNSName
              - .
              - !Ref HostedZoneName
              - .
          Type: A
          AliasTarget:
            DNSName: !GetAtt
              - ApplicationLoadBalancer
              - DNSName
            EvaluateTargetHealth: true
            HostedZoneId: !GetAtt
              - ApplicationLoadBalancer
              - CanonicalHostedZoneID
Outputs:
  URL:
    Description: URL of the website
    Value: !Join
      - ''
      - - !If
          - UseALBSSL
          - !Join
            - ''
            - - 'https://'
              - !Join
                - ''
                - - !Select
                    - '0'
                    - !Split
                      - .
                      - !GetAtt
                        - ApplicationLoadBalancer
                        - DNSName
                  - .
                  - !Ref HostedZoneName
                  - .
          - !Join
            - ''
            - - 'http://'
              - !GetAtt
                - ApplicationLoadBalancer
                - DNSName
```
