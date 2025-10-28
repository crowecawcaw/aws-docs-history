# You can't join a storage virtual machine (SVM) to Active Directory

If you're unable to join an SVM to an Active Directory (AD),
first review [How joining SVMs to Microsoft Active Directory works](self-managed-AD-join.md "self-managed-AD-join.md"). Common problems
that prevent an SVM from joining to your Active Directory are listed in the following sections, including the error
messages generated for each circumstance.

###### Topics

- [The SVM NetBIOS name is the same as the
  NetBIOS name for the home domain.](#join-svm-ad-fails-netbios-name-home-domain "#join-svm-ad-fails-netbios-name-home-domain")
- [The SVM is already joined to another Active Directory](#join-svm-ad-fails-already-joined "#join-svm-ad-fails-already-joined")
- [Amazon FSx can't connect to your Active Directory domain controllers
  because the SVM's NetBIOS name is already in use](#join-svm-ad-fails-netbios-name-in-use "#join-svm-ad-fails-netbios-name-in-use")
- [Amazon FSx can't communicate with your Active Directory domain controllers](#join-svm-ad-fails-no-port-traffic "#join-svm-ad-fails-no-port-traffic")
- [Amazon FSx can't connect to your
  Active Directory due to unmet port requirements or service account permissions](#join-svm-ad-fails-ports-or-permissions "#join-svm-ad-fails-ports-or-permissions")
- [Amazon FSx can't connect to your Active Directory
  domain controllers because the service account credentials are not valid](#join-svm-ad-fails-invalid-service-credentials "#join-svm-ad-fails-invalid-service-credentials")
- [Amazon FSx can't connect to your Active
  Directory domain controllers because of insufficient service account credentials](#join-svm-ad-fails-insufficient-service-credentials "#join-svm-ad-fails-insufficient-service-credentials")
- [Amazon FSx can't communicate with your Active
  Directory DNS servers or domain controllers](#join-svm-ad-fails-dns-servers "#join-svm-ad-fails-dns-servers")
- [Amazon FSx can't communicate with your Active
  Directory because of a invalid Active Directory domain name.](#join-svm-ad-fails-fqdn "#join-svm-ad-fails-fqdn")
- [The service account can't access the administrators group specified in the SVM Active Directory configuration](#join-svm-ad-fails-no-admin-group "#join-svm-ad-fails-no-admin-group")
- [Amazon FSx can't connect to the Active
  Directory domain controllers because the organizational unit specified doesn't exist or
  isn't accessible](#bad-org-unit-service-credentials "#bad-org-unit-service-credentials")

## The SVM NetBIOS name is the same as the

NetBIOS name for the home domain.

Joining an SVM to your self-managed Active Directory fails with the following error message:

**`Amazon FSx is unable to establish a connection with your Active Directory. This is because
 the server name you specified is the NetBIOS name of the home domain. To fix this problem, 
 choose a NetBIOS name for your SVM that is different from the NetBIOS name of the home domain. Then 
 reattempt to join your SVM to your Active Directory.`**

To resolve this issue, follow the procedure described in [Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API](join-svm-to-ad.md "join-svm-to-ad.md") to reattempt joining your SVM to your AD. Ensure that you use
a NetBIOS name for your SVM that's different than the NetBIOS name of the Active Directory's
home domain.

## The SVM is already joined to another Active Directory

Joining an SVM to an Active Directory fails with the following error message:

**`Amazon FSx is unable to establish a connection to your Active Directory. This is because the SVM is already joined to a domain. 
 To join this SVM to a different domain, you can use the ONTAP CLI or REST API to unjoin this SVM from Active Directory. Then reattempt 
 to join your SVM to a different Active Directory.`**

To resolve the issue, do the following:

1. Use the NetApp ONTAP CLI to unjoin the SVM from its current Active Directory. For more
   information, see [Unjoin an Active Directory from your SVM using the NetApp ONTAP CLI](manage-svm-ad-config-ontap-cli.md#using-ontap-cli-to-unjoin-ad "manage-svm-ad-config-ontap-cli.md#using-ontap-cli-to-unjoin-ad").
2. Follow the procedure described in
   [Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API](join-svm-to-ad.md "join-svm-to-ad.md") to reattempt joining your SVM to the new AD.

## Amazon FSx can't connect to your Active Directory domain controllers

because the SVM's NetBIOS name is already in use

Creating an SVM joined to your self-managed AD fails with the following error message:

**`Amazon FSx is unable to establish a connection with your Active Directory. This is because the NetBIOS (computer) name you specified 
 is already in-use in your Active Directory. To fix this problem, pick a NetBIOS name for your SVM that is not in use in your Active Directory., specifying a NetBIOS (computer)
 Then reattempt to join your SVM to your Active Directory.`**

To resolve this issue, follow the procedure described in [Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API](join-svm-to-ad.md "join-svm-to-ad.md") to reattempt joining your SVM to your AD. Ensure that you use
a NetBIOS name for your SVM that's unique and not already in use in your Active
Directory.

## Amazon FSx can't communicate with your Active Directory domain controllers

Joining an SVM to your self-managed AD fails with the following error message:

**`Amazon FSx is unable to communicate with your Active Directory. 
 To fix this problem, ensure that network traffic is allowed between Amazon FSx and your domain controllers. 
 Then reattempt to join your SVM to your Active Directory.`**

To resolve this issue, do the following:

1. Review the requirements described in
   [Network configuration requirements](self-manage-prereqs.md#ontap-ad-network-configs "self-manage-prereqs.md#ontap-ad-network-configs"), and make changes
   needed to enable network communications between Amazon FSx and your AD.
2. Once Amazon FSx is able to communicate with your AD, follow the procedure described in
   [Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API](join-svm-to-ad.md "join-svm-to-ad.md") and reattempt joining your SVM to your AD.

## Amazon FSx can't connect to your

Active Directory due to unmet port requirements or service account permissions

Joining an SVM to your self-managed AD fails with the following error message:

**`Amazon FSx is unable to establish a connection with your Active Directory. This is due to either the port 
 requirements for your Active Directory not being met, or the service account provided not having permissions 
 to join the storage virtual machine to the domain with the specified organization unit. To fix this problem, 
 update your storage virtual machine's Active Directory configuration after resolving any permissions issues 
 with ports and service accounts, as recommended in the Amazon FSx user guide.`**

To resolve this issue, do the following:

1. Review the requirements described in
   [Network configuration requirements](self-manage-prereqs.md#ontap-ad-network-configs "self-manage-prereqs.md#ontap-ad-network-configs"), and make changes
   needed to meet the networking requirements and make sure communications are enabled on the required ports
2. Review the service account requirements described in
   [Active Directory service account requirements](self-manage-prereqs.md#ontap-ad-service-account-prereqs "self-manage-prereqs.md#ontap-ad-service-account-prereqs"). Ensure that
   service account has the delegated permissions necessary to join your SVM to the
   AD domain using the specified organizational unit.
3. Once you have made changes to the port permissions or the service account, follow the procedure described in
   [Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API](join-svm-to-ad.md "join-svm-to-ad.md") and reattempt joining your SVM to your AD.

## Amazon FSx can't connect to your Active Directory

domain controllers because the service account credentials are not valid

Joining an SVM to your self-managed Active Directory fails with the following error message:

**`Amazon FSx is unable to establish a connection with your Active Directory domain controller(s) 
 because the service account credentials provided are invalid. To fix this problem, update your 
 storage virtual machine's Active Directory configuration with a valid service account.`**

To resolve this issue, use the procedure described in [Updating existing SVM Active Directory configurations using the AWS Management Console, AWS CLI, and API](update-svm-ad-config.md "update-svm-ad-config.md") to update the SVM's service account credentials. When
entering the service account user name, be sure to include only the user name (for example,
`ServiceAcct`), and don't include any domain prefix (for example,
`corp.com\ServiceAcct`) or domain suffix (for example,
`ServiceAcct@corp.com`). Don't use the distinguished name (DN) when entering the
service account user name (for example,
`CN=ServiceAcct,OU=example,DC=corp,DC=com`).

## Amazon FSx can't connect to your Active

Directory domain controllers because of insufficient service account credentials

Joining an SVM to your self-managed Active Directory fails with the following error message:

**`Amazon FSx is unable to establish a connection with your Active Directory domain controller(s). This is due to either unmet port requirements
 for the Active Directory, or the service account provided does not have permission to join the storage virtual machine to the domain
 with the specified organizational unit.`**

To resolve this issue, make sure that you have delegated the required permissions to the service account that you provided.
The service account must be able to create and delete computer objects in the OU in the domain to which you're joining the file system.
The service account also needs, at a minimum, to have permissions to do the following:

- Reset passwords
- Restrict accounts from reading and writing data
- Validated ability to write to the DNS hostname
- Validated ability to write to the service principal name
- Ability to create and delete computer objects
- Validated ability to read and write Account Restrictions

For more information about creating a service account with correct permissions, see
[Active Directory service account requirements](self-manage-prereqs.md#ontap-ad-service-account-prereqs "self-manage-prereqs.md#ontap-ad-service-account-prereqs") and
[Delegating permissions to your Amazon FSx service
account](self-managed-AD-best-practices.md#connect_delegate_privileges "self-managed-AD-best-practices.md#connect_delegate_privileges").

## Amazon FSx can't communicate with your Active

Directory DNS servers or domain controllers

Joining an SVM to your self-managed Active Directory fails with the following error message:

**`Amazon FSx is unable to communicate with your Active Directory. This is because Amazon FSx can't reach the 
 DNS servers provided or domain controllers for your domain. To fix this problem, update your storage virtual machine's
 Active Directory configuration with valid DNS servers and a networking configuration that allows traffic to flow 
 from the storage virtual machine to the domain controller.`**

To resolve this issue, use the following procedure:

1.  If only some of the domain controllers in your Active Directory are reachable, for example due
    to geographical limitations or firewalls, you can add preferred domain controllers. Using this
    option, Amazon FSx attempts to contact the preferred domain controllers. Add preferred domain
    controllers using the [`vserver cifs domain preferred-dc add`](https://docs.netapp.com/us-en/ontap/smb-admin/add-preferred-domain-controllers-task.html "https://docs.netapp.com/us-en/ontap/smb-admin/add-preferred-domain-controllers-task.html") NetApp ONTAP CLI command, as
    follows:
    1. To access the ONTAP CLI, establish an SSH session on the management port of the
       Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
       `management_endpoint_ip` with the IP address of the file system's
       management port.

    ```
    `[~]$` `ssh fsxadmin@`management_endpoint_ip``
    ```

    For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Enter the following command, where:

        * `-vserver vserver_name` specifies the storage virtual machine (SVM) name.
        * `-domain domain_name` specifies the fully qualified Active Directory name (FQDN) of
         the domain to which the specified domain controllers belong.
        * `-preferred-dc IP_address,…​` specifies one or more IP addresses of the preferred domain controllers,
         as a comma-delimited list, in order of preference.

    ```
    `FsxId123456789::>` vserver cifs domain preferred-dc add -vserver vserver_name -domain domain_name -preferred-dc IP_address, …​+
    ```

    The following command adds domain controllers 172.17.102.25 and 172.17.102.24 to the list of preferred domain controllers
    that the SMB server on SVM vs1 uses to manage external access to the cifs.lab.example.com domain.

    ```
    `FsxId123456789::>` vserver cifs domain preferred-dc add -vserver vs1 -domain cifs.lab.example.com -preferred-dc 172.17.102.25,172.17.102.24
    ```

2.  Check to see if your Domain Controller can be resolved with DNS. Use the [`vserver services access-check dns forward-lookup`](https://docs.netapp.com/us-en/ontap-cli-9121/vserver-services-access-check-dns-forward-lookup.html "https://docs.netapp.com/us-en/ontap-cli-9121/vserver-services-access-check-dns-forward-lookup.html") NetApp ONTAP CLI
    command to return the IP address of a hostname based on the look up on the DNS server specified
    or the vserver’s DNS configuration.
    1. To access the ONTAP CLI, establish an SSH session on the management port of the
       Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
       `management_endpoint_ip` with the IP address of the file system's
       management port.

    ```
    `[~]$` `ssh fsxadmin@`management_endpoint_ip``
    ```

    For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Enter the ONTAP CLI advanced mode using the following command.

    ```
    `FsxId123456789::>` set adv
    ```

    3. Enter the following command, where:
       - `-vserver vserver_name` specifies the storage virtual machine (SVM) name.
       - `-hostname host_name` specifies the hostname to look up on the DNS server.
       - `-node node_name​` specifies the name of the node on which the command is executed.
       - `-lookup-type` specifies the type of IP address to be looked up on the DNS server, default is `all`.

    ```
    `FsxId123456789::>` vserver services access-check dns forward-lookup \
    -vserver `vserver_name` -node `node_name` \
    -domains `domain_name` -name-servers `dns_server_ip_address` \
    -hostname `host_name`
    ```

3.  Review the [information you need to have](self-managed-AD-join.md#ad-info-for-svm-join "self-managed-AD-join.md#ad-info-for-svm-join") when joining an SVM to an AD.
4.  Review the [networking requirements](self-manage-prereqs.md#ontap-ad-network-configs "self-manage-prereqs.md#ontap-ad-network-configs") when joining an SVM to an AD.
5.  Use the procedure described in [Network configuration requirements](self-manage-prereqs.md#ontap-ad-network-configs "self-manage-prereqs.md#ontap-ad-network-configs")
    to update your SVM's AD configuration using the correct IP addresses for your AD DNS servers.

## Amazon FSx can't communicate with your Active

Directory because of a invalid Active Directory domain name.

Joining an SVM to your self-managed Active Directory fails with the following error message:

**`Amazon FSx has detected the provided FQDN is invalid. To fix this problem, update your storage virtual machine's 
 Active Directory configuration with an FQDN that adheres to configuration requirements.`**

To resolve this issue, use the following procedure:

1. Review the on-premises Active Directory domain name requirements described in
   [Information needed when joining an SVM to an Active Directory](self-managed-AD-join.md#ad-info-for-svm-join "self-managed-AD-join.md#ad-info-for-svm-join") Make sure that the
   AD you are attempting to join meets that requirement.
2. Use the procedure described in [Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API](join-svm-to-ad.md "join-svm-to-ad.md")
   and reattempt joining your SVM to an AD. Be sure to use the correct format for the AD domain's FQDN.

## The service account can't access the administrators group specified in the SVM Active Directory configuration

Joining an SVM to your self-managed Active Directory fails with the following error message:

**`Amazon FSx is unable to apply your Active Directory configuration. This is because the administrators group you provided either 
 doesn't exist or isn't accessible to the service account you provided. To fix this problem, ensure that your networking configuration allows traffic 
 from the SVM to your Active Directory’s domain controller(s) and DNS servers. Then update your SVM’s Active Directory configuration, providing your 
 Active Directory’s DNS servers and, specifying an administrators group in the domain that is accessible to the service account provided.`**

To resolve this issue, do the following:

1. Review the information about [providing a domain group](self-managed-AD-join.md#ad-info-for-svm-join "self-managed-AD-join.md#ad-info-for-svm-join") to perform administrative actions on your SVM. Make sure
   that you are using the correct name of the AD domain administrators group.
2. Use the procedure described in [Joining SVMs to Active Directory using the AWS Management Console, AWS CLI and API](join-svm-to-ad.md "join-svm-to-ad.md") and reattempt joining your SVM to an AD.

## Amazon FSx can't connect to the Active

Directory domain controllers because the organizational unit specified doesn't exist or
isn't accessible

Joining an SVM to your self-managed Active Directory fails with the following error message:

**`Amazon FSx is unable to establish a connection with your Active Directory.
 This is because the organizational unit you specified either doesn't exist or isn't accessible to the service account provided.
 To fix this problem, update your storage virtual machine's Active Directory configuration, specifying an organizational unit 
 to which the service account has permissions to join.`**

To resolve this issue, do the following:

1. Review the [prerequisites for joining an SVM to an AD](self-manage-prereqs.md "self-manage-prereqs.md").
2. Review the [information that you need to have](self-managed-AD-join.md#ad-info-for-svm-join "self-managed-AD-join.md#ad-info-for-svm-join") when joining an SVM to an AD.
3. Reattempt joining the SVM to the AD using [this procedure](join-svm-to-ad.md "join-svm-to-ad.md") with the correct organization unit.
