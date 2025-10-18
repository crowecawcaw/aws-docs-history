# Widget


 A widget on a CloudTrail Lake dashboard.



## Contents





**QueryAlias** 


The query alias used to identify the query for the widget.



Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `^[a-zA-Z][a-zA-Z0-9._\-]*$`



Required: No




**QueryParameters** 



 The query parameters for the widget.



Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `.*`



Required: No




**QueryStatement** 



The SQL query statement for the widget.



Type: String


Length Constraints: Minimum length of 1. Maximum length of 10000.


Pattern: `(?s).*`



Required: No




**ViewProperties** 



 The view properties for the widget. For more information about view properties, see [View properties for widgets](../userguide/lake-widget-properties.md "../userguide/lake-widget-properties.md") in the *AWS CloudTrail User Guide*..



Type: String to string map


Key Length Constraints: Minimum length of 3. Maximum length of 128.


Key Pattern: `^[a-zA-Z0-9._\-]+$`



Value Length Constraints: Minimum length of 1. Maximum length of 128.


Value Pattern: `^[a-zA-Z0-9._\- ]+$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Widget "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Widget")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Widget "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Widget")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Widget "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Widget")
