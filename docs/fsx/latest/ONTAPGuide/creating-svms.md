# Creating storage virtual machines (SVM)

You can create an FSx for ONTAP SVM using the AWS Management Console, AWS CLI, and API.

The maximum number of SVMs you can create for a file system depends on your file system's deployment type,
network type, and the amount of throughput capacity provisioned. For more information,
see [Maximum number of SVMs per file system](managing-svms.md#max-svms "managing-svms.md#max-svms").

## SVM properties

When creating an SVM, you define the following properties:

- The FSx for ONTAP file system to which it belongs.
- The Microsoft Active Directory (AD) configuration – You can optionally join your SVM to
  a self-managed AD for authentication and access control of Windows and macOS
  clients. For more information, see [Working with Microsoft Active Directory
  in FSx for ONTAP](ad-integration-ontap.md "ad-integration-ontap.md").
- The root volume security style – Set the root volume security style (Unix or NTFS)
  to align with the type of clients that you're using to access your data within
  the SVM. For more information, see [Volume security style](managing-volumes.md#volume-security-style "managing-volumes.md#volume-security-style").
- The SVM administrative password – you can optionally set the password for the SVM's `vsadmin` user.
  For more information, see [Managing SVMs with the ONTAP CLI](managing-resources-ontap-apps.md#vsadmin-ontap-cli "managing-resources-ontap-apps.md#vsadmin-ontap-cli").

###### To create a storage virtual machine

(console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **Storage virtual
   machines**.
3. Choose **Create new storage virtual
   machine**.
4. For **File system**, choose the file system to
   create the storage virtual machine on.
5. In the **Storage virtual machine name** field,
   provide a name for the storage virtual machine. You can use a
   maximum of 47 alphanumeric characters, plus the underscore (\_)
   special character.
6. For **SVM administrative password**, you can
   optionally choose **Specify a password** and
   provide a password for this SVM's `vsadmin` user.
   You can use the `vsadmin` user to administer the SVM
   using the ONTAP CLI or REST API. For more information about the
   `vsadmin` user, see [Managing SVMs with the ONTAP CLI](managing-resources-ontap-apps.md#vsadmin-ontap-cli "managing-resources-ontap-apps.md#vsadmin-ontap-cli").

If you choose **Don't specify a password**
(the default), you can still use the file system's
`fsxadmin` user to manage your file system using the
ONTAP CLI or REST API, but you can't use your SVM's
`vsadmin` user to do the same. 7. For **Active Directory**, you have the following
options:

    * If you are not joining your file system to an
     Active Directory (AD), choose **Do not join an Active
     Directory**.
    * If you are joining your SVM to a self-managed
     AD domain, choose **Join an Active
     Directory**, and provide the following details
     for your AD. For more information, see
     [Prerequisites for joining an SVM to a
     self-managed Microsoft AD](self-manage-prereqs.md "self-manage-prereqs.md").




    	+ The NetBIOS name of the Active Directory computer
    	 object to create for your SVM. The NetBIOS name
    	 cannot exceed 15 characters. This is the name of this SVM in Active Directory.
    	+ The fully qualified domain name (FQDN) of your Active
    	 Directory. The FQDN cannot exceed 255 characters.
    	+ **DNS server IP addresses** – The IPv4 or IPv6 addresses of the DNS servers for your domain.
    	+ **Service account credentials** – Choose how to provide your service account credentials:




    		- **Option 1**: AWS Secrets Manager secret ARN - The secret containing the username and password for a service account on your Active Directory domain. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager "self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager").
    		- **Option 2**: Plaintext credentials




    			* **Service account username** – The user name of the service account in your existing Microsoft Active Directory. Don't include a domain prefix or suffix. For example, for `EXAMPLE\ADMIN`, use only `ADMIN`.
    			* **Service account password** – The password for the service account.
    			* **Confirm password** – The password for the service account.
    	+ (Optional) **Organizational Unit
    	 (OU)** – The distinguished path
    	 name of the organizational unit to which you want to
    	 join your file system.
    	+ **Delegated file system
    	 administrators group** – The name of the group
    	 in your AD that can administer your file system.


    	If you are using AWS Managed Microsoft AD, you must specify a group
    	 such as AWS Delegated FSx Administrators, AWS Delegated
    	 Administrators, or a custom group with delegated permissions to
    	 the OU.


    	If you are joining to a self-managed AD,
    	 use the name of the group in your AD. The default group is
    	 `Domain Admins`.

8. For **SVM root volume security style**, choose
   the security style for the SVM depending on the type of clients that
   access your data. Choose **Unix (Linux)** if you
   primarily access your data using Linux clients; choose
   **NTFS** if you primarily access your data
   using Windows clients. For more information, see
   [Volume security style](managing-volumes.md#volume-security-style "managing-volumes.md#volume-security-style").
9. Choose **Confirm** to create the storage virtual
   machine.
   You can monitor the update progress on the **File
   systems** detail page, in the **Status**
   column of the **Storage virtual machines** pane. The
   storage virtual machine is ready for use when its status is
   **Created**.

## To create a storage virtual machine

(CLI)

- To create an FSx for ONTAP storage virtual machine (SVM), use the
  [create-storage-virtual-machine](../../../cli/latest/reference/fsx/create-storage-virtual-machine.md "../../../cli/latest/reference/fsx/create-storage-virtual-machine.md") CLI command (or the
  equivalent [CreateStorageVirtualMachine](../APIReference/API_CreateStorageVirtualMachine.md "../APIReference/API_CreateStorageVirtualMachine.md") API operation), as shown in
  the following example.

```
`aws fsx create-storage-virtual-machine \
 --file-system-id fs-0123456789abcdef0 \
 --name svm1 \
 --svm-admin-password `password` \
 --active-directory-configuration SelfManagedActiveDirectoryConfiguration='{DomainName="corp.example.com", \
OrganizationalUnitDistinguishedName="OU=FileSystems,DC=corp,DC=example,DC=com",FileSystemAdministratorsGroup="FSxAdmins", \
UserName="`FSxService`",Password="`password`", \
 DnsIps=["10.0.1.18"]}',NetBiosName=amznfsx12345`
```

After successfully creating the storage virtual machine, Amazon FSx returns its
description in JSON format, as shown in the following
example.

```
{
  "StorageVirtualMachine": {
    "CreationTime": 1625066825.306,
    "Endpoints": {
      "Management": {
        "DnsName": "svm-abcdef0123456789a.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
        "IpAddressses": ["198.19.0.4"]
      },
      "Nfs": {
        "DnsName": "svm-abcdef0123456789a.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
        "IpAddressses": ["198.19.0.4"]
      },
      "Smb": {
        "DnsName": "amznfsx12345",
        "IpAddressses": ["198.19.0.4"]
      },
      "SmbWindowsInterVpc": {
        "IpAddressses": ["198.19.0.5", "198.19.0.6"]
      },
      "Iscsi": {
        "DnsName": "iscsi.svm-abcdef0123456789a.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
        "IpAddressses": ["198.19.0.7", "198.19.0.8"]
      }
    },
    "FileSystemId": "fs-0123456789abcdef0",
    "Lifecycle": "CREATING",
    "Name": "vol1",
    "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:storage-virtual-machine/fs-0123456789abcdef0/svm-abcdef0123456789a",
    "StorageVirtualMachineId": "svm-abcdef0123456789a",
    "Subtype": "default",
    "Tags": [],
    "ActiveDirectoryConfiguration": {
      "NetBiosName": "amznfsx12345",
      "SelfManagedActiveDirectoryConfiguration": {
        "UserName": "Admin",
        "DnsIps": [
          "10.0.1.3",
          "10.0.91.97"
        ],
        "OrganizationalUnitDistinguishedName": "OU=Computers,OU=customer-ad,DC=customer-ad,DC=example,DC=com",
        "DomainName": "customer-ad.example.com"
      }
    }
  }
}
```
