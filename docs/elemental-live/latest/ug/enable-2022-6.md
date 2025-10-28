# Get ready: Reserve cores for SMPTE 2022-6

Before you can run an event that has SMPTE 2022-6 inputs, you must
reserve cores on the appliance NIC. When you reserve these cores, Elemental Live
uses them only for processing SMPTE 2022-6 and/or SMPTE 2110.

###### Important

Ensure that no events are running before you follow these steps.

###### To enable an interface for SMPTE 2022-6

1. Find out which Ethernet interfaces on the appliance apply to your NIC. For
   example, eth4 and eth5.
2. Stop all events that are currently running on the appliance.
3. In the Elemental Live web interface, go to **Settings**, and
   select **Network Devices**.
4. Choose the **edit** icon (pencil) next to the device
   that you want to enable. For L800 series appliances and bare metal appliances, this
   can only be enabled for 25 GbE NICs.
5. Select the **SMPTE 2110 and SMPTE 2022-6 Enabled** check box, and
   then choose **Save**.
6. Stop and restart the service for your changes to take effect. You can do this in
   the web interface or in the command line interface (CLI).
   - In the web interface, go to the **Settings** tab, select
     **Stop Service** and then select **Start
     Service**.

   OR
   - In the CLI, run `sudo service elemental_se restart`
