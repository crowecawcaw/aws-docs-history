

# Enabling Autonomous Ransomware Protection
<a name="enable-ARP"></a>

The following procedures explain how to use the ONTAP CLI to enable Autonomous Ransomware Protection (ARP) active mode as well as how to verify that ARP is enabled. For more information about ARP, see [How ARP works](ARP.md#how-ARP-works).

## Enabling ARP in active mode
<a name="enable-active-mode-ARP"></a>

**To enable ARP in active mode on an existing volume using the ONTAP CLI**
+ Run the following command. Replace {{vol\_name}} and {{svm\_name}} with your own information. 

  ```
  security anti-ransomware volume enable -volume {{vol_name}} -vserver {{svm_name}}
  ```

  For more information about this command, see [`security anti-ransomware volume enable`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-enable.html#description) in the NetApp documentation center.

## Enabling ARP by default at the SVM level
<a name="enable-ARP-default"></a>

**To enable ARP by default on an existing SVM using the ONTAP CLI**
+ Run the following command. Replace {{svm\_name}} with your own information. 

  ```
  vserver modify -vserver {{svm_name}} -anti-ransomware-default-volume-state dry-run
  ```

  For more information about this command, see [`vserver modify`](https://docs.netapp.com/us-en/ontap-cli/vserver-modify.html#description) in the NetApp documentation center.

## Verifying ARP's status
<a name="verify-ARP-status"></a>

**To verify the status of ARP using the ONTAP CLI**
+ Run the following command. 

  ```
  security anti-ransomware volume show
  ```

  For more information about this command, see [`security anti-ransomware volume show`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-show.html#description) in the NetApp documentation center.

You can temporarily suspend (and then resume) ARP if you're anticipating heavy workload events. For more information, see [Pause ONTAP Autonomous Ransomware Protection to exclude workload events from analysis](https://docs.netapp.com/us-en/ontap/anti-ransomware/pause-task.html) in the NetApp Documentation Center.