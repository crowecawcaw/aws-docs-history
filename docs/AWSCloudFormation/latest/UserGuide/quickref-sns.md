# Amazon SNS template snippets

This example shows an Amazon SNS topic resource. It requires a valid email address.

## JSON

```
"MySNSTopic" : {
    "Type" : "AWS::SNS::Topic",
    "Properties" : {
        "Subscription" : [ {
            "Endpoint" : "`add valid email address`",
            "Protocol" : "email"
        } ]
    }
}
```

## YAML

```
MySNSTopic:
  Type: AWS::SNS::Topic
  Properties:
    Subscription:
    - Endpoint: "`add valid email address`"
      Protocol: email
```
