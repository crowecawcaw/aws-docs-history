# Code examples for Amazon S3 using AWS SDKs

The following code examples show how to use Amazon S3 with an AWS software development kit (SDK).
 

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.

**Get started**


The following code examples show how to get started using Amazon S3.


C++


**SDK for C++**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/hello_s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/hello_s3#code-examples").
 


Code for the CMakeLists.txt CMake file.



```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS s3)

# Set this project's name.
project("hello_s3")

# Set the C++ standard to use to build this target.
# At least C++ 11 is required for the AWS SDK for C++.
set(CMAKE_CXX_STANDARD 11)

# Use the MSVC variable to determine if this is a Windows build.
set(WINDOWS_BUILD ${MSVC})

if (WINDOWS_BUILD) # Set the location where CMake can find the installed libraries for the AWS SDK.
    string(REPLACE ";" "/aws-cpp-sdk-all;" SYSTEM_MODULE_PATH "${CMAKE_SYSTEM_PREFIX_PATH}/aws-cpp-sdk-all")
    list(APPEND CMAKE_PREFIX_PATH ${SYSTEM_MODULE_PATH})
endif ()

# Find the AWS SDK for C++ package.
find_package(AWSSDK REQUIRED COMPONENTS ${SERVICE_COMPONENTS})

if (WINDOWS_BUILD AND AWSSDK_INSTALL_AS_SHARED_LIBS)
    # Copy relevant AWS SDK for C++ libraries into the current binary directory for running and debugging.

    # set(BIN_SUB_DIR "/Debug") # if you are building from the command line you may need to uncomment this
    # and set the proper subdirectory to the executables' location.

    AWSSDK_CPY_DYN_LIBS(SERVICE_COMPONENTS "" ${CMAKE_CURRENT_BINARY_DIR}${BIN_SUB_DIR})
endif ()

add_executable(${PROJECT_NAME}
        hello_s3.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello\_s3.cpp source file.



```
#include <aws/core/Aws.h>
#include <aws/s3/S3Client.h>
#include <iostream>
#include <aws/core/auth/AWSCredentialsProviderChain.h>
using namespace Aws;
using namespace Aws::Auth;

/*
 *  A "Hello S3" starter application which initializes an Amazon Simple Storage Service (Amazon S3) client
 *  and lists the Amazon S3 buckets in the selected region.
 *
 *  main function
 *
 *  Usage: 'hello_s3'
 *
 */

int main(int argc, char **argv) {
    Aws::SDKOptions options;
    // Optionally change the log level for debugging.
//   options.loggingOptions.logLevel = Utils::Logging::LogLevel::Debug;
    Aws::InitAPI(options); // Should only be called once.
    int result = 0;
    {
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";
               
        // You don't normally have to test that you are authenticated. But the S3 service permits anonymous requests, thus the s3Client will return "success" and 0 buckets even if you are unauthenticated, which can be confusing to a new user. 
        auto provider = Aws::MakeShared<DefaultAWSCredentialsProviderChain>("alloc-tag");
        auto creds = provider->GetAWSCredentials();
        if (creds.IsEmpty()) {
            std::cerr << "Failed authentication" << std::endl;
        }

        Aws::S3::S3Client s3Client(clientConfig);
        auto outcome = s3Client.ListBuckets();

        if (!outcome.IsSuccess()) {
            std::cerr << "Failed with error: " << outcome.GetError() << std::endl;
            result = 1;
        } else {
            std::cout << "Found " << outcome.GetResult().GetBuckets().size()
                      << " buckets\n";
            for (auto &bucket: outcome.GetResult().GetBuckets()) {
                std::cout << bucket.GetName() << std::endl;
            }
        }
    }

    Aws::ShutdownAPI(options); // Should only be called once.
    return result;
}


```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBuckets")
 in *AWS SDK for C++ API Reference*.




Go


**SDK for Go V2**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples").
 



```

package main

import (
	"context"
	"errors"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/aws/smithy-go"
)

// main uses the AWS SDK for Go V2 to create an Amazon Simple Storage Service
// (Amazon S3) client and list up to 10 buckets in your account.
// This example uses the default settings specified in your shared credentials
// and config files.
func main() {
	ctx := context.Background()
	sdkConfig, err := config.LoadDefaultConfig(ctx)
	if err != nil {
		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
		fmt.Println(err)
		return
	}
	s3Client := s3.NewFromConfig(sdkConfig)
	count := 10
	fmt.Printf("Let's list up to %v buckets for your account.\n", count)
	result, err := s3Client.ListBuckets(ctx, &s3.ListBucketsInput{})
	if err != nil {
		var ae smithy.APIError
		if errors.As(err, &ae) && ae.ErrorCode() == "AccessDenied" {
			fmt.Println("You don't have permission to list buckets for this account.")
		} else {
			fmt.Printf("Couldn't list buckets for your account. Here's why: %v\n", err)
		}
		return
	}
	if len(result.Buckets) == 0 {
		fmt.Println("You don't have any buckets!")
	} else {
		if count > len(result.Buckets) {
			count = len(result.Buckets)
		}
		for _, bucket := range result.Buckets[:count] {
			fmt.Printf("\t%v\n", *bucket.Name)
		}
	}
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
import software.amazon.awssdk.services.s3.model.Bucket;
import software.amazon.awssdk.services.s3.model.ListBucketsResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 * <p>
 * For more information, see the following documentation topic:
 * <p>
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloS3 {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        S3Client s3 = S3Client.builder()
            .region(region)
            .build();

        listBuckets(s3);
    }

    /**
     * Lists all the S3 buckets associated with the provided AWS S3 client.
     *
     * @param s3 the S3Client instance used to interact with the AWS S3 service
     */
    public static void listBuckets(S3Client s3) {
        try {
            ListBucketsResponse response = s3.listBuckets();
            List<Bucket> bucketList = response.buckets();
            bucketList.forEach(bucket -> {
                System.out.println("Bucket Name: " + bucket.name());
            });

        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
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
 



```
import {
  paginateListBuckets,
  S3Client,
  S3ServiceException,
} from "@aws-sdk/client-s3";

/**
 * List the S3 buckets in your configured AWS account.
 */
export const helloS3 = async () => {
  // When no region or credentials are provided, the SDK will use the
  // region and credentials from the local AWS config.
  const client = new S3Client({});

  try {
    /**
     * @type { import("@aws-sdk/client-s3").Bucket[] }
     */
    const buckets = [];

    for await (const page of paginateListBuckets({ client }, {})) {
      buckets.push(...page.Buckets);
    }
    console.log("Buckets: ");
    console.log(buckets.map((bucket) => bucket.Name).join("\n"));
    return buckets;
  } catch (caught) {
    // ListBuckets does not throw any modeled errors. Any error caught
    // here will be something generic like `AccessDenied`.
    if (caught instanceof S3ServiceException) {
      console.error(`${caught.name}: ${caught.message}`);
    } else {
      // Something besides S3 failed.
      throw caught;
    }
  }
};


```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/ListBucketsCommand "https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/ListBucketsCommand")
 in *AWS SDK for JavaScript API Reference*.




PHP


**SDK for PHP**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/s3#code-examples").
 



```
use Aws\S3\S3Client;

$client = new S3Client(['region' => 'us-west-2']);
$results = $client->listBuckets();
var_dump($results);


```


* For API details, see
 [ListBuckets](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBuckets")
 in *AWS SDK for PHP API Reference*.




Python


**SDK for Python (Boto3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3#code-examples").
 



```
import boto3


def hello_s3():
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service
    (Amazon S3) client and list the buckets in your account.
    This example uses the default settings specified in your shared credentials
    and config files.
    """

    # Create an S3 client.
    s3_client = boto3.client("s3")

    print("Hello, Amazon S3! Let's list your buckets:")

    # Create a paginator for the list_buckets operation.
    paginator = s3_client.get_paginator("list_buckets")

    # Use the paginator to get a list of all buckets.
    response_iterator = paginator.paginate(
        PaginationConfig={
            "PageSize": 50,  # Adjust PageSize as needed.
            "StartingToken": None,
        }
    )

    # Iterate through the pages of the response.
    buckets_found = False
    for page in response_iterator:
        if "Buckets" in page and page["Buckets"]:
            buckets_found = True
            for bucket in page["Buckets"]:
                print(f"\t{bucket['Name']}")

    if not buckets_found:
        print("No buckets found!")


if __name__ == "__main__":
    hello_s3()


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

# frozen_string_literal: true

# S3Manager is a class responsible for managing S3 operations
# such as listing all S3 buckets in the current AWS account.
class S3Manager
  def initialize(client)
    @client = client
    @logger = Logger.new($stdout)
  end

  # Lists and prints all S3 buckets in the current AWS account.
  def list_buckets
    @logger.info('Here are the buckets in your account:')

    response = @client.list_buckets

    if response.buckets.empty?
      @logger.info("You don't have any S3 buckets yet.")
    else
      response.buckets.each do |bucket|
        @logger.info("- #{bucket.name}")
      end
    end
  rescue Aws::Errors::ServiceError => e
    @logger.error("Encountered an error while listing buckets: #{e.message}")
  end
end

if $PROGRAM_NAME == __FILE__
  s3_client = Aws::S3::Client.new
  manager = S3Manager.new(s3_client)
  manager.list_buckets
end



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
/// S3 Hello World Example using the AWS SDK for Rust.
///
/// This example lists the objects in a bucket, uploads an object to that bucket,
/// and then retrieves the object and prints some S3 information about the object.
/// This shows a number of S3 features, including how to use built-in paginators
/// for large data sets.
///
/// # Arguments
///
/// * `client` - an S3 client configured appropriately for the environment.
/// * `bucket` - the bucket name that the object will be uploaded to. Must be present in the region the `client` is configured to use.
/// * `filename` - a reference to a path that will be read and uploaded to S3.
/// * `key` - the string key that the object will be uploaded as inside the bucket.
async fn list_bucket_and_upload_object(
    client: &aws_sdk_s3::Client,
    bucket: &str,
    filepath: &Path,
    key: &str,
) -> Result<(), S3ExampleError> {
    // List the buckets in this account
    let mut objects = client
        .list_objects_v2()
        .bucket(bucket)
        .into_paginator()
        .send();

    println!("key\tetag\tlast_modified\tstorage_class");
    while let Some(Ok(object)) = objects.next().await {
        for item in object.contents() {
            println!(
                "{}\t{}\t{}\t{}",
                item.key().unwrap_or_default(),
                item.e_tag().unwrap_or_default(),
                item.last_modified()
                    .map(|lm| format!("{lm}"))
                    .unwrap_or_default(),
                item.storage_class()
                    .map(|sc| format!("{sc}"))
                    .unwrap_or_default()
            );
        }
    }

    // Prepare a ByteStream around the file, and upload the object using that ByteStream.
    let body = aws_sdk_s3::primitives::ByteStream::from_path(filepath)
        .await
        .map_err(|err| {
            S3ExampleError::new(format!(
                "Failed to create bytestream for {filepath:?} ({err:?})"
            ))
        })?;
    let resp = client
        .put_object()
        .bucket(bucket)
        .key(key)
        .body(body)
        .send()
        .await?;

    println!(
        "Upload success. Version: {:?}",
        resp.version_id()
            .expect("S3 Object upload missing version ID")
    );

    // Retrieve the just-uploaded object.
    let resp = client.get_object().bucket(bucket).key(key).send().await?;
    println!("etag: {}", resp.e_tag().unwrap_or("(missing)"));
    println!("version: {}", resp.version_id().unwrap_or("(missing)"));

    Ok(())
}


```

S3ExampleError utilities.



```
/// S3ExampleError provides a From<T: ProvideErrorMetadata> impl to extract
/// client-specific error details. This serves as a consistent backup to handling
/// specific service errors, depending on what is needed by the scenario.
/// It is used throughout the code examples for the AWS SDK for Rust.
#[derive(Debug)]
pub struct S3ExampleError(String);
impl S3ExampleError {
    pub fn new(value: impl Into<String>) -> Self {
        S3ExampleError(value.into())
    }

    pub fn add_message(self, message: impl Into<String>) -> Self {
        S3ExampleError(format!("{}: {}", message.into(), self.0))
    }
}

impl<T: aws_sdk_s3::error::ProvideErrorMetadata> From<T> for S3ExampleError {
    fn from(value: T) -> Self {
        S3ExampleError(format!(
            "{}: {}",
            value
                .code()
                .map(String::from)
                .unwrap_or("unknown code".into()),
            value
                .message()
                .map(String::from)
                .unwrap_or("missing reason".into()),
        ))
    }
}

impl std::error::Error for S3ExampleError {}

impl std::fmt::Display for S3ExampleError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}


```


* For API details, see
 [ListBuckets](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.list_buckets "https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.list_buckets")
 in *AWS SDK for Rust API reference*.





###### Code examples

* [Basics](service_code_examples_s3_basics.md "service_code_examples_s3_basics.md")


	+ [Hello Amazon S3](s3_example_s3_Hello_section.md "s3_example_s3_Hello_section.md")
	+ [Learn the basics](s3_example_s3_Scenario_GettingStarted_section.md "s3_example_s3_Scenario_GettingStarted_section.md")
	+ [Actions](service_code_examples_s3_actions.md "service_code_examples_s3_actions.md")
	
	
		- [AbortMultipartUpload](s3_example_s3_AbortMultipartUpload_section.md "s3_example_s3_AbortMultipartUpload_section.md")
		- [CompleteMultipartUpload](s3_example_s3_CompleteMultipartUpload_section.md "s3_example_s3_CompleteMultipartUpload_section.md")
		- [CopyObject](s3_example_s3_CopyObject_section.md "s3_example_s3_CopyObject_section.md")
		- [CreateBucket](s3_example_s3_CreateBucket_section.md "s3_example_s3_CreateBucket_section.md")
		- [CreateMultiRegionAccessPoint](s3_example_s3_CreateMultiRegionAccessPoint_section.md "s3_example_s3_CreateMultiRegionAccessPoint_section.md")
		- [CreateMultipartUpload](s3_example_s3_CreateMultipartUpload_section.md "s3_example_s3_CreateMultipartUpload_section.md")
		- [CreatePresignedPost](s3_example_s3_CreatePresignedPost_section.md "s3_example_s3_CreatePresignedPost_section.md")
		- [DeleteBucket](s3_example_s3_DeleteBucket_section.md "s3_example_s3_DeleteBucket_section.md")
		- [DeleteBucketAnalyticsConfiguration](s3_example_s3_DeleteBucketAnalyticsConfiguration_section.md "s3_example_s3_DeleteBucketAnalyticsConfiguration_section.md")
		- [DeleteBucketCors](s3_example_s3_DeleteBucketCors_section.md "s3_example_s3_DeleteBucketCors_section.md")
		- [DeleteBucketEncryption](s3_example_s3_DeleteBucketEncryption_section.md "s3_example_s3_DeleteBucketEncryption_section.md")
		- [DeleteBucketInventoryConfiguration](s3_example_s3_DeleteBucketInventoryConfiguration_section.md "s3_example_s3_DeleteBucketInventoryConfiguration_section.md")
		- [DeleteBucketLifecycle](s3_example_s3_DeleteBucketLifecycle_section.md "s3_example_s3_DeleteBucketLifecycle_section.md")
		- [DeleteBucketMetricsConfiguration](s3_example_s3_DeleteBucketMetricsConfiguration_section.md "s3_example_s3_DeleteBucketMetricsConfiguration_section.md")
		- [DeleteBucketPolicy](s3_example_s3_DeleteBucketPolicy_section.md "s3_example_s3_DeleteBucketPolicy_section.md")
		- [DeleteBucketReplication](s3_example_s3_DeleteBucketReplication_section.md "s3_example_s3_DeleteBucketReplication_section.md")
		- [DeleteBucketTagging](s3_example_s3_DeleteBucketTagging_section.md "s3_example_s3_DeleteBucketTagging_section.md")
		- [DeleteBucketWebsite](s3_example_s3_DeleteBucketWebsite_section.md "s3_example_s3_DeleteBucketWebsite_section.md")
		- [DeleteObject](s3_example_s3_DeleteObject_section.md "s3_example_s3_DeleteObject_section.md")
		- [DeleteObjectTagging](s3_example_s3_DeleteObjectTagging_section.md "s3_example_s3_DeleteObjectTagging_section.md")
		- [DeleteObjects](s3_example_s3_DeleteObjects_section.md "s3_example_s3_DeleteObjects_section.md")
		- [DeletePublicAccessBlock](s3_example_s3_DeletePublicAccessBlock_section.md "s3_example_s3_DeletePublicAccessBlock_section.md")
		- [GetBucketAccelerateConfiguration](s3_example_s3_GetBucketAccelerateConfiguration_section.md "s3_example_s3_GetBucketAccelerateConfiguration_section.md")
		- [GetBucketAcl](s3_example_s3_GetBucketAcl_section.md "s3_example_s3_GetBucketAcl_section.md")
		- [GetBucketAnalyticsConfiguration](s3_example_s3_GetBucketAnalyticsConfiguration_section.md "s3_example_s3_GetBucketAnalyticsConfiguration_section.md")
		- [GetBucketCors](s3_example_s3_GetBucketCors_section.md "s3_example_s3_GetBucketCors_section.md")
		- [GetBucketEncryption](s3_example_s3_GetBucketEncryption_section.md "s3_example_s3_GetBucketEncryption_section.md")
		- [GetBucketInventoryConfiguration](s3_example_s3_GetBucketInventoryConfiguration_section.md "s3_example_s3_GetBucketInventoryConfiguration_section.md")
		- [GetBucketLifecycleConfiguration](s3_example_s3_GetBucketLifecycleConfiguration_section.md "s3_example_s3_GetBucketLifecycleConfiguration_section.md")
		- [GetBucketLocation](s3_example_s3_GetBucketLocation_section.md "s3_example_s3_GetBucketLocation_section.md")
		- [GetBucketLogging](s3_example_s3_GetBucketLogging_section.md "s3_example_s3_GetBucketLogging_section.md")
		- [GetBucketMetricsConfiguration](s3_example_s3_GetBucketMetricsConfiguration_section.md "s3_example_s3_GetBucketMetricsConfiguration_section.md")
		- [GetBucketNotification](s3_example_s3_GetBucketNotification_section.md "s3_example_s3_GetBucketNotification_section.md")
		- [GetBucketPolicy](s3_example_s3_GetBucketPolicy_section.md "s3_example_s3_GetBucketPolicy_section.md")
		- [GetBucketPolicyStatus](s3_example_s3_GetBucketPolicyStatus_section.md "s3_example_s3_GetBucketPolicyStatus_section.md")
		- [GetBucketReplication](s3_example_s3_GetBucketReplication_section.md "s3_example_s3_GetBucketReplication_section.md")
		- [GetBucketRequestPayment](s3_example_s3_GetBucketRequestPayment_section.md "s3_example_s3_GetBucketRequestPayment_section.md")
		- [GetBucketTagging](s3_example_s3_GetBucketTagging_section.md "s3_example_s3_GetBucketTagging_section.md")
		- [GetBucketVersioning](s3_example_s3_GetBucketVersioning_section.md "s3_example_s3_GetBucketVersioning_section.md")
		- [GetBucketWebsite](s3_example_s3_GetBucketWebsite_section.md "s3_example_s3_GetBucketWebsite_section.md")
		- [GetObject](s3_example_s3_GetObject_section.md "s3_example_s3_GetObject_section.md")
		- [GetObjectAcl](s3_example_s3_GetObjectAcl_section.md "s3_example_s3_GetObjectAcl_section.md")
		- [GetObjectAttributes](s3_example_s3_GetObjectAttributes_section.md "s3_example_s3_GetObjectAttributes_section.md")
		- [GetObjectLegalHold](s3_example_s3_GetObjectLegalHold_section.md "s3_example_s3_GetObjectLegalHold_section.md")
		- [GetObjectLockConfiguration](s3_example_s3_GetObjectLockConfiguration_section.md "s3_example_s3_GetObjectLockConfiguration_section.md")
		- [GetObjectRetention](s3_example_s3_GetObjectRetention_section.md "s3_example_s3_GetObjectRetention_section.md")
		- [GetObjectTagging](s3_example_s3_GetObjectTagging_section.md "s3_example_s3_GetObjectTagging_section.md")
		- [GetPublicAccessBlock](s3_example_s3_GetPublicAccessBlock_section.md "s3_example_s3_GetPublicAccessBlock_section.md")
		- [HeadBucket](s3_example_s3_HeadBucket_section.md "s3_example_s3_HeadBucket_section.md")
		- [HeadObject](s3_example_s3_HeadObject_section.md "s3_example_s3_HeadObject_section.md")
		- [ListBucketAnalyticsConfigurations](s3_example_s3_ListBucketAnalyticsConfigurations_section.md "s3_example_s3_ListBucketAnalyticsConfigurations_section.md")
		- [ListBucketInventoryConfigurations](s3_example_s3_ListBucketInventoryConfigurations_section.md "s3_example_s3_ListBucketInventoryConfigurations_section.md")
		- [ListBuckets](s3_example_s3_ListBuckets_section.md "s3_example_s3_ListBuckets_section.md")
		- [ListMultipartUploads](s3_example_s3_ListMultipartUploads_section.md "s3_example_s3_ListMultipartUploads_section.md")
		- [ListObjectVersions](s3_example_s3_ListObjectVersions_section.md "s3_example_s3_ListObjectVersions_section.md")
		- [ListObjects](s3_example_s3_ListObjects_section.md "s3_example_s3_ListObjects_section.md")
		- [ListObjectsV2](s3_example_s3_ListObjectsV2_section.md "s3_example_s3_ListObjectsV2_section.md")
		- [PutBucketAccelerateConfiguration](s3_example_s3_PutBucketAccelerateConfiguration_section.md "s3_example_s3_PutBucketAccelerateConfiguration_section.md")
		- [PutBucketAcl](s3_example_s3_PutBucketAcl_section.md "s3_example_s3_PutBucketAcl_section.md")
		- [PutBucketCors](s3_example_s3_PutBucketCors_section.md "s3_example_s3_PutBucketCors_section.md")
		- [PutBucketEncryption](s3_example_s3_PutBucketEncryption_section.md "s3_example_s3_PutBucketEncryption_section.md")
		- [PutBucketLifecycleConfiguration](s3_example_s3_PutBucketLifecycleConfiguration_section.md "s3_example_s3_PutBucketLifecycleConfiguration_section.md")
		- [PutBucketLogging](s3_example_s3_PutBucketLogging_section.md "s3_example_s3_PutBucketLogging_section.md")
		- [PutBucketNotification](s3_example_s3_PutBucketNotification_section.md "s3_example_s3_PutBucketNotification_section.md")
		- [PutBucketNotificationConfiguration](s3_example_s3_PutBucketNotificationConfiguration_section.md "s3_example_s3_PutBucketNotificationConfiguration_section.md")
		- [PutBucketPolicy](s3_example_s3_PutBucketPolicy_section.md "s3_example_s3_PutBucketPolicy_section.md")
		- [PutBucketReplication](s3_example_s3_PutBucketReplication_section.md "s3_example_s3_PutBucketReplication_section.md")
		- [PutBucketRequestPayment](s3_example_s3_PutBucketRequestPayment_section.md "s3_example_s3_PutBucketRequestPayment_section.md")
		- [PutBucketTagging](s3_example_s3_PutBucketTagging_section.md "s3_example_s3_PutBucketTagging_section.md")
		- [PutBucketVersioning](s3_example_s3_PutBucketVersioning_section.md "s3_example_s3_PutBucketVersioning_section.md")
		- [PutBucketWebsite](s3_example_s3_PutBucketWebsite_section.md "s3_example_s3_PutBucketWebsite_section.md")
		- [PutObject](s3_example_s3_PutObject_section.md "s3_example_s3_PutObject_section.md")
		- [PutObjectAcl](s3_example_s3_PutObjectAcl_section.md "s3_example_s3_PutObjectAcl_section.md")
		- [PutObjectLegalHold](s3_example_s3_PutObjectLegalHold_section.md "s3_example_s3_PutObjectLegalHold_section.md")
		- [PutObjectLockConfiguration](s3_example_s3_PutObjectLockConfiguration_section.md "s3_example_s3_PutObjectLockConfiguration_section.md")
		- [PutObjectRetention](s3_example_s3_PutObjectRetention_section.md "s3_example_s3_PutObjectRetention_section.md")
		- [RestoreObject](s3_example_s3_RestoreObject_section.md "s3_example_s3_RestoreObject_section.md")
		- [SelectObjectContent](s3_example_s3_SelectObjectContent_section.md "s3_example_s3_SelectObjectContent_section.md")
		- [UploadPart](s3_example_s3_UploadPart_section.md "s3_example_s3_UploadPart_section.md")
		- [UploadPartCopy](s3_example_s3_UploadPartCopy_section.md "s3_example_s3_UploadPartCopy_section.md")
* [Scenarios](service_code_examples_s3_scenarios.md "service_code_examples_s3_scenarios.md")


	+ [Check if a bucket exists](s3_example_s3_Scenario_DoesBucketExist_section.md "s3_example_s3_Scenario_DoesBucketExist_section.md")
	+ [Convert text to speech and back to text](s3_example_cross_Telephone_section.md "s3_example_cross_Telephone_section.md")
	+ [Create a presigned URL](s3_example_s3_Scenario_PresignedUrl_section.md "s3_example_s3_Scenario_PresignedUrl_section.md")
	+ [Create a serverless application to manage photos](s3_example_cross_PAM_section.md "s3_example_cross_PAM_section.md")
	+ [Create a web page that lists Amazon S3 objects](s3_example_s3_Scenario_ListObjectsWeb_section.md "s3_example_s3_Scenario_ListObjectsWeb_section.md")
	+ [Create an Amazon Textract explorer application](s3_example_cross_TextractExplorer_section.md "s3_example_cross_TextractExplorer_section.md")
	+ [Delete all objects in a bucket](s3_example_s3_Scenario_DeleteAllObjects_section.md "s3_example_s3_Scenario_DeleteAllObjects_section.md")
	+ [Delete incomplete multipart uploads](s3_example_s3_Scenario_AbortMultipartUpload_section.md "s3_example_s3_Scenario_AbortMultipartUpload_section.md")
	+ [Detect PPE in images](s3_example_cross_RekognitionPhotoAnalyzerPPE_section.md "s3_example_cross_RekognitionPhotoAnalyzerPPE_section.md")
	+ [Detect entities in text extracted from an image](s3_example_cross_TextractComprehendDetectEntities_section.md "s3_example_cross_TextractComprehendDetectEntities_section.md")
	+ [Detect faces in an image](s3_example_cross_DetectFaces_section.md "s3_example_cross_DetectFaces_section.md")
	+ [Detect objects in images](s3_example_cross_RekognitionPhotoAnalyzer_section.md "s3_example_cross_RekognitionPhotoAnalyzer_section.md")
	+ [Detect people and objects in a video](s3_example_cross_RekognitionVideoDetection_section.md "s3_example_cross_RekognitionVideoDetection_section.md")
	+ [Download S3 'directories'](s3_example_s3_Scenario_DownloadS3Directory_section.md "s3_example_s3_Scenario_DownloadS3Directory_section.md")
	+ [Download objects to a local directory](s3_example_s3_DownloadBucketToDirectory_section.md "s3_example_s3_DownloadBucketToDirectory_section.md")
	+ [Download stream of unknown size](s3_example_s3_Scenario_DownloadStream_section.md "s3_example_s3_Scenario_DownloadStream_section.md")
	+ [Get an object from a Multi-Region Access Point](s3_example_s3_GetObject_MRAP_section.md "s3_example_s3_GetObject_MRAP_section.md")
	+ [Get an object from a bucket if it has been modified](s3_example_s3_GetObject_IfModifiedSince_section.md "s3_example_s3_GetObject_IfModifiedSince_section.md")
	+ [Get started with S3](s3_example_s3_GettingStarted_section.md "s3_example_s3_GettingStarted_section.md")
	+ [Get started with encryption](s3_example_s3_Encryption_section.md "s3_example_s3_Encryption_section.md")
	+ [Get started with tags](s3_example_s3_Scenario_Tagging_section.md "s3_example_s3_Scenario_Tagging_section.md")
	+ [Lock Amazon S3 objects](s3_example_s3_Scenario_ObjectLock_section.md "s3_example_s3_Scenario_ObjectLock_section.md")
	+ [Make conditional requests](s3_example_s3_Scenario_ConditionalRequests_section.md "s3_example_s3_Scenario_ConditionalRequests_section.md")
	+ [Manage access control lists (ACLs)](s3_example_s3_Scenario_ManageACLs_section.md "s3_example_s3_Scenario_ManageACLs_section.md")
	+ [Manage large messages using S3](s3_example_sqs_Scenario_SqsExtendedClient_section.md "s3_example_sqs_Scenario_SqsExtendedClient_section.md")
	+ [Manage versioned objects in batches with a Lambda function](s3_example_s3_Scenario_BatchObjectVersioning_section.md "s3_example_s3_Scenario_BatchObjectVersioning_section.md")
	+ [Parse URIs](s3_example_s3_Scenario_URIParsing_section.md "s3_example_s3_Scenario_URIParsing_section.md")
	+ [Perform a multipart copy](s3_example_s3_MultipartCopy_section.md "s3_example_s3_MultipartCopy_section.md")
	+ [Process S3 event notifications](s3_example_s3_Scenario_ProcessS3EventNotification_section.md "s3_example_s3_Scenario_ProcessS3EventNotification_section.md")
	+ [Save EXIF and other image information](s3_example_cross_DetectLabels_section.md "s3_example_cross_DetectLabels_section.md")
	+ [Send event notifications to EventBridge](s3_example_s3_Scenario_PutBucketNotificationConfiguration_section.md "s3_example_s3_Scenario_PutBucketNotificationConfiguration_section.md")
	+ [Track uploads and downloads](s3_example_s3_Scenario_TrackUploadDownload_section.md "s3_example_s3_Scenario_TrackUploadDownload_section.md")
	+ [Transform data with S3 Object Lambda](s3_example_cross_ServerlessS3DataTransformation_section.md "s3_example_cross_ServerlessS3DataTransformation_section.md")
	+ [Unit and integration test with an SDK](s3_example_cross_Testing_section.md "s3_example_cross_Testing_section.md")
	+ [Upload directory to a bucket](s3_example_s3_UploadDirectoryToBucket_section.md "s3_example_s3_UploadDirectoryToBucket_section.md")
	+ [Upload or download large files](s3_example_s3_Scenario_UsingLargeFiles_section.md "s3_example_s3_Scenario_UsingLargeFiles_section.md")
	+ [Upload stream of unknown size](s3_example_s3_Scenario_UploadStream_section.md "s3_example_s3_Scenario_UploadStream_section.md")
	+ [Use checksums](s3_example_s3_Scenario_UseChecksums_section.md "s3_example_s3_Scenario_UseChecksums_section.md")
	+ [Work with Amazon S3 object integrity](s3_example_s3_Scenario_ObjectIntegrity_section.md "s3_example_s3_Scenario_ObjectIntegrity_section.md")
	+ [Work with versioned objects](s3_example_s3_Scenario_ObjectVersioningUsage_section.md "s3_example_s3_Scenario_ObjectVersioningUsage_section.md")
* [Serverless examples](service_code_examples_s3_serverless_examples.md "service_code_examples_s3_serverless_examples.md") 


	+ [Invoke a Lambda function from an Amazon S3 trigger](s3_example_serverless_S3_Lambda_section.md "s3_example_serverless_S3_Lambda_section.md")
