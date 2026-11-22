

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Fn::Base64`

The intrinsic function `Fn::Base64` returns the Base64 representation of the input string. This function is typically used to pass encoded data to Amazon EC2 instances by way of the `UserData` property.

## Declaration
<a name="w2aac24c12b5"></a>

### JSON
<a name="intrinsic-function-reference-base64-syntax.json"></a>

```json
{ "Fn::Base64" : {{valueToEncode}} }
```

### YAML
<a name="intrinsic-function-reference-base64-syntax.yaml"></a>

Syntax for the full function name:

```yaml
Fn::Base64: {{valueToEncode}}
```

Syntax for the short form:

```yaml
!Base64 {{valueToEncode}}
```

**Note**  
If you use the short form and immediately include another function in the `valueToEncode` parameter, use the full function name for at least one of the functions. For example, the following syntax isn't valid:  

```yaml
!Base64 !Sub {{string}}
!Base64 !Ref {{logical_ID}}
```
Instead, use the full function name for at least one of the functions, as shown in the following examples:  

```yaml
!Base64
  "Fn::Sub": {{string}}

Fn::Base64:
  !Sub {{string}}
```

## Parameters
<a name="w2aac24c12b7"></a>

valueToEncode  
The string value you want to convert to Base64.

## Return value:
<a name="w2aac24c12b9"></a>

The original string, in Base64 representation.

## Examples
<a name="w2aac24c12c11"></a>

### JSON
<a name="intrinsic-function-reference-base64-example.json"></a>

```json
{ "Fn::Base64" : "AWS CloudFormation" }
```

### YAML
<a name="intrinsic-function-reference-base64-example.yaml"></a>

```yaml
Fn::Base64: AWS CloudFormation
```

## Supported functions
<a name="w2aac24c12c13"></a>

You can use any function that returns a string inside the `Fn::Base64` function.