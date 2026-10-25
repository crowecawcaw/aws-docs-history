

# Permissions for managing functions
<a name="functions-prerequisites-caller-permissions"></a>

The identity that creates and attaches functions — a person in the console, or an application calling the API — needs the Elemental Inference function actions, plus permission to pass the feed's access role to Elemental Inference. Function ARNs have the form `arn:aws:elemental-inference:{{region}}:{{111122223333}}:function/{{function-id}}`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elemental-inference:CreateFunction",
        "elemental-inference:GetFunction",
        "elemental-inference:UpdateFunction",
        "elemental-inference:DeleteFunction",
        "elemental-inference:ListFunctions",
        "elemental-inference:GetFeed",
        "elemental-inference:UpdateFeed",
        "elemental-inference:GetMetadata",
        "elemental-inference:TagResource",
        "elemental-inference:UntagResource",
        "elemental-inference:ListTagsForResource"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::{{111122223333}}:role/{{ElementalInferenceFeedAccessRole}}",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "elemental-inference.amazonaws.com"
        }
      }
    }
  ]
}
```

`CreateFunction` supports tagging on create, so you can also restrict it with the `aws:RequestTag/${TagKey}` and `aws:TagKeys` condition keys. For more information, see [Identity and Access Management for AWS Elemental Inference](security-iam.md).