# Code examples for IAM using AWS SDKs

The following code examples show how to use IAM with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using IAM.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples").

```
namespace IAMActions;

public class HelloIAM
{
    static async Task Main(string[] args)
    {
        // Getting started with AWS Identity and Access Management (IAM). List
        // the policies for the account.
        var iamClient = new AmazonIdentityManagementServiceClient();

        var listPoliciesPaginator = iamClient.Paginators.ListPolicies(new ListPoliciesRequest());
        var policies = new List<ManagedPolicy>();

        await foreach (var response in listPoliciesPaginator.Responses)
        {
            policies.AddRange(response.Policies);
        }

        Console.WriteLine("Here are the policies defined for your account:\n");
        policies.ForEach(policy =>
        {
            Console.WriteLine($"Created: {policy.CreateDate}\t{policy.PolicyName}\t{policy.Description}");
        });
    }
}



```

- For API details, see
  [ListPolicies](../../../goto/DotNetSDKV3/iam-2010-05-08/ListPolicies.md "../../../goto/DotNetSDKV3/iam-2010-05-08/ListPolicies.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iam/hello_iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iam/hello_iam#code-examples").

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS iam)

# Set this project's name.
project("hello_iam")

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
        hello_iam.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the iam.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/iam/IAMClient.h>
#include <aws/iam/model/ListPoliciesRequest.h>
#include <iostream>
#include <iomanip>

/*
 *  A "Hello IAM" starter application which initializes an AWS Identity and Access Management (IAM) client
 *  and lists the IAM policies.
 *
 *  main function
 *
 *  Usage: 'hello_iam'
 *
 */

int main(int argc, char **argv) {
    Aws::SDKOptions options;
    // Optionally change the log level for debugging.
//   options.loggingOptions.logLevel = Utils::Logging::LogLevel::Debug;
    Aws::InitAPI(options); // Should only be called once.
    int result = 0;
    {
        const Aws::String DATE_FORMAT("%Y-%m-%d");
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

        Aws::IAM::IAMClient iamClient(clientConfig);
        Aws::IAM::Model::ListPoliciesRequest request;

        bool done = false;
        bool header = false;
        while (!done) {
            auto outcome = iamClient.ListPolicies(request);
            if (!outcome.IsSuccess()) {
                std::cerr << "Failed to list iam policies: " <<
                          outcome.GetError().GetMessage() << std::endl;
                result = 1;
                break;
            }

            if (!header) {
                std::cout << std::left << std::setw(55) << "Name" <<
                          std::setw(30) << "ID" << std::setw(80) << "Arn" <<
                          std::setw(64) << "Description" << std::setw(12) <<
                          "CreateDate" << std::endl;
                header = true;
            }

            const auto &policies = outcome.GetResult().GetPolicies();
            for (const auto &policy: policies) {
                std::cout << std::left << std::setw(55) <<
                          policy.GetPolicyName() << std::setw(30) <<
                          policy.GetPolicyId() << std::setw(80) << policy.GetArn() <<
                          std::setw(64) << policy.GetDescription() << std::setw(12) <<
                          policy.GetCreateDate().ToGmtString(DATE_FORMAT.c_str()) <<
                          std::endl;
            }

            if (outcome.GetResult().GetIsTruncated()) {
                request.SetMarker(outcome.GetResult().GetMarker());
            } else {
                done = true;
            }
        }
    }


    Aws::ShutdownAPI(options); // Should only be called once.
    return result;
}


```

- For API details, see
  [ListPolicies](../../../goto/SdkForCpp/iam-2010-05-08/ListPolicies.md "../../../goto/SdkForCpp/iam-2010-05-08/ListPolicies.md")
  in _AWS SDK for C++ API Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples").

```

package main

import (
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/iam"
)

// main uses the AWS SDK for Go (v2) to create an AWS Identity and Access Management (IAM)
// client and list up to 10 policies in your account.
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
	iamClient := iam.NewFromConfig(sdkConfig)
	const maxPols = 10
	fmt.Printf("Let's list up to %v policies for your account.\n", maxPols)
	result, err := iamClient.ListPolicies(ctx, &iam.ListPoliciesInput{
		MaxItems: aws.Int32(maxPols),
	})
	if err != nil {
		fmt.Printf("Couldn't list policies for your account. Here's why: %v\n", err)
		return
	}
	if len(result.Policies) == 0 {
		fmt.Println("You don't have any policies!")
	} else {
		for _, policy := range result.Policies {
			fmt.Printf("\t%v\n", *policy.PolicyName)
		}
	}
}



```

- For API details, see
  [ListPolicies](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListPolicies "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListPolicies")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iam#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.iam.IamClient;
import software.amazon.awssdk.services.iam.model.ListPoliciesResponse;
import software.amazon.awssdk.services.iam.model.Policy;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloIAM {
    public static void main(String[] args) {
        Region region = Region.AWS_GLOBAL;
        IamClient iam = IamClient.builder()
                .region(region)
                .build();

        listPolicies(iam);
    }

    public static void listPolicies(IamClient iam) {
        ListPoliciesResponse response = iam.listPolicies();
        List<Policy> polList = response.policies();
        polList.forEach(policy -> {
            System.out.println("Policy Name: " + policy.policyName());
        });
    }
}


```

- For API details, see
  [ListPolicies](../../../goto/SdkForJavaV2/iam-2010-05-08/ListPolicies.md "../../../goto/SdkForJavaV2/iam-2010-05-08/ListPolicies.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

```
import { IAMClient, paginateListPolicies } from "@aws-sdk/client-iam";

const client = new IAMClient({});

export const listLocalPolicies = async () => {
  /**
   * In v3, the clients expose paginateOperationName APIs that are written using async generators so that you can use async iterators in a for await..of loop.
   * https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/index.html#paginators
   */
  const paginator = paginateListPolicies(
    { client, pageSize: 10 },
    // List only customer managed policies.
    { Scope: "Local" },
  );

  console.log("IAM policies defined in your account:");
  let policyCount = 0;
  for await (const page of paginator) {
    if (page.Policies) {
      for (const policy of page.Policies) {
        console.log(`${policy.PolicyName}`);
        policyCount++;
      }
    }
  }
  console.log(`Found ${policyCount} policies.`);
};


```

- For API details, see
  [ListPolicies](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/ListPoliciesCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/ListPoliciesCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples").

```

import boto3


def main():
    """
    Lists the managed policies in your AWS account using the AWS SDK for Python (Boto3).
    """
    iam = boto3.client("iam")

    try:
        # Get a paginator for the list_policies operation
        paginator = iam.get_paginator("list_policies")

        # Iterate through the pages of results
        for page in paginator.paginate(Scope="All", OnlyAttached=False):
            for policy in page["Policies"]:
                print(f"Policy name: {policy['PolicyName']}")
                print(f"  Policy ARN: {policy['Arn']}")
    except boto3.exceptions.BotoCoreError as e:
        print(f"Encountered an error while listing policies: {e}")


if __name__ == "__main__":
    main()



```

- For API details, see
  [ListPolicies](../../../goto/boto3/iam-2010-05-08/ListPolicies.md "../../../goto/boto3/iam-2010-05-08/ListPolicies.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples").

```

require 'aws-sdk-iam'
require 'logger'

# IAMManager is a class responsible for managing IAM operations
# such as listing all IAM policies in the current AWS account.
class IAMManager
  def initialize(client)
    @client = client
    @logger = Logger.new($stdout)
  end

  # Lists and prints all IAM policies in the current AWS account.
  def list_policies
    @logger.info('Here are the IAM policies in your account:')

    paginator = @client.list_policies
    policies = []

    paginator.each_page do |page|
      policies.concat(page.policies)
    end

    if policies.empty?
      @logger.info("You don't have any IAM policies.")
    else
      policies.each do |policy|
        @logger.info("- #{policy.policy_name}")
      end
    end
  end
end

if $PROGRAM_NAME == __FILE__
  iam_client = Aws::IAM::Client.new
  manager = IAMManager.new(iam_client)
  manager.list_policies
end



```

- For API details, see
  [ListPolicies](../../../goto/SdkForRubyV3/iam-2010-05-08/ListPolicies.md "../../../goto/SdkForRubyV3/iam-2010-05-08/ListPolicies.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples").

From src/bin/hello.rs.

```

use aws_sdk_iam::error::SdkError;
use aws_sdk_iam::operation::list_policies::ListPoliciesError;
use clap::Parser;

const PATH_PREFIX_HELP: &str = "The path prefix for filtering the results.";

#[derive(Debug, clap::Parser)]
#[command(about)]
struct HelloScenarioArgs {
    #[arg(long, default_value="/", help=PATH_PREFIX_HELP)]
    pub path_prefix: String,
}

#[tokio::main]
async fn main() -> Result<(), SdkError<ListPoliciesError>> {
    let sdk_config = aws_config::load_from_env().await;
    let client = aws_sdk_iam::Client::new(&sdk_config);

    let args = HelloScenarioArgs::parse();

    iam_service::list_policies(client, args.path_prefix).await?;

    Ok(())
}


```

From src/iam-service-lib.rs.

```
pub async fn list_policies(
    client: iamClient,
    path_prefix: String,
) -> Result<Vec<String>, SdkError<ListPoliciesError>> {
    let list_policies = client
        .list_policies()
        .path_prefix(path_prefix)
        .scope(PolicyScopeType::Local)
        .into_paginator()
        .items()
        .send()
        .try_collect()
        .await?;

    let policy_names = list_policies
        .into_iter()
        .map(|p| {
            let name = p
                .policy_name
                .unwrap_or_else(|| "Missing Policy Name".to_string());
            println!("{}", name);
            name
        })
        .collect();

    Ok(policy_names)
}


```

- For API details, see
  [ListPolicies](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_policies "https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_policies")
  in _AWS SDK for Rust API reference_.

###### Code examples

- [Basics](service_code_examples_iam_basics.md "service_code_examples_iam_basics.md")
  - [Hello IAM](iam_example_iam_Hello_section.md "iam_example_iam_Hello_section.md")
  - [Learn the basics](iam_example_iam_Scenario_CreateUserAssumeRole_section.md "iam_example_iam_Scenario_CreateUserAssumeRole_section.md")
  - [Actions](service_code_examples_iam_actions.md "service_code_examples_iam_actions.md")
    - [AddClientIdToOpenIdConnectProvider](iam_example_iam_AddClientIdToOpenIdConnectProvider_section.md "iam_example_iam_AddClientIdToOpenIdConnectProvider_section.md")
    - [AddRoleToInstanceProfile](iam_example_iam_AddRoleToInstanceProfile_section.md "iam_example_iam_AddRoleToInstanceProfile_section.md")
    - [AddUserToGroup](iam_example_iam_AddUserToGroup_section.md "iam_example_iam_AddUserToGroup_section.md")
    - [AttachGroupPolicy](iam_example_iam_AttachGroupPolicy_section.md "iam_example_iam_AttachGroupPolicy_section.md")
    - [AttachRolePolicy](iam_example_iam_AttachRolePolicy_section.md "iam_example_iam_AttachRolePolicy_section.md")
    - [AttachUserPolicy](iam_example_iam_AttachUserPolicy_section.md "iam_example_iam_AttachUserPolicy_section.md")
    - [ChangePassword](iam_example_iam_ChangePassword_section.md "iam_example_iam_ChangePassword_section.md")
    - [CreateAccessKey](iam_example_iam_CreateAccessKey_section.md "iam_example_iam_CreateAccessKey_section.md")
    - [CreateAccountAlias](iam_example_iam_CreateAccountAlias_section.md "iam_example_iam_CreateAccountAlias_section.md")
    - [CreateGroup](iam_example_iam_CreateGroup_section.md "iam_example_iam_CreateGroup_section.md")
    - [CreateInstanceProfile](iam_example_iam_CreateInstanceProfile_section.md "iam_example_iam_CreateInstanceProfile_section.md")
    - [CreateLoginProfile](iam_example_iam_CreateLoginProfile_section.md "iam_example_iam_CreateLoginProfile_section.md")
    - [CreateOpenIdConnectProvider](iam_example_iam_CreateOpenIdConnectProvider_section.md "iam_example_iam_CreateOpenIdConnectProvider_section.md")
    - [CreatePolicy](iam_example_iam_CreatePolicy_section.md "iam_example_iam_CreatePolicy_section.md")
    - [CreatePolicyVersion](iam_example_iam_CreatePolicyVersion_section.md "iam_example_iam_CreatePolicyVersion_section.md")
    - [CreateRole](iam_example_iam_CreateRole_section.md "iam_example_iam_CreateRole_section.md")
    - [CreateSAMLProvider](iam_example_iam_CreateSAMLProvider_section.md "iam_example_iam_CreateSAMLProvider_section.md")
    - [CreateServiceLinkedRole](iam_example_iam_CreateServiceLinkedRole_section.md "iam_example_iam_CreateServiceLinkedRole_section.md")
    - [CreateUser](iam_example_iam_CreateUser_section.md "iam_example_iam_CreateUser_section.md")
    - [CreateVirtualMfaDevice](iam_example_iam_CreateVirtualMfaDevice_section.md "iam_example_iam_CreateVirtualMfaDevice_section.md")
    - [DeactivateMfaDevice](iam_example_iam_DeactivateMfaDevice_section.md "iam_example_iam_DeactivateMfaDevice_section.md")
    - [DeleteAccessKey](iam_example_iam_DeleteAccessKey_section.md "iam_example_iam_DeleteAccessKey_section.md")
    - [DeleteAccountAlias](iam_example_iam_DeleteAccountAlias_section.md "iam_example_iam_DeleteAccountAlias_section.md")
    - [DeleteAccountPasswordPolicy](iam_example_iam_DeleteAccountPasswordPolicy_section.md "iam_example_iam_DeleteAccountPasswordPolicy_section.md")
    - [DeleteGroup](iam_example_iam_DeleteGroup_section.md "iam_example_iam_DeleteGroup_section.md")
    - [DeleteGroupPolicy](iam_example_iam_DeleteGroupPolicy_section.md "iam_example_iam_DeleteGroupPolicy_section.md")
    - [DeleteInstanceProfile](iam_example_iam_DeleteInstanceProfile_section.md "iam_example_iam_DeleteInstanceProfile_section.md")
    - [DeleteLoginProfile](iam_example_iam_DeleteLoginProfile_section.md "iam_example_iam_DeleteLoginProfile_section.md")
    - [DeleteOpenIdConnectProvider](iam_example_iam_DeleteOpenIdConnectProvider_section.md "iam_example_iam_DeleteOpenIdConnectProvider_section.md")
    - [DeletePolicy](iam_example_iam_DeletePolicy_section.md "iam_example_iam_DeletePolicy_section.md")
    - [DeletePolicyVersion](iam_example_iam_DeletePolicyVersion_section.md "iam_example_iam_DeletePolicyVersion_section.md")
    - [DeleteRole](iam_example_iam_DeleteRole_section.md "iam_example_iam_DeleteRole_section.md")
    - [DeleteRolePermissionsBoundary](iam_example_iam_DeleteRolePermissionsBoundary_section.md "iam_example_iam_DeleteRolePermissionsBoundary_section.md")
    - [DeleteRolePolicy](iam_example_iam_DeleteRolePolicy_section.md "iam_example_iam_DeleteRolePolicy_section.md")
    - [DeleteSAMLProvider](iam_example_iam_DeleteSAMLProvider_section.md "iam_example_iam_DeleteSAMLProvider_section.md")
    - [DeleteServerCertificate](iam_example_iam_DeleteServerCertificate_section.md "iam_example_iam_DeleteServerCertificate_section.md")
    - [DeleteServiceLinkedRole](iam_example_iam_DeleteServiceLinkedRole_section.md "iam_example_iam_DeleteServiceLinkedRole_section.md")
    - [DeleteSigningCertificate](iam_example_iam_DeleteSigningCertificate_section.md "iam_example_iam_DeleteSigningCertificate_section.md")
    - [DeleteUser](iam_example_iam_DeleteUser_section.md "iam_example_iam_DeleteUser_section.md")
    - [DeleteUserPermissionsBoundary](iam_example_iam_DeleteUserPermissionsBoundary_section.md "iam_example_iam_DeleteUserPermissionsBoundary_section.md")
    - [DeleteUserPolicy](iam_example_iam_DeleteUserPolicy_section.md "iam_example_iam_DeleteUserPolicy_section.md")
    - [DeleteVirtualMfaDevice](iam_example_iam_DeleteVirtualMfaDevice_section.md "iam_example_iam_DeleteVirtualMfaDevice_section.md")
    - [DetachGroupPolicy](iam_example_iam_DetachGroupPolicy_section.md "iam_example_iam_DetachGroupPolicy_section.md")
    - [DetachRolePolicy](iam_example_iam_DetachRolePolicy_section.md "iam_example_iam_DetachRolePolicy_section.md")
    - [DetachUserPolicy](iam_example_iam_DetachUserPolicy_section.md "iam_example_iam_DetachUserPolicy_section.md")
    - [EnableMfaDevice](iam_example_iam_EnableMfaDevice_section.md "iam_example_iam_EnableMfaDevice_section.md")
    - [GenerateCredentialReport](iam_example_iam_GenerateCredentialReport_section.md "iam_example_iam_GenerateCredentialReport_section.md")
    - [GenerateServiceLastAccessedDetails](iam_example_iam_GenerateServiceLastAccessedDetails_section.md "iam_example_iam_GenerateServiceLastAccessedDetails_section.md")
    - [GetAccessKeyLastUsed](iam_example_iam_GetAccessKeyLastUsed_section.md "iam_example_iam_GetAccessKeyLastUsed_section.md")
    - [GetAccountAuthorizationDetails](iam_example_iam_GetAccountAuthorizationDetails_section.md "iam_example_iam_GetAccountAuthorizationDetails_section.md")
    - [GetAccountPasswordPolicy](iam_example_iam_GetAccountPasswordPolicy_section.md "iam_example_iam_GetAccountPasswordPolicy_section.md")
    - [GetAccountSummary](iam_example_iam_GetAccountSummary_section.md "iam_example_iam_GetAccountSummary_section.md")
    - [GetContextKeysForCustomPolicy](iam_example_iam_GetContextKeysForCustomPolicy_section.md "iam_example_iam_GetContextKeysForCustomPolicy_section.md")
    - [GetContextKeysForPrincipalPolicy](iam_example_iam_GetContextKeysForPrincipalPolicy_section.md "iam_example_iam_GetContextKeysForPrincipalPolicy_section.md")
    - [GetCredentialReport](iam_example_iam_GetCredentialReport_section.md "iam_example_iam_GetCredentialReport_section.md")
    - [GetGroup](iam_example_iam_GetGroup_section.md "iam_example_iam_GetGroup_section.md")
    - [GetGroupPolicy](iam_example_iam_GetGroupPolicy_section.md "iam_example_iam_GetGroupPolicy_section.md")
    - [GetInstanceProfile](iam_example_iam_GetInstanceProfile_section.md "iam_example_iam_GetInstanceProfile_section.md")
    - [GetLoginProfile](iam_example_iam_GetLoginProfile_section.md "iam_example_iam_GetLoginProfile_section.md")
    - [GetOpenIdConnectProvider](iam_example_iam_GetOpenIdConnectProvider_section.md "iam_example_iam_GetOpenIdConnectProvider_section.md")
    - [GetPolicy](iam_example_iam_GetPolicy_section.md "iam_example_iam_GetPolicy_section.md")
    - [GetPolicyVersion](iam_example_iam_GetPolicyVersion_section.md "iam_example_iam_GetPolicyVersion_section.md")
    - [GetRole](iam_example_iam_GetRole_section.md "iam_example_iam_GetRole_section.md")
    - [GetRolePolicy](iam_example_iam_GetRolePolicy_section.md "iam_example_iam_GetRolePolicy_section.md")
    - [GetSamlProvider](iam_example_iam_GetSamlProvider_section.md "iam_example_iam_GetSamlProvider_section.md")
    - [GetServerCertificate](iam_example_iam_GetServerCertificate_section.md "iam_example_iam_GetServerCertificate_section.md")
    - [GetServiceLastAccessedDetails](iam_example_iam_GetServiceLastAccessedDetails_section.md "iam_example_iam_GetServiceLastAccessedDetails_section.md")
    - [GetServiceLastAccessedDetailsWithEntities](iam_example_iam_GetServiceLastAccessedDetailsWithEntities_section.md "iam_example_iam_GetServiceLastAccessedDetailsWithEntities_section.md")
    - [GetServiceLinkedRoleDeletionStatus](iam_example_iam_GetServiceLinkedRoleDeletionStatus_section.md "iam_example_iam_GetServiceLinkedRoleDeletionStatus_section.md")
    - [GetUser](iam_example_iam_GetUser_section.md "iam_example_iam_GetUser_section.md")
    - [GetUserPolicy](iam_example_iam_GetUserPolicy_section.md "iam_example_iam_GetUserPolicy_section.md")
    - [ListAccessKeys](iam_example_iam_ListAccessKeys_section.md "iam_example_iam_ListAccessKeys_section.md")
    - [ListAccountAliases](iam_example_iam_ListAccountAliases_section.md "iam_example_iam_ListAccountAliases_section.md")
    - [ListAttachedGroupPolicies](iam_example_iam_ListAttachedGroupPolicies_section.md "iam_example_iam_ListAttachedGroupPolicies_section.md")
    - [ListAttachedRolePolicies](iam_example_iam_ListAttachedRolePolicies_section.md "iam_example_iam_ListAttachedRolePolicies_section.md")
    - [ListAttachedUserPolicies](iam_example_iam_ListAttachedUserPolicies_section.md "iam_example_iam_ListAttachedUserPolicies_section.md")
    - [ListEntitiesForPolicy](iam_example_iam_ListEntitiesForPolicy_section.md "iam_example_iam_ListEntitiesForPolicy_section.md")
    - [ListGroupPolicies](iam_example_iam_ListGroupPolicies_section.md "iam_example_iam_ListGroupPolicies_section.md")
    - [ListGroups](iam_example_iam_ListGroups_section.md "iam_example_iam_ListGroups_section.md")
    - [ListGroupsForUser](iam_example_iam_ListGroupsForUser_section.md "iam_example_iam_ListGroupsForUser_section.md")
    - [ListInstanceProfiles](iam_example_iam_ListInstanceProfiles_section.md "iam_example_iam_ListInstanceProfiles_section.md")
    - [ListInstanceProfilesForRole](iam_example_iam_ListInstanceProfilesForRole_section.md "iam_example_iam_ListInstanceProfilesForRole_section.md")
    - [ListMfaDevices](iam_example_iam_ListMfaDevices_section.md "iam_example_iam_ListMfaDevices_section.md")
    - [ListOpenIdConnectProviders](iam_example_iam_ListOpenIdConnectProviders_section.md "iam_example_iam_ListOpenIdConnectProviders_section.md")
    - [ListPolicies](iam_example_iam_ListPolicies_section.md "iam_example_iam_ListPolicies_section.md")
    - [ListPolicyVersions](iam_example_iam_ListPolicyVersions_section.md "iam_example_iam_ListPolicyVersions_section.md")
    - [ListRolePolicies](iam_example_iam_ListRolePolicies_section.md "iam_example_iam_ListRolePolicies_section.md")
    - [ListRoleTags](iam_example_iam_ListRoleTags_section.md "iam_example_iam_ListRoleTags_section.md")
    - [ListRoles](iam_example_iam_ListRoles_section.md "iam_example_iam_ListRoles_section.md")
    - [ListSAMLProviders](iam_example_iam_ListSAMLProviders_section.md "iam_example_iam_ListSAMLProviders_section.md")
    - [ListServerCertificates](iam_example_iam_ListServerCertificates_section.md "iam_example_iam_ListServerCertificates_section.md")
    - [ListSigningCertificates](iam_example_iam_ListSigningCertificates_section.md "iam_example_iam_ListSigningCertificates_section.md")
    - [ListUserPolicies](iam_example_iam_ListUserPolicies_section.md "iam_example_iam_ListUserPolicies_section.md")
    - [ListUserTags](iam_example_iam_ListUserTags_section.md "iam_example_iam_ListUserTags_section.md")
    - [ListUsers](iam_example_iam_ListUsers_section.md "iam_example_iam_ListUsers_section.md")
    - [ListVirtualMfaDevices](iam_example_iam_ListVirtualMfaDevices_section.md "iam_example_iam_ListVirtualMfaDevices_section.md")
    - [PutGroupPolicy](iam_example_iam_PutGroupPolicy_section.md "iam_example_iam_PutGroupPolicy_section.md")
    - [PutRolePermissionsBoundary](iam_example_iam_PutRolePermissionsBoundary_section.md "iam_example_iam_PutRolePermissionsBoundary_section.md")
    - [PutRolePolicy](iam_example_iam_PutRolePolicy_section.md "iam_example_iam_PutRolePolicy_section.md")
    - [PutUserPermissionsBoundary](iam_example_iam_PutUserPermissionsBoundary_section.md "iam_example_iam_PutUserPermissionsBoundary_section.md")
    - [PutUserPolicy](iam_example_iam_PutUserPolicy_section.md "iam_example_iam_PutUserPolicy_section.md")
    - [RemoveClientIdFromOpenIdConnectProvider](iam_example_iam_RemoveClientIdFromOpenIdConnectProvider_section.md "iam_example_iam_RemoveClientIdFromOpenIdConnectProvider_section.md")
    - [RemoveRoleFromInstanceProfile](iam_example_iam_RemoveRoleFromInstanceProfile_section.md "iam_example_iam_RemoveRoleFromInstanceProfile_section.md")
    - [RemoveUserFromGroup](iam_example_iam_RemoveUserFromGroup_section.md "iam_example_iam_RemoveUserFromGroup_section.md")
    - [ResyncMfaDevice](iam_example_iam_ResyncMfaDevice_section.md "iam_example_iam_ResyncMfaDevice_section.md")
    - [SetDefaultPolicyVersion](iam_example_iam_SetDefaultPolicyVersion_section.md "iam_example_iam_SetDefaultPolicyVersion_section.md")
    - [TagRole](iam_example_iam_TagRole_section.md "iam_example_iam_TagRole_section.md")
    - [TagUser](iam_example_iam_TagUser_section.md "iam_example_iam_TagUser_section.md")
    - [UntagRole](iam_example_iam_UntagRole_section.md "iam_example_iam_UntagRole_section.md")
    - [UntagUser](iam_example_iam_UntagUser_section.md "iam_example_iam_UntagUser_section.md")
    - [UpdateAccessKey](iam_example_iam_UpdateAccessKey_section.md "iam_example_iam_UpdateAccessKey_section.md")
    - [UpdateAccountPasswordPolicy](iam_example_iam_UpdateAccountPasswordPolicy_section.md "iam_example_iam_UpdateAccountPasswordPolicy_section.md")
    - [UpdateAssumeRolePolicy](iam_example_iam_UpdateAssumeRolePolicy_section.md "iam_example_iam_UpdateAssumeRolePolicy_section.md")
    - [UpdateGroup](iam_example_iam_UpdateGroup_section.md "iam_example_iam_UpdateGroup_section.md")
    - [UpdateLoginProfile](iam_example_iam_UpdateLoginProfile_section.md "iam_example_iam_UpdateLoginProfile_section.md")
    - [UpdateOpenIdConnectProviderThumbprint](iam_example_iam_UpdateOpenIdConnectProviderThumbprint_section.md "iam_example_iam_UpdateOpenIdConnectProviderThumbprint_section.md")
    - [UpdateRole](iam_example_iam_UpdateRole_section.md "iam_example_iam_UpdateRole_section.md")
    - [UpdateRoleDescription](iam_example_iam_UpdateRoleDescription_section.md "iam_example_iam_UpdateRoleDescription_section.md")
    - [UpdateSamlProvider](iam_example_iam_UpdateSamlProvider_section.md "iam_example_iam_UpdateSamlProvider_section.md")
    - [UpdateServerCertificate](iam_example_iam_UpdateServerCertificate_section.md "iam_example_iam_UpdateServerCertificate_section.md")
    - [UpdateSigningCertificate](iam_example_iam_UpdateSigningCertificate_section.md "iam_example_iam_UpdateSigningCertificate_section.md")
    - [UpdateUser](iam_example_iam_UpdateUser_section.md "iam_example_iam_UpdateUser_section.md")
    - [UploadServerCertificate](iam_example_iam_UploadServerCertificate_section.md "iam_example_iam_UploadServerCertificate_section.md")
    - [UploadSigningCertificate](iam_example_iam_UploadSigningCertificate_section.md "iam_example_iam_UploadSigningCertificate_section.md")

- [Scenarios](service_code_examples_iam_scenarios.md "service_code_examples_iam_scenarios.md")
  - [Build and manage a resilient service](iam_example_cross_ResilientService_section.md "iam_example_cross_ResilientService_section.md")
  - [Create read-only and read-write users](iam_example_iam_Scenario_UserPolicies_section.md "iam_example_iam_Scenario_UserPolicies_section.md")
  - [Manage access keys](iam_example_iam_Scenario_ManageAccessKeys_section.md "iam_example_iam_Scenario_ManageAccessKeys_section.md")
  - [Manage policies](iam_example_iam_Scenario_PolicyManagement_section.md "iam_example_iam_Scenario_PolicyManagement_section.md")
  - [Manage roles](iam_example_iam_Scenario_RoleManagement_section.md "iam_example_iam_Scenario_RoleManagement_section.md")
  - [Manage your account](iam_example_iam_Scenario_AccountManagement_section.md "iam_example_iam_Scenario_AccountManagement_section.md")
  - [Permission policy allows AWS Compute Optimizer Automation to apply recommended actions](iam_example_iam-policies.AWSMettleDocs.latest.userguide.managed-policies.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.managed-policies.xml.md")
  - [Permission policy to enable Automation across your organization](iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md")
  - [Permission policy to enable Automation for your account](iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md")
  - [Permission policy to grant full access to Compute Optimizer Automation for a management account of an organization](iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md")
  - [Permission policy to grant full access to Compute Optimizer Automation for standalone AWS accounts](iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md")
  - [Permission policy to grant read-only access to Compute Optimizer Automation for a management account of an organization](iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md")
  - [Permission policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts](iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.md")
  - [Permission policy to grant service-linked role permissions for Compute Optimization Automation](iam_example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.md "iam_example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.md")
  - [Roll back a policy version](iam_example_iam_Scenario_RollbackPolicyVersion_section.md "iam_example_iam_Scenario_RollbackPolicyVersion_section.md")
  - [Set up Attribute-Based Access Control](iam_example_dynamodb_Scenario_ABACSetup_section.md "iam_example_dynamodb_Scenario_ABACSetup_section.md")
  - [Work with Streams and Time-to-Live](iam_example_dynamodb_Scenario_StreamsAndTTL_section.md "iam_example_dynamodb_Scenario_StreamsAndTTL_section.md")
  - [Work with the IAM Policy Builder API](iam_example_iam_Scenario_IamPolicyBuilder_section.md "iam_example_iam_Scenario_IamPolicyBuilder_section.md")
