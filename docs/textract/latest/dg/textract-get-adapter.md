

# Get adapter

You can retrieve configuration information for an adapter at any time by calling the [GetAdapter](https://docs.aws.amazon.com/textract/latest/APIReference/API_GetAdapter.html) operation and specifying an AdapterId. GetAdapter returns information on AdapterName, Description, CreationTime, AutoUpdate status, and FeatureTypes.

To see details for your adapter with the console:
+ Sign in to the [Amazon Textract console](https://console.aws.amazon.com/textract/).
+ Select **Custom Queries** from the navigation panel on the left.
+ From the list of **Your adapters**, select the adapter you want to view the details for.
+ Review the details for the adapter on your Adapter details page.

To see details for your adapter with the CLI/SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to get details on an adapter, replacing the example adapter ID with the ID of your own adapter: 

------
#### [ CLI ]

```
aws textract get-adapter \
--adapter-id "abcdef123456"
```

------