# Code examples for Amazon EC2 using AWS SDKs

The following code examples show how to use Amazon EC2 with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Amazon EC2.

.NET

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/EC2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/EC2#code-examples").

```

namespace EC2Actions;

public class HelloEc2
{
    /// <summary>
    /// HelloEc2 lists the existing security groups for the default users.
    /// </summary>
    /// <param name="args">Command line arguments</param>
    /// <returns>Async task.</returns>
    static async Task Main(string[] args)
    {
        // Set up dependency injection for Amazon Elastic Compute Cloud (Amazon EC2).
        using var host = Microsoft.Extensions.Hosting.Host.CreateDefaultBuilder(args)
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonEC2>()
                .AddTransient<EC2Wrapper>()
            )
            .Build();

        // Now the client is available for injection.
        var ec2Client = host.Services.GetRequiredService<IAmazonEC2>();

        try
        {
            // Retrieve information for up to 10 Amazon EC2 security groups.
            var request = new DescribeSecurityGroupsRequest { MaxResults = 10 };
            var securityGroups = new List<SecurityGroup>();

            var paginatorForSecurityGroups =
                ec2Client.Paginators.DescribeSecurityGroups(request);

            await foreach (var securityGroup in paginatorForSecurityGroups.SecurityGroups)
            {
                securityGroups.Add(securityGroup);
            }

            // Now print the security groups returned by the call to
            // DescribeSecurityGroupsAsync.
            Console.WriteLine("Welcome to the EC2 Hello Service example. " +
                              "\nLet's list your Security Groups:");
            securityGroups.ForEach(group =>
            {
                Console.WriteLine(
                    $"Security group: {group.GroupName} ID: {group.GroupId}");
            });
        }
        catch (AmazonEC2Exception ex)
        {
            Console.WriteLine($"An Amazon EC2 service error occurred while listing security groups. {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred while listing security groups. {ex.Message}");
        }
    }
}


```

- For API details, see
  [DescribeSecurityGroups](../../../goto/DotNetSDKV4/ec2-2016-11-15/DescribeSecurityGroups.md "../../../goto/DotNetSDKV4/ec2-2016-11-15/DescribeSecurityGroups.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/ec2/hello_ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/ec2/hello_ec2#code-examples").

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS ec2)

# Set this project's name.
project("hello_ec2")

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
        hello_ec2.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello_ec2.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/ec2/EC2Client.h>
#include <aws/ec2/model/DescribeInstancesRequest.h>
#include <iomanip>
#include <iostream>

/*
 *  A "Hello EC2" starter application which initializes an Amazon Elastic Compute Cloud (Amazon EC2) client and describes
 *  the Amazon EC2 instances.
 *
 *  main function
 *
 *  Usage: 'hello_ec2'
 *
 */

int main(int argc, char **argv) {
    (void)argc;
    (void)argv;

    Aws::SDKOptions options;
    // Optionally change the log level for debugging.
//   options.loggingOptions.logLevel = Utils::Logging::LogLevel::Debug;
    Aws::InitAPI(options); // Should only be called once.
    int result = 0;
    {
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

        Aws::EC2::EC2Client ec2Client(clientConfig);
        Aws::EC2::Model::DescribeInstancesRequest request;
        bool header = false;
        bool done = false;
        while (!done) {
            Aws::EC2::Model::DescribeInstancesOutcome outcome = ec2Client.DescribeInstances(request);
            if (outcome.IsSuccess()) {
                if (!header) {
                    std::cout << std::left <<
                              std::setw(48) << "Name" <<
                              std::setw(20) << "ID" <<
                              std::setw(25) << "Ami" <<
                              std::setw(15) << "Type" <<
                              std::setw(15) << "State" <<
                              std::setw(15) << "Monitoring" << std::endl;
                    header = true;
                }

                const std::vector<Aws::EC2::Model::Reservation> &reservations =
                        outcome.GetResult().GetReservations();

                for (const auto &reservation: reservations) {
                    const std::vector<Aws::EC2::Model::Instance> &instances =
                            reservation.GetInstances();
                    for (const auto &instance: instances) {
                        Aws::String instanceStateString =
                                Aws::EC2::Model::InstanceStateNameMapper::GetNameForInstanceStateName(
                                        instance.GetState().GetName());

                        Aws::String typeString =
                                Aws::EC2::Model::InstanceTypeMapper::GetNameForInstanceType(
                                        instance.GetInstanceType());

                        Aws::String monitorString =
                                Aws::EC2::Model::MonitoringStateMapper::GetNameForMonitoringState(
                                        instance.GetMonitoring().GetState());
                        Aws::String name = "Unknown";

                        const std::vector<Aws::EC2::Model::Tag> &tags = instance.GetTags();
                        auto nameIter = std::find_if(tags.cbegin(), tags.cend(),
                                                     [](const Aws::EC2::Model::Tag &tag) {
                                                         return tag.GetKey() == "Name";
                                                     });
                        if (nameIter != tags.cend()) {
                            name = nameIter->GetValue();
                        }
                        std::cout <<
                                  std::setw(48) << name <<
                                  std::setw(20) << instance.GetInstanceId() <<
                                  std::setw(25) << instance.GetImageId() <<
                                  std::setw(15) << typeString <<
                                  std::setw(15) << instanceStateString <<
                                  std::setw(15) << monitorString << std::endl;
                    }
                }

                if (!outcome.GetResult().GetNextToken().empty()) {
                    request.SetNextToken(outcome.GetResult().GetNextToken());
                } else {
                    done = true;
                }
            } else {
                std::cerr << "Failed to describe EC2 instances:" <<
                          outcome.GetError().GetMessage() << std::endl;
                result = 1;
                break;
            }
        }
    }


    Aws::ShutdownAPI(options); // Should only be called once.
    return result;
}


```

- For API details, see
  [DescribeSecurityGroups](../../../goto/SdkForCpp/ec2-2016-11-15/DescribeSecurityGroups.md "../../../goto/SdkForCpp/ec2-2016-11-15/DescribeSecurityGroups.md")
  in _AWS SDK for C++ API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ec2#code-examples").

```

    /**
     * Asynchronously describes the security groups for the specified group ID.
     *
     * @param groupName the name of the security group to describe
     * @return a {@link CompletableFuture} that represents the asynchronous operation
     *         of describing the security groups. The future will complete with a
     *         {@link DescribeSecurityGroupsResponse} object that contains the
     *         security group information.
     */
    public CompletableFuture<String> describeSecurityGroupArnByNameAsync(String groupName) {
        DescribeSecurityGroupsRequest request = DescribeSecurityGroupsRequest.builder()
            .groupNames(groupName)
            .build();

        DescribeSecurityGroupsPublisher paginator = getAsyncClient().describeSecurityGroupsPaginator(request);
        AtomicReference<String> groupIdRef = new AtomicReference<>();
        return paginator.subscribe(response -> {
            response.securityGroups().stream()
                .filter(securityGroup -> securityGroup.groupName().equals(groupName))
                .findFirst()
                .ifPresent(securityGroup -> groupIdRef.set(securityGroup.groupId()));
        }).thenApply(v -> {
            String groupId = groupIdRef.get();
            if (groupId == null) {
                throw new RuntimeException("No security group found with the name: " + groupName);
            }
            return groupId;
        }).exceptionally(ex -> {
            logger.info("Failed to describe security group: " + ex.getMessage());
            throw new RuntimeException("Failed to describe security group", ex);
        });
    }


```

- For API details, see
  [DescribeSecurityGroups](../../../goto/SdkForJavaV2/ec2-2016-11-15/DescribeSecurityGroups.md "../../../goto/SdkForJavaV2/ec2-2016-11-15/DescribeSecurityGroups.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ec2#code-examples").

```

import { DescribeSecurityGroupsCommand, EC2Client } from "@aws-sdk/client-ec2";

// Call DescribeSecurityGroups and display the result.
export const main = async () => {
  const client = new EC2Client();
  try {
    const { SecurityGroups } = await client.send(
      new DescribeSecurityGroupsCommand({}),
    );

    const securityGroupList = SecurityGroups.slice(0, 9)
      .map((sg) => ` • ${sg.GroupId}: ${sg.GroupName}`)
      .join("\n");

    console.log(
      "Hello, Amazon EC2! Let's list up to 10 of your security groups:",
    );
    console.log(securityGroupList);
  } catch (err) {
    console.error(err);
  }
};

// Call function if run directly.
import { fileURLToPath } from "node:url";
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main();
}


```

- For API details, see
  [DescribeSecurityGroups](../../../AWSJavaScriptSDK/v3/latest/client/ec2/command/DescribeSecurityGroupsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/ec2/command/DescribeSecurityGroupsCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ec2#code-examples").

```
suspend fun describeEC2SecurityGroups(groupId: String) {
    val request =
        DescribeSecurityGroupsRequest {
            groupIds = listOf(groupId)
        }

    Ec2Client.fromEnvironment { region = "us-west-2" }.use { ec2 ->
        val response = ec2.describeSecurityGroups(request)
        response.securityGroups?.forEach { group ->
            println("Found Security Group with id ${group.groupId}, vpc id ${group.vpcId} and description ${group.description}")
        }
    }
}


```

- For API details, see
  [DescribeSecurityGroups](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ec2#code-examples").

```
def hello_ec2(ec2_client):
    """
    Use the AWS SDK for Python (Boto3) to list the security groups in your account.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param ec2_client: A Boto3 EC2 client. This client provides low-level
                       access to AWS EC2 services.
    """
    print("Hello, Amazon EC2! Let's list up to 10 of your security groups:")
    try:
        paginator = ec2_client.get_paginator("describe_security_groups")
        response_iterator = paginator.paginate(PaginationConfig={'MaxItems': 10}) # List only 10 security groups.
        logging.basicConfig(level=logging.INFO) # Enable logging.
        for page in response_iterator:
            for sg in page["SecurityGroups"]:
                logger.info(f"\t{sg['GroupId']}: {sg['GroupName']}")
    except ClientError as err:
        logger.error("Failed to list security groups.")
        if err.response["Error"]["Code"] == "AccessDeniedException":
            logger.error("You do not have permission to list security groups.")
        raise


if __name__ == "__main__":
    hello_ec2(boto3.client("ec2"))


```

- For API details, see
  [DescribeSecurityGroups](../../../goto/boto3/ec2-2016-11-15/DescribeSecurityGroups.md "../../../goto/boto3/ec2-2016-11-15/DescribeSecurityGroups.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/ec2#code-examples").

```

require 'aws-sdk-ec2'
require 'logger'

# EC2Manager is a class responsible for managing EC2 operations
# such as listing all EC2 instances in the current AWS account.
class EC2Manager
  def initialize(client)
    @client = client
    @logger = Logger.new($stdout)
  end

  # Lists and prints all EC2 instances in the current AWS account.
  def list_instances
    @logger.info('Listing instances')

    instances = fetch_instances

    if instances.empty?
      @logger.info('You have no instances')
    else
      print_instances(instances)
    end
  end

  private

  # Fetches all EC2 instances using pagination.
  #
  # @return [Array<Aws::EC2::Types::Instance>] List of EC2 instances.
  def fetch_instances
    paginator = @client.describe_instances
    instances = []

    paginator.each_page do |page|
      page.reservations.each do |reservation|
        reservation.instances.each do |instance|
          instances << instance
        end
      end
    end

    instances
  end

  # Prints details of the given EC2 instances.
  #
  # @param instances [Array<Aws::EC2::Types::Instance>] List of EC2 instances to print.
  def print_instances(instances)
    instances.each do |instance|
      @logger.info("Instance ID: #{instance.instance_id}")
      @logger.info("Instance Type: #{instance.instance_type}")
      @logger.info("Public IP: #{instance.public_ip_address}")
      @logger.info("Public DNS Name: #{instance.public_dns_name}")
      @logger.info("\n")
    end
  end
end

if $PROGRAM_NAME == __FILE__
  ec2_client = Aws::EC2::Client.new(region: 'us-west-2')
  manager = EC2Manager.new(ec2_client)
  manager.list_instances
end



```

- For API details, see
  [DescribeSecurityGroups](../../../goto/SdkForRubyV3/ec2-2016-11-15/DescribeSecurityGroups.md "../../../goto/SdkForRubyV3/ec2-2016-11-15/DescribeSecurityGroups.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ec2#code-examples").

```
async fn show_security_groups(client: &aws_sdk_ec2::Client, group_ids: Vec<String>) {
    let response = client
        .describe_security_groups()
        .set_group_ids(Some(group_ids))
        .send()
        .await;

    match response {
        Ok(output) => {
            for group in output.security_groups() {
                println!(
                    "Found Security Group {} ({}), vpc id {} and description {}",
                    group.group_name().unwrap_or("unknown"),
                    group.group_id().unwrap_or("id-unknown"),
                    group.vpc_id().unwrap_or("vpcid-unknown"),
                    group.description().unwrap_or("(none)")
                );
            }
        }
        Err(err) => {
            let err = err.into_service_error();
            let meta = err.meta();
            let message = meta.message().unwrap_or("unknown");
            let code = meta.code().unwrap_or("unknown");
            eprintln!("Error listing EC2 Security Groups: ({code}) {message}");
        }
    }
}


```

- For API details, see
  [DescribeSecurityGroups](https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_security_groups "https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_security_groups")
  in _AWS SDK for Rust API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/ec2#code-examples").

The `Package.swift` file.

```
// swift-tools-version: 5.9
//
// The swift-tools-version declares the minimum version of Swift required to
// build this package.

import PackageDescription

let package = Package(
    name: "hello-ec2",
    // Let Xcode know the minimum Apple platforms supported.
    platforms: [
        .macOS(.v13),
        .iOS(.v15)
    ],
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        .package(
            url: "https://github.com/awslabs/aws-sdk-swift",
            from: "1.0.0"),
        .package(
            url: "https://github.com/apple/swift-argument-parser.git",
            branch: "main"
        )
    ],
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products
        // from dependencies.
        .executableTarget(
            name: "hello-ec2",
            dependencies: [
                .product(name: "AWSEC2", package: "aws-sdk-swift"),
                .product(name: "ArgumentParser", package: "swift-argument-parser")
            ],
            path: "Sources")

    ]
)


```

The `entry.swift` file.

```
// An example that shows how to use the AWS SDK for Swift to perform a simple
// operation using Amazon Elastic Compute Cloud (EC2).
//

import ArgumentParser
import Foundation

import AWSEC2

struct ExampleCommand: ParsableCommand {
    @Option(help: "The AWS Region to run AWS API calls in.")
    var awsRegion = "us-east-1"

    @Option(
        help: ArgumentHelp("The level of logging for the Swift SDK to perform."),
        completion: .list([
            "critical",
            "debug",
            "error",
            "info",
            "notice",
            "trace",
            "warning"
        ])
    )
    var logLevel: String = "error"

    static var configuration = CommandConfiguration(
        commandName: "hello-ec2",
        abstract: """
        Demonstrates a simple operation using Amazon EC2.
        """,
        discussion: """
        An example showing how to make a call to Amazon EC2 using the AWS SDK for Swift.
        """
    )

    /// Return an array of strings giving the names of every security group
    /// the user is a member of.
    ///
    /// - Parameter ec2Client: The `EC2Client` to use when calling
    ///   `describeSecurityGroupsPaginated()`.
    ///
    /// - Returns: An array of strings giving the names of every security
    ///   group the user is a member of.
    func getSecurityGroupNames(ec2Client: EC2Client) async -> [String] {
        let pages = ec2Client.describeSecurityGroupsPaginated(
            input: DescribeSecurityGroupsInput()
        )

        var groupNames: [String] = []

        do {
            for try await page in pages {
                guard let groups = page.securityGroups else {
                    print("*** Error: No groups returned.")
                    continue
                }

                for group in groups {
                    groupNames.append(group.groupName ?? "<unknown>")
                }
            }
        } catch {
            print("*** Error: \(error.localizedDescription)")
        }

        return groupNames
    }

    /// Called by ``main()`` to run the bulk of the example.
    func runAsync() async throws {
        let ec2Config = try await EC2Client.EC2ClientConfiguration(region: awsRegion)
        let ec2Client = EC2Client(config: ec2Config)

        let groupNames = await getSecurityGroupNames(ec2Client: ec2Client)

        print("Found \(groupNames.count) security group(s):")

        for group in groupNames {
            print("    \(group)")
        }
    }
}

/// The program's asynchronous entry point.
@main
struct Main {
    static func main() async {
        let args = Array(CommandLine.arguments.dropFirst())

        do {
            let command = try ExampleCommand.parse(args)
            try await command.runAsync()
        } catch {
            ExampleCommand.exit(withError: error)
        }
    }
}


```

- For API details, see
  [DescribeSecurityGroups](<https://sdk.amazonaws.com/swift/api/awsec2/latest/documentation/awsec2/ec2client/describesecuritygroups(input:)> "https://sdk.amazonaws.com/swift/api/awsec2/latest/documentation/awsec2/ec2client/describesecuritygroups(input:)")
  in _AWS SDK for Swift API reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon EC2](example_ec2_Hello_section.md "example_ec2_Hello_section.md")
  - [Learn the basics](example_ec2_Scenario_GetStartedInstances_section.md "example_ec2_Scenario_GetStartedInstances_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [AcceptVpcPeeringConnection](example_ec2_AcceptVpcPeeringConnection_section.md "example_ec2_AcceptVpcPeeringConnection_section.md")
    - [AllocateAddress](example_ec2_AllocateAddress_section.md "example_ec2_AllocateAddress_section.md")
    - [AllocateHosts](example_ec2_AllocateHosts_section.md "example_ec2_AllocateHosts_section.md")
    - [AssignPrivateIpAddresses](example_ec2_AssignPrivateIpAddresses_section.md "example_ec2_AssignPrivateIpAddresses_section.md")
    - [AssociateAddress](example_ec2_AssociateAddress_section.md "example_ec2_AssociateAddress_section.md")
    - [AssociateDhcpOptions](example_ec2_AssociateDhcpOptions_section.md "example_ec2_AssociateDhcpOptions_section.md")
    - [AssociateRouteTable](example_ec2_AssociateRouteTable_section.md "example_ec2_AssociateRouteTable_section.md")
    - [AttachInternetGateway](example_ec2_AttachInternetGateway_section.md "example_ec2_AttachInternetGateway_section.md")
    - [AttachNetworkInterface](example_ec2_AttachNetworkInterface_section.md "example_ec2_AttachNetworkInterface_section.md")
    - [AttachVolume](example_ec2_AttachVolume_section.md "example_ec2_AttachVolume_section.md")
    - [AttachVpnGateway](example_ec2_AttachVpnGateway_section.md "example_ec2_AttachVpnGateway_section.md")
    - [AuthorizeSecurityGroupEgress](example_ec2_AuthorizeSecurityGroupEgress_section.md "example_ec2_AuthorizeSecurityGroupEgress_section.md")
    - [AuthorizeSecurityGroupIngress](example_ec2_AuthorizeSecurityGroupIngress_section.md "example_ec2_AuthorizeSecurityGroupIngress_section.md")
    - [CancelCapacityReservation](example_ec2_CancelCapacityReservation_section.md "example_ec2_CancelCapacityReservation_section.md")
    - [CancelImportTask](example_ec2_CancelImportTask_section.md "example_ec2_CancelImportTask_section.md")
    - [CancelSpotFleetRequests](example_ec2_CancelSpotFleetRequests_section.md "example_ec2_CancelSpotFleetRequests_section.md")
    - [CancelSpotInstanceRequests](example_ec2_CancelSpotInstanceRequests_section.md "example_ec2_CancelSpotInstanceRequests_section.md")
    - [ConfirmProductInstance](example_ec2_ConfirmProductInstance_section.md "example_ec2_ConfirmProductInstance_section.md")
    - [CopyImage](example_ec2_CopyImage_section.md "example_ec2_CopyImage_section.md")
    - [CopySnapshot](example_ec2_CopySnapshot_section.md "example_ec2_CopySnapshot_section.md")
    - [CreateCapacityReservation](example_ec2_CreateCapacityReservation_section.md "example_ec2_CreateCapacityReservation_section.md")
    - [CreateCustomerGateway](example_ec2_CreateCustomerGateway_section.md "example_ec2_CreateCustomerGateway_section.md")
    - [CreateDhcpOptions](example_ec2_CreateDhcpOptions_section.md "example_ec2_CreateDhcpOptions_section.md")
    - [CreateFlowLogs](example_ec2_CreateFlowLogs_section.md "example_ec2_CreateFlowLogs_section.md")
    - [CreateImage](example_ec2_CreateImage_section.md "example_ec2_CreateImage_section.md")
    - [CreateInstanceExportTask](example_ec2_CreateInstanceExportTask_section.md "example_ec2_CreateInstanceExportTask_section.md")
    - [CreateInternetGateway](example_ec2_CreateInternetGateway_section.md "example_ec2_CreateInternetGateway_section.md")
    - [CreateKeyPair](example_ec2_CreateKeyPair_section.md "example_ec2_CreateKeyPair_section.md")
    - [CreateLaunchTemplate](example_ec2_CreateLaunchTemplate_section.md "example_ec2_CreateLaunchTemplate_section.md")
    - [CreateNetworkAcl](example_ec2_CreateNetworkAcl_section.md "example_ec2_CreateNetworkAcl_section.md")
    - [CreateNetworkAclEntry](example_ec2_CreateNetworkAclEntry_section.md "example_ec2_CreateNetworkAclEntry_section.md")
    - [CreateNetworkInterface](example_ec2_CreateNetworkInterface_section.md "example_ec2_CreateNetworkInterface_section.md")
    - [CreatePlacementGroup](example_ec2_CreatePlacementGroup_section.md "example_ec2_CreatePlacementGroup_section.md")
    - [CreateRoute](example_ec2_CreateRoute_section.md "example_ec2_CreateRoute_section.md")
    - [CreateRouteTable](example_ec2_CreateRouteTable_section.md "example_ec2_CreateRouteTable_section.md")
    - [CreateSecurityGroup](example_ec2_CreateSecurityGroup_section.md "example_ec2_CreateSecurityGroup_section.md")
    - [CreateSnapshot](example_ec2_CreateSnapshot_section.md "example_ec2_CreateSnapshot_section.md")
    - [CreateSpotDatafeedSubscription](example_ec2_CreateSpotDatafeedSubscription_section.md "example_ec2_CreateSpotDatafeedSubscription_section.md")
    - [CreateSubnet](example_ec2_CreateSubnet_section.md "example_ec2_CreateSubnet_section.md")
    - [CreateTags](example_ec2_CreateTags_section.md "example_ec2_CreateTags_section.md")
    - [CreateVolume](example_ec2_CreateVolume_section.md "example_ec2_CreateVolume_section.md")
    - [CreateVpc](example_ec2_CreateVpc_section.md "example_ec2_CreateVpc_section.md")
    - [CreateVpcEndpoint](example_ec2_CreateVpcEndpoint_section.md "example_ec2_CreateVpcEndpoint_section.md")
    - [CreateVpnConnection](example_ec2_CreateVpnConnection_section.md "example_ec2_CreateVpnConnection_section.md")
    - [CreateVpnConnectionRoute](example_ec2_CreateVpnConnectionRoute_section.md "example_ec2_CreateVpnConnectionRoute_section.md")
    - [CreateVpnGateway](example_ec2_CreateVpnGateway_section.md "example_ec2_CreateVpnGateway_section.md")
    - [DeleteCustomerGateway](example_ec2_DeleteCustomerGateway_section.md "example_ec2_DeleteCustomerGateway_section.md")
    - [DeleteDhcpOptions](example_ec2_DeleteDhcpOptions_section.md "example_ec2_DeleteDhcpOptions_section.md")
    - [DeleteFlowLogs](example_ec2_DeleteFlowLogs_section.md "example_ec2_DeleteFlowLogs_section.md")
    - [DeleteInternetGateway](example_ec2_DeleteInternetGateway_section.md "example_ec2_DeleteInternetGateway_section.md")
    - [DeleteKeyPair](example_ec2_DeleteKeyPair_section.md "example_ec2_DeleteKeyPair_section.md")
    - [DeleteLaunchTemplate](example_ec2_DeleteLaunchTemplate_section.md "example_ec2_DeleteLaunchTemplate_section.md")
    - [DeleteNetworkAcl](example_ec2_DeleteNetworkAcl_section.md "example_ec2_DeleteNetworkAcl_section.md")
    - [DeleteNetworkAclEntry](example_ec2_DeleteNetworkAclEntry_section.md "example_ec2_DeleteNetworkAclEntry_section.md")
    - [DeleteNetworkInterface](example_ec2_DeleteNetworkInterface_section.md "example_ec2_DeleteNetworkInterface_section.md")
    - [DeletePlacementGroup](example_ec2_DeletePlacementGroup_section.md "example_ec2_DeletePlacementGroup_section.md")
    - [DeleteRoute](example_ec2_DeleteRoute_section.md "example_ec2_DeleteRoute_section.md")
    - [DeleteRouteTable](example_ec2_DeleteRouteTable_section.md "example_ec2_DeleteRouteTable_section.md")
    - [DeleteSecurityGroup](example_ec2_DeleteSecurityGroup_section.md "example_ec2_DeleteSecurityGroup_section.md")
    - [DeleteSnapshot](example_ec2_DeleteSnapshot_section.md "example_ec2_DeleteSnapshot_section.md")
    - [DeleteSpotDatafeedSubscription](example_ec2_DeleteSpotDatafeedSubscription_section.md "example_ec2_DeleteSpotDatafeedSubscription_section.md")
    - [DeleteSubnet](example_ec2_DeleteSubnet_section.md "example_ec2_DeleteSubnet_section.md")
    - [DeleteTags](example_ec2_DeleteTags_section.md "example_ec2_DeleteTags_section.md")
    - [DeleteVolume](example_ec2_DeleteVolume_section.md "example_ec2_DeleteVolume_section.md")
    - [DeleteVpc](example_ec2_DeleteVpc_section.md "example_ec2_DeleteVpc_section.md")
    - [DeleteVpcEndpoints](example_ec2_DeleteVpcEndpoints_section.md "example_ec2_DeleteVpcEndpoints_section.md")
    - [DeleteVpnConnection](example_ec2_DeleteVpnConnection_section.md "example_ec2_DeleteVpnConnection_section.md")
    - [DeleteVpnConnectionRoute](example_ec2_DeleteVpnConnectionRoute_section.md "example_ec2_DeleteVpnConnectionRoute_section.md")
    - [DeleteVpnGateway](example_ec2_DeleteVpnGateway_section.md "example_ec2_DeleteVpnGateway_section.md")
    - [DeregisterImage](example_ec2_DeregisterImage_section.md "example_ec2_DeregisterImage_section.md")
    - [DescribeAccountAttributes](example_ec2_DescribeAccountAttributes_section.md "example_ec2_DescribeAccountAttributes_section.md")
    - [DescribeAddresses](example_ec2_DescribeAddresses_section.md "example_ec2_DescribeAddresses_section.md")
    - [DescribeAvailabilityZones](example_ec2_DescribeAvailabilityZones_section.md "example_ec2_DescribeAvailabilityZones_section.md")
    - [DescribeBundleTasks](example_ec2_DescribeBundleTasks_section.md "example_ec2_DescribeBundleTasks_section.md")
    - [DescribeCapacityReservations](example_ec2_DescribeCapacityReservations_section.md "example_ec2_DescribeCapacityReservations_section.md")
    - [DescribeCustomerGateways](example_ec2_DescribeCustomerGateways_section.md "example_ec2_DescribeCustomerGateways_section.md")
    - [DescribeDhcpOptions](example_ec2_DescribeDhcpOptions_section.md "example_ec2_DescribeDhcpOptions_section.md")
    - [DescribeFlowLogs](example_ec2_DescribeFlowLogs_section.md "example_ec2_DescribeFlowLogs_section.md")
    - [DescribeHostReservationOfferings](example_ec2_DescribeHostReservationOfferings_section.md "example_ec2_DescribeHostReservationOfferings_section.md")
    - [DescribeHosts](example_ec2_DescribeHosts_section.md "example_ec2_DescribeHosts_section.md")
    - [DescribeIamInstanceProfileAssociations](example_ec2_DescribeIamInstanceProfileAssociations_section.md "example_ec2_DescribeIamInstanceProfileAssociations_section.md")
    - [DescribeIdFormat](example_ec2_DescribeIdFormat_section.md "example_ec2_DescribeIdFormat_section.md")
    - [DescribeIdentityIdFormat](example_ec2_DescribeIdentityIdFormat_section.md "example_ec2_DescribeIdentityIdFormat_section.md")
    - [DescribeImageAttribute](example_ec2_DescribeImageAttribute_section.md "example_ec2_DescribeImageAttribute_section.md")
    - [DescribeImages](example_ec2_DescribeImages_section.md "example_ec2_DescribeImages_section.md")
    - [DescribeImportImageTasks](example_ec2_DescribeImportImageTasks_section.md "example_ec2_DescribeImportImageTasks_section.md")
    - [DescribeImportSnapshotTasks](example_ec2_DescribeImportSnapshotTasks_section.md "example_ec2_DescribeImportSnapshotTasks_section.md")
    - [DescribeInstanceAttribute](example_ec2_DescribeInstanceAttribute_section.md "example_ec2_DescribeInstanceAttribute_section.md")
    - [DescribeInstanceStatus](example_ec2_DescribeInstanceStatus_section.md "example_ec2_DescribeInstanceStatus_section.md")
    - [DescribeInstanceTypes](example_ec2_DescribeInstanceTypes_section.md "example_ec2_DescribeInstanceTypes_section.md")
    - [DescribeInstances](example_ec2_DescribeInstances_section.md "example_ec2_DescribeInstances_section.md")
    - [DescribeInternetGateways](example_ec2_DescribeInternetGateways_section.md "example_ec2_DescribeInternetGateways_section.md")
    - [DescribeKeyPairs](example_ec2_DescribeKeyPairs_section.md "example_ec2_DescribeKeyPairs_section.md")
    - [DescribeNetworkAcls](example_ec2_DescribeNetworkAcls_section.md "example_ec2_DescribeNetworkAcls_section.md")
    - [DescribeNetworkInterfaceAttribute](example_ec2_DescribeNetworkInterfaceAttribute_section.md "example_ec2_DescribeNetworkInterfaceAttribute_section.md")
    - [DescribeNetworkInterfaces](example_ec2_DescribeNetworkInterfaces_section.md "example_ec2_DescribeNetworkInterfaces_section.md")
    - [DescribePlacementGroups](example_ec2_DescribePlacementGroups_section.md "example_ec2_DescribePlacementGroups_section.md")
    - [DescribePrefixLists](example_ec2_DescribePrefixLists_section.md "example_ec2_DescribePrefixLists_section.md")
    - [DescribeRegions](example_ec2_DescribeRegions_section.md "example_ec2_DescribeRegions_section.md")
    - [DescribeRouteTables](example_ec2_DescribeRouteTables_section.md "example_ec2_DescribeRouteTables_section.md")
    - [DescribeScheduledInstanceAvailability](example_ec2_DescribeScheduledInstanceAvailability_section.md "example_ec2_DescribeScheduledInstanceAvailability_section.md")
    - [DescribeScheduledInstances](example_ec2_DescribeScheduledInstances_section.md "example_ec2_DescribeScheduledInstances_section.md")
    - [DescribeSecurityGroups](example_ec2_DescribeSecurityGroups_section.md "example_ec2_DescribeSecurityGroups_section.md")
    - [DescribeSnapshotAttribute](example_ec2_DescribeSnapshotAttribute_section.md "example_ec2_DescribeSnapshotAttribute_section.md")
    - [DescribeSnapshots](example_ec2_DescribeSnapshots_section.md "example_ec2_DescribeSnapshots_section.md")
    - [DescribeSpotDatafeedSubscription](example_ec2_DescribeSpotDatafeedSubscription_section.md "example_ec2_DescribeSpotDatafeedSubscription_section.md")
    - [DescribeSpotFleetInstances](example_ec2_DescribeSpotFleetInstances_section.md "example_ec2_DescribeSpotFleetInstances_section.md")
    - [DescribeSpotFleetRequestHistory](example_ec2_DescribeSpotFleetRequestHistory_section.md "example_ec2_DescribeSpotFleetRequestHistory_section.md")
    - [DescribeSpotFleetRequests](example_ec2_DescribeSpotFleetRequests_section.md "example_ec2_DescribeSpotFleetRequests_section.md")
    - [DescribeSpotInstanceRequests](example_ec2_DescribeSpotInstanceRequests_section.md "example_ec2_DescribeSpotInstanceRequests_section.md")
    - [DescribeSpotPriceHistory](example_ec2_DescribeSpotPriceHistory_section.md "example_ec2_DescribeSpotPriceHistory_section.md")
    - [DescribeSubnets](example_ec2_DescribeSubnets_section.md "example_ec2_DescribeSubnets_section.md")
    - [DescribeTags](example_ec2_DescribeTags_section.md "example_ec2_DescribeTags_section.md")
    - [DescribeVolumeAttribute](example_ec2_DescribeVolumeAttribute_section.md "example_ec2_DescribeVolumeAttribute_section.md")
    - [DescribeVolumeStatus](example_ec2_DescribeVolumeStatus_section.md "example_ec2_DescribeVolumeStatus_section.md")
    - [DescribeVolumes](example_ec2_DescribeVolumes_section.md "example_ec2_DescribeVolumes_section.md")
    - [DescribeVpcAttribute](example_ec2_DescribeVpcAttribute_section.md "example_ec2_DescribeVpcAttribute_section.md")
    - [DescribeVpcClassicLink](example_ec2_DescribeVpcClassicLink_section.md "example_ec2_DescribeVpcClassicLink_section.md")
    - [DescribeVpcClassicLinkDnsSupport](example_ec2_DescribeVpcClassicLinkDnsSupport_section.md "example_ec2_DescribeVpcClassicLinkDnsSupport_section.md")
    - [DescribeVpcEndpointServices](example_ec2_DescribeVpcEndpointServices_section.md "example_ec2_DescribeVpcEndpointServices_section.md")
    - [DescribeVpcEndpoints](example_ec2_DescribeVpcEndpoints_section.md "example_ec2_DescribeVpcEndpoints_section.md")
    - [DescribeVpcs](example_ec2_DescribeVpcs_section.md "example_ec2_DescribeVpcs_section.md")
    - [DescribeVpnConnections](example_ec2_DescribeVpnConnections_section.md "example_ec2_DescribeVpnConnections_section.md")
    - [DescribeVpnGateways](example_ec2_DescribeVpnGateways_section.md "example_ec2_DescribeVpnGateways_section.md")
    - [DetachInternetGateway](example_ec2_DetachInternetGateway_section.md "example_ec2_DetachInternetGateway_section.md")
    - [DetachNetworkInterface](example_ec2_DetachNetworkInterface_section.md "example_ec2_DetachNetworkInterface_section.md")
    - [DetachVolume](example_ec2_DetachVolume_section.md "example_ec2_DetachVolume_section.md")
    - [DetachVpnGateway](example_ec2_DetachVpnGateway_section.md "example_ec2_DetachVpnGateway_section.md")
    - [DisableVgwRoutePropagation](example_ec2_DisableVgwRoutePropagation_section.md "example_ec2_DisableVgwRoutePropagation_section.md")
    - [DisableVpcClassicLink](example_ec2_DisableVpcClassicLink_section.md "example_ec2_DisableVpcClassicLink_section.md")
    - [DisableVpcClassicLinkDnsSupport](example_ec2_DisableVpcClassicLinkDnsSupport_section.md "example_ec2_DisableVpcClassicLinkDnsSupport_section.md")
    - [DisassociateAddress](example_ec2_DisassociateAddress_section.md "example_ec2_DisassociateAddress_section.md")
    - [DisassociateRouteTable](example_ec2_DisassociateRouteTable_section.md "example_ec2_DisassociateRouteTable_section.md")
    - [EnableVgwRoutePropagation](example_ec2_EnableVgwRoutePropagation_section.md "example_ec2_EnableVgwRoutePropagation_section.md")
    - [EnableVolumeIo](example_ec2_EnableVolumeIo_section.md "example_ec2_EnableVolumeIo_section.md")
    - [EnableVpcClassicLink](example_ec2_EnableVpcClassicLink_section.md "example_ec2_EnableVpcClassicLink_section.md")
    - [EnableVpcClassicLinkDnsSupport](example_ec2_EnableVpcClassicLinkDnsSupport_section.md "example_ec2_EnableVpcClassicLinkDnsSupport_section.md")
    - [GetConsoleOutput](example_ec2_GetConsoleOutput_section.md "example_ec2_GetConsoleOutput_section.md")
    - [GetHostReservationPurchasePreview](example_ec2_GetHostReservationPurchasePreview_section.md "example_ec2_GetHostReservationPurchasePreview_section.md")
    - [GetPasswordData](example_ec2_GetPasswordData_section.md "example_ec2_GetPasswordData_section.md")
    - [ImportImage](example_ec2_ImportImage_section.md "example_ec2_ImportImage_section.md")
    - [ImportKeyPair](example_ec2_ImportKeyPair_section.md "example_ec2_ImportKeyPair_section.md")
    - [ImportSnapshot](example_ec2_ImportSnapshot_section.md "example_ec2_ImportSnapshot_section.md")
    - [ModifyCapacityReservation](example_ec2_ModifyCapacityReservation_section.md "example_ec2_ModifyCapacityReservation_section.md")
    - [ModifyHosts](example_ec2_ModifyHosts_section.md "example_ec2_ModifyHosts_section.md")
    - [ModifyIdFormat](example_ec2_ModifyIdFormat_section.md "example_ec2_ModifyIdFormat_section.md")
    - [ModifyImageAttribute](example_ec2_ModifyImageAttribute_section.md "example_ec2_ModifyImageAttribute_section.md")
    - [ModifyInstanceAttribute](example_ec2_ModifyInstanceAttribute_section.md "example_ec2_ModifyInstanceAttribute_section.md")
    - [ModifyInstanceCreditSpecification](example_ec2_ModifyInstanceCreditSpecification_section.md "example_ec2_ModifyInstanceCreditSpecification_section.md")
    - [ModifyNetworkInterfaceAttribute](example_ec2_ModifyNetworkInterfaceAttribute_section.md "example_ec2_ModifyNetworkInterfaceAttribute_section.md")
    - [ModifyReservedInstances](example_ec2_ModifyReservedInstances_section.md "example_ec2_ModifyReservedInstances_section.md")
    - [ModifySnapshotAttribute](example_ec2_ModifySnapshotAttribute_section.md "example_ec2_ModifySnapshotAttribute_section.md")
    - [ModifySpotFleetRequest](example_ec2_ModifySpotFleetRequest_section.md "example_ec2_ModifySpotFleetRequest_section.md")
    - [ModifySubnetAttribute](example_ec2_ModifySubnetAttribute_section.md "example_ec2_ModifySubnetAttribute_section.md")
    - [ModifyVolumeAttribute](example_ec2_ModifyVolumeAttribute_section.md "example_ec2_ModifyVolumeAttribute_section.md")
    - [ModifyVpcAttribute](example_ec2_ModifyVpcAttribute_section.md "example_ec2_ModifyVpcAttribute_section.md")
    - [MonitorInstances](example_ec2_MonitorInstances_section.md "example_ec2_MonitorInstances_section.md")
    - [MoveAddressToVpc](example_ec2_MoveAddressToVpc_section.md "example_ec2_MoveAddressToVpc_section.md")
    - [PurchaseHostReservation](example_ec2_PurchaseHostReservation_section.md "example_ec2_PurchaseHostReservation_section.md")
    - [PurchaseScheduledInstances](example_ec2_PurchaseScheduledInstances_section.md "example_ec2_PurchaseScheduledInstances_section.md")
    - [RebootInstances](example_ec2_RebootInstances_section.md "example_ec2_RebootInstances_section.md")
    - [RegisterImage](example_ec2_RegisterImage_section.md "example_ec2_RegisterImage_section.md")
    - [RejectVpcPeeringConnection](example_ec2_RejectVpcPeeringConnection_section.md "example_ec2_RejectVpcPeeringConnection_section.md")
    - [ReleaseAddress](example_ec2_ReleaseAddress_section.md "example_ec2_ReleaseAddress_section.md")
    - [ReleaseHosts](example_ec2_ReleaseHosts_section.md "example_ec2_ReleaseHosts_section.md")
    - [ReplaceIamInstanceProfileAssociation](example_ec2_ReplaceIamInstanceProfileAssociation_section.md "example_ec2_ReplaceIamInstanceProfileAssociation_section.md")
    - [ReplaceNetworkAclAssociation](example_ec2_ReplaceNetworkAclAssociation_section.md "example_ec2_ReplaceNetworkAclAssociation_section.md")
    - [ReplaceNetworkAclEntry](example_ec2_ReplaceNetworkAclEntry_section.md "example_ec2_ReplaceNetworkAclEntry_section.md")
    - [ReplaceRoute](example_ec2_ReplaceRoute_section.md "example_ec2_ReplaceRoute_section.md")
    - [ReplaceRouteTableAssociation](example_ec2_ReplaceRouteTableAssociation_section.md "example_ec2_ReplaceRouteTableAssociation_section.md")
    - [ReportInstanceStatus](example_ec2_ReportInstanceStatus_section.md "example_ec2_ReportInstanceStatus_section.md")
    - [RequestSpotFleet](example_ec2_RequestSpotFleet_section.md "example_ec2_RequestSpotFleet_section.md")
    - [RequestSpotInstances](example_ec2_RequestSpotInstances_section.md "example_ec2_RequestSpotInstances_section.md")
    - [ResetImageAttribute](example_ec2_ResetImageAttribute_section.md "example_ec2_ResetImageAttribute_section.md")
    - [ResetInstanceAttribute](example_ec2_ResetInstanceAttribute_section.md "example_ec2_ResetInstanceAttribute_section.md")
    - [ResetNetworkInterfaceAttribute](example_ec2_ResetNetworkInterfaceAttribute_section.md "example_ec2_ResetNetworkInterfaceAttribute_section.md")
    - [ResetSnapshotAttribute](example_ec2_ResetSnapshotAttribute_section.md "example_ec2_ResetSnapshotAttribute_section.md")
    - [RevokeSecurityGroupEgress](example_ec2_RevokeSecurityGroupEgress_section.md "example_ec2_RevokeSecurityGroupEgress_section.md")
    - [RevokeSecurityGroupIngress](example_ec2_RevokeSecurityGroupIngress_section.md "example_ec2_RevokeSecurityGroupIngress_section.md")
    - [RunInstances](example_ec2_RunInstances_section.md "example_ec2_RunInstances_section.md")
    - [RunScheduledInstances](example_ec2_RunScheduledInstances_section.md "example_ec2_RunScheduledInstances_section.md")
    - [StartInstances](example_ec2_StartInstances_section.md "example_ec2_StartInstances_section.md")
    - [StopInstances](example_ec2_StopInstances_section.md "example_ec2_StopInstances_section.md")
    - [TerminateInstances](example_ec2_TerminateInstances_section.md "example_ec2_TerminateInstances_section.md")
    - [UnassignPrivateIpAddresses](example_ec2_UnassignPrivateIpAddresses_section.md "example_ec2_UnassignPrivateIpAddresses_section.md")
    - [UnmonitorInstances](example_ec2_UnmonitorInstances_section.md "example_ec2_UnmonitorInstances_section.md")
    - [UpdateSecurityGroupRuleDescriptionsIngress](example_ec2_UpdateSecurityGroupRuleDescriptionsIngress_section.md "example_ec2_UpdateSecurityGroupRuleDescriptionsIngress_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Build and manage a resilient service](example_cross_ResilientService_section.md "example_cross_ResilientService_section.md")
  - [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")
  - [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")
  - [Get started with Transit Gateway](example_vpc_TransitGatewayGettingStarted_section.md "example_vpc_TransitGatewayGettingStarted_section.md")
  - [Get started with VPC IPAM](example_vpc_GettingStartedIpam_section.md "example_vpc_GettingStartedIpam_section.md")
