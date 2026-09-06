

# Configuring VPC connectivity
<a name="vpc-connectivity-configure"></a>

This section walks you through configuring VPC connectivity for a Amazon GameLift Streams stream group using the AWS CLI.

## Step 1: Create a stream group with VPC configuration
<a name="vpc-connectivity-step1"></a>

When creating a stream group, include the `VpcTransitConfiguration` parameter in your location configuration. Specify your VPC ID and the CIDR blocks that your streaming application needs to access.

```
aws gameliftstreams create-stream-group \
    --description "Stream group with VPC connectivity" \
    --stream-class gen5n_high \
    --default-application-identifier arn:aws:gameliftstreams:us-west-2:123456789012:application/a-ABC123def \
    --location-configurations '[{
        "LocationName": "us-west-2",
        "AlwaysOnCapacity": 1,
        "VpcTransitConfiguration": {
            "VpcId": "vpc-0123456789abcdef0",
            "Ipv4CidrBlocks": ["10.0.0.0/16"]
        }
    }]'
```

Wait for the stream group to become active:

```
aws gameliftstreams wait stream-group-active \
    --identifier sg-1AB2C3De4
```

When the stream group status is `ACTIVE`, get stream group details and note the following values from the response:

```
aws gameliftstreams get-stream-group \
              --identifier sg-1AB2C3De4
```
+ `TransitGatewayId` – The ID of the transit gateway created by Amazon GameLift Streams.
+ `TransitGatewayResourceShareArn` – The ARN of the RAM resource share.
+ `InternalVpcIpv4CidrBlock` – The CIDR block of the service VPC that you need to add to your route tables.

## Step 2: Accept the RAM resource share
<a name="vpc-connectivity-step2"></a>

Accept the resource share invitation to gain access to the transit gateway:

```
# Get the resource share invitation
aws ram get-resource-share-invitations \
    --resource-share-arns arn:aws:ram:us-west-2:123456789012:resource-share/abc12345-1234-1234-1234-abc123456789

# Accept the invitation
aws ram accept-resource-share-invitation \
    --resource-share-invitation-arn arn:aws:ram:us-west-2:123456789012:resource-share-invitation/abc12345-1234-1234-1234-abc123456789
```

## Step 3: Create a VPC attachment
<a name="vpc-connectivity-step3"></a>

Attach your VPC to the transit gateway. You need to specify at least one subnet from your VPC:

```
# Get your subnet IDs
aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=vpc-0123456789abcdef0" \
    --query "Subnets[*].SubnetId"

# Create the VPC attachment
aws ec2 create-transit-gateway-vpc-attachment \
    --transit-gateway-id tgw-0123456789abcdef0 \
    --vpc-id vpc-0123456789abcdef0 \
    --subnet-ids subnet-0123456789abcdef0 subnet-0123456789abcdef1
```

Wait for the attachment to become available:

```
aws ec2 describe-transit-gateway-vpc-attachments \
    --transit-gateway-attachment-ids tgw-attach-0123456789abcdef0 \
    --query "TransitGatewayVpcAttachments[0].State"
```

## Step 4: Configure routing
<a name="vpc-connectivity-step4"></a>

Add a route to your VPC route table to direct traffic destined for the service VPC through the transit gateway. Use the `InternalVpcIpv4CidrBlock` value from the stream group response:

```
# Get your route table ID
aws ec2 describe-route-tables \
    --filters "Name=vpc-id,Values=vpc-0123456789abcdef0" \
    --query "RouteTables[*].RouteTableId"

# Add the route
aws ec2 create-route \
    --route-table-id rtb-0123456789abcdef0 \
    --destination-cidr-block 10.1.0.0/16 \
    --transit-gateway-id tgw-0123456789abcdef0
```

**Note**  
Replace `10.1.0.0/16` with the actual `InternalVpcIpv4CidrBlock` value from your stream group.

## (Optional) Step 5: Update security groups
<a name="vpc-connectivity-step5"></a>

When connecting to EC2 instances in your VPC, update the security groups of your EC2 instances to allow inbound traffic from the service VPC CIDR block so your applications can send traffic to your EC2 instances:

```
aws ec2 authorize-security-group-ingress \
    --group-id sg-0123456789abcdef0 \
    --protocol tcp \
    --port 443 \
    --cidr 10.1.0.0/16
```

**Note**  
Replace the following values with your actual configuration:  
`sg-0123456789abcdef0` – The security group ID of your private resource.
`tcp` – The protocol your application uses (tcp or udp).
`443` – The port number your application listens on.
`10.1.0.0/16` – The `InternalVpcIpv4CidrBlock` value from your stream group.

## (Optional) Step 6: Update CIDR blocks
<a name="vpc-connectivity-step6"></a>

You can update the CIDR blocks for a stream group location's VPC connectivity configuration without recreating the stream group. This is useful when you need to expand or modify the IP address ranges that your streaming application can access in your VPC.

To update the CIDR blocks, use the `UpdateStreamGroup` API:

```
aws gameliftstreams update-stream-group \
    --identifier sg-1AB2C3De4 \
    --location-configurations '[{
        "LocationName": "us-west-2",
        "VpcTransitConfiguration": {
            "VpcId": "vpc-0123456789abcdef0",
            "Ipv4CidrBlocks": ["10.0.0.0/16", "10.2.0.0/16"]
        }
    }]'
```

After updating the CIDR blocks, Amazon GameLift Streams automatically updates the routing configuration in the service-managed VPC.

**Note**  
The VPC ID cannot be changed when updating CIDR blocks. To connect to a different VPC, you must delete and recreate the stream group location (for streaming locations other than the primary) or create a new stream group (for the primary location).