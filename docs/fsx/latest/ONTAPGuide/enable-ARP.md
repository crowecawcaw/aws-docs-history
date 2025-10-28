# Enabling Autonomous Ransomware Protection

The following procedures explain how to use the ONTAP CLI to enable Autonomous Ransomware Protection (ARP) active mode
as well as how to verify that ARP is enabled. For more information about ARP, see [How ARP works](ARP.md#how-ARP-works "ARP.md#how-ARP-works").

###### To enable ARP in active mode on an existing volume using the ONTAP CLI

- Run the following command. Replace `vol_name` and `svm_name` with your
  own information.

```
`security anti-ransomware volume enable -volume `vol_name` -vserver `svm_name``
```

For more information about this command, see [`security anti-ransomware volume enable`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-enable.html#description "https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-enable.html#description")
in the NetApp documentation center.

###### To enable ARP by default on an existing SVM using the ONTAP CLI

- Run the following command. Replace `svm_name` with your own information.

```
`vserver modify -vserver `svm_name` -anti-ransomware-default-volume-state dry-run`
```

For more information about this command, see [`vserver modify`](https://docs.netapp.com/us-en/ontap-cli/vserver-modify.html#description "https://docs.netapp.com/us-en/ontap-cli/vserver-modify.html#description")
in the NetApp documentation center.

###### To verify the status of ARP using the ONTAP CLI

- Run the following command.

```
`security anti-ransomware volume show`
```

For more information about this command, see [`security anti-ransomware volume show`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-show.html#description "https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-show.html#description")
in the NetApp documentation center.
You can temporarily suspend (and then resume) ARP if you're anticipating heavy workload events. For more information, see
[Pause ONTAP Autonomous Ransomware Protection to exclude workload events from analysis](https://docs.netapp.com/us-en/ontap/anti-ransomware/pause-task.html "https://docs.netapp.com/us-en/ontap/anti-ransomware/pause-task.html") in
the NetApp Documentation Center.
