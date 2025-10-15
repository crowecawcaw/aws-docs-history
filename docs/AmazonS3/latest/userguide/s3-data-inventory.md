# Amazon Simple Storage Service data inventory


## Amazon S3


Amazon S3 provides scalable object storage in the AWS Cloud. It allows you to store and retrieve any amount of data from anywhere on the web. 
 Based on its unique architecture, S3 is designed to exceed 99.999999999% (11 nines) data durability. Additionally, S3 stores data redundantly 
 across a minimum of 3 Availability Zones by default, providing built-in resilience against widespread disaster. Customers can store data in a 
 single Availability Zone to minimize storage cost or latency, in multiple Availability Zones for resilience against the permanent loss of an entire data center, or in multiple 
 AWS Regions to meet geographic resilience requirements. 



###### Key Characteristics



Geographic location

Amazon S3 is hosted in multiple locations worldwide. You select locations for your data that put them close to your customers.



Buckets

A bucket is a container for objects stored in Amazon S3. Every object is contained within a bucket.



Objects

Objects are the fundamental entities stored in Amazon S3. Objects consist of object data and metadata.



Storage Classes

Amazon S3 offers different storage classes optimized for different use cases.



Storage Management

Amazon S3 has storage management features that you can use to manage costs and adhere to compliance requirements. 
 



Access management and security

Amazon S3 provides features for auditing and managing access to your buckets and objects.




## Geographic location


Amazon S3 is available in every AWS Region worldwide. Each Region is a separate geographic area.


### Why this matters


After you determine where you want to store your data, you can decide whether to deploy functionally equivalent storage in the same locations or different locations, depending on your needs.


### To get a summary of your Amazon S3 buckets across all Regions


Use the following AWS CLI command:



```

   aws s3api list-buckets /
    --max-items 100 / 
    --page-size 100 
   
```

For more information, see [list-buckets](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-buckets.html "https://docs.aws.amazon.com/cli/latest/reference/s3api/list-buckets.html") in the AWS CLI Command Reference.


## Buckets


Amazon S3 buckets are containers for objects. Each bucket has a unique name across all of AWS. Amazon S3 supports four types of buckets: general purpose buckets, 
 Directory buckets, table buckets, and vector buckets. Each type of bucket provides a unique set of features for different use cases. For more information on the 
 different bucket types, see [Buckets](Welcome.md#BasicsBucket "Welcome.md#BasicsBucket") in the Amazon S3 User Guide.


### Why these matter


After you list your buckets, you can validate your buckets settings for functionally equivalent storage systems by reviewing the various bucket configuration settings. 
 


### To list bucket configurations



```
aws s3api get-bucket-versioning --bucket ``amzn-s3-demo-bucket1``
aws s3api get-bucket-encryption --bucket ``amzn-s3-demo-bucket1``
aws s3api get-bucket-logging --bucket ``amzn-s3-demo-bucket1``
```

For more information, see [get-bucket-versioning](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-bucket-versioning.html "https://docs.aws.amazon.com/cli/latest/reference/s3api/get-bucket-versioning.html") in the AWS CLI Command Reference.


## Objects


Objects are the fundamental entities stored in Amazon S3. Each object consists of data, a key (name), and metadata.


### Why these matter


Understanding your object characteristics helps plan for equivalent storage capacity and performance requirements in functionally equivalent systems.


### To list objects and their properties



```
aws s3api list-objects-v2 --bucket ``amzn-s3-demo-bucket1`` /
    --query 'Contents[].{Key: Key, Size: Size, LastModified: LastModified}'
```

For more information, see [list-objects-v2](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-objects-v2.html "https://docs.aws.amazon.com/cli/latest/reference/s3api/list-objects-v2.html") in the AWS CLI Command Reference.


## Storage Classes



* Amazon S3 Standard
* Amazon S3 Intelligent-Tiering
* Amazon S3 Standard-IA
* Amazon S3 One Zone-IA
* Amazon S3 Glacier Instant Retrieval
* Amazon S3 Glacier Flexible Retrieval
* Amazon S3 Glacier Deep Archive
* Amazon S3 Express One Zone

### Why these matter


Understanding your storage class usage helps determine appropriate storage tiers in functionally equivalent systems. For more information, see 
 [Understanding and managing Amazon S3 storage classes](storage-class-intro.md "storage-class-intro.md") in the Amazon S3 User Guide.


### To review setorage class selection and usage


You can use Amazon S3 Storage Lens to review your storage class selection and usage. For more information, 
 see [Understanding and manage Amazon S3 storage classes](storage-class-intro.md "storage-class-intro.md") in the Amazon S3 User Guide.


## Storage management


### Why this matters


Understanding your storage management usage helps plan for equivalent features to manage costs and adhere to compliance requirements in functionally equivalent systems.


### To review storage managment feature selection and usage


You can use Amazon S3 Storage Lens to review your usage of storage management features. For more information, see 
 [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md") in the Amazon S3 User Guide.
 


## Access management and security


### Why these matter


Understanding your access management and security settings help you plan for equivalent features to manage access and security requirements in functionally 
 equivalent systems.


### To review your access management and security settings


After you list your buckets, you can validate your buckets security and access settings for functionally equivalent storage systems by reviewing the various 
 bucket configuration settings.



```

aws s3api get-public-access-block --bucket `amzn-s3-demo-bucket1` 
aws s3api get-bucket-acl --bucket `amzn-s3-demo-bucket1` 
aws s3api get-bucket-encryption --bucket `amzn-s3-demo-bucket1`
aws s3api get-bucket-policy --bucket `amzn-s3-demo-bucket1`
    
```

## Data Transfer


You can transfer data from Amazon S3 using several methods:



* AWS CLI
* AWS SDK
* Amazon S3 REST API
* Third-party tools

### Example using AWS CLI


To download an entire bucket:



```
aws s3 sync s3://``amzn-s3-demo-bucket1`` /local/path
```

For more information, see [sync](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html "https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html") in the AWS CLI Command Reference.


To download specific objects:



```
aws s3 cp s3://``amzn-s3-demo-bucket1``/path/to/object /local/path
```

For more information, see [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html "https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html") in the AWS CLI Command Reference.


## Related Resources


The following are additional characteristics of Amazon S3:



* [Access control in Amazon S3](access-management.md "access-management.md")
* [Security in Amazon S3](security.md "security.md")
* [Data protection in Amazon S3](data-protection.md "data-protection.md")
* [Logging and monitoring in Amazon S3](monitoring-overview.md "monitoring-overview.md")
