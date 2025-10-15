# RestoreRequest

Container for restore job parameters.


## Contents





**Days** 


Lifetime of the active copy in days. Do not use with restores that specify
 `OutputLocation`.


The Days element is required for regular restores, and must not be provided for select
 requests.


Type: Integer


Required: No




**Description** 


The optional description for the job.


Type: String


Required: No




**GlacierJobParameters** 


S3 Glacier related parameters pertaining to this job. Do not use with restores that specify
 `OutputLocation`.


Type: [GlacierJobParameters](API_GlacierJobParameters.md "API_GlacierJobParameters.md") data type


Required: No




**OutputLocation** 


Describes the location where the restore job's output is stored.


Type: [OutputLocation](API_OutputLocation.md "API_OutputLocation.md") data type


Required: No




**SelectParameters** 


###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
 continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")



Describes the parameters for Select job types.


Type: [SelectParameters](API_SelectParameters.md "API_SelectParameters.md") data type


Required: No




**Tier** 


Retrieval tier at which the restore will be processed.


Type: String


Valid Values: `Standard | Bulk | Expedited`



Required: No




**Type** 


###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
 continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")



Type of restore request.


Type: String


Valid Values: `SELECT`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RestoreRequest "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RestoreRequest")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RestoreRequest "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RestoreRequest")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RestoreRequest "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RestoreRequest")
