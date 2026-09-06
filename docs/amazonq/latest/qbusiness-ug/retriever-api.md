

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Creating a retriever for an Amazon Q Business application using APIs
<a name="retriever-api"></a>

You can't create an Amazon Q Business retriever using the AWS Management Console. If you use the console, Amazon Q Business creates a retriever for you when you create an Amazon Q Business index. If you're using an Amazon Kendra index as retriever, adding an Amazon Kendra index will also add a retriever. 

**Note**  
You can only add an Amazon Kendra index as retriever if you have existing Amazon Kendra indexes.

When you use the APIs, you must create a retriever for your Amazon Q Business index separately.



| API action | API description | Relevant User Guide topic | 
| --- | --- | --- | 
| [CreateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateRetriever.html) | Creates an Amazon Q Business or Amazon Kendra retriever | +  [Creating an Amazon Q Business retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/native-retriever.html) <br />+  [Creating an Amazon Kendra retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/add-kendra-retriever.html)  | 
| [DeleteRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteRetriever.html) | Deletes an Amazon Q Business or Amazon Kendra retriever | +  [Deleting an Amazon Q Business retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-native-retriever-actions.html#delete-native-retriever) <br />+  [Deleting an Amazon Kendra retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-kendra-retriever-actions.html#delete-kendra-retriever)  | 
| [GetRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetRetriever.html) | Gets information about an existing Amazon Q Business or Amazon Kendra retriever | +  [Getting Amazon Q Business retriever properties](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-native-retriever-actions.html#describe-native-retriever) <br />+  [Getting Amazon Kendra retriever properties](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-kendra-retriever-actions.html#describe-kendra-retriever)  | 
| [ListRetrievers](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListRetrievers.html) | Lists existing Amazon Q Business or Amazon Kendra retrievers | +  [Listing retrievers](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-native-retriever-actions.html#list-native-retriever) <br />+  [Getting Amazon Kendra retriever properties](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-kendra-retriever-actions.html#list-kendra-retriever)  | 
| [UpdateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateRetriever.html) | Updates an existing Amazon Q Business or Amazon Kendra retriever | +  [Updating an Amazon Q Business retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-native-retriever-actions.html#update-native-retriever) <br />+  [Updating an Amazon Kendra retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-kendra-retriever-actions.html#update-kendra-retriever)  | 