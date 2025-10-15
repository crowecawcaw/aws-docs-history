# Examples: Signature Calculations in AWS Signature
 Version 4

###### Topics

* [Signature Calculation Examples Using Java (AWS
 Signature Version 4)](#sig-v4-examples-using-sdk-java "#sig-v4-examples-using-sdk-java")
* [Examples of Signature Calculations Using C# (AWS Signature Version 4)](#sig-v4-examples-using-sdk-dotnet "#sig-v4-examples-using-sdk-dotnet")
 For authenticated requests, unless you are using the AWS SDKs, you have to write code to
 calculate signatures that provide authentication information in your requests. Signature
 calculation in AWS Signature Version 4 (see [Authenticating Requests (AWS Signature Version
 4)](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md")) can be a complex undertaking, and we
 recommend that you use the AWS SDKs whenever possible. 

 This section provides examples of signature calculations written in Java and C#. The code
 samples send the following requests and use the HTTP Authorization header to provide
 authentication information:


* **PUT object** – Separate examples illustrate both uploading the full payload at once and
 uploading the payload in chunks. For information about using the Authorization
 header for authentication, see [Authenticating Requests: Using the
 Authorization Header (AWS Signature Version 4)](sigv4-auth-using-authorization-header.md "sigv4-auth-using-authorization-header.md").
* **GET object** – This example generates a presigned URL to get an object. Query
 parameters provide the signature and other authentication information. Users can
 paste a presigned URL in their browser to retrieve the object, or you can use
 the URL to create a clickable link. For information about using query parameters
 for authentication, see [Authenticating Requests: Using Query Parameters (AWS
 Signature Version 4)](sigv4-query-string-auth.md "sigv4-query-string-auth.md").
The rest of this section describes the examples in Java and C#. The topics include
 instructions for downloading the samples and for executing them.

## Signature Calculation Examples Using Java (AWS
 Signature Version 4)


The Java sample that shows signature calculation can be downloaded at [https://docs.aws.amazon.com/AmazonS3/latest/API/samples/AWSS3SigV4JavaSamples.zip](samples/AWSS3SigV4JavaSamples.zip "samples/AWSS3SigV4JavaSamples.zip"). Note that these samples use AWS SDK for Java v1, and we recommend using [AWS SDK for Java v2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html "https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html") for new applications. In
 `RunAllSamples.java`, the `main()` function executes sample
 requests to create an object, retrieve an object, and create a presigned URL for the
 object. The sample creates an object from the text string provided in the code:



```
PutS3ObjectSample.putS3Object(bucketName, regionName, awsAccessKey, awsSecretKey); 
GetS3ObjectSample.getS3Object(bucketName, regionName, awsAccessKey, awsSecretKey); 
PresignedUrlSample.getPresignedUrlToS3Object(bucketName, regionName, awsAccessKey, awsSecretKey); 
PutS3ObjectChunkedSample.putS3ObjectChunked(bucketName, regionName, awsAccessKey, awsSecretKey);
```


###### To test the examples on a Linux-based computer


The following instructions are for the Linux operating system.


1. In a terminal, navigate to the directory that contains
 `AWSS3SigV4JavaSamples.zip`.
2. Extract the .zip file.
3. In a text editor, open the file
 `./com/amazonaws/services/s3/samples/RunAllSamples.java`. Update
 code with the following information:







	* The name of a bucket where the new object can be created. 
	
	
	
	
	
	###### Note
	
	The examples use a virtual-hosted style request to
	 access the bucket. To avoid potential errors, ensure
	 that your bucket name conforms to the bucket naming
	 rules as explained in [Bucket Restrictions and Limitations](../userguide/BucketRestrictions.md "../userguide/BucketRestrictions.md") in the
	 *Amazon Simple Storage Service User Guide*.
	* AWS Region where the bucket resides. 
	
	
	 If bucket is in the US East (N. Virginia) region, use us-east-1 to specify the region.
	 For
	 a list of other AWS Regions, go to [Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
	 *AWS General Reference*.
4. Compile the source code and store the compiled classes into the `bin/`
 directory.



```
javac -d bin -source 6 -verbose com
```
5. Change the directory to `bin/`, and then run 
 `RunAllSamples`.






```
java com.amazonaws.services.s3.sample.RunAllSamples
```

The code runs all the methods in `main()`. For each request, the output will
 show the canonical request, the string to sign, and the signature.


## Examples of Signature Calculations Using C# (AWS Signature Version 4)


 The C# sample that shows signature calculation can be downloaded at [https://docs.aws.amazon.com/AmazonS3/latest/API/samples/AmazonS3SigV4\_Samples\_CSharp.zip](samples/AmazonS3SigV4_Samples_CSharp.zip "samples/AmazonS3SigV4_Samples_CSharp.zip"). Note that these samples use AWS SDK for .NET v1, and we recommend using [AWS SDK for .NET v3](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/home.html "https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/home.html") for new applications.
 In `Program.cs`, the `main()` function executes sample requests to create an
 object, retrieve an object, and create a presigned URL for the object. The code for
 signature calculation is in the `\Signers` folder. 



```
PutS3ObjectSample.Run(awsRegion, bucketName, "MySampleFile.txt");

Console.WriteLine("\n\n************************************************");
PutS3ObjectChunkedSample.Run(awsRegion, bucketName, "MySampleFileChunked.txt");

Console.WriteLine("\n\n************************************************");
GetS3ObjectSample.Run(awsRegion, bucketName, "MySampleFile.txt");

Console.WriteLine("\n\n************************************************");
PresignedUrlSample.Run(awsRegion, bucketName, "MySampleFile.txt");
```


###### To test the examples with Microsoft Visual Studio 2010 or later


1. Extract the .zip file.
2. Start Visual Studio, and then open the .sln file.
3. Update the App.config file with valid security credentials.
4. Update the code as follows:







	* In `Program.cs`, provide the bucket name and 
	 the AWS Region where the bucket resides.
	 The sample creates an object in this bucket.
5. Run the code.
6. To verify that the object was created, copy the presigned URL that the
 program creates, and then paste it in a browser window.
