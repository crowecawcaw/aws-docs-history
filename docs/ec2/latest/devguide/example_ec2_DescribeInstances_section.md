# Use `DescribeInstances` with an AWS SDK or CLI

The following code examples show how to use `DescribeInstances`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Learn the basics](example_ec2_Scenario_GetStartedInstances_section.md "example_ec2_Scenario_GetStartedInstances_section.md")
- [Build and manage a resilient service](example_cross_ResilientService_section.md "example_cross_ResilientService_section.md")
- [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EC2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EC2#code-examples").

```
    /// <summary>
    /// Get information about EC2 instances with a particular state.
    /// </summary>
    /// <param name="tagName">The name of the tag to filter on.</param>
    /// <param name="tagValue">The value of the tag to look for.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> GetInstancesWithState(string state)
    {
        try
        {
            // Filters the results of the instance list.
            var filters = new List<Filter>
            {
                new Filter
                {
                    Name = $"instance-state-name",
                    Values = new List<string> { state, },
                },
            };
            var request = new DescribeInstancesRequest { Filters = filters, };

            Console.WriteLine($"\nShowing instances with state {state}");
            var paginator = _amazonEC2.Paginators.DescribeInstances(request);

            await foreach (var response in paginator.Responses)
            {
                foreach (var reservation in response.Reservations)
                {
                    foreach (var instance in reservation.Instances)
                    {
                        Console.Write($"Instance ID: {instance.InstanceId} ");
                        Console.WriteLine($"\tCurrent State: {instance.State.Name}");
                    }
                }
            }

            return true;
        }
        catch (AmazonEC2Exception ec2Exception)
        {
            if (ec2Exception.ErrorCode == "InvalidParameterValue")
            {
                _logger.LogError(
                    $"Invalid parameter value for filtering instances.");
            }

            return false;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Couldn't list instances because: {ex.Message}");
            return false;
        }
    }


```

- For API details, see
  [DescribeInstances](../../../goto/DotNetSDKV3/ec2-2016-11-15/DescribeInstances.md "../../../goto/DotNetSDKV3/ec2-2016-11-15/DescribeInstances.md")
  in _AWS SDK for .NET API Reference_.

Bash

**AWS CLI with Bash script**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/ec2#code-examples").

```
###############################################################################
# function ec2_describe_instances
#
# This function describes one or more Amazon Elastic Compute Cloud (Amazon EC2) instances.
#
# Parameters:
#       -i instance_id - The ID of the instance to describe (optional).
#       -q query - The query to filter the response (optional).
#       -h - Display help.
#
# Returns:
#       0 - If successful.
#       1 - If it fails.
###############################################################################
function ec2_describe_instances() {
  local instance_id query response
  local option OPTARG # Required to use getopts command in a function.

  # bashsupport disable=BP5008
  function usage() {
    echo "function ec2_describe_instances"
    echo "Describes one or more Amazon Elastic Compute Cloud (Amazon EC2) instances."
    echo "  -i instance_id - The ID of the instance to describe (optional)."
    echo "  -q query - The query to filter the response (optional)."
    echo "  -h - Display help."
    echo ""
  }

  # Retrieve the calling parameters.
  while getopts "i:q:h" option; do
    case "${option}" in
      i) instance_id="${OPTARG}" ;;
      q) query="${OPTARG}" ;;
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

  local aws_cli_args=()

  if [[ -n "$instance_id" ]]; then
    # shellcheck disable=SC2206
    aws_cli_args+=("--instance-ids" $instance_id)
  fi

  local query_arg=""
  if [[ -n "$query" ]]; then
    query_arg="--query '$query'"
  else
    query_arg="--query Reservations[*].Instances[*].[InstanceId,ImageId,InstanceType,KeyName,VpcId,PublicIpAddress,State.Name]"
  fi

  # shellcheck disable=SC2086
  response=$(aws ec2 describe-instances \
    "${aws_cli_args[@]}" \
    $query_arg \
    --output text) || {
    aws_cli_error_log ${?}
    errecho "ERROR: AWS reports describe-instances operation failed.$response"
    return 1
  }

  echo "$response"

  return 0
}


```

The utility functions used in this example.

```
###############################################################################
# function errecho
#
# This function outputs everything sent to it to STDERR (standard error output).
###############################################################################
function errecho() {
  printf "%s\n" "$*" 1>&2
}

##############################################################################
# function aws_cli_error_log()
#
# This function is used to log the error messages from the AWS CLI.
#
# The function expects the following argument:
#         $1 - The error code returned by the AWS CLI.
#
#  Returns:
#          0: - Success.
#
##############################################################################
function aws_cli_error_log() {
  local err_code=$1
  errecho "Error code : $err_code"
  if [ "$err_code" == 1 ]; then
    errecho "  One or more S3 transfers failed."
  elif [ "$err_code" == 2 ]; then
    errecho "  Command line failed to parse."
  elif [ "$err_code" == 130 ]; then
    errecho "  Process received SIGINT."
  elif [ "$err_code" == 252 ]; then
    errecho "  Command syntax invalid."
  elif [ "$err_code" == 253 ]; then
    errecho "  The system environment or configuration was invalid."
  elif [ "$err_code" == 254 ]; then
    errecho "  The service returned an error."
  elif [ "$err_code" == 255 ]; then
    errecho "  255 is a catch-all error."
  fi

  return 0
}


```

- For API details, see
  [DescribeInstances](../../../goto/aws-cli/ec2-2016-11-15/DescribeInstances.md "../../../goto/aws-cli/ec2-2016-11-15/DescribeInstances.md")
  in _AWS CLI Command Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/ec2#code-examples").

```
//! Describe all Amazon Elastic Compute Cloud (Amazon EC2) instances associated with an account.
/*!
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::EC2::describeInstances(
        const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::EC2::EC2Client ec2Client(clientConfiguration);
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
            return false;
        }
    }

    return true;
}


```

- For API details, see
  [DescribeInstances](../../../goto/SdkForCpp/ec2-2016-11-15/DescribeInstances.md "../../../goto/SdkForCpp/ec2-2016-11-15/DescribeInstances.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**Example 1: To describe an instance**

The following `describe-instances` example describes the specified instance.

```
`aws ec2 describe-instances \
 --instance-ids `i-1234567890abcdef0``

```

Output:

```
{
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-0abcdef1234567890",
                    "InstanceId": "i-1234567890abcdef0",
                    "InstanceType": "t3.nano",
                    "KeyName": "my-key-pair",
                    "LaunchTime": "2022-11-15T10:48:59+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "us-east-2a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                    "PrivateIpAddress": "10-0-0-157",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com",
                    "PublicIpAddress": "34.253.223.13",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-04a636d18e83cfacb",
                    "VpcId": "vpc-1234567890abcdef0",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2022-11-15T10:49:00+00:00",
                                "DeleteOnTermination": true,
                                "Status": "attached",
                                "VolumeId": "vol-02e6ccdca7de29cf2"
                            }
                        }
                    ],
                    "ClientToken": "1234abcd-1234-abcd-1234-d46a8903e9bc",
                    "EbsOptimized": true,
                    "EnaSupport": true,
                    "Hypervisor": "xen",
                    "IamInstanceProfile": {
                        "Arn": "arn:aws:iam::111111111111:instance-profile/AmazonSSMRoleForInstancesQuickSetup",
                        "Id": "111111111111111111111"
                    },
                    "NetworkInterfaces": [
                        {
                            "Association": {
                                "IpOwnerId": "amazon",
                                "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com",
                                "PublicIp": "34.253.223.13"
                            },
                            "Attachment": {
                                "AttachTime": "2022-11-15T10:48:59+00:00",
                                "AttachmentId": "eni-attach-1234567890abcdefg",
                                "DeleteOnTermination": true,
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "launch-wizard-146",
                                    "GroupId": "sg-1234567890abcdefg"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "00:11:22:33:44:55",
                            "NetworkInterfaceId": "eni-1234567890abcdefg",
                            "OwnerId": "104024344472",
                            "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                            "PrivateIpAddress": "10-0-0-157",
                            "PrivateIpAddresses": [
                                {
                                    "Association": {
                                        "IpOwnerId": "amazon",
                                        "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com",
                                        "PublicIp": "34.253.223.13"
                                    },
                                    "Primary": true,
                                    "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                                    "PrivateIpAddress": "10-0-0-157"
                                }
                            ],
                            "SourceDestCheck": true,
                            "Status": "in-use",
                            "SubnetId": "subnet-1234567890abcdefg",
                            "VpcId": "vpc-1234567890abcdefg",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-146",
                            "GroupId": "sg-1234567890abcdefg"
                        }
                    ],
                    "SourceDestCheck": true,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "my-instance"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 2
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": false
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "enabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": false
                    },
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2022-11-15T10:48:59+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": true,
                        "EnableResourceNameDnsAAAARecord": false
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                }
            ],
            "OwnerId": "111111111111",
            "ReservationId": "r-1234567890abcdefg"
        }
    ]
}
```

**Example 2: To filter for instances with the specified type**

The following `describe-instances` example uses filters to scope the results to instances of the specified type.

```
`aws ec2 describe-instances \
 --filters `Name=instance-type,Values=m5.large``

```

For example output, see Example 1.

For more information, see [List and filter using the CLI](../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI "../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI") in the _Amazon EC2 User Guide_.

**Example 3: To filter for instances with the specified type and Availability Zone**

The following `describe-instances` example uses multiple filters to scope the results to instances with the specified type that are also in the specified Availability Zone.

```
`aws ec2 describe-instances \
 --filters `Name=instance-type,Values=t2.micro,t3.micro` `Name=availability-zone,Values=us-east-2c``

```

For example output, see Example 1.

**Example 4: To filter for instances with the specified type and Availability Zone using a JSON file**

The following `describe-instances` example uses a JSON input file to perform the same filtering as the previous example. When filters get more complicated, they can be easier to specify in a JSON file.

```
`aws ec2 describe-instances \
 --filters `file://filters.json``

```

Contents of `filters.json`:

```
[
    {
        "Name": "instance-type",
        "Values": ["t2.micro", "t3.micro"]
    },
    {
        "Name": "availability-zone",
        "Values": ["us-east-2c"]
    }
]
```

For example output, see Example 1.

**Example 5: To filter for instances with the specified Owner tag**

The following `describe-instances` example uses tag filters to scope the results to instances that have a tag with the specified tag key (Owner), regardless of the tag value.

```
`aws ec2 describe-instances \
 --filters `"Name=tag-key,Values=Owner"``

```

For example output, see Example 1.

**Example 6: To filter for instances with the specified my-team tag value**

The following `describe-instances` example uses tag filters to scope the results to instances that have a tag with the specified tag value (my-team), regardless of the tag key.

```
`aws ec2 describe-instances \
 --filters `"Name=tag-value,Values=my-team"``

```

For example output, see Example 1.

**Example 7: To filter for instances with the specified Owner tag and my-team value**

The following `describe-instances` example uses tag filters to scope the results to instances that have the specified tag (Owner=my-team).

```
`aws ec2 describe-instances \
 --filters `"Name=tag:Owner,Values=my-team"``

```

For example output, see Example 1.

**Example 8: To display only instance and subnet IDs for all instances**

The following `describe-instances` examples use the `--query` parameter to display only the instance and subnet IDs for all instances, in JSON format.

Linux and macOS:

```
`aws ec2 describe-instances \
 --query '`Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId}`' \
 --output `json``

```

Windows:

```
`aws ec2 describe-instances `^`
 --query `"Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId}"` `^`
 --output `json``

```

Output:

```
[
    {
        "Instance": "i-057750d42936e468a",
        "Subnet": "subnet-069beee9b12030077"
    },
    {
        "Instance": "i-001efd250faaa6ffa",
        "Subnet": "subnet-0b715c6b7db68927a"
    },
    {
        "Instance": "i-027552a73f021f3bd",
        "Subnet": "subnet-0250c25a1f4e15235"
    }
    ...
]
```

**Example 9: To filter instances of the specified type and only display their instance IDs**

The following `describe-instances` example uses filters to scope the results to instances of the specified type and the `--query` parameter to display only the instance IDs.

```
`aws ec2 describe-instances \
 --filters `"Name=instance-type,Values=t2.micro"` \
 --query `"Reservations[*].Instances[*].[InstanceId]"` \
 --output `text``

```

Output:

```
i-031c0dc19de2fb70c
i-00d8bff789a736b75
i-0b715c6b7db68927a
i-0626d4edd54f1286d
i-00b8ae04f9f99908e
i-0fc71c25d2374130c
```

**Example 10: To filter instances of the specified type and only display their instance IDs, Availability Zone, and the specified tag value**

The following `describe-instances` examples display the instance ID, Availability Zone, and the value of the `Name` tag for instances that have a tag with the name `tag-key`, in table format.

Linux and macOS:

```
`aws ec2 describe-instances \
 --filters `Name=tag-key,Values=Name` \
 --query '`Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==`Name`]|[0].Value}`' \
 --output `table``

```

Windows:

```
`aws ec2 describe-instances `^`
 --filters `Name=tag-key,Values=Name` `^`
 --query `"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}"` `^`
 --output `table``

```

Output:

````
-------------------------------------------------------------
|                     DescribeInstances                     | +--------------+-----------------------+--------------------+
|      AZ      |       Instance        |        Name        | +--------------+-----------------------+--------------------+
|  us-east-2b  |  i-057750d42936e468a  |  my-prod-server    |
|  us-east-2a  |  i-001efd250faaa6ffa  |  test-server-1     |
|  us-east-2a  |  i-027552a73f021f3bd  |  test-server-2     | +--------------+-----------------------+--------------------+ ``` **Example 11: To describe instances in a partition placement group** The following `describe-instances` example describes the specified instance. The output includes the placement information for the instance, which contains the placement group name and the partition number for the instance. ``` `aws ec2 describe-instances \ --instance-ids `i-0123a456700123456` \ --query `"Reservations[*].Instances[*].Placement"`` ``` Output: ``` [ [ { "AvailabilityZone": "us-east-1c", "GroupName": "HDFS-Group-A", "PartitionNumber": 3, "Tenancy": "default" } ] ] ``` For more information, see [Describing instances in a placement group](../../../AWSEC2/latest/UserGuide/placement-groups.md#describe-instance-placement "../../../AWSEC2/latest/UserGuide/placement-groups.md#describe-instance-placement") in the *Amazon EC2 User Guide*. **Example 12: To filter to instances with the specified placement group and partition number** The following `describe-instances` example filters the results to only those instances with the specified placement group and partition number. ``` `aws ec2 describe-instances \ --filters `"Name=placement-group-name,Values=HDFS-Group-A"` `"Name=placement-partition-number,Values=7"`` ``` The following shows only the relevant information from the output. ``` "Instances": [ { "InstanceId": "i-0123a456700123456", "InstanceType": "r4.large", "Placement": { "AvailabilityZone": "us-east-1c", "GroupName": "HDFS-Group-A", "PartitionNumber": 7, "Tenancy": "default" } }, { "InstanceId": "i-9876a543210987654", "InstanceType": "r4.large", "Placement": { "AvailabilityZone": "us-east-1c", "GroupName": "HDFS-Group-A", "PartitionNumber": 7, "Tenancy": "default" } ], ``` For more information, see [Describing instances in a placement group](../../../AWSEC2/latest/UserGuide/placement-groups.md#describe-instance-placement "../../../AWSEC2/latest/UserGuide/placement-groups.md#describe-instance-placement") in the *Amazon EC2 User Guide*. **Example 13: To filter to instances that are configured to allow access to tags from instance metadata** The following `describe-instances` example filters the results to only those instances that are configured to allow access to instance tags from instance metadata. ``` `aws ec2 describe-instances \ --filters `"Name=metadata-options.instance-metadata-tags,Values=enabled"` \ --query `"Reservations[*].Instances[*].InstanceId"` \ --output `text`` ``` The following shows the expected output. ``` i-1234567890abcdefg i-abcdefg1234567890 i-11111111aaaaaaaaa i-aaaaaaaa111111111 ``` For more information, see [Work with instance tags in instance metadata](../../../en_us/AWSEC2/latest/UserGuide/Using_Tags.md#view-access-to-tags-in-IMDS "../../../en_us/AWSEC2/latest/UserGuide/Using_Tags.md#view-access-to-tags-in-IMDS") in the *Amazon EC2 User Guide*. <br>• For API details, see [DescribeInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html") in *AWS CLI Command Reference*. Java **SDK for Java 2.x** ###### Note There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ec2#code-examples"). ``` /** <br>• Asynchronously describes the state of an EC2 instance. <br>• The paginator helps you iterate over multiple pages of results. * <br>• @param newInstanceId the ID of the EC2 instance to describe <br>• @return a {@link CompletableFuture} that, when completed, contains a string describing the state of the EC2 instance */ public CompletableFuture<String> describeEC2InstancesAsync(String newInstanceId) { DescribeInstancesRequest request = DescribeInstancesRequest.builder() .instanceIds(newInstanceId) .build(); DescribeInstancesPublisher paginator = getAsyncClient().describeInstancesPaginator(request); AtomicReference<String> publicIpAddressRef = new AtomicReference<>(); return paginator.subscribe(response -> { response.reservations().stream() .flatMap(reservation -> reservation.instances().stream()) .filter(instance -> instance.instanceId().equals(newInstanceId)) .findFirst() .ifPresent(instance -> publicIpAddressRef.set(instance.publicIpAddress())); }).thenApply(v -> { String publicIpAddress = publicIpAddressRef.get(); if (publicIpAddress == null) { throw new RuntimeException("Instance with ID " + newInstanceId + " not found."); } return publicIpAddress; }).exceptionally(ex -> { logger.info("Failed to describe instances: " + ex.getMessage()); throw new RuntimeException("Failed to describe instances", ex); }); } ``` <br>• For API details, see [DescribeInstances](../../../goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstances.md "../../../goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstances.md") in *AWS SDK for Java 2.x API Reference*. JavaScript **SDK for JavaScript (v3)** ###### Note There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ec2#code-examples"). ``` import { EC2Client, paginateDescribeInstances } from "@aws-sdk/client-ec2"; /** <br>• List all of your EC2 instances running with the provided architecture that <br>• were launched in the past month. <br>• @param {{ pageSize: string, architectures: string[] }} options */ export const main = async ({ pageSize, architectures }) => { pageSize = Number.parseInt(pageSize); const client = new EC2Client({}); const d = new Date(); const year = d.getFullYear(); const month = `0${d.getMonth() + 1}`.slice(-2); const launchTimePattern = `${year}-${month}-*`; const paginator = paginateDescribeInstances( { client, pageSize, }, { Filters: [ { Name: "architecture", Values: architectures }, { Name: "instance-state-name", Values: ["running"] }, { Name: "launch-time", Values: [launchTimePattern], }, ], }, ); try { /** <br>• @type {import('@aws-sdk/client-ec2').Instance[]} */ const instanceList = []; for await (const page of paginator) { const { Reservations } = page; for (const reservation of Reservations) { instanceList.push(...reservation.Instances); } } console.log( `Running instances launched this month:\n\n${instanceList.map((instance) => instance.InstanceId).join("\n")}`, ); } catch (caught) { if (caught instanceof Error && caught.name === "InvalidParameterValue") { console.warn(`${caught.message}.`); } else { throw caught; } } }; ``` <br>• For API details, see [DescribeInstances](../../../AWSJavaScriptSDK/v3/latest/client/ec2/command/DescribeInstancesCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/ec2/command/DescribeInstancesCommand.md") in *AWS SDK for JavaScript API Reference*. Kotlin **SDK for Kotlin** ###### Note There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ec2#code-examples"). ``` suspend fun describeEC2Instances() { val request = DescribeInstancesRequest { maxResults = 6 } Ec2Client.fromEnvironment { region = "us-west-2" }.use { ec2 -> val response = ec2.describeInstances(request) response.reservations?.forEach { reservation -> reservation.instances?.forEach { instance -> println("Instance Id is ${instance.instanceId}") println("Image id is ${instance.imageId}") println("Instance type is ${instance.instanceType}") println("Instance state name is ${instance.state?.name}") println("monitoring information is ${instance.monitoring?.state}") } } } } ``` <br>• For API details, see [DescribeInstances](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html") in *AWS SDK for Kotlin API reference*. PowerShell **Tools for PowerShell V4** **Example 1: This example describes the specified instance.** ``` (Get-EC2Instance -InstanceId i-12345678).Instances ``` **Output:** ``` AmiLaunchIndex        : 0 Architecture          : x86_64 BlockDeviceMappings   : {/dev/sda1} ClientToken           : TleEy1448154045270 EbsOptimized          : False Hypervisor            : xen IamInstanceProfile    : Amazon.EC2.Model.IamInstanceProfile ImageId               : ami-12345678 InstanceId            : i-12345678 InstanceLifecycle     : InstanceType          : t2.micro KernelId              : KeyName               : my-key-pair LaunchTime            : 12/4/2015 4:44:40 PM Monitoring            : Amazon.EC2.Model.Monitoring NetworkInterfaces     : {ip-10-0-2-172.us-west-2.compute.internal} Placement             : Amazon.EC2.Model.Placement Platform              : Windows PrivateDnsName        : ip-10-0-2-172.us-west-2.compute.internal PrivateIpAddress      : 10.0.2.172 ProductCodes          : {} PublicDnsName         : PublicIpAddress       : RamdiskId             : RootDeviceName        : /dev/sda1 RootDeviceType        : ebs SecurityGroups        : {default} SourceDestCheck       : True SpotInstanceRequestId : SriovNetSupport       : State                 : Amazon.EC2.Model.InstanceState StateReason           : StateTransitionReason : SubnetId              : subnet-12345678 Tags                  : {Name} VirtualizationType    : hvm VpcId                 : vpc-12345678 ``` **Example 2: This example describes all your instances in the current region, grouped by reservation. To see the instance details expand the Instances collection within each reservation object.** ``` Get-EC2Instance ``` **Output:** ``` GroupNames    : {} Groups        : {} Instances     : {} OwnerId       : 123456789012 RequesterId   : 226008221399 ReservationId : r-c5df370c GroupNames    : {} Groups        : {} Instances     : {} OwnerId       : 123456789012 RequesterId   : 854251627541 ReservationId : r-63e65bab ... ``` **Example 3: This example illustrates using a filter to query for EC2 instances in a specific subnet of a VPC.** ``` (Get-EC2Instance -Filter @{Name="vpc-id";Values="vpc-1a2bc34d"},@{Name="subnet-id";Values="subnet-1a2b3c4d"}).Instances ``` **Output:** ``` InstanceId          InstanceType Platform PrivateIpAddress PublicIpAddress SecurityGroups SubnetId        VpcId ----------          ------------ -------- ---------------- --------------- -------------- --------        ----- i-01af...82cf180e19 t2.medium    Windows  10.0.0.98                        ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0374...7e9d5b0c45 t2.xlarge    Windows  10.0.0.53                        ...            subnet-1a2b3c4d vpc-1a2b3c4d ``` **Example 4: This example illustrates using a filter with multiple values to query for EC2 instances that are both running and stopped** ``` $InstanceParams = @{ Filter = @( @{'Name' = 'instance-state-name';'Values' = @("running","stopped")} ) } (Get-EC2Instance @InstanceParams).Instances ``` **Output:** ``` InstanceId          InstanceType Platform PrivateIpAddress PublicIpAddress SecurityGroups SubnetId        VpcId ----------          ------------ -------- ---------------- --------------- -------------- --------        ----- i-05a9...f6c5f46e18 t3.medium             10.0.1.7                         ...            subnet-1a2b3c4d vpc-1a2b3c4d i-02cf...945c4fdd07 t3.medium    Windows  10.0.1.8                         ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0ac0...c037f9f3a1 t3.xlarge    Windows  10.0.1.10                        ...            subnet-1a2b3c4d vpc-1a2b3c4d i-066b...57b7b08888 t3.medium    Windows  10.0.1.11                        ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0fee...82e83ccd72 t3.medium    Windows  10.0.1.5                         ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0a68...274cc5043b t3.medium    Windows  10.0.1.6                         ...            subnet-1a2b3c4d vpc-1a2b3c4d ``` **Example 5: This example illustrates using a filter with multiple values to query for EC2 instances that are both running and stopped and using the Select-Object cmdlet for choosing specific values to output.** ``` $InstanceParams = @{ Filter = @( @{'Name' = 'instance-state-name';'Values' = @("running","stopped")} ) } $SelectParams = @{ Property = @( "InstanceID", "InstanceType", "Platform", "PrivateIpAddress", @{Name="Name";Expression={$_.Tags[$_.Tags.Key.IndexOf("Name")].Value}}, @{Name="State";Expression={$_.State.Name}} ) } $result = Get-EC2Instance @InstanceParams $result.Instances | Select-Object @SelectParams | Format-Table -AutoSize ``` **Output:** ``` InstanceId          InstanceType Platform PrivateIpAddress Name         State ----------          ------------ -------- ---------------- ----         ----- i-05a9...f6c5f46e18 t3.medium             10.0.1.7         ec2-name-01  running i-02cf...945c4fdd07 t3.medium    Windows  10.0.1.8         ec2-name-02  stopped i-0ac0...c037f9f3a1 t3.xlarge    Windows  10.0.1.10        ec2-name-03  running i-066b...57b7b08888 t3.medium    Windows  10.0.1.11        ec2-name-04  stopped i-0fee...82e83ccd72 t3.medium    Windows  10.0.1.5         ec2-name-05  running i-0a68...274cc5043b t3.medium    Windows  10.0.1.6         ec2-name-06  stopped ``` <br>• For API details, see [DescribeInstances](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md") in *AWS Tools for PowerShell Cmdlet Reference (V4)*. **Tools for PowerShell V5** **Example 1: This example describes the specified instance.** ``` (Get-EC2Instance -InstanceId i-12345678).Instances ``` **Output:** ``` AmiLaunchIndex        : 0 Architecture          : x86_64 BlockDeviceMappings   : {/dev/sda1} ClientToken           : TleEy1448154045270 EbsOptimized          : False Hypervisor            : xen IamInstanceProfile    : Amazon.EC2.Model.IamInstanceProfile ImageId               : ami-12345678 InstanceId            : i-12345678 InstanceLifecycle     : InstanceType          : t2.micro KernelId              : KeyName               : my-key-pair LaunchTime            : 12/4/2015 4:44:40 PM Monitoring            : Amazon.EC2.Model.Monitoring NetworkInterfaces     : {ip-10-0-2-172.us-west-2.compute.internal} Placement             : Amazon.EC2.Model.Placement Platform              : Windows PrivateDnsName        : ip-10-0-2-172.us-west-2.compute.internal PrivateIpAddress      : 10.0.2.172 ProductCodes          : {} PublicDnsName         : PublicIpAddress       : RamdiskId             : RootDeviceName        : /dev/sda1 RootDeviceType        : ebs SecurityGroups        : {default} SourceDestCheck       : True SpotInstanceRequestId : SriovNetSupport       : State                 : Amazon.EC2.Model.InstanceState StateReason           : StateTransitionReason : SubnetId              : subnet-12345678 Tags                  : {Name} VirtualizationType    : hvm VpcId                 : vpc-12345678 ``` **Example 2: This example describes all your instances in the current region, grouped by reservation. To see the instance details expand the Instances collection within each reservation object.** ``` Get-EC2Instance ``` **Output:** ``` GroupNames    : {} Groups        : {} Instances     : {} OwnerId       : 123456789012 RequesterId   : 226008221399 ReservationId : r-c5df370c GroupNames    : {} Groups        : {} Instances     : {} OwnerId       : 123456789012 RequesterId   : 854251627541 ReservationId : r-63e65bab ... ``` **Example 3: This example illustrates using a filter to query for EC2 instances in a specific subnet of a VPC.** ``` (Get-EC2Instance -Filter @{Name="vpc-id";Values="vpc-1a2bc34d"},@{Name="subnet-id";Values="subnet-1a2b3c4d"}).Instances ``` **Output:** ``` InstanceId          InstanceType Platform PrivateIpAddress PublicIpAddress SecurityGroups SubnetId        VpcId ----------          ------------ -------- ---------------- --------------- -------------- --------        ----- i-01af...82cf180e19 t2.medium    Windows  10.0.0.98                        ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0374...7e9d5b0c45 t2.xlarge    Windows  10.0.0.53                        ...            subnet-1a2b3c4d vpc-1a2b3c4d ``` **Example 4: This example illustrates using a filter with multiple values to query for EC2 instances that are both running and stopped** ``` $InstanceParams = @{ Filter = @( @{'Name' = 'instance-state-name';'Values' = @("running","stopped")} ) } (Get-EC2Instance @InstanceParams).Instances ``` **Output:** ``` InstanceId          InstanceType Platform PrivateIpAddress PublicIpAddress SecurityGroups SubnetId        VpcId ----------          ------------ -------- ---------------- --------------- -------------- --------        ----- i-05a9...f6c5f46e18 t3.medium             10.0.1.7                         ...            subnet-1a2b3c4d vpc-1a2b3c4d i-02cf...945c4fdd07 t3.medium    Windows  10.0.1.8                         ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0ac0...c037f9f3a1 t3.xlarge    Windows  10.0.1.10                        ...            subnet-1a2b3c4d vpc-1a2b3c4d i-066b...57b7b08888 t3.medium    Windows  10.0.1.11                        ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0fee...82e83ccd72 t3.medium    Windows  10.0.1.5                         ...            subnet-1a2b3c4d vpc-1a2b3c4d i-0a68...274cc5043b t3.medium    Windows  10.0.1.6                         ...            subnet-1a2b3c4d vpc-1a2b3c4d ``` **Example 5: This example illustrates using a filter with multiple values to query for EC2 instances that are both running and stopped and using the Select-Object cmdlet for choosing specific values to output.** ``` $InstanceParams = @{ Filter = @( @{'Name' = 'instance-state-name';'Values' = @("running","stopped")} ) } $SelectParams = @{ Property = @( "InstanceID", "InstanceType", "Platform", "PrivateIpAddress", @{Name="Name";Expression={$_.Tags[$_.Tags.Key.IndexOf("Name")].Value}}, @{Name="State";Expression={$_.State.Name}} ) } $result = Get-EC2Instance @InstanceParams $result.Instances | Select-Object @SelectParams | Format-Table -AutoSize ``` **Output:** ``` InstanceId          InstanceType Platform PrivateIpAddress Name         State ----------          ------------ -------- ---------------- ----         ----- i-05a9...f6c5f46e18 t3.medium             10.0.1.7         ec2-name-01  running i-02cf...945c4fdd07 t3.medium    Windows  10.0.1.8         ec2-name-02  stopped i-0ac0...c037f9f3a1 t3.xlarge    Windows  10.0.1.10        ec2-name-03  running i-066b...57b7b08888 t3.medium    Windows  10.0.1.11        ec2-name-04  stopped i-0fee...82e83ccd72 t3.medium    Windows  10.0.1.5         ec2-name-05  running i-0a68...274cc5043b t3.medium    Windows  10.0.1.6         ec2-name-06  stopped ``` **Example 6: This example validates permissions for getting EC2 instances using the DryRun parameter without actually fetching them. Note: This throws an exception if succeeded which is the expected behavior.** ``` Get-EC2Tag -DryRun $true ``` **Output:** ``` Get-EC2Instance: Request would have succeeded, but DryRun flag is set. ``` <br>• For API details, see [DescribeInstances](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md") in *AWS Tools for PowerShell Cmdlet Reference (V5)*. Python **SDK for Python (Boto3)** ###### Note There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ec2#code-examples"). ``` class EC2InstanceWrapper: """Encapsulates Amazon Elastic Compute Cloud (Amazon EC2) instance actions using the client interface.""" def __init__( self, ec2_client: Any, instances: Optional[List[Dict[str, Any]]] = None ) -> None: """ Initializes the EC2InstanceWrapper with an EC2 client and optional instances. :param ec2_client: A Boto3 Amazon EC2 client. This client provides low-level access to AWS EC2 services. :param instances: A list of dictionaries representing Boto3 Instance objects. These are high-level objects that wrap instance actions. """ self.ec2_client = ec2_client self.instances = instances or [] @classmethod def from_client(cls) -> "EC2InstanceWrapper": """ Creates an EC2InstanceWrapper instance with a default EC2 client. :return: An instance of EC2InstanceWrapper initialized with the default EC2 client. """ ec2_client = boto3.client("ec2") return cls(ec2_client) def display(self, state_filter: Optional[str] = "running") -> None: """ Displays information about instances, filtering by the specified state. :param state_filter: The instance state to include in the output. Only instances in this state will be displayed. Default is 'running'. Example states: 'running', 'stopped'. """ if not self.instances: logger.info("No instances to display.") return instance_ids = [instance["InstanceId"] for instance in self.instances] paginator = self.ec2_client.get_paginator("describe_instances") page_iterator = paginator.paginate(InstanceIds=instance_ids) try: for page in page_iterator: for reservation in page["Reservations"]: for instance in reservation["Instances"]: instance_state = instance["State"]["Name"] # Apply the state filter (default is 'running') if state_filter and instance_state != state_filter: continue  # Skip this instance if it doesn't match the filter # Create a formatted string with instance details instance_info = ( f"• ID: {instance['InstanceId']}\n" f"• Image ID: {instance['ImageId']}\n" f"• Instance type: {instance['InstanceType']}\n" f"• Key name: {instance['KeyName']}\n" f"• VPC ID: {instance['VpcId']}\n" f"• Public IP: {instance.get('PublicIpAddress', 'N/A')}\n" f"• State: {instance_state}" ) print(instance_info) except ClientError as err: logger.error( f"Failed to display instance(s). : {' '.join(map(str, instance_ids))}" ) error_code = err.response["Error"]["Code"] if error_code == "InvalidInstanceID.NotFound": logger.error( "One or more instance IDs do not exist. " "Please verify the instance IDs and try again." ) raise ``` <br>• For API details, see [DescribeInstances](../../../goto/boto3/ec2-2016-11-15/DescribeInstances.md "../../../goto/boto3/ec2-2016-11-15/DescribeInstances.md") in *AWS SDK for Python (Boto3) API Reference*. Ruby **SDK for Ruby** ###### Note There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/ec2#code-examples"). ``` require 'aws-sdk-ec2' # @param ec2_resource [Aws::EC2::Resource] An initialized EC2 resource object. # @example #   list_instance_ids_states(Aws::EC2::Resource.new(region: 'us-west-2')) def list_instance_ids_states(ec2_resource) response = ec2_resource.instances if response.count.zero? puts 'No instances found.' else puts 'Instances -- ID, state:' response.each do |instance| puts "#{instance.id}, #{instance.state.name}" end end rescue StandardError => e puts "Error getting information about instances: #{e.message}" end # Example usage: def run_me region = '' # Print usage information and then stop. if ARGV[0] == '--help' || ARGV[0] == '-h' puts 'Usage:   ruby ec2-ruby-example-get-all-instance-info.rb REGION' # Replace us-west-2 with the AWS Region you're using for Amazon EC2. puts 'Example: ruby ec2-ruby-example-get-all-instance-info.rb us-west-2' exit 1 # If no values are specified at the command prompt, use these default values. # Replace us-west-2 with the AWS Region you're using for Amazon EC2. elsif ARGV.count.zero? region = 'us-west-2' # Otherwise, use the values as specified at the command prompt. else region = ARGV[0] end ec2_resource = Aws::EC2::Resource.new(region: region) list_instance_ids_states(ec2_resource) end run_me if $PROGRAM_NAME == __FILE__ ``` <br>• For API details, see [DescribeInstances](../../../goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstances.md "../../../goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstances.md") in *AWS SDK for Ruby API Reference*. Rust **SDK for Rust** ###### Note There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ec2#code-examples"). Retrieve details for an EC2 Instance. ``` pub async fn describe_instance(&self, instance_id: &str) -> Result<Instance, EC2Error> { let response = self .client .describe_instances() .instance_ids(instance_id) .send() .await?; let instance = response .reservations() .first() .ok_or_else(|| EC2Error::new(format!("No instance reservations for {instance_id}")))? .instances() .first() .ok_or_else(|| { EC2Error::new(format!("No instances in reservation for {instance_id}")) })?; Ok(instance.clone()) } ``` After creating an EC2 instance, retrieve and store its details. ``` /// Create an EC2 instance with the given ID on a given type, using a /// generated KeyPair and applying a list of security groups. pub async fn create( &mut self, ec2: &EC2, image_id: &str, instance_type: InstanceType, key_pair: &KeyPairInfo, security_groups: Vec<&SecurityGroup>, ) -> Result<(), EC2Error> { let instance_id = ec2 .create_instance(image_id, instance_type, key_pair, security_groups) .await?; let instance = ec2.describe_instance(&instance_id).await?; self.instance = Some(instance); Ok(()) } ``` <br>• For API details, see [DescribeInstances](https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_instances "https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_instances") in *AWS SDK for Rust API reference*. SAP ABAP **SDK for SAP ABAP** ###### Note There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ec2#code-examples"). ``` TRY. oo_result = lo_ec2->describeinstances( ).                        " oo_result is returned for testing purposes. " " Retrieving details of EC2 instances. " DATA: lv_istance_id    TYPE /aws1/ec2string, lv_status        TYPE /aws1/ec2instancestatename, lv_instance_type TYPE /aws1/ec2instancetype, lv_image_id      TYPE /aws1/ec2string. LOOP AT oo_result->get_reservations( ) INTO DATA(lo_reservation). LOOP AT lo_reservation->get_instances( ) INTO DATA(lo_instance). lv_istance_id = lo_instance->get_instanceid( ). lv_status = lo_instance->get_state( )->get_name( ). lv_instance_type = lo_instance->get_instancetype( ). lv_image_id = lo_instance->get_imageid( ). ENDLOOP. ENDLOOP. MESSAGE 'Retrieved information about EC2 instances.' TYPE 'I'. CATCH /aws1/cx_rt_service_generic INTO DATA(lo_exception). DATA(lv_error) = |"{ lo_exception->av_err_code }" - { lo_exception->av_err_msg }|. MESSAGE lv_error TYPE 'E'. ENDTRY. ``` <br>• For API details, see [DescribeInstances](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md") in *AWS SDK for SAP ABAP API reference*. For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md"). This topic also includes information about getting started and details about previous SDK versions.
````
