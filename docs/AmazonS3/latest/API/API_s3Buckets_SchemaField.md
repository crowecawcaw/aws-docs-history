# SchemaField

Contains details about a schema field.


## Contents





**name** 


The name of the field.


Type: String


Required: Yes




**type** 


The field type. S3 Tables supports all Apache Iceberg primitive types. For more information, see the [Apache Iceberg documentation](https://iceberg.apache.org/spec/#primitive-types "https://iceberg.apache.org/spec/#primitive-types").


Type: String


Required: Yes




**required** 


A Boolean value that specifies whether values are required for each row in this field. By default, this is `false` and null values are allowed in the field. If this is `true` the field does not allow null values.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/SchemaField "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/SchemaField")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/SchemaField "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/SchemaField")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/SchemaField "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/SchemaField")
