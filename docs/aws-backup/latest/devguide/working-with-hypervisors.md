# Working with hypervisors

After you finish [Creating a gateway](working-with-gateways.md#create-gateway "working-with-gateways.md#create-gateway"), you
can connect it to a hypervisor to enable AWS Backup to work with the virtual machines managed
by that hypervisor. For example, the hypervisor for VMware VMs is VMware vCenter Server.
Ensure your hypervisor is configured with the [necessary permissions for AWS Backup](configure-infrastructure-bgw.md#bgw-vmware-permissions "configure-infrastructure-bgw.md#bgw-vmware-permissions").

## Adding a hypervisor

###### To add a hypervisor:

1. In the left navigation pane, under the **External resources**
   section, choose **Hypervisors**.
2. Choose **Add hypervisor**.
3. In the **Hypervisor settings** section, type in a
   **Hypervisor name**.
4. For **vCenter server host**, use the dropdown menu to select
   either **IP address** or **FQDN** (fully-qualified
   domain name). Type in the corresponding value.
5. To allow AWS Backup to discover the virtual machines on the hypervisor, enter the
   hypervisor’s **Username** and **Password**.
6. Encrypt your password. You can
   [specify this encryption](bgw-hypervisor-encryption-page.md "bgw-hypervisor-encryption-page.md") by selecting a specific
   service-managed KMS key or a customer-managed KMS key using the dropdown menu or
   choose **Create KMS key**. If you do not select a specific key,
   AWS Backup will encrypt your password using a service-owned key.
7. In the **Connecting gateway** section, use the dropdown list to
   specify which Gateway to connect to your hypervisor.
8. Choose **Test gateway connection** to verify your previous
   inputs.
9. _Optionally_, in the **Hypervisor tags** section, you can assign
   tags to the hypervisor by choosing **Add new tag**.
10. _Optional_
    [**VMware tag mapping**](backing-up-vms.md#backup-gateway-vmwaretags "backing-up-vms.md#backup-gateway-vmwaretags"): You can add up to 10 VMware tags you
    currently use on your virtual machines to generate AWS tags.
11. In the **Log group setting** panel, you may choose to integrate with
    [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to maintain logs of your hypervisor (standard
    [CloudWatch Logs pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
    will apply based on usage). Each hypervisor can belong to one log group.
    1. If you have not yet created a log group, select the **Create a new log group**
       radio button. The hypervisor you are editing will be associated with this log group.
    2. If you have previously created a log group for a different hypervisor, you can use that log
       group for this hypervisor. Select **Use an existing log group**.
    3. If you do not want CloudWatch logging, select **Deactivate logging**.

12. Choose **Add hypervisor**, which takes you to its detail
    page.

###### Tip

You can use Amazon CloudWatch Logs (see step 11 above) to obtain information about your hypervisor, including
error monitoring, network connection between the gateway and the hypervisor, and network configuration information.
For information about CloudWatch log groups, see
[Working with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch User Guide_.

## Viewing virtual machines managed by a

hypervisor

###### To view virtual machines on a hypervisor:

1. In the left navigation pane, under the **External resources**
   section, choose **Hypervisors**.
2. In the **Hypervisors** section, choose a hypervisor by its
   **Hypervisor name** to go to its detail page.
3. In the section under **Hypervisor summary**, choose the
   **Virtual machines** tab.
4. In the **Connected virtual machines** section, a list of
   virtual machines populates automatically.

## Viewing gateways connected to a

hypervisor

###### To view gateways connected to the hypervisor:

1. Choose the **Gateways** tab.
2. In the **Connected gateways** section, a list of gateways
   populates automatically.

## Connecting a hypervisor to additional

gateways

Your backup and restore speeds might be limited by the bandwidth of the connection
between your gateway and hypervisor. You can increase these speeds by connecting one or
more additional gateways to your hypervisor. You can do this in the **Connected
gateways** section as follows:

1. Choose **Connect**.
2. Select another gateway using the dropdown menu. Alternatively, choose
   **Create gateway** to create a new gateway.
3. Choose **Connect**.

## Editing a hypervisor configuration

If you do not use the **Test gateway connection** feature, you
might add a hypervisor with an incorrect username or password. In that case, the
hypervisor’s connection status is always `Pending`. Alternatively, you might
rotate the username or password to access your hypervisor. Update this information using
the following procedure:

###### To edit an already-added hypervisor:

1. In the left navigation pane, under the **External resources**
   section, choose **Hypervisors**.
2. In the **Hypervisors** section, choose a hypervisor by its
   **Hypervisor name** to go to its detail page.
3. Choose **Edit**.
4. The top panel is named **Hypervisor settings**.
   1. Under **vCenter server host**, you can also edit the FQDN
      (Fully-Qualified Domain Name) or the IP address.
   2. _Optionally,_ enter the hypervisor’s **Username** and
      **Password**.

5. In the **Log group setting** panel, you may choose to integrate with
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to maintain logs of your hypervisor (standard
   [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
   will apply based on usage). Each hypervisor can belong to one log group.
   1. If you have not yet created a log group, select the **Create a new log group**
      radio button. The hypervisor you are editing will be associated with this log group.
   2. If you have previously created a log group for a different hypervisor, you can use that log
      group for this hypervisor. Select **Use an existing log group**.
   3. If you do not want CloudWatch logging, select **Deactivate logging**.

###### Tip

You can use Amazon CloudWatch Logs (see step 5 above) to obtain information about your hypervisor, including
error monitoring, network connection between the gateway and the hypervisor, and network configuration information.
For information about CloudWatch log groups, see
[Working with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch User Guide_.

To update a hypervisor programmatically, use the CLI command
[update-hypervisor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup-gateway/update-hypervisor.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup-gateway/update-hypervisor.html") and
[UpdateHypervisor](API_BGW_UpdateHypervisor.md "API_BGW_UpdateHypervisor.md") API call.

## Deleting a hypervisor configuration

If you need to remove an already-added hypervisor, remove the hypervisor configuration
and add another. This remove operation applies to the configuration to connect to the
hypervisor. It does not delete the hypervisor.

###### To delete the configuration to connect to an already-added hypervisor:

1. In the left navigation pane, under the **External resources**
   section, choose **Hypervisors**.
2. In the **Hypervisors** section, choose a hypervisor by its
   **Hypervisor name** to go to its detail page.
3. Choose **Remove**, then choose **Remove
   hypervisor**.
4. Optional: replace the removed hypervisor configuration using the procedure for
   [Adding a hypervisor](#add-hypervisor "#add-hypervisor").

## Understanding hypervisor status

The following describes each of the possible hypevisor statuses and, if applicable,
remediation steps. The `ONLINE` status is the normal status of the
hypervisor. A hypervisor should have this status all or most of the time it’s in use for
backup and recovery of VMs managed by the hypervisor.

| Hypervisor statuses | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Meaning and remediation |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `ONLINE`            | You added a hypervisor to AWS Backup, associated with it a gateway, and can<br>connect with that gateway over your network to perform backup and recovery of<br>virtual machines managed by the hypervisor.<br>You can perform [on-demand and scheduled<br>backups](backing-up-vms.md "backing-up-vms.md") of those virtual machines at any time.                                                                                                                                                                                                                                                                                                                                                                            |
| `PENDING`           | You added a hypervisor to AWS Backup but:<br>• It is not associated with any gateway, or<br>• It is associated with one or more gateways, but all those gateways<br>were deleted or are otherwise not active.<br>To change a hypervisor status from `PENDING` to<br>`ONLINE`, [create a gateway](working-with-gateways.md#create-gateway "working-with-gateways.md#create-gateway") and [connect your hypervisor to that gateway](working-with-hypervisors.md#add-more-gateways "working-with-hypervisors.md#add-more-gateways").                                                                                                                                                                                            |
| `OFFLINE`           | You added a hypervisor to AWS Backup and associated it with a gateway, but the<br>gateway cannot connect to the hypervisor over your network.<br>To change a hypervisor status from `OFFLINE` to<br>`ONLINE`, verify the correctness of your [network configuration](configure-infrastructure-bgw.md#bgw-network-configuration "configure-infrastructure-bgw.md#bgw-network-configuration").<br>If the issue persists, verify that your hypervisor’s IP address or<br>fully-qualified domain name is correct. If they are incorrect, [add your hypervisor again using the correct information and test your<br>gateway connection](working-with-hypervisors.md#add-hypervisor "working-with-hypervisors.md#add-hypervisor"). |
| `ERROR`             | You added a hypervisor to AWS Backup and associated it with a gateway, but the<br>gateway cannot communicate with the hypervisor.<br>To change a hypervisor status from `ERROR` to<br>`ONLINE`, verify that hypervisor’s username and password are<br>correct. If they are incorrect, [edit your hypervisor configuration](working-with-hypervisors.md#edit-hypervisor "working-with-hypervisors.md#edit-hypervisor").                                                                                                                                                                                                                                                                                                       |

**Next steps**

To back up virtual machines on your hypervisor, see [Backing up virtual machines](backing-up-vms.md "backing-up-vms.md").
