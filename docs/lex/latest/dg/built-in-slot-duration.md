End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.DURATION

Converts words that indicate durations into a numeric
duration.

The duration is resolved to a format based on the [ISO-8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations "https://en.wikipedia.org/wiki/ISO_8601#Durations"),
`PnYnMnWnDTnHnMnS`. The `P` indicates
that this is a duration, the `n` is a numeric value,
and the capital letter following the `n` is the
specific date or time element. For example, `P3D`
means 3 days. A `T` is used to indicate that the
remaining values represent time elements rather than date
elements.

Examples:

- "ten minutes": `PT10M`
- "five hours": `PT5H`
- "three days": `P3D`
- "forty five seconds": `PT45S`
- "eight weeks": `P8W`
- "seven years": `P7Y`
- "five hours ten minutes": `PT5H10M`
- "two years three hours ten minutes":
  `P2YT3H10M`
