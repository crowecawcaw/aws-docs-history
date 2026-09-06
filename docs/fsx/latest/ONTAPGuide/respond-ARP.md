

# Responding to Autonomous Ransomware Protection alerts
<a name="respond-ARP"></a>

The following procedures explain how to use the ONTAP CLI to view Autonomous Ransomware Protection (ARP) alerts, generate attack reports, and take action on reports. For more information about how ARP detects and responds to attacks, see [What ARP looks for](ARP.md#ARP-detects) and [How to respond to a suspected attack with ARP](ARP.md#suspected-attack-ARP).

## Viewing ARP alerts
<a name="view-ARP-alert"></a>

**To view an ARP alert on a volume using the ONTAP CLI**
+ Run the following command. Replace {{svm\_name}} and {{vol\_name}} with your own information. 

  ```
  security anti-ransomware volume show -vserver {{svm_name}} -volume {{vol_name}}
  ```

  After running the command, you'll see output similar to the following example:

  ```
  Vserver Name: fsx
  Volume Name: vol1
  State: enabled
  Attack Probability: moderate
  Attack Timeline: 9/14/2021 01:03:23
  Number of Attacks: 1
  ```

  For more information about this command, see [`security anti-ransomware volume show`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-show.html#description) in the NetApp documentation center.

## Generating ARP reports
<a name="generate-ARP-report"></a>

**To generate ARP reports using the ONTAP CLI**
+ Run the following command. Replace {{vol\_name}} and {{/file\_location/}} with your own information. After you generate the report, you can view it on a client system. 

  ```
  security anti-ransomware volume attack generate-report -volume {{vol_name}} -dest-path {{/file_location/}}
  ```

  For more information about this command, see [`security anti-ransomware volume attack generate-report`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-attack-generate-report.html#description) in the NetApp documentation center.

## Taking action on ARP reports
<a name="take-action-ARP"></a>

**To take action on a false positive attack from an ARP report using the ONTAP CLI**
+ Run the following command. Replace {{svm\_name}}, {{vol\_name}}, and {{[extension identifiers]}} with your own information. 

  ```
  security anti-ransomware volume attack clear-suspect -vserver {{svm_name}} -volume {{vol_name}} {{[extension identifiers]}} -false-positive true
  ```

  For more information about this command, see [`security anti-ransomware volume attack clear-suspect`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-attack-clear-suspect.html#description) in the NetApp documentation center.
**Note**  
When you mark an alert as a false positive, it updates the ransomware profile. After doing so, you won't receive an alert about that particular scenario again.

**To take action on a potential attack from an ARP report using the ONTAP CLI**
+ Run the following command. Replace {{svm\_name}}, {{vol\_name}}, and {{[extension identifiers]}} with your own information. 

  ```
  security anti-ransomware volume attack clear-suspect -vserver {{svm_name}} -volume {{vol_name}} {{[extension identifiers]}} -false-positive false
  ```

  For more information about this command, see [`security anti-ransomware volume attack clear-suspect`](https://docs.netapp.com/us-en/ontap-cli/security-anti-ransomware-volume-attack-clear-suspect.html#description) in the NetApp documentation center.