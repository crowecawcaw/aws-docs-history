

# List adapter versions

An Amazon Textract Core adapter can have a number of different versions associated with it. In order to see which adapter versions are associated with a given adapter, you can call the [ListAdapterVersions](https://docs.aws.amazon.com/textract/latest/APIReference/API_ListAdapterVersions.html) operation. The operation will return all versions of an adapter unless provided with filtering criteria using the optional arguments such as AdapterId, AfterCreationTime, BeforeCreationTime, Statuses, or MaxResults.

To see a list of your adapter versions with the console:
+ Sign in to the [Amazon Textract console](https://console.aws.amazon.com/textract/).
+ Select **Custom Queries** from the left navigation panel.
+ From the list of your adapters, select the adapter.
+ View the adapter versions in the **Adapter versions** box.

To list your adapter versions with the AWS CLI or AWS SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to list your adapter versions: 

------
#### [ CLI ]

```
aws textract list-adapter-versions 
```

------