# Delete a workflow version

You can delete a user-defined workflow version using the console, CLI, or one of the SDKs. Deleting a workflow
version doesn't affect any ongoing runs that are using the workflow version.

You can't delete the [Default workflow version](workflows-default-version.md "workflows-default-version.md"). You delete all the user-defined versions, then delete the workflow.

###### Topics

- [Delete a workflow version using the console](#workflow-versions-console-delete "#workflow-versions-console-delete")
- [Delete a workflow version using the CLI](#workflow-versions-api-delete "#workflow-versions-api-delete")
- [Delete a workflow version using an SDK](#workflow-versions-sdk-delete "#workflow-versions-sdk-delete")

## Delete a workflow version using the console

###### To delete a workflow version

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Private workflows**.
3. On the **Private workflows** page, choose the workflow.
4. On the **Workflow** page, choose the workflow version to delete and choose
   **Delete selected** from the **Actions** list.
5. In the **Delete workflow version** modal, enter "confirm" to confirm the deletion.
6. Choose **Delete**.

The console displays a page banner with the deleted workflow version.

## Delete a workflow version using the CLI

You can delete a user-defined workflow version using the following CLI command. The combination of workflow ID
and version name uniquely identifies the version.

```
aws omics delete-workflow-version
--workflow-id 9876543
--version-name "my_version"
```

You receive no response to the `delete-workflow-version` request.

## Delete a workflow version using an SDK

You can delete a workflow using one of the SDKs.

The following example shows how to delete a workflow using the Python SDK.

```
import boto3

omics = boto3.client('omics')

response = omics.delete_workflow_version(
   workflowID=1234567,
   versionName='3.0.0'
)
```
