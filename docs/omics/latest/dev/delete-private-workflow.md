AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Delete a private workflow

When you no longer need a workflow, you can delete it using the HealthOmics console,
AWS CLI commands, or one of the AWS SDKs.
You can delete a workflow that meets the following criteria:

- Its status is ACTIVE or FAILED.
- It has no active shares.
- You've deleted all the workflow versions.
  Deleting a workflow doesn't affect any ongoing runs that are using the workflow.

###### Topics

- [Deleting a workflow using the console](#console-delete-workflows "#console-delete-workflows")
- [Deleting a workflow using the CLI](#api-delete-workflows "#api-delete-workflows")
- [Deleting a workflow using an SDK](#sdk-delete-workflows "#sdk-delete-workflows")

## Deleting a workflow using the console

###### To delete a workflow

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Private workflows**.
3. On the **Private workflows** page, choose the workflow to delete.
4. On the **Workflow** page, choose **Delete selected** from the
   **Actions** list.
5. In the **Delete workflow** modal, enter "confirm" to confirm the deletion.
6. Choose **Delete**.

## Deleting a workflow using the CLI

The following example shows how you can use the AWS CLI command to delete a
workflow. To run the example, replace the `workflow id` with the ID of the workflow you want to delete.

```
aws omics delete-workflow
  --id ``workflow id``
```

HealthOmics doesn't send a response to the `delete-workflow` request.

## Deleting a workflow using an SDK

You can delete a workflow using one of the SDKs.

The following example shows how to delete a workflow using the Python SDK.

```
import boto3

omics = boto3.client('omics')

response = omics.delete_workflow(
   id='1234567'
)
```
