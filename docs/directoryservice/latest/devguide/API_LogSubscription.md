

# LogSubscription
<a name="API_LogSubscription"></a>

Represents a log subscription, which tracks real-time data from a chosen log group to a specified destination.

## Contents
<a name="API_LogSubscription_Contents"></a>

 ** DirectoryId **   <a name="DirectoryService-Type-LogSubscription-DirectoryId"></a>
Identifier (ID) of the directory that you want to associate with the log subscription.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** LogGroupName **   <a name="DirectoryService-Type-LogSubscription-LogGroupName"></a>
The name of the log group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[-._/#A-Za-z0-9]+`   
Required: No

 ** SubscriptionCreatedDateTime **   <a name="DirectoryService-Type-LogSubscription-SubscriptionCreatedDateTime"></a>
The date and time that the log subscription was created.  
Type: Timestamp  
Required: No

## See Also
<a name="API_LogSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/LogSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/LogSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/LogSubscription) 