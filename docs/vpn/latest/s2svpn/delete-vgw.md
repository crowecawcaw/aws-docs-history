# Detach and delete a virtual private gateway in AWS Site-to-Site VPN

If you no longer require a virtual private gateway for your VPC, you can detach it
from the VPC.

###### To detach a virtual private gateway using the console

1. In the navigation pane, choose **Virtual private gateways**.
2. Select the virtual private gateway and choose **Actions**, **Detach
   from VPC**.
3. Choose **Detach virtual private gateway**.
   If you no longer require a detached virtual private gateway, you can delete it. You
   can't delete a virtual private gateway that's still attached to a VPC. After you delete
   your virtual private gateway, it remains visible for a short while with a state of
   `deleted`, and then the entry is automatically removed.

###### To delete a virtual private gateway using the console

1. In the navigation pane, choose **Virtual private gateways**.
2. Select the virtual private gateway and choose **Actions**, **Delete
   virtual private gateway**.
3. When prompted for confirmation, enter `delete` and then choose
   **Delete**.

###### To detach a virtual private gateway using the command line or API

- [DetachVpnGateway](../../../AWSEC2/latest/APIReference/API_DetachVpnGateway.md "../../../AWSEC2/latest/APIReference/API_DetachVpnGateway.md") (Amazon EC2 Query API)
- [detach-vpn-gateway](../../../cli/latest/reference/ec2/detach-vpn-gateway.md "../../../cli/latest/reference/ec2/detach-vpn-gateway.md") (AWS CLI)
- [Dismount-EC2VpnGateway](../../../powershell/latest/reference/items/Dismount-EC2VpnGateway.md "../../../powershell/latest/reference/items/Dismount-EC2VpnGateway.md") (AWS Tools for Windows PowerShell)

###### To delete a virtual private gateway using the command line or API

- [DeleteVpnGateway](../../../AWSEC2/latest/APIReference/API_DeleteVpnGateway.md "../../../AWSEC2/latest/APIReference/API_DeleteVpnGateway.md") (Amazon EC2 Query API)
- [delete-vpn-gateway](../../../cli/latest/reference/ec2/delete-vpn-gateway.md "../../../cli/latest/reference/ec2/delete-vpn-gateway.md") (AWS CLI)
- [Remove-EC2VpnGateway](../../../powershell/latest/reference/items/Remove-EC2VpnGateway.md "../../../powershell/latest/reference/items/Remove-EC2VpnGateway.md") (AWS Tools for Windows PowerShell)
