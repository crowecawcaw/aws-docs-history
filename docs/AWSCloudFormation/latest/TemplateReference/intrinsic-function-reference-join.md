This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::Join`

The intrinsic function `Fn::Join` appends a set of values into a single value,
separated by the specified delimiter. If a delimiter is the empty string, the set of values
are concatenated with no delimiter.

## Declaration

### JSON

```
{ "Fn::Join" : [ "`delimiter`", [ `comma-delimited list of values` ] ] }
```

### YAML

Syntax for the full function name:

```
Fn::Join: [ `delimiter`, [ `comma-delimited list of values` ] ]
```

Syntax for the short form:

```
!Join [ `delimiter`, [ `comma-delimited list of values` ] ]
```

## Parameters

delimiter

The value you want to occur between fragments. The delimiter will occur between
fragments only. It won't terminate the final value.

ListOfValues

The list of values you want combined.

## Return value

The combined string.

## Examples

### Join a simple string

array

The following example returns: `"a:b:c"`.

#### JSON

```
"Fn::Join" : [ ":", [ "a", "b", "c" ] ]
```

#### YAML

```
!Join [ ":", [ a, b, c ] ]
```

### Join using the ref function

with parameters

The following example uses `Fn::Join` to construct a string value. It uses
the `Ref` function with the `AWS::Partition` parameter and the
`AWS::AccountId` pseudo parameter.

#### JSON

```
{
  "Fn::Join": [
    "", [
      "arn:",
      {
        "Ref": "AWS::Partition"
      },
      ":s3:::elasticbeanstalk-*-",
      {
        "Ref": "AWS::AccountId"
      }
    ]
  ]
}
```

#### YAML

```
!Join
  - ''
  - - 'arn:'
    - !Ref AWS::Partition
    - ':s3:::elasticbeanstalk-*-'
    - !Ref AWS::AccountId
```

###### Note

Also see the [Fn::Sub](intrinsic-function-reference-sub.md "intrinsic-function-reference-sub.md") function for similar
functionality.

## Supported

functions

For the `Fn::Join` delimiter, you can't use any functions. You must specify a
string value.

For the `Fn::Join` list of values, you can use the following
functions:

- `Fn::Base64`
- `Fn::FindInMap`
- `Fn::GetAtt`
- `Fn::GetAZs`
- `Fn::If`
- `Fn::ImportValue`
- `Fn::Join`
- `Fn::Split`
- `Fn::Select`
- `Fn::Sub`
- `Ref`
