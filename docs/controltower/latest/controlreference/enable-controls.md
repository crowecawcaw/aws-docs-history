# Enable controls with AWS CloudFormation

You can enable controls with AWS CloudFormation, either through the AWS CloudFormation console, or through the
AWS CLI. This section gives an example of each type.

Each control in AWS Control Tower has a unique identifier for use with the control APIs. The
identifier for each control is shown in the **API controlIdentifier**
field, on the **Control details** page in the AWS Control Tower console. This
identifier is distinct from the **ControlID** field, which is a
classification system for controls.

For more information about control identifiers, see [Resource identifiers for APIs and controls](control-identifiers.md "control-identifiers.md").

## Create the stack through AWS CloudFormation

You can use AWS CloudFormation to help you enable AWS Control Tower controls. Here's an example
template.

```
Resources:
    TestControl:
        Type: AWS::ControlTower::EnabledControl
        Properties:
            ControlIdentifier: arn:aws:controltower:us-west-2::control/AWS-GR_RESTRICT_ROOT_USER
            TargetIdentifier: arn:aws:organizations::123456789012:ou/o-ybfpt9XXXl/ou-XXXc-nlqXXXXX
```

To create your stack through the AWS CloudFormation console, edit the template to contain the
control and target of your choice, then save the template with the file name
`template.yaml`. Follow the AWS CloudFormation wizard. When the wizard asks for a
template file, enter the file you saved as `template.yaml`. For more
information, see [Creating
a stack on the Amazon CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").

###### Note

The limit for `EnableControl` and `DisableControl`
updates in AWS Control Tower is 100 concurrent operations.

## Create the stack through AWS CloudFormation and the AWS CLI

Here's an example of creating the stack with the CLI.

```
aws cloudformation create-stack --region us-west-2 --stack-name testControlTower --template-body "$(cat << TEMPLATE
Resources:
  TestControl:
    Type: AWS::ControlTower::EnabledControl
    Properties:
      ControlIdentifier: arn:aws:controltower:us-west-2::control/AWS-GR_RESTRICT_ROOT_USER
      TargetIdentifier: arn:aws:organizations::123456789012:ou/o-ybfpt9XXXl/ou-XXXc-nlqXXXXX
TEMPLATE)"
```

You can also save the example template as a `template.yaml` file, then
upload your file to an Amazon S3 bucket. Later, you can provide the URL for the bucket
with the `--template-url` flag.

When you enter your template into the wizard or through the CLI, if the stack is
created, it means that the control was enabled.

**View the progress of your stack through the AWS
CLI:**

```
aws cloudformation describe-stack-events --region us-west-2 --stack-name testControlTower
```

or

```
aws cloudformation describe-stacks --region us-west-2 --stack-name testControlTower
```

**Delete the stack through the AWS CLI:**

```
aws cloudformation delete-stack --region us-west-2 --stack-name testControlTower
```

## Configure controls with AWS CloudFormation

The following examples show how to configure controls through AWS CloudFormation templates. These examples happen to show **Value** as a list, but it can be any of several types.

### Enable configurable controls with AWS CloudFormation templates

Enable a control with parameters through AWS CloudFormation:

```
aws cloudformation create-stack \
    --stack-name ExampleStack \
    --template-body file://ExampleStack.yml \
    --region us-east-1
```

**Example templates in YAML and JSON:**

```

Resources:
  MyExampleControl:
    Properties:
      ControlIdentifier: arn:aws:controltower:us-east-1::control/EXAMPLE_NAME
      TargetIdentifier: arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2
      Parameters:
      - Key: AllowedRegions
        Value:
        - us-east-1
        - us-west-1
      - Key: ExemptedPrincipalArns
        Value:
        - arn:aws:iam::*:role/ReadOnly
      - Key: ExemptedActions
        Value:
        - logs:DescribeLogGroups
        - logs:StartQuery
        - logs:GetQueryResults
    Type: AWS::ControlTower::EnabledControl



{
  "Resources": {
    "MyExampleControl": {
      "Type": "AWS::ControlTower::EnabledControl",
      "Properties": {
        "TargetIdentifier": "arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2",
        "ControlIdentifier": "arn:aws:controltower:us-east-1::control/EXAMPLE_NAME",
        "Parameters": [
          {
            "Key": "AllowedRegions",
            "Value": [
              "us-east-1",
              "us-west-1"
            ]
          },
          {
            "Key": "ExemptedPrincipalArns",
            "Value": [
              "arn:aws:iam::*:role/ReadOnly"
            ]
          },
          {
            "Key": "ExemptedActions",
            "Value": [
              "logs:DescribeLogGroups",
              "logs:StartQuery",
              "logs:GetQueryResults"
            ]
          }
        ]
      }
    }
  }
}

```
