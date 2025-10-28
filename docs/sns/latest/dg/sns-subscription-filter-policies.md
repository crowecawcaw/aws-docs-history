# Amazon SNS subscription filter

policies

A subscription filter policy allows you to specify property names and assign a list of
values to each property name. For more information, see [Amazon SNS message filtering](sns-message-filtering.md "sns-message-filtering.md").

When Amazon SNS evaluates message attributes or message body properties against the
subscription filter policy, it ignores the ones that aren't specified in the policy.

###### Important

AWS services such as IAM and Amazon SNS use a distributed computing model called eventual consistency.
Additions or changes to a subscription filter policy require up to 15 minutes to fully take effect.

A subscription accepts a message under the following conditions:

- When the filter policy scope is set to `MessageAttributes`, each
  property name in the filter policy matches a message attribute name. For each
  matching property name in the filter policy, at least one property value matches the
  message attribute value.
- When the filter policy scope is set to `MessageBody`, each property
  name in the filter policy matches a message body property name. For each matching
  property name in the filter policy, at least one property value matches the message
  body property value.
  Amazon SNS currently supports the following filter operators:

- [AND logic](and-or-logic.md#and-logic "and-or-logic.md#and-logic")
- [OR logic](and-or-logic.md#or-logic "and-or-logic.md#or-logic")
- [OR operator](and-or-logic.md#or-operator "and-or-logic.md#or-operator")
- [Key matching](attribute-key-matching.md "attribute-key-matching.md")
- [Numeric value exact matching](numeric-value-matching.md#numeric-exact-matching "numeric-value-matching.md#numeric-exact-matching")
- [Numeric value anything-but
  matching](numeric-value-matching.md#numeric-anything-but-matching "numeric-value-matching.md#numeric-anything-but-matching")
- [Numeric value range
  matching](numeric-value-matching.md#numeric-value-range-matching "numeric-value-matching.md#numeric-value-range-matching")
- [String value exact matching](string-value-matching.md#string-exact-matching "string-value-matching.md#string-exact-matching")
- [String value anything-but
  matching](string-value-matching.md#string-anything-but-matching "string-value-matching.md#string-anything-but-matching")
- [String matching using a prefix
  with the anything-but operator](string-value-matching.md#string-anything-but-matching "string-value-matching.md#string-anything-but-matching")
- [String value equals-ignore case](string-value-matching.md#string-equals-ignore "string-value-matching.md#string-equals-ignore")
- [String value IP address
  matching](string-value-matching.md#string-address-matching "string-value-matching.md#string-address-matching")
- [String value prefix matching](string-value-matching.md#string-prefix-matching "string-value-matching.md#string-prefix-matching")
- [String value suffix matching](string-value-matching.md#string-suffix-matching "string-value-matching.md#string-suffix-matching")
