# Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling controls

###### Topics

- [[CT.AUTOSCALING.PR.1] Require an Amazon EC2 Auto Scaling group to have multiple Availability Zones](#ct-autoscaling-pr-1-description "#ct-autoscaling-pr-1-description")
- [[CT.AUTOSCALING.PR.2] Require an Amazon EC2 Auto Scaling group launch configuration to configure Amazon EC2 instances for IMDSv2](#ct-autoscaling-pr-2-description "#ct-autoscaling-pr-2-description")
- [[CT.AUTOSCALING.PR.4] Require an Amazon EC2 Auto Scaling group associated with an AWS Elastic Load Balancing (ELB) to have ELB health checks activated](#ct-autoscaling-pr-4-description "#ct-autoscaling-pr-4-description")
- [[CT.AUTOSCALING.PR.5] Require that an Amazon EC2 Auto Scaling group launch configuration does not have Amazon EC2 instances with public IP addresses](#ct-autoscaling-pr-5-description "#ct-autoscaling-pr-5-description")
- [[CT.AUTOSCALING.PR.6] Require any Amazon EC2 Auto Scaling groups to use multiple instance types](#ct-autoscaling-pr-6-description "#ct-autoscaling-pr-6-description")
- [[CT.AUTOSCALING.PR.8] Require an Amazon EC2 Auto Scaling group to have EC2 launch templates configured](#ct-autoscaling-pr-8-description "#ct-autoscaling-pr-8-description")
- [[CT.AUTOSCALING.PR.9] Require an Amazon EBS volume configured through an Amazon EC2 Auto Scaling launch configuration to encrypt data at rest](#ct-autoscaling-pr-9-description "#ct-autoscaling-pr-9-description")
- [[CT.AUTOSCALING.PR.10] Require an Amazon EC2 Auto Scaling group to use only AWS Nitro instance types when overriding a launch template](#ct-autoscaling-pr-10-description "#ct-autoscaling-pr-10-description")
- [[CT.AUTOSCALING.PR.11] Require only AWS Nitro instance types that support network traffic encryption between
  instances to be added to an Amazon EC2 Auto Scaling group, when overriding a launch template](#ct-autoscaling-pr-11-description "#ct-autoscaling-pr-11-description")

## [CT.AUTOSCALING.PR.1] Require an Amazon EC2 Auto Scaling group to have multiple Availability Zones

This control checks whether your Amazon EC2 Auto Scaling group spans multiple Availability Zones.

- **Control objective:** Improve availability
- **Implementation:** CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::AutoScalingGroup`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.1 rule specification](#ct-autoscaling-pr-1-rule "#ct-autoscaling-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.1 rule specification](#ct-autoscaling-pr-1-rule "#ct-autoscaling-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.AUTOSCALING.PR.1 example templates](#ct-autoscaling-pr-1-templates "#ct-autoscaling-pr-1-templates")

**Explanation**

Amazon EC2 Auto Scaling groups can be configured to use multiple Availability Zones. An Auto Scaling group with a single Availability Zone is preferred in some use cases, such as batch-jobs or when inter-AZ transfer costs need to be kept to a minimum. However, an Auto Scaling group that does not span multiple Availability Zones will not launch instances in another Availability Zone to compensate if the configured single Availability Zone becomes unavailable.

### Remediation for rule failure

Configure Auto Scaling groups with multiple Availability Zones.

The examples that follow show how to implement this remediation.

#### Auto Scaling group - Example

Auto Scaling group configured with multiple Availability Zones. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "LaunchTemplate": {
                "LaunchTemplateId": {
                    "Ref": "LaunchTemplate"
                },
                "Version": {
                    "Fn::GetAtt": "LaunchTemplate.LatestVersionNumber"
                }
            },
            "MaxSize": "1",
            "MinSize": "0",
            "DesiredCapacity": "1",
            "AvailabilityZones": [
                {
                    "Fn::Select": [
                        0,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                {
                    "Fn::Select": [
                        1,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                }
            ]
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    LaunchTemplate:
      LaunchTemplateId: !Ref 'LaunchTemplate'
      Version: !GetAtt 'LaunchTemplate.LatestVersionNumber'
    MaxSize: '1'
    MinSize: '0'
    DesiredCapacity: '1'
    AvailabilityZones:
      - !Select
        - 0
        - !GetAZs ''
      - !Select
        - 1
        - !GetAZs ''


```

### CT.AUTOSCALING.PR.1 rule specification

```

#####################################
##       Rule Specification        ##
#####################################

Rule Identifier:
  autoscaling_multiple_az_check

Description:
  Checks if Auto Scaling groups span multiple Availability Zones.

Reports on:
   AWS::AutoScaling::AutoScalingGroup

Evaluates:
  CloudFormation, CloudFormation hook

Rule Parameters:
  None

Scenarios:
  Scenario: 1
    Given: The input document is an CloudFormation or CloudFormation hook document
      And: The input document does not contain any Auto Scaling groups
     Then: SKIP
  Scenario: 2
    Given: The input document is an CloudFormation or CloudFormation hoo document
      And: The input document contains an Auto Scaling group resource
      And: 'AvailabilityZones' is not present on the Auto Scaling group resource
     Then: FAIL
  Scenario: 3
    Given: The input document is an CloudFormation or CloudFormation hook document
      And: The input document contains an Auto Scaling group resource
      And: 'AvailabilityZones' is present on the Auto Scaling group resource
      And: The number of 'AvailabilityZones' present is less than 2 (< 2) or the number of
           unique 'AvailabilityZones' provided is less than 2 (< 2)
     Then: FAIL
  Scenario: 4
    Given: The input document is an CloudFormation or CloudFormation Hook Document
      And: The input document contains an Auto Scaling group resource
      And: 'AvailabilityZones' is present on the Auto Scaling group resource
      And: The number of 'AvailabilityZones' present is greater than or equal to 2 (>= 2)
      And: At least two unique 'AvailabilityZones' have been provided
     Then: PASS


```

### CT.AUTOSCALING.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
        InstanceType: t3.micro
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      LaunchTemplate:
        LaunchTemplateId:
          Ref: LaunchTemplate
        Version:
          Fn::GetAtt: LaunchTemplate.LatestVersionNumber
      MaxSize: '1'
      MinSize: '0'
      DesiredCapacity: '1'
      AvailabilityZones:
      - Fn::Select:
        - 0
        - Fn::GetAZs: ""
      - Fn::Select:
        - 1
        - Fn::GetAZs: ""


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
        InstanceType: t3.micro
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      LaunchTemplate:
        LaunchTemplateId:
          Ref: LaunchTemplate
        Version:
          Fn::GetAtt: LaunchTemplate.LatestVersionNumber
      MaxSize: '1'
      MinSize: '0'
      DesiredCapacity: '1'
      AvailabilityZones:
      - Fn::Select:
        - 0
        - Fn::GetAZs: ""


```

## [CT.AUTOSCALING.PR.2] Require an Amazon EC2 Auto Scaling group launch configuration to configure Amazon EC2 instances for IMDSv2

This control checks whether an Amazon EC2 Auto Scaling launch configuration is configured to require the use of Instance Metadata Service Version 2 (IMDSv2).

- **Control objective:** Protect configurations
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::LaunchConfiguration`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.2 rule specification](#ct-autoscaling-pr-2-rule "#ct-autoscaling-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.2 rule specification](#ct-autoscaling-pr-2-rule "#ct-autoscaling-pr-2-rule")
- For examples of PASS and FAIL CloudFront Templates related to
  this control, see:
  [CT.AUTOSCALING.PR.2 example templates](#ct-autoscaling-pr-2-templates "#ct-autoscaling-pr-2-templates")

**Explanation**

IMDS provides data about your instance, which you can use to configure or manage the running instance.

Version 2 of the IMDS adds protections that weren't available in IMDSv1, to safeguard your EC2 instances further.

###### Usage considerations

- This control applies only to Amazon EC2 Auto Scaling launch configurations that allow access to instance metadata.

### Remediation for rule failure

Provide a `MetadataOptions` configuration and set the value of `HttpTokens` to `required`.

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Launch Configuration - Example

Amazon EC2 Auto Scaling launch configuration with IMDSv2 enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingLaunchConfiguration": {
        "Type": "AWS::AutoScaling::LaunchConfiguration",
        "Properties": {
            "ImageId": {
                "Ref": "LatestAmiId"
            },
            "InstanceType": "t3.micro",
            "MetadataOptions": {
                "HttpTokens": "required"
            }
        }
    }
}

```

**YAML example**

```

AutoScalingLaunchConfiguration:
  Type: AWS::AutoScaling::LaunchConfiguration
  Properties:
    ImageId: !Ref 'LatestAmiId'
    InstanceType: t3.micro
    MetadataOptions:
      HttpTokens: required


```

### CT.AUTOSCALING.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   autoscaling_launch_config_requires_imdsv2_check
#
# Description:
#   This control checks whether an Amazon EC2 Auto Scaling launch configuration is configured to require the use of Instance Metadata Service Version 2 (IMDSv2).
#
# Reports on:
#   AWS::AutoScaling::LaunchConfiguration
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#  Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any Autoscaling launch configuration resources
#      Then: SKIP
#  Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Autoscaling launch configuration resource
#       And: 'MetadataOptions' has been provided.
#       And: 'MetadataOptions.HttpEndpoint' has been provided is equal to 'disabled'
#      Then: SKIP
#  Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Autoscaling launch configuration resource
#       And: 'MetadataOptions.HttpEndpoint' has not been provided or has been provided and is equal to 'enabled'
#       And: 'MetadataOptions.HttpTokens' has not been provided
#      Then: FAIL
#  Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Autoscaling launch configuration resource
#       And: 'MetadataOptions' has been provided.
#       And: 'MetadataOptions.HttpEndpoint' has not been provided or has been provided and is equal to 'enabled'
#       And: 'MetadataOptions.HttpTokens' has been provided and set to a value other than 'required'
#      Then: FAIL
#  Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Autoscaling launch configuration resource
#       And: 'MetadataOptions' has been provided.
#       And: 'MetadataOptions.HttpEndpoint' has not been provided or has been provided and is equal to 'enabled'
#       And: 'MetadataOptions.HttpTokens' has been provided and set to 'required'
#      Then: PASS

#
# Constants
#
let AUTOSCALING_LAUNCH_CONFIGURATION_TYPE = "AWS::AutoScaling::LaunchConfiguration"
let INPUT_DOCUMENT = this

#
# Assignments
#
let autoscaling_launch_configurations = Resources.*[ Type == %AUTOSCALING_LAUNCH_CONFIGURATION_TYPE ]

#
# Primary Rules
#
rule autoscaling_launch_config_requires_imdsv2_check when is_cfn_template(%INPUT_DOCUMENT)
                                                          %autoscaling_launch_configurations not empty {
    check(%autoscaling_launch_configurations.Properties)
        <<
        [CT.AUTOSCALING.PR.2]: Require an Amazon EC2 Auto Scaling group launch configuration to configure Amazon EC2 instances for IMDSv2
            [FIX]: Provide a 'MetadataOptions' configuration and set the value of 'HttpTokens' to 'required'.
        >>
}

rule autoscaling_launch_config_requires_imdsv2_check when is_cfn_hook(%INPUT_DOCUMENT, %AUTOSCALING_LAUNCH_CONFIGURATION_TYPE) {
    check(%INPUT_DOCUMENT.%AUTOSCALING_LAUNCH_CONFIGURATION_TYPE.resourceProperties)
        <<
        [CT.AUTOSCALING.PR.2]: Require an Amazon EC2 Auto Scaling group launch configuration to configure Amazon EC2 instances for IMDSv2
            [FIX]: Provide a 'MetadataOptions' configuration and set the value of 'HttpTokens' to 'required'.
        >>
}

#
# Parameterized Rules
#
rule check(autoscaling_launch_configuration) {
    %autoscaling_launch_configuration [
        # Scenario 2
        filter_autoscaling_launch_configurations(this)
    ] {
        # Scenario 3, 4 and 5
        MetadataOptions exists
        MetadataOptions is_struct

        MetadataOptions {
            HttpTokens exists
            HttpTokens == "required"
        }
    }
}

rule filter_autoscaling_launch_configurations(autoscaling_launch_configurations) {
    %autoscaling_launch_configurations {
        MetadataOptions not exists or
        filter_metadata_options(this)
    }
}

rule filter_metadata_options(metadata_options) {
    %metadata_options {
        MetadataOptions is_struct
        MetadataOptions {
            HttpEndpoint not exists or
            HttpEndpoint == "enabled"
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

### CT.AUTOSCALING.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  AutoScalingLaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId:
        Ref: LatestAmiId
      InstanceType: t3.micro
      MetadataOptions:
        HttpTokens: required


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  AutoScalingLaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId:
        Ref: LatestAmiId
      InstanceType: t3.micro
      MetadataOptions:
        HttpTokens: optional


```

## [CT.AUTOSCALING.PR.4] Require an Amazon EC2 Auto Scaling group associated with an AWS Elastic Load Balancing (ELB) to have ELB health checks activated

This control checks whether your Amazon EC2 Auto Scaling groups that are associated with a load balancer are using
Elastic Load Balancing health checks.

- **Control objective:** Improve availability
- **Implementation:** CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::AutoScalingGroup`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.4 rule specification](#ct-autoscaling-pr-4-rule "#ct-autoscaling-pr-4-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.4 rule specification](#ct-autoscaling-pr-4-rule "#ct-autoscaling-pr-4-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [GitHub](https://github.com/aws-samples/aws-control-tower-samples/tree/main/samples/CT.AUTOSCALING.PR.4 "https://github.com/aws-samples/aws-control-tower-samples/tree/main/samples/CT.AUTOSCALING.PR.4")

**Explanation**

This configuration requirement ensures that the group can determine an instance's health based on additional tests provided by the load balancer. Using Elastic Load Balancing health checks can help support the availability of applications that use EC2 Auto Scaling groups.

###### Usage considerations

- This control only applies to Auto Scaling groups associated with a Classic Load Balancer or Target Group

### Remediation for rule failure

Configure Amazon EC2 Auto Scaling groups associated with an Elastic Load Balancing to use Elastic Load Balancing health checks.

The examples that follow show how to implement this remediation.

#### Auto Scaling group - Example One

Auto Scaling group with a Classic Load Balancer association and Elastic Load Balancing health checks. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "LaunchTemplate": {
                "LaunchTemplateId": {
                    "Ref": "LaunchTemplate"
                },
                "Version": {
                    "Fn::GetAtt": "LaunchTemplate.LatestVersionNumber"
                }
            },
            "MaxSize": "1",
            "MinSize": "0",
            "DesiredCapacity": "1",
            "LoadBalancerNames": [
                {
                    "Ref": "ElasticLoadBalancer"
                }
            ],
            "HealthCheckType": "ELB",
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ]
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    LaunchTemplate:
      LaunchTemplateId: !Ref 'LaunchTemplate'
      Version: !GetAtt 'LaunchTemplate.LatestVersionNumber'
    MaxSize: '1'
    MinSize: '0'
    DesiredCapacity: '1'
    LoadBalancerNames:
      - !Ref 'ElasticLoadBalancer'
    HealthCheckType: ELB
    VPCZoneIdentifier:
      - !Ref 'Subnet'


```

The examples that follow show how to implement this remediation.

#### Auto Scaling group - Example Two

Auto Scaling group with a Target Group association and Elastic Load Balancing health checks. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "LaunchTemplate": {
                "LaunchTemplateId": {
                    "Ref": "LaunchTemplate"
                },
                "Version": {
                    "Fn::GetAtt": "LaunchTemplate.LatestVersionNumber"
                }
            },
            "MaxSize": "1",
            "MinSize": "0",
            "DesiredCapacity": "1",
            "TargetGroupARNs": [
                {
                    "Ref": "ELBv2TargetGroup"
                }
            ],
            "HealthCheckType": "ELB",
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ]
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    LaunchTemplate:
      LaunchTemplateId: !Ref 'LaunchTemplate'
      Version: !GetAtt 'LaunchTemplate.LatestVersionNumber'
    MaxSize: '1'
    MinSize: '0'
    DesiredCapacity: '1'
    TargetGroupARNs:
      - !Ref 'ELBv2TargetGroup'
    HealthCheckType: ELB
    VPCZoneIdentifier:
      - !Ref 'Subnet'


```

### CT.AUTOSCALING.PR.4 rule specification

```

#####################################
##       Rule Specification        ##
#####################################

Rule Identifier:
  autoscaling_group_elb_healthcheck_required_check

Description:
  This control checks whether your Auto Scaling groups that are associated with a load balancer are using
  Elastic Load Balancing health checks.

Reports on:
  AWS::AutoScaling::AutoScalingGroup

Evaluates:
  AWS CloudFormation, AWS CloudFormation hook

Rule Parameters:
  None

Scenarios:
  Scenario: 1
    Given: The input document is an AWS CloudFormation or CloudFormation hook document
      And: The input document does not contain any Auto Scaling group
     Then: SKIP
  Scenario: 2
    Given: The input document is an AWS CloudFormation or CloudFormation hook document
      And: The input document contains an Auto Scaling group resource
      And: 'LoadBalancerNames' or 'TargetGroupARNs' are not present on the Auto Scaling group resource or empty lists
     Then: SKIP
  Scenario: 3
    Given: The input document is an AWS CloudFormation or CloudFormation hook document
      And: The input document contains an Auto Scaling group resource
      And: 'LoadBalancerNames' or 'TargetGroupARNs' are present on the Auto Scaling group with at least
           one configuration
      And: 'HealthCheckType' is not present
     Then: FAIL
  Scenario: 4
    Given: The input document is an AWS CloudFormation or CloudFormation hook document
      And: The input document contains an Auto Scaling group resource
      And: 'LoadBalancerNames' or 'TargetGroupARNs' are present on the Auto Scaling group with at least
           one configuration
      And: 'HealthCheckType' is present and set to a value other than 'ELB' (e.g. 'EC2')
     Then: FAIL
  Scenario: 5
    Given: The input document is an AWS CloudFormation or CloudFormation hook document
      And: The input document contains an Auto Scaling group resource
      And: 'LoadBalancerNames' or 'TargetGroupARNs' are present on the Auto Scaling group with at least
           one configuration
      And: 'HealthCheckType' is present and set to 'ELB'
     Then: PASS


```

## [CT.AUTOSCALING.PR.5] Require that an Amazon EC2 Auto Scaling group launch configuration does not have Amazon EC2 instances with public IP addresses

This control checks whether Amazon EC2 Auto Scaling groups have public IP addresses configured through Launch Configurations.

- **Control objective:** Limit network access
- **Implementation:** CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::LaunchConfiguration`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.5 rule specification](#ct-autoscaling-pr-5-rule "#ct-autoscaling-pr-5-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.5 rule specification](#ct-autoscaling-pr-5-rule "#ct-autoscaling-pr-5-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.AUTOSCALING.PR.5 example templates](#ct-autoscaling-pr-5-templates "#ct-autoscaling-pr-5-templates")

**Explanation**

Amazon EC2 instances in an Auto Scaling group launch configuration should not have an associated public IP address, except for in limited edge cases. Amazon EC2 instances should only be accessible from behind a load balancer instead of being directly exposed to the internet.

### Remediation for rule failure

Set `AssociatePublicIpAddress` to false on Auto Scaling Launch Configurations.

The examples that follow show how to implement this remediation.

#### Auto Scaling Launch Configuration - Example

Auto Scaling Launch Configuration configured to disable public IP address association. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingLaunchConfiguration": {
        "Type": "AWS::AutoScaling::LaunchConfiguration",
        "Properties": {
            "ImageId": {
                "Ref": "LatestAmiId"
            },
            "InstanceType": "t3.micro",
            "AssociatePublicIpAddress": false
        }
    }
}

```

**YAML example**

```

AutoScalingLaunchConfiguration:
  Type: AWS::AutoScaling::LaunchConfiguration
  Properties:
    ImageId: !Ref 'LatestAmiId'
    InstanceType: t3.micro
    AssociatePublicIpAddress: false


```

### CT.AUTOSCALING.PR.5 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   autoscaling_launch_config_public_ip_disabled_check
#
# Description:
#   Checks if Auto Scaling Launch Configurations have been configured to disable public IP address association.
#
# Reports on:
#   AWS::Auto Scaling::LaunchConfiguration
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation Hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or CloudFormation hook document
#       And: The input document does not contain any Auto Scaling Launch Configuration Resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or CloudFormation hook document
#       And: The input document contains an Auto Scaling Launch Configuration Resource
#       And: 'AssociatePublicIpAddress' is not present on the Auto Scaling Launch Configuration Resource
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or CloudFormation hook document
#       And: The input document contains an Auto Scaling Launch Configuration Resource
#       And: 'AssociatePublicIpAddress' is present on the Auto Scaling Launch Configuration Resource
#            and is set to bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or CloudFormation hook document
#       And: The input document contains an Auto Scaling Launch Configuration Resource
#       And: 'AssociatePublicIpAddress' is present on the Auto Scaling Launch Configuration Resource
#            and is set to bool(false)
#      Then: PASS

#
# Constants
#
let AUTOSCALING_LAUNCH_CONFIGURATION_TYPE = 'AWS::AutoScaling::LaunchConfiguration'
let INPUT_DOCUMENT = this

#
# Assignments
#
let autoscaling_launch_configurations = Resources.*[ Type == %AUTOSCALING_LAUNCH_CONFIGURATION_TYPE ]

#
# Primary Rules
#
rule autoscaling_launch_config_public_ip_disabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                             %autoscaling_launch_configurations not empty {

    check(%autoscaling_launch_configurations.Properties)
        <<
        [CT.AUTOSCALING.PR.5]: Require than an Amazon EC2 Auto Scaling group launch configuration does not have EC2 instances with public IP addresses
        [FIX]: Set 'AssociatePublicIpAddress' to false on Auto Scaling Launch Configurations.
        >>

}

rule autoscaling_launch_config_public_ip_disabled_check when is_cfn_hook(%INPUT_DOCUMENT, %AUTOSCALING_LAUNCH_CONFIGURATION_TYPE) {

    check(%INPUT_DOCUMENT.%AUTOSCALING_LAUNCH_CONFIGURATION_TYPE.resourceProperties)
        <<
        [CT.AUTOSCALING.PR.5]: Require than an Amazon EC2 Auto Scaling group launch configuration does not have EC2 instances with public IP addresses
        [FIX]: Set 'AssociatePublicIpAddress' to false on Auto Scaling Launch Configurations.
        >>
}

#
# Parameterized Rules
#
rule check(launch_configuration) {
    %launch_configuration {
        # Scenario 2
        AssociatePublicIpAddress exists
        # Scenarios 3 and 4
        AssociatePublicIpAddress == false
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.AUTOSCALING.PR.5 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  AutoScalingLaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId:
        Ref: LatestAmiId
      InstanceType: t3.micro
      AssociatePublicIpAddress: false


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  AutoScalingLaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId:
        Ref: LatestAmiId
      InstanceType: t3.micro
      AssociatePublicIpAddress: true


```

## [CT.AUTOSCALING.PR.6] Require any Amazon EC2 Auto Scaling groups to use multiple instance types

This control checks whether an Amazon EC2 Auto Scaling group uses multiple instance types through a mixed instance policy and explicit instance type overrides.

- **Control objective:** Improve availability
- **Implementation:** CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::AutoScalingGroup`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.6 rule specification](#ct-autoscaling-pr-6-rule "#ct-autoscaling-pr-6-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.6 rule specification](#ct-autoscaling-pr-6-rule "#ct-autoscaling-pr-6-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:

[CT.AUTOSCALING.PR.6 example templates](#ct-autoscaling-pr-6-templates "#ct-autoscaling-pr-6-templates")

**Explanation**

You can enhance availability by deploying your application across multiple instance types running in multiple Availability Zones. AWS Control Tower recommends using multiple instance types so that the Auto Scaling group can launch another instance type if there is insufficient instance capacity in your chosen Availability Zones.

###### Usage considerations

- This control applies only to Amazon EC2 Auto Scaling groups that do not use attribute-based instance type selection within a mixed instances policy (configured by means of the `InstanceRequirements` property within mixed instances policy `Overrides`).

### Remediation for rule failure

Within a `MixedInstancePolicy` configuration, provide a `LaunchTemplate` configuration with two entries in the `Overrides` property. Within each override, set the `InstanceType` property to a different Amazon EC2 instance type.

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Group - Example

Amazon EC2 Auto Scaling group configured with multiple instance types. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ],
            "MaxSize": "2",
            "MinSize": "1",
            "MixedInstancesPolicy": {
                "LaunchTemplate": {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateId": {
                            "Ref": "EC2LaunchTemplate"
                        },
                        "Version": {
                            "Fn::GetAtt": [
                                "EC2LaunchTemplate",
                                "LatestVersionNumber"
                            ]
                        }
                    },
                    "Overrides": [
                        {
                            "InstanceType": "t3.micro"
                        },
                        {
                            "InstanceType": "m5.large"
                        }
                    ]
                }
            }
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - !Ref 'Subnet'
    MaxSize: '2'
    MinSize: '1'
    MixedInstancesPolicy:
      LaunchTemplate:
        LaunchTemplateSpecification:
          LaunchTemplateId: !Ref 'EC2LaunchTemplate'
          Version: !GetAtt 'EC2LaunchTemplate.LatestVersionNumber'
        Overrides:
          - InstanceType: t3.micro
          - InstanceType: m5.large


```

### CT.AUTOSCALING.PR.6 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   autoscaling_mixed_instances_policy_multiple_instance_types_check
#
# Description:
#   This control checks whether an Amazon EC2 Auto Scaling group uses multiple instance types through a mixed instance policy and explicit instance type overrides.
#
# Reports on:
#   AWS::AutoScaling::AutoscalingGroup
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#  Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any Autoscaling Group resources
#      Then: SKIP
#  Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains Autoscaling Group resources
#       And: 'MixedInstancesPolicy.LaunchTemplate.Overrides' has been provided as a list
#       And: There exists any 'Overrides' entry where 'InstanceRequirements' is present
#       And: There exists no 'Overrides' entry where 'InstanceType' is present
#      Then: SKIP
#  Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains Autoscaling Group resources
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.Overrides' has not been provided
#      Then: FAIL
#  Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains Autoscaling Group resources
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.Overrides' has been provided as a list
#       And: 'InstanceType' is not present or is present as a empty string in 'MixedInstancesPolicy.LaunchTemplate.Overrides'
#      Then: FAIL
#  Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains Autoscaling Group resources
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.Overrides' has been provided as a list
#       And: There exists any 'Overrides' entry where 'InstanceRequirements' is present
#       And: There exists any 'Overrides' entry where 'InstanceType' is present
#      Then: FAIL
#  Scenario: 6
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains Autoscaling Group resources
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.Overrides' has been provided as a list
#       And: 'InstanceType' is present in 'MixedInstancesPolicy.LaunchTemplate.Overrides' as a non empty string
#       And: Length of 'MixedInstancesPolicy.LaunchTemplate.Overrides' is less than or equal to 1
#      Then: FAIL
#  Scenario: 7
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains Autoscaling Group resources
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.Overrides' has been provided as a list
#       And: 'InstanceType' is present in 'MixedInstancesPolicy.LaunchTemplate.Overrides' as a non empty string
#       And: Length of 'MixedInstancesPolicy.LaunchTemplate.Overrides' is greater than 1
#      Then: PASS

#
# Constants
#
let AUTOSCALING_GROUP_TYPE = "AWS::AutoScaling::AutoScalingGroup"
let INPUT_DOCUMENT = this

#
# Assignments
#
let autoscaling_groups = Resources.*[ Type == %AUTOSCALING_GROUP_TYPE ]

#
# Primary Rules
#
rule autoscaling_mixed_instances_policy_multiple_instance_types_check when is_cfn_template(%INPUT_DOCUMENT)
                                                                           %autoscaling_groups not empty {
    check(%autoscaling_groups.Properties)
        <<
        [CT.AUTOSCALING.PR.6]: Require any Amazon EC2 Auto Scaling groups to use multiple instance types
            [FIX]: Within a 'MixedInstancePolicy' configuration, provide a 'LaunchTemplate' configuration with two entries in the 'Overrides' property. Within each override, set the 'InstanceType' property to a different Amazon EC2 instance type.
        >>
}

rule autoscaling_mixed_instances_policy_multiple_instance_types_check when is_cfn_hook(%INPUT_DOCUMENT, %AUTOSCALING_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%AUTOSCALING_GROUP_TYPE.resourceProperties)
        <<
        [CT.AUTOSCALING.PR.6]: Require any Amazon EC2 Auto Scaling groups to use multiple instance types
            [FIX]: Within a 'MixedInstancePolicy' configuration, provide a 'LaunchTemplate' configuration with two entries in the 'Overrides' property. Within each override, set the 'InstanceType' property to a different Amazon EC2 instance type.
        >>
}

#
# Parameterized Rules
#
rule check(autoscaling_group) {
    %autoscaling_group [
        # Scenario 2
        filter_asg_no_instance_requirement_overrides(this)
    ] {
        # Scenario 4, 5, 6
        MixedInstancesPolicy exists
        MixedInstancesPolicy is_struct

        MixedInstancesPolicy {
            LaunchTemplate exists
            LaunchTemplate is_struct

            LaunchTemplate {
                LaunchTemplateSpecification exists
                LaunchTemplateSpecification is_struct

                Overrides exists
                Overrides is_list
                Overrides not empty

                Overrides[0] exists
                Overrides[1] exists

                Overrides[*] {
                    InstanceType exists
                    check_is_string_and_not_empty(InstanceType)
                }

                Overrides[0].InstanceType not in Overrides[1].InstanceType
            }
        }
    }

    %autoscaling_group [
        # Scenario 2
        filter_asg_conflicting_overrides(this)
    ] {
        MixedInstancesPolicy {
            LaunchTemplate {
                Overrides[*] {
                    check_mutually_exclusive_property_combination(InstanceType, InstanceRequirements) or
                    check_mutually_exclusive_property_combination(InstanceRequirements, InstanceType)
                }
            }
        }
    }
}

rule filter_asg_no_instance_requirement_overrides(autoscaling_group) {
    %autoscaling_group {
        MixedInstancesPolicy not exists or
        filter_mixed_instances_policy_no_instance_requirement_overrides(this)
    }
}

rule filter_mixed_instances_policy_no_instance_requirement_overrides(autoscaling_group) {
    %autoscaling_group {
        MixedInstancesPolicy is_struct
        MixedInstancesPolicy {
            LaunchTemplate not exists or
            filter_launch_templates_no_instance_requirement_overrides(this)
        }
    }
}

rule filter_launch_templates_no_instance_requirement_overrides(launch_template) {
    %launch_template {
        LaunchTemplate is_struct
        LaunchTemplate {
            Overrides not exists or
            filter_overrides_no_instance_requirement_overrides(this)
        }
    }
}

rule filter_overrides_no_instance_requirement_overrides(overrides) {
    %overrides {
        Overrides is_list
        Overrides empty or
        Overrides[*] {
            InstanceRequirements not exists
        }
    }
}

rule filter_asg_conflicting_overrides(autoscaling_group) {
    %autoscaling_group {
        MixedInstancesPolicy not exists or
        filter_mixed_instances_policy_conflicting_overrides(this)
    }
}

rule filter_mixed_instances_policy_conflicting_overrides(autoscaling_group) {
    %autoscaling_group {
        MixedInstancesPolicy is_struct
        MixedInstancesPolicy {
            LaunchTemplate not exists or
            filter_launch_templates_conflicting_overrides(this)
        }
    }
}

rule filter_launch_templates_conflicting_overrides(launch_template) {
    %launch_template {
        LaunchTemplate is_struct
        LaunchTemplate {
            Overrides not exists or
            filter_overrides_conflicting_overrides(this)
        }
    }
}

rule filter_overrides_conflicting_overrides(overrides) {
    %overrides {
        Overrides is_list
        Overrides empty or
        some Overrides[*] {
            InstanceRequirements exists
            InstanceType exists
        }
    }
}

rule check_mutually_exclusive_property_combination(property1, property2) {
    %property1 not exists
    %property2 exists
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists or
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

### CT.AUTOSCALING.PR.6 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  EC2LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName:
        Fn::Sub: ${AWS::StackName}-example
      LaunchTemplateData:
        InstanceType: t3.micro
        ImageId:
          Ref: LatestAmiId
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
      - Ref: Subnet
      MaxSize: '2'
      MinSize: '1'
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: EC2LaunchTemplate
            Version:
              Fn::GetAtt:
              - EC2LaunchTemplate
              - LatestVersionNumber
          Overrides:
          - InstanceType: t3.micro
          - InstanceType: m5.large


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  EC2LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName:
        Fn::Sub: ${AWS::StackName}-example
      LaunchTemplateData:
        InstanceType: t3.micro
        ImageId:
          Ref: LatestAmiId
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
      - Ref: Subnet
      MaxSize: '2'
      MinSize: '1'
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: EC2LaunchTemplate
            Version:
              Fn::GetAtt:
              - EC2LaunchTemplate
              - LatestVersionNumber
          Overrides:
          - InstanceType: t3.micro


```

## [CT.AUTOSCALING.PR.8] Require an Amazon EC2 Auto Scaling group to have EC2 launch templates configured

This control checks whether an Amazon EC2 Auto Scaling group is configured to use an EC2 launch template.

- **Control objective:** Manage vulnerabilities
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::AutoScalingGroup`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.8 rule specification](#ct-autoscaling-pr-8-rule "#ct-autoscaling-pr-8-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.8 rule specification](#ct-autoscaling-pr-8-rule "#ct-autoscaling-pr-8-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.AUTOSCALING.PR.8 example templates](#ct-autoscaling-pr-8-templates "#ct-autoscaling-pr-8-templates")

**Explanation**

An Auto Scaling group can be created from an EC2 launch template or from a launch configuration. If you use a launch template to create an Auto Scaling group, you have access to the latest features and improvements.

### Remediation for rule failure

Provide a `LaunchTemplate` or `MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification` configuration with a valid `Version` and a `LaunchTemplateId` or `LaunchTemplateName`.

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Group - Example One

Amazon EC2 Auto Scaling group configured with an EC2 launch template. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ],
            "MaxSize": "2",
            "MinSize": "1",
            "LaunchTemplate": {
                "LaunchTemplateName": "SampleLaunchTemplate",
                "Version": {
                    "Fn::GetAtt": [
                        "EC2LaunchTemplate",
                        "LatestVersionNumber"
                    ]
                }
            }
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - !Ref 'Subnet'
    MaxSize: '2'
    MinSize: '1'
    LaunchTemplate:
      LaunchTemplateName: SampleLaunchTemplate
      Version: !GetAtt 'EC2LaunchTemplate.LatestVersionNumber'


```

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Group - Example Two

Amazon EC2 Auto Scaling group configured with a mixed instances policy and EC2 launch template. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ],
            "MaxSize": "2",
            "MinSize": "1",
            "MixedInstancesPolicy": {
                "LaunchTemplate": {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateId": {
                            "Ref": "EC2LaunchTemplate"
                        },
                        "Version": {
                            "Fn::GetAtt": [
                                "EC2LaunchTemplate",
                                "LatestVersionNumber"
                            ]
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

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - !Ref 'Subnet'
    MaxSize: '2'
    MinSize: '1'
    MixedInstancesPolicy:
      LaunchTemplate:
        LaunchTemplateSpecification:
          LaunchTemplateId: !Ref 'EC2LaunchTemplate'
          Version: !GetAtt 'EC2LaunchTemplate.LatestVersionNumber'


```

### CT.AUTOSCALING.PR.8 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   autoscaling_launch_template_check
#
# Description:
#   This control checks whether an Amazon EC2 Auto Scaling group is configured to use an EC2 launch template.
#
# Reports on:
#   AWS::AutoScaling::AutoscalingGroup
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#  Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contains any Amazon EC2 Auto Scaling group resources
#      Then: SKIP
#  Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling group resource
#       And: 'LaunchTemplate' has not been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has not been provided
#      Then: FAIL
#  Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling group resource
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has not been provided
#       And: 'LaunchTemplate' has been provided
#       And: 'LaunchTemplate' has an invalid configuration ('Version' has not been provided and one of 'LaunchTemplateId'
#            or 'LaunchTemplateName' has not been provided or 'Version' has been provided as an empty string or invalid local
#            reference and one of 'LaunchTemplateId' or 'LaunchTemplateName' has been provided as an empty string or an
#            invalid local reference)
#      Then: FAIL
#  Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling group resource
#       And: 'LaunchTemplate' has not been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has an invalid configuration ('Version' has
#            not been provided and one of 'LaunchTemplateId' or 'LaunchTemplateName' has not been provided or 'Version' has
#            been provided as an empty string or invalid local reference and one of 'LaunchTemplateId' or 'LaunchTemplateName'
#            has been provided as an empty string or an invalid local reference)
#      Then: FAIL
#  Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling group resource
#       And: 'LaunchTemplate' has been provided
#       And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has
#            been provided.
#       Then: FAIL
#   Scenario: 6
#      Given: The input document is an CloudFormation or CloudFormation hook document
#        And: The input document contains an Amazon EC2 Auto Scaling group resource
#        And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has not been provided
#        And: 'LaunchTemplate' has been provided
#        And: 'LaunchTemplate' has a valid configuration ('Version' has been provided and one of 'LaunchTemplateId' or
#             'LaunchTemplateName' has been provided as a non-empty string or valid local reference)
#       Then: PASS
#   Scenario: 7
#      Given: The input document is an CloudFormation or CloudFormation hook document
#        And: The input document contains an Amazon EC2 Auto Scaling group resource
#        And: 'LaunchTemplate' has not been provided
#        And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has been provided
#        And: 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' has a valid configuration ('Version' has
#             been provided and one of 'LaunchTemplateId' or 'LaunchTemplateName' has been provided as a non-empty string
#             or valid local reference)
#       Then: PASS

#
# Constants
#
let AUTOSCALING_GROUP_TYPE = "AWS::AutoScaling::AutoScalingGroup"
let INPUT_DOCUMENT = this

#
# Assignments
#
let autoscaling_groups = Resources.*[ Type == %AUTOSCALING_GROUP_TYPE ]

#
# Primary Rules
#
rule autoscaling_launch_template_check when is_cfn_template(%INPUT_DOCUMENT)
                                            %autoscaling_groups not empty {
    check(%autoscaling_groups.Properties)
        <<
        [CT.AUTOSCALING.PR.8]: Require an Amazon EC2 Auto Scaling group to have EC2 launch templates configured
            [FIX]: Provide a 'LaunchTemplate' or 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' configuration with a valid 'Version' and a 'LaunchTemplateId' or 'LaunchTemplateName'.
        >>
}

rule autoscaling_launch_template_check when is_cfn_hook(%INPUT_DOCUMENT, %AUTOSCALING_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%AUTOSCALING_GROUP_TYPE.resourceProperties)
        <<
        [CT.AUTOSCALING.PR.8]: Require an Amazon EC2 Auto Scaling group to have EC2 launch templates configured
            [FIX]: Provide a 'LaunchTemplate' or 'MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification' configuration with a valid 'Version' and a 'LaunchTemplateId' or 'LaunchTemplateName'.
        >>
}

#
# Parameterized Rules
#
rule check(autoscaling_groups) {
    %autoscaling_groups {
        # Scenario 3 and 6
        check_launch_template(this) or

        # Scenario 4 and 7
        check_mixed_instances_policy(this)
    }
}

rule check_launch_template(autoscaling_groups) {
    %autoscaling_groups {
        check_mutually_exclusive_property_combination(LaunchTemplate, MixedInstancesPolicy)
        LaunchTemplate is_struct
        LaunchTemplate {
            check_valid_launch_template_config(this)
        }
    }
}

rule check_mixed_instances_policy(autoscaling_groups) {
    %autoscaling_groups {
        check_mutually_exclusive_property_combination(MixedInstancesPolicy, LaunchTemplate)
        MixedInstancesPolicy is_struct
        MixedInstancesPolicy {
            LaunchTemplate exists
            LaunchTemplate is_struct
            LaunchTemplate {
                LaunchTemplateSpecification exists
                LaunchTemplateSpecification is_struct
                check_valid_launch_template_config(LaunchTemplateSpecification)
            }
        }
    }
}

rule check_valid_launch_template_config(launch_template_specification) {
    %launch_template_specification {
        check_valid_launch_template_property(Version)
        check_valid_prop_combination(LaunchTemplateId, LaunchTemplateName) or
        check_valid_prop_combination(LaunchTemplateName, LaunchTemplateId)
    }
}

rule check_valid_prop_combination(valid_property, invalid_property) {
    check_mutually_exclusive_property_combination(%valid_property, %invalid_property)
    check_valid_launch_template_property(%valid_property)
}

rule check_mutually_exclusive_property_combination(valid_property, invalid_property) {
    %invalid_property not exists
    %valid_property exists
}

rule check_valid_launch_template_property(property) {
    %property {
        check_is_string_and_not_empty(this) or
        check_local_references(%INPUT_DOCUMENT, this, "AWS::EC2::LaunchTemplate")
    }
}

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
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

### CT.AUTOSCALING.PR.8 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  EC2LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName:
        Fn::Sub: ${AWS::StackName}-example
      LaunchTemplateData:
        InstanceType: t3.micro
        ImageId:
          Ref: LatestAmiId
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
      - Ref: Subnet
      MaxSize: '2'
      MinSize: '1'
      LaunchTemplate:
        LaunchTemplateId:
          Ref: EC2LaunchTemplate
        Version:
          Fn::GetAtt:
          - EC2LaunchTemplate
          - LatestVersionNumber


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  AutoScalingLaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId:
        Ref: LatestAmiId
      InstanceType: t3.micro
      LaunchConfigurationName: "AutoScalingLaunchConfiguration"
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
      - Ref: Subnet
      MaxSize: '2'
      MinSize: '1'
      LaunchConfigurationName: "AutoScalingLaunchConfiguration"


```

## [CT.AUTOSCALING.PR.9] Require an Amazon EBS volume configured through an Amazon EC2 Auto Scaling launch configuration to encrypt data at rest

This control checks whether Auto Scaling launch configurations with Amazon EBS volume block device mappings enable Amazon EBS volume encryption.

- **Control objective:** Encrypt data at rest
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::LaunchConfiguration`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.9 rule specification](#ct-autoscaling-pr-9-rule "#ct-autoscaling-pr-9-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.9 rule specification](#ct-autoscaling-pr-9-rule "#ct-autoscaling-pr-9-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.AUTOSCALING.PR.9 example templates](#ct-autoscaling-pr-9-templates "#ct-autoscaling-pr-9-templates")

**Explanation**

Enable Amazon EBS encryption at rest, to provide an added layer of security for your sensitive data in Amazon EBS volumes. Amazon EBS encryption offers a straightforward encryption
solution for your Amazon EBS resources. It doesn't require you to build, maintain, and secure your own key management infrastructure. It uses KMS keys
when creating encrypted volumes and snapshots.

###### Usage considerations

- This control applies only to Amazon EC2 Auto Scaling launch configurations that specify Amazon EBS block device mappings.

### Remediation for rule failure

For every entry in the BlockDeviceMappings parameter with an `Ebs` configuration, set the value of `Encryption` to true.

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Launch Configuration - Example

An Amazon EC2 Auto Scaling launch configuration configured with an Amazon EBS block device mapping that has volume encryption enabled.
The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LaunchConfiguration": {
        "Type": "AWS::AutoScaling::LaunchConfiguration",
        "Properties": {
            "ImageId": {
                "Ref": "LatestAmiId"
            },
            "InstanceType": "t3.micro",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/sdc",
                    "Ebs": {
                        "Encrypted": true,
                        "VolumeSize": 100,
                        "VolumeType": "gp3"
                    }
                }
            ]
        }
    }
}

```

**YAML example**

```

LaunchConfiguration:
  Type: AWS::AutoScaling::LaunchConfiguration
  Properties:
    ImageId: !Ref 'LatestAmiId'
    InstanceType: t3.micro
    BlockDeviceMappings:
      - DeviceName: /dev/sdc
        Ebs:
          Encrypted: true
          VolumeSize: 100
          VolumeType: gp3


```

### CT.AUTOSCALING.PR.9 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   autoscaling_launch_config_encrypted_volumes_check
#
# Description:
#   This control checks whether Auto Scaling launch configurations with Amazon EBS volume block device mappings enable Amazon EBS volume encryption.
#
# Reports on:
#   AWS::AutoScaling::LaunchConfiguration
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
#       And: The input document does not contain any Amazon EC2 Auto Scaling launch configuration resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling launch configuration resource
#       And: 'BlockDeviceMappings' has not been provided or has been provided as an empty list
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling launch configuration resource
#       And: 'BlockDeviceMappings' has been provided as a non-empty list
#       And: No entries in 'BlockDeviceMappings' contain 'Ebs' as a struct
#      Then: SKIP
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling launch configuration resource
#       And: 'BlockDeviceMappings' has been provided as a non-empty list
#       And: An entry in 'BlockDeviceMappings' contains 'Ebs' as a struct
#       And: In the same entry, 'Encrypted' in 'Ebs' has not been provided or has been provided
#            and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 Auto Scaling launch configuration resource
#       And: 'BlockDeviceMappings' has been provided as a non-empty list
#       And: An entry in 'BlockDeviceMappings' contains 'Ebs' as a struct
#       And: In the same entry, 'Encrypted' in 'Ebs' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let INPUT_DOCUMENT = this
let AUTOSCALING_LAUNCH_CONFIGURATION_TYPE = "AWS::AutoScaling::LaunchConfiguration"

#
# Assignments
#
let autoscaling_launch_configurations = Resources.*[ Type == %AUTOSCALING_LAUNCH_CONFIGURATION_TYPE ]

#
# Primary Rules
#
rule autoscaling_launch_config_encrypted_volumes_check when is_cfn_template(this)
                                                            %autoscaling_launch_configurations not empty {
    check(%autoscaling_launch_configurations.Properties)
        <<
        [CT.AUTOSCALING.PR.9]: Require an Amazon EBS volume configured through an Amazon EC2 Auto Scaling launch configuration to encrypt data at rest
        [FIX]: For every entry in the BlockDeviceMappings parameter with an 'Ebs' configuration, set the value of 'Encryption' to true.
        >>
}

rule autoscaling_launch_config_encrypted_volumes_check when is_cfn_hook(%INPUT_DOCUMENT, %AUTOSCALING_LAUNCH_CONFIGURATION_TYPE) {
    check(%INPUT_DOCUMENT.%AUTOSCALING_LAUNCH_CONFIGURATION_TYPE.resourceProperties)
        <<
        [CT.AUTOSCALING.PR.9]: Require an Amazon EBS volume configured through an Amazon EC2 Auto Scaling launch configuration to encrypt data at rest
        [FIX]: For every entry in the BlockDeviceMappings parameter with an 'Ebs' configuration, set the value of 'Encryption' to true.
        >>
}

#
# Parameterized Rules
#
rule check(autoscaling_launch_configuration) {
    %autoscaling_launch_configuration [
        # Scenarios 2 and 3
        filter_launch_configuration_contains_ebs_block_device_mappings(this)
    ] {
        BlockDeviceMappings[
            Ebs exists
            Ebs is_struct
        ] {
            Ebs {
                # Scenarios 4 and 5
                Encrypted exists
                Encrypted == true
            }
        }
    }
}

rule filter_launch_configuration_contains_ebs_block_device_mappings(launch_configuration) {
    %launch_configuration {
        BlockDeviceMappings exists
        BlockDeviceMappings is_list
        BlockDeviceMappings not empty

        some BlockDeviceMappings[*] {
            Ebs exists
            Ebs is_struct
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

### CT.AUTOSCALING.PR.9 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value "AWS::EC2::Image::Id"
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId:
        Ref: LatestAmiId
      InstanceType: t3.micro
      BlockDeviceMappings:
      - DeviceName: /dev/sdc
        Ebs:
          Encrypted: true
          VolumeSize: 100
          VolumeType: gp3


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value "AWS::EC2::Image::Id"
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  LaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId:
        Ref: LatestAmiId
      InstanceType: t3.micro
      BlockDeviceMappings:
      - DeviceName: /dev/sdc
        Ebs:
          Encrypted: false
          VolumeSize: 100
          VolumeType: gp3


```

## [CT.AUTOSCALING.PR.10] Require an Amazon EC2 Auto Scaling group to use only AWS Nitro instance types when overriding a launch template

This control checks whether, when using a `MixedInstancesPolicy` resource parameter override, an Amazon EC2 Auto Scaling
group overrides launch templates by specifying AWS Nitro instance types only.

- **Control objective:** Protect data integrity, Enforce least privilege
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::AutoScalingGroup`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.10 rule specification](#ct-autoscaling-pr-10-rule "#ct-autoscaling-pr-10-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.10 rule specification](#ct-autoscaling-pr-10-rule "#ct-autoscaling-pr-10-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.AUTOSCALING.PR.10 example templates](#ct-autoscaling-pr-10-templates "#ct-autoscaling-pr-10-templates")

**Explanation**

The Nitro System is a collection of hardware and software components built by AWS to enable high performance, high availability, and high security.
The Nitro System provides enhanced security because it continuously monitors, protects, and verifies the instance's
hardware and firmware. Virtualization resources are offloaded to dedicated hardware and software, thereby minimizing the attack surface.
The Nitro System security model is locked down to prohibit administrative access, greatly reducing the possibility of human error and tampering.

###### Usage considerations

- This control applies only to Amazon EC2 Auto Scaling groups that are configured with launch template overrides that specify an instance type or instance attributes. A `LaunchTemplate.LaunchTemplateSpecification` configuration specifies one or more `Overrides` that also include `InstanceType`
  or `InstanceRequirements`.
- This control does not check the instance type configured on a launch template. To ensure that launch templates use Nitro instances types, use this control in conjunction with related controls that check launch templates for Nitro instance types.

### Remediation for rule failure

In the MixedInstancesPolicy.LaunchTemplate property, if it has one or more `Overrides` fields that include `InstanceType` or `InstanceRequirements`, set the value of `InstanceType` to an Amazon EC2 instance type that is based on the AWS Nitro system, or set the value of
`AllowedInstanceTypes` in `InstanceRequirements` to one or more Amazon EC2 instance types that are based on the AWS Nitro system.

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Group - Example One

An Amazon EC2 Auto Scaling group configured with a launch template override and instance type based on the AWS Nitro system. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "MixedInstancesPolicy": {
                "LaunchTemplate": {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateId": {
                            "Ref": "LaunchTemplate"
                        },
                        "Version": {
                            "Fn::GetAtt": "LaunchTemplate.LatestVersionNumber"
                        }
                    },
                    "Overrides": [
                        {
                            "InstanceType": "t3.micro"
                        }
                    ]
                }
            },
            "MaxSize": 1,
            "MinSize": 0,
            "DesiredCapacity": 1,
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ]
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    MixedInstancesPolicy:
      LaunchTemplate:
        LaunchTemplateSpecification:
          LaunchTemplateId: !Ref 'LaunchTemplate'
          Version: !GetAtt 'LaunchTemplate.LatestVersionNumber'
        Overrides:
          - InstanceType: t3.micro
    MaxSize: 1
    MinSize: 0
    DesiredCapacity: 1
    VPCZoneIdentifier:
      - !Ref 'Subnet'


```

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Group - Example Two

An Amazon EC2 Auto Scaling group configured with a launch template override and instance requirements that specify a list of allowed instances
based on the AWS Nitro system. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "MixedInstancesPolicy": {
                "LaunchTemplate": {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateId": {
                            "Ref": "LaunchTemplate"
                        },
                        "Version": {
                            "Fn::GetAtt": "LaunchTemplate.LatestVersionNumber"
                        }
                    },
                    "Overrides": [
                        {
                            "InstanceRequirements": {
                                "AllowedInstanceTypes": [
                                    "m5.*",
                                    "c5.*"
                                ],
                                "VCpuCount": {
                                    "Min": 2,
                                    "Max": 4
                                },
                                "MemoryMiB": {
                                    "Min": 4000,
                                    "Max": 8000
                                }
                            }
                        }
                    ]
                }
            },
            "MaxSize": 1,
            "MinSize": 0,
            "DesiredCapacity": 1,
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ]
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    MixedInstancesPolicy:
      LaunchTemplate:
        LaunchTemplateSpecification:
          LaunchTemplateId: !Ref 'LaunchTemplate'
          Version: !GetAtt 'LaunchTemplate.LatestVersionNumber'
        Overrides:
          - InstanceRequirements:
              AllowedInstanceTypes:
                - m5.*
                - c5.*
              VCpuCount:
                Min: 2
                Max: 4
              MemoryMiB:
                Min: 4000
                Max: 8000
    MaxSize: 1
    MinSize: 0
    DesiredCapacity: 1
    VPCZoneIdentifier:
      - !Ref 'Subnet'


```

### CT.AUTOSCALING.PR.10 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   autoscaling_group_nitro_instance_override_check
#
# Description:
#   This control checks whether, when using a `MixedInstancesPolicy` resource parameter override, an Amazon EC2 Auto Scaling group overrides launch templates with AWS Nitro instance types only.
#
# Reports on:
#   AWS::AutoScaling::AutoScalingGroup
#
# Evaluates:
#   CloudFormation, CloudFormation Hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any Amazon EC2 auto scaling group resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has not been provided or
#            has been provided as an empty list
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: No entries in 'Overrides' include 'InstanceType' or 'InstanceRequirements'
#      Then: SKIP
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceType' has been provided and set to an instance type
#            other than a Nitro instance type
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceRequirements' has been provided
#       And: For the same entry in 'Overrides', 'AllowedInstanceTypes' has not been provided or has been
#            provided as an empty list
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceRequirements' has been provided
#       And: For the same entry in 'Overrides', 'AllowedInstanceTypes' has been provided as a non-empty list
#       And: An entry in 'AllowedInstanceTypes' is set to an instance type other than a Nitro instance type
#      Then: FAIL
#   Scenario: 7
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceType' has been provided and set to a Nitro instance type
#      Then: PASS
#   Scenario: 8
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceRequirements' has been provided
#       And: For the same entry in 'Overrides', 'AllowedInstanceTypes' has been provided as a non-empty list
#       And: Every entry in 'AllowedInstanceTypes' is set to a Nitro instance type
#      Then: PASS

#
# Constants
#
let INPUT_DOCUMENT = this
let AUTOSCALING_GROUP_TYPE = "AWS::AutoScaling::AutoScalingGroup"
let NITRO_INSTANCE_TYPES = [
    /^a1\..+?$/,
    /^c5\..+?$/, /^c5a\..+?$/, /^c5ad\..+?$/, /^c5d\..+?$/, /^c5n\..+?$/, /^c6a\..+?$/,
    /^c6g\..+?$/, /^c6gd\..+?$/, /^c6gn\..+?$/, /^c6i\..+?$/, /^c6id\..+?$/, /^c6in\..+?$/,
    /^c7a\..+?$/, /^c7g\..+?$/, /^c7gd\..+?$/, /^c7gn\..+?$/, /^c7i-flex\..+?$/,
    /^c7i\..+?$/, /^c8g\..+?$/, /^c8gd\..+?$/, /^c8gn\..+?$/,
    /^d3\..+?$/, /^d3en\..+?$/, /^dl1\..+?$/, /^dl2q\..+?$/,
    /^f2\..+?$/,
    /^g4ad\..+?$/, /^g4dn\..+?$/, /^g5\..+?$/, /^g5g\..+?$/, /^g6\..+?$/, /^g6e\..+?$/,
    /^g6f\..+?$/, /^gr6\..+?$/, /^gr6f\..+?$/,
    /^hpc6a\..+?$/, /^hpc6id\..+?$/, /^hpc7a\..+?$/, /^hpc7g\..+?$/,
    /^i3\.metal$/, /^i3en\..+?$/, /^i4g\..+?$/, /^i4i\..+?$/, /^i7i\..+?$/, /^i7ie\..+?$/,
    /^i8g\..+?$/, /^im4gn\..+?$/, /^inf1\..+?$/, /^inf2\..+?$/, /^is4gen\..+?$/,
    /^m5\..+?$/, /^m5a\..+?$/, /^m5ad\..+?$/, /^m5d\..+?$/, /^m5dn\..+?$/, /^m5n\..+?$/,
    /^m5zn\..+?$/, /^m6a\..+?$/, /^m6g\..+?$/, /^m6gd\..+?$/, /^m6i\..+?$/, /^m6id\..+?$/,
    /^m6idn\..+?$/, /^m6in\..+?$/, /^m7a\..+?$/, /^m7g\..+?$/, /^m7gd\..+?$/,
    /^m7i-flex\..+?$/, /^m7i\..+?$/, /^m8g\..+?$/, /^m8gd\..+?$/, /^mac1\.metal$/,
    /^mac2-m1ultra\.metal$/, /^mac2-m2\.metal$/, /^mac2-m2pro\.metal$/, /^mac2\.metal$/,
    /^p3dn\..+?$/, /^p4d\..+?$/, /^p4de\..+?$/, /^p5\..+?$/, /^p5e\..+?$/, /^p5en\..+?$/,
    /^p6-b200\..+?$/,
    /^r5\..+?$/, /^r5a\..+?$/, /^r5ad\..+?$/, /^r5b\..+?$/, /^r5d\..+?$/, /^r5dn\..+?$/,
    /^r5n\..+?$/, /^r6a\..+?$/, /^r6g\..+?$/, /^r6gd\..+?$/, /^r6i\..+?$/, /^r6id\..+?$/,
    /^r6idn\..+?$/, /^r6in\..+?$/, /^r7a\..+?$/, /^r7g\..+?$/, /^r7gd\..+?$/, /^r7i\..+?$/,
    /^r7iz\..+?$/, /^r8g\..+?$/, /^r8gd\..+?$/, /^r8i-flex\..+?$/, /^r8i\..+?$/,
    /^t3\..+?$/, /^t3a\..+?$/, /^t4g\..+?$/, /^trn1\..+?$/, /^trn1n\..+?$/, /^trn2\..+?$/,
    /^u-12tb1\..+?$/, /^u-18tb1\..+?$/, /^u-24tb1\..+?$/, /^u-3tb1\..+?$/, /^u-6tb1\..+?$/,
    /^u-9tb1\..+?$/, /^u7i-12tb\..+?$/, /^u7i-6tb\..+?$/, /^u7i-8tb\..+?$/,
    /^u7in-16tb\..+?$/, /^u7in-24tb\..+?$/, /^u7in-32tb\..+?$/,
    /^vt1\..+?$/,
    /^x2gd\..+?$/, /^x2idn\..+?$/, /^x2iedn\..+?$/, /^x2iezn\..+?$/, /^x8g\..+?$/,
    /^z1d\..+?$/
]

#
# Assignments
#
let autoscaling_groups = Resources.*[ Type == %AUTOSCALING_GROUP_TYPE ]

#
# Primary Rules
#
rule autoscaling_group_nitro_instance_override_check when is_cfn_template(%INPUT_DOCUMENT)
                                                          %autoscaling_groups not empty {
    check(%autoscaling_groups.Properties)
        <<
        [CT.AUTOSCALING.PR.10]: Require an Amazon EC2 Auto Scaling group to override only those launch templates with AWS Nitro instance types
        [FIX]: In the MixedInstancesPolicy.LaunchTemplate property, if it has one or more 'Overrides' fields that include 'InstanceType' or 'InstanceRequirements',
        set the value of 'InstanceType' to an Amazon EC2 instance type that is based on the AWS Nitro system, or set the value of 'AllowedInstanceTypes' in 'InstanceRequirements' to one or more Amazon EC2 instance
        types that are based on the AWS Nitro system.
        >>
}

rule autoscaling_group_nitro_instance_override_check when is_cfn_hook(%INPUT_DOCUMENT, %AUTOSCALING_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%AUTOSCALING_GROUP_TYPE.resourceProperties)
        <<
        [CT.AUTOSCALING.PR.10]: Require an Amazon EC2 Auto Scaling group to override only those launch templates with AWS Nitro instance types
        [FIX]: In the MixedInstancesPolicy.LaunchTemplate property, if it has one or more 'Overrides' fields that include 'InstanceType' or 'InstanceRequirements',
        set the value of 'InstanceType' to an Amazon EC2 instance type that is based on the AWS Nitro system, or set the value of 'AllowedInstanceTypes' in 'InstanceRequirements' to one or more Amazon EC2
        instance types that are based on the AWS Nitro system.
        >>
}

#
# Parameterized Rules
#
rule check(autoscaling_group) {
    %autoscaling_group [
        # Scenarios 2 and 3
        filter_launch_template_overrides(this)
    ] {
        MixedInstancesPolicy {
            LaunchTemplate {
                Overrides[ InstanceType exists ] {
                    # Scenarios 4 and 7
                    InstanceType in %NITRO_INSTANCE_TYPES
                }
                Overrides[ InstanceRequirements exists ] {
                    InstanceRequirements {
                        # Scenarios 5, 6 and 8
                        AllowedInstanceTypes exists
                        AllowedInstanceTypes is_list
                        AllowedInstanceTypes not empty
                        AllowedInstanceTypes[*] in %NITRO_INSTANCE_TYPES
                    }
                }
            }
        }
    }
}

rule filter_launch_template_overrides(autoscaling_group) {
    %autoscaling_group {
        MixedInstancesPolicy exists
        MixedInstancesPolicy is_struct

        MixedInstancesPolicy {
            LaunchTemplate exists
            LaunchTemplate is_struct

            LaunchTemplate {
                Overrides exists
                Overrides is_list
                Overrides not empty

                some Overrides[*] {
                    InstanceType exists or
                    InstanceRequirements exists
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

### CT.AUTOSCALING.PR.10 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value 'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceType: t3.micro
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceRequirements:
              AllowedInstanceTypes:
              - m5.*
              - c5.*
              VCpuCount:
                Min: 2
                Max: 4
              MemoryMiB:
                Min: 4000
                Max: 8000
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceType: t2.micro
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceRequirements:
              AllowedInstanceTypes:
              - c4.large
              VCpuCount:
                Max: 16
                Min: 1
              MemoryMiB:
                Min: 1000
                Max: 17000
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```

## [CT.AUTOSCALING.PR.11] Require only AWS Nitro instance types that support network traffic encryption between

instances to be added to an Amazon EC2 Auto Scaling group, when overriding a launch template

This control checks whether an Amazon EC2 Auto Scaling group uses AWS Nitro instance types that
support network traffic encryption between instances, when overriding a launch template. The Auto Scaling
group creates this override in the `AWS::Autoscaling::AutoscalingGroup.MixedInstancesPolicy.LaunchTemplate` parameter.

- **Control objective:** Encrypt data in transit, Protect data integrity, Enforce least privilege
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AutoScaling::AutoScalingGroup`
- **CloudFormation guard rule:**
  [CT.AUTOSCALING.PR.11 rule specification](#ct-autoscaling-pr-11-rule "#ct-autoscaling-pr-11-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.AUTOSCALING.PR.11 rule specification](#ct-autoscaling-pr-11-rule "#ct-autoscaling-pr-11-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.AUTOSCALING.PR.11 example templates](#ct-autoscaling-pr-11-templates "#ct-autoscaling-pr-11-templates")

**Explanation**

The Nitro System is a collection of hardware and software components built by AWS to enable high performance, high availability, and high security. The Nitro System provides
enhanced security because it continuously monitors, protects, and verifies the instance's hardware and firmware. Virtualization resources are offloaded to dedicated hardware and software,
thereby minimizing the attack surface. The Nitro System security model is locked down to prohibit administrative access, greatly reducing the possibility of human error and tampering.

AWS provides secure and private connectivity between Amazon EC2 instances of all types. In addition, some instance types use the offload capabilities of the underlying Nitro System hardware to
encrypt in-transit traffic between instances, automatically. This encryption uses Authenticated Encryption with Associated Data (AEAD) algorithms, and 256-bit encryption. It has no impact on
network performance.

###### Usage considerations

- This control applies only to Amazon EC2 Auto Scaling groups that are configured with launch template overrides that specify an instance type or instance attributes. A `LaunchTemplate.LaunchTemplateSpecification` configuration specifies one or more `Overrides` that also include `InstanceType` or `InstanceRequirements`.
- This control does not check the instance type configured on a launch template. To ensure that launch templates use Nitro instances types that support encryption in-transit between instances, use this control in conjunction with related controls that check launch templates for Nitro instance types that support encryption in-transit between instances.
- To support in-transit traffic encryption between instances, the Amazon EC2 instances must be one of the types required by this control, the instances must be in the same AWS Region, and they must be in the same VPC or group of peered VPCs, in which traffic does not pass through a virtual network
  device or service, such as a load balancer or a transit gateway.

### Remediation for rule failure

In `MixedInstancesPolicy.LaunchTemplate` with one or more `Overrides` that include `InstanceType` or `InstanceRequirements`, set either `InstanceType` to an EC2 instance type based on the AWS Nitro system that supports encryption in-transit between instances, or set `AllowedInstanceTypes` in `InstanceRequirements` to one or more EC2 instance types based on the AWS Nitro system that supports encryption in-transit between instances.

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Group - Example One

An Amazon EC2 Auto Scaling group configured with a launch template override and an instance type that is based on the AWS Nitro system. It supports encryption in transit between instances.
The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "MixedInstancesPolicy": {
                "LaunchTemplate": {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateId": {
                            "Ref": "LaunchTemplate"
                        },
                        "Version": {
                            "Fn::GetAtt": "LaunchTemplate.LatestVersionNumber"
                        }
                    },
                    "Overrides": [
                        {
                            "InstanceType": "c5a.large"
                        }
                    ]
                }
            },
            "MaxSize": 1,
            "MinSize": 0,
            "DesiredCapacity": 1,
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ]
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    MixedInstancesPolicy:
      LaunchTemplate:
        LaunchTemplateSpecification:
          LaunchTemplateId: !Ref 'LaunchTemplate'
          Version: !GetAtt 'LaunchTemplate.LatestVersionNumber'
        Overrides:
          - InstanceType: c5a.large
    MaxSize: 1
    MinSize: 0
    DesiredCapacity: 1
    VPCZoneIdentifier:
      - !Ref 'Subnet'


```

The examples that follow show how to implement this remediation.

#### Amazon EC2 Auto Scaling Group - Example Two

An Amazon EC2 Auto Scaling group configured with a launch template override and its instance requirements, which specify a list of allowed instances that are based on the AWS Nitro system.
It supports encryption in transit between instances. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "AutoScalingGroup": {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
            "MixedInstancesPolicy": {
                "LaunchTemplate": {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateId": {
                            "Ref": "LaunchTemplate"
                        },
                        "Version": {
                            "Fn::GetAtt": "LaunchTemplate.LatestVersionNumber"
                        }
                    },
                    "Overrides": [
                        {
                            "InstanceRequirements": {
                                "AllowedInstanceTypes": [
                                    "c5a.*",
                                    "m6a.*"
                                ],
                                "VCpuCount": {
                                    "Min": 2,
                                    "Max": 4
                                },
                                "MemoryMiB": {
                                    "Min": 4000,
                                    "Max": 8000
                                }
                            }
                        }
                    ]
                }
            },
            "MaxSize": 1,
            "MinSize": 0,
            "DesiredCapacity": 1,
            "VPCZoneIdentifier": [
                {
                    "Ref": "Subnet"
                }
            ]
        }
    }
}

```

**YAML example**

```

AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    MixedInstancesPolicy:
      LaunchTemplate:
        LaunchTemplateSpecification:
          LaunchTemplateId: !Ref 'LaunchTemplate'
          Version: !GetAtt 'LaunchTemplate.LatestVersionNumber'
        Overrides:
          - InstanceRequirements:
              AllowedInstanceTypes:
                - c5a.*
                - m6a.*
              VCpuCount:
                Min: 2
                Max: 4
              MemoryMiB:
                Min: 4000
                Max: 8000
    MaxSize: 1
    MinSize: 0
    DesiredCapacity: 1
    VPCZoneIdentifier:
      - !Ref 'Subnet'


```

### CT.AUTOSCALING.PR.11 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   autoscaling_group_nitro_encryption_in_transit_override_check
#
# Description:
#   This control checks whether an Auto Scaling group, when using a mixed instance policy, overrides only those launch templates with AWS Nitro
instance types that support encryption in transit between instances.
#
# Reports on:
#   AWS::AutoScaling::AutoScalingGroup
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
#       And: The input document does not contain any Amazon EC2 auto scaling group resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has not been provided or
#            has been provided as an empty list
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: No entries in 'Overrides' include 'InstanceType' or 'InstanceRequirements'
#      Then: SKIP
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceType' has been provided and set to an instance type
#            other than a Nitro instance type that supports encryption in-transit between instances
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceRequirements' has been provided
#       And: For the same entry in 'Overrides', 'AllowedInstanceTypes' has not been provided or has been
#            provided as an empty list
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceRequirements' has been provided
#       And: For the same entry in 'Overrides', 'AllowedInstanceTypes' has been provided as a non-empty list
#       And: An entry in 'AllowedInstanceTypes' is set to an instance type other than a Nitro instance type
#            that supports encryption in-transit between instances
#      Then: FAIL
#   Scenario: 7
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceType' has been provided and set to a Nitro instance type
#            that supports encryption in-transit between instances
#      Then: PASS
#   Scenario: 8
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EC2 auto scaling group resource
#       And: 'Overrides' in 'MixedInstancesPolicy.LaunchTemplate' has been provided as a non-empty list
#       And: For an entry in 'Overrides', 'InstanceRequirements' has been provided
#       And: For the same entry in 'Overrides', 'AllowedInstanceTypes' has been provided as a non-empty list
#       And: Every entry in 'AllowedInstanceTypes' is set to a Nitro instance type that
#            supports encryption in-transit between instances
#      Then: PASS

#
# Constants
#
let INPUT_DOCUMENT = this
let AUTOSCALING_GROUP_TYPE = "AWS::AutoScaling::AutoScalingGroup"
let NITRO_ENCRYPTION_IN_TRANSIT_INSTANCE_TYPES = [
    /^c5a\..+?$/, /^c5ad\..+?$/, /^c5n\..+?$/, /^c6a\..+?$/, /^c6gn\..+?$/, /^c6i\..+?$/,
    /^c6id\..+?$/, /^c6in\..+?$/, /^c7a\..+?$/, /^c7g\..+?$/, /^c7gd\..+?$/, /^c7gn\..+?$/,
    /^c7i-flex\..+?$/, /^c7i\..+?$/, /^c8g\..+?$/, /^c8gd\..+?$/, /^c8gn\..+?$/,
    /^d3\..+?$/, /^d3en\..+?$/, /^dl1\..+?$/, /^dl2q\..+?$/,
    /^f2\..+?$/,
    /^g4ad\..+?$/, /^g4dn\..+?$/, /^g5\..+?$/, /^g6\..+?$/, /^g6e\..+?$/, /^g6f\..+?$/,
    /^gr6\..+?$/, /^gr6f\..+?$/,
    /^hpc6a\..+?$/, /^hpc6id\..+?$/, /^hpc7a\..+?$/, /^hpc7g\..+?$/,
    /^i3en\..+?$/, /^i4g\..+?$/, /^i4i\..+?$/, /^i7i\..+?$/, /^i7ie\..+?$/, /^i8g\..+?$/,
    /^im4gn\..+?$/, /^inf1\..+?$/, /^inf2\..+?$/, /^is4gen\..+?$/,
    /^m5dn\..+?$/, /^m5n\..+?$/, /^m5zn\..+?$/, /^m6a\..+?$/, /^m6i\..+?$/, /^m6id\..+?$/,
    /^m6idn\..+?$/, /^m6in\..+?$/, /^m7a\..+?$/, /^m7g\..+?$/, /^m7gd\..+?$/,
    /^m7i-flex\..+?$/, /^m7i\..+?$/, /^m8g\..+?$/, /^m8gd\..+?$/,
    /^p3dn\..+?$/, /^p4d\..+?$/, /^p4de\..+?$/, /^p5\..+?$/, /^p5e\..+?$/, /^p5en\..+?$/,
    /^p6-b200\..+?$/,
    /^r5dn\..+?$/, /^r5n\..+?$/, /^r6a\..+?$/, /^r6i\..+?$/, /^r6id\..+?$/, /^r6idn\..+?$/,
    /^r6in\..+?$/, /^r7a\..+?$/, /^r7g\..+?$/, /^r7gd\..+?$/, /^r7i\..+?$/, /^r7iz\..+?$/,
    /^r8g\..+?$/, /^r8gd\..+?$/, /^r8i-flex\..+?$/, /^r8i\..+?$/,
    /^trn1\..+?$/, /^trn1n\..+?$/, /^trn2\..+?$/,
    /^u-12tb1\..+?$/, /^u-18tb1\..+?$/, /^u-24tb1\..+?$/, /^u-3tb1\..+?$/, /^u-6tb1\..+?$/,
    /^u-9tb1\..+?$/, /^u7i-12tb\..+?$/, /^u7i-6tb\..+?$/, /^u7i-8tb\..+?$/,
    /^u7in-16tb\..+?$/, /^u7in-24tb\..+?$/, /^u7in-32tb\..+?$/,
    /^vt1\..+?$/,
    /^x2idn\..+?$/, /^x2iedn\..+?$/, /^x2iezn\..+?$/, /^x8g\..+?$/
]

#
# Assignments
#
let autoscaling_groups = Resources.*[ Type == %AUTOSCALING_GROUP_TYPE ]

#
# Primary Rules
#
rule autoscaling_group_nitro_encryption_in_transit_override_check when is_cfn_template(%INPUT_DOCUMENT)
                                                                       %autoscaling_groups not empty {
    check(%autoscaling_groups.Properties)
        <<
        [CT.AUTOSCALING.PR.11]: Require an Amazon EC2 instance to use a Nitro instance type that supports encryption in transit between instances when created using the
        'AWS::AutoScaling::AutoScalingGroup' resource type
        [FIX]: In 'MixedInstancesPolicy.LaunchTemplate' with one or more 'Overrides' that include 'InstanceType' or 'InstanceRequirements', set either 'InstanceType' to an Amazon EC2 instance type based on
        the AWS Nitro system that supports encryption in-transit between instances, or set 'AllowedInstanceTypes' in 'InstanceRequirements' to one or more Amazon EC2 instance types based on the AWS Nitro system
        that supports encryption in-transit between instances.
        >>
}

rule autoscaling_group_nitro_encryption_in_transit_override_check when is_cfn_hook(%INPUT_DOCUMENT, %AUTOSCALING_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%AUTOSCALING_GROUP_TYPE.resourceProperties)
        <<
        [CT.AUTOSCALING.PR.11]: Require an Amazon EC2 instance to use a Nitro instance type that supports encryption in transit between instances when created using the
        'AWS::AutoScaling::AutoScalingGroup' resource type
        [FIX]: In 'MixedInstancesPolicy.LaunchTemplate' with one or more 'Overrides' that include 'InstanceType' or 'InstanceRequirements', set either 'InstanceType' to an Amazon EC2 instance type based on the AWS Nitro
        system that supports encryption in-transit between instances, or set 'AllowedInstanceTypes' in 'InstanceRequirements' to one or more Amazon EC2 instance types based on the AWS Nitro system
        that supports encryption in-transit between instances.
        >>
}

#
# Parameterized Rules
#
rule check(autoscaling_group) {
    %autoscaling_group [
        # Scenarios 2 and 3
        filter_launch_template_overrides(this)
    ] {
        MixedInstancesPolicy {
            LaunchTemplate {
                Overrides[ InstanceType exists ] {
                    # Scenarios 4 and 7
                    InstanceType in %NITRO_ENCRYPTION_IN_TRANSIT_INSTANCE_TYPES
                }
                Overrides[ InstanceRequirements exists ] {
                    InstanceRequirements {
                        # Scenarios 5, 6 and 8
                        AllowedInstanceTypes exists
                        AllowedInstanceTypes is_list
                        AllowedInstanceTypes not empty
                        AllowedInstanceTypes[*] in %NITRO_ENCRYPTION_IN_TRANSIT_INSTANCE_TYPES
                    }
                }
            }
        }
    }
}

rule filter_launch_template_overrides(autoscaling_group) {
    %autoscaling_group {
        MixedInstancesPolicy exists
        MixedInstancesPolicy is_struct

        MixedInstancesPolicy {
            LaunchTemplate exists
            LaunchTemplate is_struct

            LaunchTemplate {
                Overrides exists
                Overrides is_list
                Overrides not empty

                some Overrides[*] {
                    InstanceType exists or
                    InstanceRequirements exists
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
        AWSTemplateFormatVersion exists or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.AUTOSCALING.PR.11 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value 'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceType: c5a.large
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```

PASS Example - Use this template to verify a compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value 'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceRequirements:
              AllowedInstanceTypes:
              - m6a.*
              - c5a.*
              VCpuCount:
                Min: 2
                Max: 4
              MemoryMiB:
                Min: 4000
                Max: 8000
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value 'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceType: t2.micro
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Parameters:
  LatestAmiId:
    Description: Region specific latest AMI ID from the Parameter Store
    Type: AWS::SSM::Parameter::Value 'AWS::EC2::Image::Id'
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
  LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        ImageId:
          Ref: LatestAmiId
  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId:
              Ref: LaunchTemplate
            Version:
              Fn::GetAtt: LaunchTemplate.LatestVersionNumber
          Overrides:
          - InstanceRequirements:
              AllowedInstanceTypes:
              - c4.large
              VCpuCount:
                Max: 16
                Min: 1
              MemoryMiB:
                Min: 1000
                Max: 17000
      MaxSize: 1
      MinSize: 0
      DesiredCapacity: 1
      VPCZoneIdentifier:
      - Ref: Subnet


```
