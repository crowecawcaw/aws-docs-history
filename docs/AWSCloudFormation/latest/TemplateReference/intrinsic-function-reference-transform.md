This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::Transform`

The intrinsic function `Fn::Transform` specifies a macro to perform custom
processing on part of a stack template. Macros enable you to perform custom processing on
templates, from simple actions like find-and-replace operations to extensive transformations
of entire templates. For more information, see [Using CloudFormation macros to perform custom processing
on templates](../UserGuide/template-macros.md "../UserGuide/template-macros.md") in the _AWS CloudFormation User Guide_.

You can also use `Fn::Transform` to call the [AWS::Include transform](transform-aws-include.md "transform-aws-include.md") transform, which is a macro hosted by CloudFormation.

## Declaration

### JSON

Syntax for the full function name:

```
{
    "Fn::Transform": {
        "Name": "`macro name`",
        "Parameters": {
            "`Key`": "`value`"
        }
    }
}
```

Syntax for the short form:

```
{
    "Transform": {
        "Name": "`macro name`",
        "Parameters": {
            "`Key`": "`value`"
        }
    }
}
```

### YAML

Syntax for the full function name:

```
Fn::Transform:
  Name : `macro name`
  Parameters :
    `Key` : `value`
```

Syntax for the short form:

```
!Transform
  Name: `macro name`
  Parameters:
    `Key`: `value`
```

## Parameters

`Name`

The name of the macro you want to perform the processing.

`Parameters`

The list parameters, specified as key-value pairs, to pass to the macro.

## Return value

The processed template snippet to be included in the processed stack template.

## Examples

The following example calls the `AWS::Include` transform, specifying that the
location to retrieve a template snippet from is passed in the `InputValue`
parameter.

### JSON

```
{
    "Fn::Transform": {
        "Name": "AWS::Include",
        "Parameters": {
            "Location": {
                "Ref": "InputValue"
            }
        }
    }
}
```

### YAML

```
Fn::Transform:
  Name: AWS::Include
  Parameters:
    Location: !Ref InputValue
```

## Supported

functions

None.

CloudFormation passes any intrinsic function calls included in `Fn::Transform` to
the specified macro as literal strings.
