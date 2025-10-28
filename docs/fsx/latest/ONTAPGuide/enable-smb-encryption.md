# Enabling SMB encryption of data in transit

By default, when you create an SVM, SMB encryption is turned off. You can either enable
SMB encryption required on individual shares, or on an SVM, which turns it on for all shares
on that SVM.

###### Note

When SMB encryption required is enabled on an SVM or share, SMB clients that do
not support encryption cannot connect to that SVM or share.

###### To require SMB encryption for incoming SMB traffic on an SVM

Use the following procedure to require SMB encryption on a SVM using the NetApp ONTAP CLI.

1. To connect to the SVM management endpoint with SSH, use user name `vsadmin`
   and the vsadmin password that you set when you created the SVM. If you did not set a vsadmin
   password, use user name `fsxadmin` and the fsxadmin password. You can SSH into the
   SVM from a client that is in the same VPC as the file system, using the management endpoint IP
   address or DNS name.

```
ssh vsadmin@`svm-management-endpoint-ip-address`
```

The command with sample values:

```
ssh vsadmin@198.51.100.10
```

The SSH command using the management endpoint DNS name:

```
ssh vsadmin@`svm-management-endpoint-dns-name`
```

The SSH command using a sample DNS name:

```
ssh vsadmin@management.svm-`abcdef01234567892`fs-`08fc3405e03933af0`.fsx.`us-east-2`.aws.com
```

```
`Password:` ``vsadmin-password``
`This is your first recorded login.
FsxIdabcdef01234567892::>`
```

2. Use the [`vserver cifs security modify`](https://docs.netapp.com/us-en/ontap-cli-9131/vserver-cifs-security-modify.html "https://docs.netapp.com/us-en/ontap-cli-9131/vserver-cifs-security-modify.html")
   NetApp ONTAP CLI command to require SMB encryption for incoming SMB traffic to the SVM.

```
`vserver cifs security modify -vserver `vserver_name` -is-smb-encryption-required true`
```

3. To stop requiring SMB encryption for incoming SMB traffic, use the following command.

```
`vserver cifs security modify -vserver `vserver_name` -is-smb-encryption-required false`
```

4. To see the current `is-smb-encryption-required` setting on an SVM, use the
   [`vserver cifs security show`](https://docs.netapp.com/us-en/ontap-cli-9131/vserver-cifs-security-show.html "https://docs.netapp.com/us-en/ontap-cli-9131/vserver-cifs-security-show.html")
   NetApp ONTAP CLI command:

```
`vserver cifs security show -vserver `vs1` -fields is-smb-encryption-required`

`vserver is-smb-encryption-required
-------- -------------------------
vs1 true`
```

For more information about managing SMB encryption on an SVM, see
[Configuring required SMB encryption on SMB servers for data transfers over SMB](https://docs.netapp.com/us-en/ontap/smb-admin/configure-required-encryption-concept.html "https://docs.netapp.com/us-en/ontap/smb-admin/configure-required-encryption-concept.html") in the NetApp ONTAP Documentation Center.

###### To enable SMB encryption on a volume

Use the following procedure to enable SMB encryption on a share using the NetApp ONTAP CLI.

1. Establish a secure shell (SSH) connection to the SVM's management endpoint as described in
   [Managing SVMs with the ONTAP CLI](managing-resources-ontap-apps.md#vsadmin-ontap-cli "managing-resources-ontap-apps.md#vsadmin-ontap-cli").
2. Use the following NetApp ONTAP CLI command to create a new SMB share and require SMB encryption when accessing this share.

```
`vserver cifs share create -vserver `vserver_name` -share-name `share_name` -path `share_path` -share-properties encrypt-data`
```

For more information, see [`vserver cifs share create`](https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__create.html "https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__create.html") in the NetApp ONTAP CLI Command man pages. 3. To require SMB encryption on an existing SMB share, use the following command.

```
`vserver cifs share properties add -vserver `vserver_name` -share-name `share_name` -share-properties encrypt-data`
```

For more information, see [`vserver cifs share create`](https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__properties__add.html "https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__properties__add.html") in the NetApp ONTAP CLI Command man pages. 4. To turn off SMB encryption on an existing SMB share, use the following command.

```
`vserver cifs share properties remove -vserver `vserver_name` -share-name `share_name` -share-properties encrypt-data`
```

For more information, see [`vserver cifs share properties remove`](https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__properties__remove.html "https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__properties__remove.html") in the NetApp ONTAP CLI Command man pages. 5. To see the current `is-smb-encryption-required` setting on an SMB share, use the following NetApp ONTAP CLI command:

```
`vserver cifs share properties show -vserver `vserver_name` -share-name `share_name` -fields share-properties`
```

If one of the properties returned by the command is the `encrypt-data` property,
then that property specifies that SMB encryption must be used when accessing this share.

For more information, see [`vserver cifs share properties show`](https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__properties__show.html "https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/vserver__cifs__share__properties__show.html") in the NetApp ONTAP CLI Command man pages.
