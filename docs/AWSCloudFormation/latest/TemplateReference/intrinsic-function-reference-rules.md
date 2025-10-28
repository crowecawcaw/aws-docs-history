This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# Rule functions

Rule functions are special functions that work only in the `Rules` section of a
CloudFormation template. These functions help you validate parameter values using custom logic. All
validations occur before CloudFormation creates or updates any resources.

Rules are useful when standard parameter constraints are insufficient. For example, when SSL
is enabled, both a certificate and domain name must be provided. A rule can ensure that these
dependencies are met.

In the condition or assertions of a rule, you can use intrinsic functions, such as
`Fn::Equals`, `Fn::Not`, and `Fn::RefAll`. The condition
property determines if CloudFormation applies the assertions. If the condition evaluates to
`true`, CloudFormation evaluates the assertions to verify whether a parameter value is
valid when a stack is created or updated. If a parameter value isn't valid, CloudFormation doesn't
create or update the stack. If the condition evaluates to `false`, CloudFormation doesn't
check the parameter value and proceeds with the stack operation.

If you're new to using rules in your templates, we recommend you first review the [CloudFormation template Rules
syntax](../UserGuide/rules-section-structure.md "../UserGuide/rules-section-structure.md") topic in the _AWS CloudFormation User Guide_.

###### Topics

- [Fn::And](#fn-and "#fn-and")
- [Fn::Contains](#fn-contains "#fn-contains")
- [Fn::EachMemberEquals](#fn-eachmemberequals "#fn-eachmemberequals")
- [Fn::EachMemberIn](#fn-eachmemberin "#fn-eachmemberin")
- [Fn::Equals](#fn-equals "#fn-equals")
- [Fn::Not](#fn-not "#fn-not")
- [Fn::Or](#fn-or "#fn-or")
- [Fn::RefAll](#fn-refall "#fn-refall")
- [Fn::ValueOf](#fn-valueof "#fn-valueof")
- [Fn::ValueOfAll](#fn-valueofall "#fn-valueofall")
- [Supported functions](#supported-rule-functions "#supported-rule-functions")
- [Supported attributes](#rules-parameter-attributes "#rules-parameter-attributes")

## `Fn::And`

Returns `true` if all the specified conditions evaluate to `true`;
returns `false` if any one of the conditions evaluates to `false`.
`Fn::And` acts as an AND operator. The minimum number of conditions that you can
include is two, and the maximum is ten.

### Declaration

```
"Fn::And" : [{`condition`}, {`...`}]
```

### Parameters

_condition_

A rule-specific intrinsic function that evaluates to `true` or
`false`.

### Example

The following example evaluates to `true` if the referenced security group
name is equal to `sg-mysggroup` and if the `InstanceType` parameter
value is either `t3.large` or `t3.small`:

```
"Fn::And": [
  {
    "Fn::Equals": [
      "sg-mysggroup",
      {"Ref": "ASecurityGroup"}
    ]
  },
  {
    "Fn::Contains": [
      [
        "t3.large",
        "t3.small"
      ],
      {"Ref": "InstanceType"}
    ]
  }
]

```

## `Fn::Contains`

Returns `true` if a specified string matches at least one value in a list of
strings.

### Declaration

```
"Fn::Contains" : [[`list_of_strings`], `string`]
```

### Parameters

_list_of_strings_

A list of strings, such as `"A", "B", "C"`.

_string_

A string, such as `"A"`, that you want to compare against a list of
strings.

### Example

The following function evaluates to `true` if the `InstanceType`
parameter value is contained in the list (`t3.large` or
`t3.small`):

```
"Fn::Contains" : [
  ["t3.large", "t3.small"], {"Ref" : "InstanceType"}
]
```

## `Fn::EachMemberEquals`

Returns `true` if a specified string matches all values in a list.

### Declaration

```
"Fn::EachMemberEquals" : [[`list_of_strings`], `string`]
```

### Parameters

_list_of_strings_

A list of strings, such as `"A", "B", "C"`.

_string_

A string, such as `"A"`, that you want to compare against a list of
strings.

### Example

The following function returns `true` if the `Department` tag for
all parameters of type
`AWS::EC2::VPC::Id` have a value of `IT`:

```
"Fn::EachMemberEquals" : [
  {"Fn::ValueOfAll" : ["AWS::EC2::VPC::Id", "Tags.Department"]}, "IT"
]
```

## `Fn::EachMemberIn`

Returns `true` if each member in a list of strings matches at least one value
in a second list of strings.

### Declaration

```
"Fn::EachMemberIn" : [[`strings_to_check`], [`strings_to_match`]]
```

### Parameters

_strings_to_check_

A list of strings, such as `"A", "B", "C"`. CloudFormation checks whether
each member in the `strings_to_check` parameter is in the
`strings_to_match` parameter.

_strings_to_match_

A list of strings, such as `"A", "B", "C"`. Each member in the
`strings_to_match` parameter is compared against the members of the
`strings_to_check` parameter.

### Example

The following function checks whether users specify a subnet that's in a valid virtual
private cloud (VPC). The VPC must be in the account and the Region in which users are
working with the stack. The function applies to all parameters of type
`AWS::EC2::Subnet::Id`.

```
"Fn::EachMemberIn" : [
  {"Fn::ValueOfAll" : ["AWS::EC2::Subnet::Id", "VpcId"]}, {"Fn::RefAll" : "AWS::EC2::VPC::Id"}
]
```

## `Fn::Equals`

Compares two values to determine whether they're equal. Returns `true` if the
two values are equal and `false` if they aren't.

### Declaration

```
"Fn::Equals" : ["`value_1`", "`value_2`"]
```

### Parameters

_`value`_

A value of any type that you want to compare with another value.

### Example

The following example evaluates to `true` if the value for the
`EnvironmentType` parameter is equal to `prod`:

```
"Fn::Equals" : [{"Ref" : "EnvironmentType"}, "prod"]
```

## `Fn::Not`

Returns `true` for a condition that evaluates to `false`, and
returns `false` for a condition that evaluates to `true`.
`Fn::Not` acts as a NOT operator.

### Declaration

```
"Fn::Not" : [{`condition`}]
```

### Parameters

_`condition`_

A rule-specific intrinsic function that evaluates to `true` or
`false`.

### Example

The following example evaluates to `true` if the value for the
`EnvironmentType` parameter isn't equal to `prod`:

```
"Fn::Not" : [{"Fn::Equals" : [{"Ref" : "EnvironmentType"}, "prod"]}]
```

## `Fn::Or`

Returns `true` if any one of the specified conditions evaluates to
`true`; returns `false` if all the conditions evaluate to
`false`. `Fn::Or` acts as an OR operator. The minimum number of
conditions that you can include is two, and the maximum is ten.

### Declaration

```
"Fn::Or" : [{`condition`}, {`...`}]
```

### Parameters

_`condition`_

A rule-specific intrinsic function that evaluates to `true` or
`false`.

### Example

The following example evaluates to `true` if the referenced security group
name is equal to `sg-mysggroup` or if the `InstanceType` parameter
value is either `t3.large` or `t3.small`:

```
"Fn::Or" : [
  {"Fn::Equals" : ["sg-mysggroup", {"Ref" : "ASecurityGroup"}]},
  {"Fn::Contains" : [["t3.large", "t3.small"], {"Ref" : "InstanceType"}]}
]
```

## `Fn::RefAll`

Returns all values for a specified parameter type.

### Declaration

```
"Fn::RefAll" : "`parameter_type`"
```

### Parameters

_parameter_type_

An AWS-specific parameter type, such as `AWS::EC2::SecurityGroup::Id`
or `AWS::EC2::VPC::Id`. For more information, see [Supported AWS-specific parameter types](../UserGuide/cloudformation-supplied-parameter-types.md#aws-specific-parameter-types-supported "../UserGuide/cloudformation-supplied-parameter-types.md#aws-specific-parameter-types-supported") in the
_AWS CloudFormation User Guide_.

### Example

The following function returns a list of all VPC IDs for the Region and AWS account in
which the stack is being created or updated:

```
"Fn::RefAll" : "AWS::EC2::VPC::Id"
```

## `Fn::ValueOf`

Returns an attribute value or list of values for a specific parameter and
attribute.

### Declaration

```
"Fn::ValueOf" : [ "`parameter_logical_id`", "`attribute`" ]
```

### Parameters

_attribute_

The name of an attribute to retrieve a value from. For more information about
attributes, see [Supported attributes](#rules-parameter-attributes "#rules-parameter-attributes").

_parameter_logical_id_

The name of a parameter to retrieve attribute values from. The parameter must be
declared in the `Parameters` section of the template.

### Examples

The following example returns the value of the `Department` tag for the VPC
that's specified by the `ElbVpc` parameter:

```
"Fn::ValueOf" : ["ElbVpc", "Tags.Department"]
```

If you specify multiple values for a parameter, the Fn::ValueOf function can return a
list. For example, you can specify multiple subnets and get a list of Availability Zones
where each member is the Availability Zone of a particular subnet:

```
"Fn::ValueOf" : ["ListOfElbSubnets", "AvailabilityZone"]
```

## `Fn::ValueOfAll`

Returns a list of all attribute values for a given parameter type and attribute.

### Declaration

```
"Fn::ValueOfAll" : ["`parameter_type`", "`attribute`"]
```

### Parameters

_attribute_

The name of an attribute from which you want to retrieve a value. For more
information about attributes, see [Supported attributes](#rules-parameter-attributes "#rules-parameter-attributes").

_parameter_type_

An AWS-specific parameter type, such as `AWS::EC2::SecurityGroup::Id`
or `AWS::EC2::VPC::Id`. For more information, see [Supported AWS-specific parameter types](../UserGuide/cloudformation-supplied-parameter-types.md#aws-specific-parameter-types-supported "../UserGuide/cloudformation-supplied-parameter-types.md#aws-specific-parameter-types-supported") in the
_AWS CloudFormation User Guide_.

### Example

In the following example, the `Fn::ValueOfAll` function returns a list of
values, where each member is the `Department` tag value for VPCs with that
tag:

```
"Fn::ValueOfAll" : ["AWS::EC2::VPC::Id", "Tags.Department"]
```

## Supported functions

You can't use another function within the `Fn::ValueOf` and
`Fn::ValueOfAll` functions. However, you can use the following functions within
all other rule-specific intrinsic functions:

- `Ref`
- Other rule-specific intrinsic functions

## Supported attributes

The following list describes the attribute values that you can retrieve for specific
resources and parameter types:

The `AWS::EC2::VPC::Id` parameter type or VPC IDs.

- DefaultNetworkAcl
- DefaultSecurityGroup
- Tags.`tag_key`

The `AWS::EC2::Subnet::Id` parameter type or subnet IDs,

- AvailabilityZone
- Tags.`tag_key`
- VpcId

The `AWS::EC2::SecurityGroup::Id` parameter type or security group
IDs.

- Tags.`tag_key`
