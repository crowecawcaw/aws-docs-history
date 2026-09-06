

# UpdateCase
<a name="updatecase"></a>

Updates an existing case by providing the case’s id and the fields that should be updated.

## Parameter object
<a name="updatecase-parameter"></a>

```
{
  “LinkContactToCase” : "true" or "false", If set to true, cases open automatically when the agent accepts the contact.
  “CaseId”: the unique identifier of the case
  “CaseRequestFields”: An optional map of case fields to be updated. Keys should be fields from the Cases domain. Values can be static or dynamic.
}
```

## Results and conditions
<a name="updatecase-results"></a>

None.

## Errors
<a name="updatecase-errors"></a>
+ ContactNotLinked - If you specify to link the contact to case, then this error branch will appear. It might be that the contact was not linked after the case is retrieved (partial success/partial failure). If this happens, then the flow will follow this branch.
+ NoMatchingError - An error was encountered while trying to find the case. This may be due to a system error, or how Update case is configured.

## Restrictions
<a name="updatecase-restrictions"></a>

None. This can be used in any type of flow and any channel.

## Corresponding block in the UI
<a name="updatecase-ui"></a>

[Flow block: Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases-block.html)