# Use `ListBuckets` with an AWS SDK or CLI

The following code examples show how to use `ListBuckets`.


.NET


**SDK for .NET**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples").
 



```
namespace ListBucketsExample
{
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    using Amazon.S3;
    using Amazon.S3.Model;

    /// <summary>
    /// This example uses the AWS SDK for .NET to list the Amazon Simple Storage
    /// Service (Amazon S3) buckets belonging to the default account.
    /// </summary>
    public class ListBuckets
    {
        private static IAmazonS3 _s3Client;

        /// <summary>
        /// Get a list of the buckets owned by the default user.
        /// </summary>
        /// <param name="client">An initialized Amazon S3 client object.</param>
        /// <returns>The response from the ListingBuckets call that contains a
        /// list of the buckets owned by the default user.</returns>
        public static async Task<ListBucketsResponse> GetBuckets(IAmazonS3 client)
        {
            return await client.ListBucketsAsync();
        }

        /// <summary>
        /// This method lists the name and creation date for the buckets in
        /// the passed List of S3 buckets.
        /// </summary>
        /// <param name="bucketList">A List of S3 bucket objects.</param>
        public static void DisplayBucketList(List<S3Bucket> bucketList)
        {
            bucketList
                .ForEach(b => Console.WriteLine($"Bucket name: {b.BucketName}, created on: {b.CreationDate}"));
        }

        public static async Task Main()
        {
            // The client uses the AWS Region of the default user.
            // If the Region where the buckets were created is different,
            // pass the Region to the client constructor. For example:
            // _s3Client = new AmazonS3Client(RegionEndpoint.USEast1);
            _s3Client = new AmazonS3Client();
            var response = await GetBuckets(_s3Client);
            DisplayBucketList(response.Buckets);
        }
    }
}



```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBuckets")
 in *AWS SDK for .NET API Reference*.




C++


**SDK for C++**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples").
 



```
bool AwsDoc::S3::listBuckets(const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);

    auto outcome = client.ListBuckets();

    bool result = true;
    if (!outcome.IsSuccess()) {
        std::cerr << "Failed with error: " << outcome.GetError() << std::endl;
        result = false;
    } else {
        std::cout << "Found " << outcome.GetResult().GetBuckets().size() << " buckets\n";
        for (auto &&b: outcome.GetResult().GetBuckets()) {
            std::cout << b.GetName() << std::endl;
        }
    }

    return result;
}


```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBuckets")
 in *AWS SDK for C++ API Reference*.




CLI


**AWS CLI**

The following command uses the `list-buckets` command to display the names of all your Amazon S3 buckets (across all
regions):



```
`aws s3api list-buckets --query `"Buckets[].Name"``

```

The query option filters the output of `list-buckets` down to only the bucket names.


For more information about buckets, see Working with Amazon S3 Buckets in the *Amazon S3 Developer Guide*.



* For API details, see
 [ListBuckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html")
 in *AWS CLI Command Reference*.




Go


**SDK for Go V2**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples").
 



```

import (
	"bytes"
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/aws/aws-sdk-go-v2/service/s3/types"
	"github.com/aws/smithy-go"
)

// BucketBasics encapsulates the Amazon Simple Storage Service (Amazon S3) actions
// used in the examples.
// It contains S3Client, an Amazon S3 service client that is used to perform bucket
// and object actions.
type BucketBasics struct {
	S3Client *s3.Client
}



// ListBuckets lists the buckets in the current account.
func (basics BucketBasics) ListBuckets(ctx context.Context) ([]types.Bucket, error) {
	var err error
	var output *s3.ListBucketsOutput
	var buckets []types.Bucket
	bucketPaginator := s3.NewListBucketsPaginator(basics.S3Client, &s3.ListBucketsInput{})
	for bucketPaginator.HasMorePages() {
		output, err = bucketPaginator.NextPage(ctx)
		if err != nil {
			var apiErr smithy.APIError
			if errors.As(err, &apiErr) && apiErr.ErrorCode() == "AccessDenied" {
				fmt.Println("You don't have permission to list buckets for this account.")
				err = apiErr
			} else {
				log.Printf("Couldn't list buckets for your account. Here's why: %v\n", err)
			}
			break
		} else {
			buckets = append(buckets, output.Buckets...)
		}
	}
	return buckets, err
}



```


* For API details, see
 [ListBuckets](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.ListBuckets "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.ListBuckets")
 in *AWS SDK for Go API Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 



```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.paginators.ListBucketsIterable;
/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class ListBuckets {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        S3Client s3 = S3Client.builder()
            .region(region)
            .build();

        listAllBuckets(s3);

    }

    /**
     * Lists all the S3 buckets available in the current AWS account.
     *
     * @param s3 The {@link S3Client} instance to use for interacting with the Amazon S3 service.
     */
    public static void listAllBuckets(S3Client s3) {
        ListBucketsIterable response = s3.listBucketsPaginator();
        response.buckets().forEach(bucket ->
            System.out.println("Bucket Name: " + bucket.name()));
    }


```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBuckets")
 in *AWS SDK for Java 2.x API Reference*.




JavaScript


**SDK for JavaScript (v3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples").
 


List the buckets.



```
import {
  paginateListBuckets,
  S3Client,
  S3ServiceException,
} from "@aws-sdk/client-s3";

/**
 * List the Amazon S3 buckets in your account.
 */
export const main = async () => {
  const client = new S3Client({});
  /** @type {?import('@aws-sdk/client-s3').Owner} */
  let Owner = null;

  /** @type {import('@aws-sdk/client-s3').Bucket[]} */
  const Buckets = [];

  try {
    const paginator = paginateListBuckets({ client }, {});

    for await (const page of paginator) {
      if (!Owner) {
        Owner = page.Owner;
      }

      Buckets.push(...page.Buckets);
    }

    console.log(
      `${Owner.DisplayName} owns ${Buckets.length} bucket${
        Buckets.length === 1 ? "" : "s"
      }:`,
    );
    console.log(`${Buckets.map((b) => ` • ${b.Name}`).join("\n")}`);
  } catch (caught) {
    if (caught instanceof S3ServiceException) {
      console.error(
        `Error from S3 while listing buckets.  ${caught.name}: ${caught.message}`,
      );
    } else {
      throw caught;
    }
  }
};


```


* For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-example-creating-buckets.html#s3-example-creating-buckets-list-buckets "https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-example-creating-buckets.html#s3-example-creating-buckets-list-buckets").
* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/ListBucketsCommand "https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/ListBucketsCommand")
 in *AWS SDK for JavaScript API Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns all S3 buckets.**



```
Get-S3Bucket

```

**Example 2: This command returns bucket named "test-files"**



```
Get-S3Bucket -BucketName amzn-s3-demo-bucket

```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns all S3 buckets.**



```
Get-S3Bucket

```

**Example 2: This command returns bucket named "test-files"**



```
Get-S3Bucket -BucketName amzn-s3-demo-bucket

```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




Python


**SDK for Python (Boto3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/s3_basics#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/s3_basics#code-examples").
 



```
class BucketWrapper:
    """Encapsulates S3 bucket actions."""

    def __init__(self, bucket):
        """
        :param bucket: A Boto3 Bucket resource. This is a high-level resource in Boto3
                       that wraps bucket actions in a class-like structure.
        """
        self.bucket = bucket
        self.name = bucket.name


    @staticmethod
    def list(s3_resource):
        """
        Get the buckets in all Regions for the current account.

        :param s3_resource: A Boto3 S3 resource. This is a high-level resource in Boto3
                            that contains collections and factory methods to create
                            other high-level S3 sub-resources.
        :return: The list of buckets.
        """
        try:
            buckets = list(s3_resource.buckets.all())
            logger.info("Got buckets: %s.", buckets)
        except ClientError:
            logger.exception("Couldn't get buckets.")
            raise
        else:
            return buckets



```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBuckets")
 in *AWS SDK for Python (Boto3) API Reference*.




Ruby


**SDK for Ruby**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/s3#code-examples").
 



```
require 'aws-sdk-s3'

# Wraps Amazon S3 resource actions.
class BucketListWrapper
  attr_reader :s3_resource

  # @param s3_resource [Aws::S3::Resource] An Amazon S3 resource.
  def initialize(s3_resource)
    @s3_resource = s3_resource
  end

  # Lists buckets for the current account.
  #
  # @param count [Integer] The maximum number of buckets to list.
  def list_buckets(count)
    puts 'Found these buckets:'
    @s3_resource.buckets.each do |bucket|
      puts "\t#{bucket.name}"
      count -= 1
      break if count.zero?
    end
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't list buckets. Here's why: #{e.message}"
    false
  end
end

# Example usage:
def run_demo
  wrapper = BucketListWrapper.new(Aws::S3::Resource.new)
  wrapper.list_buckets(25)
end

run_demo if $PROGRAM_NAME == __FILE__


```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBuckets")
 in *AWS SDK for Ruby API Reference*.




Rust


**SDK for Rust**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples").
 



```
async fn show_buckets(
    strict: bool,
    client: &Client,
    region: BucketLocationConstraint,
) -> Result<(), S3ExampleError> {
    let mut buckets = client.list_buckets().into_paginator().send();

    let mut num_buckets = 0;
    let mut in_region = 0;

    while let Some(Ok(output)) = buckets.next().await {
        for bucket in output.buckets() {
            num_buckets += 1;
            if strict {
                let r = client
                    .get_bucket_location()
                    .bucket(bucket.name().unwrap_or_default())
                    .send()
                    .await?;

                if r.location_constraint() == Some(&region) {
                    println!("{}", bucket.name().unwrap_or_default());
                    in_region += 1;
                }
            } else {
                println!("{}", bucket.name().unwrap_or_default());
            }
        }
    }

    println!();
    if strict {
        println!(
            "Found {} buckets in the {} region out of a total of {} buckets.",
            in_region, region, num_buckets
        );
    } else {
        println!("Found {} buckets in all regions.", num_buckets);
    }

    Ok(())
}


```


* For API details, see
 [ListBuckets](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.list_buckets "https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.list_buckets")
 in *AWS SDK for Rust API reference*.




Swift


**SDK for Swift**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/s3#code-examples").
 



```
import AWSS3

    /// Return an array containing information about every available bucket.
    ///
    /// - Returns: An array of ``S3ClientTypes.Bucket`` objects describing
    ///   each bucket.
    public func getAllBuckets() async throws -> [S3ClientTypes.Bucket] {
        return try await client.listBuckets(input: ListBucketsInput())
    }


```


* For API details, see
 [ListBuckets](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/listbuckets(input:) "https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/listbuckets(input:)")
 in *AWS SDK for Swift API reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
