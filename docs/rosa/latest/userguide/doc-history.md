

# Document history
<a name="doc-history"></a>

The following table describes the important changes to the documentation. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Updated ROSAAmazonEBSCSIDriverOperatorPolicy](#doc-history) | We updated the managed policy `ROSAAmazonEBSCSIDriverOperatorPolicy` to extend the Amazon EBS CSI driver to the release-1.61 feature set. With this update, the Amazon EBS CSI Driver Operator can copy and lock Amazon EBS snapshots and enable fast snapshot restores. It can also use customer-managed AWS KMS keys for encrypted volume operations. For more information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | August 18, 2026 | 
| [Updated ROSANodePoolManagementPolicy](#doc-history) | Updated the AWS managed policy ROSANodePoolManagementPolicy to allow the NodePool controller to describe EC2 instance types. The controller can also receive and delete spot-instance interruption messages from customer-managed Amazon SQS queues carrying the `red-hat: "true"` resource tag. For more information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | July 28, 2026 | 
| [Updated ROSAControlPlaneOperatorPolicy](#doc-history) | Updated the AWS managed policy ROSAControlPlaneOperatorPolicy. With this update, the Control Plane Operator can add and remove tags on Red Hat-managed security groups (`ec2:DeleteTags`). A safeguard prevents the operator from removing the `red-hat-managed` tag itself. For more information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | July 28, 2026 | 
| [New ROSAKarpenterControllerPolicy](#doc-history) |  AWS released a new managed policy `ROSAKarpenterControllerPolicy` to enable the Karpenter controller to dynamically provision, scale, and manage EC2 worker nodes for ROSA with hosted control planes clusters. For more information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | July 22, 2026 | 
| [Updated ROSAControlPlaneOperatorPolicy](#doc-history) | Updated the AWS managed policy ROSAControlPlaneOperatorPolicy to allow tagging of Red Hat-managed security groups for proper resource lifecycle management and to add security-group/\* to ManageVPCEndpointWithCondition to fix VPCE reconciliation failures during cluster upgrades. For more information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | April 9, 2026 | 
| [Updated ROSAKubeControllerPolicy](#doc-history) | Updated the AWS managed policy ROSAKubeControllerPolicy to clarify Elastic Load Balancing permissions for registering and deregistering targets with target groups. For more information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | March 5, 2026 | 
| [Updated ROSANodePoolManagementPolicy](#doc-history) |  ROSA has updated the managed policy `ROSANodePoolManagementPolicy` to add resource access for capacity reservations to support the Capacity Reservations feature. For information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | September 3, 2025 | 
| [Updated ROSAInstallerPolicy](#doc-history) | Updated the AWS managed policy ROSAInstallerPolicy to support the new Capacity Reservations feature in ROSA and improve Kubernetes cluster tag management. For information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | August 7, 2025 | 
| [New ROSASharedVPCRoute53Policy](#doc-history) |  ROSA has released a new managed policy `ROSASharedVPCRoute53Policy` to allow the ROSA installer to configure Route 53 records in shared VPC environments. For information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | August 7, 2025 | 
| [New ROSASharedVPCEndpointPolicy](#doc-history) |  ROSA has released a new managed policy `ROSASharedVPCEndpointPolicy` to allow the ROSA installer to configure VPC endpoints and security groups in shared VPC environments. This policy provides a subset of EC2 permissions tailored for shared VPC use cases. For information, see [ROSA updates to AWS managed policies](https://docs.aws.amazon.com/rosa/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-account-updates). | August 7, 2025 | 
| [Updated ROSAImageRegistryOperatorPolicy](#doc-history) | Updated the AWS managed policy ROSAImageRegistryOperatorPolicy. | May 19, 2025 | 
| [Updated ROSANodePoolManagementPolicy](#doc-history) | Updated the AWS managed policy ROSANodePoolManagementPolicy . | May 5, 2025 | 
| [Updated ROSAImageRegistryOperatorPolicy](#doc-history) | Updated the AWS managed policy ROSAImageRegistryOperatorPolicy. | April 16, 2025 | 
| [Updated ROSAWorkerInstancePolicy](#doc-history) | Updated the AWS managed policy ROSAWorkerInstancePolicy. | March 3, 2025 | 
| [Updated ROSANodePoolManagementPolicy](#doc-history) | Updated the AWS managed policy ROSANodePoolManagementPolicy. | February 24, 2025 | 
| [Updated ROSAAmazonEBSCSIDriverOperatorPolicy](#doc-history) | Updated the AWS managed policy ROSAAmazonEBSCSIDriverOperatorPolicy. | January 17, 2025 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Middle East (UAE) AWS Region. | May 13, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Europe (Paris) AWS Region. | May 6, 2024 | 
| [Updated ROSANodePoolManagementPolicy](#doc-history) | Updated the AWS managed policy ROSANodePoolManagementPolicy. | May 2, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Europe (Spain) AWS Region. | April 29, 2024 | 
| [Updated ROSAInstallerPolicy](#doc-history) | Updated the AWS managed policy ROSAInstallerPolicy. | April 24, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Europe (Zurich) AWS Region. | April 19, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Asia Pacific (Osaka) AWS Region. | April 17, 2024 | 
| [Updated ROSAInstallerPolicy and ROSASRESupportPolicy](#doc-history) | Updated the AWS managed policies ROSAInstallerPolicy and ROSASRESupportPolicy. | April 10, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Asia Pacific (Hong Kong) AWS Region. | April 8, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the South America (São Paulo) AWS Region. | April 1, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Middle East (Bahrain) AWS Region. | March 25, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Asia Pacific (Seoul) AWS Region. | March 14, 2024 | 
| [ROSA with HCP AWS Region expansion](#doc-history) | ROSA with hosted control planes (HCP) is now available in the Africa (Cape Town) AWS Region. | March 5, 2024 | 
| [Updated ROSAInstallerPolicy](#doc-history) | Updated the AWS managed policy ROSAInstallerPolicy. | January 26, 2024 | 
| [Updated ROSASRESupportPolicy](#doc-history) | Updated the AWS managed policy ROSASRESupportPolicy. | January 22, 2024 | 
| [Updated ROSAImageRegistryOperatorPolicy](#doc-history) | Updated the AWS managed policy ROSAImageRegistryOperatorPolicy. | December 12, 2023 | 
| [Updated ROSAKubeControllerPolicy](#doc-history) | Updated the AWS managed policy ROSAKubeControllerPolicy. | October 16, 2023 | 
| [Updated ROSAManageSubscription](#doc-history) | Updated the AWS managed policy ROSAManageSubscription. | August 1, 2023 | 
| [Updated ROSAKubeControllerPolicy](#doc-history) | Updated the AWS managed policy ROSAKubeControllerPolicy. | July 13, 2023 | 
| [Added ROSA security pages](#doc-history) | Resilience in ROSA, Infrastructure security in ROSA, and Data protection in ROSA pages were added. | June 30, 2023 | 
| [Added the deployment options page](#doc-history) | Deployment options page was added. | June 9, 2023 | 
| [Added new AWS managed policy ROSANodePoolManagementPolicy](#doc-history) | New AWS managed policy ROSANodePoolManagementPolicy was added. | June 8, 2023 | 
| [Added new AWS managed policy ROSAInstallerPolicy](#doc-history) | New AWS managed policy ROSAInstallerPolicy was added. | June 6, 2023 | 
| [Added new AWS managed policy ROSASRESupportPolicy](#doc-history) | New AWS managed policy ROSASRESupportPolicy was added. | June 1, 2023 | 
| [Added Overview of responsibilities for ROSA](#doc-history) | Added Overview of responsibilities for ROSA page. | May 26, 2023 | 
| [Updated What is Red Hat OpenShift Service on AWS?](#doc-history) | Updated the What is Red Hat OpenShift Service on AWS page. | May 24, 2023 | 
| [Added new AWS managed policies for ROSA operator roles](#doc-history) | New AWS managed policies ROSAImageRegistryOperatorPolicy, ROSAKubeControllerPolicy, and ROSAKMSProviderPolicy were added. | April 27, 2023 | 
| [Added new AWS managed policy ROSAControlPlaneOperatorPolicy](#doc-history) | New AWS managed policy ROSAControlPlaneOperatorPolicy was added. | April 24, 2023 | 
| [Added new AWS managed policies for ROSA account roles](#doc-history) | New AWS managed policy pages for ROSA account and operator roles page were added. | April 20, 2023 | 
| [Added the ROSA service quotas page](#doc-history) | The ROSA service quotas page was added. | December 22, 2022 | 
| [Added troubleshooting pages](#doc-history) | Troubleshooting pages were added. | November 1, 2022 | 
| [Added getting started pages](#doc-history) | Getting started pages were added. | August 12, 2022 | 
| [Added new AWS managed policy ROSAManageSubscription](#doc-history) | New AWS managed policy ROSAManageSubscription was added. | April 11, 2022 | 
| [Initial release](#doc-history) | The initial release of the Red Hat OpenShift Service on AWS User Guide. | March 24, 2021 | 