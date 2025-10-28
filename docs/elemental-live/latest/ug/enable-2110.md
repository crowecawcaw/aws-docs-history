# Setup: Reserve cores for SMPTE 2110

Before you can run an event using SMPTE 2110, you must reserve cores on the appliance
NIC. When you reserve these cores, AWS Elemental Live uses them only for processing SMPTE 2110
and/or SMPTE 2022-6.

The setting to reserve cores applies to the appliance. Therefore you need to reserve the
cores only once, not every time you set up a new event that uses SMPTE 2110 or SMPTE
2022-6.

###### Important

Make sure you reserve the cores only when you plan to create events that have SMPTE
2110 inputs or outputs and/or SMPTE 2022-6 inputs.

After you reserve the cores, AWS Elemental Live uses these cores only for processing SMPTE
2110 and/or SMPTE 2022-6. Other processing won't be able to use these cores.

###### To reserve cores

1. Find out which Ethernet interfaces on the appliance apply to your NIC. For
   example, eth4 and eth5.
2. Stop all events that are currently running on the appliance.
3. In the Elemental Live web interface, choose **Settings**. (Don't choose
   **Input Devices** or **Routers** from the
   submenu).
4. On the **Settings** page, choose the **Network**
   tab, then choose the **Network Devices** tab.
5. Choose the **edit** icon (pencil) next to the
   Ethernet interface that you identified, and select the **SMPTE 2110 and SMPTE
   2022-6 Enabled** check box.
6. Repeat for the other Ethernet interface, if applicable.
7. Choose **Save**.
8. Stop and restart the service for your changes to take effect. You can do this in
   the web interface or in the command line interface (CLI).
   - In the web interface, go to the **Settings** tab, select
     **Stop Service** and then **Start
     Service**.

   OR
   - In the CLI, run `sudo service elemental_se restart`
