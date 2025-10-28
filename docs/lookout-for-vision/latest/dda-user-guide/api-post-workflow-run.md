Defect Detection App is in preview release and is subject to change.

# POST /workflows/{workflowId}/run

Manually runs a workflow. Before you can run a workflow, you must first
configure the workflow with a call to [PATCH /workflows/{workflowId}](api-patch-workflow.md "api-patch-workflow.md"). If you don't know the
`workflowId`, call [GET /workflows](api-get-workflows.md "api-get-workflows.md") to get a list of the workflows that are
on the station.

For more information, see [Workflow](api-dt-Workflow.md "api-dt-Workflow.md").

## Endpoint

```
POST /workflows/{workflowId}/run
```

`workflowId` is the identifier for the workflow that you want
to manually run.

## Request

parameters

None

## Response

A [WorkflowResult](api-dt-WorkflowResult.md "api-dt-WorkflowResult.md") object
that contains the result from the workflow.

Format: [WorkflowResult](api-dt-WorkflowResult.md "api-dt-WorkflowResult.md")
