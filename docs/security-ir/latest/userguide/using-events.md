# Using AWS Security Incident Response Events

You can create EventBridge rules to match these events and trigger automated actions. Here are some example use cases:

_Match all AWS Security Incident Response events:_

```

         {
           "source": ["aws.security-ir"]
         }

```

_Match only case events:_

```

         {
           "source": ["aws.security-ir"],
           "detail-type": [
             "Case Created",
             "Case Updated",
             "Case Closed",
             "Case Comment Created",
             "Case Comment Updated"
           ]
         }

```

_Match cases updated by AWS Responders:_

```

         {
           "source": ["aws.security-ir"],
           "detail-type": ["Case Updated"],
           "detail": {
             "updatedBy": ["AWS Responder"]
           }
         }

```

_Match events for a specific case:_

```

         {
           "source": ["aws.security-ir"],
           "detail": {
             "caseId": ["1234567890"]
           }
         }

```
