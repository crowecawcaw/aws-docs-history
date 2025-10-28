End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.DATE

Converts words that represent dates into a date format.

The date is provided to your intent in ISO-8601 date format.
The date that your intent receives in the slot can vary
depending on the specific phrase uttered by the user.

- Utterances that map to a specific date, such as
  "today," "now," or "November twenty-fifth," convert to a
  complete date: `2020-11-25`. This defaults to
  dates _on or after_ the current
  date.
- Utterances that map to a specific week, such as "this
  week," or "next week," convert to the date of the first
  day of the week. In ISO-8601 format, the week starts on
  Monday and ends on Sunday. For example, if today is
  2020-11-25, "next week" converts to
  `2020-11-30`.
- Utterances that map to a month, but not a specific
  day, such as "next month," convert to the last day of
  the month. For example, if today is 2020-11-25, "next
  month" converts to `2020-12-31`.
- Utterances that map to a year, but not a specific
  month or day, such as "next year," convert to the last
  day of the following year. For example, if today is
  2020-11-25, "next year" converts to
  `2021-12-31`.
