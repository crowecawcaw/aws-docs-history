# Automate prefix list updates with IPAM

A [managed prefix list](../userguide/managed-prefix-lists.md "../userguide/managed-prefix-lists.md") is a set of CIDR blocks that you can reference in security group rules and route tables instead of specifying individual IP addresses. For example, instead of creating separate security group rules for `10.1.0.0/16`, `10.2.0.0/16`, and `10.3.0.0/16`, you can create one prefix list containing all three CIDRs and reference it in a single rule.

There are two types:

- **Customer-managed prefix lists**: IP ranges you define and manage
- **AWS-managed prefix lists**: IP ranges for AWS services (like S3 or CloudFront)
  This IPAM feature automates the management of **customer-managed prefix lists** by keeping your CIDR entries synchronized with your network changes.

## The problem this solves

Without automation, network teams spend significant time manually updating prefix lists when infrastructure changes and maintaining consistent prefix lists across environments and Regions.

IPAM solves this by letting you create rules that automatically populate prefix lists. You can use two approaches: reference CIDRs from your IPAM pools, or create rules based on your actual AWS resources—such as '
include all VPCs tagged with env=prod', 'include all subnets in us-east-1', or 'include all Elastic IP addresses owned by account 123456789'. When you add or remove these resources, IPAM automatically updates the
prefix list with their CIDRs.

## How it works

You create rules that tell IPAM which IP addresses to include in a prefix list. For example, "include all VPC CIDRs tagged with env=prod". When you add or remove production VPCs, IPAM automatically updates the prefix list.

## When to use it

- **Security groups**: Create a rule "include all VPCs tagged env=prod" so when you add new production VPCs, they're automatically allowed in your security group rules
- **Multi-region**: Deploy the same IPAM rules in multiple regions to keep identical prefix lists without manually copying CIDR entries
- **Dynamic infrastructure**: When you create/delete VPCs or subnets, their CIDRs are automatically added/removed from prefix lists without manual updates

## Prerequisites

Before you begin, ensure you have:

- An [IPAM](create-ipam.md "create-ipam.md") with [Advanced Tier](mod-ipam-tier.md "mod-ipam-tier.md") enabled
- A [customer-managed prefix list](../userguide/managed-prefix-lists.md#create-prefix-list "../userguide/managed-prefix-lists.md#create-prefix-list") (or create one during setup)
- [IAM permissions](iam-ipam.md "iam-ipam.md") for IPAM and EC2 prefix list operations

## Setup steps

### Step 1: Create an IPAM prefix list resolver

Define which CIDRs to include in your prefix list by creating an IPAM prefix list resolver.

AWS Management Console

###### To create an IPAM prefix list resolver

1. Open the [IPAM console](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Prefix list resolvers**.
3. Choose **Create prefix list resolver**.
4. In **Step 1: Configure resolver details**, choose the following:
   - **IPAM**: An IPAM instance
   - **Address family**: IPv4 or IPv6
   - **Name tag - optional**: A descriptive name
   - **Description - optional**: A description
   - **Tags**: Resource tags

5. Choose **Next**.
6. In **Step 2: Configure rules**, choose **Add rule**. You can add up to 99 rules.

###### Important

You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules. 7. Choose one of the rule types:

    * **Static CIDR**: A fixed list of CIDRs that do not change (like a manual list replicated across Regions)
    * **IPAM pool CIDR**: CIDRs from specific IPAM pools (like all CIDRs from your IPAM production pool)


    If you choose this option, choose the following:




    	+ **IPAM scope**: Select the IPAM scope to search for resources
    	+ **Conditions:**




    		- **Property**




    			* **IPAM pool ID**: Select an IPAM pool that contains the resources
    			* **CIDR** (like 10.24.34.0/23)
    		- **Operation**: Equals/Not equals
    		- **Value**: The value on which to match the condition
    * **Scope resource CIDR**: CIDRs from AWS resources like VPCs, subnets, EIPs within an IPAM scope


    If you choose this option, choose the following:




    	+ **IPAM scope**: Select the IPAM scope to search for resources
    	+ **Resource type**: Select a resource, like a VPC or subnet.
    	+ **Conditions**:




    		- **Property**:




    			* Resource ID: The unique ID of a resource (like vpc-1234567890abcdef0)
    			* Resource owner (like 111122223333)
    			* Resource region (like us-east-1)
    			* Resource tag (like key: name, value: dev-vpc-1)
    			* CIDR (like 10.24.34.0/23)
    		- **Operation**: Equals/Not equals
    		- **Value**: The value on which to match the condition

8. Choose **Next**.
9. Choose **Validate and create**.

Command line
The commands in this section link to the _AWS CLI Command Reference_. The
documentation provides detailed descriptions of the options that you can use when you
run the commands.

Use the following AWS CLI commands to create an IPAM prefix list resolver:

- Use the [create-ipam-prefix-list-resolver](../../../cli/latest/reference/ec2/create-ipam-prefix-list-resolver.md "../../../cli/latest/reference/ec2/create-ipam-prefix-list-resolver.md") command and save the returned resolver ID for step 2.

### Step 2: Create a resolver target to connect to a prefix list

Link your resolver to an existing prefix list by creating a resolver target. Use the resolver ID returned from Step 1.

AWS Management Console

###### To create an IPAM prefix list resolver target

1. In the IPAM console, choose **Prefix list resolvers**.
2. Choose the resolver you created in Step 1.
3. On the resolver details page, choose the **Targets** tab.
4. Choose **Create target**.
5. Configure the target:
   - **Region**: Select the Region where the existing managed prefix list exists or where you will create one.
   - **Prefix list**: Choose an existing managed prefix list or create a new one

6. Under **Desired version**, select one of the following:
   - **Always track latest
     version**: Choose this for automatic updates when you want your prefix lists to stay current with infrastructure changes without manual intervention.
   - **Track specific version**: Choose this for stability when you need predictable, controlled updates and want to manually approve changes to your prefix lists.

7. Choose **Create target**.

Command line
The commands in this section link to the _AWS CLI Command Reference_. The
documentation provides detailed descriptions of the options that you can use when you
run the commands.

Use the following AWS CLI commands to create an IPAM prefix list resolver target:

- Use the [create-ipam-prefix-list-resolver-target](../../../cli/latest/reference/ec2/create-ipam-prefix-list-resolver-target.md "../../../cli/latest/reference/ec2/create-ipam-prefix-list-resolver-target.md") command with the resolver ID from step 1 and your existing prefix list ID.

IPAM now automatically updates your prefix list based on your rules. The prefix list will be populated with CIDRs matching your criteria.

### Step 3: Monitor versions and synchronization

As a result of creating a prefix list resolver and target, the prefix list resolver
generates CIDR versions based on your rules and then the target syncs those CIDRs from the
resolver to a specific managed prefix list. Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list
changes due to infrastructure changes.

**Version example:**

**Initial State (Version 1)**

Production environment:

- vpc-prod-web (10.1.0.0/16) - tagged env=prod
- vpc-prod-db (10.2.0.0/16) - tagged env=prod

Resolver rule: Include all VPCs tagged env=prod

**Version 1 CIDRs:** 10.1.0.0/16, 10.2.0.0/16

**Infrastructure Change (Version 2)**

New VPC added:

- vpc-prod-api (10.3.0.0/16) - tagged env=prod

IPAM automatically detects the change and creates a new version.

**Version 2 CIDRs:** 10.1.0.0/16, 10.2.0.0/16, 10.3.0.0/16

This section explains how you can monitor version creation with the AWS console or AWS CLI and synchronization success with the AWS CLI.

Also, we encourage you to set CloudWatch alarms on failure metrics as you may need to reassess and adjust CIDR selection rules to stay within the limits for version and prefix list size. For a list of CloudWatch metrics related to IPAM prefix lists, see [IPAM prefix list resolver metrics](cloudwatch-ipam-ip-address-usage.md#cloudwatch-ipam-prefix-list-resolver-metrics "cloudwatch-ipam-ip-address-usage.md#cloudwatch-ipam-prefix-list-resolver-metrics").

AWS Management Console

###### To view versions created and monitor the target synchronization

1. In the IPAM console, choose **Prefix list resolvers**.
2. Choose the resolver you created in Step 1.
3. On the resolver details page, choose the **Versions** tab. Here you'll see any versions that have been created by the resolver along with any CIDRs in the version.
4. On the resolver details page, choose the **Monitoring** tab. In this view, [IPAM prefix list resolver metrics](cloudwatch-ipam-ip-address-usage.md#cloudwatch-ipam-prefix-list-resolver-metrics "cloudwatch-ipam-ip-address-usage.md#cloudwatch-ipam-prefix-list-resolver-metrics") are presented in graph form:
   - Prefix list resolver version creation success
   - Prefix list resolver version creation failure

5. From the **Monitoring** tab, you can also configure a CloudWatch alarm by choosing **Create alarm for prefix list resolver version creation**. You're taken to the CloudWatch console with the alarm partially configured for the metric. For more information about how to finish creating the alarm, see [Create a CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the _Amazon CloudWatch User Guide_.

Command line
The commands in this section link to the _AWS CLI Command Reference_. The
documentation provides detailed descriptions of the options that you can use when you
run the commands.

Use the following AWS CLI commands to monitor versions and synchronization:

1. Use the [get-ipam-prefix-list-resolver-version-entries](../../../cli/latest/reference/ec2/get-ipam-prefix-list-resolver-version-entries.md "../../../cli/latest/reference/ec2/get-ipam-prefix-list-resolver-version-entries.md") command to view the latest version created by resolver.
2. Use the [describe-ipam-prefix-list-resolver-targets](../../../cli/latest/reference/ec2/describe-ipam-prefix-list-resolver-targets.md "../../../cli/latest/reference/ec2/describe-ipam-prefix-list-resolver-targets.md") command to monitor resolver target sync status.

The monitor command shows:

- state - current sync state (create-complete, modify-complete, and more)
- lastSyncedVersion - last successfully synced version
- desiredVersion - target version to sync to
- stateMessage - error details if sync failed

### Step 4: (Optional) Enable and disable IPAM prefix list sync

If a managed prefix list has been configured as an IPAM prefix list target and you want to make changes to the prefix list without needing permission to access the IPAM prefix list resolver target, you can [modify the managed prefix list](../userguide/work-with-cust-managed-prefix-lists.md#modify-managed-prefix-list "../userguide/work-with-cust-managed-prefix-lists.md#modify-managed-prefix-list") and disable synchronization with the IPAM prefix list resolver. When disabled, the prefix list CIDRs are not automatically updated and you can make changes to them. When enabled, the prefix list CIDRs are automatically updated based on the associated resolver's CIDR selection rules.
