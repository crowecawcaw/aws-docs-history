Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'AWS Lambda invoke' variables

By default, the **AWS Lambda invoke** action produces one variable per
top-level key in the Lambda response payload.

For example, if the response payload looks like this:

```
responsePayload = {
  "name": "Saanvi",
  "location": "Seattle",
  "department": {
    "company": "Amazon",
    "team": "AWS"
  }
}
```

...then the action would generate the following variables.

| Key        | Value                                |
| ---------- | ------------------------------------ |
| name       | Saanvi                               |
| location   | Seattle                              |
| department | {"company": "Amazon", "team": "AWS"} |

###### Note

You can change which variables are generated using the `ResponseFilters` YAML
property. For more information, see the [ResponseFilters](lam-invoke-action-ref.md#lam.invoke.response.filters "lam-invoke-action-ref.md#lam.invoke.response.filters") in the ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md "lam-invoke-action-ref.md").

The variables produced and set by the 'AWS Lambda invoke' action at run time are known as
_predefined variables_.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").
