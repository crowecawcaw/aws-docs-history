

# Step 3: Create a VPC endpoint for Amazon Keyspaces
<a name="vpc-endpoints-tutorial.create-endpoint"></a>

In this step, you create a dual-stack VPC endpoint for Amazon Keyspaces using the AWS CLI. To create the VPC endpoint using the VPC console, you can follow the [ Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) instructions in the *AWS PrivateLink Guide*. When filtering for the ** Service name**, enter **Cassandra**.

**To create a VPC endpoint using the AWS CLI**

1. Before you begin, verify that you can communicate with Amazon Keyspaces using its public endpoint.

   ```
   aws keyspaces list-tables --keyspace-name '{{myKeyspace}}'
   ```

   The output shows a list of Amazon Keyspaces tables that are contained in the specified keyspace. If you don't have any tables, the list is empty.

   ```
   {
       "tables": [
           {
               "keyspaceName": "myKeyspace",
               "tableName": "myTable1",
               "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/table/myTable1"
           },
           {
               "keyspaceName": "myKeyspace",
               "tableName": "myTable2",
               "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/table/myTable2"
           }
       ]
   }
   ```

1. Verify that Amazon Keyspaces is an available service for creating VPC endpoints in the current AWS Region. (The command is shown in bold text, followed by example output.)

   ```
   aws ec2 describe-vpc-endpoint-services
    
   {
       "ServiceNames": [
           "com.amazonaws.us-east-1.cassandra", 
           "com.amazonaws.us-east-1.cassandra-fips"
           "api.aws.us-east-1.cassandra-streams"
       ]
   }
   ```

   If Amazon Keyspaces is one of the available services in the output of the command, you can proceed with creating a VPC endpoint.

1. To connect to Amazon Keyspaces using IPv6 enabled dual-stack endpoints, confirm that your VPC supports IPv6 and configure subnets with IPv6 support. To add IPv6 support to an existing VPC that currently only supports IPv4, see [ IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) in the *Amazon VPC User Guide;*.

1. Determine your VPC identifier.

   ```
   aws ec2 describe-vpcs
    
   {
       "Vpcs": [
           {
               "OwnerId": "111122223333",
               "InstanceTenancy": "default",
               "Ipv6CidrBlockAssociationSet": [
                   {
                       "AssociationId": "vpc-cidr-assoc-0000aaa0a00a00aa0",
                       "Ipv6CidrBlock": "2600:1f18:e19:7d00::/56",
                       "Ipv6CidrBlockState": {
                           "State": "associated"
                       },
                       "NetworkBorderGroup": "us-east-1",
                       "Ipv6Pool": "Amazon",
                       "Ipv6AddressAttribute": "public",
                       "IpSource": "amazon"
                   }
               ],
               "CidrBlockAssociationSet": [
                   {
                       "AssociationId": "vpc-cidr-assoc-00a0000a",
                       "CidrBlock": "111.11.0.0/16",
                       "CidrBlockState": {
                           "State": "associated"
                       }
                   }
               ],
               "IsDefault": true,
               "BlockPublicAccessStates": {
                   "InternetGatewayBlockMode": "off"
               },
               "VpcId": "vpc-a1234bcd",
               "State": "available",
               "CidrBlock": "111.11.0.0/16",
               "DhcpOptionsId": "dopt-a00aaaaa"
           }
       ]
   }
   ```

   In the example output, the VPC ID is `vpc-a1234bcd`.

1. Use a filter to gather details about the subnets of the VPC.

   ```
   aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-a1234bcd"
    
   {
       "Subnets": [
           {
               "AvailabilityZoneId": "use1-az1",
               "MapCustomerOwnedIpOnLaunch": false,
               "OwnerId": "111122223333",
               "AssignIpv6AddressOnCreation": false,
               "Ipv6CidrBlockAssociationSet": [
                   {
                       "AssociationId": "subnet-cidr-assoc-05d75732736740283",
                       "Ipv6CidrBlock": "***********************",
                       "Ipv6CidrBlockState": {
                           "State": "associated"
                       },
                       "Ipv6AddressAttribute": "public",
                       "IpSource": "amazon"
                   }
               ],
               "SubnetArn": "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-70b24b16",
               "EnableDns64": false,
               "Ipv6Native": false,
               "PrivateDnsNameOptionsOnLaunch": {
                   "HostnameType": "ip-name",
                   "EnableResourceNameDnsARecord": false,
                   "EnableResourceNameDnsAAAARecord": false
               },
               "BlockPublicAccessStates": {
                   "InternetGatewayBlockMode": "off"
               },
               "SubnetId": "subnet-70b24b16",
               "State": "available",
               "VpcId": "vpc-a1234bcd",
               "CidrBlock": "**********/20",
               "AvailableIpAddressCount": 4089,
               "AvailabilityZone": "us-east-1a",
               "DefaultForAz": true,
               "MapPublicIpOnLaunch": true
           },
           {
               "AvailabilityZoneId": "use1-az2",
               "MapCustomerOwnedIpOnLaunch": false,
               "OwnerId": "111122223333",
               "AssignIpv6AddressOnCreation": false,
               "Ipv6CidrBlockAssociationSet": [
                   {
                       "AssociationId": "subnet-cidr-assoc-0ec6fb253e05b17eb",
                       "Ipv6CidrBlock": "***********************",
                       "Ipv6CidrBlockState": {
                           "State": "associated"
                       },
                       "Ipv6AddressAttribute": "public",
                       "IpSource": "amazon"
                   }
               ],
               "SubnetArn": "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-c63ffbe7",
               "EnableDns64": false,
               "Ipv6Native": false,
               "PrivateDnsNameOptionsOnLaunch": {
                   "HostnameType": "ip-name",
                   "EnableResourceNameDnsARecord": false,
                   "EnableResourceNameDnsAAAARecord": false
               },
               "BlockPublicAccessStates": {
                   "InternetGatewayBlockMode": "off"
               },
               "SubnetId": "subnet-c63ffbe7",
               "State": "available",
               "VpcId": "vpc-a1234bcd",
               "CidrBlock": "***********/20",
               "AvailableIpAddressCount": 4087,
               "AvailabilityZone": "us-east-1b",
               "DefaultForAz": true,
               "MapPublicIpOnLaunch": true
           }
       ]
   }
   ```

   In the example output, there are two available subnet IDs: `subnet-70b24b16` and `subnet-c63ffbe7`. 

1. Create the VPC endpoint. For the `--vpc-id` parameter, specify the VPC ID from the previous step. For the `--subnet-ids` parameter, specify the subnet IDs from the previous step. Use the `--vpc-endpoint-type` parameter to define the endpoint as an interface. To create a dual-stack endpoint, use `--ip-address-type dualstack`. For more information about the command, see [`create-vpc-endpoint`](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) in the *AWS CLI Command Reference*. 

   ```
   aws ec2 create-vpc-endpoint \
    --vpc-endpoint-type Interface \
    --vpc-id vpc-a1234bcd \
    --ip-address-type dualstack \
    --service-name com.amazonaws.us-east-1.cassandra \
    --subnet-ids subnet-70b24b16 subnet-c63ffbe7
    
   {
       "VpcEndpoint": {
           "VpcEndpointId": "vpce-000000abc111d2ef3",
           "VpcEndpointType": "Interface",
           "VpcId": "vpc-a1234bcd",
           "ServiceName": "com.amazonaws.us-east-1.cassandra",
           "State": "pending",
           "RouteTableIds": [],
           "SubnetIds": [
               "subnet-70b24b16",
               "subnet-c63ffbe7"
           ],
           "Groups": [
               {
                   "GroupId": "sg-0123456789",
                   "GroupName": "default"
               }
           ],
           "IpAddressType": "dualstack",
           "DnsOptions": {
               "DnsRecordIpType": "dualstack"
           },
           "PrivateDnsEnabled": true,
           "RequesterManaged": false,
           "NetworkInterfaceIds": [
               "eni-08cd525f72ea6f1fa",
               "eni-07b1f6c895169d8fb"
           ],
           "DnsEntries": [
               {
                   "DnsName": "vpce-0000000000-1234567.cassandra.us-east-1.vpce.amazonaws.com",
                   "HostedZoneId": "Z7HUB22UULQXV"
               },
               {
                   "DnsName": "vpce-0000000000-1234567-us-east-1a.cassandra.us-east-1.vpce.amazonaws.com",
                   "HostedZoneId": "Z7HUB22UULQXV"
               },
               {
                   "DnsName": "cassandra.us-east-1.amazonaws.com",
                   "HostedZoneId": "ZONEIDPENDING"
               },
               {
                   "DnsName": "cassandra.us-east-1.api.aws",
                   "HostedZoneId": "ZONEIDPENDING"
               }
           ],
           "CreationTimestamp": "2025-09-19T15:19:19.266000+00:00",
           "OwnerId": "111122223333",
           "ServiceRegion": "us-east-1"
       }
   }
   ```