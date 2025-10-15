# Outpost

Contains the details for the Outpost object.


## Contents





**CapacityInBytes** 


The Amazon S3 capacity of the outpost in bytes.


Type: Long


Required: No




**OutpostArn** 


Specifies the unique Amazon Resource Name (ARN) for the outpost.


Type: String


Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)$`



Required: No




**OutpostId** 


Specifies the unique identifier for the outpost.


Type: String


Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`



Required: No




**OwnerId** 


Returns the AWS account ID of the outpost owner. Useful for comparing owned versus shared outposts.


Type: String


Pattern: `^\d{12}$`



Required: No




**S3OutpostArn** 


Specifies the unique S3 on Outposts ARN for use with AWS Resource Access Manager (AWS RAM).


Type: String


Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|\d{12})/s3$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/Outpost "https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/Outpost")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/Outpost "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/Outpost")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/Outpost "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/Outpost")
