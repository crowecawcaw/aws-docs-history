# Troubleshooting AWS CloudFormation Guard

If you encounter issues while working with AWS CloudFormation Guard, consult the topics in this
section.

###### Topics

- [Clause fails when no resources of the selected type are present](#troubleshooting-when-conditions-filters "#troubleshooting-when-conditions-filters")
- [Guard does not evaluate CloudFormation template with short-form Fn::GetAtt references](#troubleshooting-cfn-intrinsic-functions "#troubleshooting-cfn-intrinsic-functions")
- [General troubleshooting topics](#troubleshooting-general "#troubleshooting-general")

## Clause fails when no resources of the selected type are present

When a query uses a filter like `Resources.*[ Type == 'AWS::ApiGateway::RestApi'
 ]`, if there are no `AWS::ApiGateway::RestApi` resources in the input, the
clause evaluates to `FAIL`.

```
%api_gws.Properties.EndpointConfiguration.Types[*] == "PRIVATE"
```

To avoid this outcome, assign filters to variables and use the `when` condition
check.

```
let api_gws = Resources.*[ Type == 'AWS::ApiGateway::RestApi' ]
    when %api_gws !empty { ...}
```

## Guard does not evaluate CloudFormation template with short-form Fn::GetAtt references

Guard doesn't support the short forms of intrinsic functions. For example, using
`!Join`, `!Sub` in a YAML-formatted CloudFormation template isn't supported.
Instead, use the expanded forms of CloudFormation intrinsic functions. For example, use
`Fn::Join`, `Fn::Sub` in YAML-formatted CloudFormation templates when
evaluating them against Guard rules.

For more information about intrinsic functions, see the [intrinsic function
reference](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md") in the _AWS CloudFormation User Guide_.

## General troubleshooting topics

- Verify that `string` literals don't contain embedded escaped strings.
  Guard doesn't support embedded escape strings in `string`
  literals. If your intent is to parse inline JSON strings, use the
  `json_parse()` function available in Guard 3.0.0 and later. For more
  information, see [Using built-in functions](writing-rules.md#built-in-functions "writing-rules.md#built-in-functions").
- Verify that your `!=` comparisons compare compatible data types. For example, a
  `string` and an `int` are not compatible data types for comparison. When
  performing `!=` comparison, if the values are incompatible, an error occurs
  internally. Currently, the error is suppressed and converted to `false` to satisfy
  the [PartialEq](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "https://doc.rust-lang.org/std/cmp/trait.PartialEq.html") trait
  in Rust.
