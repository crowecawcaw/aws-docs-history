AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Update a workflow version

You can update the description and the default run storage configuration for a private workflow version. To
change any other information in the workflow version, create a new version.

###### Topics

- [Update a workflow version using the console](#workflow-versions-console-update "#workflow-versions-console-update")
- [Update a workflow version using the CLI](#workflow-versions-api-update "#workflow-versions-api-update")
- [Update a workflow version using an SDK](#workflow-versions-sdk-update "#workflow-versions-sdk-update")

## Update a workflow version using the console

###### To update a workflow version

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Private workflows**.
3. On the **Private workflows** page, choose the workflow.
4. On the **Workflow** page, choose the workflow version to update and choose
   **Edit selected** from the **Actions** list.
   - If you choose the default version, the console opens the **Edit workflow** page. For more
     information, see [Update a private workflow](update-private-workflow.md "update-private-workflow.md").
   - If you choose a user-defined version, the console opens the **Edit version** page.

5. On the **Edit version** page, provide the following information
   - **Version description** (optional) - A description of
     this version.

6. In the **Default run storage configuration** panel, provide the following default values
   for runs that use this workflow version. You can override the default values when you start a run:
   - For **Run storage type**, select **Static** or **Dynamic**.
   - For static run storage, select the default amount of **Run storage capacity** for
     runs that use this workflow version. The default value for this parameter is 1200 GiB.

7. Choose **Save changes**.

The console returns to the workflow detail page and displays a page banner with the updated workflow version.

## Update a workflow version using the CLI

You can update parameters for a workflow version using the following CLI command. The combination of workflow ID and version
name uniquely identifies the version.

```
aws omics update-workflow-version
--workflow-id 1234567
--version-name "my_version"
--storage-type 'STATIC'
--storage-capacity 2400
--description "version description"
```

You receive no response to the `update-workflow-version` request.

## Update a workflow version using an SDK

You can update a workflow version using one of the SDKs. The following python SDK example shows how to update
the storage type and description for a workflow version.

```
import boto3

omics = boto3.client('omics')

response = omics.update_workflow_version(
   workflowID=1234567,
   versionName='3.0.0',
   storageType='DYNAMIC',
   description='new version description'
)
```
