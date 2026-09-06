

# Secondary Networks
<a name="secondary-networks"></a>

Secondary Networks are virtual networks purpose-built for specialized networking use cases. These networks are logically isolated within partitions of the AWS cloud. You can create resources such as secondary subnets within your secondary network. Secondary networks are tightly coupled with Amazon VPCs, such that select instances are multi-homed and launched into both a VPC and a Secondary Network.

Secondary Networks are currently available for select instance types and through capacity reservations with long term commitments. Please reach out to your account team for more information if you think secondary networks may be beneficial for your workload.

**Topics**
+ [What are Secondary Networks?](#secondary-networks-overview)
+ [Key concepts](#secondary-networks-concepts)
+ [Architecture](#secondary-networks-architecture)
+ [Additional considerations](#secondary-networks-considerations)
+ [Getting started](#secondary-networks-getting-started)
+ [Managing Secondary Network resources](#secondary-networks-managing-resources)
+ [Network design best practices](#secondary-networks-best-practices)
+ [Troubleshooting](#secondary-networks-troubleshooting)
+ [Quotas and limits](#secondary-networks-quotas-limits)

## What are Secondary Networks?
<a name="secondary-networks-overview"></a>

Secondary Networks provide a logical, isolated network, used in combination with a VPC network, such that instances are multi-homed into two independent networks. The benefits of secondary networks include:
+ High-performance networking for specialized use cases and protocols such as east-west connectivity for ML workloads
+ Multi-tenant support with logical isolation
+ Instances seamlessly integrate with VPCs and AWS services

## Key concepts
<a name="secondary-networks-concepts"></a>

Secondary Network  
A regional networking construct that provides a logical Layer 3 network with an IPv4 CIDR block (ranging from /28 to /12). Secondary Networks operate independently from VPCs on physically partitioned network infrastructure.

Secondary Subnet  
An Availability Zone-specific construct within a Secondary Network, similar to VPC subnets. Secondary Subnets support CIDR blocks ranging from /28 to /12.

Secondary Interface  
Network interfaces attached to secondary network cards, providing east-west connectivity within secondary subnets. These interfaces are physically and logically separate from Elastic Network Interfaces (ENIs).

## Architecture
<a name="secondary-networks-architecture"></a>

EC2 instances that support Secondary Networks are multi-homed, meaning they can communicate within both a VPC and a Secondary Network simultaneously:
+ **VPC**: Provides north-south TCP/IP connectivity to AWS services, storage, databases, networking services, and the internet
+ **Secondary Network**: Provides east-west connectivity between supported specialized instances

## Additional considerations
<a name="secondary-networks-considerations"></a>
+ Secondary interfaces are managed through RunInstances and they cannot be independently created or deleted.
+ Secondary interfaces cannot be attached/detached after the instance is launched.
+ Secondary interfaces IP addresses cannot be changed once launched.
+ VPC features such as Security Groups, NACLs, Flow Logs are not supported in Secondary Networks.

## Getting started
<a name="secondary-networks-getting-started"></a>

### Prerequisites
<a name="secondary-networks-prerequisites"></a>

Before launching instances with Secondary Networks, ensure you have also configured your VPC in the targeted Region and a Subnet in the targeted Availability Zone of your EC2 capacity.

### Step 1: Create a Secondary Network
<a name="secondary-networks-create-network"></a>

Create a Secondary Network in the same region as your VPC. This is a regional resource that provides logical isolation for your RDMA traffic.

```
aws ec2 create-secondary-network \
  --network-type rdma \
  --ipv4-cidr-block 172.31.0.0/16 \
  --region us-east-2
```

**Parameters:**
+ `--network-type`: Network type (currently only rdma is supported)
+ `--ipv4-cidr-block`: IPv4 CIDR block between /28 and /12
+ `--region`: AWS Region (US-East-2)

**Note**  
**Best Practice**: Choose a CIDR block that does not overlap with your VPC CIDR to simplify routing at the instance level.

### Step 2: Create a Secondary Subnet
<a name="secondary-networks-create-subnet"></a>

Create a Secondary Subnet in the same Availability Zone as your VPC subnet. This is an AZ-specific resource.

```
aws ec2 create-secondary-subnet \
  --secondary-network-id sn-1234567890abcdef0 \
  --ipv4-cidr-block 172.31.24.0/24 \
  --availability-zone us-east-2a
```

**Note**  
**IP Address Reservation**: Like VPC subnets, Amazon reserves the first 4 IP addresses and the last IP address in each Secondary Subnet for internal use.

### Step 3: Launch an instance
<a name="secondary-networks-launch-instance"></a>

Launch an instance into both your VPC subnet and Secondary Subnet. The instance will be multi-homed with connectivity to both networks.

```
aws ec2 run-instances \
  --image-id ami-12345678 \
  --count 1 \
  --instance-type <instance> \
  --key-name MyKeyPair \
  --instance-market-options '{"MarketType": "capacity-block"}' \
  --capacity-reservation-specification '{"CapacityReservationTarget": \
  {"CapacityReservationId": "cr-1234567890abcdef0"}}' \
  --network-interfaces \ 
    "NetworkCardIndex=0,DeviceIndex=0,Groups=sg-12345678,\
    SubnetId=subnet-0987654321fedcba0,InterfaceType=interface" \
  --secondary-interfaces \
    "NetworkCardIndex=1,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true", \
    "NetworkCardIndex=2,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true", \
    "NetworkCardIndex=3,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true", \
    "NetworkCardIndex=4,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true", \
    "NetworkCardIndex=5,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true", \
    "NetworkCardIndex=6,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true", \
    "NetworkCardIndex=7,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true", \
    "NetworkCardIndex=8,DeviceIndex=0,SecondarySubnetId=ss-98765421yxz,\
    InterfaceType=secondary,PrivateIpAddressCount=1,DeleteOnTermination=true"
```

**Key Parameters:**
+ `--network-interfaces`: Specifies the primary Nitro ENI for VPC connectivity (Network Card Index 0)
+ `--secondary-interfaces`: Specifies 8 secondary interfaces for east-west connectivity within Secondary Subnets (Network Card Indices 1-8)
+ `InterfaceType=secondary`: Indicates a Secondary Interface

## Managing Secondary Network resources
<a name="secondary-networks-managing-resources"></a>

### Describing Secondary Networks
<a name="secondary-networks-describe-networks"></a>

View details about your Secondary Networks:

```
aws ec2 describe-secondary-networks \
  --secondary-network-id sn-1234567890abcdef0
```

### Describing Secondary Subnets
<a name="secondary-networks-describe-subnets"></a>

View details about your Secondary Subnets:

```
aws ec2 describe-secondary-subnets \
  --secondary-subnet-id ss-98765421yxz
```

### Describing Secondary Interfaces
<a name="secondary-networks-describe-interfaces"></a>

View details about Secondary Network Interfaces attached to your instances:

```
aws ec2 describe-secondary-interfaces \
  --filters "Name=attachment.instance-id,Values=i-1234567890abcdef0"
```

### Deleting resources
<a name="secondary-networks-deleting-resources"></a>

Delete a Secondary Subnet:

```
aws ec2 delete-secondary-subnet \
  --secondary-subnet-id ss-98765421yxz
```

Delete a Secondary Network:

```
aws ec2 delete-secondary-network \
  --secondary-network-id sn-1234567890abcdef0
```

**Important**  
You must terminate all instances and delete all Secondary Subnets before deleting a Secondary Network.

## Network design best practices
<a name="secondary-networks-best-practices"></a>

### CIDR planning
<a name="secondary-networks-cidr-planning"></a>

**Avoid Overlapping CIDRs**: While Secondary Networks are physically isolated from VPCs, using non-overlapping CIDR blocks simplifies routing configuration at the instance operating system level.

**Note**  
Amazon reserves 5 IP addresses per subnet.

### Traffic segregation
<a name="secondary-networks-traffic-segregation"></a>

**Segregate by Secondary Network**: Create separate Secondary Networks for different projects, teams, or security boundaries. Secondary Networks provide logical isolation between instances. Instances cannot communicate across different Secondary Networks.

**Use Multiple Subnets**: Within a Secondary Network, use multiple Secondary Subnets to segment traffic by GPU index, Availability Zone, or workload type. As an example, a common architecture pattern is to deploy a single secondary network with 4 or 8 secondary subnets, where each secondary subnet is aligned to a group of GPUs of common indices.

## Troubleshooting
<a name="secondary-networks-troubleshooting"></a>

### Instance launch failures
<a name="secondary-networks-launch-failures"></a>

**Problem**: Instance fails to launch with Secondary Network interfaces.

**Solutions**:
+ Verify that your AMI includes proper driver support
+ Ensure your Secondary Subnet has sufficient available IP addresses
+ Confirm that your capacity reservation is in "active" state
+ Check that your Secondary Subnet is in the same Availability Zone as your VPC subnet

### Connectivity issues
<a name="secondary-networks-connectivity-issues"></a>

**Problem**: Unable to establish RDMA connectivity between instances.

**Solutions**:
+ Verify that all instances are in the same Secondary Network and Secondary Subnet
+ Check that secondary interface drivers are properly loaded on the instance
+ Ensure that your application is binding to the correct network interfaces
+ Instances within the same secondary subnet are reachable through direct routes. Cross subnet communication is available via a static route vended via DHCP.

### API errors
<a name="secondary-networks-api-errors"></a>

**Problem**: API calls for Secondary Network and Secondary Subnet operations fail.

**Solutions**:
+ Verify IAM permissions for ec2:CreateSecondaryNetwork, ec2:CreateSecondarySubnet.
+ Check that CIDR blocks are within the supported range (/28 to /12)
+ Verify that you're using the correct Region and Availability Zone

## Quotas and limits
<a name="secondary-networks-quotas-limits"></a>

To request quota increases, use the AWS Service Quotas or contact AWS Support.


**Secondary Networks quotas and limits**  

| Resource | Limit | Adjustable | 
| --- | --- | --- | 
| Secondary Networks per region | 5 | Yes | 
| Secondary Subnets per Secondary Network | 200 | Yes | 
| CIDR block size | /28 to /12 | No | 