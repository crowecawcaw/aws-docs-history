AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Sharing HealthOmics workflows

As the owner of a private workflow, you can share the workflow with an AWS account in the same region.
To share a workflow with more than one AWS account, you create multiple shares of the same workflow.

As the owner, you can revoke access to a shared workflow by deleting the share.

###### Note

HealthOmics automatically allows a shared workflow to access the Amazon ECR repository while the workflow is running in the
subscriber's account. You don't need to grant additional repository access for shared workflows.

When you share a workflow, the subscriber can use any of the workflow versions. If you need version-level access
control for a shared workflow, we recommend that you create separate workflows rather than using workflow
versions.

###### Topics

- [Subscribing to a shared workflow](#shared-workflow-subscribe "#shared-workflow-subscribe")
- [Monitoring status of a workflow share](#shared-workflow-monitor "#shared-workflow-monitor")
- [Sharing a private workflow using the console](#shared-workflow-create-console "#shared-workflow-create-console")
- [Sharing a private workflow using the CLI](#shared-workflow-create-api "#shared-workflow-create-api")
- [Accepting a shared workflow using the console](#shared-workflow-accept-console "#shared-workflow-accept-console")
- [Running a shared workflow using the console](#shared-workflow-using-console "#shared-workflow-using-console")
- [Running a shared workflow using the API](#shared-workflow-using-api "#shared-workflow-using-api")

## Subscribing to a shared workflow

To subscribe to a shared workflow, you follow these overall steps to accept and use the workflow:

1. Use the console or API to accept the share. Set your current region to the same region as the share request.
   - To find the share request in the console, navigate to the **All Resource
     shares** page, then choose the **Shared with me** tab.

2. Use the console or API to create a run for the shared workflow.
   - To find the workflow details page in the console, navigate to **Shared with me**
     (see step 1), then choose the **Resource link** for the shared workflow.

3. You provide your own input data for the workflow.
4. The shared workflow runs in your AWS account.

As the subscriber to a shared workflow, the system blocks you from performing the following workflow
actions:

- Exporting a shared workflow
- Re-running the shared workflow
  - You create a new run for the shared workflow.

- Re-sharing the workflow.
- Assigning a tag to the workflow.
- Deleting the workflow.
  - When you no longer need the workflow, you delete the workflow share.

See [Cross-account resource sharing in AWS HealthOmics](resource-sharing.md "resource-sharing.md") for additional information
about resource sharing.

## Monitoring status of a workflow share

HealthOmics sends an event to EventBridge for each status change of a workflow share. If you want to receive notifications about
specific status changes, set up an EventBridge rule to monitor **Workflow share Status Change** events.
For example:

- You want a notification each time you receive a workflow share request, and each time a user revokes a workflow
  share.
- After you initiate a workflow share request, you want to receive a notification when the user accepts or declines
  the request.

For details about using events, see [Using EventBridge with AWS HealthOmics](eventbridge.md "eventbridge.md").

## Sharing a private workflow using the console

From the console, you can share a private workflow with an AWS account in the same region as the workflow.

###### To share a private workflow

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Private workflows**.
3. From the **Workflows** table on the **Private workflows** page,
   select the workflow to share, and choose **Share**.
4. In the **Share details** panel of the **Share workflow** page,
   enter a descriptive name for the share and enter the AWS account of the subscriber.
5. Choose **Share resource**. The console displays resource shares in the
   **All resource shares** page.

The initial state of the share is pending. After the subscriber accepts the share, the state changes to
active.

## Sharing a private workflow using the CLI

Use the **create-share** API operation to create a workflow share. The
principal subscriber is the AWS account of the user who will get access to the workflow.

```
aws omics create-share \
  --resource-arn "arn:aws:omics:us-west-2:555555555555:workflow/123456" \
  --principal-subscriber "123456789012" \
  --name "my_Share-123"
```

If the create is successful, you receive a response with the share ID and status.

```
{
"shareId": "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a",
"name": "my_Share-123",
"status": "PENDING"
}
```

The share remains in pending state until the subscriber accepts it using the `accept-share`
API operation.

See [Cross-account resource sharing in AWS HealthOmics](resource-sharing.md "resource-sharing.md") for other API usage examples.

## Accepting a shared workflow using the console

You can use the console to accept an offered workflow share. Make sure to set the console to the same
Region as the workflow.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **All Resource shares**, then choose the
   **Shared with me** tab.
3. From the **Resources shared with me** table , select the workflow share and then
   choose **Accept**.

After you accept the workflow, choose the **Resource link** for the shared workflow
to view its details.

## Running a shared workflow using the console

After you accept a workflow share, you can start a run on the workflow.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **All Resource shares**, then choose the
   **Shared with me** tab.
3. From the **Resources shared with me** table, choose the **Resource
   link** for the shared workflow.
4. In the **Workflow details** page, choose **Create run**.

The console opens the **Create run** page, with the workflow type (shared) and
**Workflow ID** pre-populated. 5. Configure the remaining fields in the **Create run** form.
For additional information, see [Starting a run using the console](starting-a-run.md#starting-a-run-console "starting-a-run.md#starting-a-run-console").

## Running a shared workflow using the API

Use get-workflow to retrieve the ARN of the shared workflow.

```
aws omics get-workflow --id 1234567 \
--workflow-owner-id 55555555555
```

When you run the workflow, provide the workflow owner’s AWS account ID and the ARN of the shared
workflow.

```
aws omics start-run --id 1234567 --workflow-owner-id 55555555555 \
--role-arn arn:aws:iam::1234567892012:role/service-role/OmicsWorkflow-20221004T164236 \
--name ArchiveTest --retention-mode REMOVE
```
