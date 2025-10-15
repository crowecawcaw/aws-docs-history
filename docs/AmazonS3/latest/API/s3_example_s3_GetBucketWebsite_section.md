# Use `GetBucketWebsite` with an AWS SDK or CLI

The following code examples show how to use `GetBucketWebsite`.


.NET


**SDK for .NET**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples").
 



```
                // Get the website configuration.
                GetBucketWebsiteRequest getRequest = new GetBucketWebsiteRequest()
                {
                    BucketName = bucketName,
                };
                GetBucketWebsiteResponse getResponse = await client.GetBucketWebsiteAsync(getRequest);
                Console.WriteLine($"Index document: {getResponse.WebsiteConfiguration.IndexDocumentSuffix}");
                Console.WriteLine($"Error document: {getResponse.WebsiteConfiguration.ErrorDocument}");



```


* For API details, see
 [GetBucketWebsite](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketWebsite "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketWebsite")
 in *AWS SDK for .NET API Reference*.




C++


**SDK for C++**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples").
 



```
bool AwsDoc::S3::getWebsiteConfig(const Aws::String &bucketName,
                                  const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client s3Client(clientConfig);

    Aws::S3::Model::GetBucketWebsiteRequest request;
    request.SetBucket(bucketName);

    Aws::S3::Model::GetBucketWebsiteOutcome outcome =
            s3Client.GetBucketWebsite(request);

    if (!outcome.IsSuccess()) {
        const Aws::S3::S3Error &err = outcome.GetError();

        std::cerr << "Error: GetBucketWebsite: "
                  << err.GetMessage() << std::endl;
    } else {
        Aws::S3::Model::GetBucketWebsiteResult websiteResult = outcome.GetResult();

        std::cout << "Success: GetBucketWebsite: "
                  << std::endl << std::endl
                  << "For bucket '" << bucketName << "':"
                  << std::endl
                  << "Index page : "
                  << websiteResult.GetIndexDocument().GetSuffix()
                  << std::endl
                  << "Error page: "
                  << websiteResult.GetErrorDocument().GetKey()
                  << std::endl;
    }

    return outcome.IsSuccess();
}


```


* For API details, see
 [GetBucketWebsite](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketWebsite "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketWebsite")
 in *AWS SDK for C++ API Reference*.




CLI


**AWS CLI**

The following command retrieves the static website configuration for a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api get-bucket-website --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "IndexDocument": {
        "Suffix": "index.html"
    },
    "ErrorDocument": {
        "Key": "error.html"
    }
}
```


* For API details, see
 [GetBucketWebsite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-website.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-website.html")
 in *AWS CLI Command Reference*.




JavaScript


**SDK for JavaScript (v3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples").
 


Get the website configuration.



```
import {
  GetBucketWebsiteCommand,
  S3Client,
  S3ServiceException,
} from "@aws-sdk/client-s3";

/**
 * Log the website configuration for a bucket.
 * @param {{ bucketName }}
 */
export const main = async ({ bucketName }) => {
  const client = new S3Client({});

  try {
    const response = await client.send(
      new GetBucketWebsiteCommand({
        Bucket: bucketName,
      }),
    );
    console.log(
      `Your bucket is set up to host a website with the following configuration:\n${JSON.stringify(response, null, 2)}`,
    );
  } catch (caught) {
    if (
      caught instanceof S3ServiceException &&
      caught.name === "NoSuchWebsiteConfiguration"
    ) {
      console.error(
        `Error from S3 while getting website configuration for ${bucketName}. The bucket isn't configured as a website.`,
      );
    } else if (caught instanceof S3ServiceException) {
      console.error(
        `Error from S3 while getting website configuration for ${bucketName}.  ${caught.name}: ${caught.message}`,
      );
    } else {
      throw caught;
    }
  }
};


```


* For API details, see
 [GetBucketWebsite](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/GetBucketWebsiteCommand "https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/GetBucketWebsiteCommand")
 in *AWS SDK for JavaScript API Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the details of the static website configurations of the given S3 bucket.**



```
Get-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketWebsite](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the details of the static website configurations of the given S3 bucket.**



```
Get-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket'

```


* For API details, see
 [GetBucketWebsite](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
