

# SMSEC04-BP01 Use Access Control Lists to restrict content to trusted providers only
<a name="smsec04-bp01"></a>

Control access from the start so that you are the only one that can send content into your workflow from the beginning.

**Desired outcome:**
+ Only you are able to send content into your workflows and infrastructure
+ Your content is protected from attacks or degradation wherever possible

**Common anti-patterns:**
+ Organizations configure media ingest endpoints to accept connections from any IP address without restricting to known content provider ranges, allowing unauthorized sources to inject content into the workflow.
+ Teams deploy live contribution endpoints with default security group rules that permit all inbound traffic, exposing ingest infrastructure to unauthorized access and potential content injection.
+ Organizations create access control list (ACL) entries for temporary contributors but never remove them after the engagement ends, accumulating stale permissions that expand the attack surface over time.
+ Teams rely solely on application-layer authentication without network-level ACLs, leaving ingest endpoints vulnerable to reconnaissance and brute-force attacks from arbitrary IP addresses.
+ Organizations use overly broad Classless Inter-Domain Routing (CIDR) ranges in ACLs rather than specific provider IP addresses, inadvertently allowing access from unrelated networks within the same address block.

**Benefits of establishing this best practice:**
+ Only authorized content sources can deliver media to processing pipelines, blocking injection of unauthorized, malicious, or counterfeit content into live and video on demand (VOD) workflows.
+ Network-level ACLs block reconnaissance and connection attempts from unknown sources before they reach application-layer authentication, reducing exposure to brute-force and exploitation attempts.
+ Regularly audited ACLs confirm that only current, active content providers maintain access, removing residual permissions from past engagements.
+ Restricting ingest to known providers guarantees that content entering the workflow is from verified sources, maintaining chain-of-custody integrity for licensed material.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

When delivering content to an origin service like AWS Elemental MediaPackage v2, Identity and Access Management (IAM) policies can be implemented so that the service only accepts ingest content from sources you designate. IAM roles to allow users from only specific IPs or specific credentials can be assigned to resources within AWS so that content can't be delivered without appropriate permissions.

Along with IAM policies and permissions, services may offer security groups with Access Control Lists (ACLs) that only allow a set list of users or IP addresses that are allowed to connect and deliver content. Keeping these lists up to date by adding approved entries and pruning old entries maintains confidence in your ingest.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure MediaPackage v2 policies:** In MediaPackage v2, create and assign [policies and permissions](https://docs.aws.amazon.com/mediapackage/latest/userguide/policies-permissions.html) to the channel that you will send video to.

1. **Implement network ACLs:** In Amazon EC2 or Amazon VPC, implement an [Access Control List](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) to allow or disallow connections.

1. **Maintain and audit ACL entries:** Add implementation process to regularly review and prune ACL entries to remove stale or unauthorized IP addresses.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC04-BP02 Encrypt content ingest traffic using TLS](smsec04-bp02.html)

**Related documents**
+ [AWS Elemental MediaPackage Policies and Permissions](https://docs.aws.amazon.com/mediapackage/latest/userguide/policies-permissions.html)
+ [Amazon VPC Network ACL Basics](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-basics)

**Related services**
+ [AWS Elemental MediaPackage v2](https://aws.amazon.com/mediapackage/)
+ [Amazon IAM](https://aws.amazon.com/iam/)
+ [Amazon VPC](https://aws.amazon.com/vpc/)