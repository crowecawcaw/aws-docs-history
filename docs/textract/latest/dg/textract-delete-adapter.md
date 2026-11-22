

# Delete an adapter

You can delete a custom Amazon Textract Core adapter at any time by calling the [DeleteAdapter](https://docs.aws.amazon.com/textract/latest/APIReference/API_DeleteAdapter.html) API operation. You can delete an adapter by providing the DeleteAdapter operation with the AdapterId of the adapter that you want to delete. Invoking DeleteAdapter will delete all Adapter Versions associated with the Adapter ARN.

To delete an adapter with the console:
+ Sign in to the [Amazon Textract console](https://console.aws.amazon.com/textract/).
+ Select **Custom Queries** from the left navigation panel.
+ From the list of your adapters, select the adapter to delete.
+ Select **Delete** and follow the instructions to delete your adapter.

To delete an adapter with the AWS CLI or AWS SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to delete an adapter, replacing the example adapter ID with the ID of your own adapter: 

------
#### [ CLI ]

```
aws textract delete-adapter \
--adapter-id 'abcdef123456'
```

------