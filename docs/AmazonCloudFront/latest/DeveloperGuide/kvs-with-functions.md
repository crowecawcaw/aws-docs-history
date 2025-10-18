# Amazon CloudFront KeyValueStore

CloudFront KeyValueStore is a secure, global, low-latency key value datastore that allows read access from
 within [CloudFront Functions](cloudfront-functions.md "cloudfront-functions.md"), enabling advanced
 customizable logic at the CloudFront edge locations. 

With CloudFront KeyValueStore, you make updates to function code and updates to the data associated with a
 function independently of each other. This separation simplifies function code and makes it
 easy to update data without the need to deploy code changes. 

###### Note

To use CloudFront KeyValueStore, your CloudFront function must use [JavaScript runtime 2.0](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md").

The following is the general procedure for using key-value pairs: 


* Create key value stores, and populate it with a set of key-value pairs. You can add
 your key value stores to an Amazon S3 bucket or enter them manually.
* Associate the key value stores with your CloudFront function.
* Within your function code, use the name of the key to either retrieve the value
 associated with the key or to evaluate if a key exists. For more information about
 using key-value pairs in function code, and about helper methods, see [Helper methods for key value stores](functions-custom-methods.md "functions-custom-methods.md").

## Use cases


You can use key-value pairs for the following examples:



* **URL rewrites or redirects** – The key-value pair can
 hold the rewritten URLs or the redirect URLs.
* **A/B testing and feature flags** – You can create a
 function to run experiments by assigning a percentage of traffic to a specific
 version of your website.
* **Access authorization** – You can implement access
 control to allow or deny requests based on criteria defined by you and the data
 stored in a key value store.

## Supported formats for values


You can store the value in a key-value pair in any of the following formats:



* String
* Byte-encoded string
* JSON

## Security


The CloudFront function and all its key value stores data are handled securely, as
 follows:



* CloudFront encrypts each key value stores at rest and during transit (when reading or
 writing to the key value stores) when you call the [CloudFront KeyValueStore](../../../cloudfront/latest/APIReference/API_Operations_Amazon_CloudFront_KeyValueStore.md "../../../cloudfront/latest/APIReference/API_Operations_Amazon_CloudFront_KeyValueStore.md") API operations.
* When the function is run, CloudFront decrypts each key-value pair in memory at the
 CloudFront edge locations.

To get started with CloudFront KeyValueStore, see the following topics. 

###### Topics

* [Work with key value store](kvs-with-functions-kvs.md "kvs-with-functions-kvs.md")
* [Work with key value data](kvs-with-functions-kvp.md "kvs-with-functions-kvp.md")

* For more information about getting started with CloudFront KeyValueStore, see the [Introducing Amazon CloudFront KeyValueStore](https://aws.amazon.com/blogs/aws/introducing-amazon-cloudfront-keyvaluestore-a-low-latency-datastore-for-cloudfront-functions/ "https://aws.amazon.com/blogs/aws/introducing-amazon-cloudfront-keyvaluestore-a-low-latency-datastore-for-cloudfront-functions/") AWS blog post.
