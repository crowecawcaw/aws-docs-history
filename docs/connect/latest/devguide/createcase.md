

# CreateCase
<a name="createcase"></a>

Creates a new case using an existing case template. Templates come with predefined fields, some of which are required and will appear in a side panel when you start. You can review and fill in the required fields, and optionally update any other available fields based on your needs. These fields are set up in your instance ahead of time. You can also choose to link a contact to the new case if needed.

## Parameter object
<a name="createcase-parameter"></a>

```
"Parameters": {
        "LinkContactToCase": "true" or "false", If set to true, cases will open automatically when the agent accepts the contact.
        "CaseTemplateId": A templateId aligned with the existing case templateName
        "CaseRequestFields": An optional map of case fields to be set. Keys should be fields from Cases domain. Values can be static or dynamic.
}
```

## Results and conditions
<a name="createcase-results"></a>

None.

## Errors
<a name="createcase-errors"></a>
+ ContactNotLinked - If you specify to link the contact to case, then this error branch will appear. It might be that the contact was not linked after the case is retrieved (partial success/partial failure). If this happens, then the flow will follow this branch.
+ NoMatchingError - An error was encountered while trying to find the case. This may be due to a system error or how CreateCase is configured.

## Restrictions
<a name="createcase-restrictions"></a>

None. This can be used in any type of flow and any channel.

## Corresponding block in the UI
<a name="createcase-ui"></a>

[Flow block: Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases-block.html)