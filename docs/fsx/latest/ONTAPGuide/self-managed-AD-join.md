# How joining SVMs to Microsoft Active Directory works

Your organization might manage identities and devices using an Active Directory, whether on-premises or in
the cloud. With FSx for ONTAP, you can join your SVMs directly to your existing Active Directory
domain in the following ways:

- Joining new SVMs to an Active Directory at creation:
  - Using the **Standard create** option in Amazon FSx console to create a new
    FSx for ONTAP file system, you can join the default SVM to a self-managed Active Directory. For more information,
    see [To create a file system
    (console)](creating-file-systems.md#create-MAZ-file-system-console "creating-file-systems.md#create-MAZ-file-system-console").
  - Using the Amazon FSx console, AWS CLI, or Amazon FSx API to create a new SVM on an existing FSx for ONTAP file system.
    For more information, see [Creating storage virtual machines (SVM)](creating-svms.md "creating-svms.md").

- Joining existing SVMs to an Active Directory:
  - Using the AWS Management Console, AWS CLI, and API to join an SVM to an Active Directory, and to reattempt joining an SVM to an Active Directory
    if the initial attempt to join failed. You can also update some Active Directory configuration properties for SVMs that are
    already joined to an Active Directory. For more information, see
    [Managing SVM Active Directory configurations](manage-svm-ad-config.md "manage-svm-ad-config.md").
  - Using the NetApp ONTAP CLI or REST API to join, reattempt joining, and unjoining SVM Active Directory configurations. For more information,
    see [Updating SVM Active Directory configurations using the NetApp CLI](manage-svm-ad-config-ontap-cli.md "manage-svm-ad-config-ontap-cli.md").

###### Important

- Amazon FSx only registers DNS records for an SVM if you use Microsoft DNS as the default DNS
  service. If you use a third-party DNS, you must set up DNS entries manually for your
  Amazon FSx SVMs after you create them.
- If you use AWS Managed Microsoft AD, you must specify a group such as AWS Delegated FSx Administrators,
  AWS Delegated Administrators, or a custom group with delegated permissions to the
  OU.
  When you join an FSx for ONTAP SVM directly to a self-managed Active Directory, the SVM resides in the
  same Active Directory forest (the top-most logical container in an Active Directory configuration that contains domains,
  users, and computers) and in the same Active Directory domain as your users and existing resources, including
  existing file servers.

## Information needed when joining an SVM to an Active Directory

You have to provide the following information about your Active Directory when joining an SVM to an Active Directory,
regardless of the API operation you choose:

- The NetBIOS name of the Active Directory computer object to create for your SVM. This is the name of the SVM
  in Active Directory, which must be unique within your Active Directory. Don't use the NetBIOS name of the home
  domain. The NetBIOS name can't exceed 15 characters.
- The fully qualified domain name (FQDN) of your Active Directory. The FQDN can't exceed 255
  characters.

###### Note

The FQDN can't be in the Single Label Domain (SLD) format. Amazon FSx doesn't support SLD domains.

- Up to three IP addresses of the DNS servers or domain hosts for your domain.

The DNS server IP addresses and Active Directory domain controller IP addresses can be in any IP address
range, except:

    + IP addresses that conflict with Amazon Web Services-owned IP addresses in that AWS Region. For a list
     of AWS IP addresses by Region, see the [AWS IP address ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md").
    + IP addresses in the following CIDR block range: 198.19.0.0/16

- Credentials for an Active Directory service account that Amazon FSx uses to join the SVM to your domain. You can provide these as either:
  - **Option 1:** AWS Secrets Manager secret ARN - The secret containing the username and password for a service account on your Active Directory domain. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager "self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager").
  - **Option 2:** Plaintext credentials
    - **Service account username** – The user name of the service account in your existing Microsoft Active Directory. Don't include a domain prefix or suffix. For example, for `EXAMPLE\ADMIN`, use only `ADMIN`.
    - **Service account password** – The password for the service account.

- (Optional) The Organizational Unit (OU) in the domain that you join the SVM to.

###### Note

If you join your SVM to an AWS Directory Service Active Directory, you must provide an OU that's within the default OU
that Directory Service creates for the directory objects that are related to AWS. This is
because the Directory Service doesn't provide access to your Active Directory's default
`Computers` OU. For example, if your Active Directory domain is
`example.com`, you can specify the following OU:
`OU=Computers,OU=example,DC=example,DC=com`.

- (Optional) The domain group that you are delegating authority to for performing
  administrative actions on your file system. For example, this domain group might manage
  Windows SMB file shares, take ownership of files and folders, and so on. If you don’t
  specify this group, Amazon FSx delegates this authority to the Domain Admins group in your
  Active Directory domain by default.
