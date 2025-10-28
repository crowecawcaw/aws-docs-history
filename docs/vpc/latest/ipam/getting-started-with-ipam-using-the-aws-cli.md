# Getting started with IPAM using the AWS CLI

This tutorial guides you through the process of setting up and using Amazon VPC IP Address
Manager (IPAM) with the AWS CLI using a single AWS account. By the end of this tutorial,
you will have created an IPAM, created a hierarchy of IP address pools, and allocated a CIDR
to a VPC.

## Prerequisites

Before you begin this tutorial, make sure you have:

- An AWS account with permissions to create and manage IPAM resources.
- The AWS CLI installed and configured with appropriate credentials. For information about installing the AWS CLI, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
  For information about configuring the AWS CLI, see [Configuration basics](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md").
- Basic understanding of IP addressing and CIDR notation.
- Basic knowledge of Amazon VPC concepts.
- Approximately 30 minutes to complete the tutorial.

## Create an IPAM

The first step is to create an IPAM with operating regions. An IPAM helps you plan, track, and monitor IP addresses for your AWS workloads.

Create an IPAM with operating regions in us-east-1 and us-west-2:

```
aws ec2 create-ipam \
  --description "My IPAM" \
  --operating-regions RegionName=us-east-1 RegionName=us-west-2
```

This command creates an IPAM and enables it to manage IP addresses in the specified regions. The operating regions are the AWS Regions where the IPAM is allowed to manage IP address CIDRs.

Verify that your IPAM was created:

```
aws ec2 describe-ipams
```

Take note of the IPAM ID from the output, as you'll need it for subsequent steps.

Wait for the IPAM to be fully created and available (approximately 20 seconds):

```
sleep 20
```

## Get the IPAM scope ID

When you create an IPAM, AWS automatically creates a private and a public scope. For this tutorial, we'll use the private scope.

Retrieve the IPAM details and extract the private scope ID:

```
aws ec2 describe-ipams --ipam-id ipam-0abcd1234
```

Replace `ipam-0abcd1234` with your actual IPAM ID.

From the output, identify and note the private scope ID from the `PrivateDefaultScopeId` field. It will look something like `ipam-scope-0abcd1234`.

## Create a top-level IPv4 pool

Now, let's create a top-level pool in the private scope. This pool will serve as the parent for all other pools in our hierarchy.

Create a top-level IPv4 pool:

```
aws ec2 create-ipam-pool \
  --ipam-scope-id ipam-scope-0abcd1234 \
  --address-family ipv4 \
  --description "Top-level pool"
```

Replace `ipam-scope-0abcd1234` with your actual private scope ID.

Wait for the pool to be fully created and available:

```
aws ec2 describe-ipam-pools --ipam-pool-ids ipam-pool-0abcd1234 --query 'IpamPools[0].State' --output text
```

Replace `ipam-pool-0abcd1234` with your actual top-level pool ID. The state should be `create-complete` before proceeding.

After the pool is available, provision a CIDR block to it:

```
aws ec2 provision-ipam-pool-cidr \
  --ipam-pool-id ipam-pool-0abcd1234 \
  --cidr 10.0.0.0/8
```

Wait for the CIDR to be fully provisioned:

```
aws ec2 get-ipam-pool-cidrs --ipam-pool-id ipam-pool-0abcd1234 --query "IpamPoolCidrs[?Cidr=='10.0.0.0/8'].State" --output text
```

The state should be `provisioned` before proceeding.

## Create a regional IPv4 pool

Next, create a regional pool within the top-level pool. This pool will be specific to a particular AWS Region.

Create a regional IPv4 pool:

```
aws ec2 create-ipam-pool \
  --ipam-scope-id ipam-scope-0abcd1234 \
  --source-ipam-pool-id ipam-pool-0abcd1234 \
  --locale us-east-1 \
  --address-family ipv4 \
  --description "Regional pool in us-east-1"
```

Replace `ipam-scope-0abcd1234` with your actual private scope ID and `ipam-pool-0abcd1234` with your top-level pool ID.

Wait for the regional pool to be fully created and available:

```
aws ec2 describe-ipam-pools --ipam-pool-ids ipam-pool-1abcd1234 --query 'IpamPools[0].State' --output text
```

Replace `ipam-pool-1abcd1234` with your actual regional pool ID. The state should be `create-complete` before proceeding.

After the pool is available, provision a CIDR block to it:

```
aws ec2 provision-ipam-pool-cidr \
  --ipam-pool-id ipam-pool-1abcd1234 \
  --cidr 10.0.0.0/16
```

Wait for the CIDR to be fully provisioned:

```
aws ec2 get-ipam-pool-cidrs --ipam-pool-id ipam-pool-1abcd1234 --query "IpamPoolCidrs[?Cidr=='10.0.0.0/16'].State" --output text
```

The state should be `provisioned` before proceeding.

## Create a development IPv4 pool

Now, create a development pool within the regional pool. This pool will be used for development environments.

Create a development IPv4 pool:

```
aws ec2 create-ipam-pool \
  --ipam-scope-id ipam-scope-0abcd1234 \
  --source-ipam-pool-id ipam-pool-1abcd1234 \
  --locale us-east-1 \
  --address-family ipv4 \
  --description "Development pool"
```

Replace `ipam-scope-0abcd1234` with your actual private scope ID and `ipam-pool-1abcd1234` with your regional pool ID.

Note: It's important to include the `--locale` parameter to match the parent pool's locale.

Wait for the development pool to be fully created and available:

```
aws ec2 describe-ipam-pools --ipam-pool-ids ipam-pool-2abcd1234 --query 'IpamPools[0].State' --output text
```

Replace `ipam-pool-2abcd1234` with your actual development pool ID. The state should be `create-complete` before proceeding.

After the pool is available, provision a CIDR block to it:

```
aws ec2 provision-ipam-pool-cidr \
  --ipam-pool-id ipam-pool-2abcd1234 \
  --cidr 10.0.0.0/24
```

Wait for the CIDR to be fully provisioned:

```
aws ec2 get-ipam-pool-cidrs --ipam-pool-id ipam-pool-2abcd1234 --query "IpamPoolCidrs[?Cidr=='10.0.0.0/24'].State" --output text
```

The state should be `provisioned` before proceeding.

## Create a VPC using an IPAM pool CIDR

Finally, create a VPC that uses a CIDR from your IPAM pool. This demonstrates how IPAM can be used to allocate IP address space to AWS resources.

Create a VPC using an IPAM pool CIDR:

```
aws ec2 create-vpc \
  --ipv4-ipam-pool-id ipam-pool-2abcd1234 \
  --ipv4-netmask-length 26 \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=IPAM-VPC}]'
```

Replace `ipam-pool-2abcd1234` with your actual development pool ID.

The `--ipv4-netmask-length 26` parameter specifies that you want a /26 CIDR block (64 IP addresses) allocated from the pool. This netmask length is chosen to ensure it's smaller than the pool's CIDR block (/24).

Verify that your VPC was created:

```
aws ec2 describe-vpcs --filters "Name=tag:Name,Values=IPAM-VPC"
```

## Verify the IPAM pool allocation

Check that the CIDR was allocated from your IPAM pool:

```
aws ec2 get-ipam-pool-allocations \
  --ipam-pool-id ipam-pool-2abcd1234
```

Replace `ipam-pool-2abcd1234` with your actual development pool ID.

This command shows all allocations from the specified IPAM pool, including the VPC you just created.

## Troubleshooting

Here are some common issues you might encounter when working with IPAM:

- **Permission errors**: Ensure that your IAM user or role has the necessary permissions to create and manage IPAM resources. You may need the `ec2:CreateIpam`, `ec2:CreateIpamPool`, and other related permissions.
- **Resource limit exceeded**: By default, you can create only one IPAM per account. If you already have an IPAM, you'll need to delete it before creating a new one or use the existing one.
- **CIDR allocation failures**: When provisioning CIDRs to pools, ensure that the CIDR you're trying to provision doesn't overlap with existing allocations in other pools.
- **API request timeouts**: If you encounter "RequestExpired" errors, it might be due to network latency or time synchronization issues. Try the command again.
- **Incorrect state errors**: If you receive "IncorrectState" errors, it might be because you're trying to perform an operation on a resource that's not in the correct state. Wait for the resource to be fully created or provisioned before proceeding.
- **Allocation size errors**: If you receive "InvalidParameterValue" errors about allocation size, ensure that the netmask length you're requesting is appropriate for the pool size. For example, you can't allocate a /25 CIDR from a /24 pool.
- **Dependency violations**: When cleaning up resources, you might encounter "DependencyViolation" errors. This is because resources have dependencies on each other. Make sure to delete resources in the reverse order of creation and deprovision CIDRs before deleting pools.

## Clean up resources

When you're done with this tutorial, you should clean up the resources you created to avoid incurring unnecessary charges.

1. Delete the VPC:

```
aws ec2 delete-vpc --vpc-id vpc-0abcd1234
```

2. Deprovision the CIDR from the development pool:

```
aws ec2 deprovision-ipam-pool-cidr --ipam-pool-id ipam-pool-2abcd1234 --cidr 10.0.0.0/24
```

3. Delete the development pool:

```
aws ec2 delete-ipam-pool --ipam-pool-id ipam-pool-2abcd1234
```

4. Deprovision the CIDR from the regional pool:

```
aws ec2 deprovision-ipam-pool-cidr --ipam-pool-id ipam-pool-1abcd1234 --cidr 10.0.0.0/16
```

5. Delete the regional pool:

```
aws ec2 delete-ipam-pool --ipam-pool-id ipam-pool-1abcd1234
```

6. Deprovision the CIDR from the top-level pool:

```
aws ec2 deprovision-ipam-pool-cidr --ipam-pool-id ipam-pool-0abcd1234 --cidr 10.0.0.0/8
```

7. Delete the top-level pool:

```
aws ec2 delete-ipam-pool --ipam-pool-id ipam-pool-0abcd1234
```

8. Delete the IPAM:

```
aws ec2 delete-ipam --ipam-id ipam-0abcd1234
```

Replace all IDs with your actual resource IDs.

###### Note

You may need to wait between these operations to allow the resources to be fully deleted before proceeding to the next step. If you encounter dependency violations, wait a few seconds and try again.

## Next steps

Now that you've learned how to create and use IPAM with the AWS CLI, you might want to explore more advanced features:

- [Plan for IP address provisioning](planning-ipam.md "planning-ipam.md") – Learn how to plan your IP address space effectively
- [Monitor CIDR usage by resource](monitor-cidr-compliance-ipam.md "monitor-cidr-compliance-ipam.md") – Understand how to monitor IP address usage
- [Share an IPAM pool using AWS RAM](share-pool-ipam.md "share-pool-ipam.md") – Learn how to share IPAM pools across AWS accounts
- [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md") – Discover how to use IPAM across your organization
