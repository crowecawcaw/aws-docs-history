

# Importing actions individually
<a name="importing-actions"></a>

After you complete [Creating a schema and a dataset](data-prep-creating-datasets.md) to create an [Actions dataset](actions-datasets.md), you can individually import one or more new actions into the dataset. When you individually import actions, you keep your Actions dataset current with small batch imports as your catalog grows. You can import up to 10 actions at a time. If you have a large number of new actions, we recommend that you first import data in bulk and then import action data individually as necessary. See [Importing bulk data into Amazon Personalize with a dataset import job](bulk-data-import-step.md).

You can use the Amazon Personalize console, the AWS Command Line Interface (AWS CLI), or AWS SDKs to import actions. If you import an action with the same `actionId` as an action that's already in your Actions dataset, Amazon Personalize replaces it with the new action.

For information about how new records influence recommendations, see [Updating data in datasets after training](updating-datasets.md). 

**Topics**
+ [Importing actions individually (console)](#importing-actions-console)
+ [Importing actions individually (AWS CLI)](#importing-actions-cli)
+ [Importing actions individually (AWS SDKs)](#importing-actions-cli-sdk)

## Importing actions individually (console)
<a name="importing-actions-console"></a>

You can import up to 10 actions into an Actions dataset at a time. This section assumes that you have already created an Actions dataset. For information about creating datasets, see [Creating a schema and a dataset](data-prep-creating-datasets.md).

**To import actions individually (console)**

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home) and sign in to your account.

1. On the **Dataset groups** page, choose the dataset group with the Actions dataset that you want to add to.

1. In the navigation pane, choose **Datasets**. 

1. On the **Datasets** page, choose the Actions dataset. 

1. At the top right of the dataset details page, choose **Modify dataset**, and then choose **Create record**. 

1. In **Create action record(s)** page, for **Record input**, enter the action details in JSON format. The action's field names and values must match the schema you used when you created the Actions dataset. Amazon Personalize provides a JSON template with field names and data types from this schema.

1. Choose **Create record(s)**. In **Response**, the result of the import is listed and a success or failure message is displayed.

## Importing actions individually (AWS CLI)
<a name="importing-actions-cli"></a>

Add one or more actions to your Actions dataset using the `PutActions` API operation. You can import up to 10 actions at once. This section assumes that you have already created an Actions dataset. For information about creating datasets, see [Creating a schema and a dataset](data-prep-creating-datasets.md).

Use the following `put-actions` command to add one or more actions with the AWS CLI. Replace `dataset arn` with the Amazon Resource Name (ARN) of your dataset and `actionId` with the ID of the action. If an action with the same `actionId` is already in your Actions dataset, Amazon Personalize replaces it with the new one.

For `properties`, for each field in your Actions dataset, replace the `propertyName` with the field name from your schema in camel case. For example, ACTION\_EXPIRATION\_TIMESTAMP would be `actionExpirationTimestamp` and CREATION\_TIMESTAMP would be creationTimestamp. Replace `property data` with the data for the property.

```
aws personalize-events put-actions \
  --dataset-arn {{dataset arn}} \
  --actions '[{
      "actionId": "{{actionId}}", 
      "properties": "{\"{{propertyName}}\": "\{{property data}}\"}" 
    }, 
    {
      "actionId": "{{actionId}}", 
      "properties": "{\"{{propertyName}}\": "\{{property data}}\"}" 
    }]'
```

## Importing actions individually (AWS SDKs)
<a name="importing-actions-cli-sdk"></a>

Add one or more actions to your Actions dataset using the PutActions operation. You can import up to 10 actions with a single `PutActions` call. If an action with the same `actionId` is already in your Actions dataset, Amazon Personalize replaces it with the new one. This section assumes that you have already created an Actions dataset. For information about creating datasets, see [Creating a schema and a dataset](data-prep-creating-datasets.md).

 The following code shows how to add one or more actions to your Actions dataset. For each action, specify the `actionId`. If an action with the same `actionId` is already in your Actions dataset, Amazon Personalize replaces it with the new one. For `properties`, for each additional field in your Actions dataset, replace the `propertyName` with the field name from your schema in camel case. For example, ACTION\_EXPIRATION\_TIMESTAMP would be `actionExpirationTimestamp` and CREATION\_TIMESTAMP would be creationTimestamp. Replace `property data` with the data for the property. 

```
import boto3

personalize_events = boto3.client(service_name='personalize-events')

personalize_events.put_actions(
    datasetArn = '{{dataset arn}}',
    actions = [{
      'actionId': '{{actionId}}',
      'properties': "{\"{{propertyName}}\": \"{{property value}}\"}"   
      },
      {
      'actionId': '{{actionId}}',
      'properties': "{\"{{propertyName}}\": \"{{property value}}\"}"   
      }]
)
```