

# EventTopic
<a name="API_EventTopic"></a>

Information about Amazon SNS topic and AWS Directory Service directory associations.

## Contents
<a name="API_EventTopic_Contents"></a>

 ** CreatedDateTime **   <a name="DirectoryService-Type-EventTopic-CreatedDateTime"></a>
The date and time of when you associated your directory with the Amazon SNS topic.  
Type: Timestamp  
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-EventTopic-DirectoryId"></a>
The Directory ID of an AWS Directory Service directory that will publish status messages to an Amazon SNS topic.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** Status **   <a name="DirectoryService-Type-EventTopic-Status"></a>
The topic registration status.  
Type: String  
Valid Values: `Registered | Topic not found | Failed | Deleted`   
Required: No

 ** TopicArn **   <a name="DirectoryService-Type-EventTopic-TopicArn"></a>
The Amazon SNS topic ARN (Amazon Resource Name).  
Type: String  
Required: No

 ** TopicName **   <a name="DirectoryService-Type-EventTopic-TopicName"></a>
The name of an Amazon SNS topic the receives status messages from the directory.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

## See Also
<a name="API_EventTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/EventTopic) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/EventTopic) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/EventTopic) 