# Connect to your Windows instance using Fleet Manager

You can use Fleet Manager, a capability of AWS Systems Manager, to connect to Windows instances
using the Remote Desktop Protocol (RDP) and display up to four Windows instances on the
same page in the AWS Management Console. You can connect to the first instance in the Fleet Manager
Remote Desktop directly from the **Instances** page in the Amazon EC2
console. For more information about Fleet Manager, see [Connect to a managed instance
using Remote Desktop](../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md "../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md") in the _AWS Systems Manager User Guide_.

You do not need to specifically allow incoming RDP traffic from your IP address if
you use Fleet Manager to connect. Fleet Manager handles that for you.

###### Prerequisites

Before attempting to connect to an instance using Fleet Manager, you must set
up your environment. For more information, see [Setting up your environment](../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md#rdp-prerequisites "../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md#rdp-prerequisites") in the
_AWS Systems Manager User Guide_.

###### To connect to a Windows instance using Fleet Manager

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation pane, choose **Instances**.
3. Select the instance and then choose **Connect**.
4. On the **RDP client** tab, for **Connection Type**,
   choose **Connect using Fleet Manager**.
5. Choose **Fleet Manager Remote Desktop**. This opens the
   **Fleet Manager Remote Desktop** page in the AWS Systems Manager
   console.
6. Enter your credentials and then choose **Connect**.
7. If the RDP connection is successful, Fleet Manager displays the Windows desktop.
   When you are finished with the session, choose **Actions**,
   **End session**.
   For more information, see [Connecting to a Windows Server managed instance using Remote Desktop](../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md "../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md") in the
   _AWS Systems Manager User Guide_.
