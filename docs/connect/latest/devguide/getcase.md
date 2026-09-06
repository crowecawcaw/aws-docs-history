

# GetCase
<a name="getcase"></a>

Searches all existing cases with the provided customer ID. Add request fields to filter by case fields. Specify the case fields to be returned in the response to persist in the context.

## Parameter object
<a name="getcase-parameter"></a>

```
{
    "LinkContactToCase": "true" or "false", If set to true, cases will open automatically when the agent accepts the contact.
   "GetLastUpdatedCase": "true" or "false", You can specify to get only the last updated case for any search criteria. 
    "CustomerId": "Customer's Id", Search all cases for this customer Id.
    "CaseRequestFields": An optional map of cases request fields. Keys should be fields from Cases domain. Values can be static or dynamic.
    "CaseResponseFields": [ ] An optional list of field names that should be persisted in the case namespace.
}
```

## Results and conditions
<a name="getcase-results"></a>

None.

## Errors
<a name="getcase-errors"></a>
+ NoMatchingError - An error was encountered while trying to find the case. This may be due to a system error or how Get case is configured.
+ ContactNotLinked - If you specify to link the contact to case, then this error branch will appear. It might be that the contact was not linked after the case is retrieved (partial success/partial failure). If this happens, then the flow will follow this branch.
+ MultipleFound - Multiple cases are found with the search criteria.
+ NoneFound - No cases are found with the search criteria.

## Restrictions
<a name="getcase-restrictions"></a>

None. This can be used in any type of flow and any channel.

## Corresponding block in the UI
<a name="getcase-ui"></a>

[Flow block: Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases-block.html)