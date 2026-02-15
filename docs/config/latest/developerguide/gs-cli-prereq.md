# Prerequisites for Setting Up AWS Config with the AWS CLI

Before setting up AWS with the AWS CLI, you need to create an Amazon S3 bucket, an Amazon SNS topic,
and an IAM role with attached policies as prerequisites. You can then use the AWS CLI to specify
the bucket, topic, and role for AWS Config. Follow this procedure to set up your prerequisites for
AWS Config.

###### Topics

- [Step 1: Creating an Amazon S3 Bucket](#gs-cli-create-s3bucket "#gs-cli-create-s3bucket")
- [Step 2: Creating an Amazon SNS Topic](#gs-cli-create-snstopic "#gs-cli-create-snstopic")
- [Step 3: Creating an IAM Role](#gs-cli-create-iamrole "#gs-cli-create-iamrole")

## Step 1: Creating an Amazon S3 Bucket

If you already have an Amazon S3 bucket in your account and want to use it, skip this step and
go to [Step 2: Creating an Amazon SNS Topic](#gs-cli-create-snstopic "#gs-cli-create-snstopic").

###### To create a bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. In **Bucket name**, enter a DNS-compliant name for your
   bucket.

The bucket name must:

    * Be unique across all of Amazon S3.
    * Be between 3 and 63 characters long.
    * Not contain uppercase characters.
    * Start with a lowercase letter or number.

After you create the bucket, you can't change its name. Make sure the bucket name
you choose is unique across all existing bucket names in Amazon S3. For more information on
bucket naming rules and conventions, see [Bucket restrictions and
Limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the _Amazon Simple Storage Service User Guide_.

###### Important

Avoid including sensitive information in the bucket
name. The bucket name is visible in the URLs that point to the objects in the
bucket. 4. In **Region**, choose the AWS Region where you want the bucket
to reside.

Choose a Region close to you to minimize latency and costs and address regulatory
requirements. Objects stored in a Region never leave that Region unless you explicitly
transfer them to another Region. For a list of Amazon S3 AWS Regions, see [AWS service endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the
_Amazon Web Services General Reference_. 5. In **Bucket settings for Block Public Access**, choose the Block
Public Access settings that you want to apply to the bucket.

We recommend that you leave all settings enabled unless you know you need to turn
one or more of them off for your use case, such as to host a public website. Block
public access settings that you enable for the bucket will also be enabled for all
access points that you create on the bucket. For more information about blocking
public access, see [Using Amazon S3 Block
Public Access](../../../AmazonS3/latest/dev/access-control-block-public-access.md "../../../AmazonS3/latest/dev/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_. 6. (Optional) If you want to enable S3 Object Lock:

    1. Choose **Advanced settings**, and read the message that
     appears.


    ###### Important

    You can only enable S3 Object Lock for a bucket when you create it. If you
     enable Object Lock for the bucket, you can't disable it later. Enabling
     Object Lock also enables versioning for the bucket. After you enable
     Object Lock for the bucket, you must configure the Object Lock settings before
     any objects in the bucket will be protected. For more information about
     configuring protection for objects, see [Configuring S3 Object Lock
     using the Amazon S3 console](../../../AmazonS3/latest/dev/object-lock-console.md "../../../AmazonS3/latest/dev/object-lock-console.md").
    2. If you want to enable Object Lock, enter *enable* in the text box and choose
     **Confirm**.For more information about the S3 Object Lock feature, see [Locking Objects

Using Amazon S3 Object Lock](../../../AmazonS3/latest/dev/object-lock.md "../../../AmazonS3/latest/dev/object-lock.md") in the _Amazon Simple Storage Service User Guide_. 7. Choose **Create bucket**.
When you use the AWS SDKs to create a bucket, you must create a client and then use
the client to send a request to create a bucket. As a best practice, you should create
your client and bucket in the same AWS Region. If you don't specify a Region when you
create a client or a bucket, Amazon S3 uses the default Region US East (N. Virginia).

To create a client to access a dual-stack endpoint, you must specify an AWS Region.
For more information, see [Amazon S3 dual-stack endpoints](../../../AmazonS3/latest/dev/dual-stack-endpoints.md#dual-stack-endpoints-description "../../../AmazonS3/latest/dev/dual-stack-endpoints.md#dual-stack-endpoints-description"). For a list of available AWS Regions, see [Regions and endpoints](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") in
the _AWS General Reference_.

When you create a client, the Region maps to the Region-specific endpoint. The client
uses this endpoint to communicate with Amazon S3:
`s3.`<region>`.amazonaws.com`. If your Region
launched after March 20, 2019, your client and bucket must be in the same Region. However,
you can use a client in the US East (N. Virginia) Region to create a bucket in any Region
that launched before March 20, 2019. For more information, see [Legacy
Endpoints](../../../AmazonS3/latest/dev/VirtualHosting.md#s3-legacy-endpoints "../../../AmazonS3/latest/dev/VirtualHosting.md#s3-legacy-endpoints").

These AWS SDK code examples perform the following tasks:

- **Create a client by explicitly specifying an
  AWS Region** — In the example, the client uses the
  `s3.us-west-2.amazonaws.com` endpoint to communicate with Amazon S3. You can
  specify any AWS Region. For a list of AWS Regions, see [Regions and endpoints](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") in the _AWS
  General Reference_.
- **Send a create bucket request by specifying only a bucket
  name** — The client sends a request to Amazon S3 to create the bucket in
  the Region where you created a client.
- **Retrieve information about the location of the
  bucket** — Amazon S3 stores bucket location information in the
  _location_ subresource that is associated with the bucket.
  The following code examples show how to use `CreateBucket`.

.NET

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/S3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/S3#code-examples").

```

    /// <summary>
    /// Shows how to create a new Amazon S3 bucket.
    /// </summary>
    /// <param name="bucketName">The name of the bucket to create.</param>
    /// <returns>A boolean value representing the success or failure of
    /// the bucket creation process.</returns>
    public async Task<bool> CreateBucketAsync(string bucketName)
    {
        try
        {
            var request = new PutBucketRequest
            {
                BucketName = bucketName,
                UseClientRegion = true,
            };

            var response = await _amazonS3.PutBucketAsync(request);
            return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
        }
        catch (AmazonS3Exception ex)
        {
            Console.WriteLine($"Error creating bucket: '{ex.Message}'");
            return false;
        }
    }



```

- For API details, see
  [CreateBucket](../../../goto/DotNetSDKV4/s3-2006-03-01/CreateBucket.md "../../../goto/DotNetSDKV4/s3-2006-03-01/CreateBucket.md")
  in _AWS SDK for .NET API Reference_.

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples").

Create a bucket with object lock enabled.

```
    /// <summary>
    /// Create a new Amazon S3 bucket with object lock actions.
    /// </summary>
    /// <param name="bucketName">The name of the bucket to create.</param>
    /// <param name="enableObjectLock">True to enable object lock on the bucket.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> CreateBucketWithObjectLock(string bucketName, bool enableObjectLock)
    {
        Console.WriteLine($"\tCreating bucket {bucketName} with object lock {enableObjectLock}.");
        try
        {
            var request = new PutBucketRequest
            {
                BucketName = bucketName,
                UseClientRegion = true,
                ObjectLockEnabledForBucket = enableObjectLock,
            };

            var response = await _amazonS3.PutBucketAsync(request);

            return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
        }
        catch (AmazonS3Exception ex)
        {
            Console.WriteLine($"Error creating bucket: '{ex.Message}'");
            return false;
        }
    }


```

- For API details, see
  [CreateBucket](../../../goto/DotNetSDKV3/s3-2006-03-01/CreateBucket.md "../../../goto/DotNetSDKV3/s3-2006-03-01/CreateBucket.md")
  in _AWS SDK for .NET API Reference_.

Bash

**AWS CLI with Bash script**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/s3#code-examples").

```
###############################################################################
# function iecho
#
# This function enables the script to display the specified text only if
# the global variable $VERBOSE is set to true.
###############################################################################
function iecho() {
  if [[ $VERBOSE == true ]]; then
    echo "$@"
  fi
}

###############################################################################
# function errecho
#
# This function outputs everything sent to it to STDERR (standard error output).
###############################################################################
function errecho() {
  printf "%s\n" "$*" 1>&2
}

###############################################################################
# function create-bucket
#
# This function creates the specified bucket in the specified AWS Region, unless
# it already exists.
#
# Parameters:
#       -b bucket_name  -- The name of the bucket to create.
#       -r region_code  -- The code for an AWS Region in which to
#                          create the bucket.
#
# Returns:
#       The URL of the bucket that was created.
#     And:
#       0 - If successful.
#       1 - If it fails.
###############################################################################
function create_bucket() {
  local bucket_name region_code response
  local option OPTARG # Required to use getopts command in a function.

  # bashsupport disable=BP5008
  function usage() {
    echo "function create_bucket"
    echo "Creates an Amazon S3 bucket. You must supply a bucket name:"
    echo "  -b bucket_name    The name of the bucket. It must be globally unique."
    echo "  [-r region_code]    The code for an AWS Region in which the bucket is created."
    echo ""
  }

  # Retrieve the calling parameters.
  while getopts "b:r:h" option; do
    case "${option}" in
      b) bucket_name="${OPTARG}" ;;
      r) region_code="${OPTARG}" ;;
      h)
        usage
        return 0
        ;;
      \?)
        echo "Invalid parameter"
        usage
        return 1
        ;;
    esac
  done

  if [[ -z "$bucket_name" ]]; then
    errecho "ERROR: You must provide a bucket name with the -b parameter."
    usage
    return 1
  fi

  local bucket_config_arg
  # A location constraint for "us-east-1" returns an error.
  if [[ -n "$region_code" ]] && [[ "$region_code" != "us-east-1" ]]; then
    bucket_config_arg="--create-bucket-configuration LocationConstraint=$region_code"
  fi

  iecho "Parameters:\n"
  iecho "    Bucket name:   $bucket_name"
  iecho "    Region code:   $region_code"
  iecho ""

  # If the bucket already exists, we don't want to try to create it.
  if (bucket_exists "$bucket_name"); then
    errecho "ERROR: A bucket with that name already exists. Try again."
    return 1
  fi

  # shellcheck disable=SC2086
  response=$(aws s3api create-bucket \
    --bucket "$bucket_name" \
    $bucket_config_arg)

  # shellcheck disable=SC2181
  if [[ ${?} -ne 0 ]]; then
    errecho "ERROR: AWS reports create-bucket operation failed.\n$response"
    return 1
  fi
}


```

- For API details, see
  [CreateBucket](../../../goto/aws-cli/s3-2006-03-01/CreateBucket.md "../../../goto/aws-cli/s3-2006-03-01/CreateBucket.md")
  in _AWS CLI Command Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples").

```
bool AwsDoc::S3::createBucket(const Aws::String &bucketName,
                              const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);
    Aws::S3::Model::CreateBucketRequest request;
    request.SetBucket(bucketName);

    if (clientConfig.region != "us-east-1") {
        Aws::S3::Model::CreateBucketConfiguration createBucketConfig;
        createBucketConfig.SetLocationConstraint(
                Aws::S3::Model::BucketLocationConstraintMapper::GetBucketLocationConstraintForName(
                        clientConfig.region));
        request.SetCreateBucketConfiguration(createBucketConfig);
    }

    Aws::S3::Model::CreateBucketOutcome outcome = client.CreateBucket(request);
    if (!outcome.IsSuccess()) {
        auto err = outcome.GetError();
        std::cerr << "Error: createBucket: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "Created bucket " << bucketName <<
                  " in the specified AWS Region." << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [CreateBucket](../../../goto/SdkForCpp/s3-2006-03-01/CreateBucket.md "../../../goto/SdkForCpp/s3-2006-03-01/CreateBucket.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**Example 1: To create a bucket**

The following `create-bucket` example creates a bucket named `amzn-s3-demo-bucket`:

```
`aws s3api create-bucket \
 --bucket `amzn-s3-demo-bucket` \
 --region `us-east-1``

```

Output:

```
{
    "Location": "/amzn-s3-demo-bucket"
}
```

For more information, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

**Example 2: To create a bucket with owner enforced**

The following `create-bucket` example creates a bucket named `amzn-s3-demo-bucket` that uses the bucket owner enforced setting for S3 Object Ownership.

```
`aws s3api create-bucket \
 --bucket `amzn-s3-demo-bucket` \
 --region `us-east-1` \
 --object-ownership `BucketOwnerEnforced``

```

Output:

```
{
    "Location": "/amzn-s3-demo-bucket"
}
```

For more information, see [Controlling ownership of objects and disabling ACLs](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the _Amazon S3 User Guide_.

**Example 3: To create a bucket outside of the `us-east-1` region**

The following `create-bucket` example creates a bucket named `amzn-s3-demo-bucket` in the
`eu-west-1` region. Regions outside of `us-east-1` require the appropriate
`LocationConstraint` to be specified in order to create the bucket in the
desired region.

```
`aws s3api create-bucket \
 --bucket `amzn-s3-demo-bucket` \
 --region `eu-west-1` \
 --create-bucket-configuration `LocationConstraint=eu-west-1``

```

Output:

```
{
    "Location": "http://amzn-s3-demo-bucket.s3.amazonaws.com/"
}
```

For more information, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

- For API details, see
  [CreateBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html")
  in _AWS CLI Command Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/s3#code-examples").

Create a bucket with default configuration.

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



// CreateBucket creates a bucket with the specified name in the specified Region.
func (basics BucketBasics) CreateBucket(ctx context.Context, name string, region string) error {
	_, err := basics.S3Client.CreateBucket(ctx, &s3.CreateBucketInput{
		Bucket: aws.String(name),
		CreateBucketConfiguration: &types.CreateBucketConfiguration{
			LocationConstraint: types.BucketLocationConstraint(region),
		},
	})
	if err != nil {
		var owned *types.BucketAlreadyOwnedByYou
		var exists *types.BucketAlreadyExists
		if errors.As(err, &owned) {
			log.Printf("You already own bucket %s.\n", name)
			err = owned
		} else if errors.As(err, &exists) {
			log.Printf("Bucket %s already exists.\n", name)
			err = exists
		}
	} else {
		err = s3.NewBucketExistsWaiter(basics.S3Client).Wait(
			ctx, &s3.HeadBucketInput{Bucket: aws.String(name)}, time.Minute)
		if err != nil {
			log.Printf("Failed attempt to wait for bucket %s to exist.\n", name)
		}
	}
	return err
}



```

Create a bucket with object locking and wait for it to exist.

```

import (
	"bytes"
	"context"
	"errors"
	"fmt"
	"log"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/aws/aws-sdk-go-v2/service/s3/types"
	"github.com/aws/smithy-go"
)

// S3Actions wraps S3 service actions.
type S3Actions struct {
	S3Client  *s3.Client
	S3Manager *manager.Uploader
}



// CreateBucketWithLock creates a new S3 bucket with optional object locking enabled
// and waits for the bucket to exist before returning.
func (actor S3Actions) CreateBucketWithLock(ctx context.Context, bucket string, region string, enableObjectLock bool) (string, error) {
	input := &s3.CreateBucketInput{
		Bucket: aws.String(bucket),
		CreateBucketConfiguration: &types.CreateBucketConfiguration{
			LocationConstraint: types.BucketLocationConstraint(region),
		},
	}

	if enableObjectLock {
		input.ObjectLockEnabledForBucket = aws.Bool(true)
	}

	_, err := actor.S3Client.CreateBucket(ctx, input)
	if err != nil {
		var owned *types.BucketAlreadyOwnedByYou
		var exists *types.BucketAlreadyExists
		if errors.As(err, &owned) {
			log.Printf("You already own bucket %s.\n", bucket)
			err = owned
		} else if errors.As(err, &exists) {
			log.Printf("Bucket %s already exists.\n", bucket)
			err = exists
		}
	} else {
		err = s3.NewBucketExistsWaiter(actor.S3Client).Wait(
			ctx, &s3.HeadBucketInput{Bucket: aws.String(bucket)}, time.Minute)
		if err != nil {
			log.Printf("Failed attempt to wait for bucket %s to exist.\n", bucket)
		}
	}

	return bucket, err
}



```

- For API details, see
  [CreateBucket](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.CreateBucket "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.CreateBucket")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").

Create a bucket.

```

    /**
     * Creates an S3 bucket asynchronously.
     *
     * @param bucketName the name of the S3 bucket to create
     * @return a {@link CompletableFuture} that completes when the bucket is created and ready
     * @throws RuntimeException if there is a failure while creating the bucket
     */
    public CompletableFuture<Void> createBucketAsync(String bucketName) {
        CreateBucketRequest bucketRequest = CreateBucketRequest.builder()
            .bucket(bucketName)
            .build();

        CompletableFuture<CreateBucketResponse> response = getAsyncClient().createBucket(bucketRequest);
        return response.thenCompose(resp -> {
            S3AsyncWaiter s3Waiter = getAsyncClient().waiter();
            HeadBucketRequest bucketRequestWait = HeadBucketRequest.builder()
                .bucket(bucketName)
                .build();

            CompletableFuture<WaiterResponse<HeadBucketResponse>> waiterResponseFuture =
                s3Waiter.waitUntilBucketExists(bucketRequestWait);
            return waiterResponseFuture.thenAccept(waiterResponse -> {
                waiterResponse.matched().response().ifPresent(headBucketResponse -> {
                    logger.info(bucketName + " is ready");
                });
            });
        }).whenComplete((resp, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to create bucket", ex);
            }
        });
    }


```

Create a bucket with object lock enabled.

```
    // Create a new Amazon S3 bucket with object lock options.
    public void createBucketWithLockOptions(boolean enableObjectLock, String bucketName) {
        S3Waiter s3Waiter = getClient().waiter();
        CreateBucketRequest bucketRequest = CreateBucketRequest.builder()
            .bucket(bucketName)
            .objectLockEnabledForBucket(enableObjectLock)
            .build();

        getClient().createBucket(bucketRequest);
        HeadBucketRequest bucketRequestWait = HeadBucketRequest.builder()
            .bucket(bucketName)
            .build();

        // Wait until the bucket is created and print out the response.
        s3Waiter.waitUntilBucketExists(bucketRequestWait);
        System.out.println(bucketName + " is ready");
    }


```

- For API details, see
  [CreateBucket](../../../goto/SdkForJavaV2/s3-2006-03-01/CreateBucket.md "../../../goto/SdkForJavaV2/s3-2006-03-01/CreateBucket.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples").

Create the bucket.

```
import {
  BucketAlreadyExists,
  BucketAlreadyOwnedByYou,
  CreateBucketCommand,
  S3Client,
  waitUntilBucketExists,
} from "@aws-sdk/client-s3";

/**
 * Create an Amazon S3 bucket.
 * @param {{ bucketName: string }} config
 */
export const main = async ({ bucketName }) => {
  const client = new S3Client({});

  try {
    const { Location } = await client.send(
      new CreateBucketCommand({
        // The name of the bucket. Bucket names are unique and have several other constraints.
        // See https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html
        Bucket: bucketName,
      }),
    );
    await waitUntilBucketExists({ client }, { Bucket: bucketName });
    console.log(`Bucket created with location ${Location}`);
  } catch (caught) {
    if (caught instanceof BucketAlreadyExists) {
      console.error(
        `The bucket "${bucketName}" already exists in another AWS account. Bucket names must be globally unique.`,
      );
    }
    // WARNING: If you try to create a bucket in the North Virginia region,
    // and you already own a bucket in that region with the same name, this
    // error will not be thrown. Instead, the call will return successfully
    // and the ACL on that bucket will be reset.
    else if (caught instanceof BucketAlreadyOwnedByYou) {
      console.error(
        `The bucket "${bucketName}" already exists in this AWS account.`,
      );
    } else {
      throw caught;
    }
  }
};


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/s3-example-creating-buckets.md#s3-example-creating-buckets-new-bucket-2 "../../../sdk-for-javascript/v3/developer-guide/s3-example-creating-buckets.md#s3-example-creating-buckets-new-bucket-2").
- For API details, see
  [CreateBucket](../../../AWSJavaScriptSDK/v3/latest/client/s3/command/CreateBucketCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/s3/command/CreateBucketCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/s3#code-examples").

```
suspend fun createNewBucket(bucketName: String) {
    val request =
        CreateBucketRequest {
            bucket = bucketName
        }

    S3Client.fromEnvironment { region = "us-east-1" }.use { s3 ->
        s3.createBucket(request)
        println("$bucketName is ready")
    }
}


```

- For API details, see
  [CreateBucket](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/s3#code-examples").

Create a bucket.

```
        $s3client = new Aws\S3\S3Client(['region' => 'us-west-2']);

        try {
            $this->s3client->createBucket([
                'Bucket' => $this->bucketName,
                'CreateBucketConfiguration' => ['LocationConstraint' => $region],
            ]);
            echo "Created bucket named: $this->bucketName \n";
        } catch (Exception $exception) {
            echo "Failed to create bucket $this->bucketName with error: " . $exception->getMessage();
            exit("Please fix error with bucket creation before continuing.");
        }


```

- For API details, see
  [CreateBucket](../../../goto/SdkForPHPV3/s3-2006-03-01/CreateBucket.md "../../../goto/SdkForPHPV3/s3-2006-03-01/CreateBucket.md")
  in _AWS SDK for PHP API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/s3_basics#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/s3_basics#code-examples").

Create a bucket with default settings.

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


    def create(self, region_override=None):
        """
        Create an Amazon S3 bucket in the default Region for the account or in the
        specified Region.

        :param region_override: The Region in which to create the bucket. If this is
                                not specified, the Region configured in your shared
                                credentials is used.
        """
        if region_override is not None:
            region = region_override
        else:
            region = self.bucket.meta.client.meta.region_name
        try:
            self.bucket.create(CreateBucketConfiguration={"LocationConstraint": region})

            self.bucket.wait_until_exists()
            logger.info("Created bucket '%s' in region=%s", self.bucket.name, region)
        except ClientError as error:
            logger.exception(
                "Couldn't create bucket named '%s' in region=%s.",
                self.bucket.name,
                region,
            )
            raise error



```

Create a versioned bucket with a lifecycle configuration.

```
def create_versioned_bucket(bucket_name, prefix):
    """
    Creates an Amazon S3 bucket, enables it for versioning, and configures a lifecycle
    that expires noncurrent object versions after 7 days.

    Adding a lifecycle configuration to a versioned bucket is a best practice.
    It helps prevent objects in the bucket from accumulating a large number of
    noncurrent versions, which can slow down request performance.

    Usage is shown in the usage_demo_single_object function at the end of this module.

    :param bucket_name: The name of the bucket to create.
    :param prefix: Identifies which objects are automatically expired under the
                   configured lifecycle rules.
    :return: The newly created bucket.
    """
    try:
        bucket = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": s3.meta.client.meta.region_name
            },
        )
        logger.info("Created bucket %s.", bucket.name)
    except ClientError as error:
        if error.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
            logger.warning("Bucket %s already exists! Using it.", bucket_name)
            bucket = s3.Bucket(bucket_name)
        else:
            logger.exception("Couldn't create bucket %s.", bucket_name)
            raise

    try:
        bucket.Versioning().enable()
        logger.info("Enabled versioning on bucket %s.", bucket.name)
    except ClientError:
        logger.exception("Couldn't enable versioning on bucket %s.", bucket.name)
        raise

    try:
        expiration = 7
        bucket.LifecycleConfiguration().put(
            LifecycleConfiguration={
                "Rules": [
                    {
                        "Status": "Enabled",
                        "Prefix": prefix,
                        "NoncurrentVersionExpiration": {"NoncurrentDays": expiration},
                    }
                ]
            }
        )
        logger.info(
            "Configured lifecycle to expire noncurrent versions after %s days "
            "on bucket %s.",
            expiration,
            bucket.name,
        )
    except ClientError as error:
        logger.warning(
            "Couldn't configure lifecycle on bucket %s because %s. "
            "Continuing anyway.",
            bucket.name,
            error,
        )

    return bucket




```

- For API details, see
  [CreateBucket](../../../goto/boto3/s3-2006-03-01/CreateBucket.md "../../../goto/boto3/s3-2006-03-01/CreateBucket.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/s3#code-examples").

```
require 'aws-sdk-s3'

# Wraps Amazon S3 bucket actions.
class BucketCreateWrapper
  attr_reader :bucket

  # @param bucket [Aws::S3::Bucket] An Amazon S3 bucket initialized with a name. This is a client-side object until
  #                                 create is called.
  def initialize(bucket)
    @bucket = bucket
  end

  # Creates an Amazon S3 bucket in the specified AWS Region.
  #
  # @param region [String] The Region where the bucket is created.
  # @return [Boolean] True when the bucket is created; otherwise, false.
  def create?(region)
    @bucket.create(create_bucket_configuration: { location_constraint: region })
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't create bucket. Here's why: #{e.message}"
    false
  end

  # Gets the Region where the bucket is located.
  #
  # @return [String] The location of the bucket.
  def location
    if @bucket.nil?
      'None. You must create a bucket before you can get its location!'
    else
      @bucket.client.get_bucket_location(bucket: @bucket.name).location_constraint
    end
  rescue Aws::Errors::ServiceError => e
    "Couldn't get the location of #{@bucket.name}. Here's why: #{e.message}"
  end
end

# Example usage:
def run_demo
  region = "us-west-2"
  wrapper = BucketCreateWrapper.new(Aws::S3::Bucket.new("amzn-s3-demo-bucket-#{Random.uuid}"))
  return unless wrapper.create?(region)

  puts "Created bucket #{wrapper.bucket.name}."
  puts "Your bucket's region is: #{wrapper.location}"
end

run_demo if $PROGRAM_NAME == __FILE__


```

- For API details, see
  [CreateBucket](../../../goto/SdkForRubyV3/s3-2006-03-01/CreateBucket.md "../../../goto/SdkForRubyV3/s3-2006-03-01/CreateBucket.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples").

```
pub async fn create_bucket(
    client: &aws_sdk_s3::Client,
    bucket_name: &str,
    region: &aws_config::Region,
) -> Result<Option<aws_sdk_s3::operation::create_bucket::CreateBucketOutput>, S3ExampleError> {
    let constraint = aws_sdk_s3::types::BucketLocationConstraint::from(region.to_string().as_str());
    let cfg = aws_sdk_s3::types::CreateBucketConfiguration::builder()
        .location_constraint(constraint)
        .build();
    let create = client
        .create_bucket()
        .create_bucket_configuration(cfg)
        .bucket(bucket_name)
        .send()
        .await;

    // BucketAlreadyExists and BucketAlreadyOwnedByYou are not problems for this task.
    create.map(Some).or_else(|err| {
        if err
            .as_service_error()
            .map(|se| se.is_bucket_already_exists() || se.is_bucket_already_owned_by_you())
            == Some(true)
        {
            Ok(None)
        } else {
            Err(S3ExampleError::from(err))
        }
    })
}


```

- For API details, see
  [CreateBucket](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.create_bucket "https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.create_bucket")
  in _AWS SDK for Rust API reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/s3#code-examples").

```
    TRY.
        " determine our region from our session
        DATA(lv_region) = CONV /aws1/s3_bucketlocationcnstrnt( lo_session->get_region( ) ).
        DATA lo_constraint TYPE REF TO /aws1/cl_s3_createbucketconf.
        " When in the us-east-1 region, you must not specify a constraint
        " In all other regions, specify the region as the constraint
        IF lv_region = 'us-east-1'.
          CLEAR lo_constraint.
        ELSE.
          lo_constraint = NEW /aws1/cl_s3_createbucketconf( lv_region ).
        ENDIF.

        lo_s3->createbucket(
            iv_bucket = iv_bucket_name
            io_createbucketconfiguration  = lo_constraint ).
        MESSAGE 'S3 bucket created.' TYPE 'I'.
      CATCH /aws1/cx_s3_bucketalrdyexists.
        MESSAGE 'Bucket name already exists.' TYPE 'E'.
      CATCH /aws1/cx_s3_bktalrdyownedbyyou.
        MESSAGE 'Bucket already exists and is owned by you.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [CreateBucket](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/s3/basics#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/s3/basics#code-examples").

```
import AWSS3

    public func createBucket(name: String) async throws {
        var input = CreateBucketInput(
            bucket: name
        )

        // For regions other than "us-east-1", you must set the locationConstraint in the createBucketConfiguration.
        // For more information, see LocationConstraint in the S3 API guide.
        // https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html#API_CreateBucket_RequestBody
        if let region = configuration.region {
            if region != "us-east-1" {
                input.createBucketConfiguration = S3ClientTypes.CreateBucketConfiguration(locationConstraint: S3ClientTypes.BucketLocationConstraint(rawValue: region))
            }
        }

        do {
            _ = try await client.createBucket(input: input)
        }
        catch let error as BucketAlreadyOwnedByYou {
            print("The bucket '\(name)' already exists and is owned by you. You may wish to ignore this exception.")
            throw error
        }
        catch {
            print("ERROR: ", dump(error, name: "Creating a bucket"))
            throw error
        }
    }


```

- For API details, see
  [CreateBucket](<https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/createbucket(input:)> "https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/createbucket(input:)")
  in _AWS SDK for Swift API reference_.

###### Note

You can also use an Amazon S3 bucket from a different account, but you may need to create a
policy for the bucket that grants access permissions to AWS Config. For information on granting
permissions to an Amazon S3 bucket, see [Permissions for the Amazon S3 Bucket for the AWS Config Delivery
Channel](s3-bucket-policy.md "s3-bucket-policy.md"), and then go to [Step 2: Creating an Amazon SNS Topic](#gs-cli-create-snstopic "#gs-cli-create-snstopic").

## Step 2: Creating an Amazon SNS Topic

If you already have an Amazon SNS topic in your account and want to use it, skip this step and
go to [Step 3: Creating an IAM Role](#gs-cli-create-iamrole "#gs-cli-create-iamrole").

###### To create an Amazon SNS topic

1.  Open the Amazon SNS console at
    [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2.  Do one of the following:
    - If no topics have ever been created under your AWS account before, read the
      description of Amazon SNS on the home page.

    - If topics have been created under your AWS account before, on the navigation
      panel, choose **Topics**.

3.  On the **Topics** page, choose **Create
    topic**.
4.  On the **Create topic** page, in the **Details**
    section, do the following:
    1. For **Type**, choose a topic type
       (**Standard** or **FIFO**).
    2. Enter a **Name** for the topic. For a [FIFO topic](../../../sns/latest/dg/sns-fifo-topics.md "../../../sns/latest/dg/sns-fifo-topics.md"), add
       **.fifo** to the end of the name.
    3. (Optional) Enter a **Display name** for the topic.
    4. (Optional) For a FIFO topic, you can choose **content-based message
       deduplication** to enable default message deduplication. For more
       information, see [Message
       deduplication for FIFO topics](../../../sns/latest/dg/fifo-message-dedup.md "../../../sns/latest/dg/fifo-message-dedup.md").

5.  (Optional) Expand the **Encryption** section and do the
    following. For more information, see [Encryption at rest](../../../sns/latest/dg/sns-server-side-encryption.md "../../../sns/latest/dg/sns-server-side-encryption.md").
    1. Choose **Enable encryption**.
    2. Specify the customer master key (CMK). For more information, see [Key
       terms](../../../sns/latest/dg/sns-server-side-encryption.md#sse-key-terms "../../../sns/latest/dg/sns-server-side-encryption.md#sse-key-terms").

    For each CMK type, the **Description**,
    **Account**, and **CMK ARN** are
    displayed.

    ###### Important

    If you aren't the owner of the CMK, or if you log in with an account
    that doesn't have the `kms:ListAliases` and
    `kms:DescribeKey` permissions, you won't be able to view
    information about the CMK on the Amazon SNS console.

    Ask the owner of the CMK to grant you these permissions. For more
    information, see the [AWS KMS API Permissions:
    Actions and Resources Reference](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the
    _AWS Key Management Service Developer Guide_.

        * The AWS managed CMK for Amazon SNS **(Default)
         alias/aws/sns** is selected by default.


        ###### Note

        Keep the following in mind:



        	+ The first time you use the AWS Management Console to specify the AWS managed
        	 CMK for Amazon SNS for a topic, AWS KMS creates the AWS managed CMK for
        	 Amazon SNS.
        	+ Alternatively, the first time you use the `Publish`
        	 action on a topic with SSE enabled, AWS KMS creates the AWS managed CMK
        	 for Amazon SNS.
        * To use a custom CMK from your AWS account, choose the **Customer
         master key (CMK)** field and then choose the custom CMK from the
         list.


        ###### Note

        For instructions on creating custom CMKs, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
         *AWS Key Management Service Developer Guide*
        * To use a custom CMK ARN from your AWS account or from another AWS
         account, enter it into the **Customer master key (CMK)**
         field.

6.  (Optional) By default, only the topic owner can publish or subscribe to the topic.
    To configure additional access permissions, expand the **Access
    policy** section. For more information, see [Identity and access
    management in Amazon SNS](../../../sns/latest/dg/sns-authentication-and-access-control.md "../../../sns/latest/dg/sns-authentication-and-access-control.md") and [Example cases for Amazon SNS access
    control](../../../sns/latest/dg/sns-access-policy-use-cases.md "../../../sns/latest/dg/sns-access-policy-use-cases.md").

###### Note

When you create a topic using the console, the default policy uses the
`aws:SourceOwner` condition key. This key is similar to
`aws:SourceAccount`. 7. (Optional) To configure how Amazon SNS retries failed message delivery attempts, expand
the **Delivery retry policy (HTTP/S)** section. For more information,
see [Amazon SNS message delivery
retries](../../../sns/latest/dg/sns-message-delivery-retries.md "../../../sns/latest/dg/sns-message-delivery-retries.md"). 8. (Optional) To configure how Amazon SNS logs the delivery of messages to CloudWatch, expand
the **Delivery status logging** section. For more information, see
[Amazon SNS message delivery
status](../../../sns/latest/dg/sns-topic-attributes.md "../../../sns/latest/dg/sns-topic-attributes.md"). 9. (Optional) To add metadata tags to the topic, expand the **Tags**
section, enter a **Key** and a **Value** (optional)
and choose **Add tag**. For more information, see [Amazon SNS topic tagging](../../../sns/latest/dg/sns-tags.md "../../../sns/latest/dg/sns-tags.md"). 10. Choose **Create topic**.

The topic is created and the
**`MyTopic`** page is displayed.

The topic's **Name**, **ARN**, (optional)
**Display name**, and **Topic owner**'s AWS
account ID are displayed in the **Details** section. 11. Copy the topic ARN to the clipboard, for example:

```
arn:aws:sns:us-east-2:123456789012:MyTopic
```

###### To subscribe an email address to the Amazon SNS topic

1.  Open the Amazon SNS console at
    [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2.  In the left navigation pane, choose **Subscriptions**.
3.  On the **Subscriptions** page, choose **Create
    subscription**.
4.  On the **Create subscription** page, in the
    **Details** section, do the following:

        1. For **Topic ARN**, choose the Amazon Resource Name (ARN) of a
         topic.
        2. For **Protocol**, choose an endpoint type.  The available endpoint types are:




        	* [HTTP/HTTPS](../../../sns/latest/dg/sns-http-https-endpoint-as-subscriber.md "../../../sns/latest/dg/sns-http-https-endpoint-as-subscriber.md")
        	* [Email/Email-JSON](../../../sns/latest/dg/sns-email-notifications.md "../../../sns/latest/dg/sns-email-notifications.md")
        	* [Amazon Data Firehose](../../../sns/latest/dg/sns-firehose-as-subscriber.md "../../../sns/latest/dg/sns-firehose-as-subscriber.md")
        	* [Amazon SQS](../../../sns/latest/dg/sns-sqs-as-subscriber.md "../../../sns/latest/dg/sns-sqs-as-subscriber.md")


        	###### Note

        	To subscribe to an [SNS
        	 FIFO topic](../../../sns/latest/dg/sns-fifo-topics.md "../../../sns/latest/dg/sns-fifo-topics.md"), choose this option.
        	* [AWS Lambda](../../../sns/latest/dg/sns-lambda-as-subscriber.md "../../../sns/latest/dg/sns-lambda-as-subscriber.md")
        	* [Platform application endpoint](../../../sns/latest/dg/sns-mobile-application-as-subscriber.md "../../../sns/latest/dg/sns-mobile-application-as-subscriber.md")
        	* [SMS](../../../sns/latest/dg/sns-mobile-phone-number-as-subscriber.md "../../../sns/latest/dg/sns-mobile-phone-number-as-subscriber.md")
        3. For **Endpoint**, enter the endpoint value, such as an email
         address or the ARN of an Amazon SQS queue.
        4. Firehose endpoints only: For **Subscription role ARN**, specify
         the ARN of the IAM role that you created for writing to Firehose delivery streams.
         For more information, see [Prerequisites for
         subscribing Firehose delivery streams to Amazon SNS topics](../../../sns/latest/dg/prereqs-kinesis-data-firehose.md "../../../sns/latest/dg/prereqs-kinesis-data-firehose.md").
        5. (Optional) For Firehose, Amazon SQS, HTTP/S endpoints, you can also enable raw message
         delivery. For more information, see [Amazon SNS raw message
         delivery](../../../sns/latest/dg/sns-large-payload-raw-message-delivery.md "../../../sns/latest/dg/sns-large-payload-raw-message-delivery.md").
        6. (Optional) To configure a filter policy, expand the **Subscription
         filter policy** section. For more information, see [Amazon SNS subscription
         filter policies](../../../sns/latest/dg/sns-subscription-filter-policies.md "../../../sns/latest/dg/sns-subscription-filter-policies.md").
        7. (Optional) To configure a dead-letter queue for the subscription, expand the
         **Redrive policy (dead-letter queue)** section. For more
         information, see [Amazon SNS
         dead-letter queues (DLQs)](../../../sns/latest/dg/sns-dead-letter-queues.md "../../../sns/latest/dg/sns-dead-letter-queues.md").
        8. Choose **Create subscription**.


        The console creates the subscription and opens the subscription's
         **Details** page.

    To use an AWS SDK, you must configure it with your credentials. For more
    information, see [The shared config and credentials
    files](../../../sdkref/latest/guide/creds-config-files.md "../../../sdkref/latest/guide/creds-config-files.md") in the _AWS SDKs and Tools Reference Guide_.

The following code examples show how to use `CreateTopic`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SNS#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SNS#code-examples").

Create a topic with a specific name.

```
    using System;
    using System.Threading.Tasks;
    using Amazon.SimpleNotificationService;
    using Amazon.SimpleNotificationService.Model;

    /// <summary>
    /// This example shows how to use Amazon Simple Notification Service
    /// (Amazon SNS) to add a new Amazon SNS topic.
    /// </summary>
    public class CreateSNSTopic
    {
        public static async Task Main()
        {
            string topicName = "ExampleSNSTopic";

            IAmazonSimpleNotificationService client = new AmazonSimpleNotificationServiceClient();

            var topicArn = await CreateSNSTopicAsync(client, topicName);
            Console.WriteLine($"New topic ARN: {topicArn}");
        }

        /// <summary>
        /// Creates a new SNS topic using the supplied topic name.
        /// </summary>
        /// <param name="client">The initialized SNS client object used to
        /// create the new topic.</param>
        /// <param name="topicName">A string representing the topic name.</param>
        /// <returns>The Amazon Resource Name (ARN) of the created topic.</returns>
        public static async Task<string> CreateSNSTopicAsync(IAmazonSimpleNotificationService client, string topicName)
        {
            var request = new CreateTopicRequest
            {
                Name = topicName,
            };

            var response = await client.CreateTopicAsync(request);

            return response.TopicArn;
        }
    }



```

Create a new topic with a name and specific FIFO and de-duplication attributes.

```
    /// <summary>
    /// Create a new topic with a name and specific FIFO and de-duplication attributes.
    /// </summary>
    /// <param name="topicName">The name for the topic.</param>
    /// <param name="useFifoTopic">True to use a FIFO topic.</param>
    /// <param name="useContentBasedDeduplication">True to use content-based de-duplication.</param>
    /// <returns>The ARN of the new topic.</returns>
    public async Task<string> CreateTopicWithName(string topicName, bool useFifoTopic, bool useContentBasedDeduplication)
    {
        var createTopicRequest = new CreateTopicRequest()
        {
            Name = topicName,
        };

        if (useFifoTopic)
        {
            // Update the name if it is not correct for a FIFO topic.
            if (!topicName.EndsWith(".fifo"))
            {
                createTopicRequest.Name = topicName + ".fifo";
            }

            // Add the attributes from the method parameters.
            createTopicRequest.Attributes = new Dictionary<string, string>
            {
                { "FifoTopic", "true" }
            };
            if (useContentBasedDeduplication)
            {
                createTopicRequest.Attributes.Add("ContentBasedDeduplication", "true");
            }
        }

        var createResponse = await _amazonSNSClient.CreateTopicAsync(createTopicRequest);
        return createResponse.TopicArn;
    }


```

- For API details, see
  [CreateTopic](../../../goto/DotNetSDKV3/sns-2010-03-31/CreateTopic.md "../../../goto/DotNetSDKV3/sns-2010-03-31/CreateTopic.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples").

```
//! Create an Amazon Simple Notification Service (Amazon SNS) topic.
/*!
  \param topicName: An Amazon SNS topic name.
  \param topicARNResult: String to return the Amazon Resource Name (ARN) for the topic.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::SNS::createTopic(const Aws::String &topicName,
                              Aws::String &topicARNResult,
                              const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::SNS::SNSClient snsClient(clientConfiguration);

    Aws::SNS::Model::CreateTopicRequest request;
    request.SetName(topicName);

    const Aws::SNS::Model::CreateTopicOutcome outcome = snsClient.CreateTopic(request);

    if (outcome.IsSuccess()) {
        topicARNResult = outcome.GetResult().GetTopicArn();
        std::cout << "Successfully created an Amazon SNS topic " << topicName
                  << " with topic ARN '" << topicARNResult
                  << "'." << std::endl;

    }
    else {
        std::cerr << "Error creating topic " << topicName << ":" <<
                  outcome.GetError().GetMessage() << std::endl;
        topicARNResult.clear();
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [CreateTopic](../../../goto/SdkForCpp/sns-2010-03-31/CreateTopic.md "../../../goto/SdkForCpp/sns-2010-03-31/CreateTopic.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To create an SNS topic**

The following `create-topic` example creates an SNS topic named `my-topic`.

```
`aws sns create-topic \
 --name `my-topic``

```

Output:

```
{
    "ResponseMetadata": {
        "RequestId": "1469e8d7-1642-564e-b85d-a19b4b341f83"
    },
    "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic"
}
```

For more information, see [Using the AWS Command Line Interface with Amazon SQS and Amazon SNS](../../../cli/latest/userguide/cli-sqs-queue-sns-topic.md "../../../cli/latest/userguide/cli-sqs-queue-sns-topic.md") in the _AWS Command Line Interface User Guide_.

- For API details, see
  [CreateTopic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-topic.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-topic.html")
  in _AWS CLI Command Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples").

```

import (
	"context"
	"encoding/json"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/sns"
	"github.com/aws/aws-sdk-go-v2/service/sns/types"
)

// SnsActions encapsulates the Amazon Simple Notification Service (Amazon SNS) actions
// used in the examples.
type SnsActions struct {
	SnsClient *sns.Client
}



// CreateTopic creates an Amazon SNS topic with the specified name. You can optionally
// specify that the topic is created as a FIFO topic and whether it uses content-based
// deduplication instead of ID-based deduplication.
func (actor SnsActions) CreateTopic(ctx context.Context, topicName string, isFifoTopic bool, contentBasedDeduplication bool) (string, error) {
	var topicArn string
	topicAttributes := map[string]string{}
	if isFifoTopic {
		topicAttributes["FifoTopic"] = "true"
	}
	if contentBasedDeduplication {
		topicAttributes["ContentBasedDeduplication"] = "true"
	}
	topic, err := actor.SnsClient.CreateTopic(ctx, &sns.CreateTopicInput{
		Name:       aws.String(topicName),
		Attributes: topicAttributes,
	})
	if err != nil {
		log.Printf("Couldn't create topic %v. Here's why: %v\n", topicName, err)
	} else {
		topicArn = *topic.TopicArn
	}

	return topicArn, err
}



```

- For API details, see
  [CreateTopic](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.CreateTopic "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.CreateTopic")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.CreateTopicRequest;
import software.amazon.awssdk.services.sns.model.CreateTopicResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class CreateTopic {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <topicName>

                Where:
                   topicName - The name of the topic to create (for example, mytopic).

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String topicName = args[0];
        System.out.println("Creating a topic with name: " + topicName);
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        String arnVal = createSNSTopic(snsClient, topicName);
        System.out.println("The topic ARN is" + arnVal);
        snsClient.close();
    }

    public static String createSNSTopic(SnsClient snsClient, String topicName) {
        CreateTopicResponse result;
        try {
            CreateTopicRequest request = CreateTopicRequest.builder()
                    .name(topicName)
                    .build();

            result = snsClient.createTopic(request);
            return result.topicArn();

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }
}


```

- For API details, see
  [CreateTopic](../../../goto/SdkForJavaV2/sns-2010-03-31/CreateTopic.md "../../../goto/SdkForJavaV2/sns-2010-03-31/CreateTopic.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sns#code-examples").

Create the client in a separate module and export it.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});


```

Import the SDK and client modules and call the API.

```
import { CreateTopicCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} topicName - The name of the topic to create.
 */
export const createTopic = async (topicName = "TOPIC_NAME") => {
  const response = await snsClient.send(
    new CreateTopicCommand({ Name: topicName }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '087b8ad2-4593-50c4-a496-d7e90b82cf3e',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   TopicArn: 'arn:aws:sns:us-east-1:xxxxxxxxxxxx:TOPIC_NAME'
  // }
  return response;
};


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.md#sns-examples-managing-topics-createtopic "../../../sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.md#sns-examples-managing-topics-createtopic").
- For API details, see
  [CreateTopic](../../../AWSJavaScriptSDK/v3/latest/client/sns/command/CreateTopicCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/sns/command/CreateTopicCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples").

```
suspend fun createSNSTopic(topicName: String): String {
    val request =
        CreateTopicRequest {
            name = topicName
        }

    SnsClient.fromEnvironment { region = "us-east-1" }.use { snsClient ->
        val result = snsClient.createTopic(request)
        return result.topicArn.toString()
    }
}


```

- For API details, see
  [CreateTopic](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples").

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\Sns\SnsClient;


/**
 * Create a Simple Notification Service topics in your AWS account at the requested region.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */

$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

$topicname = 'myTopic';

try {
    $result = $SnSclient->createTopic([
        'Name' => $topicname,
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}



```

- For more information, see [AWS SDK for PHP Developer Guide](../../../sdk-for-php/v3/developer-guide/sns-examples-managing-topics.md#create-a-topic "../../../sdk-for-php/v3/developer-guide/sns-examples-managing-topics.md#create-a-topic").
- For API details, see
  [CreateTopic](../../../goto/SdkForPHPV3/sns-2010-03-31/CreateTopic.md "../../../goto/SdkForPHPV3/sns-2010-03-31/CreateTopic.md")
  in _AWS SDK for PHP API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns#code-examples").

```
class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource


    def create_topic(self, name):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: The newly created topic.
        """
        try:
            topic = self.sns_resource.create_topic(Name=name)
            logger.info("Created topic %s with ARN %s.", name, topic.arn)
        except ClientError:
            logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return topic



```

```
class SnsWrapper:
    """Wrapper class for managing Amazon SNS operations."""

    def __init__(self, sns_client: Any) -> None:
        """
        Initialize the SnsWrapper.

        :param sns_client: A Boto3 Amazon SNS client.
        """
        self.sns_client = sns_client

    @classmethod
    def from_client(cls) -> 'SnsWrapper':
        """
        Create an SnsWrapper instance using a default boto3 client.

        :return: An instance of this class.
        """
        sns_client = boto3.client('sns')
        return cls(sns_client)


    def create_topic(
        self,
        topic_name: str,
        is_fifo: bool = False,
        content_based_deduplication: bool = False
    ) -> str:
        """
        Create an SNS topic.

        :param topic_name: The name of the topic to create.
        :param is_fifo: Whether to create a FIFO topic.
        :param content_based_deduplication: Whether to use content-based deduplication for FIFO topics.
        :return: The ARN of the created topic.
        :raises ClientError: If the topic creation fails.
        """
        try:
            # Add .fifo suffix for FIFO topics
            if is_fifo and not topic_name.endswith('.fifo'):
                topic_name += '.fifo'

            attributes = {}
            if is_fifo:
                attributes['FifoTopic'] = 'true'
                if content_based_deduplication:
                    attributes['ContentBasedDeduplication'] = 'true'

            response = self.sns_client.create_topic(
                Name=topic_name,
                Attributes=attributes
            )

            topic_arn = response['TopicArn']
            logger.info(f"Created topic: {topic_name} with ARN: {topic_arn}")
            return topic_arn

        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code', 'Unknown')
            logger.error(f"Error creating topic {topic_name}: {error_code} - {e}")
            raise



```

- For API details, see
  [CreateTopic](../../../goto/boto3/sns-2010-03-31/CreateTopic.md "../../../goto/boto3/sns-2010-03-31/CreateTopic.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/sns#code-examples").

```
# This class demonstrates how to create an Amazon Simple Notification Service (SNS) topic.
class SNSTopicCreator
  # Initializes an SNS client.
  #
  # Utilizes the default AWS configuration for region and credentials.
  def initialize
    @sns_client = Aws::SNS::Client.new
  end

  # Attempts to create an SNS topic with the specified name.
  #
  # @param topic_name [String] The name of the SNS topic to create.
  # @return [Boolean] true if the topic was successfully created, false otherwise.
  def create_topic(topic_name)
    @sns_client.create_topic(name: topic_name)
    puts "The topic '#{topic_name}' was successfully created."
    true
  rescue Aws::SNS::Errors::ServiceError => e
    # Handles SNS service errors gracefully.
    puts "Error while creating the topic named '#{topic_name}': #{e.message}"
    false
  end
end

# Example usage:
if $PROGRAM_NAME == __FILE__
  topic_name = 'YourTopicName' # Replace with your topic name
  sns_topic_creator = SNSTopicCreator.new

  puts "Creating the topic '#{topic_name}'..."
  unless sns_topic_creator.create_topic(topic_name)
    puts 'The topic was not created. Stopping program.'
    exit 1
  end
end


```

- For more information, see [AWS SDK for Ruby Developer Guide](../../../sdk-for-ruby/v3/developer-guide/sns-example-create-topic.md "../../../sdk-for-ruby/v3/developer-guide/sns-example-create-topic.md").
- For API details, see
  [CreateTopic](../../../goto/SdkForRubyV3/sns-2010-03-31/CreateTopic.md "../../../goto/SdkForRubyV3/sns-2010-03-31/CreateTopic.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/sns#code-examples").

```
async fn make_topic(client: &Client, topic_name: &str) -> Result<(), Error> {
    let resp = client.create_topic().name(topic_name).send().await?;

    println!(
        "Created topic with ARN: {}",
        resp.topic_arn().unwrap_or_default()
    );

    Ok(())
}


```

- For API details, see
  [CreateTopic](https://docs.rs/aws-sdk-sns/latest/aws_sdk_sns/client/struct.Client.html#method.create_topic "https://docs.rs/aws-sdk-sns/latest/aws_sdk_sns/client/struct.Client.html#method.create_topic")
  in _AWS SDK for Rust API reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sns#code-examples").

```
    TRY.
        oo_result = lo_sns->createtopic( iv_name = iv_topic_name ). " oo_result is returned for testing purposes. "
        MESSAGE 'SNS topic created' TYPE 'I'.
      CATCH /aws1/cx_snstopiclimitexcdex.
        MESSAGE 'Unable to create more topics. You have reached the maximum number of topics allowed.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [CreateTopic](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sns#code-examples").

```
import AWSSNS

        let config = try await SNSClient.SNSClientConfiguration(region: region)
        let snsClient = SNSClient(config: config)

        let output = try await snsClient.createTopic(
            input: CreateTopicInput(name: name)
        )

        guard let arn = output.topicArn else {
            print("No topic ARN returned by Amazon SNS.")
            return
        }


```

- For API details, see
  [CreateTopic](<https://sdk.amazonaws.com/swift/api/awssns/latest/documentation/awssns/snsclient/createtopic(input:)> "https://sdk.amazonaws.com/swift/api/awssns/latest/documentation/awssns/snsclient/createtopic(input:)")
  in _AWS SDK for Swift API reference_.

###### Note

You can also use an Amazon SNS topic in a different account, but in that case you might need
to create a policy for topic that grants access permissions to AWS Config. For information on
granting permissions to an Amazon SNS topic, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md "sns-topic-policy.md") and then go to [Step 3: Creating an IAM Role](#gs-cli-create-iamrole "#gs-cli-create-iamrole").

## Step 3: Creating an IAM Role

###### Important

**(Recommended) Use the AWS Config service-linked role**

It is recommended to use the AWS Config service-linked role: `AWSServiceRoleForConfig`. Service-linked roles are predefined and include all the permissions that AWS Config requires to call other AWS services. The AWS Config service-linked role is required for service-linked configuration recorders.

For more information, see [Using Service-Linked Roles for AWS Config](using-service-linked-roles.md "using-service-linked-roles.md").

You can use the IAM console to create an IAM role that grants AWS Config permissions to
access your Amazon S3 bucket, access your Amazon SNS topic, and get configuration details for
supported AWS resources. When you use the console to create an IAM role, AWS Config
automatically attaches the required permissions to the role for you.

###### Note

If you have used an AWS service that uses AWS Config (such as AWS Security Hub or
AWS Control Tower) and an AWS Config role has already been created, you should make sure
that the IAM role you use when setting up AWS Config keeps the same minimum privileges as
the already created AWS Config role in order for the other AWS service to continue to run as
expected.

For example, if AWS Control Tower has an IAM role that allows AWS Config to read Amazon S3
objects, you should guarantee the same permissions are granted within the IAM role you
use when setting up AWS Config. Otherwise, it may interfere with AWS Control Tower's
operations.

For more information about IAM roles for AWS Config, see [AWS Identity and Access Management](security-iam.md "security-iam.md").

###### To create a role for an AWS service

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**,
   and then choose **Create role**.
3. For **Select trusted entity**, choose **AWS
   service**.
4. Choose the use case you want for AWS Config: **Config - Customizable**,
   **Config - Organizations**, **Config**, or
   **Config - Conformance Packs**. Then, choose
   **Next**.
5. On the **Name, review, and create** page, review the details
   about your role, and choose **Create Role**.
   To use an AWS SDK, you must configure it with your credentials. For more
   information, see [The shared config and credentials
   files](../../../sdkref/latest/guide/creds-config-files.md "../../../sdkref/latest/guide/creds-config-files.md") in the _AWS SDKs and Tools Reference Guide_.

The following code examples show how to use `CreateRole`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples").

```
    /// <summary>
    /// Create a new IAM role.
    /// </summary>
    /// <param name="roleName">The name of the IAM role.</param>
    /// <param name="rolePolicyDocument">The name of the IAM policy document
    /// for the new role.</param>
    /// <returns>The Amazon Resource Name (ARN) of the role.</returns>
    public async Task<string> CreateRoleAsync(string roleName, string rolePolicyDocument)
    {
        var request = new CreateRoleRequest
        {
            RoleName = roleName,
            AssumeRolePolicyDocument = rolePolicyDocument,
        };

        var response = await _IAMService.CreateRoleAsync(request);
        return response.Role.Arn;
    }



```

- For API details, see
  [CreateRole](../../../goto/DotNetSDKV3/iam-2010-05-08/CreateRole.md "../../../goto/DotNetSDKV3/iam-2010-05-08/CreateRole.md")
  in _AWS SDK for .NET API Reference_.

Bash

**AWS CLI with Bash script**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/iam#code-examples").

```
###############################################################################
# function errecho
#
# This function outputs everything sent to it to STDERR (standard error output).
###############################################################################
function errecho() {
  printf "%s\n" "$*" 1>&2
}

###############################################################################
# function iam_create_role
#
# This function creates an IAM role.
#
# Parameters:
#       -n role_name -- The name of the IAM role.
#       -p policy_json -- The assume role policy document.
#
# Returns:
#       The ARN of the role.
#     And:
#       0 - If successful.
#       1 - If it fails.
###############################################################################
function iam_create_role() {
  local role_name policy_document response
  local option OPTARG # Required to use getopts command in a function.

  # bashsupport disable=BP5008
  function usage() {
    echo "function iam_create_user_access_key"
    echo "Creates an AWS Identity and Access Management (IAM) role."
    echo "  -n role_name   The name of the IAM role."
    echo "  -p policy_json -- The assume role policy document."
    echo ""
  }

  # Retrieve the calling parameters.
  while getopts "n:p:h" option; do
    case "${option}" in
      n) role_name="${OPTARG}" ;;
      p) policy_document="${OPTARG}" ;;
      h)
        usage
        return 0
        ;;
      \?)
        echo "Invalid parameter"
        usage
        return 1
        ;;
    esac
  done
  export OPTIND=1

  if [[ -z "$role_name" ]]; then
    errecho "ERROR: You must provide a role name with the -n parameter."
    usage
    return 1
  fi

  if [[ -z "$policy_document" ]]; then
    errecho "ERROR: You must provide a policy document with the -p parameter."
    usage
    return 1
  fi

  response=$(aws iam create-role \
    --role-name "$role_name" \
    --assume-role-policy-document "$policy_document" \
    --output text \
    --query Role.Arn)

  local error_code=${?}

  if [[ $error_code -ne 0 ]]; then
    aws_cli_error_log $error_code
    errecho "ERROR: AWS reports create-role operation failed.\n$response"
    return 1
  fi

  echo "$response"

  return 0
}


```

- For API details, see
  [CreateRole](../../../goto/aws-cli/iam-2010-05-08/CreateRole.md "../../../goto/aws-cli/iam-2010-05-08/CreateRole.md")
  in _AWS CLI Command Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iam#code-examples").

```
bool AwsDoc::IAM::createIamRole(
        const Aws::String &roleName,
        const Aws::String &policy,
        const Aws::Client::ClientConfiguration &clientConfig) {
    Aws::IAM::IAMClient client(clientConfig);
    Aws::IAM::Model::CreateRoleRequest request;

    request.SetRoleName(roleName);
    request.SetAssumeRolePolicyDocument(policy);

    Aws::IAM::Model::CreateRoleOutcome outcome = client.CreateRole(request);
    if (!outcome.IsSuccess()) {
        std::cerr << "Error creating role. " <<
                  outcome.GetError().GetMessage() << std::endl;
    }
    else {
        const Aws::IAM::Model::Role iamRole = outcome.GetResult().GetRole();
        std::cout << "Created role " << iamRole.GetRoleName() << "\n";
        std::cout << "ID: " << iamRole.GetRoleId() << "\n";
        std::cout << "ARN: " << iamRole.GetArn() << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [CreateRole](../../../goto/SdkForCpp/iam-2010-05-08/CreateRole.md "../../../goto/SdkForCpp/iam-2010-05-08/CreateRole.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**Example 1: To create an IAM role**

The following `create-role` command creates a role named `Test-Role` and attaches a trust policy to it.

```
`aws iam create-role \
 --role-name `Test-Role` \
 --assume-role-policy-document `file://Test-Role-Trust-Policy.json``

```

Output:

```
{
    "Role": {
        "AssumeRolePolicyDocument": "<URL-encoded-JSON>",
        "RoleId": "AKIAIOSFODNN7EXAMPLE",
        "CreateDate": "2013-06-07T20:43:32.821Z",
        "RoleName": "Test-Role",
        "Path": "/",
        "Arn": "arn:aws:iam::123456789012:role/Test-Role"
    }
}
```

The trust policy is defined as a JSON document in the _Test-Role-Trust-Policy.json_ file. (The file name and extension do not have significance.) The trust policy must specify a principal.

To attach a permissions policy to a role, use the `put-role-policy` command.

For more information, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the _AWS IAM User Guide_.

**Example 2: To create an IAM role with specified maximum session duration**

The following `create-role` command creates a role named `Test-Role` and sets a maximum session duration of 7200 seconds (2 hours).

```
`aws iam create-role \
 --role-name `Test-Role` \
 --assume-role-policy-document `file://Test-Role-Trust-Policy.json` \
 --max-session-duration `7200``

```

Output:

```
{
    "Role": {
        "Path": "/",
        "RoleName": "Test-Role",
        "RoleId": "AKIAIOSFODNN7EXAMPLE",
        "Arn": "arn:aws:iam::12345678012:role/Test-Role",
        "CreateDate": "2023-05-24T23:50:25+00:00",
        "AssumeRolePolicyDocument": {
            "Version":"2012-10-17",
            "Statement": [
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::12345678012:root"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    }
}
```

For more information, see [Modifying a role maximum session duration (AWS API)](../../../IAM/latest/UserGuide/roles-managingrole-editing-api.md#roles-modify_max-session-duration-api "../../../IAM/latest/UserGuide/roles-managingrole-editing-api.md#roles-modify_max-session-duration-api") in the _AWS IAM User Guide_.

**Example 3: To create an IAM Role with tags**

The following command creates an IAM Role `Test-Role` with tags. This example uses the `--tags` parameter flag with the following JSON-formatted tags: `'{"Key": "Department", "Value": "Accounting"}' '{"Key": "Location", "Value": "Seattle"}'`. Alternatively, the `--tags` flag can be used with tags in the shorthand format: `'Key=Department,Value=Accounting Key=Location,Value=Seattle'`.

```
`aws iam create-role \
 --role-name `Test-Role` \
 --assume-role-policy-document `file://Test-Role-Trust-Policy.json` \
 --tags '`{"Key": "Department", "Value": "Accounting"}`' '`{"Key": "Location", "Value": "Seattle"}`'`

```

Output:

```
{
    "Role": {
        "Path": "/",
        "RoleName": "Test-Role",
        "RoleId": "AKIAIOSFODNN7EXAMPLE",
        "Arn": "arn:aws:iam::123456789012:role/Test-Role",
        "CreateDate": "2023-05-25T23:29:41+00:00",
        "AssumeRolePolicyDocument": {
            "Version":"2012-10-17",
            "Statement": [
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::123456789012:root"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        },
        "Tags": [
            {
                "Key": "Department",
                "Value": "Accounting"
            },
            {
                "Key": "Location",
                "Value": "Seattle"
            }
        ]
    }
}
```

For more information, see [Tagging IAM roles](../../../IAM/latest/UserGuide/id_tags_roles.md "../../../IAM/latest/UserGuide/id_tags_roles.md") in the _AWS IAM User Guide_.

- For API details, see
  [CreateRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html")
  in _AWS CLI Command Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples").

```

import (
	"context"
	"encoding/json"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/iam"
	"github.com/aws/aws-sdk-go-v2/service/iam/types"
)

// RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
// used in the examples.
// It contains an IAM service client that is used to perform role actions.
type RoleWrapper struct {
	IamClient *iam.Client
}



// CreateRole creates a role that trusts a specified user. The trusted user can assume
// the role to acquire its permissions.
// PolicyDocument shows how to work with a policy document as a data structure and
// serialize it to JSON by using Go's JSON marshaler.
func (wrapper RoleWrapper) CreateRole(ctx context.Context, roleName string, trustedUserArn string) (*types.Role, error) {
	var role *types.Role
	trustPolicy := PolicyDocument{
		Version: "2012-10-17",
		Statement: []PolicyStatement{{
			Effect:    "Allow",
			Principal: map[string]string{"AWS": trustedUserArn},
			Action:    []string{"sts:AssumeRole"},
		}},
	}
	policyBytes, err := json.Marshal(trustPolicy)
	if err != nil {
		log.Printf("Couldn't create trust policy for %v. Here's why: %v\n", trustedUserArn, err)
		return nil, err
	}
	result, err := wrapper.IamClient.CreateRole(ctx, &iam.CreateRoleInput{
		AssumeRolePolicyDocument: aws.String(string(policyBytes)),
		RoleName:                 aws.String(roleName),
	})
	if err != nil {
		log.Printf("Couldn't create role %v. Here's why: %v\n", roleName, err)
	} else {
		role = result.Role
	}
	return role, err
}



```

- For API details, see
  [CreateRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateRole "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateRole")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iam#code-examples").

```
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import software.amazon.awssdk.services.iam.model.CreateRoleRequest;
import software.amazon.awssdk.services.iam.model.CreateRoleResponse;
import software.amazon.awssdk.services.iam.model.IamException;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.iam.IamClient;
import java.io.FileReader;

/*
*   This example requires a trust policy document. For more information, see:
*   https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/
*
*
*  In addition, set up your development environment, including your credentials.
*
*  For information, see this documentation topic:
*
*  https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class CreateRole {
    public static void main(String[] args) throws Exception {
        final String usage = """
                Usage:
                    <rolename> <fileLocation>\s

                Where:
                    rolename - The name of the role to create.\s
                    fileLocation - The location of the JSON document that represents the trust policy.\s
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String rolename = args[0];
        String fileLocation = args[1];
        Region region = Region.AWS_GLOBAL;
        IamClient iam = IamClient.builder()
                .region(region)
                .build();

        String result = createIAMRole(iam, rolename, fileLocation);
        System.out.println("Successfully created user: " + result);
        iam.close();
    }

    public static String createIAMRole(IamClient iam, String rolename, String fileLocation) throws Exception {
        try {
            JSONObject jsonObject = (JSONObject) readJsonSimpleDemo(fileLocation);
            CreateRoleRequest request = CreateRoleRequest.builder()
                    .roleName(rolename)
                    .assumeRolePolicyDocument(jsonObject.toJSONString())
                    .description("Created using the AWS SDK for Java")
                    .build();

            CreateRoleResponse response = iam.createRole(request);
            System.out.println("The ARN of the role is " + response.role().arn());

        } catch (IamException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }

    public static Object readJsonSimpleDemo(String filename) throws Exception {
        FileReader reader = new FileReader(filename);
        JSONParser jsonParser = new JSONParser();
        return jsonParser.parse(reader);
    }
}


```

- For API details, see
  [CreateRole](../../../goto/SdkForJavaV2/iam-2010-05-08/CreateRole.md "../../../goto/SdkForJavaV2/iam-2010-05-08/CreateRole.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

Create the role.

```
import { CreateRoleCommand, IAMClient } from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} roleName
 */
export const createRole = (roleName) => {
  const command = new CreateRoleCommand({
    AssumeRolePolicyDocument: JSON.stringify({
      Version: "2012-10-17",
      Statement: [
        {
          Effect: "Allow",
          Principal: {
            Service: "lambda.amazonaws.com",
          },
          Action: "sts:AssumeRole",
        },
      ],
    }),
    RoleName: roleName,
  });

  return client.send(command);
};


```

- For API details, see
  [CreateRole](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/CreateRoleCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/CreateRoleCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/iam#code-examples").

```
$uuid = uniqid();
$service = new IAMService();

$assumeRolePolicyDocument = "{
                \"Version\": \"2012-10-17\",
                \"Statement\": [{
                    \"Effect\": \"Allow\",
                    \"Principal\": {\"AWS\": \"{$user['Arn']}\"},
                    \"Action\": \"sts:AssumeRole\"
                }]
            }";
$assumeRoleRole = $service->createRole("iam_demo_role_$uuid", $assumeRolePolicyDocument);
echo "Created role: {$assumeRoleRole['RoleName']}\n";

    /**
     * @param string $roleName
     * @param string $rolePolicyDocument
     * @return array
     * @throws AwsException
     */
    public function createRole(string $roleName, string $rolePolicyDocument)
    {
        $result = $this->customWaiter(function () use ($roleName, $rolePolicyDocument) {
            return $this->iamClient->createRole([
                'AssumeRolePolicyDocument' => $rolePolicyDocument,
                'RoleName' => $roleName,
            ]);
        });
        return $result['Role'];
    }



```

- For API details, see
  [CreateRole](../../../goto/SdkForPHPV3/iam-2010-05-08/CreateRole.md "../../../goto/SdkForPHPV3/iam-2010-05-08/CreateRole.md")
  in _AWS SDK for PHP API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a new role named `MyNewRole` and attaches to it the policy found in the file `NewRoleTrustPolicy.json`. Note that you must use the `-Raw` switch parameter to successfully process the JSON policy file. The policy document displayed in the output is URL encoded. It is decoded in this example with the `UrlDecode` .NET method.**

```
$results = New-IAMRole -AssumeRolePolicyDocument (Get-Content -raw NewRoleTrustPolicy.json) -RoleName MyNewRole
$results

```

**Output:**

```
Arn                      : arn:aws:iam::123456789012:role/MyNewRole
AssumeRolePolicyDocument : %7B%0D%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%0D%0A%20%20%22Statement%22
                           %3A%20%5B%0D%0A%20%20%20%20%7B%0D%0A%20%20%20%20%20%20%22Sid%22%3A%20%22%22%2C
                           %0D%0A%20%20%20%20%20%20%22Effect%22%3A%20%22Allow%22%2C%0D%0A%20%20%20%20%20%20
                           %22Principal%22%3A%20%7B%0D%0A%20%20%20%20%20%20%20%20%22AWS%22%3A%20%22arn%3Aaws
                           %3Aiam%3A%3A123456789012%3ADavid%22%0D%0A%20%20%20%20%20%20%7D%2C%0D%0A%20%20%20
                           %20%20%20%22Action%22%3A%20%22sts%3AAssumeRole%22%0D%0A%20%20%20%20%7D%0D%0A%20
                           %20%5D%0D%0A%7D
CreateDate               : 4/15/2015 11:04:23 AM
Path                     : /
RoleId                   : V5PAJI2KPN4EAEXAMPLE1
RoleName                 : MyNewRole

[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.AssumeRolePolicyDocument)
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:David"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- For API details, see
  [CreateRole](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a new role named `MyNewRole` and attaches to it the policy found in the file `NewRoleTrustPolicy.json`. Note that you must use the `-Raw` switch parameter to successfully process the JSON policy file. The policy document displayed in the output is URL encoded. It is decoded in this example with the `UrlDecode` .NET method.**

```
$results = New-IAMRole -AssumeRolePolicyDocument (Get-Content -raw NewRoleTrustPolicy.json) -RoleName MyNewRole
$results

```

**Output:**

```
Arn                      : arn:aws:iam::123456789012:role/MyNewRole
AssumeRolePolicyDocument : %7B%0D%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%0D%0A%20%20%22Statement%22
                           %3A%20%5B%0D%0A%20%20%20%20%7B%0D%0A%20%20%20%20%20%20%22Sid%22%3A%20%22%22%2C
                           %0D%0A%20%20%20%20%20%20%22Effect%22%3A%20%22Allow%22%2C%0D%0A%20%20%20%20%20%20
                           %22Principal%22%3A%20%7B%0D%0A%20%20%20%20%20%20%20%20%22AWS%22%3A%20%22arn%3Aaws
                           %3Aiam%3A%3A123456789012%3ADavid%22%0D%0A%20%20%20%20%20%20%7D%2C%0D%0A%20%20%20
                           %20%20%20%22Action%22%3A%20%22sts%3AAssumeRole%22%0D%0A%20%20%20%20%7D%0D%0A%20
                           %20%5D%0D%0A%7D
CreateDate               : 4/15/2015 11:04:23 AM
Path                     : /
RoleId                   : V5PAJI2KPN4EAEXAMPLE1
RoleName                 : MyNewRole

[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.AssumeRolePolicyDocument)
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:David"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- For API details, see
  [CreateRole](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples").

```
def create_role(role_name, allowed_services):
    """
    Creates a role that lets a list of specified services assume the role.

    :param role_name: The name of the role.
    :param allowed_services: The services that can assume the role.
    :return: The newly created role.
    """
    trust_policy = {
        "Version":"2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": service},
                "Action": "sts:AssumeRole",
            }
            for service in allowed_services
        ],
    }

    try:
        role = iam.create_role(
            RoleName=role_name, AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
        logger.info("Created role %s.", role.name)
    except ClientError:
        logger.exception("Couldn't create role %s.", role_name)
        raise
    else:
        return role




```

- For API details, see
  [CreateRole](../../../goto/boto3/iam-2010-05-08/CreateRole.md "../../../goto/boto3/iam-2010-05-08/CreateRole.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples").

```
  # Creates a role and attaches policies to it.
  #
  # @param role_name [String] The name of the role.
  # @param assume_role_policy_document [Hash] The trust relationship policy document.
  # @param policy_arns [Array<String>] The ARNs of the policies to attach.
  # @return [String, nil] The ARN of the new role if successful, or nil if an error occurred.
  def create_role(role_name, assume_role_policy_document, policy_arns)
    response = @iam_client.create_role(
      role_name: role_name,
      assume_role_policy_document: assume_role_policy_document.to_json
    )
    role_arn = response.role.arn

    policy_arns.each do |policy_arn|
      @iam_client.attach_role_policy(
        role_name: role_name,
        policy_arn: policy_arn
      )
    end

    role_arn
  rescue Aws::IAM::Errors::ServiceError => e
    @logger.error("Error creating role: #{e.message}")
    nil
  end


```

- For API details, see
  [CreateRole](../../../goto/SdkForRubyV3/iam-2010-05-08/CreateRole.md "../../../goto/SdkForRubyV3/iam-2010-05-08/CreateRole.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples").

```
pub async fn create_role(
    client: &iamClient,
    role_name: &str,
    role_policy_document: &str,
) -> Result<Role, iamError> {
    let response: CreateRoleOutput = loop {
        if let Ok(response) = client
            .create_role()
            .role_name(role_name)
            .assume_role_policy_document(role_policy_document)
            .send()
            .await
        {
            break response;
        }
    };

    Ok(response.role.unwrap())
}


```

- For API details, see
  [CreateRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_role "https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_role")
  in _AWS SDK for Rust API reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/iam#code-examples").

```
    TRY.
        oo_result = lo_iam->createrole(
          iv_rolename = iv_role_name
          iv_assumerolepolicydocument = iv_assume_role_policy_document ).
        MESSAGE 'Role created successfully.' TYPE 'I'.
      CATCH /aws1/cx_iamentityalrdyexex.
        MESSAGE 'Role already exists.' TYPE 'E'.
      CATCH /aws1/cx_iammalformedplydocex.
        MESSAGE 'Assume role policy document is malformed.' TYPE 'E'.
      CATCH /aws1/cx_iamlimitexceededex.
        MESSAGE 'Role limit exceeded.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [CreateRole](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples").

```
import AWSIAM
import AWSS3


    public func createRole(name: String, policyDocument: String) async throws -> String {
        let input = CreateRoleInput(
            assumeRolePolicyDocument: policyDocument,
            roleName: name
        )
        do {
            let output = try await client.createRole(input: input)
            guard let role = output.role else {
                throw ServiceHandlerError.noSuchRole
            }
            guard let id = role.roleId else {
                throw ServiceHandlerError.noSuchRole
            }
            return id
        } catch {
            print("ERROR: createRole:", dump(error))
            throw error
        }
    }


```

- For API details, see
  [CreateRole](<https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/createrole(input:)> "https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/createrole(input:)")
  in _AWS SDK for Swift API reference_.
