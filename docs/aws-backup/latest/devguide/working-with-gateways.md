# Working with gateways

To back up and restore your virtual machines (VMs) using AWS Backup, you must first install
a Backup gateway. A gateway is software in the form of an OVF (Open Virtualization Format)
template that connects Amazon Web Services Backup to your hypervisor, allowing it to automatically
detect your virtual machines, and enables you to back up and restore them.

A single gateway can run up to 4 backup or restore jobs at once. To run more than 4
jobs at once, create more gateways and associate them with your hypervisor.

## Creating a gateway

You can create a backup gateway using two approaches:

- **Console method (standard)**: Creates IPv4-only gateways through the AWS Backup console with automatic activation
- **Manual method**: Supports both IPv4 and IPv6 by obtaining activation keys and using AWS CLI commands

Both methods require downloading and deploying the OVF template first (see [Download VM software](vm-backups.md#download-vm-software "vm-backups.md#download-vm-software")).

### Console method (IPv4 only)

Use this method for standard IPv4 gateway creation through the AWS Backup console with automatic activation.

###### To create a gateway:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, under the **External resources**
   section, choose **Gateways**.
3. Choose **Create gateway**.
4. In the **Set up gateway** section, follow these instructions to
   download and deploy the OVF template.

###### Connecting the hypervisor

Gateways connect AWS Backup to your hypervisor so you can create and
store backups of your virtual machines. To set up your gateway on
VMware ESXi, download the [OVF template](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-AE61948B-C2EE-436E-BAFB-3C7209088552.html "https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-AE61948B-C2EE-436E-BAFB-3C7209088552.html"). The download
may take about 10 minutes.

After it is complete, proceed with the following steps:

1. Connect to your virtual machine hypervisor using VMware vSphere.
2. Right-click a parent object of a virtual machine and select
   _Deploy OVF Template._

![The Deploy OVF Template menu item.](images/gateway-user-deploy-ovf-template-20.png) 3. Choose **Local file**, and upload
the **aws-appliance-latest.ova** file you downloaded.

![The Local file option on the Select an OVF template panel.](images/gateway-user-select-ovf-template-50.png) 4. Follow the deployment wizard steps to deploy it. On the
**Select storage** page, select virtual disk format
**Thick Provision Lazy Zeroed**.

![The Thick Provision Lazy Zeroed option on the Select storage panel.](images/gateway-user-thick-provision-lazy-70.png) 5. After deploying the OVF, right-click the gateway and choose
**Edit Settings**.

![The Edit Settings menu item.](images/gateway-user-edit-settings-30.png)

    1. Under **VM Options**, go to **VM Tools**.
    2. Ensure that for **Synchronize Time with Host**,
     **Synchronize at start up and resume** is selected.



    ![The Synchronize at startup and resume VM option.](images/gateway-user-synchronize-time-60.png)

6. Turn on the virtual machine by selecting “Power On” from the **Actions** menu.

![The Power On menu item.](images/gateway-user-power-on-vm-40.png) 7. Copy the IP address from the VM summary and enter it below.

![The IP Addresses field on the Summary page.](images/gateway-user-copy-ip-address-10.png)

Once the VMWare software is downloaded, complete the following steps:

1. In the **Gateway connection** section, type in the **IP
   address** of the gateway.
   1. To find this IP address, go to the vSphere Client.
   2. Select your gateway under the **Summary** tab.
   3. Copy the **IP address** and paste it in the AWS Backup console
      text bar.

2. In the **Gateway settings** section,
   1. Type in a **Gateway name**.
   2. Verify the AWS Region.
   3. Choose whether the endpoint is publicly accessible or hosted with your virtual private cloud (VPC).
   4. Depending on the endpoint chosen, enter the VPC endpoint DNS Name.

   For more information, see [Create
   a VPC endpoint](backup-network.md#backup-privatelink "backup-network.md#backup-privatelink").

3. _[Optional]_ In the **Gateway tags** section, you can assign tags
   by inputting the **key** and _optional_ **value**.
   To add more than one tag, click **Add another tag**.
4. To complete the process, click **Create gateway**, which takes you to the gateway
   detail page.

### Manual gateway creation (IPv4 and IPv6)

For IPv6 support, create gateways manually using activation keys. IPv6 support requires gateway appliance version 2.x+ and additional firewall configuration on [dual-stack endpoints](configure-infrastructure-bgw.md#bgw-firewall-configuration "configure-infrastructure-bgw.md#bgw-firewall-configuration").

###### Important

**IPv6 hypervisor requirement:** If your gateway is activated through IPv6, you **must** create a hypervisor with an IPv6 address. For example, use `2607:fda8:1001:210::252` instead of `10.0.0.252`. If you associate an IPv6 gateway with an IPv4 hypervisor, backup and restore jobs will likely fail.

#### Getting an activation key

To receive an activation key for your gateway, make a web request to the gateway virtual machine (VM) or use the gateway local console. The gateway VM returns a response that contains the activation key, which is then passed as one of the parameters for the `CreateGateway` API to specify the configuration of your gateway.

###### Tip

Gateway activation keys expire in 30 minutes if unused.

**Getting an activation key using web request**

The following examples show you how to get an activation key using HTTP request. You can either use a web browser or Linux curl or equivalent command using the following URLs.

###### Note

Replace the highlighted variables with actual values for your gateway. Acceptable values
are as follows:

- `gateway_ip_address` - The IPv4 address of your gateway,
  for example `172.31.29.201`
- `region_code` - The Region where you want to activate your
  gateway. See [Regional endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in
  the _AWS General Reference Guide_. If this parameter is not
  specified, or if the value provided is misspelled or doesn't match a valid region, the
  command will default to the `us-east-1` region.

IPv4:

```
curl "http://`gateway_ip_address`/?activationRegion=`region_code`&gatewayType=BACKUP_VM&endpointType=DUALSTACK&ipVersion=ipv4&no_redirect"
```

IPv6:

```
curl "http://`gateway_ip_address`/?activationRegion=`region_code`&gatewayType=BACKUP_VM&endpointType=DUALSTACK&ipVersion=ipv6&no_redirect"
```

###### Getting an activation key using local console

The following examples show you how to get an activation key using gateway host's local console

1. Log in to your virtual machine console.
2. From the **AWS Appliance Activation - Configuration** main menu, select `0` to choose **Get activation key**
3. Select `2` **Backup Gateway** for gateway family option
4. Enter the AWS Region where you want to activate your gateway
5. For network type, enter `1` for Public or `2` for VPC endpoint
6. For endpoint type, enter `1` for standard endpoint or `2` for dual-stack endpoint
   1. For dual-stack endpoint, select `1` for IPv4 or `2` for IPv6

7. Activation key will be populated automatically

#### Creating the gateway

Use the AWS CLI to create the gateway after obtaining an activation key:

1. Obtain activation key using curl commands or local console method
2. Create gateway using AWS CLI, for more information, see [CreateGateway](API_BGW_CreateGateway.md "API_BGW_CreateGateway.md") in
   the _Backup gateway API Reference_.

```
aws backup-gateway create-gateway \
                    --region `region_code` \
                    --activation-key `activation_key` \
                    --gateway-display-name `gateway_name` \
                    --gateway-type BACKUP_VM
```

3. Verify gateway appears in AWS Backup console under **External Resources** → **Gateways**

## Editing or deleting a gateway

###### To edit or delete a gateway:

1. In the left navigation pane, under the **External resources**
   section, choose **Gateways**.
2. In the **Gateways** section, choose a gateway by its
   **Gateway name**.
3. To edit the gateway name, choose **Edit**.
4. To delete the gateway, choose **Delete**, then choose
   **Delete gateway**.

You cannot reactivate a deleted gateway. If you want to connect to the
hypervisor again, follow the procedure in [Creating a gateway](#create-gateway "#create-gateway") . 5. To connect to a hypervisor, in the **Connected hypervisor**
section, choose **Connect**.

Each gateway connects to a single hypervisor. However, you can connect multiple
gateways to the same hypervisor to increase the bandwidth between them beyond that
of the first gateway. 6. To assign, edit, or manage tags, in the **Tags** section,
choose **Manage tags**.

## Backup gateway Bandwidth Throttling

###### Note

This feature will be available on new gateways deployed after
December 15, 2022. For existing gateways, this new capability will be available through
an automatic software update on or before January 30, 2023. To update the gateway
to the latest version manually, use AWS CLI command
[`UpdateGatewaySoftwareNow`](API_BGW_UpdateGatewaySoftwareNow.md "API_BGW_UpdateGatewaySoftwareNow.md").

You can limit the upload throughput from your gateway to AWS Backup to control the
amount of network bandwidth the gateway uses. By default, an activated gateway has no
rate limits.

You can configure a bandwidth rate-limit schedule using the AWS Backup Console or using
API through the AWS CLI
([`PutBandwidthRateLimitSchedule`](API_BGW_PutBandwidthRateLimitSchedule.md "API_BGW_PutBandwidthRateLimitSchedule.md")). When you use a bandwidth rate
limit schedule, you can configure limits to change automatically throughout the day or
week.

Bandwidth rate limiting works by balancing the throughput of all data being uploaded,
averaged over each second. While it is possible for uploads to cross the bandwidth rate
limit briefly for any given micro- or millisecond, this does not typically result in large
spikes over longer periods of time.

You can add up to a maximum of 20 intervals. The maximum value for the upload rate
is 8,000,000 Mbps.

### View and edit the bandwidth rate-limit schedule for your gateway using

the AWS Backup console.

This section describes how to view and edit the bandwidth rate limit schedule for
your gateway.

###### To view and edit the bandwidth rate limit schedule

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, choose **Gateways**. In the
   Gateways pane, gateways are displayed by name. Click the radio button adjacent to
   the gateway name you want to manage.
3. Once you select a radio button, the drop-down menu
   **Action** is available to click. Click **Actions**,
   then click **Edit bandwidth rate limit schedule**. The current schedule
   is displayed. By default, a new or unedited gateway has no defined bandwidth rate limits.

###### Note

You can also click **Manage schedule** in the gateway details page to navigate
to the Edit bandwidth page. 4. _(Optional)_ Choose **Add interval** to add
a new configurable interval to the schedule. For each interval, input the following
information:

    1. **Days of week** — Select the recurring day
     or days on which you want the interval to apply. When chosen, the days will
     display below the drop-down menu. You can remove them by clicking the
     **X** next to the day.
    2. **Start time** — Enter the start time for the
     bandwidth interval, using the *HH:MM* 24-hour format. Time is
     rendered in Universal Coordinated Time (UTC).


    Note: Your bandwidth-rate-limit interval begins at the start of the specified minute.
    3. **End time** — Enter the end time for the bandwidth
     interval, using the *HH:MM* 24-hour format. Time is rendered in
     Universal Coordinated Time (UTC).


    ###### Important

    The bandwidth-rate-limit interval ends at the end of the minute specified.
     To schedule an interval that ends at the end of an hour, enter `59`.
     To schedule consecutive continuous intervals, transitioning at the start of the hour,
     with no interruption between the intervals, enter `59` for the end minute of
     the first interval. Enter `00` for the start minute of the succeeding interval.
    4. **Upload rate** — Enter the upload rate limit,
     in megabits per second (Mbps). The minimum value is 102 megabytes per second
     (Mbps).

5. _(Optional)_ Repeat the previous step as desired until
   your bandwidth rate-limit schedule is complete. If you need to delete an interval
   from your schedule, choose **Remove**.

###### Important

Bandwidth rate-limit intervals cannot overlap. The start time of an
interval must occur after the end time of a preceding interval and before the start
time of a following interval; its end time must occur before the start time of the
following interval. 6. When you are finished, click the **Save changes** button.

### View and edit the bandwidth rate-limit schedule for your gateway using

AWS CLI.

The
[`GetBandwidthRateLimitSchedule`](API_BGW_GetBandwidthRateLimitSchedule.md "API_BGW_GetBandwidthRateLimitSchedule.md") action can be used to view the
bandwidth throttle schedule for a specified gateway. If there is no schedule set, the
schedule will be an empty list of intervals. Here is an example using the AWS CLI to fetch
the bandwidth schedule of a gateway:

```
aws backup-gateway get-bandwidth-rate-limit-schedule --gateway-arn "arn:aws:backup-gateway:`region`:`account-id`:gateway/bgw-`gw id`"
```

To edit a gateway’s bandwidth throttle schedule, you can use the
[`PutBandwidthRateLimitSchedule`](API_BGW_PutBandwidthRateLimitSchedule.md "API_BGW_PutBandwidthRateLimitSchedule.md") action. Note
that you can only update a gateway’s schedule as a whole, rather than modifying,
adding, or removing individual intervals. Calling this action will overwrite the
gateway’s previous bandwidth throttle schedule.

```
aws backup-gateway put-bandwidth-rate-limit-schedule --gateway-arn "arn:aws:backup-gateway:`region`:`account-id`:gateway/`gw-id`" --bandwidth-rate-limit-intervals ...
```
