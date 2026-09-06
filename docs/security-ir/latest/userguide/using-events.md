

# Using AWS Security Incident Response Events
<a name="using-events"></a>

You can create EventBridge rules to match these events and trigger automated actions. Here are some example use cases:

*Match all AWS Security Incident Response events:*

```
         {
           "source": ["aws.security-ir"]
         }
```

*Match only case events:*

```
         {
           "source": ["aws.security-ir"],
           "detail-type": [
             "Case Created",
             "Case Updated",
             "Case Closed",
             "Case Comment Added",
             "Case Comment Updated"
           ]
         }
```

*Match cases updated by AWS Responders:*

```
         {
           "source": ["aws.security-ir"],
           "detail-type": ["Case Updated"],
           "detail": {
             "updatedBy": ["AWS Responder"]
           }
         }
```

*Match events for a specific case:*

```
         {
           "source": ["aws.security-ir"],
           "detail": {
             "caseId": ["1234567890"]
           }
         }
```