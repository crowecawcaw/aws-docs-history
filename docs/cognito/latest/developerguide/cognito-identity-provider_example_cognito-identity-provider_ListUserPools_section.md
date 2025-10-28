# Use `ListUserPools` with an AWS SDK or CLI

The following code examples show how to use `ListUserPools`.

.NET

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/Cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/Cognito#code-examples").

```
    /// <summary>
    /// List the Amazon Cognito user pools for an account.
    /// </summary>
    /// <returns>A list of UserPoolDescriptionType objects.</returns>
    public async Task<List<UserPoolDescriptionType>> ListUserPoolsAsync()
    {
        var userPools = new List<UserPoolDescriptionType>();

        var userPoolsPaginator = _cognitoService.Paginators.ListUserPools(new ListUserPoolsRequest());

        await foreach (var response in userPoolsPaginator.Responses)
        {
            userPools.AddRange(response.UserPools);
        }

        return userPools;
    }



```

- For API details, see
  [ListUserPools](../../../goto/DotNetSDKV4/cognito-idp-2016-04-18/ListUserPools.md "../../../goto/DotNetSDKV4/cognito-idp-2016-04-18/ListUserPools.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To list user pools**

The following `list-user-pools` example lists 3 of the available user pools in the AWS account of the current CLI credentials.

```
`aws cognito-idp list-user-pools \
 --max-results `3``

```

Output:

```
{
    "NextToken": "[Pagination token]",
    "UserPools": [
        {
            "CreationDate": 1681502497.741,
            "Id": "us-west-2_EXAMPLE1",
            "LambdaConfig": {
                "CustomMessage": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "PreSignUp": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "PreTokenGeneration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "PreTokenGenerationConfig": {
                    "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                    "LambdaVersion": "V1_0"
                }
            },
            "LastModifiedDate": 1681502497.741,
            "Name": "user pool 1"
        },
        {
            "CreationDate": 1686064178.717,
            "Id": "us-west-2_EXAMPLE2",
            "LambdaConfig": {
            },
            "LastModifiedDate": 1686064178.873,
            "Name": "user pool 2"
        },
        {
            "CreationDate": 1627681712.237,
            "Id": "us-west-2_EXAMPLE3",
            "LambdaConfig": {
                "UserMigration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction"
            },
            "LastModifiedDate": 1678486942.479,
            "Name": "user pool 3"
        }
    ]
}
```

For more information, see [Amazon Cognito user pools](cognito-user-pools.md "cognito-user-pools.md") in the _Amazon Cognito Developer Guide_.

- For API details, see
  [ListUserPools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pools.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pools.html")
  in _AWS CLI Command Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/cognito#code-examples").

```

package main

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
)

// main uses the AWS SDK for Go V2 to create an Amazon Simple Notification Service
// (Amazon SNS) client and list the topics in your account.
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
	cognitoClient := cognitoidentityprovider.NewFromConfig(sdkConfig)
	fmt.Println("Let's list the user pools for your account.")
	var pools []types.UserPoolDescriptionType
	paginator := cognitoidentityprovider.NewListUserPoolsPaginator(
		cognitoClient, &cognitoidentityprovider.ListUserPoolsInput{MaxResults: aws.Int32(10)})
	for paginator.HasMorePages() {
		output, err := paginator.NextPage(ctx)
		if err != nil {
			log.Printf("Couldn't get user pools. Here's why: %v\n", err)
		} else {
			pools = append(pools, output.UserPools...)
		}
	}
	if len(pools) == 0 {
		fmt.Println("You don't have any user pools!")
	} else {
		for _, pool := range pools {
			fmt.Printf("\t%v: %v\n", *pool.Name, *pool.Id)
		}
	}
}



```

- For API details, see
  [ListUserPools](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ListUserPools "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ListUserPools")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cognito#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cognitoidentityprovider.CognitoIdentityProviderClient;
import software.amazon.awssdk.services.cognitoidentityprovider.model.CognitoIdentityProviderException;
import software.amazon.awssdk.services.cognitoidentityprovider.model.ListUserPoolsResponse;
import software.amazon.awssdk.services.cognitoidentityprovider.model.ListUserPoolsRequest;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class ListUserPools {
    public static void main(String[] args) {
        CognitoIdentityProviderClient cognitoClient = CognitoIdentityProviderClient.builder()
                .region(Region.US_EAST_1)
                .build();

        listAllUserPools(cognitoClient);
        cognitoClient.close();
    }

    public static void listAllUserPools(CognitoIdentityProviderClient cognitoClient) {
        try {
            ListUserPoolsRequest request = ListUserPoolsRequest.builder()
                    .maxResults(10)
                    .build();

            ListUserPoolsResponse response = cognitoClient.listUserPools(request);
            response.userPools().forEach(userpool -> {
                System.out.println("User pool " + userpool.name() + ", User ID " + userpool.id());
            });

        } catch (CognitoIdentityProviderException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [ListUserPools](../../../goto/SdkForJavaV2/cognito-idp-2016-04-18/ListUserPools.md "../../../goto/SdkForJavaV2/cognito-idp-2016-04-18/ListUserPools.md")
  in _AWS SDK for Java 2.x API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/cognitoidentityprovider#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/cognitoidentityprovider#code-examples").

```
async fn show_pools(client: &Client) -> Result<(), Error> {
    let response = client.list_user_pools().max_results(10).send().await?;
    let pools = response.user_pools();
    println!("User pools:");
    for pool in pools {
        println!("  ID:              {}", pool.id().unwrap_or_default());
        println!("  Name:            {}", pool.name().unwrap_or_default());
        println!("  Lambda Config:   {:?}", pool.lambda_config().unwrap());
        println!(
            "  Last modified:   {}",
            pool.last_modified_date().unwrap().to_chrono_utc()?
        );
        println!(
            "  Creation date:   {:?}",
            pool.creation_date().unwrap().to_chrono_utc()
        );
        println!();
    }
    println!("Next token: {}", response.next_token().unwrap_or_default());

    Ok(())
}


```

- For API details, see
  [ListUserPools](https://docs.rs/aws-sdk-cognitoidentityprovider/latest/aws_sdk_cognitoidentityprovider/client/struct.Client.html#method.list_user_pools "https://docs.rs/aws-sdk-cognitoidentityprovider/latest/aws_sdk_cognitoidentityprovider/client/struct.Client.html#method.list_user_pools")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
