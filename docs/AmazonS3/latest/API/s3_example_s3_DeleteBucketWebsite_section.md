# Use `DeleteBucketWebsite` with an AWS SDK or CLI

The following code examples show how to use `DeleteBucketWebsite`.


C++


**SDK for C++**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples").
 



```
bool AwsDoc::S3::deleteBucketWebsite(const Aws::String &bucketName,
                                     const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);
    Aws::S3::Model::DeleteBucketWebsiteRequest request;
    request.SetBucket(bucketName);

    Aws::S3::Model::DeleteBucketWebsiteOutcome outcome =
            client.DeleteBucketWebsite(request);

    if (!outcome.IsSuccess()) {
        auto err = outcome.GetError();
        std::cerr << "Error: deleteBucketWebsite: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "Website configuration was removed." << std::endl;
    }

    return outcome.IsSuccess();
}


```


* For API details, see
 [DeleteBucketWebsite](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketWebsite")
 in *AWS SDK for C++ API Reference*.




CLI


**AWS CLI**

The following command deletes a website configuration from a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api delete-bucket-website --bucket `amzn-s3-demo-bucket``

```


* For API details, see
 [DeleteBucketWebsite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-website.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-website.html")
 in *AWS CLI Command Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 



```

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.DeleteBucketWebsiteRequest;
import software.amazon.awssdk.services.s3.model.S3Exception;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 * <p>
 * For more information, see the following documentation topic:
 * <p>
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class DeleteWebsiteConfiguration {
    public static void main(String[] args) {
        final String usage = """

            Usage:     <bucketName>

            Where:
                bucketName - The Amazon S3 bucket to delete the website configuration from.
            """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String bucketName = args[0];
        System.out.format("Deleting website configuration for Amazon S3 bucket: %s\n", bucketName);
        Region region = Region.US_EAST_1;
        S3Client s3 = S3Client.builder()
            .region(region)
            .build();

        deleteBucketWebsiteConfig(s3, bucketName);
        System.out.println("Done!");
        s3.close();
    }

    /**
     * Deletes the website configuration for an Amazon S3 bucket.
     *
     * @param s3 The {@link S3Client} instance used to interact with Amazon S3.
     * @param bucketName The name of the S3 bucket for which the website configuration should be deleted.
     * @throws S3Exception If an error occurs while deleting the website configuration.
     */
    public static void deleteBucketWebsiteConfig(S3Client s3, String bucketName) {
        DeleteBucketWebsiteRequest delReq = DeleteBucketWebsiteRequest.builder()
            .bucket(bucketName)
            .build();

        try {
            s3.deleteBucketWebsite(delReq);

        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.out.println("Failed to delete website configuration!");
            System.exit(1);
        }
    }
}


```


* For API details, see
 [DeleteBucketWebsite](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketWebsite")
 in *AWS SDK for Java 2.x API Reference*.




JavaScript


**SDK for JavaScript (v3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples").
 


Delete the website configuration from the bucket.



```
import {
  DeleteBucketWebsiteCommand,
  S3Client,
  S3ServiceException,
} from "@aws-sdk/client-s3";

/**
 * Remove the website configuration for a bucket.
 * @param {{ bucketName: string }}
 */
export const main = async ({ bucketName }) => {
  const client = new S3Client({});

  try {
    await client.send(
      new DeleteBucketWebsiteCommand({
        Bucket: bucketName,
      }),
    );
    // The response code will be successful for both removed configurations and
    // configurations that did not exist in the first place.
    console.log(
      `The bucket "${bucketName}" is not longer configured as a website, or it never was.`,
    );
  } catch (caught) {
    if (
      caught instanceof S3ServiceException &&
      caught.name === "NoSuchBucket"
    ) {
      console.error(
        `Error from S3 while removing website configuration from ${bucketName}. The bucket doesn't exist.`,
      );
    } else if (caught instanceof S3ServiceException) {
      console.error(
        `Error from S3 while removing website configuration from ${bucketName}.  ${caught.name}: ${caught.message}`,
      );
    } else {
      throw caught;
    }
  }
};


```


* For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-example-static-web-host.html#s3-example-static-web-host-delete-website "https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-example-static-web-host.html#s3-example-static-web-host-delete-website").
* For API details, see
 [DeleteBucketWebsite](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/DeleteBucketWebsiteCommand "https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/DeleteBucketWebsiteCommand")
 in *AWS SDK for JavaScript API Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command disables the static website hosting property of the given S3 bucket.**



```
Remove-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketWebsite (DeleteBucketWebsite)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```


* For API details, see
 [DeleteBucketWebsite](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command disables the static website hosting property of the given S3 bucket.**



```
Remove-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketWebsite (DeleteBucketWebsite)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```


* For API details, see
 [DeleteBucketWebsite](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
