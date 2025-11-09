# Updating SVM Active Directory configurations using the NetApp CLI

You can use the NetApp ONTAP CLI to join and unjoin your SVM to an Active Directory, and to modify an existing SVM Active Directory configuration.

## Joining an SVM to an Active Directory using the ONTAP CLI

You can join existing SVMs to an Active Directory using the ONTAP CLI, as described in the following procedure.
You can do this even if your SVM is already joined to an Active Directory.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Create a DNS entry for your Active Directory by providing the full directory DNS name (`corp.example.com`) and at least one DNS server IP address.

```
`::>``vserver services name-service dns create -vserver `svm_name` -domains `corp.example.com` -name-servers `dns_ip_1`, `dns_ip_2``
```

To verify the connection to your DNS servers, run the following command. Replace `svm_name` with your own information.

```
`FsxId0ae30e5b7f1a50b6a::>``vserver services name-service dns check -vserver `svm_name``

                              `Name Server
Vserver Name Server Status Status Details
------------- --------------- ------------ --------------------------
svm_name 172.31.14.245 up Response time (msec): 0
svm_name 172.31.25.207 up Response time (msec): 1
2 entries were displayed.`
```

3. To join your SVM to your Active Directory, run the following command. Note that you will
   must specify a `computer_name` that doesn't already exist in your Active
   Directory and provide the directory DNS name for `-domain`. For
   `-OU`, enter the OUs that you want the SVM to join, as well as the full
   DNS name in DC format.

```
`::>``vserver cifs create -vserver svm_name -cifs-server `computer_name` -domain `corp.example.com` -OU `OU=Computers,OU=example,DC=corp,DC=example,DC=com``
```

To verify the status of your Active Directory connection, run the following command:

```
`::>``vserver cifs check -vserver `svm_name``

              `Vserver : svm_name
 Cifs NetBIOS Name : svm_netBIOS_name
 Cifs Status : Running
 Site : Default-First-Site-Name
Node Name DC Server Name DC Server IP Status Status Details
--------------- -------------- --------------- ------ --------------
FsxId0ae30e5b7f1a50b6a-01
 corp.example.com
 172.31.14.245 up Response time (msec): 5
FsxId0ae30e5b7f1a50b6a-02
 corp.example.com
 172.31.14.245 up Response time (msec): 20
2 entries were displayed.`
```

4. If you can't access shares after this join, determine whether the account you’re using
   to access the share has permissions. For example, if you're using the default
   `Admin` account (a delegated administrator) with an AWS managed Active Directory, you
   will must run the following command in ONTAP. The `netbios_domain`
   corresponds with your Active Directory’s domain name (for
   `corp.example.com`, the `netbios_domain` used here is
   `example`).

```
`FsxId0123456789a::>``vserver cifs users-and-groups local-group add-members -vserver svm_name -group-name BUILTIN\Administrators -member-names netbios_domain\admin`
```

## Modify an Active Directory configuration using the ONTAP CLI

You can use the ONTAP CLI to modify an existing Active Directory configuration. 

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Run the following command to temporarily bring down the SVM's CIFS server: 

```
`FsxId0123456789a::>``vserver cifs modify -vserver `svm_name` -status-admin down`
```

3. If you need to modify the DNS entries of your Active Directory, run the following command: 

```
`::>``vserver services name-service dns modify -vserver `svm_name` -domains `corp.example.com` -name-servers `dns_ip_1`,`dns_ip_2``
```

You can validate the connection status to your Active Directory's DNS servers using the `vserver services name-service dns check -vserver svm_name` command.

```
`::>``vserver services name-service dns check -vserver `svm_name``
                              `Name Server
Vserver Name Server Status Status Details
------------- --------------- ------------ --------------------------
svmciad dns_ip_1 up Response time (msec): 1
svmciad dns_ip_2 up Response time (msec): 1
2 entries were displayed.`
```

4.  If you need to modify the Active Directory configuration itself, you can change existing fields by
    using the following command, replacing:

        * `computer_name`, if you want to modify the NetBIOS (machine account) name of the SVM.
        * `domain_name`, if you want to modify the name of the domain.
         This should correspond with the DNS domain entry noted in Step 3 of this section
         (`corp.example.com`).
        * `organizational_unit`, if you want to modify the OU
         (`OU=Computers,OU=example,DC=corp,DC=example,DC=com`).

    You will need to reenter the Active Directory credentials that you used to join this device to the
    Active Directory.

```
`::>``vserver cifs modify -vserver `svm_name` -cifs-server computer_name -domain `domain_name` -OU `organizational_unit``
```

You can verify the connection status of your Active Directory connection using the `vserver cifs check -vserver `svm_name`` command. 5. When you finish modifying your Active Directory and DNS configuration, bring the CIFS server back up by
running the following command:

```
`::>``vserver cifs modify -vserver `svm_name` -status-admin up`
```

## Unjoin an Active Directory from your SVM using the NetApp ONTAP CLI

The NetApp ONTAP CLI can also be used to unjoin your SVM from an Active Directory by following the steps below:

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Delete the CIFS server that unjoined your device from the Active Directory by running the following
command. For ONTAP to delete the machine account for your SVM, provide the credentials that
you originally used to join the SVM to the Active Directory.  

```
`FsxId0123456789a::>``vserver cifs modify -vserver `svm_name` -status-admin down`
```

3. If you need to modify the DNS entries of your Active Directory, run the following command: 

```
`FsxId0123456789a::``vserver cifs delete -vserver `svm_name``

`In order to delete an Active Directory machine account for the CIFS server, you must supply the name and password of a Windows account with
sufficient privileges to remove computers from the "CORP.ADEXAMPLE.COM" domain.

Enter the user name: `user_name`

Enter the password:

Warning: There are one or more shares associated with this CIFS server
 Do you really want to delete this CIFS server and all its shares? {y|n}: `y``
```

4. Delete the DNS servers for your Active Directory by running the following command:

```
`::``vserver services name-service dns delete -vserver `svm_name``
```

If you see a warning like the following—indicating that `dns` should
be removed as an `ns-switch`—and you don't plan to rejoin this
device to an Active Directory, you can remove the `ns-switch` entries.

```
`Warning: "DNS" is present as one of the sources in one or more ns-switch databases but no valid DNS configuration was found for Vserver
 "svm_name". Remove "DNS" from ns-switch using the "vserver services name-service ns-switch" command. Configuring "DNS" as a source
 in the ns-switch setting when there is no valid configuration can cause protocol access issues.`
```

5. (Optional) Remove the `ns-switch` entries for `dns` by running the
   following command. Verify the source order, then remove the `dns` entry for
   the `hosts` database by modifying the `sources` so that they
   contain only the other sources listed. In this example, the only other source is
   `files`.

```
`::>``vserver services name-service ns-switch show -vserver `svm_name` -database hosts`

                     `Vserver: svm_name
Name Service Switch Database: hosts
 Name Service Source Order: files, dns`
```

```
`::>``vserver services name-service ns-switch modify -vserver `svm_name` -database hosts -sources files`
```

6. (Optional) Remove the `dns` entry by modifying the `sources` for
   the database host to include only `files`.

```
`::>``vserver services name-service ns-switch modify -vserver svm_name -database hosts -sources files`
```
