End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Built-in slot type

Any migrated slot that uses a slot type that is not supported
in Amazon Lex V2 won't be given a slot type value. To use this
slot:

- Create a custom slot type
- Add slot type values that are expected for the slot
  type
- Update the slot to use the new custom slot type
