# Update a Notebook Instance

After you create a notebook instance, you can update it using the SageMaker AI console and
[`UpdateNotebookInstance`](../APIReference/API_UpdateNotebookInstance.md "../APIReference/API_UpdateNotebookInstance.md") API operation.

You can update the tags of a notebook instance that is `InService`. To
update any other attribute of a notebook instance, its status must be
`Stopped`.

###### To update a notebook instance in the SageMaker AI console:

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **Notebook instances**.
3. Choose the notebook instance that you want to update by selecting the notebook
   instance **Name** from the list.
4. If your notebook **Status** is not `Stopped`,
   select the **Stop** button to stop the notebook instance.

When you do this, the notebook instance status changes to
`Stopping`. Wait until the status changes to `Stopped`
to complete the following steps. 5. Select the **Edit** button to open the **Edit
notebook instance** page. For information about the notebook
properties you can update, see [Create an Amazon SageMaker notebook instance](howitworks-create-ws.md "howitworks-create-ws.md"). 6. Update your notebook instance and select the **Update notebook
instance** button at the bottom of the page when you are done to
return to the notebook instances page. Your notebook instance status changes to
**Updating**.

When the notebook instance update is complete, the status changes to
`Stopped`.
