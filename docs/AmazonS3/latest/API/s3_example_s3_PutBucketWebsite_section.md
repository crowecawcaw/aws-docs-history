# Use `PutBucketWebsite` with an AWS SDK or CLI

The following code examples show how to use `PutBucketWebsite`.


.NET


**SDK for .NET**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples").
 



```
                // Put the website configuration.
                PutBucketWebsiteRequest putRequest = new PutBucketWebsiteRequest()
                {
                    BucketName = bucketName,
                    WebsiteConfiguration = new WebsiteConfiguration()
                    {
                        IndexDocumentSuffix = indexDocumentSuffix,
                        ErrorDocument = errorDocument,
                    },
                };
                PutBucketWebsiteResponse response = await client.PutBucketWebsiteAsync(putRequest);



```


* For API details, see
 [PutBucketWebsite](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketWebsite")
 in *AWS SDK for .NET API Reference*.




C++


**SDK for C++**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples").
 



```
bool AwsDoc::S3::putWebsiteConfig(const Aws::String &bucketName,
                                  const Aws::String &indexPage, const Aws::String &errorPage,
                                  const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);

    Aws::S3::Model::IndexDocument indexDocument;
    indexDocument.SetSuffix(indexPage);

    Aws::S3::Model::ErrorDocument errorDocument;
    errorDocument.SetKey(errorPage);

    Aws::S3::Model::WebsiteConfiguration websiteConfiguration;
    websiteConfiguration.SetIndexDocument(indexDocument);
    websiteConfiguration.SetErrorDocument(errorDocument);

    Aws::S3::Model::PutBucketWebsiteRequest request;
    request.SetBucket(bucketName);
    request.SetWebsiteConfiguration(websiteConfiguration);

    Aws::S3::Model::PutBucketWebsiteOutcome outcome =
            client.PutBucketWebsite(request);

    if (!outcome.IsSuccess()) {
        std::cerr << "Error: PutBucketWebsite: "
                  << outcome.GetError().GetMessage() << std::endl;
    } else {
        std::cout << "Success: Set website configuration for bucket '"
                  << bucketName << "'." << std::endl;
    }

    return outcome.IsSuccess();
}


```


* For API details, see
 [PutBucketWebsite](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketWebsite")
 in *AWS SDK for C++ API Reference*.




CLI


**AWS CLI**

The applies a static website configuration to a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api put-bucket-website --bucket `amzn-s3-demo-bucket` --website-configuration `file://website.json``

```

The file `website.json` is a JSON document in the current folder that specifies index and error pages for the website:



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
 [PutBucketWebsite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-website.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-website.html")
 in *AWS CLI Command Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 



```

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.IndexDocument;
import software.amazon.awssdk.services.s3.model.PutBucketWebsiteRequest;
import software.amazon.awssdk.services.s3.model.WebsiteConfiguration;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.regions.Region;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 * <p>
 * For more information, see the following documentation topic:
 * <p>
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class SetWebsiteConfiguration {
    public static void main(String[] args) {
        final String usage = """

            Usage:    <bucketName> [indexdoc]\s

            Where:
               bucketName   - The Amazon S3 bucket to set the website configuration on.\s
               indexdoc - The index document, ex. 'index.html'
                          If not specified, 'index.html' will be set.
            """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String bucketName = args[0];
        String indexDoc = "index.html";
        Region region = Region.US_EAST_1;
        S3Client s3 = S3Client.builder()
            .region(region)
            .build();

        setWebsiteConfig(s3, bucketName, indexDoc);
        s3.close();
    }

    /**
     * Sets the website configuration for an Amazon S3 bucket.
     *
     * @param s3 The {@link S3Client} instance to use for the AWS SDK operations.
     * @param bucketName The name of the S3 bucket to configure.
     * @param indexDoc The name of the index document to use for the website configuration.
     */
    public static void setWebsiteConfig(S3Client s3, String bucketName, String indexDoc) {
        try {
            WebsiteConfiguration websiteConfig = WebsiteConfiguration.builder()
                .indexDocument(IndexDocument.builder().suffix(indexDoc).build())
                .build();

            PutBucketWebsiteRequest pubWebsiteReq = PutBucketWebsiteRequest.builder()
                .bucket(bucketName)
                .websiteConfiguration(websiteConfig)
                .build();

            s3.putBucketWebsite(pubWebsiteReq);
            System.out.println("The call was successful");

        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```


* For API details, see
 [PutBucketWebsite](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketWebsite")
 in *AWS SDK for Java 2.x API Reference*.




JavaScript


**SDK for JavaScript (v3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples").
 


Set the website configuration.



```
import {
  PutBucketWebsiteCommand,
  S3Client,
  S3ServiceException,
} from "@aws-sdk/client-s3";

/**
 * Configure an Amazon S3 bucket to serve a static website.
 * Website access must also be granted separately. For more information
 * on setting the permissions for website access, see
 * https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html.
 *
 * @param {{ bucketName: string }}
 */
export const main = async ({ bucketName }) => {
  const client = new S3Client({});
  const command = new PutBucketWebsiteCommand({
    Bucket: bucketName,
    WebsiteConfiguration: {
      ErrorDocument: {
        // The object key name to use when a 4XX class error occurs.
        Key: "error.html",
      },
      IndexDocument: {
        // A suffix that is appended to a request when the request is
        // for a directory.
        Suffix: "index.html",
      },
    },
  });

  try {
    await client.send(command);
    console.log(
      `The bucket "${bucketName}" has been configured as a static website.`,
    );
  } catch (caught) {
    if (
      caught instanceof S3ServiceException &&
      caught.name === "NoSuchBucket"
    ) {
      console.error(
        `Error from S3 while configuring the bucket "${bucketName}" as a static website. The bucket doesn't exist.`,
      );
    } else if (caught instanceof S3ServiceException) {
      console.error(
        `Error from S3 while configuring the bucket "${bucketName}" as a static website. ${caught.name}: ${caught.message}`,
      );
    } else {
      throw caught;
    }
  }
};


```


* For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-example-static-web-host.html#s3-example-static-web-host-set-website "https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-example-static-web-host.html#s3-example-static-web-host-set-website").
* For API details, see
 [PutBucketWebsite](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/PutBucketWebsiteCommand "https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/PutBucketWebsiteCommand")
 in *AWS SDK for JavaScript API Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: The command enables website hosting for the given bucket with the index document as 'index.html' and error document as 'error.html'.**



```
Write-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket' -WebsiteConfiguration_IndexDocumentSuffix 'index.html' -WebsiteConfiguration_ErrorDocument 'error.html'

```


* For API details, see
 [PutBucketWebsite](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: The command enables website hosting for the given bucket with the index document as 'index.html' and error document as 'error.html'.**



```
Write-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket' -WebsiteConfiguration_IndexDocumentSuffix 'index.html' -WebsiteConfiguration_ErrorDocument 'error.html'

```


* For API details, see
 [PutBucketWebsite](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




Ruby


**SDK for Ruby**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/s3#code-examples").
 



```
require 'aws-sdk-s3'

# Wraps Amazon S3 bucket website actions.
class BucketWebsiteWrapper
  attr_reader :bucket_website

  # @param bucket_website [Aws::S3::BucketWebsite] A bucket website object configured with an existing bucket.
  def initialize(bucket_website)
    @bucket_website = bucket_website
  end

  # Sets a bucket as a static website.
  #
  # @param index_document [String] The name of the index document for the website.
  # @param error_document [String] The name of the error document to show for 4XX errors.
  # @return [Boolean] True when the bucket is configured as a website; otherwise, false.
  def set_website(index_document, error_document)
    @bucket_website.put(
      website_configuration: {
        index_document: { suffix: index_document },
        error_document: { key: error_document }
      }
    )
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't configure #{@bucket_website.bucket.name} as a website. Here's why: #{e.message}"
    false
  end
end

# Example usage:
def run_demo
  bucket_name = "amzn-s3-demo-bucket"
  index_document = "index.html"
  error_document = "404.html"

  wrapper = BucketWebsiteWrapper.new(Aws::S3::BucketWebsite.new(bucket_name))
  return unless wrapper.set_website(index_document, error_document)

  puts "Successfully configured bucket #{bucket_name} as a static website."
end

run_demo if $PROGRAM_NAME == __FILE__


```


* For API details, see
 [PutBucketWebsite](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketWebsite")
 in *AWS SDK for Ruby API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
