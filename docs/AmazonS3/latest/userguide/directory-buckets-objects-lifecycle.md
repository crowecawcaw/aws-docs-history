# Working with S3 Lifecycle for
 directory buckets

 S3 Lifecycle helps you store objects in S3 Express One Zone in directory buckets cost
 effectively by deleting expired objects on your behalf. To manage the lifecycle of your
 objects, create an S3 Lifecycle configuration for your directory bucket. An S3 Lifecycle
 configuration is a set of rules that define actions that Amazon S3 applies to a group of
 objects. You can set an Amazon S3 Lifecycle configuration on a directory bucket by using the
 AWS Command Line Interface (AWS CLI), the AWS SDKs, the Amazon S3 REST API and AWS
 CloudFormation. 

In your lifecycle configuration, you use rules to define actions that you want Amazon S3 to take on your objects. 
 For objects stored in directory buckets, you can create lifecycle rules to expire objects as they age. 
 You can also create lifecycle rules to delete incomplete multipart uploads in directory buckets at a daily frequency. 

When you add a Lifecycle configuration to a bucket, the configuration rules apply to both
 existing objects and objects that you add later. For example, if you add a Lifecycle
 configuration rule today with an expiration action that causes objects with a specific
 prefix to expire 30 days after creation, S3 will queue for removal any existing objects that
 are more than 30 days old and that have the specified prefix.


## How S3 Lifecycle for directory buckets is different


For objects in directory buckets, you can create lifecycle rules to expire objects and delete incomplete multipart uploads. 
 However, S3 Lifecycle for directory buckets doesn't support transition actions between storage classes. 
 


**CreateSession**


Lifecycle uses public `DeleteObject` and `DeleteObjects` API operations to expire objects in directory buckets. 
 To use these API operations, S3 Lifecycle will use the `CreateSession` API to establish temporary security credentials 
 to access the objects in the directory buckets. For more information, see [`CreateSession`in the *Amazon S3 API Reference*.](../API/API_CreateSession.md "../API/API_CreateSession.md")



If you have an active policy that denies delete permissions to the 
 lifecycle principal, this will prevent you from allowing S3 Lifecycle to delete objects on your behalf. 


### Using a bucket policy to Grant permissions to the S3 Lifecycle service principal


The following bucket policy grants permission to allow CreateSession calls with the
 default `ReadWrite` session and allows the lifecycle service principal.


###### Example – Bucket policy to allow `CreateSession` calls with the default
 `ReadWrite` session


```

 { 
   "Version":"2008-10-17",		 	 	  
   "Statement":[
      {
         "Effect":"Allow",
         "Principal": {
            "Service":"lifecycle.s3.amazonaws.com"
          },
          "Action":"s3express:CreateSession", 
          "Condition": { 
             "StringEquals": {
                "s3express:SessionMode": "ReadWrite"
              }
           }, 
           "Resource":"arn:aws:s3express:us-east-2:412345678921:bucket/amzn-s3-demo-bucket--use2-az2--x-s3"
       }
   ] 
}
						
```

**Monitoring lifecycle rules**

For objects stored in directory buckets, S3 Lifecycle generates AWS CloudTrail management and data event logs.
 For more information, see [CloudTrail log file examples for S3 Express One Zone](s3-express-log-files.md "s3-express-log-files.md").
 

For more information about creating lifecycle configurations and troubleshooting S3 Lifecycle related issues, see the following topics: 

###### Topics

* [Creating and managing a Lifecycle
 configuration for your directory bucket](directory-bucket-create-lc.md "directory-bucket-create-lc.md")
* [Troubleshooting S3 Lifecycle issues for directory buckets](directory-buckets-lifecycle-troubleshooting.md "directory-buckets-lifecycle-troubleshooting.md")
