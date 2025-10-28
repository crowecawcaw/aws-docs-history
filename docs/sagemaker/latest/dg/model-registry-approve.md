# Update the Approval Status of a

Model

After you create a model version, you typically want to evaluate its performance
before you deploy it to a production endpoint. If it performs to your requirements,
you can update the approval status of the model version to `Approved`.
Setting the status to `Approved` can initiate CI/CD deployment for the
model. If the model version does not perform to your requirements, you can update
the approval status to `Rejected`.

You can manually update the approval status of a model version after you register
it, or you can create a condition step to evaluate the model when you create a SageMaker AI
pipeline. For information about creating a condition step in a SageMaker AI pipeline, see
[Pipelines steps](build-and-manage-steps.md "build-and-manage-steps.md").

When you use one of the SageMaker AI provided project templates and the approval status of
a model version changes, the following action occurs. Only valid transitions are
shown.

- `PendingManualApproval` to `Approved` –
  initiates CI/CD deployment for the approved model version
- `PendingManualApproval` to `Rejected` – No
  action
- `Rejected` to `Approved` – initiates CI/CD
  deployment for the approved model version
- `Approved` to `Rejected` – initiates CI/CD to
  deploy the latest model version with an `Approved` status
  You can update the approval status of a model version by using the AWS SDK for Python (Boto3)
  or by using the Amazon SageMaker Studio console. You can also update the approval status of
  a model version as part of a condition step in a SageMaker AI pipeline. For information
  about using a model approval step in a SageMaker AI pipeline, see [Pipelines overview](pipelines-overview.md "pipelines-overview.md").

## Update the Approval Status of a

Model (Boto3)

When you created the model version in [Register a Model Version](model-registry-version.md "model-registry-version.md"), you set the
`ModelApprovalStatus` to `PendingManualApproval`. You
update the approval status for the model by calling
`update_model_package`. Note that you can automate this process
by writing code that, for example, sets the approval status of a model depending
on the result of an evaluation of some measure of the model's performance. You
can also create a step in a pipeline that automatically deploys a new model
version when it is approved. The following code snippet shows how to manually
change the approval status to `Approved`.

```
model_package_update_input_dict = {
    "ModelPackageArn" : model_package_arn,
    "ModelApprovalStatus" : "Approved"
}
model_package_update_response = sm_client.update_model_package(**model_package_update_input_dict)
```

## Update the Approval Status of a

Model (Studio or Studio Classic)

To manually change the approval status in the Amazon SageMaker Studio console,
complete the following steps based on whether you use Studio or
Studio Classic.

Studio

1. Open the SageMaker Studio console by following the
   instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose the
   **Models** to display a list of your
   model groups.
3. Choose the **Registered models** tab, if
   not selected already.
4. Immediately below the **Registered
   models** tab label, choose **Model
   Groups**, if not selected already.
5. From the model groups list, choose the angle bracket to
   the left of the model group that you want to view.
6. A list of the model versions in the model group appears.
   If you don't see the model version that you want to delete,
   choose **View all** to display the complete
   list of model versions in the model group details
   page.
7. Select the name of the model version that you want to
   update.
8. The **Deploy** tab displays the current
   approval status. Choose the dropdown menu next to the
   current approval status and select the updated approval
   status.

Studio Classic

1. Sign in to Amazon SageMaker Studio Classic. For more information, see
   [Launch
   Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the left navigation pane, choose the
   **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Choose **Models**, and then
   **Model registry**.
4. From the model groups list, select the name of the Model
   Group that you want to view. A new tab opens with a list of
   the model versions in the Model Group.
5. In the list of model versions, select the name of the
   model version that you want to update.
6. Under the **Actions** dropdown menu, you
   can choose one of two possible menu options to update the
   model version status.
   - Using the **Update Status**
     option
     1. Under the **Actions**
        dropdown menu, choose the **Update
        Status** dropdown menu, and choose the
        new model version status.
     2. (Optional) In the
        **Comment** field, add additional
        details.
     3. Choose **Save and
        Update**.

   - Using the **Edit** option
     1. Under the **Actions**
        dropdown menu, choose
        **Edit**.
     2. (Optional) In the
        **Comment** field, add additional
        details.
     3. Choose **Save
        changes**.

7. Confirm the model version status is updated to the correct
   value in the model version page.
