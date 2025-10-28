End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.Percentage

Converts words and symbols that represent a percentage into a
numeric value with a percent sign (%).

If the user enters a number without a percent sign or the word
"percent," the slot value is set to the number. The following
table shows how the `AMAZON.Percentage` slot type
captures percentages.

| Input               | Response |
| ------------------- | -------- |
| 50 percent          | 50%      |
| 0.4 percent         | 0.4%     |
| 23.5%               | 23.5%    |
| twenty five percent | 25%      |
