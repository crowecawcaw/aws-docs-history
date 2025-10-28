This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step B: Assign the Devices

Next, add the Ethernet devices to the bond that you created in [Step A: Create the Bond](config-wrkr-cf-cg-ethernet-bond-create.md "config-wrkr-cf-cg-ethernet-bond-create.md").

###### To add devices to the bond

1. On the **Network Devices** page of the AWS Elemental Server web
   interface, locate the devices that you're adding to the bond.
2. For each device, choose **Edit Network Device** (pencil icon) and
   make the following changes:
   - Make sure that **Management** isn't selected. Whether the
     devices are management interfaces or not is defined in the bond and not in the
     individual devices.
   - In **Master Device**, select the bond that these devices are to
     be assigned to.

3. Choose **Save** and **Apply Changes**.
