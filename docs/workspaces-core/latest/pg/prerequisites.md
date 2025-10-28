# Prerequisites

To deploy a Amazon WorkSpaces Core-based virtual desktop infrastructure (VDI) using WorkSpaces Core bundles
or Managed Instances, customers must meet the following requirements:

- Customers must either work with a technology partner or build and manage their
  own control plane. This includes brokering, orchestration, and pixel streaming
  capabilities.
- For customers who choose to deploy using WorkSpaces Core bundles, Active Directory integration
  is required. This can be achieved by deploying AWS Managed Microsoft AD in the customer’s
  account or by using an existing on-premises or self-managed directory.
- Customers are expected to supply their own pixel streaming protocol, regardless
  of the provisioning model used.
- If the deployment includes the Windows Client operating system, customers must meet
  the requirements of the Bring Your Own License (BYOL) model. This includes using eligible
  Windows desktop licenses that are covered under Microsoft’s licensing terms for AWS. Detailed
  information about BYOL eligibility and deployment can be found in the
  [Amazon WorkSpaces Administration Guide](../../../workspaces/latest/adminguide/byol-windows-images.md "../../../workspaces/latest/adminguide/byol-windows-images.md").
- If customers are deploying desktops using the Windows Server operating system, they will
  need to provide Remote desktop licensing.

      + Amazon WorkSpaces Core includes a license that permits two Remote Desktop connections
       for administrative use only. To support additional concurrent user sessions, customers must acquire
       Microsoft Remote Desktop Services (RDS) Client Access Licenses (CALs) with active Software Assurance.
       These licenses can be brought to AWS through Microsoft’s License Mobility program.


      + If customers have Microsoft Software Assurance with License Mobility, they might be able
       to bring their Microsoft RDS CALs and then use them with Amazon WorkSpaces Core. For more information
       about how to sign up for and complete a license verification process, and to view eligibility requirements,
       see License Mobility.
      + To verify license eligibility through License Mobility, complete the following steps:




      	1. Confirm that your Microsoft licenses include Software Assurance and are eligible for License Mobility.
      	2. Go to the Microsoft License Mobility Verification form.
      	3. Fill out the form using the following AWS partner details:




      		- Email Address: `microsoft@amazon.com`
      		- Partner Name: `Amazon Web Services`
      		- Partner Website: `aws.amazon.com`
      	4. Submit the form to Microsoft.
      	5. Wait for confirmation from Microsoft, which will be sent to both you and AWS upon successful
      	 verification. For more information, see Microsoft licensing on AWS.

  For more information, see [Microsoft licensing on AWS](../../../prescriptive-guidance/latest/migration-microsoft-workloads-aws/licensing-microsoft-workloads.md "../../../prescriptive-guidance/latest/migration-microsoft-workloads-aws/licensing-microsoft-workloads.md").
