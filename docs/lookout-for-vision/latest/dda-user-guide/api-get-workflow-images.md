Defect Detection App is in preview release and is subject to change.

# GET /workflows/{workflowId}/images

Gets the analysis results for the last 2 images that the workflow analyzed. For more information, see [Workflow](api-dt-Workflow.md "api-dt-Workflow.md").

## Endpoint

```
GET /workflows/{workflowId}/images
```

`workflowId` is the identifier for the workflow that you want
to use.

## Request

parameters

None

## Response

An array (`images`) of two [WorkflowResult](api-dt-WorkflowResult.md "api-dt-WorkflowResult.md") objects that contain the analysis
results for the last 2 analyzed images (one `WorkflowObject` for each
image). To determine the results for the latest image analyzed, check the
`creationTime` field in the `WorkflowResult`
object.

Format: JSON
