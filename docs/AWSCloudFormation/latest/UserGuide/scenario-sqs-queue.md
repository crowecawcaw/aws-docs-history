# Amazon SQS template snippets

This example shows an Amazon SQS queue.

## JSON



```
"MyQueue" : {
    "Type" : "AWS::SQS::Queue",
    "Properties" : {
        "VisibilityTimeout" : "`value`"
    }
}
```

## YAML



```
MyQueue:
  Type: AWS::SQS::Queue
  Properties:
    VisibilityTimeout: `value`
```
