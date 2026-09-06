

# Update adapter
<a name="textract-update-adapter"></a>

With Amazon Textract, you can update some configuration options of an adapter. Simultaneously, you can update any adapter versions associated with the adapter. To do this, call the [UpdateAdapter](https://docs.aws.amazon.com/textract/latest/APIReference/API_UpdateAdapter.html) operation and provide the operation with the AdapterId and configuration elements that you want to update. The AdapterName and FeatureTypes elements cannot be updated. 

To update an adapter with the AWS CLI or AWS SDK:
+ If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).
+ Use the following code to create an adapter: 

------
#### [ CLI ]

```
aws textract update-adapter \
--adapter-id 'abcdef123456' \  
--description 'demo new'
```

------