# CSVOutput

Describes how uncompressed comma-separated values (CSV)-formatted results are formatted.


## Contents





**FieldDelimiter** 


The value used to separate individual fields in a record. You can specify an arbitrary
 delimiter.


Type: String


Required: No




**QuoteCharacter** 


A single character used for escaping when the field delimiter is part of the value. For example, if
 the value is `a, b`, Amazon S3 wraps this field value in quotation marks, as follows: `" a ,
 b "`.


Type: String


Required: No




**QuoteEscapeCharacter** 


The single character used for escaping the quote character inside an already escaped value.


Type: String


Required: No




**QuoteFields** 


Indicates whether to use quotation marks around output fields. 



* `ALWAYS`: Always use quotation marks for output fields.
* `ASNEEDED`: Use quotation marks for output fields when needed.

Type: String


Valid Values: `ALWAYS | ASNEEDED`



Required: No




**RecordDelimiter** 


A single character used to separate individual records in the output. Instead of the default value,
 you can specify an arbitrary delimiter.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CSVOutput "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CSVOutput")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CSVOutput "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CSVOutput")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CSVOutput "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CSVOutput")
