# Update an accelerator to change your IP addresses

After you assign BYOIP addresses as static IP addresses for an accelerator in AWS Global Accelerator,
you can update the accelerator later to use different IP addresses from your address ranges.
You can also update an accelerator that uses your own IP addresses to instead use IP addresses provided by AWS Global Accelerator.

After an Amazon-owned static IP address is changed, you can revert to the original static IP address, but you
must do so _within 10 days_ of when it was changed.
After 10 days, the original static IP address is returned to the Amazon IP address pool and reused. After that,
if you update your accelerator to change a BYOIP address to a Global Accelerator-assigned IP address, you are assigned a new IP
address from the Amazon IP address pool. To learn more about reverting your IP address, see
[Revert a static IP address change](#AGAUpdateAddressRevert "#AGAUpdateAddressRevert").

The following sections provide information about how to change IP addresses when you use bring your
own IP address (BYOIP) with Global Accelerator, and list the requirements and things to know when you change static
IP addresses.

## How to update an accelerator to change an IP address

To change an IP address for an accelerator, edit the accelerator and then, under **IP addresses**,
select a new IP address. Your options for whether you can select an address from your own BYOIP address pool or
the Amazon IP address pool depend on what your accelerator already has for static IP addresses, and other factors.

Make sure that you review the [requirements and things to
be aware of](#AGAUpdateAccRequirements "#AGAUpdateAccRequirements") for changing accelerator static IP addresses before you begin.

The following topics provide procedures for updating accelerators.

- **Use Global Accelerator console to update an accelerator.** For more information,
  see the following:

  - [Update accelerator](about-accelerators.editing.md "about-accelerators.editing.md")
  - [Edit a custom routing accelerator in Global Accelerator](about-custom-routing-accelerators.editing.md "about-custom-routing-accelerators.editing.md")

- **Use the Global Accelerator API to update an accelerator.** For more information,
  including examples of using the CLI, see the following in the AWS Global Accelerator API Reference:

  - [UpdateAccelerator](../api/API_UpdateAccelerator.md "../api/API_UpdateAccelerator.md")
  - [UpdateCustomRoutingAccelerator](../api/API_UpdateCustomRoutingAccelerator.md "../api/API_UpdateCustomRoutingAccelerator.md")

## Requirements when you update an accelerator to change IP addresses

When you update an accelerator to change one or both static IP addresses,
keep in mind the following:

- You can change the BYOIP address for both standard accelerators and custom routing accelerators. After you create an
  accelerator with one or two BYOIP addresses, that accelerator must always have at least one BYOIP address. However, you can update
  the accelerator to change one or both static IP addresses to use a BYOIP address or to change the BYOIP address
- If you have an accelerator with two BYOIP static IP addresses, you can change only one of them to use a static IP
  address assigned by Global Accelerator. Note the following about changing a BYOIP static IP address for an accelerator to a Global Accelerator-assigned static
  IP address:

  - You can only change the address back to your original BYOIP static IP address if you
    make the change _within 10 days_ of when you changed it to a Global Accelerator-assigned address.
    After 10 days, the original BYOIP static IP address is released and can no longer be restored. After that,
    if you update your accelerator to change a BYOIP address to a Global Accelerator-assigned IP address, you are assigned a new IP
    address from the Global Accelerator IP address pool.
  - You can't change both BYOIP static IP addresses to use Global Accelerator static IP addresses instead. To use two
    static IP addresses that are assigned by Global Accelerator with an accelerator, create a new accelerator.

- If you have an accelerator that is using two BYOIP addresses, you can change either of them to
  a different BYOIP address. The same restrictions apply as when you add BYOIP addresses when you create an accelerator,
  however. For example, if you update an accelerator to use two different BYOIP addresses, the addresses must be from different
  BYOIP address ranges that you've added to Global Accelerator.
- If you've configured cross-account BYOIP addresses, when you update the static IP addresses for an accelerator,
  you can use a cross-account address.
- In one specific scenario, when you update a BYOIP address, Global Accelerator might need to change your Amazon static IP address
  so that it can complete the update successfully. The Amazon static IP address can only be impacted when 1) you update a
  BYOIP static IPv4 address for your accelerator to use a BYOIP address from another account (that is, a cross-account
  BYOIP address), and 2) your second static IP address on the accelerator is from the Amazon pool.

If you didn't want the Amazon static IP address to change, you can revert to the previous Amazon IP
address, but only if no more than 10 days has elapsed since you made the update. When you revert the change, the
original Amazon IP address is restored for your accelerator. After 10 days has elapsed, however, the Amazon IP
address is released back into the available IP addresses pool and can't be restored.

## Revert a static IP address change

To revert to the original Amazon IP address for your accelerator, do the following:

- Update the accelerator with the original BYOIP static IP address that you changed to a new address.

When you make this update, Global Accelerator will restore the original Amazon static IP address as well.
