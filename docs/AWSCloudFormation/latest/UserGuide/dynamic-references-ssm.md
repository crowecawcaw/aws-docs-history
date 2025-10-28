# Get a plaintext value from Systems Manager Parameter

Store

When you're creating a CloudFormation template, you might want to use plaintext values
stored in Parameter Store. Parameter Store is a capability of AWS Systems Manager. For an
introduction to Parameter Store, see [AWS Systems Manager Parameter
Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the _AWS Systems Manager User Guide_.

To use a plaintext value from Parameter Store within your template, you use a
`ssm` dynamic reference. This reference allows you to access values from
parameters of type `String` or `StringList` in Parameter Store.

To verify which version of an `ssm` dynamic reference will be used in a
stack operation, create a change set for the stack operation. Then, review the processed
template on the **Template** tab. For more information, see [Create a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-create.md "using-cfn-updating-stacks-changesets-create.md").

When using `ssm` dynamic references, there are a few important things to
keep in mind:

- CloudFormation doesn't support drift detection on dynamic references. For
  `ssm` dynamic references where you haven't specified the
  parameter version, we recommend that, if you update the parameter version in
  Systems Manager, you also perform a stack update operation on any stacks that include the
  `ssm` dynamic reference, in order to fetch the latest parameter
  version.
- To use a `ssm` dynamic reference in the `Parameters`
  section of your CloudFormation template, you must include a version number.
  CloudFormation doesn't allow you to reference a Parameter Store value without a
  version number in this section. Alternatively, you can define your parameter as
  a Systems Manager parameter type in your template. When you do this, you can specify a
  Systems Manager parameter key as the default value for your parameter. CloudFormation will
  then retrieve the latest version of the parameter value from Parameter Store,
  without you having to specify a version number. This can make your templates
  simpler and easier to maintain. For more information, see [Specify existing resources at
  runtime with CloudFormation-supplied parameter types](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md").
- For custom resources, CloudFormation resolves the `ssm` dynamic
  references before sending the request to the custom resource.
- CloudFormation doesn't support using dynamic references to reference a parameter
  shared from another AWS account.
- CloudFormation doesn't support using Systems Manager parameter labels in dynamic
  references.

## Permissions

To specify a parameter stored in the Systems Manager Parameter Store, you must have
permission to call [GetParameters](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md") for the specified parameter. To learn
how to create IAM policies that provide access to specific Systems Manager parameters, see
[Restricting access to
Systems Manager parameters using IAM policies](../../../systems-manager/latest/userguide/sysman-paramstore-access.md "../../../systems-manager/latest/userguide/sysman-paramstore-access.md") in the
_AWS Systems Manager User Guide_.

## Reference pattern

To reference a plaintext value stored in Systems Manager Parameter Store in your CloudFormation
template, use the following `ssm` reference pattern.

```
{{resolve:ssm:`parameter-name`:`version`}}
```

Your reference must adhere to the following regular expression pattern for
parameter-name and version:

```
{{resolve:ssm:[a-zA-Z0-9_.\-/]+(:\d+)?}}
```

`parameter-name`

The name of the parameter in the Parameter Store. The parameter name
is case-sensitive.

Required.

`version`

An integer that specifies the version of the parameter to use. If you
don't specify the exact version, CloudFormation uses the latest version of
the parameter whenever you create or update the stack. For more
information, see [Working with
parameter versions](../../../systems-manager/latest/userguide/sysman-paramstore-versions.md "../../../systems-manager/latest/userguide/sysman-paramstore-versions.md") in the
_AWS Systems Manager User Guide_.

Optional.

## Examples

###### Topics

- [Public AMI ID
  parameter](#dynamic-references-ssm-public-ami-example "#dynamic-references-ssm-public-ami-example")
- [Custom AMI ID
  parameter](#dynamic-references-ssm-custom-ami-example "#dynamic-references-ssm-custom-ami-example")

### Public AMI ID

parameter

The following example creates an EC2 instance that references a public AMI
parameter. The dynamic reference retrieves the latest Amazon Linux 2023 AMI ID
from the public parameter. For more information about public parameters, see [Discovering public parameters in Parameter Store](../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md "../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md") in the
_AWS Systems Manager User Guide_.

#### JSON

```
{
    "Resources": {
        "MyInstance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": "{{resolve:ssm:`/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64`}}",
                "InstanceType": "t2.micro"
            }
        }
    }
}
```

#### YAML

```
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: '{{resolve:ssm:`/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64`}}'
      InstanceType: t2.micro
```

### Custom AMI ID

parameter

The following example creates an EC2 launch template that references a custom
AMI ID stored in the Parameter Store. The dynamic reference retrieves the AMI ID
from version `2` of the
`golden-ami` parameter any time an
instance is launched from the launch template.

#### JSON

```
{
    "Resources": {
        "MyLaunchTemplate": {
            "Type": "AWS::EC2::LaunchTemplate",
            "Properties": {
                "LaunchTemplateName": {
                    "Fn::Sub": "${AWS::StackName}-launch-template"
                },
                "LaunchTemplateData": {
                    "ImageId": "{{resolve:ssm:`golden-ami:2`}}",
                    "InstanceType": "t2.micro"
                }
            }
        }
    }
}
```

#### YAML

```
Resources:
  MyLaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName: !Sub ${AWS::StackName}-launch-template
      LaunchTemplateData:
        ImageId: '{{resolve:ssm:`golden-ami:2`}}'
        InstanceType: t2.micro
```
