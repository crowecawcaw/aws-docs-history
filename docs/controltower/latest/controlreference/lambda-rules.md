# AWS Lambda controls

###### Topics

- [[CT.LAMBDA.PR.2] Require AWS Lambda function policies to prohibit public access](#ct-lambda-pr-2-description "#ct-lambda-pr-2-description")
- [[CT.LAMBDA.PR.3] Require an AWS Lambda function to be in a customer-managed Amazon Virtual Private Cloud (VPC)](#ct-lambda-pr-3-description "#ct-lambda-pr-3-description")
- [[CT.LAMBDA.PR.4] Require an AWS Lambda layer permission to grant access to
  an AWS organization or specific AWS account](#ct-lambda-pr-4-description "#ct-lambda-pr-4-description")
- [[CT.LAMBDA.PR.5] Require an AWS Lambda function URL to
  use AWS IAM-based authentication](#ct-lambda-pr-5-description "#ct-lambda-pr-5-description")
- [[CT.LAMBDA.PR.6] Require an AWS Lambda function URL CORS policy to restrict access to
  specific origins](#ct-lambda-pr-6-description "#ct-lambda-pr-6-description")

## [CT.LAMBDA.PR.2] Require AWS Lambda function policies to prohibit public access

This control checks whether an AWS Lambda function resource-based policy prohibits public access.

- **Control objective:** Limit network access
- **Implementation:** CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Lambda::Permission`
- **CloudFormation guard rule:**
  [CT.LAMBDA.PR.2 rule specification](#ct-lambda-pr-2-rule "#ct-lambda-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.LAMBDA.PR.2 rule specification](#ct-lambda-pr-2-rule "#ct-lambda-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.LAMBDA.PR.2 example templates](#ct-lambda-pr-2-templates "#ct-lambda-pr-2-templates")

**Explanation**

The Lambda function should not be publicly accessible, because it may permit unintended access to your code stored in the function.

### Remediation for rule failure

When setting `Principal` to `*`, provide one of `SourceAccount`, `SourceArn`, or `PrincipalOrgID`. When setting `Principal` to a service principal (for example, s3.amazonaws.com), provide one of `SourceAccount` or `SourceArn`.

The examples that follow show how to implement this remediation.

#### AWS Lambda Function Policy - Example One

AWS Lambda function policy configured with an AWS account ID principal. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LambdaPermission": {
        "Type": "AWS::Lambda::Permission",
        "Properties": {
            "Action": "lambda:InvokeFunction",
            "FunctionName": {
                "Ref": "LambdaFunction"
            },
            "Principal": {
                "Ref": "AWS::AccountId"
            }
        }
    }
}

```

**YAML example**

```

LambdaPermission:
  Type: AWS::Lambda::Permission
  Properties:
    Action: lambda:InvokeFunction
    FunctionName: !Ref 'LambdaFunction'
    Principal: !Ref 'AWS::AccountId'


```

The examples that follow show how to implement this remediation.

#### AWS Lambda Function Policy - Example Two

AWS Lambda function policy configured with a wildcard principal and source account condition. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LambdaPermission": {
        "Type": "AWS::Lambda::Permission",
        "Properties": {
            "Action": "lambda:InvokeFunction",
            "FunctionName": {
                "Ref": "LambdaFunction"
            },
            "Principal": "*",
            "SourceAccount": {
                "Ref": "AWS::AccountId"
            }
        }
    }
}

```

**YAML example**

```

LambdaPermission:
  Type: AWS::Lambda::Permission
  Properties:
    Action: lambda:InvokeFunction
    FunctionName: !Ref 'LambdaFunction'
    Principal: '*'
    SourceAccount: !Ref 'AWS::AccountId'


```

The examples that follow show how to implement this remediation.

#### AWS Lambda Function Policy - Example Three

AWS Lambda function policy configured with a service principal and source ARN condition. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LambdaPermission": {
        "Type": "AWS::Lambda::Permission",
        "Properties": {
            "Action": "lambda:InvokeFunction",
            "FunctionName": {
                "Ref": "LambdaFunction"
            },
            "Principal": "s3.amazonaws.com",
            "SourceArn": {
                "Fn::GetAtt": [
                    "S3Bucket",
                    "Arn"
                ]
            }
        }
    }
}

```

**YAML example**

```

LambdaPermission:
  Type: AWS::Lambda::Permission
  Properties:
    Action: lambda:InvokeFunction
    FunctionName: !Ref 'LambdaFunction'
    Principal: s3.amazonaws.com
    SourceArn: !GetAtt 'S3Bucket.Arn'


```

### CT.LAMBDA.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   lambda_function_public_access_prohibited_check
#
# Description:
#   This control checks whether an AWS Lambda function resource-based policy prohibits public access.
#
# Reports on:
#   AWS::Lambda::Permission
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
#       And: The input document does not contain any Lambda permission resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda permission resource
#       And: 'FunctionUrlAuthType' has been provided with a value of 'NONE'
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda permission resource
#       And: 'Principal' has been provided with a wildcard value ('*')
#       And: 'SourceAccount' has not been provided or provided with an empty string value
#       And: 'SourceArn' has not been provided or provided with an empty string value or non-valid local reference
#       And: 'PrincipalOrgID' has not been provided or provided with an empty string value
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda permission resource
#       And: 'Principal' has been provided with value that does not match an AWS Account ID, AWS IAM ARN or
#            wildcard value ('*')
#       And: 'SourceAccount' has not been provided or provided with an empty string value
#       And: 'SourceArn' has not been provided or provided with an empty string value or non-valid local reference
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda permission resource
#       And: 'Principal' has been provided with an AWS Account ID or AWS IAM ARN value
#      Then: PASS
#   Scenario: 6
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda permission resource
#       And: 'Principal' has been provided with a wildcard value ('*')
#       And: At least one of 'SourceAccount', 'SourceArn' or 'PrincipalOrgID' have been provided with non-empty string
#            values (or a valid local reference for 'SourceArn')
#      Then: PASS
#   Scenario: 7
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda permission resource
#       And: 'Principal' has been provided with value that does not match an AWS Account ID or AWS IAM ARN
#       And: At least one of 'SourceAccount', 'SourceArn' have been provided with non-empty string values (or a valid
#            local reference for 'SourceArn')
#      Then: PASS

#
# Constants
#
let LAMBDA_PERMISSION_TYPE = "AWS::Lambda::Permission"
let AWS_ACCOUNT_ID_PATTERN = /\d{12}/
let AWS_IAM_PRINCIPAL_PATTERN = /^arn:aws[a-z0-9\-]*:iam::\d{12}:.+/

let INPUT_DOCUMENT = this

#
# Assignments
#
let lambda_permissions = Resources.*[ Type == %LAMBDA_PERMISSION_TYPE ]

#
# Primary Rules
#
rule lambda_function_public_access_prohibited_check when is_cfn_template(%INPUT_DOCUMENT)
                                                         %lambda_permissions not empty {
    check(%lambda_permissions.Properties)
        <<
        [CT.LAMBDA.PR.2]: Require AWS Lambda function policies to prohibit public access
        [FIX]: When setting 'Principal' to '*', provide one of 'SourceAccount', 'SourceArn', or 'PrincipalOrgID'. When setting 'Principal' to a service principal (for example, s3.amazonaws.com), provide one of 'SourceAccount' or 'SourceArn'.
        >>
}

rule lambda_function_public_access_prohibited_check when is_cfn_hook(%INPUT_DOCUMENT, %LAMBDA_PERMISSION_TYPE) {
    check(%INPUT_DOCUMENT.%LAMBDA_PERMISSION_TYPE.resourceProperties)
        <<
        [CT.LAMBDA.PR.2]: Require AWS Lambda function policies to prohibit public access
        [FIX]: When setting 'Principal' to '*', provide one of 'SourceAccount', 'SourceArn', or 'PrincipalOrgID'. When setting 'Principal' to a service principal (for example, s3.amazonaws.com), provide one of 'SourceAccount' or 'SourceArn'.
        >>
}

#
# Parameterized Rules
#
rule check(lambda_permission) {
    %lambda_permission {
        # Scenario 2 and 5
        FunctionUrlAuthType not exists or
        FunctionUrlAuthType != "NONE"
    }

    %lambda_permission [
        Principal exists
        Principal == "*"
    ] {
        # Scenario 3 and 6
        SourceAccount exists or
        SourceArn exists or
        PrincipalOrgID exists

        check_is_string_and_not_empty(SourceAccount) or
        check_is_string_or_local_reference(SourceArn) or
        check_is_string_and_not_empty(PrincipalOrgID)
    }

    %lambda_permission [
        Principal exists
        Principal != "*"
        Principal != %AWS_ACCOUNT_ID_PATTERN
        Principal != %AWS_IAM_PRINCIPAL_PATTERN
    ] {
        # Scenario 4 and 7
        SourceAccount exists or
        SourceArn exists

        check_is_string_and_not_empty(SourceAccount) or
        check_is_string_or_local_reference(SourceArn)
    }
}

rule check_is_string_or_local_reference(value) {
    %value {
        check_is_string_and_not_empty(this) or
        check_local_references(%INPUT_DOCUMENT, this)
    }
}

rule check_local_references(doc, reference_properties) {
    %reference_properties {
        'Fn::GetAtt' {
            query_for_resource(%doc, this[0])
                <<Local Stack reference was invalid>>
        } or Ref {
            query_for_resource(%doc, this)
                <<Local Stack reference was invalid>>
        }
    }
}

rule query_for_resource(doc, resource_key) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
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

### CT.LAMBDA.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Runtime: python3.9
      Code:
        ZipFile: "def handler(event, context):\n  print(\"hello\")\n"
      Description: TestS3EventFunction
  LambdaPermission:
    Type: AWS::Lambda::Permission
    Properties:
      Action: lambda:InvokeFunction
      FunctionName:
        Ref: LambdaFunction
      Principal:
        Ref: AWS::AccountId


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Runtime: python3.9
      Code:
        ZipFile: "def handler(event, context):\n  print(\"hello\")\n"
      Description: TestS3EventFunction
  LambdaPermission:
    Type: AWS::Lambda::Permission
    Properties:
      Action: lambda:InvokeFunction
      FunctionName:
        Ref: LambdaFunction
      Principal: '*'


```

## [CT.LAMBDA.PR.3] Require an AWS Lambda function to be in a customer-managed Amazon Virtual Private Cloud (VPC)

This control checks whether an AWS Lambda function has been configured with access to resources in a customer-managed Amazon Virtual Private Cloud (VPC).

- **Control objective:** Limit network access
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Lambda::Function`
- **CloudFormation guard rule:**
  [CT.LAMBDA.PR.3 rule specification](#ct-lambda-pr-3-rule "#ct-lambda-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.LAMBDA.PR.3 rule specification](#ct-lambda-pr-3-rule "#ct-lambda-pr-3-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.LAMBDA.PR.3 example templates](#ct-lambda-pr-3-templates "#ct-lambda-pr-3-templates")

**Explanation**

AWS Lambda functions can be linked to private subnets within a virtual private cloud (VPC) in your AWS account to connect to resources such as databases, cache instances, or internal services. Ensure that the subnets and security groups used allow access to the necessary resources.

###### Usage considerations

- This control does not evaluate the VPC subnet routing configuration to determine public reachability.
- This control does not support AWS Lambda@Edge Functions. Lambda@Edge does not support functions that are configured with access to resources inside your VPC.
- Lambda functions can't connect directly to a VPC with dedicated instance tenancy. To connect to resources in a dedicated VPC, peer it to a second VPC with default tenancy.

### Remediation for rule failure

In `VpcConfig`, provide the `SubnetIds` property with one or more Subnet IDs, and provide the `SecurityGroupIds` property with one or more Security Group IDs.

The examples that follow show how to implement this remediation.

#### AWS Lambda Function - Example

AWS Lambda function configured to access resources in a VPC. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LambdaFunction": {
        "Type": "AWS::Lambda::Function",
        "Properties": {
            "Role": {
                "Fn::GetAtt": "LambdaFunctionRole.Arn"
            },
            "Handler": "index.handler",
            "Code": {
                "ZipFile": "def handler(event, context):\n    print(\"sample function\")\n"
            },
            "Runtime": "python3.9",
            "VpcConfig": {
                "SubnetIds": [
                    {
                        "Fn::GetAtt": [
                            "SubnetOne",
                            "SubnetId"
                        ]
                    },
                    {
                        "Fn::GetAtt": [
                            "SubnetTwo",
                            "SubnetId"
                        ]
                    }
                ],
                "SecurityGroupIds": [
                    {
                        "Fn::GetAtt": [
                            "SecurityGroup",
                            "GroupId"
                        ]
                    }
                ]
            }
        }
    }
}

```

**YAML example**

```

LambdaFunction:
  Type: AWS::Lambda::Function
  Properties:
    Role: !GetAtt 'LambdaFunctionRole.Arn'
    Handler: index.handler
    Code:
      ZipFile: "def handler(event, context):\n    print(\"sample function\")\n"
    Runtime: python3.9
    VpcConfig:
      SubnetIds:
        - !GetAtt 'SubnetOne.SubnetId'
        - !GetAtt 'SubnetTwo.SubnetId'
      SecurityGroupIds:
        - !GetAtt 'SecurityGroup.GroupId'


```

### CT.LAMBDA.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   lambda_inside_vpc_check
#
# Description:
#   This control checks whether an AWS Lambda function has been configured with access to resources in a customer-managed Amazon Virtual Private Cloud (VPC).
#
# Reports on:
#   AWS::Lambda::Function
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
#       And: The input document does not contain any Lambda function resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function resource
#       And: 'VpcConfig' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function resource
#       And: 'VpcConfig' has been provided
#       And: 'SubnetIds' in 'VpcConfig' has been provided as a non-empty list that contains non-empty strings or valid
#            local references
#       And: 'SecurityGroupIds' in 'VpcConfig' has not been been provided or has been provided as an empty list
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function resource
#       And: 'VpcConfig' has been provided
#       And: 'SecurityGroupIds' in 'VpcConfig' has been provided as a non-empty list that contains non-empty strings
#            or valid local references
#       And: 'SubnetIds' in 'VpcConfig' has not been been provided or has been provided as an empty list
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function resource
#       And: 'VpcConfig' has been provided
#       And: 'SecurityGroupIds' in 'VpcConfig' has been provided as a non-empty list that contains non-empty strings or
#            valid local references
#       And: 'SubnetIds' in 'VpcConfig' has been provided as a non-empty list that contains non-empty strings or valid
#            local references
#      Then: PASS

#
# Constants
#
let LAMBDA_FUNCTION_TYPE = "AWS::Lambda::Function"
let INPUT_DOCUMENT = this

#
# Assignments
#
let lambda_functions = Resources.*[ Type == %LAMBDA_FUNCTION_TYPE ]

#
# Primary Rules
#
rule lambda_inside_vpc_check when is_cfn_template(%INPUT_DOCUMENT)
                                  %lambda_functions not empty {
    check(%lambda_functions.Properties)
        <<
        [CT.LAMBDA.PR.3]: Require an AWS Lambda function to be in a customer-managed Amazon Virtual Private Cloud (VPC)
        [FIX]: In 'VpcConfig', provide the 'SubnetIds' property with one or more Subnet IDs, and provide the 'SecurityGroupIds' property with one or more Security Group IDs.
        >>
}

rule lambda_inside_vpc_check when is_cfn_hook(%INPUT_DOCUMENT, %LAMBDA_FUNCTION_TYPE) {
    check(%INPUT_DOCUMENT.%LAMBDA_FUNCTION_TYPE.resourceProperties)
        <<
        [CT.LAMBDA.PR.3]: Require an AWS Lambda function to be in a customer-managed Amazon Virtual Private Cloud (VPC)
        [FIX]: In 'VpcConfig', provide the 'SubnetIds' property with one or more Subnet IDs, and provide the 'SecurityGroupIds' property with one or more Security Group IDs.
        >>
}

#
# Parameterized Rules
#
rule check(lambda_function) {
    %lambda_function {
        # Scenario 2
        VpcConfig exists
        VpcConfig is_struct

        VpcConfig {
            # Scenario 3 and 5
            SubnetIds exists
            SubnetIds is_list
            SubnetIds not empty
            SubnetIds[*] {
                check_is_string_and_not_empty(this) or
                check_local_references(%INPUT_DOCUMENT, this, "AWS::EC2::Subnet")
            }
            # Scenario 4 and 5
            SecurityGroupIds exists
            SecurityGroupIds is_list
            SecurityGroupIds not empty
            SecurityGroupIds[*] {
                check_is_string_and_not_empty(this) or
                check_local_references(%INPUT_DOCUMENT, this, "AWS::EC2::SecurityGroup")
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

### CT.LAMBDA.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  SubnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetTwo:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ''
  SecurityGroup1:
    Type: AWS::EC2::SecurityGroup
    Properties:
      VpcId:
        Ref: VPC
      GroupDescription:
        Fn::Sub: ${AWS::StackName}-example
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            - ec2:CreateNetworkInterface
            - ec2:DescribeNetworkInterfaces
            - ec2:DeleteNetworkInterface
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Code:
        ZipFile: |
          def handler(event, context):
              print("example")
      Runtime: python3.9
      VpcConfig:
        SubnetIds:
        - Fn::GetAtt:
          - SubnetOne
          - SubnetId
        - Fn::GetAtt:
          - SubnetTwo
          - SubnetId
        SecurityGroupIds:
        - Fn::GetAtt:
          - SecurityGroup1
          - GroupId


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            - ec2:CreateNetworkInterface
            - ec2:DescribeNetworkInterfaces
            - ec2:DeleteNetworkInterface
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Code:
        ZipFile: |
          def handler(event, context):
              print("example")
      Runtime: python3.9


```

## [CT.LAMBDA.PR.4] Require an AWS Lambda layer permission to grant access to

an AWS organization or specific AWS account

This control checks whether an AWS Lambda layer permission has been configured to grant
access to an AWS organization or to a specific AWS account only, by ensuring that public access
from all AWS accounts has not been granted to a layer.

- **Control objective:** Enforce least privilege
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Lambda::LayerVersionPermission`
- **CloudFormation guard rule:**
  [CT.LAMBDA.PR.4 rule specification](#ct-lambda-pr-4-rule "#ct-lambda-pr-4-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.LAMBDA.PR.4 rule specification](#ct-lambda-pr-4-rule "#ct-lambda-pr-4-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.LAMBDA.PR.4 example templates](#ct-lambda-pr-4-templates "#ct-lambda-pr-4-templates")

**Explanation**

By default, a layer that you create is **private** to your AWS account. However, you can
share the layer with other accounts or make it public, optionally.

A **public** layer may allow unintended access to your
source code and applications. A public Lambda layer can expose valuable information
about your account, resources, and internal processes.

### Remediation for rule failure

Set the `OrganizationId` parameter to the ID of an AWS organization, or
set the `Principal` parameter to an AWS account ID.

The examples that follow show how to implement this remediation.

#### AWS Lambda layer permission - Example one

An AWS Lambda version permission URL configured to grant layer usage permission
to all accounts in an organization. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LayerVersionPermission": {
        "Type": "AWS::Lambda::LayerVersionPermission",
        "Properties": {
            "Action": "lambda:GetLayerVersion",
            "LayerVersionArn": {
                "Ref": "LayerVersion"
            },
            "OrganizationId": "o-abc123defg"
        }
    }
}

```

**YAML example**

```

LayerVersionPermission:
  Type: AWS::Lambda::LayerVersionPermission
  Properties:
    Action: lambda:GetLayerVersion
    LayerVersionArn: !Ref 'LayerVersion'
    OrganizationId: o-abc123defg


```

The examples that follow show how to implement this remediation.

#### AWS Lambda layer permission - Example two

An AWS Lambda version permission URL configured to grant layer usage permission
for an AWS account. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "LayerVersionPermission": {
        "Type": "AWS::Lambda::LayerVersionPermission",
        "Properties": {
            "Action": "lambda:GetLayerVersion",
            "LayerVersionArn": {
                "Ref": "LayerVersion"
            },
            "Principal": "123456789012"
        }
    }
}

```

**YAML example**

```

LayerVersionPermission:
  Type: AWS::Lambda::LayerVersionPermission
  Properties:
    Action: lambda:GetLayerVersion
    LayerVersionArn: !Ref 'LayerVersion'
    Principal: '123456789012'


```

### CT.LAMBDA.PR.4 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   lambda_layer_public_access_prohibited_check
#
# Description:
#   This control checks whether an AWS Lambda layer permission has been configured to grant access to an AWS organization or to a specific AWS account only, by ensuring that public access from all AWS accounts has not been granted to a layer.
#
# Reports on:
#   AWS::Lambda::LayerVersionPermission
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
#       And: The input document does not contain any Lambda layer version permission resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda layer version permission resource
#       And: 'OrganizationId' has not been provided
#       And: 'Principal' has been provided and set to '*'
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda layer version permission resource
#       And: 'OrganizationId' has not been provided
#       And: 'Principal' has been provided and set to a non-empty string value other than '*'
#      Then: PASS
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda layer version permission resource
#       And: 'OrganizationId' has been provided as a non-empty string
#      Then: PASS

#
# Constants
#
let LAMBDA_LAYER_PERMISSION_TYPE = "AWS::Lambda::LayerVersionPermission"
let INPUT_DOCUMENT = this

#
# Assignments
#
let lambda_layer_permissions = Resources.*[ Type == %LAMBDA_LAYER_PERMISSION_TYPE ]

#
# Primary Rules
#
rule lambda_layer_public_access_prohibited_check when is_cfn_template(%INPUT_DOCUMENT)
                                                      %lambda_layer_permissions not empty {
    check(%lambda_layer_permissions.Properties)
        <<
        [CT.LAMBDA.PR.4]: Require an AWS Lambda layer permission to grant access to an AWS organization or specific AWS account
        [FIX]: Set the 'OrganizationId' parameter to the ID of an AWS organization, or set the 'Principal' parameter to an AWS account ID.
        >>
}

rule lambda_layer_public_access_prohibited_check when is_cfn_hook(%INPUT_DOCUMENT, %LAMBDA_LAYER_PERMISSION_TYPE) {
    check(%INPUT_DOCUMENT.%LAMBDA_LAYER_PERMISSION_TYPE.resourceProperties)
        <<
        [CT.LAMBDA.PR.4]: Require an AWS Lambda layer permission to grant access to an AWS organization or specific AWS account
        [FIX]: Set the 'OrganizationId' parameter to the ID of an AWS organization, or set the 'Principal' parameter to an AWS account ID.
        >>
}

#
# Parameterized Rules
#
rule check(lambda_layer_permission) {
    %lambda_layer_permission [
        OrganizationId not exists
    ] {
        # Scenarios 2 and 3
        Principal exists
        check_is_string_and_not_empty(Principal)
        Principal != "*"
    }
    %lambda_layer_permission [
        OrganizationId exists
    ] {
        # Scenario 4
        check_is_string_and_not_empty(OrganizationId)
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

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}


```

### CT.LAMBDA.PR.4 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  LayerVersion:
    Type: AWS::Lambda::LayerVersion
    Properties:
      CompatibleRuntimes:
      - python3.9
      Content:
        S3Bucket: example-layer-bucket
        S3Key: layer.zip
      Description: Example layer
      LayerName: example-layer
      LicenseInfo: MIT
  LayerVersionPermission:
    Type: AWS::Lambda::LayerVersionPermission
    Properties:
      Action: lambda:GetLayerVersion
      LayerVersionArn:
        Ref: LayerVersion
      OrganizationId: o-abc123defg
      Principal: "*"


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  LayerVersion:
    Type: AWS::Lambda::LayerVersion
    Properties:
      CompatibleRuntimes:
      - python3.9
      Content:
        S3Bucket: example-layer-bucket
        S3Key: layer.zip
      Description: Example layer
      LayerName: example-layer
      LicenseInfo: MIT
  LayerVersionPermission:
    Type: AWS::Lambda::LayerVersionPermission
    Properties:
      Action: lambda:GetLayerVersion
      LayerVersionArn:
        Ref: LayerVersion
      Principal: "*"


```

## [CT.LAMBDA.PR.5] Require an AWS Lambda function URL to

use AWS IAM-based authentication

This control checks whether an AWS Lambda function URL is configured to use authentication that's
based on IAM.

- **Control objective:** Enforce least privilege
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Lambda::Url`
- **CloudFormation guard rule:**
  [CT.LAMBDA.PR.5 rule specification](#ct-lambda-pr-5-rule "#ct-lambda-pr-5-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.LAMBDA.PR.5 rule specification](#ct-lambda-pr-5-rule "#ct-lambda-pr-5-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.LAMBDA.PR.5 example templates](#ct-lambda-pr-5-templates "#ct-lambda-pr-5-templates")

**Explanation**

You can control access to a Lambda function URL using the `AuthType` parameter,
combined with resource-based policies that are attached to your specific function. The
configuration of these two components determines who can invoke or perform other administrative
actions on your function URL.

The `AuthType` parameter determines how Lambda authenticates or authorizes
requests to your Lambda function URL (endpoint). Setting `AuthType` to
`NONE` means that Lambda does not perform any authentication before it invokes your function.
However, your function's resource-based policy is always in effect, and the policy must grant
public access before your Lambda function URL (endpoint) can receive requests.

### Remediation for rule failure

Set the `AuthType` parameter to `AWS_IAM`

The examples that follow show how to implement this remediation.

#### AWS Lambda function URL - Example

An AWS Lambda function URL (endpoint) configured with AWS IAM-based authentication.
The example is shown in JSON and in YAML.

**JSON example**

```

{
    "FunctionUrl": {
        "Type": "AWS::Lambda::Url",
        "Properties": {
            "TargetFunctionArn": {
                "Fn::GetAtt": [
                    "LambdaFunction",
                    "Arn"
                ]
            },
            "AuthType": "AWS_IAM"
        }
    }
}

```

**YAML example**

```

FunctionUrl:
  Type: AWS::Lambda::Url
  Properties:
    TargetFunctionArn: !GetAtt 'LambdaFunction.Arn'
    AuthType: AWS_IAM


```

### CT.LAMBDA.PR.5 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   lambda_function_url_auth_check
#
# Description:
#   This control checks whether an AWS Lambda function URL is configured to use authentication that's
based on AWS IAM.
#
# Reports on:
#   AWS::Lambda::Url
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
#       And: The input document does not contain any Lambda function URL resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function URL resource
#       And: 'AuthType' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function URL resource
#       And: 'AuthType' been provided and set to a value other than 'AWS_IAM'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function URL resource
#       And: 'AuthType' been provided and set to 'AWS_IAM'
#      Then: PASS

#
# Constants
#
let LAMBDA_FUNCTION_URL_TYPE = "AWS::Lambda::Url"
let AUTHORIZED_AUTHENTICATION_TYPES = ["AWS_IAM"]
let INPUT_DOCUMENT = this

#
# Assignments
#
let lambda_function_urls = Resources.*[ Type == %LAMBDA_FUNCTION_URL_TYPE ]

#
# Primary Rules
#
rule lambda_function_url_auth_check when is_cfn_template(%INPUT_DOCUMENT)
                                         %lambda_function_urls not empty {
    check(%lambda_function_urls.Properties)
        <<
        [CT.LAMBDA.PR.5]: Require an AWS Lambda function URL to use AWS IAM-based authentication
        [FIX]: Set the 'AuthType' parameter to 'AWS_IAM'
        >>
}

rule lambda_function_url_auth_check when is_cfn_hook(%INPUT_DOCUMENT, %LAMBDA_FUNCTION_URL_TYPE) {
    check(%INPUT_DOCUMENT.%LAMBDA_FUNCTION_URL_TYPE.resourceProperties)
        <<
        [CT.LAMBDA.PR.5]: Require an AWS Lambda function URL to use AWS IAM-based authentication
        [FIX]: Set the 'AuthType' parameter to 'AWS_IAM'
        >>
}

#
# Parameterized Rules
#
rule check(lambda_function_url) {
    %lambda_function_url {
        # Scenario 2
        AuthType exists
        # Scenarios 3 and 4
        AuthType in %AUTHORIZED_AUTHENTICATION_TYPES
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

### CT.LAMBDA.PR.5 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Code:
        ZipFile: "def handler(event, context):\n    print(\"example\")\n"
      Runtime: python3.9
  FunctionUrl:
    Type: AWS::Lambda::Url
    Properties:
      TargetFunctionArn:
        Fn::GetAtt:
        - LambdaFunction
        - Arn
      AuthType: AWS_IAM


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Code:
        ZipFile: "def handler(event, context):\n    print(\"example\")\n"
      Runtime: python3.9
  FunctionUrl:
    Type: AWS::Lambda::Url
    Properties:
      TargetFunctionArn:
        Fn::GetAtt:
        - LambdaFunction
        - Arn
      AuthType: NONE


```

## [CT.LAMBDA.PR.6] Require an AWS Lambda function URL CORS policy to restrict access to

specific origins

This control checks whether an AWS Lambda function URL is configured with a cross-origin resource sharing
(CORS) policy that does not grant access to all origins.

- **Control objective:** Limit network access
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Lambda::Url`
- **CloudFormation guard rule:**
  [CT.LAMBDA.PR.6 rule specification](#ct-lambda-pr-6-rule "#ct-lambda-pr-6-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.LAMBDA.PR.6 rule specification](#ct-lambda-pr-6-rule "#ct-lambda-pr-6-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.LAMBDA.PR.6 example templates](#ct-lambda-pr-6-templates "#ct-lambda-pr-6-templates")

**Explanation**

Cross-Origin Resource Sharing (CORS) is a mechanism based on an HTTP-header, which allows a server to
indicate any origins (domain, scheme, or port) other than its own, from which a browser should permit
loading resources.

If you set a wildcard origin (`*`) in a CORS policy, you allow code running in browsers
from any origin to gain access to your function URL.

### Remediation for rule failure

In the `Cors` parameter, ensure that the value of `AllowOrigins` does not
contain wildcard origins (`*`, `http://*` and `https://*`)

The examples that follow show how to implement this remediation.

#### AWS Lambda Function URL - Example

AWS Lambda function URL configured with a cross-origin resource sharing (CORS) policy that restricts access to a
specific origin. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "FunctionUrl": {
        "Type": "AWS::Lambda::Url",
        "Properties": {
            "TargetFunctionArn": {
                "Fn::GetAtt": [
                    "LambdaFunction",
                    "Arn"
                ]
            },
            "AuthType": "AWS_IAM",
            "Cors": {
                "AllowOrigins": [
                    "https://example.com"
                ]
            }
        }
    }
}

```

**YAML example**

```

FunctionUrl:
  Type: AWS::Lambda::Url
  Properties:
    TargetFunctionArn: !GetAtt 'LambdaFunction.Arn'
    AuthType: AWS_IAM
    Cors:
      AllowOrigins:
        - https://example.com


```

### CT.LAMBDA.PR.6 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   lambda_function_url_cors_check
#
# Description:
#   This control checks whether an AWS Lambda function URL is configured with a cross-origin resource sharing (CORS) policy that does not grant access to all origins.
#
# Reports on:
#   AWS::Lambda::Url
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
#       And: The input document does not contain any Lambda function URL resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function URL resource
#       And: 'AllowOrigins' in 'Cors' has not been provided or has been provided as an empty list
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function URL resource
#       And: 'Cors' has been provided
#       And: 'AllowOrigins' in 'Cors' has been provided as a non-empty list
#       And: 'AllowOrigins' has an entry that contains a wildcard value '*'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Lambda function URL resource
#       And: 'Cors' has been provided
#       And: 'AllowOrigins' in 'Cors' has been provided as a non-empty list
#       And: No entries in 'AllowOrigins' contain a wildcard value '*'
#      Then: PASS

#
# Constants
#
let LAMBDA_FUNCTION_URL_TYPE = "AWS::Lambda::Url"
let INPUT_DOCUMENT = this

#
# Assignments
#
let lambda_function_urls = Resources.*[ Type == %LAMBDA_FUNCTION_URL_TYPE ]

#
# Primary Rules
#
rule lambda_function_url_cors_check when is_cfn_template(%INPUT_DOCUMENT)
                                         %lambda_function_urls not empty {
    check(%lambda_function_urls.Properties)
        <<
        [CT.LAMBDA.PR.6]: Require an AWS Lambda function URL CORS policy to restrict access to specific origins
        [FIX]: In the 'Cors' parameter, ensure that the value of 'AllowOrigins' does not contain wildcard origins ('*', 'http://*' and 'https://*')
        >>
}

rule lambda_function_url_cors_check when is_cfn_hook(%INPUT_DOCUMENT, %LAMBDA_FUNCTION_URL_TYPE) {
    check(%INPUT_DOCUMENT.%LAMBDA_FUNCTION_URL_TYPE.resourceProperties)
        <<
        [CT.LAMBDA.PR.6]: Require an AWS Lambda function URL CORS policy to restrict access to specific origins
        [FIX]: In the 'Cors' parameter, ensure that the value of 'AllowOrigins' does not contain wildcard origins ('*', 'http://*' and 'https://*')
        >>
}

#
# Parameterized Rules
#
rule check(lambda_function_url) {
    %lambda_function_url[
        # Scenario 2
        filter_cors_origins(this)
    ] {
        Cors {
            # Scenarios 3 and 4
            AllowOrigins[*] != /\*/
        }
    }
}

rule filter_cors_origins(lambda_function_url) {
    %lambda_function_url {
        Cors exists
        Cors is_struct
        Cors {
            AllowOrigins exists
            AllowOrigins is_list
            AllowOrigins not empty
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

### CT.LAMBDA.PR.6 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Code:
        ZipFile: "def handler(event, context):\n    print(\"example\")\n"
      Runtime: python3.9
  FunctionUrl:
    Type: AWS::Lambda::Url
    Properties:
      TargetFunctionArn:
        Fn::GetAtt:
        - LambdaFunction
        - Arn
      AuthType: AWS_IAM
      Cors:
        AllowOrigins:
        - https://example.com


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  LambdaFunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: LambdaFunctionPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role:
        Fn::GetAtt: LambdaFunctionRole.Arn
      Handler: index.handler
      Code:
        ZipFile: "def handler(event, context):\n    print(\"example\")\n"
      Runtime: python3.9
  FunctionUrl:
    Type: AWS::Lambda::Url
    Properties:
      TargetFunctionArn:
        Fn::GetAtt:
        - LambdaFunction
        - Arn
      AuthType: AWS_IAM
      Cors:
        AllowOrigins:
        - '*'


```
