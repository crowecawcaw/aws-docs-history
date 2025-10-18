# ImportsListItem

 Contains information about an import that was returned by a lookup request. 


## Contents





**CreatedTimestamp** 


 The timestamp of the import's creation. 


Type: Timestamp


Required: No




**Destinations** 


 The ARN of the destination event data store. 


Type: Array of strings


Array Members: Fixed number of 1 item.


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




**ImportId** 


 The ID of the import. 


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`



Required: No




**ImportStatus** 


 The status of the import. 


Type: String


Valid Values: `INITIALIZING | IN_PROGRESS | FAILED | STOPPED | COMPLETED`



Required: No




**UpdatedTimestamp** 


 The timestamp of the import's last update. 


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ImportsListItem "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ImportsListItem")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ImportsListItem "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ImportsListItem")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ImportsListItem "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ImportsListItem")
