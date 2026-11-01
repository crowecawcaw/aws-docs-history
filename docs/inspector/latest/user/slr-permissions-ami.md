

# Service-linked role permissions for Amazon Inspector machine image scans
<a name="slr-permissions-ami"></a>

Amazon Inspector machine image scanning uses the service-linked role named `AWSServiceRoleForAmazonInspector2Ami`. This SLR allows Amazon Inspector to read the data from the existing Amazon EBS snapshots that back the machine images that your account owns. Unlike agentless Amazon EC2 scanning, machine image scanning doesn't create new snapshots. This service-linked role trusts the `ami.inspector2.amazonaws.com` service to assume the role.

The permissions policy for the role, which is named `AmazonInspector2AmiServiceRolePolicy`, allows Amazon Inspector to perform tasks such as:
+ Use Amazon Elastic Compute Cloud (Amazon EC2) actions to retrieve information about the machine images that your account owns and the snapshots that back them.
+ Use Amazon EBS actions to read the contents of the snapshots that back your machine images.
+ Use select AWS KMS decryption actions to decrypt snapshots encrypted with AWS KMS customer managed keys.

Amazon Inspector doesn't use this role to scan machine images that you have excluded from scans. For more information, see [Excluding copied and backup machine images](machine-image-scan-configuration.md#machine-image-exclusions).

For the permissions in this policy, see [AmazonInspector2AmiServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonInspector2AmiServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.