# Use `GetObjectLockConfiguration` with an AWS SDK or CLI

The following code examples show how to use `GetObjectLockConfiguration`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Lock Amazon S3 objects](s3_example_s3_Scenario_ObjectLock_section.md "s3_example_s3_Scenario_ObjectLock_section.md")

.NET


**SDK for .NET**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3/scenarios/S3ObjectLockScenario#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3/scenarios/S3ObjectLockScenario#code-examples").
 



```
    /// <summary>
    /// Get the object lock configuration details for an S3 bucket.
    /// </summary>
    /// <param name="bucketName">The bucket to get details.</param>
    /// <returns>The bucket's object lock configuration details.</returns>
    public async Task<ObjectLockConfiguration> GetBucketObjectLockConfiguration(string bucketName)
    {
        try
        {
            var request = new GetObjectLockConfigurationRequest()
            {
                BucketName = bucketName
            };

            var response = await _amazonS3.GetObjectLockConfigurationAsync(request);
            Console.WriteLine($"\tBucket object lock config for {bucketName} in {bucketName}: " +
                              $"\n\tEnabled: {response.ObjectLockConfiguration.ObjectLockEnabled}" +
                              $"\n\tRule: {response.ObjectLockConfiguration.Rule?.DefaultRetention}");

            return response.ObjectLockConfiguration;
        }
        catch (AmazonS3Exception ex)
        {
            Console.WriteLine($"\tUnable to fetch object lock config: '{ex.Message}'");
            return new ObjectLockConfiguration();
        }
    }


```


* For API details, see
 [GetObjectLockConfiguration](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectLockConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectLockConfiguration")
 in *AWS SDK for .NET API Reference*.




CLI


**AWS CLI**

**To retrieve an object lock configuration for a bucket**


The following `get-object-lock-configuration` example retrieves the object lock configuration for the specified bucket.



```
`aws s3api get-object-lock-configuration \
 --bucket `amzn-s3-demo-bucket-with-object-lock``

```

Output:



```
{
    "ObjectLockConfiguration": {
        "ObjectLockEnabled": "Enabled",
        "Rule": {
            "DefaultRetention": {
                "Mode": "COMPLIANCE",
                "Days": 50
            }
        }
    }
}
```


* For API details, see
 [GetObjectLockConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-lock-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-lock-configuration.html")
 in *AWS CLI Command Reference*.




Go


**SDK for Go V2**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/s3_object_lock#code-examples").
 



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



// GetObjectLockConfiguration retrieves the object lock configuration for an S3 bucket.
func (actor S3Actions) GetObjectLockConfiguration(ctx context.Context, bucket string) (*types.ObjectLockConfiguration, error) {
	var lockConfig *types.ObjectLockConfiguration
	input := &s3.GetObjectLockConfigurationInput{
		Bucket: aws.String(bucket),
	}

	output, err := actor.S3Client.GetObjectLockConfiguration(ctx, input)
	if err != nil {
		var noBucket *types.NoSuchBucket
		var apiErr *smithy.GenericAPIError
		if errors.As(err, &noBucket) {
			log.Printf("Bucket %s does not exist.\n", bucket)
			err = noBucket
		} else if errors.As(err, &apiErr) && apiErr.ErrorCode() == "ObjectLockConfigurationNotFoundError" {
			log.Printf("Bucket %s does not have an object lock configuration.\n", bucket)
			err = nil
		}
	} else {
		lockConfig = output.ObjectLockConfiguration
	}

	return lockConfig, err
}



```


* For API details, see
 [GetObjectLockConfiguration](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectLockConfiguration "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#Client.GetObjectLockConfiguration")
 in *AWS SDK for Go API Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 



```
    // Get the object lock configuration details for an S3 bucket.
    public void getBucketObjectLockConfiguration(String bucketName) {
        GetObjectLockConfigurationRequest objectLockConfigurationRequest = GetObjectLockConfigurationRequest.builder()
            .bucket(bucketName)
            .build();

        GetObjectLockConfigurationResponse response = getClient().getObjectLockConfiguration(objectLockConfigurationRequest);
        System.out.println("Bucket object lock config for "+bucketName +":  ");
        System.out.println("\tEnabled: "+response.objectLockConfiguration().objectLockEnabled());
        System.out.println("\tRule: "+ response.objectLockConfiguration().rule().defaultRetention());
    }


```


* For API details, see
 [GetObjectLockConfiguration](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectLockConfiguration")
 in *AWS SDK for Java 2.x API Reference*.




JavaScript


**SDK for JavaScript (v3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/s3#code-examples").
 



```
import {
  GetObjectLockConfigurationCommand,
  S3Client,
  S3ServiceException,
} from "@aws-sdk/client-s3";

/**
 * Gets the Object Lock configuration for a bucket.
 * @param {{ bucketName: string }}
 */
export const main = async ({ bucketName }) => {
  const client = new S3Client({});

  try {
    const { ObjectLockConfiguration } = await client.send(
      new GetObjectLockConfigurationCommand({
        Bucket: bucketName,
        // Optionally, you can provide additional parameters
        // ExpectedBucketOwner: "<account ID that is expected to own the bucket>",
      }),
    );
    console.log(
      `Object Lock Configuration:\n${JSON.stringify(ObjectLockConfiguration)}`,
    );
  } catch (caught) {
    if (
      caught instanceof S3ServiceException &&
      caught.name === "NoSuchBucket"
    ) {
      console.error(
        `Error from S3 while getting object lock configuration for ${bucketName}. The bucket doesn't exist.`,
      );
    } else if (caught instanceof S3ServiceException) {
      console.error(
        `Error from S3 while getting object lock configuration for ${bucketName}.  ${caught.name}: ${caught.message}`,
      );
    } else {
      throw caught;
    }
  }
};

// Call function if run directly
import { parseArgs } from "node:util";
import {
  isMain,
  validateArgs,
} from "@aws-doc-sdk-examples/lib/utils/util-node.js";

const loadArgs = () => {
  const options = {
    bucketName: {
      type: "string",
      required: true,
    },
  };
  const results = parseArgs({ options });
  const { errors } = validateArgs({ options }, results);
  return { errors, results };
};

if (isMain(import.meta.url)) {
  const { errors, results } = loadArgs();
  if (!errors) {
    main(results.values);
  } else {
    console.error(errors.join("\n"));
  }
}


```


* For API details, see
 [GetObjectLockConfiguration](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/GetObjectLockConfigurationCommand "https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/GetObjectLockConfigurationCommand")
 in *AWS SDK for JavaScript API Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the value 'Enabled' if Object lock configuration is enabled for the given S3 bucket.**



```
Get-S3ObjectLockConfiguration -BucketName 'amzn-s3-demo-bucket' -Select ObjectLockConfiguration.ObjectLockEnabled

```

**Output:**



```
Value
-----
Enabled
```


* For API details, see
 [GetObjectLockConfiguration](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the value 'Enabled' if Object lock configuration is enabled for the given S3 bucket.**



```
Get-S3ObjectLockConfiguration -BucketName 'amzn-s3-demo-bucket' -Select ObjectLockConfiguration.ObjectLockEnabled

```

**Output:**



```
Value
-----
Enabled
```


* For API details, see
 [GetObjectLockConfiguration](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




Python


**SDK for Python (Boto3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/object-locking#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/object-locking#code-examples").
 


Get the object lock configuration.



```
def is_object_lock_enabled(s3_client, bucket: str) -> bool:
    """
    Check if object lock is enabled for a bucket.

    Args:
        s3_client: Boto3 S3 client.
        bucket: The name of the bucket to check.

    Returns:
        True if object lock is enabled, False otherwise.
    """
    try:
        response = s3_client.get_object_lock_configuration(Bucket=bucket)
        return (
            "ObjectLockConfiguration" in response
            and response["ObjectLockConfiguration"]["ObjectLockEnabled"] == "Enabled"
        )
    except s3_client.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "ObjectLockConfigurationNotFoundError":
            return False
        else:
            raise




```


* For API details, see
 [GetObjectLockConfiguration](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectLockConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectLockConfiguration")
 in *AWS SDK for Python (Boto3) API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
