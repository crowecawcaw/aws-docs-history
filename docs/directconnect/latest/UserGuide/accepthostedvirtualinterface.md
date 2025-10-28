# Accept a hosted AWS Direct Connect virtual interface

Before you can begin using a hosted virtual interface, you must accept the virtual
interface. For a private virtual interface, you must also have an existing virtual private
gateway or Direct Connect gateway. For a transit virtual interface, you must have an
existing transit gateway or Direct Connect gateway.

You can accept a hosted virtual interface using either the AWS Direct Connect console or the command
line or API.

###### To accept a hosted virtual interface

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Virtual Interfaces**.
3. Select the virtual interface and then choose **View
   details**.
4. Choose **Accept**.
5. This applies to private virtual interfaces and transit virtual
   interfaces.

(Transit virtual interface) In the **Accept virtual interface** dialog
box, select a Direct Connect gateway, and then choose **Accept virtual
interface**.

(Private virtual interface) In the **Accept virtual
interface** dialog box, select a virtual private gateway or Direct
Connect gateway, and then choose **Accept virtual
interface**. 6. After you accept the hosted virtual interface, the owner of the AWS Direct Connect
connection can download the router configuration file. The **Download
router configuration** option is not available for the account that
accepts the hosted virtual interface.

###### To accept a hosted private virtual interface using the command line or

API

- [confirm-private-virtual-interface](../../../cli/latest/reference/directconnect/confirm-private-virtual-interface.md "../../../cli/latest/reference/directconnect/confirm-private-virtual-interface.md") (AWS CLI)
- [ConfirmPrivateVirtualInterface](../APIReference/API_ConfirmPrivateVirtualInterface.md "../APIReference/API_ConfirmPrivateVirtualInterface.md") (AWS Direct Connect API)

###### To accept a hosted public virtual interface using the command line or API

- [confirm-public-virtual-interface](../../../cli/latest/reference/directconnect/confirm-public-virtual-interface.md "../../../cli/latest/reference/directconnect/confirm-public-virtual-interface.md") (AWS CLI)
- [ConfirmPublicVirtualInterface](../APIReference/API_ConfirmPublicVirtualInterface.md "../APIReference/API_ConfirmPublicVirtualInterface.md") (AWS Direct Connect API)

###### To accept a hosted transit virtual interface using the command line or

API

- [confirm-transit-virtual-interface](../../../cli/latest/reference/directconnect/confirm-transit-virtual-interface.md "../../../cli/latest/reference/directconnect/confirm-transit-virtual-interface.md") (AWS CLI)
- [ConfirmTransitVirtualInterface](../APIReference/API_ConfirTransitVirtualInterface.md "../APIReference/API_ConfirTransitVirtualInterface.md") (AWS Direct Connect API)
