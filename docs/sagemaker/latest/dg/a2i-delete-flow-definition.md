# Delete a Human Review Workflow

When you delete a human review workflow or you delete your AWS account while a human
loop is in process, your human review workflow status changes to `Deleting`.
Amazon A2I automatically stops and deletes all associated human loops if workers have not
started tasks created by those human loops. If human workers are already working on a task,
that task continues to be available until it is completed or expires. As long as workers are
still working on a task, your human review workflow's status is `Deleting`. If
these tasks are completed, the results are stored in the Amazon S3 bucket specified in your flow
definition.

Deleting a flow definition does not remove any worker answers from your S3 bucket. If the
tasks are completed, but you deleted your AWS account, the results are stored in the Augmented AI
service bucket for 30 days and then permanently deleted.

After all human loops have been deleted, the human review workflow is permanently deleted.
When a human review workflow has been deleted, you can reuse its name to create a new human
review workflow.

You might want to delete a human review workflow for any of the following reasons:

- You have sent data to a set of human reviewers and you want to delete all
  non-started human loops because you do not want those workers to work on those tasks
  any longer.
- The worker task template used to generate your worker UI does not render correctly
  or is not functioning as expected.
  After you delete a human review workflow, the following changes occur:

- The human review workflow no longer appears on the **Human review
  workflows** page in the Augmented AI area of the Amazon SageMaker AI console.
- When you use the human review workflow name as input to the API operations [`DescribeFlowDefinition`](../APIReference/API_DescribeFlowDefinition.md "../APIReference/API_DescribeFlowDefinition.md") or [`DeleteFlowDefinition`](../APIReference/API_DeleteFlowDefinition.md "../APIReference/API_DeleteFlowDefinition.md"), Augmented AI returns a
  `ResourceNotFound` error.
- When you use [`ListFlowDefinitions`](../APIReference/API_ListFlowDefinitions.md "../APIReference/API_ListFlowDefinitions.md"), deleted human review workflows
  aren't included in the results.
- When you use the human review workflow ARN as input to the Augmented AI Runtime API
  operation `ListHumanLoops`, Augmented AI returns a
  `ResourceNotFoundException`.

## Delete a Flow Definition Using the

Console or the SageMaker API

You can delete a human review workflow on the **Human review
workflows** page in the Augmented AI area of the SageMaker AI console or by using the SageMaker AI
API.

Flow definitions can only be deleted if their status is `Active`.

###### Delete a human review workflow (console)

1. Navigate to the Augmented AI console at [https://console.aws.amazon.com/a2i/](https://console.aws.amazon.com/a2i "https://console.aws.amazon.com/a2i").
2. In the navigation pane, under the **Augmented AI** section, choose
   **Human review workflows**.
3. Select the hyperlinked name of the human review workflow that you want to
   delete.
4. On the **Summary** page of your human review workflow, choose
   **Delete**.
5. In the dialog box asking you to confirm that you want to delete your human
   review workflow, choose **Delete**.

You're automatically redirected to the **Human review workflows**
page. While your human review workflow is being deleted, the status
**Deleting** appears in the status column for that workflow. After
it's deleted, it doesn't appear in the list of workflows on this page.

###### Delete a human review workflow (API)

You can delete a human review workflow (flow definition) using the SageMaker AI [DeleteFlowDefinition](../APIReference/API_DeleteFlowDefinition.md "../APIReference/API_DeleteFlowDefinition.md") API operation. This API operation is supported
through the [AWS CLI](../../../cli/latest/reference/sagemaker/delete-flow-definition.md "../../../cli/latest/reference/sagemaker/delete-flow-definition.md")
and a [variety of language specific SDKs](../APIReference/API_DeleteFlowDefinition.md#API_DeleteFlowDefinition_SeeAlso "../APIReference/API_DeleteFlowDefinition.md#API_DeleteFlowDefinition_SeeAlso"). The following table shows example
requests using SDK for Python (Boto3) and the AWS CLI to delete the human review workflow,
`example-flow-definition`.

AWS SDK for Python (Boto3)
The following request example uses the SDK for Python (Boto3) to delete the human
review workflow. For more information, see [delete_flow_definition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition") in the _AWS SDK for Python (Boto) API Reference_.

```
import boto3

sagemaker_client = boto3.client('sagemaker')
response = sagemaker_client.delete_flow_definition(FlowDefinitionName='`example-flow-definition`')
```

AWS CLI
The following request example uses the AWS CLI to delete the human
review workflow. For more information, see [delete-flow-definition](../../../cli/latest/reference/sagemaker/delete-flow-definition.md "../../../cli/latest/reference/sagemaker/delete-flow-definition.md") in the _[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")_.

```
`$` aws sagemaker delete-flow-definition --flow-definition-name '``example-flow-definition``'
```

If the action is successful, Augmented AI sends back an HTTP 200 response with an empty HTTP
body.
