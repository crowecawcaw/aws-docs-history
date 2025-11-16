# Edit a dataset

###### Note

The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see
[SiteWise Monitor availability change](../appguide/iotsitewise-monitor-availability-change.md "../appguide/iotsitewise-monitor-availability-change.md").

Console

###### Edit a dataset

1. Datasets are displayed in the **Datasets** section of the **Assistant** page.
   Choose a dataset to edit. Choose **Edit** to start editing.
2. In the **Dataset details** page, choose a Kendra index from the drop down menu to
   associate with the dataset.
3. The dataset name is populated by the Kendra index selected in Step 2. Edit the name if needed.
4. (Optional) The dataset description is populated by the Kendra index selected in Step 2. Edit the description if needed.
5. In the **Permissions** section, choose from below:
   1. Choose **Create and use a new service role**. By default, AWS IoT SiteWise automatically
      creates a service role. This role allows the AWS IoT SiteWise Assistant to access your Kendra
      indexes.
   2. Choose **Use an existing service role**, and then choose the target role.

6. Choose **Save changes** to save your selection.

![Editing a dataset final picture in the Assistant page of the console](images/ai-assistant-edit-details-dataset.png)

AWS CLI

###### Edit a dataset in AWS CLI

1. Create a file **update-dataset.json** with the template provided in the example. Populate
   `datasetId`, `kendra knowledgeBaseArn` and `roleArn` to connect with this dataset.

```

{
    "datasetId": "<UUID>",
    "datasetName": "DatasetForAssistant",
    "datasetSource": {
       "sourceType": "KENDRA",
       "sourceFormat": "KNOWLEDGE_BASE",
       "sourceDetail": {
          "kendra": {
            "knowledgeBaseArn": "arn:aws:kendra::%s:index/index",
            "roleArn": "arn:aws:iam::%s:role/role"
          }
       }
    }
}

```

2. Update the dataset with the following command:

```
aws iotsitewise update-dataset --cli-input-json `file://update-dataset.json` —-region us-east-1

```
