# Removing gateway software from your

hardware appliance

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

If you no longer need a specific Storage Gateway that you have deployed on a hardware
appliance, you can remove the gateway software from the hardware appliance. After you
remove the gateway software, you can choose to deploy a new gateway in its place, or
delete the hardware appliance itself from the Storage Gateway console. To remove gateway
software from your hardware appliance, use the following procedure.

###### To remove a gateway from a hardware appliance

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Hardware** from the navigation pane on the left side
   of the console page, and then choose the **Hardware appliance
   name** for the appliance from which you want to remove gateway
   software.
3. From the **Actions** drop down menu, choose **Remove
   gateway**.

The confirmation dialog box appears. 4. Verify that you want to remove the gateway software from the specified
hardware appliance, and then type the word `remove` in the
confirmation box. 5. Choose **Remove** to permanently remove the gateway
software.

###### Note

After you remove the gateway software, you can't undo the action. For
certain gateway types, you can lose data on deletion, particularly cached
data. For more information on deleting a gateway, see [Deleting your gateway and removing associated
resources](deleting-gateway-common.md "deleting-gateway-common.md").
Removing the gateway doesn't delete the hardware appliance from the console. The
hardware appliance remains for future gateway deployments.
