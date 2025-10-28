# Best practices for working with Active Directory

Here are some suggestions and guidelines that you should consider when joining Amazon FSx for NetApp ONTAP
SVMs to your self-managed Microsoft Active Directory. Note that these are recommended as best
practices, but not required.

## Delegating permissions to your Amazon FSx service

account

Make sure to configure the service account that you provide to Amazon FSx with the minimum
permissions required. In addition, separate the Organizational Unit (OU) from other domain
controller concerns.

To join Amazon FSx SVMs to your domain, make sure that the service account has delegated
permissions. Members of the **Domain Admins** group have sufficient
permissions to perform this task. However, as a best practice, use a service account that only
has the minimum permissions necessary to do this. The following procedure demonstrates how to
delegate only the permissions necessary to join FSx for ONTAP SVMs to your domain.

Perform this procedure on a machine that's joined to your directory and has the Active
Directory User and Computers MMC snap-in installed.

###### To create a service account for your Microsoft Active Directory domain

1. Make sure that you're logged in as a domain administrator for your Microsoft Active Directory domain.
2. Open the **Active Directory User and Computers** MMC snap-in.
3. In the task pane, expand the domain node.
4. Locate and open the context (right-click) menu for the OU that you want to modify, and
   then choose **Delegate Control**.
5. On the **Delegation of Control Wizard** page,
   choose **Next**.
6. Choose **Add** to add a specific user or a specific group for
   **Selected users and groups**, and then choose
   **Next**.
7. On the **Tasks to Delegate** page, choose **Create a custom task
   to delegate**, and then choose **Next**.
8. Choose **Only the following objects in the folder**, and then choose
   **Computer objects**.
9. Choose **Create selected objects in this folder** and **Delete
   selected objects in this folder**. Then choose **Next**.
10. Under **Show these permissions**, ensure that **General** and
    **Property-specific** are selected.
11. For **Permissions**, choose the following:
    - **Reset Password**
    - **Read and write Account Restrictions**
    - **Validated write to DNS host name**
    - **Validated write to service principal name**
    - **Write msDS-SupportedEncryptionTypes**

12. Choose **Next**, and then choose **Finish**.
13. Close the **Active Directory User and Computers** MMC snap-in.

###### Important

Don't move computer objects that Amazon FSx creates in the OU after your SVMs are created. Doing
so will cause your SVMs to become misconfigured.

## Keeping your Active Directory configuration updated with

Amazon FSx

For uninterrupted availability of your Amazon FSx SVMs, update an SVM's self-managed Active
Directory (AD) configuration when you change your self-managed AD setup.

For example, suppose that your AD uses a time-based password reset policy. In this case, as
soon as the password is reset, make sure to update the service account password with Amazon FSx. To do
this, use the Amazon FSx console, Amazon FSx API, or AWS CLI. Similarly, if the DNS server IP addresses
change for your Active Directory domain, as soon as the change occurs update the DNS server IP
addresses with Amazon FSx.

If there's an issue with the updated self-managed AD configuration, the SVM state switches
to **Misconfigured**. This state shows an error message and a recommended
action beside the SVM description in the console, API, and CLI. If an issue with your SVM's AD
configuration occurs, be sure to take the recommended corrective action for the configuration
properties. If the issue is resolved, verify that your SVM's state changes to
**Created**.

For more information, see [Updating existing SVM Active Directory configurations using the AWS Management Console, AWS CLI, and API](update-svm-ad-config.md "update-svm-ad-config.md") and
[Modify an Active Directory configuration using the ONTAP CLI](manage-svm-ad-config-ontap-cli.md#using-ontap-cli-to-modify-ad "manage-svm-ad-config-ontap-cli.md#using-ontap-cli-to-modify-ad").

## Using security groups to limit traffic within your

VPC

To limit network traffic in your virtual private cloud (VPC), you can implement the
principle of least privilege in your VPC. In other words, you can limit permissions to the
minimum ones necessary. To do this, use security group rules. To learn more, see [Amazon VPC security groups](limit-access-security-groups.md#fsx-vpc-security-groups "limit-access-security-groups.md#fsx-vpc-security-groups").

## Creating outbound security group rules for your file system's

network interface

For greater security, consider configuring a security group with outbound traffic rules.
These rules should allow outbound traffic only to your self-managed AD domains
controllers or within the subnet or security group. Apply this security group to the VPC
associated with your Amazon FSx file system's elastic network interface. To learn more, see
[File System Access Control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").
