AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Update a private workflow

You can update a workflow using the HealthOmics console, AWS CLI commands, or one of the AWS SDKs.

###### Note

Don’t include any personally identifiable information (PII) in workflow names. These names are visible in
CloudWatch logs.

###### Topics

- [Updating a workflow using the console](#console-update-workflows "#console-update-workflows")
- [Updating a workflow using the CLI](#api-update-workflows "#api-update-workflows")
- [Updating a workflow using an SDK](#sdk-update-workflows "#sdk-update-workflows")

## Updating a workflow using the console

###### Steps to update a workflow

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Private workflows**.
3. On the **Private workflows** page, choose the workflow to update.
4. On the **Workflow** page:
   - If the workflow has versions, make sure that you select the **Default
     version**.
   - Choose **Edit selected** from the **Actions** list.

5. On the **Edit workflow** page, you can change any of the
   following values:
   - **Workflow name**.
   - **Workflow description**.
   - The default **Run storage type** for the workflow.
   - The default **Run storage capacity** (if the run storage type is static
     storage). For more information about the default run storage configuration, see
     [Creating a workflow using the console](create-private-workflow.md#console-create-workflows "create-private-workflow.md#console-create-workflows").

6. Choose **Save changes** to apply the changes.

## Updating a workflow using the CLI

As shown in the following example, you can update the workflow name and description. You can also change the
default run storage type (STATIC or DYNAMIC) and run storage capacity (for static storage type). For more
information about run storage types, see [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md").

```
aws omics update-workflow    \
  --id 1234567    \
  --name my_workflow      \
  --description "updated workflow"    \
  --storage-type 'STATIC'    \
  --storage-capacity 1200
```

You don't receive a response to the `update-workflow` request.

## Updating a workflow using an SDK

You can update a workflow using one of the SDKs.

The following example shows how to update a workflow using the Python SDK

```
import boto3

omics = boto3.client('omics')

response = omics.update_workflow(
   name='my_workflow',
   description='updated workflow'
)
```
