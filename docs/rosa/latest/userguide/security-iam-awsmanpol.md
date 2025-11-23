# AWS managed policies for ROSA

An AWS managed policy is a standalone policy that is created and administered by AWS.
AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they’re available for all AWS customers to use.
We recommend that you reduce permissions further by defining [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies.
If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to.
AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.
For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

## AWS managed policy: ROSAManageSubscription

You can attach the `ROSAManageSubscription` policy to your IAM entities.
Before you enable ROSA in the AWS
ROSA console, you must first attach this policy to an IAM role.

This policy grants the AWS Marketplace permissions required for you to manage the ROSA subscription.

**Permissions details**

This policy includes the following permissions.

- `aws-marketplace:Subscribe` - Grants permission to subscribe to the AWS Marketplace product for ROSA.
- `aws-marketplace:Unsubscribe` - Allows principals to remove subscriptions to AWS Marketplace products.
- `aws-marketplace:ViewSubscriptions` - Allows principals to view subscriptions from AWS Marketplace. This is required so that the IAM principal can view the available AWS Marketplace subscriptions.

To view the full JSON policy document, see [ROSAManageSubscription](../../../aws-managed-policy/latest/reference/ROSAManageSubscription.md "../../../aws-managed-policy/latest/reference/ROSAManageSubscription.md") in the _AWS Managed Policy Reference Guide_.

## ROSA with HCP account policies

This section provides details about the account policies that are required for ROSA with hosted control planes (HCP).
These AWS managed policies add permissions used by ROSA with HCP IAM roles.
The permissions are required for Red Hat site reliability engineering (SRE) technical support, cluster installation, and control plane and compute functionality.

###### Note

AWS managed policies are intended for use by ROSA with hosted control planes (HCP).
ROSA classic clusters use customer managed IAM policies.
For more information about ROSA classic policies, see [ROSA classic account policies](security-iam-rosa-classic-account-policies.md "security-iam-rosa-classic-account-policies.md") and [ROSA classic operator policies](security-iam-rosa-classic-operator-policies.md "security-iam-rosa-classic-operator-policies.md").

### AWS managed policy: ROSAWorkerInstancePolicy

You can attach `ROSAWorkerInstancePolicy` to your IAM entities.
Before creating a cluster, you must have an IAM role with this policy attached.
A ROSA service makes calls to other AWS services on your behalf.
They do this to manage the resources that you use with each cluster.

**Permissions details**

This policy includes the following permissions that allow the ROSA worker nodes to complete the following tasks:

- `ec2` — Evaluate AWS Region and Amazon EC2 instance details as part of ROSA cluster worker node lifecycle management.
- `ecr` - Evaluate and get images from ROSA-managed ECR repositories that are necessary for cluster installation and worker node lifecycle management.

To view the full JSON policy document, see [ROSAWorkerInstancePolicy](../../../aws-managed-policy/latest/reference/ROSAWorkerInstancePolicy.md "../../../aws-managed-policy/latest/reference/ROSAWorkerInstancePolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSASRESupportPolicy

You can attach `ROSASRESupportPolicy` to your IAM entities.

Before you create a ROSA with hosted control planes cluster, you must first attach this policy to an IAM role.
This policy grants required permissions to Red Hat site reliability engineers (SREs) to directly observe, diagnose, and support AWS resources associated with ROSA clusters, including the ability to change ROSA cluster node state.

**Permissions details**

This policy includes the following permissions that allow Red Hat SREs to complete the following tasks:

- `cloudtrail` — Read AWS CloudTrail events and trails relevant to the cluster.
- `cloudwatch` — Read Amazon CloudWatch metrics relevant to the cluster.
- `ec2` — Read, describe, and review Amazon EC2 components related to the cluster’s health such as security groups, VPC endpoint connections, and volume status. Launch, stop, reboot, and terminate Amazon EC2 instances.
- `elasticloadbalancing` — Read, describe, and review ELB parameters related to the cluster’s health.
- `iam` — Evaluate IAM roles that relate to the cluster’s health.
- `route53` — Review DNS settings related to the cluster’s health.
- `sts` — `DecodeAuthorizationMessage` — Read IAM messages for debugging purposes.

To view the full JSON policy document, see [ROSASRESupportPolicy](../../../aws-managed-policy/latest/reference/ROSASRESupportPolicy.md "../../../aws-managed-policy/latest/reference/ROSASRESupportPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSAInstallerPolicy

You can attach `ROSAInstallerPolicy` to your IAM entities.

Before you create a ROSA with hosted control planes cluster, you must first attach this policy to an IAM role named `[Prefix]-ROSA-Worker-Role`.
This policy allows entities to add any role that follows the `[Prefix]-ROSA-Worker-Role` pattern to an instance profile.
This policy grants necessary permissions to the installer to manage AWS resources that support ROSA cluster installation.

**Permissions details**

This policy includes the following permissions that allow the installer to complete the following tasks:

- `ec2` — Run Amazon EC2 instances using AMIs hosted in AWS accounts owned and managed by Red Hat.
  Describe Amazon EC2 instances, volumes, and network resources associated with Amazon EC2 nodes.
  This permission is required so that the Kubernetes control plane can join instances to a cluster, and the cluster can evaluate its presence within Amazon VPC.
  Inspect Amazon EC2 Capacity Reservations to support the new Capacity Reservations feature in ROSA.
  Tag and delete tags on subnets using tag keys matching `"kubernetes.io/cluster/*"`.
  This is required to ensure that the load balancer used for cluster ingress is created only in applicable subnets and to manage Kubernetes cluster identification tags.
- `elasticloadbalancing` — Add load balancers to target nodes on a cluster.
  Remove load balancers from target nodes on a cluster.
  This permission is required so that the Kubernetes control plane can dynamically provision load balancers requested by Kubernetes services and OpenShift application services.
- `kms` — Read an AWS KMS key, create and manage grants to Amazon EC2, and return a unique symmetric data key for use outside of AWS KMS.
  This is required for the use of encrypted `etcd` data when `etcd` encryption is enabled at cluster creation.
- `iam` — Validate IAM roles and policies.
  Dynamically provision and manage Amazon EC2 instance profiles relevant to the cluster.
  Add tags to an IAM instance profile by using the `iam:TagInstanceProfile` permission.
  Provide installer error messages when cluster installation fails due to a missing customer-specified cluster OIDC provider.
- `route53` — Manage Route 53 resources needed to create clusters.
- `servicequotas` — Evaluate service quotas required to create a cluster.
- `sts` — Create temporary AWS STS credentials for ROSA components.
  Assume the credentials for cluster creation.
- `secretsmanager` — Read a secret value to securely allow customer-managed OIDC configuration as part of cluster provisioning.

To view the full JSON policy document, see [ROSAInstallerPolicy](../../../aws-managed-policy/latest/reference/ROSAInstallerPolicy.md "../../../aws-managed-policy/latest/reference/ROSAInstallerPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSASharedVPCRoute53Policy

You can attach `ROSASharedVPCRoute53Policy` to your IAM entities.
You must attach this policy to an IAM role to allow a ROSA cluster to make calls to other AWS services in shared VPC environments.

This policy allows the ROSA installer to configure Route 53 records.
This policy is intended to be used on a shared VPC and provides a subset of Route 53 permissions tailored for shared VPC use cases.

**Permissions details**

This policy includes the following permissions that allow the ROSA installer to complete the following tasks:

- `route53` — Read DNS zone information and existing DNS records to understand the current DNS configuration.
  Create, modify, and delete DNS records, but only for specific ROSA-related domain patterns including `.hypershift.local`, `.openshiftapps.com`, `.devshift.org`, `.openshiftusgov.com`, and `.devshiftusgov.com`.
  Add, modify, or remove tags on Route 53 resources for resource management and organization.
- `tag` — Discover and list AWS resources based on their tags, which is useful for identifying resources managed by ROSA.

To view more details about the policy, including the latest version of the JSON policy document, see [ROSASharedVPCRoute53Policy](../../../aws-managed-policy/latest/reference/ROSASharedVPCRoute53Policy.md "../../../aws-managed-policy/latest/reference/ROSASharedVPCRoute53Policy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSASharedVPCEndpointPolicy

You can attach `ROSASharedVPCEndpointPolicy` to your IAM entities.
You must attach this policy to an IAM role to allow a ROSA cluster to make calls to other AWS services in shared VPC environments.

This policy allows the ROSA installer to configure VPC endpoints and security groups in shared VPC environments.

**Permissions details**

This policy includes the following permissions that allow the ROSA installer to complete the following tasks:

- `ec2` — Read-only permissions to describe VPC-related resources including VPC endpoints, VPCs, and security groups to understand the network environment.
  Create, delete, and modify security groups with tag-based restrictions, enabling ROSA to create and manage security groups for cluster networking while restricting operations to only ROSA-tagged resources.
  Create, modify, and delete VPC endpoints with tag-based restrictions, allowing ROSA to create and manage VPC endpoints for private connectivity to AWS services in shared VPC environments.
  Apply tags to newly created VPC endpoints and security groups during creation for proper resource identification and management.

To view more details about the policy, including the latest version of the JSON policy document, see [ROSASharedVPCEndpointPolicy](../../../aws-managed-policy/latest/reference/ROSASharedVPCEndpointPolicy.md "../../../aws-managed-policy/latest/reference/ROSASharedVPCEndpointPolicy.md") in the _AWS Managed Policy Reference Guide_.

## ROSA with HCP operator policies

This section provides details about the operator policies that are required for ROSA with hosted control planes (HCP).
You can attach these AWS managed policies to the operator roles needed to use ROSA with HCP.
The permissions are required to allow OpenShift operators to manage ROSA with HCP cluster nodes.

###### Note

AWS managed policies are intended for use by ROSA with hosted control planes (HCP).
ROSA classic clusters use customer managed IAM policies.
For more information about ROSA classic policies, see [ROSA classic account policies](security-iam-rosa-classic-account-policies.md "security-iam-rosa-classic-account-policies.md") and [ROSA classic operator policies](security-iam-rosa-classic-operator-policies.md "security-iam-rosa-classic-operator-policies.md").

### AWS managed policy: ROSAAmazonEBSCSIDriverOperatorPolicy

You can attach `ROSAAmazonEBSCSIDriverOperatorPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants necessary permissions to the Amazon EBS CSI Driver Operator to install and maintain the Amazon EBS CSI driver on a ROSA cluster.
For more information about the operator, see [aws-ebs-csi-driver operator](https://github.com/openshift/aws-ebs-csi-driver-operator#aws-ebs-csi-driver-operator "https://github.com/openshift/aws-ebs-csi-driver-operator#aws-ebs-csi-driver-operator") in the OpenShift GitHub documentation.

**Permissions details**

This policy includes the following permissions that allow the Amazon EBS Driver Operator to complete the following tasks:

- `ec2` — Create, modify, attach, detach, and delete Amazon EBS volumes that are attached to Amazon EC2 instances.
  Create and delete Amazon EBS volume snapshots and list Amazon EC2 instances, volumes, and snapshots.

To view the full JSON policy document, see [ROSAAmazonEBSCSIDriverOperatorPolicy](../../../aws-managed-policy/latest/reference/ROSAAmazonEBSCSIDriverOperatorPolicy.md "../../../aws-managed-policy/latest/reference/ROSAAmazonEBSCSIDriverOperatorPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSAIngressOperatorPolicy

You can attach `ROSAIngressOperatorPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants required permissions to the Ingress Operator to provision and manage load balancers and DNS configurations for ROSA clusters.
The policy allows read access to tag values.
The operator then filters the tag values for Route 53 resources to discover hosted zones.
For more information about the operator, see [OpenShift Ingress Operator](https://github.com/openshift/cluster-ingress-operator#openshift-ingress-operator "https://github.com/openshift/cluster-ingress-operator#openshift-ingress-operator") in the OpenShift GitHub documentation.

**Permissions details**

This policy includes the following permissions that allow the Ingress Operator to complete the following tasks:

- `elasticloadbalancing` — Describe the state of provisioned load balancers.
- `route53` — List Route 53 hosted zones and edit records that manage the DNS controlled by the ROSA cluster.
- `tag` — Manage tagged resources by using the `tag:GetResources` permission.

To view the full JSON policy document, see [ROSAIngressOperatorPolicy](../../../aws-managed-policy/latest/reference/ROSAIngressOperatorPolicy.md "../../../aws-managed-policy/latest/reference/ROSAIngressOperatorPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSAImageRegistryOperatorPolicy

You can attach `ROSAImageRegistryOperatorPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants required permissions to the Image Registry Operator to provision and manage resources for the ROSA in-cluster image registry and dependent services, including S3.
This is required so that the operator can install and maintain the internal registry of a ROSA cluster.
For more information about the operator, see [Image Registry Operator](https://github.com/openshift/cluster-image-registry-operator#image-registry-operator "https://github.com/openshift/cluster-image-registry-operator#image-registry-operator") in the OpenShift GitHub documentation.

**Permissions details**

This policy includes the following permissions that allow the Image Registry Operator to complete the following actions:

- `s3` — Manage and evaluate Amazon S3 buckets as persistent storage for container image content and cluster metadata.

To view the full JSON policy document, see [ROSAImageRegistryOperatorPolicy](../../../aws-managed-policy/latest/reference/ROSAImageRegistryOperatorPolicy.md "../../../aws-managed-policy/latest/reference/ROSAImageRegistryOperatorPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSACloudNetworkConfigOperatorPolicy

You can attach `ROSACloudNetworkConfigOperatorPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants required permissions to the Cloud Network Config Controller Operator to provision and manage networking resources for the ROSA cluster networking overlay.
The operator uses these permissions to manage private IP addresses for Amazon EC2 instances as part of the ROSA cluster.
For more information about the operator, see [Cloud-network-config-controller](https://github.com/openshift/cloud-network-config-controller#cloud-network-config-controller-cncc "https://github.com/openshift/cloud-network-config-controller#cloud-network-config-controller-cncc") in the OpenShift GitHub documentation.

**Permissions details**

This policy includes the following permissions that allow the Cloud Network Config Controller Operator to complete the following tasks:

- `ec2` — Read, assign, and describe configurations for connecting Amazon EC2 instances, Amazon VPC subnets, and elastic network interfaces in a ROSA cluster.

To view the full JSON policy document, see [ROSACloudNetworkConfigOperatorPolicy](../../../aws-managed-policy/latest/reference/ROSACloudNetworkConfigOperatorPolicy.md "../../../aws-managed-policy/latest/reference/ROSACloudNetworkConfigOperatorPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSAKubeControllerPolicy

You can attach `ROSAKubeControllerPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants required permissions to the kube controller to manage Amazon EC2, ELB, and AWS KMS resources for a ROSA with hosted control planes cluster.
For more information about this controller, see [Controller architecture](https://hypershift-docs.netlify.app/reference/controller-architecture/ "https://hypershift-docs.netlify.app/reference/controller-architecture/") in the OpenShift documentation.

**Permissions details**

This policy includes the following permissions that allow the kube controller to complete the following tasks:

- `ec2` — Create, delete, and add tags to Amazon EC2 instance security groups.
  Add inbound rules to security groups.
  Describe Availability Zones, Amazon EC2 instances, route tables, security groups, VPCs, and subnets.
- `elasticloadbalancing` — Create and manage load balancers and their policies.
  Create and manage load balancer listeners.
  Register targets with target groups and manage target groups.
  Register and de-register Amazon EC2 instances with a load balancer, and add tags to load balancers.
- `kms` — Retrieve detailed information about an AWS KMS key.
  This is required for the use of encrypted `etcd` data when `etcd` encryption is enabled at cluster creation.

To view the full JSON policy document, see [ROSAKubeControllerPolicy](../../../aws-managed-policy/latest/reference/ROSAKubeControllerPolicy.md "../../../aws-managed-policy/latest/reference/ROSAKubeControllerPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSANodePoolManagementPolicy

You can attach `ROSANodePoolManagementPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants required permissions to the NodePool controller to describe, run, and terminate Amazon EC2 instances managed as worker nodes.
This policy also grants permissions to allow for disk encryption of the worker node root volume using AWS KMS keys, to tag the elastic network interface that is attached to the worker node, and to access Amazon EC2 Capacity Reservations.
For more information about this controller, see [Controller architecture](https://hypershift-docs.netlify.app/reference/controller-architecture/ "https://hypershift-docs.netlify.app/reference/controller-architecture/") in the OpenShift documentation.

**Permissions details**

This policy includes the following permissions that allow the NodePool controller to complete the following tasks:

- `ec2` — Run Amazon EC2 instances using AMIs hosted in AWS accounts owned and managed by Red Hat.
  Manage EC2 lifecycles in the ROSA cluster.
  Dynamically create and integrate worker nodes with ELB, Amazon VPC, Route 53, Amazon EBS, and Amazon EC2.
  Access and describe capacity reservations to support the Capacity Reservation feature in ROSA.
- `iam` — Use ELB via the service-linked role named `AWSServiceRoleForElasticLoadBalancing`.
  Assign roles to Amazon EC2 instance profiles.
- `kms` — Read an AWS KMS key, create and manage grants to Amazon EC2, and return a unique symmetric data key for use outside of AWS KMS.
  This is required to allow for disk encryption of the worker node root volume.

To view the full JSON policy document, see [ROSANodePoolManagementPolicy](../../../aws-managed-policy/latest/reference/ROSANodePoolManagementPolicy.md "../../../aws-managed-policy/latest/reference/ROSANodePoolManagementPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSAKMSProviderPolicy

You can attach `ROSAKMSProviderPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants required permissions to the built-in AWS Encryption Provider to manage AWS KMS keys that support `etcd` data encryption.
This policy allows Amazon EC2 to use KMS keys that the AWS Encryption Provider provides to encrypt and decrypt `etcd` data.
For more information about this provider, see [AWS Encryption Provider](https://github.com/kubernetes-sigs/aws-encryption-provider#aws-encryption-provider "https://github.com/kubernetes-sigs/aws-encryption-provider#aws-encryption-provider") in the Kubernetes GitHub documentation.

**Permissions details**

This policy includes the following permissions that allow the AWS Encryption Provider to complete the following tasks:

- `kms` — Encrypt, decrypt, and retrieve an AWS KMS key.
  This is required for the use of encrypted `etcd` data when `etcd` encryption is enabled at cluster creation.

To view the full JSON policy document, see [ROSAKMSProviderPolicy](../../../aws-managed-policy/latest/reference/ROSAKMSProviderPolicy.md "../../../aws-managed-policy/latest/reference/ROSAKMSProviderPolicy.md") in the _AWS Managed Policy Reference Guide_.

### AWS managed policy: ROSAControlPlaneOperatorPolicy

You can attach `ROSAControlPlaneOperatorPolicy` to your IAM entities.
You must attach this policy to an operator IAM role to allow a ROSA with hosted control planes cluster to make calls to other AWS services.
A unique set of operator roles is required for each cluster.

This policy grants required permissions to the Control Plane Operator to manage Amazon EC2 and Route 53 resources for ROSA with hosted control planes clusters.
For more information about this operator, see [Controller architecture](https://hypershift-docs.netlify.app/reference/controller-architecture/ "https://hypershift-docs.netlify.app/reference/controller-architecture/") in the OpenShift documentation.

**Permissions details**

This policy includes the following permissions that allow the Control Plane Operator to complete the following tasks:

- `ec2` — Create and manage Amazon VPC endpoints.
- `route53` — List and change Route 53 record sets and list hosted zones.

To view the full JSON policy document, see [ROSAControlPlaneOperatorPolicy](../../../aws-managed-policy/latest/reference/ROSAControlPlaneOperatorPolicy.md "../../../aws-managed-policy/latest/reference/ROSAControlPlaneOperatorPolicy.md") in the _AWS Managed Policy Reference Guide_.

## ROSA updates to AWS managed policies

View details about updates to AWS managed policies for ROSA since this service began tracking these changes.
For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history](doc-history.md "doc-history.md") page.

| Change                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Date              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| ROSANodePoolManagementPolicy — Policy updated             | ROSA updated the policy to add resource access for Amazon EC2 Capacity Reservations.<br>This change allows the NodePool controller to access and describe Capacity Reservations for improved resource management.<br>To learn more, see [AWS managed policy: ROSANodePoolManagementPolicy](#security-iam-awsmanpol-rosanodepoolmanagementpolicy "#security-iam-awsmanpol-rosanodepoolmanagementpolicy").                                                                                     | September 3, 2025 |
| ROSASharedVPCEndpointPolicy — New policy added            | ROSA added a new policy to allow the ROSA installer to configure VPC endpoints and security groups in shared VPC environments.<br>This policy provides a subset of EC2 permissions tailored for shared VPC use cases.<br>To learn more, see [AWS managed policy: ROSASharedVPCEndpointPolicy](#security-iam-awsmanpol-rosasharedvpcendpointpolicy "#security-iam-awsmanpol-rosasharedvpcendpointpolicy").                                                                                    | August 7, 2025    |
| ROSASharedVPCRoute53Policy — New policy added             | ROSA added a new policy to allow the ROSA installer to configure Route 53 records in shared VPC environments.<br>This policy provides a subset of Route 53 permissions tailored for shared VPC use cases.<br>To learn more, see [AWS managed policy: ROSASharedVPCRoute53Policy](#security-iam-awsmanpol-rosasharedvpcroute53policy "#security-iam-awsmanpol-rosasharedvpcroute53policy").                                                                                                   | August 7, 2025    |
| ROSAInstallerPolicy — Policy updated                      | ROSA updated the policy to allow the ROSA installer to inspect Amazon EC2 Capacity Reservations to support the new Capacity Reservations feature in ROSA.<br>This update also allows the installer to delete tags on subnets using tag keys matching `"kubernetes.io/cluster/*"` for improved Kubernetes cluster tag management.<br>To learn more, see [AWS managed policy: ROSAInstallerPolicy](#security-iam-awsmanpol-rosainstallerpolicy "#security-iam-awsmanpol-rosainstallerpolicy"). | August 7, 2025    |
| ROSAImageRegistryOperatorPolicy — Policy updated          | ROSA updated the policy so that the permissions are scoped down to the S3 bucket resource level. This change satisfies ROSA storage requirements for both AWS Commercial and GovCloud Regions.<br>To learn more, see [AWS managed policy: ROSAImageRegistryOperatorPolicy](#security-iam-awsmanpol-rosaimageregistryoperatorpolicy "#security-iam-awsmanpol-rosaimageregistryoperatorpolicy").                                                                                               | May 19, 2025      |
| ROSANodePoolManagementPolicy — Policy updated             | ROSA updated the policy to allow tagging of the elastic network interface that is attached to the worker node.<br>To learn more, see [AWS managed policy: ROSANodePoolManagementPolicy](#security-iam-awsmanpol-rosanodepoolmanagementpolicy "#security-iam-awsmanpol-rosanodepoolmanagementpolicy").                                                                                                                                                                                        | May 5, 2025       |
| ROSAImageRegistryOperatorPolicy — Policy updated          | ROSA updated the policy to allow the Red Hat OpenShift Image Registry Operator to provision and manage Amazon S3 buckets and objects in AWS GovCloud Regions for use by the ROSA in-cluster image registry.<br>This change satisfies ROSA storage requirements for AWS GovCloud Regions.<br>To learn more, see [AWS managed policy: ROSAImageRegistryOperatorPolicy](#security-iam-awsmanpol-rosaimageregistryoperatorpolicy "#security-iam-awsmanpol-rosaimageregistryoperatorpolicy").     | April 16, 2025    |
| ROSAWorkerInstancePolicy — Policy updated                 | ROSA updated the policy to allow worker nodes to evaluate and get images from ROSA-managed ECR repositories that are necessary for cluster installation and worker node lifecycle management.<br>To learn more, see [AWS managed policy: ROSAWorkerInstancePolicy](#security-iam-awsmanpol-rosaworkerinstancepolicy "#security-iam-awsmanpol-rosaworkerinstancepolicy").                                                                                                                     | March 3, 2025     |
| ROSANodePoolManagementPolicy — Policy updated             | ROSA updated the policy to allow elastic network interfaces to be tagged similarly to EC2 instances only during ec2:RunInstances calls when the request includes the tag `red-hat-managed: true`.<br>These permissions are necessary to support ROSA with HCP 4.17 clusters.<br>To learn more, see [AWS managed policy: ROSANodePoolManagementPolicy](#security-iam-awsmanpol-rosanodepoolmanagementpolicy "#security-iam-awsmanpol-rosanodepoolmanagementpolicy").                          | February 24, 2025 |
| ROSAAmazonEBSCSIDriverOperatorPolicy — Policy updated     | ROSA updated the policy to support the new Amazon EBS snapshot authorization API.<br>To learn more, see [AWS managed policy: ROSAAmazonEBSCSIDriverOperatorPolicy](#security-iam-awsmanpol-rosaamazonebscsidriveroperatorpolicy "#security-iam-awsmanpol-rosaamazonebscsidriveroperatorpolicy").                                                                                                                                                                                             | January 17, 2025  |
| ROSANodePoolManagementPolicy — Policy updated             | ROSA updated the policy to allow the ROSA node pool<br>manager to describe DHCP option sets in order to set the proper private DNS names. To learn<br>more, see [AWS managed policy: ROSANodePoolManagementPolicy](#security-iam-awsmanpol-rosanodepoolmanagementpolicy "#security-iam-awsmanpol-rosanodepoolmanagementpolicy").                                                                                                                                                             | May 2, 2024       |
| ROSAInstallerPolicy — Policy updated                      | ROSA updated the policy to allow the ROSA installer to<br>add tags to subnets using tag keys matching `"kubernetes.io/cluster/*"`. To learn more, see<br>[AWS managed policy: ROSAInstallerPolicy](#security-iam-awsmanpol-rosainstallerpolicy "#security-iam-awsmanpol-rosainstallerpolicy").                                                                                                                                                                                               | April 24, 2024    |
| ROSASRESupportPolicy — Policy updated                     | ROSA updated the policy to allow the SRE role to retrieve information on instance profiles that have been tagged by ROSA as `red-hat-managed`.<br>To learn more, see [AWS managed policy: ROSASRESupportPolicy](#security-iam-awsmanpol-rosasresupportpolicy "#security-iam-awsmanpol-rosasresupportpolicy").                                                                                                                                                                                | April 10, 2024    |
| ROSAInstallerPolicy — Policy updated                      | ROSA updated the policy to allow the ROSA installer to validate that AWS managed policies for ROSA are attached to IAM roles used by ROSA.<br>This update also allows the installer to identify whether customer managed policies have been attached to ROSA roles.<br>To learn more, see [AWS managed policy: ROSAInstallerPolicy](#security-iam-awsmanpol-rosainstallerpolicy "#security-iam-awsmanpol-rosainstallerpolicy").                                                              | April 10, 2024    |
| ROSAInstallerPolicy — Policy updated                      | ROSA updated the policy to allow the service to provide installer alert messages when cluster installation fails due to a missing customer-specified cluster OIDC provider.<br>This update also allows the service to retrieve existing DNS name servers so that cluster provisioning operations are idempotent.<br>To learn more, see [AWS managed policy: ROSAInstallerPolicy](#security-iam-awsmanpol-rosainstallerpolicy "#security-iam-awsmanpol-rosainstallerpolicy").                 | January 26, 2024  |
| ROSASRESupportPolicy — Policy updated                     | ROSA updated the policy to allow the service to perform read operations on security groups using the DescribeSecurityGroups API.<br>To learn more, see [AWS managed policy: ROSASRESupportPolicy](#security-iam-awsmanpol-rosasresupportpolicy "#security-iam-awsmanpol-rosasresupportpolicy").                                                                                                                                                                                              | January 22, 2024  |
| ROSAImageRegistryOperatorPolicy — Policy updated          | ROSA updated the policy to allow the Image Registry Operator to take actions on Amazon S3 buckets in Regions with 14-character names.<br>To learn more, see [AWS managed policy: ROSAImageRegistryOperatorPolicy](#security-iam-awsmanpol-rosaimageregistryoperatorpolicy "#security-iam-awsmanpol-rosaimageregistryoperatorpolicy").                                                                                                                                                        | December 12, 2023 |
| ROSAKubeControllerPolicy — Policy updated                 | ROSA updated the policy to allow the kube-controller-manager to describe Availability Zones, Amazon EC2 instances, route tables, security groups, VPCs, and subnets.<br>To learn more, see [AWS managed policy: ROSAKubeControllerPolicy](#security-iam-awsmanpol-rosakubecontrollerpolicy "#security-iam-awsmanpol-rosakubecontrollerpolicy").                                                                                                                                              | October 16, 2023  |
| ROSAManageSubscription — Policy updated                   | ROSA updated the policy to add the ROSA with hosted control planes ProductId.<br>To learn more, see [AWS managed policy: ROSAManageSubscription](#security-iam-awsmanpol-rosamanagesubscription "#security-iam-awsmanpol-rosamanagesubscription").                                                                                                                                                                                                                                           | August 1, 2023    |
| ROSAKubeControllerPolicy — Policy updated                 | ROSA updated the policy to allow the kube-controller-manager to create Network Load Balancers as Kubernetes service load balancers.<br>Network Load Balancers provide greater ability to handle volatile workloads and support static IP addresses for the load balancer.<br>To learn more, see [AWS managed policy: ROSAKubeControllerPolicy](#security-iam-awsmanpol-rosakubecontrollerpolicy "#security-iam-awsmanpol-rosakubecontrollerpolicy").                                         | July 13, 2023     |
| ROSANodePoolManagementPolicy — New policy added           | ROSA added a new policy to allow the NodePool controller to describe, run, and terminate Amazon EC2 instances managed as worker nodes.<br>This policy also enables disk encryption of the worker node root volume using AWS KMS keys.<br>To learn more, see [AWS managed policy: ROSANodePoolManagementPolicy](#security-iam-awsmanpol-rosanodepoolmanagementpolicy "#security-iam-awsmanpol-rosanodepoolmanagementpolicy").                                                                 | June 8, 2023      |
| ROSAInstallerPolicy — New policy added                    | ROSA added a new policy to allow the installer to manage AWS resources that support cluster installation.<br>To learn more, see [AWS managed policy: ROSAInstallerPolicy](#security-iam-awsmanpol-rosainstallerpolicy "#security-iam-awsmanpol-rosainstallerpolicy").                                                                                                                                                                                                                        | June 6, 2023      |
| ROSASRESupportPolicy — New policy added                   | ROSA added a new policy to allow Red Hat SREs to directly observe, diagnose and support AWS resources associated with ROSA clusters, including the ability to change ROSA cluster node state.<br>To learn more, see [AWS managed policy: ROSASRESupportPolicy](#security-iam-awsmanpol-rosasresupportpolicy "#security-iam-awsmanpol-rosasresupportpolicy").                                                                                                                                 | June 1, 2023      |
| ROSAKMSProviderPolicy — New policy added                  | ROSA added a new policy to allow the built-in AWS Encryption Provider to manage AWS KMS keys to support etcd data encryption.<br>To learn more, see [AWS managed policy: ROSAKMSProviderPolicy](#security-iam-awsmanpol-rosakmsproviderpolicy "#security-iam-awsmanpol-rosakmsproviderpolicy").                                                                                                                                                                                              | April 27, 2023    |
| ROSAKubeControllerPolicy — New policy added               | ROSA added a new policy to allow the kube controller to manage Amazon EC2, ELB, and AWS KMS resources for ROSA with hosted control planes clusters.<br>To learn more, see [AWS managed policy: ROSAKubeControllerPolicy](#security-iam-awsmanpol-rosakubecontrollerpolicy "#security-iam-awsmanpol-rosakubecontrollerpolicy").                                                                                                                                                               | April 27, 2023    |
| ROSAImageRegistryOperatorPolicy — New policy added        | ROSA added a new policy to allow the Image Registry Operator to provision and manage resources for the ROSA in-cluster image registry and dependent services, including S3.<br>To learn more, see [AWS managed policy: ROSAImageRegistryOperatorPolicy](#security-iam-awsmanpol-rosaimageregistryoperatorpolicy "#security-iam-awsmanpol-rosaimageregistryoperatorpolicy").                                                                                                                  | April 27, 2023    |
| ROSAControlPlaneOperatorPolicy — New policy added         | ROSA added a new policy to allow the Control Plane Operator to manage Amazon EC2 and Route 53 resources for ROSA with hosted control planes clusters.<br>To learn more, see [AWS managed policy: ROSAControlPlaneOperatorPolicy](#security-iam-awsmanpol-rosacontrolplaneoperatorpolicy "#security-iam-awsmanpol-rosacontrolplaneoperatorpolicy").                                                                                                                                           | April 24, 2023    |
| ROSACloudNetworkConfigOperatorPolicy — New policy added   | ROSA added a new policy to allow the Cloud Network Config Controller Operator to provision and manage networking resources for the ROSA cluster networking overlay.<br>To learn more, see [AWS managed policy: ROSACloudNetworkConfigOperatorPolicy](#security-iam-awsmanpol-rosacloudnetworkconfigoperatorpolicy "#security-iam-awsmanpol-rosacloudnetworkconfigoperatorpolicy").                                                                                                           | April 20, 2023    |
| ROSAIngressOperatorPolicy — New policy added              | ROSA added a new policy to allow the Ingress Operator to provision and manage load balancers and DNS configurations for ROSA clusters.<br>To learn more, see [AWS managed policy: ROSAIngressOperatorPolicy](#security-iam-awsmanpol-rosaingressoperatorpolicy "#security-iam-awsmanpol-rosaingressoperatorpolicy").                                                                                                                                                                         | April 20, 2023    |
| ROSAAmazonEBSCSIDriverOperatorPolicy — New policy added   | ROSA added a new policy to allow the Amazon EBS CSI Driver Operator to install and maintain the Amazon EBS CSI driver on a ROSA cluster.<br>To learn more, see [AWS managed policy: ROSAAmazonEBSCSIDriverOperatorPolicy](#security-iam-awsmanpol-rosaamazonebscsidriveroperatorpolicy "#security-iam-awsmanpol-rosaamazonebscsidriveroperatorpolicy").                                                                                                                                      | April 20, 2023    |
| ROSAWorkerInstancePolicy — New policy added               | ROSA added a new policy to allow the service to manage cluster resources.<br>To learn more, see [AWS managed policy: ROSAWorkerInstancePolicy](#security-iam-awsmanpol-rosaworkerinstancepolicy "#security-iam-awsmanpol-rosaworkerinstancepolicy").                                                                                                                                                                                                                                         | April 20, 2023    |
| ROSAManageSubscription — New policy added                 | ROSA added a new policy to grant the AWS Marketplace permissions required to manage the ROSA subscription.<br>To learn more, see [AWS managed policy: ROSAManageSubscription](#security-iam-awsmanpol-rosamanagesubscription "#security-iam-awsmanpol-rosamanagesubscription").                                                                                                                                                                                                              | April 11, 2022    |
| Red Hat OpenShift Service on AWS started tracking changes | Red Hat OpenShift Service on AWS started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                      | March 2, 2022     |
