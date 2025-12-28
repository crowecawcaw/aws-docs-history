# Deprovision the address range

To stop using your address range with AWS, you first must remove any accelerators that have static IP addresses that
are allocated from the address pool and stop advertising your address range. After you complete
those steps, you can deprovision the address range.

You must stop advertising and deprovision your address range using the CLI or Global Accelerator API operations. This functionality
is not available in the AWS console.

**Step 1: Delete any associated accelerators.** To delete an
accelerator using the console or using API operations, see [Delete accelerator](about-accelerators.md "about-accelerators.md").

**Step 2. Stop advertising the address range.** To stop advertising the range, use the
following [WithdrawByoipCidr](../api/API_WithdrawByoipCidr.md "../api/API_WithdrawByoipCidr.md") command.

```
`aws globalaccelerator --region us-west-2 withdraw-byoip-cidr --cidr `address-range``
```

**Step 3. Deprovision the address range.** To deprovision the range, use the following
[DeprovisionByoipCidr](../api/API_DeprovisionByoipCidr.md "../api/API_DeprovisionByoipCidr.md") command.

```
`aws globalaccelerator --region us-west-2 deprovision-byoip-cidr --cidr `address-range``
```
