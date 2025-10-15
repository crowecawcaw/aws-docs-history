# Use `HeadBucket` with an AWS SDK or CLI

The following code examples show how to use `HeadBucket`.


Bash


**AWS CLI with Bash script**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/s3#code-examples").
 



```
###############################################################################
# function bucket_exists
#
# This function checks to see if the specified bucket already exists.
#
# Parameters:
#       $1 - The name of the bucket to check.
#
# Returns:
#       0 - If the bucket already exists.
#       1 - If the bucket doesn't exist.
###############################################################################
function bucket_exists() {
  local bucket_name
  bucket_name=$1

  # Check whether the bucket already exists.
  # We suppress all output - we're interested only in the return code.

  if aws s3api head-bucket \
    --bucket "$bucket_name" \
    >/dev/null 2>&1; then
    return 0 # 0 in Bash script means true.
  else
    return 1 # 1 in Bash script means false.
  fi
}


```


* For API details, see
 [HeadBucket](https://docs.aws.amazon.com/goto/aws-cli/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/aws-cli/s3-2006-03-01/HeadBucket")
 in *AWS CLI Command Reference*.




CLI


**AWS CLI**

The following command verifies access to a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api head-bucket --bucket `amzn-s3-demo-bucket``

```

If the bucket exists and you have access to it, no output is returned. Otherwise, an error message will be shown. For example:



```
A client error (404) occurred when calling the HeadBucket operation: Not Found
```


* For API details, see
 [HeadBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-bucket.html")
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



// BucketExists checks whether a bucket exists in the current account.
func (basics BucketBasics) BucketExists(ctx context.Context, bucketName string) (bool, error) {
	_, err := basics.S3Client.HeadBucket(ctx, &s3.HeadBucketInput{
		Bucket: aws.String(bucketName),
	})
	exists := true
	if err != nil {
		var apiError smithy.APIError
		if errors.As(err, &apiError) {
			switch apiError.(type) {
			case *types.NotFound:
				log.Printf("Bucket %v is available.\n", bucketName)
				exists = false
				err = nil
			default:
				log.Printf("Either you don't have access to bucket %v or another error occurred. "+
					"Here's what happened: %v\n", bucketName, err)
			}
		}
	} else {
		log.Printf("Bucket %v exists and you already own it.", bucketName)
	}

	return exists, err
}



```


* For API details, see
 [HeadBucket](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.HeadBucket "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.HeadBucket")
 in *AWS SDK for Go API Reference*.




PowerShell


**Tools for PowerShell V5**

**Example 1: This command returns the output with HTTP status code 200 OK for existing bucket when user has permission to access it. BucketArn parameter is only supported for S3 directory buckets.**



```
Get-S3HeadBucket -BucketName amzn-s3-demo-bucket

```

**Output:**



```
AccessPointAlias   : False
BucketArn          :
BucketLocationName : 
BucketLocationType : 
BucketRegion       : us-east-2
ResponseMetadata   : Amazon.Runtime.ResponseMetadata
ContentLength      : 0
HttpStatusCode     : OK
```

**Example 2: This command throws error with HTTP status code NotFound for non-existent bucket.**



```
Get-S3HeadBucket -BucketName amzn-s3-non-existing-bucket

```

**Output:**



```
Get-S3HeadBucket: Error making request with Error Code NotFound and Http Status Code NotFound. No further error information was returned by the service.
```

**Example 3: This command throws error with HTTP status code Forbidden for existing bucket where user does not have permission to access it.**



```
Get-S3HeadBucket -BucketName amzn-s3-no-access-bucket

```

**Output:**



```
Get-S3HeadBucket: Error making request with Error Code Forbidden and Http Status Code Forbidden. No further error information was returned by the service.
```


* For API details, see
 [HeadBucket](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
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


    def exists(self):
        """
        Determine whether the bucket exists and you have access to it.

        :return: True when the bucket exists; otherwise, False.
        """
        try:
            self.bucket.meta.client.head_bucket(Bucket=self.bucket.name)
            logger.info("Bucket %s exists.", self.bucket.name)
            exists = True
        except ClientError:
            logger.warning(
                "Bucket %s doesn't exist or you don't have access to it.",
                self.bucket.name,
            )
            exists = False
        return exists



```


* For API details, see
 [HeadBucket](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/HeadBucket")
 in *AWS SDK for Python (Boto3) API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
