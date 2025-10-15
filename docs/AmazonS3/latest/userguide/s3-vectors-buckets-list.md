# Listing vector buckets

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

You can view all your vector buckets using the Amazon S3 console or the AWS CLI. The listing
 operations support prefix-based filtering to help you find specific buckets when you have
 many vector buckets in your account. For more information about `ListVectorBuckets`, prefix
 limits, and response limits, see [ListVectorBuckets](../API/API_S3VectorBuckets_ListVectorBuckets.md "../API/API_S3VectorBuckets_ListVectorBuckets.md") in the *Amazon S3 API Reference*.


## Prefix search capability


Prefix search allows you to list buckets that start with a specific prefix, making it
 easier to organize and find related vector buckets. This is particularly useful when
 you use naming conventions that group related buckets together:



* **Environment-based**: `production-vectors-`,
 `staging-vectors-`, `dev-vectors-`
* **Use case-based**: `ml-model-vectors-`,
 `document-search-`, `image-similarity-`
* **Team-based**: `data-science-vectors-`,
 `ml-platform-vectors-`

To list vector buckets

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.


The console displays a list of all your vector buckets with the
 following information:




	* **Name** – The unique name of the
	 vector bucket
	* **Creation date** – When the bucket
	 was created
	* **Amazon Resource Name (ARN)** – The
	 full ARN for programmatic access
To filter the list:


* To find a bucket based on the start of the bucket name, enter a vector
 bucket name or prefix in the search box above the bucket list.
* Use prefixes to find groups of related buckets (for example, type "prod-"
 to find all production buckets)


The list updates in real-time as you type
