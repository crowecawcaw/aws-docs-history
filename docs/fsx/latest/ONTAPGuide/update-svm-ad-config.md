# Updating existing SVM Active Directory configurations using the AWS Management Console, AWS CLI, and API

Use the following procedure to update the Active Directory configuration of an SVM that is already joined to an Active Directory.

###### To update an SVM Active Directory configuration (AWS Management Console)

1.  Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2.  Choose the SVM to update as follows:

        * In the left navigation pane, choose **File systems**, and then choose the
         ONTAP file system with the SVM you want to update.
        * Choose the **Storage virtual machines**
         tab.


        –Or–
        * To display a list of all of the SVMs available, in the left navigation pane, expand
         **ONTAP** and choose **Storage virtual
         machines**.

    Select the SVM that you want to update from the list.

3.  On the SVM **Summary** panel, choose
    **Actions** > **Join/Update Active Directory**.
    The **Update SVM Active Directory configuration** window appears.
4.  You can update the following Active Directory configuration properties in this window.
    - **DNS server IP addresses**
      – The IPv4 or IPv6 addresses of the DNS servers for your domain.
    - **Service account credentials** – Choose how to provide your service account credentials:
      - **Option 1**: AWS Secrets Manager secret ARN - The secret containing the username and password for a service account on your Active Directory domain. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager "self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager").
      - **Option 2**: Plaintext credentials
        - **Service account username** – The user name of the service account in your existing Microsoft Active Directory. Don't include a domain prefix or suffix. For example, for `EXAMPLE\ADMIN`, use only `ADMIN`.
        - **Service account password** – The password for the service account.
        - **Confirm password** – The password for the service account.

5.  After you have entered your updates, choose **Update Active Directory**
    to make the changes.
    Use the following procedure to update the Active Directory configuration of an SVM that is already joined to an Active Directory.

###### To update an SVM Active Directory configuration (AWS CLI)

- To update an SVM's Active Directory configuration with the AWS CLI or API, use the
  [update-storage-virtual-machine](../../../cli/latest/reference/fsx/update-storage-virtual-machine.md "../../../cli/latest/reference/fsx/update-storage-virtual-machine.md") CLI command (or the equivalent
  [UpdateStorageVirtualMachine](../APIReference/API_UpdateStorageVirtualMachine.md "../APIReference/API_UpdateStorageVirtualMachine.md") API operation), as shown in the following
  example.

```
`aws fsx update-storage-virtual-machine \
 --storage-virtual-machine-id svm-abcdef0123456789a\
 --active-directory-configuration \
 SelfManagedActiveDirectoryConfiguration='{UserName="`FSxService`",\
 Password="`password`", \
 DnsIps=["10.0.1.18"]}'`
```
