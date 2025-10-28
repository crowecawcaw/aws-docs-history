# Use AMS SSP to provision Amazon FSx in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon FSx capabilities directly in your AMS managed account. Amazon FSx provides fully managed third-party file systems. Amazon FSx provides you with the native compatibility of
third-party file systems with feature sets for workloads such as Windows-based storage, high-performance computing (HPC),
machine learning, and electronic design automation (EDA). Amazon FSx automates the time-consuming administration tasks such as hardware provisioning, software configuration,
patching, and backups. Amazon FSx integrates the file systems with cloud-native AWS services, making them even more useful for a broader set of workloads.

Amazon FSx provides you with two file systems to choose from: Amazon FSx for Windows File Server for Windows-based
applications and Amazon FSx for Lustre for compute-intensive workloads.
To learn more, see [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/").

## Amazon FSx in AWS Managed Services FAQ

**Q: How do I request access to Amazon FSx in my AMS account?**

Request access to Amazon FSx by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account:
`customer_fsx_admin_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon FSx in my AMS account?**

There are no restrictions. Full functionality of the service is available.

**Q: What are the prerequisites or dependencies to using Amazon FSx in my AMS account?**

There are no prerequisites. However, for advance configurations like Multi-AZ, you must install and
manage the DFS Replication and DFS Namespaces services. For more information, see
[Deploying Multi-AZ File Systems](../../../fsx/latest/WindowsGuide/multi-az-deployments.md "../../../fsx/latest/WindowsGuide/multi-az-deployments.md").

**Q: How do I integrate my Amazon FSx file system with my multi-account landing zone Managed AD?**

When creating an Amazon FSx file system, you can specify your MALZ Managed AD as the
'AWS Managed Microsoft Active Directory' for Windows Authentication.
For more information see,
[Using Amazon FSx with AWS Directory Service for Microsoft Active Directory](../../../fsx/latest/WindowsGuide/fsx-aws-managed-ad.md "../../../fsx/latest/WindowsGuide/fsx-aws-managed-ad.md")

You must also share the Managed AD to the application account first. Do this by submitting an
RFC with the Management | Directory Service | Directory | Share directory change type (ct-369odosk0pd9w).

**Q: Which users belong in the **AWS Delegated FSx Administrators**
group?**

Only IT file server administrators. This group has **Full Access** privileges across all file shares.

**Q: Should I use the default file share, **share**, which is created when the FSx
system is provisioned?**

No, we don't recommend using the the default file share,
**share**, as provisioned. It grants **Full
Access** to **Everyone**, which which violates
the principle of least privilege. Instead, create smaller, custom file
shares that match your business needs.

**Q: How can I create custom file shares for specific organizations in my business?**

See [File Shares](../../../fsx/latest/WindowsGuide/managing-file-shares.md "../../../fsx/latest/WindowsGuide/managing-file-shares.md") for
instructions on creating custom file shares. Restrict access on each file share using the principle of least privilege.
