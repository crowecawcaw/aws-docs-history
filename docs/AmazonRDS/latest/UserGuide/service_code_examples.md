# Code examples for Amazon RDS using AWS SDKs

The following code examples show how to use Amazon RDS with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](CHAP_Tutorials.md#sdk-general-information-section "CHAP_Tutorials.md#sdk-general-information-section").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Amazon RDS.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/RDS#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/RDS#code-examples").

```
using System;
using System.Threading.Tasks;
using Amazon.RDS;
using Amazon.RDS.Model;

namespace RDSActions;

public static class HelloRds
{
    static async Task Main(string[] args)
    {
        var rdsClient = new AmazonRDSClient();

        Console.WriteLine($"Hello Amazon RDS! Following are some of your DB instances:");
        Console.WriteLine();

        // You can use await and any of the async methods to get a response.
        // Let's get the first twenty DB instances.
        var response = await rdsClient.DescribeDBInstancesAsync(
            new DescribeDBInstancesRequest()
            {
                MaxRecords = 20 // Must be between 20 and 100.
            });

        foreach (var instance in response.DBInstances)
        {
            Console.WriteLine($"\tDB name: {instance.DBName}");
            Console.WriteLine($"\tArn: {instance.DBInstanceArn}");
            Console.WriteLine($"\tIdentifier: {instance.DBInstanceIdentifier}");
            Console.WriteLine();
        }
    }
}


```

- For API details, see
  [DescribeDBInstances](../../../goto/DotNetSDKV3/rds-2014-10-31/DescribeDBInstances.md "../../../goto/DotNetSDKV3/rds-2014-10-31/DescribeDBInstances.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/rds/hello_rds#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/rds/hello_rds#code-examples").

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS rds)

# Set this project's name.
project("hello_rds")

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
        hello_rds.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello_rds.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/rds/RDSClient.h>
#include <aws/rds/model/DescribeDBInstancesRequest.h>
#include <iostream>

/*
 *  A "Hello Rds" starter application which initializes an Amazon Relational Database Service (Amazon RDS) client and
 *  describes the Amazon RDS instances.
 *
 *  main function
 *
 *  Usage: 'hello_rds'
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

        Aws::RDS::RDSClient rdsClient(clientConfig);
        Aws::String marker;
        std::vector<Aws::String> instanceDBIDs;

        do {
            Aws::RDS::Model::DescribeDBInstancesRequest request;

            if (!marker.empty()) {
                request.SetMarker(marker);
            }

            Aws::RDS::Model::DescribeDBInstancesOutcome outcome =
                    rdsClient.DescribeDBInstances(request);

            if (outcome.IsSuccess()) {
                for (auto &instance: outcome.GetResult().GetDBInstances()) {
                    instanceDBIDs.push_back(instance.GetDBInstanceIdentifier());
                }
                marker = outcome.GetResult().GetMarker();
            } else {
                result = 1;
                std::cerr << "Error with RDS::DescribeDBInstances. "
                          << outcome.GetError().GetMessage()
                          << std::endl;
                break;
            }
        } while (!marker.empty());

        std::cout << instanceDBIDs.size() << " RDS instances found." << std::endl;
        for (auto &instanceDBID: instanceDBIDs) {
            std::cout << "   Instance: " << instanceDBID << std::endl;
        }
    }

    Aws::ShutdownAPI(options); // Should only be called once.
    return result;
}


```

- For API details, see
  [DescribeDBInstances](../../../goto/SdkForCpp/rds-2014-10-31/DescribeDBInstances.md "../../../goto/SdkForCpp/rds-2014-10-31/DescribeDBInstances.md")
  in _AWS SDK for C++ API Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples").

```

package main

import (
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/rds"
)

// main uses the AWS SDK for Go V2 to create an Amazon Relational Database Service (Amazon RDS)
// client and list up to 20 DB instances in your account.
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
	rdsClient := rds.NewFromConfig(sdkConfig)
	const maxInstances = 20
	fmt.Printf("Let's list up to %v DB instances.\n", maxInstances)
	output, err := rdsClient.DescribeDBInstances(ctx,
		&rds.DescribeDBInstancesInput{MaxRecords: aws.Int32(maxInstances)})
	if err != nil {
		fmt.Printf("Couldn't list DB instances: %v\n", err)
		return
	}
	if len(output.DBInstances) == 0 {
		fmt.Println("No DB instances found.")
	} else {
		for _, instance := range output.DBInstances {
			fmt.Printf("DB instance %v has database %v.\n", *instance.DBInstanceIdentifier,
				*instance.DBName)
		}
	}
}



```

- For API details, see
  [DescribeDBInstances](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBInstances "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBInstances")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/rds#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/rds#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rds.RdsClient;
import software.amazon.awssdk.services.rds.model.DescribeDbInstancesResponse;
import software.amazon.awssdk.services.rds.model.DBInstance;
import software.amazon.awssdk.services.rds.model.RdsException;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DescribeDBInstances {

    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        RdsClient rdsClient = RdsClient.builder()
                .region(region)
                .build();

        describeInstances(rdsClient);
        rdsClient.close();
    }

    public static void describeInstances(RdsClient rdsClient) {
        try {
            DescribeDbInstancesResponse response = rdsClient.describeDBInstances();
            List<DBInstance> instanceList = response.dbInstances();
            for (DBInstance instance : instanceList) {
                System.out.println("Instance ARN is: " + instance.dbInstanceArn());
                System.out.println("The Engine is " + instance.engine());
                System.out.println("Connection endpoint is" + instance.endpoint().address());
            }

        } catch (RdsException e) {
            System.out.println(e.getLocalizedMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [DescribeDBInstances](../../../goto/SdkForJavaV2/rds-2014-10-31/DescribeDBInstances.md "../../../goto/SdkForJavaV2/rds-2014-10-31/DescribeDBInstances.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rds#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rds#code-examples").

```
"""
Purpose

Shows how to use the AWS SDK for Python (Boto3) with the Amazon Relational Database Service
(Amazon RDS) to list the databases in your account.
"""

import boto3
from botocore.exceptions import ClientError

# Create an RDS client
rds_client = boto3.client("rds")

# Create a paginator for the describe_db_instances operation
paginator = rds_client.get_paginator("describe_db_instances")

try:
    # Use the paginator to get a list of DB instances
    response_iterator = paginator.paginate(
        PaginationConfig={
            "MaxItems": 123,
            "PageSize": 50,  # Adjust PageSize as needed
            "StartingToken": None,
        }
    )

    # Iterate through the pages of the response
    instances_found = False
    for page in response_iterator:
        if "DBInstances" in page and page["DBInstances"]:
            instances_found = True
            print("Your RDS instances are:")
            for db in page["DBInstances"]:
                print(db["DBInstanceIdentifier"])

    if not instances_found:
        print("No RDS instances found!")

except ClientError as e:
    print(f"Couldn't list RDS instances. Here's why: {e.response['Error']['Message']}")



```

- For API details, see
  [DescribeDBInstances](../../../goto/boto3/rds-2014-10-31/DescribeDBInstances.md "../../../goto/boto3/rds-2014-10-31/DescribeDBInstances.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/rds#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/rds#code-examples").

```

require 'aws-sdk-rds'
require 'logger'

# RDSManager is a class responsible for managing RDS operations
# such as listing all RDS DB instances in the current AWS account.
class RDSManager
  def initialize(client)
    @client = client
    @logger = Logger.new($stdout)
  end

  # Lists and prints all RDS DB instances in the current AWS account.
  def list_db_instances
    @logger.info('Listing RDS DB instances')

    paginator = @client.describe_db_instances
    instances = []

    paginator.each_page do |page|
      instances.concat(page.db_instances)
    end

    if instances.empty?
      @logger.info('No instances found.')
    else
      @logger.info("Found #{instances.count} instance(s):")
      instances.each do |instance|
        @logger.info(" * #{instance.db_instance_identifier} (#{instance.db_instance_status})")
      end
    end
  end
end

if $PROGRAM_NAME == __FILE__
  rds_client = Aws::RDS::Client.new(region: 'us-west-2')
  manager = RDSManager.new(rds_client)
  manager.list_db_instances
end



```

- For API details, see
  [DescribeDBInstances](../../../goto/SdkForRubyV3/rds-2014-10-31/DescribeDBInstances.md "../../../goto/SdkForRubyV3/rds-2014-10-31/DescribeDBInstances.md")
  in _AWS SDK for Ruby API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon RDS](example_rds_Hello_section.md "example_rds_Hello_section.md")
  - [Learn the basics](example_rds_Scenario_GetStartedInstances_section.md "example_rds_Scenario_GetStartedInstances_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [CreateDBInstance](example_rds_CreateDBInstance_section.md "example_rds_CreateDBInstance_section.md")
    - [CreateDBParameterGroup](example_rds_CreateDBParameterGroup_section.md "example_rds_CreateDBParameterGroup_section.md")
    - [CreateDBSnapshot](example_rds_CreateDBSnapshot_section.md "example_rds_CreateDBSnapshot_section.md")
    - [DeleteDBInstance](example_rds_DeleteDBInstance_section.md "example_rds_DeleteDBInstance_section.md")
    - [DeleteDBParameterGroup](example_rds_DeleteDBParameterGroup_section.md "example_rds_DeleteDBParameterGroup_section.md")
    - [DescribeAccountAttributes](example_rds_DescribeAccountAttributes_section.md "example_rds_DescribeAccountAttributes_section.md")
    - [DescribeDBEngineVersions](example_rds_DescribeDBEngineVersions_section.md "example_rds_DescribeDBEngineVersions_section.md")
    - [DescribeDBInstances](example_rds_DescribeDBInstances_section.md "example_rds_DescribeDBInstances_section.md")
    - [DescribeDBParameterGroups](example_rds_DescribeDBParameterGroups_section.md "example_rds_DescribeDBParameterGroups_section.md")
    - [DescribeDBParameters](example_rds_DescribeDBParameters_section.md "example_rds_DescribeDBParameters_section.md")
    - [DescribeDBSnapshots](example_rds_DescribeDBSnapshots_section.md "example_rds_DescribeDBSnapshots_section.md")
    - [DescribeOrderableDBInstanceOptions](example_rds_DescribeOrderableDBInstanceOptions_section.md "example_rds_DescribeOrderableDBInstanceOptions_section.md")
    - [GenerateRDSAuthToken](example_rds_GenerateRDSAuthToken_section.md "example_rds_GenerateRDSAuthToken_section.md")
    - [ModifyDBInstance](example_rds_ModifyDBInstance_section.md "example_rds_ModifyDBInstance_section.md")
    - [ModifyDBParameterGroup](example_rds_ModifyDBParameterGroup_section.md "example_rds_ModifyDBParameterGroup_section.md")
    - [RebootDBInstance](example_rds_RebootDBInstance_section.md "example_rds_RebootDBInstance_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Create an Aurora Serverless work item tracker](example_cross_RDSDataTracker_section.md "example_cross_RDSDataTracker_section.md")

- [Serverless examples](service_code_examples_serverless_examples.md "service_code_examples_serverless_examples.md")
  - [Connecting to an Amazon RDS database in a Lambda function](example_serverless_connect_RDS_Lambda_section.md "example_serverless_connect_RDS_Lambda_section.md")
