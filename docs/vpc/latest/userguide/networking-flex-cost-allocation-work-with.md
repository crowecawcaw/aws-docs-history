

# Working with Networking Flexible Cost Allocation

Complete the following tasks to set up FCA.

## Controlling the use of Networking Flexible Cost Allocation with IAM
<a name="networking-flex-cost-allocation-iam"></a>

By default, users don't have permission to work with FCA. You can create an IAM role with a policy attached that grants users permission to create, describe, modify, associate, disassociate, and delete policies. For more information, see [Identity and access management for Amazon VPC](security-iam.md).

To associate a policy with a resource, you also need permission to describe that resource, such as `ec2:DescribeNatGateways` for a NAT gateway, `ec2:DescribeInstances` for an instance, `ec2:DescribeVpcPeeringConnections` for a peering connection, and `ec2:DescribeVpcs` or `ec2:DescribeSubnets` for a VPC or subnet scope.

For example policies, see [Networking Flexible Cost Allocation policy examples](networking-flex-cost-allocation-iam-examples.md).

## Creating a policy and associating resources
<a name="networking-flex-cost-allocation-create"></a>

Use the following procedure to create a policy and associate it with your resources. For the values to specify for each resource type, see the page for that resource type.

**Important**  
Creating and associating a policy changes how usage is itemized in your reports. A misconfigured policy can show usage with the wrong label or account, but it never moves charges between accounts.

------
#### [ AWS Management Console ]

**To create a policy and associate resources**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Networking flexible cost allocation policies**.

1. Choose **Create policy**.

1. For **Resource type**, select the resource type.

1. (Optional) For **Description**, enter a description for the policy.

1. For **Dimensions**, select the charges to allocate.

1. For **Reporting granularity**, select the granularity. If you select **CIDR**, add the CIDR ranges and labels.

1. **Showback** is turned on by default. To create the policy without allocating usage yet, turn off **Showback**.

1. Choose **Next**.

1. To associate the policy with specific resources, select the resources. To associate the policy with all resources of the resource type in an account, VPC, or subnet, choose the scope.

1. Choose **Next**, review the policy, and then choose **Create policy**.

------
#### [ AWS CLI ]

**To create a policy and associate resources**

1. Create a file named `policy-document.json` with the policy document. The following example allocates both NAT gateway dimensions and labels usage by source range.

   ```json
   {
     "ReportingGranularity": ["cidr"],
     "Dimensions": ["data-transfer", "data-processing"],
     "CidrRangeSpecifications": {
       "PrefixesType": "source-prefixes",
       "Prefixes": [
         { "CidrRange": "10.0.0.0/24", "CidrLabel": "team-a" },
         { "CidrRange": "10.0.1.0/24", "CidrLabel": "team-b" }
       ]
     }
   }
   ```

1. Create the policy using the `create-networking-flex-cost-allocation-policy` command.

   ```
   aws ec2 create-networking-flex-cost-allocation-policy \
       --network-resource-type natgw \
       --nat-fca-policy-document file://policy-document.json \
       --show-back-enabled \
       --description "Allocate shared NAT gateway costs by team" \
       --tag-specifications 'ResourceType=fca-policy,Tags=[{Key=Name,Value=shared-nat-by-team}]'
   ```

   The command uses the following parameters:
   + `--network-resource-type` – The resource type to allocate costs for: `natgw`, `ec2`, or `pcx`.
   + `--nat-fca-policy-document` – The path to the policy document. Use `--instance-fca-policy-document` or `--pcx-fca-policy-document` for the other resource types.
   + `--show-back-enabled` – Turns on allocation for the policy. Use `--show-back-disabled` to create the policy without allocating usage yet.
   + `--description` – An optional description for the policy.
   + `--tag-specifications` – Optional tags to apply to the policy.

   The following is example output.

   ```
   {
       "FcaPolicyId": "fcap-0123456789abcdef0",
       "FcaPolicyArn": "arn:aws:ec2:aa-example-1:111122223333:fca-policy/fcap-0123456789abcdef0",
       "CreatedAt": "2025-11-20T14:01:00.000Z",
       "ExpectedEffectiveAt": "2025-11-20T16:00:00.000Z"
   }
   ```

1. Associate the policy with your resources using the `associate-networking-flex-cost-allocation-policy` command. Make sure you own and can describe every resource before you associate it. If you don't own a resource, or don't have permission to describe it, the whole request fails with an `UnauthorizedOperation` error and associates nothing. To associate specific resources, use `--network-resource-ids`.

   ```
   aws ec2 associate-networking-flex-cost-allocation-policy \
       --fca-policy-id fcap-0123456789abcdef0 \
       --network-resource-ids nat-0123456789abcdef0 nat-0fedcba9876543210
   ```

   To associate all resources of the resource type in an account, VPC, or subnet, use `--network-resource-scope` instead. You can specify up to 20 resource, account, VPC, and subnet IDs in total in one request. The following example associates all NAT gateways in two VPCs.

   ```
   aws ec2 associate-networking-flex-cost-allocation-policy \
       --fca-policy-id fcap-0123456789abcdef0 \
       --network-resource-scope 'ResourceType=vpc,ResourceIds=[vpc-1a2b3c4d5e6f7a8b9,vpc-9b8a7f6e5d4c3b2a1]'
   ```

   Each association has its own expected effective time. If a resource is already associated with a policy, the output lists it under `FcaPolicyAssociationFailures`, and the other resources are still associated.

1. View the associations for the policy using the `describe-networking-flex-cost-allocation-policy-associations` command.

   ```
   aws ec2 describe-networking-flex-cost-allocation-policy-associations \
       --filters Name=fca-policy-id,Values=fcap-0123456789abcdef0
   ```

   To view the association for a specific resource, use the `resource-id` filter.

   ```
   aws ec2 describe-networking-flex-cost-allocation-policy-associations \
       --filters Name=resource-id,Values=nat-0123456789abcdef0
   ```

------
#### [ CloudFormation ]

The following template creates a NAT gateway policy and associates it with a NAT gateway that you specify. For the resource reference and more examples, see [Create Networking Flexible Cost Allocation resources with AWS CloudFormation](networking-flex-cost-allocation-cfn.md).

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Networking Flexible Cost Allocation policy for a NAT gateway
Parameters:
  NatGatewayId:
    Type: String
    Description: The ID of the NAT gateway to allocate costs for
Resources:
  NatFcaPolicy:
    Type: AWS::EC2::FcaPolicy
    Properties:
      NetworkResourceType: natgw
      NatFcaPolicyDocument:
        ReportingGranularity:
          - vpc
        Dimensions:
          - data-transfer
          - data-processing
      ShowBackEnabled: true
      Description: Allocate shared NAT gateway costs by VPC
  NatFcaPolicyAssociation:
    Type: AWS::EC2::FcaPolicyAssociation
    Properties:
      FcaPolicyId: !GetAtt NatFcaPolicy.FcaPolicyId
      NetworkResourceId: !Ref NatGatewayId
```

------

## Turning on the data in your Cost and Usage Reports
<a name="networking-flex-cost-allocation-turn-on"></a>

The itemized usage appears only in Cost and Usage Reports that include split cost allocation data. To see it, you need all of the following:
+ An active FCA policy that is associated with the resource.
+ The **Networking flexible cost allocation** preference turned on by the management account or a standalone account in the AWS Billing and Cost Management console.
+ A Cost and Usage Report that includes split cost allocation data.

Reports that don't include split cost allocation data aren't affected. They continue to show a single line item for the resource, even when a policy is in effect. Only the management account or a standalone account can turn on the **Networking flexible cost allocation** preference, the same as for Amazon ECS and Amazon EKS. The allocated line items appear in the report of the account that owns the shared resource and in the management account's report. The report uses a single split cost allocation data setting with no per-service choice, so turning it on includes the rows for every service that supports split cost allocation data. This applies to both legacy Cost and Usage Reports and Cost and Usage Report 2.0 with Data Exports.

FCA uses the same split cost allocation columns as Amazon ECS and Amazon EKS, and you turn it on in the same place.

Use the following procedure to turn on the data in your Cost and Usage Reports.

**To turn on Networking Flexible Cost Allocation in your Cost and Usage Reports**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Management preferences**.

1. In the **Split cost allocation data** section, select **Networking flexible cost allocation**.

1. Choose **Save preferences**.

Your Cost and Usage Report must also include split cost allocation data. For more information, see [Enabling split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html) in the *AWS Data Exports User Guide*.

For more information about the output, see [Understand Networking Flexible Cost Allocation in your Cost and Usage Reports](networking-flex-cost-allocation-cur.md).

## Updating a policy
<a name="networking-flex-cost-allocation-update"></a>

When you modify a policy, a new version of the policy is created. The policy ID stays the same, and a policy can have up to 100 versions. You don't need to associate the policy again. Associations use the latest version automatically. Each version has its own expected effective time, calculated in the same way as for a new association.

**Important**  
Associations always use the latest version of a policy, so an intermediate version can be skipped. For example, if you create version 2 and then create version 3 before version 2 takes effect, version 2 never takes effect. Until the latest version takes effect, the policy is treated as not yet effective, and the traffic is billed as usual. If you need each version to take effect, wait for it to take effect before you create the next version.

------
#### [ AWS Management Console ]

**To modify a policy**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Networking flexible cost allocation policies**.

1. Select the policy, and then choose **Actions**, **Modify policy**.

1. Make your changes, and then choose **Save changes**. To pause allocation without removing the associations, turn off **Showback**.

To view earlier versions of a policy, choose the **Policy** tab on the policy details page, and then choose a version. Each allocated line item in your Cost and Usage Reports shows the policy ID and the policy version that produced it, so you can match past usage to the version of the policy that was in effect.

------
#### [ AWS CLI ]

Update your policy document file, and then use the `modify-networking-flex-cost-allocation-policy` command.

```
aws ec2 modify-networking-flex-cost-allocation-policy \
    --fca-policy-id fcap-0123456789abcdef0 \
    --nat-fca-policy-document file://policy-document.json \
    --show-back-enabled \
    --description "Allocate shared NAT gateway costs by team, with team-c"
```

The command uses the following parameters:
+ `--fca-policy-id` – The ID of the policy to update.
+ `--nat-fca-policy-document` – The path to the updated policy document.
+ `--show-back-enabled` – Resumes allocation. Use `--show-back-disabled` to pause it.
+ `--description` – An optional description for the policy.

You can't change the resource type of a policy. To pause allocation without removing the associations, use `--show-back-disabled`. To resume it, use `--show-back-enabled`. Like any other change, changing showback creates a new version of the policy, and the change takes effect after the expected effective time of the new version.

The following is example output. The output includes the new version number and its expected effective time.

```
{
    "FcaPolicyId": "fcap-0123456789abcdef0",
    "UpdatedAt": "2025-11-21T09:30:00.000Z",
    "Version": 2,
    "VersionExpectedEffectiveAt": "2025-11-21T11:00:00.000Z"
}
```

To view the versions of a policy, use the `get-networking-flex-cost-allocation-policy-versions` command. To return all versions, omit `--versions-to-include`. The following example returns versions 2 and 3.

```
aws ec2 get-networking-flex-cost-allocation-policy-versions \
    --fca-policy-id fcap-0123456789abcdef0 \
    --versions-to-include 2 3
```

To view your policies and their current versions, use the `describe-networking-flex-cost-allocation-policies` command.

```
aws ec2 describe-networking-flex-cost-allocation-policies
```

------

## Stopping cost allocation
<a name="networking-flex-cost-allocation-stop"></a>

To stop allocating costs for a resource, disassociate the policy from the resource. Usage reverts to being billed as usual for traffic that is metered after the change takes effect. You can't delete a policy that has associations. Disassociate the policy from all resources, and then delete it.

------
#### [ AWS Management Console ]

**To disassociate a policy and delete it**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Networking flexible cost allocation policies**.

1. Select the policy.

1. On the **Associations** tab, select the associations, and then choose **Disassociate**.

1. Select the policy, and then choose **Actions**, **Delete policy**.

1. When prompted for confirmation, choose **Delete**.

------
#### [ AWS CLI ]

**To disassociate a policy and delete it**

1. Find the association IDs for the policy.

   ```
   aws ec2 describe-networking-flex-cost-allocation-policy-associations \
       --filters Name=fca-policy-id,Values=fcap-0123456789abcdef0
   ```

1. Disassociate the policy using the `disassociate-networking-flex-cost-allocation-policy` command.

   ```
   aws ec2 disassociate-networking-flex-cost-allocation-policy \
       --fca-policy-association-ids fcapassoc-0123456789abcdef0 fcapassoc-0fedcba9876543210
   ```

   The output lists the associations that were removed under `FcaPolicyDisassociations`, and any that couldn't be removed under `FcaPolicyDisassociationFailures`.

1. Delete the policy using the `delete-networking-flex-cost-allocation-policies` command. You can specify up to 50 policy IDs.

   ```
   aws ec2 delete-networking-flex-cost-allocation-policies \
       --fca-policy-ids fcap-0123456789abcdef0
   ```

   The output lists the deleted policies under `Successful`, and any policies that couldn't be deleted under `Failed`. A policy that still has associations isn't deleted, and its failure code is `InvalidResourceState`.

------

## Command line overview
<a name="networking-flex-cost-allocation-cli-overview"></a>

You can perform the tasks described on this page using the command line.

**Create a policy**
+ `create-networking-flex-cost-allocation-policy` (AWS CLI)

**Associate and disassociate resources**
+ `associate-networking-flex-cost-allocation-policy` (AWS CLI)
+ `disassociate-networking-flex-cost-allocation-policy` (AWS CLI)

**Describe policies, versions, and associations**
+ `describe-networking-flex-cost-allocation-policies` (AWS CLI)
+ `get-networking-flex-cost-allocation-policy-versions` (AWS CLI)
+ `describe-networking-flex-cost-allocation-policy-associations` (AWS CLI)

**Modify a policy**
+ `modify-networking-flex-cost-allocation-policy` (AWS CLI)

**Delete policies**
+ `delete-networking-flex-cost-allocation-policies` (AWS CLI)