Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchReadException

The batch read exception structure, which contains the exception type and
 message.


## Contents





**Message** 


An exception message that is associated with the failure.


Type: String


Required: No




**Type** 


A type of exception, such as `InvalidArnException`.


Type: String


Valid Values: `ValidationException | InvalidArnException | ResourceNotFoundException | InvalidNextTokenException | AccessDeniedException | NotNodeException | FacetValidationException | CannotListParentOfRootException | NotIndexException | NotPolicyException | DirectoryNotEnabledException | LimitExceededException | InternalServiceException`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadException "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadException")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadException "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadException")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadException "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadException")
