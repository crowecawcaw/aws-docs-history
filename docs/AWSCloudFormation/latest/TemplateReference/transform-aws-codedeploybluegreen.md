This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `AWS::CodeDeployBlueGreen`

transform

This topic describes how to use the `AWS::CodeDeployBlueGreen` transform to
enable ECS blue/green deployments through CodeDeploy on your stack.

For more information, see [Perform ECS blue/green deployments through CodeDeploy using CloudFormation](../UserGuide/blue-green.md "../UserGuide/blue-green.md") in the
_AWS CloudFormation User Guide_.

## Usage

To use the `AWS::CodeDeployBlueGreen` transform, you must declare it at the
top level of your CloudFormation template. You can't use
`AWS::CodeDeployBlueGreen` as a transform embedded in any other template
section.

The value for the transform declaration must be a literal string. You can't use a
parameter or function to specify a transform value.

### Syntax

To declare this transform in your CloudFormation template, use the following
syntax:

#### JSON

```
{
  "Transform":[
    "AWS::CodeDeployBlueGreen"
  ],
  "Resources":{
    `...`
  }
}
```

#### YAML

```
Transform:
  - 'AWS::CodeDeployBlueGreen'
Resources:
  `...`
```

The `AWS::CodeDeployBlueGreen` transform is a standalone declaration
with no additional parameters.

## Related resources

For complete CloudFormation template examples that you can use to enable ECS blue/green
deployments on your stack, see [Blue/green deployment template
example](../UserGuide/blue-green-template-example.md "../UserGuide/blue-green-template-example.md") in the _AWS CloudFormation User Guide_.

For general information about using macros, see [Perform custom processing on CloudFormation
templates with template macros](../UserGuide/template-macros.md "../UserGuide/template-macros.md") in the
_AWS CloudFormation User Guide_.
