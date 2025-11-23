This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::Split`

To split a string into a list of string values so that you can select an element from the
resulting string list, use the `Fn::Split` intrinsic function. Specify the location
of splits with a delimiter, such as `,` (a comma). After you split a string, use
the [Fn::Select](intrinsic-function-reference-select.md "intrinsic-function-reference-select.md") function to pick a specific
element.

For example, if a comma-delimited string of subnet IDs is imported to your stack template,
you can split the string at each comma. From the list of subnet IDs, use the
`Fn::Select` intrinsic function to specify a subnet ID for a resource.

## Declaration

### JSON

```
{ "Fn::Split" : [ "``delimiter``", "`source string`" ] }
```

### YAML

Syntax for the full function name:

```
Fn::Split: [ ``delimiter``, `source string` ]
```

Syntax for the short form:

```
!Split [ ``delimiter``, `source string` ]
```

## Parameters

You must specify both parameters.

delimiter

A string value that determines where the source string is divided.

source string

The string value that you want to split.

## Return value

A list of string values.

## Examples

The following examples demonstrate the behavior of the `Fn::Split`
function.

### Simple list

The following example splits a string at each vertical bar (`|`). The
function returns `["a", "b", "c"]`.

#### JSON

```
{ "Fn::Split" : [ "|" , "a|b|c" ] }
```

#### YAML

```
!Split [ "|" , "a|b|c" ]
```

 

### List with empty string values

If you split a string with consecutive delimiters, the resulting list will include an
empty string. The following example shows how a string with two consecutive delimiters
and an appended delimiter is split. The function returns `["a", "", "c",
 ""]`.

#### JSON

```
{ "Fn::Split" : [ "|" , "a||c|" ] }
```

#### YAML

```
!Split [ "|" , "a||c|" ]
```

 

### Split an imported output value

The following example splits an imported output value, and then selects the third
element from the resulting list of subnet IDs, as specified by the
`Fn::Select` function.

#### JSON

```
{ "Fn::Select" : [ "2", { "Fn::Split": [",", {"Fn::ImportValue": "AccountSubnetIDs"}]}] }
```

#### YAML

```
!Select [2, !Split [",", !ImportValue AccountSubnetIDs]]
```

## Supported functions

For the `Fn::Split` delimiter, you can't use any functions. You must specify
a string value.

For the `Fn::Split` list of values, you can use the following
functions:

- `Fn::Base64`
- `Fn::FindInMap`
- `Fn::GetAtt`
- `Fn::GetAZs`
- `Fn::If`
- `Fn::ImportValue`
- `Fn::Join`
- `Fn::Select`
- `Fn::Sub`
- `Ref`
