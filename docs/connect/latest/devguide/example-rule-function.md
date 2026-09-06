

# Example rule function in Connect Customer Rule Function language
<a name="example-rule-function"></a>

The following example shows a simple rule that would be evaluated to `true` if "refund" is mentioned by the customer who is in a specific queue. 

To learn how to use conditions correctly, we recommend creating a new rule in the Connect Customer console, and then calling the [DescribeRule](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRule.html) API for it.

```
{
  "Version": "2022-11-25", // A string representing the version of the rule. Currently the only supported version is 2022-11-25.
  "RuleFunction": { // RuleFunction object body
    "Operator": "AND",
    "Operands": [
      {
        "Operator": "CONTAINS_ANY",
        "Operands": [
          "refund"
        ],
        "ComparisonValue": "$.ContactLens.RealTimeCall.ExactMatch.Transcript",
        "FilterClause": {
          "LogicOperator": "AND",
          "Filters": [
            {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER"
            }
          ]
        },
        "Negate": false // If Negate were set to true, it would mean the word "refund" was NOT mentioned
      },
      {
        "Operator": "CONTAINS_ANY",
        "Operands": [
          "11111111-1234-5678-9123-12345678012" // QueueId 
        ],
        "ComparisonValue": "$.ContactLens.RealTimeCall.Queue.QueueId",
        "Negate": false
      }
    ]
  }
}
```