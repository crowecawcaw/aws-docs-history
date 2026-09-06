# Apply security posture to existing VPCs

If you have already provisioned your AWS network outside of AWS Transform, you can automatically recreate your security rules on it. AWS Transform generates security groups from your source firewall rules and associates them with your existing VPCs, which saves you time and improves accuracy and consistency compared to recreating the rules manually.

Choose **Apply security posture to existing VPCs** when your target VPCs already exist and you want to apply your source security posture to them.

The AWS Transform agent guides you through the following steps, handling the analysis and generation while you make the decisions:

1. Upload your source network file.
2. Tag your existing VPCs.
3. Match source subnets to existing VPCs.
4. Specify your VPC topology.
5. Review the generated security groups.
6. Configure resource tagging.
7. Deploy the security groups.

###### Note

Because this flow applies security posture to VPCs that already exist, it does not include the network diagram step that is part of mapping a source network to new VPCs.

## Step 1: Upload your source network file

Upload a source network file that contains security information. Because this flow extracts and applies your security posture, the file must include firewall rules. AWS Transform supports the following source file types for this flow:

- **Software-defined networks (SDNs):** VMware NSX, Cisco ACI.
- **Firewalls:** Palo Alto Networks, Fortinet FortiGate.
- **Hybrid networks (VMware and non-VMware workloads):** modelizeIT or the [AWS Transform discovery tool](discovery-tool.md "discovery-tool.md").
- **Other file types:** If your file type is not one of the supported formats listed above, AWS Transform attempts to convert it automatically.

###### Note

RVTools is not supported in this flow. RVTools files do not contain firewall rules, which are required for migrating security posture.

You can provide the file in one of two ways:

- **Use file from User Uploads** – Enter the filename, including its extension, from User Uploads.
- **Upload a new file directly in the chat** – Use the file browser or drag and drop to upload a new file.

## Step 2: Tag your existing VPCs

Tag your existing VPCs so that AWS Transform can discover them. Tagging a VPC is how you indicate that it should be included in the migration. Only VPCs that you tag are in scope for security group generation. Everything else in your account is left untouched.

AWS Transform provides a tagging page that lists the VPCs in your account with their name, VPC ID, CIDR block, and current tag status. Select the VPCs you want to include, confirm that you have reviewed them, and choose **Tag selected VPCs**. For each VPC you select, AWS Transform applies the following tags:

- **Key:** `CreatedFor` **Value:** `AWSTransform`
- **Key:** `ATWorkspace` **Value:** `workspace-id`

Any VPC that AWS Transform created is automatically tagged with **Key:** `CreatedBy` **Value:** `AWSTransform`, and is also in scope for the migration.

You can also apply or remove these tags manually from the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). After you tag your VPCs, let the agent know, and AWS Transform discovers the tagged VPCs for you.

###### Note

The tagging page shows only the VPCs in the account you are currently logged in to. If you are not signed in to the AWS Management Console, the tagging page prompts you to sign in first. For multi-account migrations, tag the VPCs in each target account separately by signing in to that account.

## Step 3: Match source subnets to existing VPCs

After you confirm your tagged VPCs, AWS Transform runs a coverage analysis that matches the source subnets in your network file to your existing VPCs by CIDR. Where a VPC's CIDR range covers a source subnet, AWS Transform associates the corresponding security groups automatically.

How your source subnets map to your existing VPCs depends on your migration approach:

- **Lift-and-shift (keep existing IP ranges):** To migrate your servers without changing their IP addresses, your existing VPCs must use CIDR ranges that match your on-premises subnets. Matching subnets are covered automatically.
- **Re-IP (change IP ranges):** To assign new IP addresses to your migrated servers, provide a CIDR mapping so AWS Transform can associate the source security posture with the correct target VPCs.

AWS Transform presents a coverage summary showing the total number of subnets and how many are covered or uncovered. For each subnet, the summary lists the on-premises subnet name, on-premises CIDR, matched VPC, matched VPC CIDR, and whether the subnet is covered.

For any uncovered subnet, you have two options:

- **Provide a CIDR mapping** – Through the chat interface, tell AWS Transform which on-premises CIDR maps to which target VPC CIDR (for example, `Map 10.68.101.0/24 to 172.31.101.0/24`). AWS Transform then associates the security groups with the correct VPCs.
- **Leave the subnet unmapped** – Uncovered subnets that you do not map are not migrated.

Each time you provide a mapping, AWS Transform stores it and shows the updated coverage. The coverage summary adds a **Mapped CIDR** column that shows the target CIDR each subnet was mapped to, along with the resolved matched VPC. For any subnets that remain uncovered, you can add more mappings or proceed to the next step. Subnets that are still uncovered when you proceed are not migrated.

When you provide CIDR mappings, keep the following guidance in mind:

- **Prefer wider mappings.** Where possible, supply a single broad mapping (for example, `10.68.0.0/16` to `172.31.0.0/16`) instead of many narrow /24 mappings. A wider mapping covers all subnets within that range at once, so you don't have to map each subnet individually.
- **Mappings also apply to your security group rules.** Only rule CIDRs that fall within a mapped CIDR range are carried over. Rule CIDRs outside your mapped ranges are not migrated, so broader mappings also help ensure your rules are fully covered.
- **Use the same prefix length on both sides.** A mapping must map to an equal-size range, such as /16 to /16 or /24 to /24. Mapping between different prefix lengths (for example, /24 to /20) is not supported.

## Step 4: Specify your VPC topology

AWS Transform asks whether your existing VPCs are isolated or connected. Your answer determines how AWS Transform generates security group rules:

- **Isolated** – Each VPC operates independently with no cross-VPC routing. AWS Transform generates security group rules using CIDR ranges.
- **Connected** – Your VPCs are connected through Transit Gateways, VPC peering, or similar. AWS Transform generates security group rules using security group referencing, where a rule references another security group instead of a CIDR range.

AWS Transform needs to know your topology before it generates security groups because cross-VPC security group referencing works only between VPCs that have network connectivity. Within-VPC referencing does not require connectivity.

###### Important

Make sure your topology selection reflects your actual network. If you select **Connected** but your VPCs do not have connectivity, deployment of cross-VPC referencing rules fails because the referenced security groups cannot be resolved across unconnected VPCs.

###### Note

For VPCs connected through a Transit Gateway, security group referencing also requires that `SecurityGroupReferencingSupport` is set to `enable` on the Transit Gateway and on each Transit Gateway VPC attachment. For more information, see [Transit gateway attachments to a VPC](../../../vpc/latest/tgw/tgw-vpc-attachments.md "../../../vpc/latest/tgw/tgw-vpc-attachments.md") in the _AWS Transit Gateway Guide_.

## Step 5: Review the generated security groups

AWS Transform runs the network mapping, the same as when you map a source network to new VPCs. When mapping completes, you review the generated security groups for your existing VPCs through a human-in-the-loop (HITL) review.

The review shows your existing VPCs, discovered by their tags, and only the security groups that AWS Transform generated and associated for them. For example, the review might show `Application VPC (172.30.0.0/16) — 3 security groups` and `Database VPC (172.31.0.0/16) — 1 security group`. Other details, such as subnets and route tables, are not shown, because this flow applies security posture only.

When you open a VPC, AWS Transform shows its IPv4 CIDR, account, source (listed as _Existing_), and description, along with a **Security groups** tab. Each security group lists its name, ID, and rule count, and indicates the source rule it was generated from (for example, _Generated using: Web-Tier-HTTPS_), so you can trace each generated group back to your source configuration. You can search the security groups by name, ID, or description.

###### Note

This review is read-only. Your existing VPCs are managed outside AWS Transform and are not modified by this migration. AWS Transform adds only the generated security groups.

After you review the security groups, let the agent know to proceed.

## Step 6: Configure resource tagging

You can optionally add custom job-level tags to the security groups that AWS Transform generates. Job-level tags apply to every security group created by this job, which helps you organize resources, track costs, and manage compliance.

###### Note

This flow supports job-level tags only. It creates only security groups, so VPC-level tagging doesn't apply.

AWS Transform applies these tags when it generates the security groups.

## Step 7: Deploy the security groups

After you review the generated security groups, choose how to deploy them. As with mapping a source network to new VPCs, you can choose AWS Transform-managed deployment or self-deployment:

- **AWS Transform-managed deployment:** After you approve, AWS Transform deploys the security groups to your existing VPCs on your behalf.
- **Self-deployment:** AWS Transform generates the security groups as Infrastructure as Code (IaC) that you deploy yourself. The same output formats are available: CloudFormation, AWS CDK, HashiCorp Terraform, and Landing Zone Accelerator (LZA).

This flow deploys security groups only. Unlike mapping a source network to new VPCs, AWS Transform does not run Reachability Analyzer, because no new network infrastructure is created, and there is no automatic rollback of deployed resources.
