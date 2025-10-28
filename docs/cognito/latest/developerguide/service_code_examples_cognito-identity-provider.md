# Code examples for Amazon Cognito Identity Provider using AWS SDKs

The following code examples show how to use Amazon Cognito Identity Provider with an AWS software development kit (SDK).

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Amazon Cognito.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cognito/hello_cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cognito/hello_cognito#code-examples").

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS cognito-idp)

# Set this project's name.
project("hello_cognito")

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

     # set(BIN_SUB_DIR "/Debug") # If you are building from the command line, you may need to uncomment this
                                    # and set the proper subdirectory to the executables' location.

     AWSSDK_CPY_DYN_LIBS(SERVICE_COMPONENTS "" ${CMAKE_CURRENT_BINARY_DIR}${BIN_SUB_DIR})
endif ()

add_executable(${PROJECT_NAME}
        hello_cognito.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello_cognito.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/cognito-idp/CognitoIdentityProviderClient.h>
#include <aws/cognito-idp/model/ListUserPoolsRequest.h>
#include <iostream>

/*
 *  A "Hello Cognito" starter application which initializes an Amazon Cognito client and lists the Amazon Cognito
 *  user pools.
 *
 *  main function
 *
 *  Usage: 'hello_cognito'
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

        Aws::CognitoIdentityProvider::CognitoIdentityProviderClient cognitoClient(clientConfig);

        Aws::String nextToken; // Used for pagination.
        std::vector<Aws::String> userPools;

        do {
            Aws::CognitoIdentityProvider::Model::ListUserPoolsRequest listUserPoolsRequest;
            if (!nextToken.empty()) {
                listUserPoolsRequest.SetNextToken(nextToken);
            }

            Aws::CognitoIdentityProvider::Model::ListUserPoolsOutcome listUserPoolsOutcome =
                    cognitoClient.ListUserPools(listUserPoolsRequest);

            if (listUserPoolsOutcome.IsSuccess()) {
                for (auto &userPool: listUserPoolsOutcome.GetResult().GetUserPools()) {

                    userPools.push_back(userPool.GetName());
                }

                nextToken = listUserPoolsOutcome.GetResult().GetNextToken();
            } else {
                std::cerr << "ListUserPools error: " << listUserPoolsOutcome.GetError().GetMessage() << std::endl;
                result = 1;
                break;
            }


        } while (!nextToken.empty());
        std::cout << userPools.size() << " user pools found." << std::endl;
        for (auto &userPool: userPools) {
            std::cout << "   user pool: " << userPool << std::endl;
        }
    }

    Aws::ShutdownAPI(options); // Should only be called once.
    return result;
}


```

- For API details, see
  [ListUserPools](../../../goto/SdkForCpp/cognito-idp-2016-04-18/ListUserPools.md "../../../goto/SdkForCpp/cognito-idp-2016-04-18/ListUserPools.md")
  in _AWS SDK for C++ API Reference_.

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

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cognito-identity-provider#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cognito-identity-provider#code-examples").

```
import {
  paginateListUserPools,
  CognitoIdentityProviderClient,
} from "@aws-sdk/client-cognito-identity-provider";

const client = new CognitoIdentityProviderClient({});

export const helloCognito = async () => {
  const paginator = paginateListUserPools({ client }, {});

  const userPoolNames = [];

  for await (const page of paginator) {
    const names = page.UserPools.map((pool) => pool.Name);
    userPoolNames.push(...names);
  }

  console.log("User pool names: ");
  console.log(userPoolNames.join("\n"));
  return userPoolNames;
};


```

- For API details, see
  [ListUserPools](../../../AWSJavaScriptSDK/v3/latest/client/cognito-identity-provider/command/ListUserPoolsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/cognito-identity-provider/command/ListUserPoolsCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cognito#code-examples").

```

import boto3

# Create a Cognito Identity Provider client
cognitoidp = boto3.client("cognito-idp")

# Initialize a paginator for the list_user_pools operation
paginator = cognitoidp.get_paginator("list_user_pools")

# Create a PageIterator from the paginator
page_iterator = paginator.paginate(MaxResults=10)

# Initialize variables for pagination
user_pools = []

# Handle pagination
for page in page_iterator:
    user_pools.extend(page.get("UserPools", []))

# Print the list of user pools
print("User Pools for the account:")
if user_pools:
    for pool in user_pools:
        print(f"Name: {pool['Name']}, ID: {pool['Id']}")
else:
    print("No user pools found.")



```

- For API details, see
  [ListUserPools](../../../goto/boto3/cognito-idp-2016-04-18/ListUserPools.md "../../../goto/boto3/cognito-idp-2016-04-18/ListUserPools.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cognito#code-examples").

```

require 'aws-sdk-cognitoidentityprovider'
require 'logger'

# CognitoManager is a class responsible for managing AWS Cognito operations
# such as listing all user pools in the current AWS account.
class CognitoManager
  def initialize(client)
    @client = client
    @logger = Logger.new($stdout)
  end

  # Lists and prints all user pools associated with the AWS account.
  def list_user_pools
    paginator = @client.list_user_pools(max_results: 10)
    user_pools = []
    paginator.each_page do |page|
      user_pools.concat(page.user_pools)
    end

    if user_pools.empty?
      @logger.info('No Cognito user pools found.')
    else
      user_pools.each do |user_pool|
        @logger.info("User pool ID: #{user_pool.id}")
        @logger.info("User pool name: #{user_pool.name}")
        @logger.info("User pool status: #{user_pool.status}")
        @logger.info('---')
      end
    end
  end
end

if $PROGRAM_NAME == __FILE__
  cognito_client = Aws::CognitoIdentityProvider::Client.new
  manager = CognitoManager.new(cognito_client)
  manager.list_user_pools
end



```

- For API details, see
  [ListUserPools](../../../goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUserPools.md "../../../goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUserPools.md")
  in _AWS SDK for Ruby API Reference_.

###### Code examples

- [Basics](service_code_examples_cognito-identity-provider_basics.md "service_code_examples_cognito-identity-provider_basics.md")
  - [Hello Amazon Cognito](cognito-identity-provider_example_cognito-identity-provider_Hello_section.md "cognito-identity-provider_example_cognito-identity-provider_Hello_section.md")
  - [Actions](service_code_examples_cognito-identity-provider_actions.md "service_code_examples_cognito-identity-provider_actions.md")
    - [AdminCreateUser](cognito-identity-provider_example_cognito-identity-provider_AdminCreateUser_section.md "cognito-identity-provider_example_cognito-identity-provider_AdminCreateUser_section.md")
    - [AdminGetUser](cognito-identity-provider_example_cognito-identity-provider_AdminGetUser_section.md "cognito-identity-provider_example_cognito-identity-provider_AdminGetUser_section.md")
    - [AdminInitiateAuth](cognito-identity-provider_example_cognito-identity-provider_AdminInitiateAuth_section.md "cognito-identity-provider_example_cognito-identity-provider_AdminInitiateAuth_section.md")
    - [AdminRespondToAuthChallenge](cognito-identity-provider_example_cognito-identity-provider_AdminRespondToAuthChallenge_section.md "cognito-identity-provider_example_cognito-identity-provider_AdminRespondToAuthChallenge_section.md")
    - [AdminSetUserPassword](cognito-identity-provider_example_cognito-identity-provider_AdminSetUserPassword_section.md "cognito-identity-provider_example_cognito-identity-provider_AdminSetUserPassword_section.md")
    - [AssociateSoftwareToken](cognito-identity-provider_example_cognito-identity-provider_AssociateSoftwareToken_section.md "cognito-identity-provider_example_cognito-identity-provider_AssociateSoftwareToken_section.md")
    - [ConfirmDevice](cognito-identity-provider_example_cognito-identity-provider_ConfirmDevice_section.md "cognito-identity-provider_example_cognito-identity-provider_ConfirmDevice_section.md")
    - [ConfirmForgotPassword](cognito-identity-provider_example_cognito-identity-provider_ConfirmForgotPassword_section.md "cognito-identity-provider_example_cognito-identity-provider_ConfirmForgotPassword_section.md")
    - [ConfirmSignUp](cognito-identity-provider_example_cognito-identity-provider_ConfirmSignUp_section.md "cognito-identity-provider_example_cognito-identity-provider_ConfirmSignUp_section.md")
    - [CreateUserPool](cognito-identity-provider_example_cognito-identity-provider_CreateUserPool_section.md "cognito-identity-provider_example_cognito-identity-provider_CreateUserPool_section.md")
    - [CreateUserPoolClient](cognito-identity-provider_example_cognito-identity-provider_CreateUserPoolClient_section.md "cognito-identity-provider_example_cognito-identity-provider_CreateUserPoolClient_section.md")
    - [DeleteUser](cognito-identity-provider_example_cognito-identity-provider_DeleteUser_section.md "cognito-identity-provider_example_cognito-identity-provider_DeleteUser_section.md")
    - [ForgotPassword](cognito-identity-provider_example_cognito-identity-provider_ForgotPassword_section.md "cognito-identity-provider_example_cognito-identity-provider_ForgotPassword_section.md")
    - [InitiateAuth](cognito-identity-provider_example_cognito-identity-provider_InitiateAuth_section.md "cognito-identity-provider_example_cognito-identity-provider_InitiateAuth_section.md")
    - [ListUserPools](cognito-identity-provider_example_cognito-identity-provider_ListUserPools_section.md "cognito-identity-provider_example_cognito-identity-provider_ListUserPools_section.md")
    - [ListUsers](cognito-identity-provider_example_cognito-identity-provider_ListUsers_section.md "cognito-identity-provider_example_cognito-identity-provider_ListUsers_section.md")
    - [ResendConfirmationCode](cognito-identity-provider_example_cognito-identity-provider_ResendConfirmationCode_section.md "cognito-identity-provider_example_cognito-identity-provider_ResendConfirmationCode_section.md")
    - [RespondToAuthChallenge](cognito-identity-provider_example_cognito-identity-provider_RespondToAuthChallenge_section.md "cognito-identity-provider_example_cognito-identity-provider_RespondToAuthChallenge_section.md")
    - [SignUp](cognito-identity-provider_example_cognito-identity-provider_SignUp_section.md "cognito-identity-provider_example_cognito-identity-provider_SignUp_section.md")
    - [UpdateUserPool](cognito-identity-provider_example_cognito-identity-provider_UpdateUserPool_section.md "cognito-identity-provider_example_cognito-identity-provider_UpdateUserPool_section.md")
    - [VerifySoftwareToken](cognito-identity-provider_example_cognito-identity-provider_VerifySoftwareToken_section.md "cognito-identity-provider_example_cognito-identity-provider_VerifySoftwareToken_section.md")

- [Scenarios](service_code_examples_cognito-identity-provider_scenarios.md "service_code_examples_cognito-identity-provider_scenarios.md")
  - [Automatically confirm known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoConfirmUser_section.md "cognito-identity-provider_example_cross_CognitoAutoConfirmUser_section.md")
  - [Automatically migrate known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md "cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md")
  - [Sign up a user with a user pool that requires MFA](cognito-identity-provider_example_cognito-identity-provider_Scenario_SignUpUserWithMfa_section.md "cognito-identity-provider_example_cognito-identity-provider_Scenario_SignUpUserWithMfa_section.md")
  - [Use Amazon Cognito identity pools](cognito-identity-provider_example_cross_CognitoFlows_section.md "cognito-identity-provider_example_cross_CognitoFlows_section.md")
  - [Write custom activity data with a Lambda function after Amazon Cognito user authentication](cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md "cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md")
