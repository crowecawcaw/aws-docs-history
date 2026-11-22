

# List adapters

You can list all of the adapters associated with your account by using the [ListAdapters](https://docs.aws.amazon.com/textract/latest/APIReference/API_ListAdapters.html) operation. You can filter the list of returned adapters by the date and time of creation by using the AfterCreationTime and BeforeCreationTime arguments. You can also set a number of maximum results to return using MaxResults.

To see a list of your adapters with the console:
+ Sign in to the [Amazon Textract console](https://console.aws.amazon.com/textract/).
+ Select **Custom Queries** from the navigation panel on the left.
+ View your adapters in the list of your adapters.

To list your adapters with the AWS CLI or AWS SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to list your adapters: 

------
#### [ CLI ]

```
aws textract list-adapters 
```

------