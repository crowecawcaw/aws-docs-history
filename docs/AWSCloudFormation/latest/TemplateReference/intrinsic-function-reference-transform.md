

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Fn::Transform`
<a name="intrinsic-function-reference-transform"></a>

The intrinsic function `Fn::Transform` specifies a macro to perform custom processing on part of a stack template. Macros enable you to perform custom processing on templates, from simple actions like find-and-replace operations to extensive transformations of entire templates. For more information, see [Using CloudFormation macros to perform custom processing on templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) in the *AWS CloudFormation User Guide*.

You can also use `Fn::Transform` to call the [`AWS::Include` transform](transform-aws-include.md) transform, which is a macro hosted by CloudFormation.

## Declaration
<a name="intrinsic-function-reference-transform-declaration"></a>

### JSON
<a name="intrinsic-function-reference-transform-syntax.json"></a>

Syntax for the full function name:

```
{
    "Fn::Transform": {
        "Name": "{{macro name}}",
        "Parameters": {
            "{{Key}}": "{{value}}"
        }
    }
}
```

Syntax for the short form:

```
{
    "Transform": {
        "Name": "{{macro name}}",
        "Parameters": {
            "{{Key}}": "{{value}}"
        }
    }
}
```

### YAML
<a name="intrinsic-function-reference-transform-syntax.yaml"></a>

Syntax for the full function name:

```
Fn::Transform:
  Name : {{macro name}}
  Parameters :
    {{Key}} : {{value}}
```

Syntax for the short form:

```
!Transform
  Name: {{macro name}}
  Parameters:
    {{Key}}: {{value}}
```

## Parameters
<a name="intrinsic-function-reference-transform-parameters"></a>

`Name`  
The name of the macro you want to perform the processing.

`Parameters`  
The list parameters, specified as key-value pairs, to pass to the macro.

## Return value
<a name="intrinsic-function-reference-transform-returnvalue"></a>

The processed template snippet to be included in the processed stack template.

## Examples
<a name="intrinsic-function-reference-transform-examples"></a>

The following example calls the `AWS::Include` transform, specifying that the location to retrieve a template snippet from is passed in the `InputValue` parameter.

### JSON
<a name="intrinsic-function-reference-transform-example-1.json"></a>

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
<a name="intrinsic-function-reference-transform-example-1.yaml"></a>

```
Fn::Transform:
  Name: AWS::Include
  Parameters:
    Location: !Ref InputValue
```

## Supported functions
<a name="intrinsic-function-reference-transform-supported-functions"></a>

None.

CloudFormation passes any intrinsic function calls included in `Fn::Transform` to the specified macro as literal strings.