# Storage

Refer to the sizing section for resources on SAP’s standard recommendations. If no storage performance requirements are available, AWS recommends General Purpose SSD (gp2) as the default EBS volume type for SAP workloads.

In practice, application servers will have a minimum of two volumes, mapped to the `C:` and `D:` drives. The `C:` drive is the boot volume containing the OS, and the `D:` drive is used to host the SAP software. We recommend using an additional, temporary volume for SAP software downloads (typically mapped as the `E:` drive).

If the installation type is distributed or HA, fileshares for the global filesystem and transport directories will need to be used across all relevant EC2 instances. In this guide, we use the standard Windows file sharing features to share these directories from the EC2 instance hosting the central services. The `sapinst.exe` installer creates these shares automatically if it is run as a user with appropriate permissions.

Customers can also use NFS-based solutions, such as [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/"), third-party solutions available from the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace"), or custom-built solutions. Choosing the correct NFS solution is beyond the scope of this guide. If you use such a solution as part of a high availability deployment, consider that the NFS solution could itself be a single point of failure without appropriate protection.
