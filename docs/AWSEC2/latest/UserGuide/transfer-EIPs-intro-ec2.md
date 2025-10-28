# Transfer an Elastic IP address between AWS accounts

You can transfer an Elastic IP address from one AWS account to another. This can be
helpful in the following situations:

- Disaster recovery – Quickly remap
  the IP addresses for public-facing internet workloads during emergency events.
- Organizational restructuring –
  Quickly move a workload from one AWS account to another. An address transfer
  avoids the need to wait for new Elastic IP addresses to be allowed by your
  security groups and network ACLs.
- Centralized security administration –
  Use a centralized AWS security account to track and transfer Elastic IP addresses
  that have been vetted for security compliance.

###### Pricing

There is no charge for transferring Elastic IP addresses.

###### Tasks

- [Enable Elastic IP address transfer](#using-instance-addressing-eips-transfer-enable-ec2 "#using-instance-addressing-eips-transfer-enable-ec2")
- [Accept a transferred Elastic IP address](#using-instance-addressing-eips-transfer-accept-ec2 "#using-instance-addressing-eips-transfer-accept-ec2")
- [Disable Elastic IP address transfer](#using-instance-addressing-eips-transfer-disable-ec2 "#using-instance-addressing-eips-transfer-disable-ec2")

## Enable Elastic IP address transfer

This section describes how to accept a transferred Elastic IP address. Note
the following limitations related to enabling Elastic IP addresses for
transfer:

- You can transfer Elastic IP addresses from any AWS account (source account) to any
  other AWS account in the same AWS Region (transfer account). You cannot transfer
  Elastic IP addresses to a different Region.
- When you transfer an Elastic IP address, there is a two-step handshake
  between the AWS accounts. When the source account starts the transfer,
  the transfer accounts have seven days to accept the Elastic IP address
  transfer. During those seven days, the source account can view the
  pending transfer (for example in the AWS console or by using the [describe-address-transfers](../../../cli/latest/reference/ec2/describe-address-transfers.md "../../../cli/latest/reference/ec2/describe-address-transfers.md") command). After seven
  days, the transfer expires and ownership of the Elastic IP
  address returns to the
  source account.
- Accepted transfers are visible to the source account (for example in
  the AWS console or by using the [describe-address-transfers](../../../cli/latest/reference/ec2/describe-address-transfers.md "../../../cli/latest/reference/ec2/describe-address-transfers.md") command) for 14 days
  after the transfers have been accepted.
- AWS does not notify transfer accounts about pending Elastic IP
  address transfer requests. The owner of the source account must notify
  the owner of the transfer account that there is an Elastic IP address
  transfer request that they must accept.
- Any tags that are associated with an Elastic IP address being
  transferred are reset when the transfer is complete.
- You cannot transfer Elastic IP addresses allocated from public IPv4
  address pools that you bring to your AWS account – commonly
  referred to as Bring Your Own IP (BYOIP) address pools.
- You cannot transfer Elastic IP
  addresses allocated from an Amazon-provided contiguous public IPv4 Amazon VPC IP Address Manager (IPAM) pool. Instead, IPAM allows you to share IPAM pools across AWS accounts by integrating IPAM with AWS Organizations and using AWS RAM. For more information, see [Allocate sequential Elastic IP addresses from an IPAM pool](../../../vpc/latest/ipam/tutorials-eip-pool.md "../../../vpc/latest/ipam/tutorials-eip-pool.md") in the _Amazon VPC IPAM User Guide_.
- If you attempt to transfer an Elastic IP address that has a reverse
  DNS record associated with it, you can begin the transfer process, but
  the transfer account will not be able to accept the transfer until the
  associated DNS record is removed.
- If you have enabled and configured AWS Outposts, you might have allocated
  Elastic IP addresses from a customer-owned IP address pool
  (CoIP). You cannot transfer Elastic IP addresses allocated from a CoIP.
  However, you can use AWS RAM to share a CoIP with another account.
  For more information, see [Customer-owned IP addresses](../../../outposts/latest/userguide/routing.md#ip-addressing "../../../outposts/latest/userguide/routing.md#ip-addressing") in the _AWS Outposts User Guide_.
- You can use Amazon VPC IPAM to track the transfer of Elastic IP addresses to
  accounts in an organization from AWS Organizations. For more information, see [View IP address history](../../../vpc/latest/ipam/view-history-cidr-ipam.md "../../../vpc/latest/ipam/view-history-cidr-ipam.md"). If an Elastic IP address is
  transferred to an AWS account outside of the organization, the IPAM audit
  history of the Elastic IP address is lost.

These steps must be completed by the source account.

Console

###### To enable Elastic IP address transfer

1. Ensure that you're using the source AWS account.
2. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
3. In the navigation pane, choose **Elastic IPs**.
4. Select one or more Elastic IP address to enable for transfer and choose **Actions**,
   **Enable transfer**.
5. If you are transferring multiple Elastic IP addresses, you’ll see the **Transfer
   type** option. Choose one of the following options:
   - Choose **Single account** if you are transferring the Elastic IP addresses to
     a single AWS account.
   - Choose **Multiple accounts** if you are transferring the Elastic IP addresses
     to multiple AWS accounts.

6. Under **Transfer account ID**, enter the IDs of the
   AWS accounts that you want to transfer the Elastic IP addresses
   to.
7. Confirm the transfer by entering `enable` in the
   text box.
8. Choose **Submit**.
9. To accept the transfer, see [Accept a transferred Elastic IP address](#using-instance-addressing-eips-transfer-accept-ec2 "#using-instance-addressing-eips-transfer-accept-ec2"). To
   disable the transfer, see [Disable Elastic IP address transfer](#using-instance-addressing-eips-transfer-disable-ec2 "#using-instance-addressing-eips-transfer-disable-ec2").

AWS CLI
**To enable Elastic IP address transfer**

Use the [enable-address-transfer](../../../cli/latest/reference/ec2/enable-address-transfer.md "../../../cli/latest/reference/ec2/enable-address-transfer.md") command.

```
aws ec2 enable-address-transfer \
    --allocation-id `eipalloc-09ad461b0d03f6aaf` \
    --transfer-account-id `123456789012`
```

PowerShell

###### To enable Elastic IP address transfer

Use the [Enable-EC2AddressTransfer](../../../powershell/latest/reference/items/Enable-EC2AddressTransfer.md "../../../powershell/latest/reference/items/Enable-EC2AddressTransfer.md") cmdlet.

```
Enable-EC2AddressTransfer `
    -AllocationId `eipalloc-09ad461b0d03f6aaf` `
    -TransferAccountId `123456789012`
```

## Accept a transferred Elastic IP address

This section describes how to accept a transferred Elastic IP address.

When you transfer an Elastic IP address, there is a two-step handshake
between the AWS accounts. When the source account starts the transfer,
the transfer accounts have seven days to accept the Elastic IP address
transfer. During those seven days, the source account can view the
pending transfer (for example in the AWS console or by using the [describe-address-transfers](../../../cli/latest/reference/ec2/describe-address-transfers.md "../../../cli/latest/reference/ec2/describe-address-transfers.md") command). After seven
days, the transfer expires and ownership of the Elastic IP
address returns to the
source account.

When accepting transfers, note the following exceptions that might occur and
how to resolve them:

- **AddressLimitExceeded**: If your
  transfer account has exceeded the Elastic IP address quota, the source
  account can enable Elastic IP address transfer, but this exception
  occurs when the transfer account tries to accept the transfer. By
  default, all AWS accounts are limited to 5 Elastic IP addresses per
  Region. See [Elastic IP address quota](elastic-ip-addresses-eip.md#using-instance-addressing-limit "elastic-ip-addresses-eip.md#using-instance-addressing-limit") for instructions on increasing
  the limit.
- **InvalidTransfer.AddressCustomPtrSet**:
  If you or someone in your organization has configured the Elastic IP
  address that you are attempting to transfer to use reverse DNS lookup,
  the source account can enable transfer for the Elastic IP address, but
  this exception occurs when the transfer account tries to accept the
  transfer. To resolve this issue, the source account must remove the DNS
  record for the Elastic IP address. For more information, see [Create a reverse DNS record for email on Amazon EC2](Using_Elastic_Addressing_Reverse_DNS.md "Using_Elastic_Addressing_Reverse_DNS.md").
- **InvalidTransfer.AddressAssociated**: If
  an Elastic IP address is associated with an ENI or EC2 instance, the
  source account can enable transfer for the Elastic IP address, but this
  exception occurs when the transfer account tries to accept the transfer.
  To resolve this issue, the source account must disassociate the Elastic
  IP address. For more information, see [Disassociate an Elastic IP
  address](working-with-eips.md#using-instance-addressing-eips-associating-different "working-with-eips.md#using-instance-addressing-eips-associating-different").

For any other exceptions, [contact
Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

These steps must be completed by the transfer account.

Console

###### To accept an Elastic IP address transfer

1. Ensure that you're using the transfer account.
2. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
3. In the navigation pane, choose **Elastic IPs**.
4. Choose **Actions**,
   **Accept transfer**.
5. No tags that are associated with the Elastic IP address being
   transferred are transferred with the Elastic IP address when you accept
   the transfer. If you want to define a **Name** tag for
   the Elastic IP address that you are accepting, select **Create a
   tag with a key of 'Name' and a value that you
   specify**.
6. Enter the Elastic IP address that you want to transfer.
7. If you are accepting multiple transferred Elastic IP addresses, choose
   **Add address** to enter an additional Elastic IP
   address.
8. Choose **Submit**.

AWS CLI
**To accept an Elastic IP address transfer**

Use the [accept-address-transfer](../../../cli/latest/reference/ec2/accept-address-transfer.md "../../../cli/latest/reference/ec2/accept-address-transfer.md") command.

```
aws ec2 accept-address-transfer --address `100.21.184.216`
```

PowerShell

###### To accept an Elastic IP address transfer

Use the [Approve-EC2AddressTransfer](../../../powershell/latest/reference/items/Approve-EC2AddressTransfer.md "../../../powershell/latest/reference/items/Approve-EC2AddressTransfer.md")
cmdlet.

```
Approve-EC2AddressTransfer -Address `100.21.184.216`
```

## Disable Elastic IP address transfer

This section describes how to disable an Elastic IP transfer after the
transfer has been enabled.

These steps must be completed by the source account that enabled the transfer.

Console

###### To disable an Elastic IP address transfer

1. Ensure that you're using the source AWS account.
2. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
3. In the navigation pane, choose **Elastic IPs**.
4. In the resource list of Elastic IPs, ensure that you have the property enabled that shows the column **Transfer status**.
5. Select one or more Elastic IP address that have a **Transfer
   status** of **Pending**, and choose
   **Actions**, **Disable
   transfer**.
6. Confirm by entering `disable` in the text
   box.
7. Choose **Submit**.

AWS CLI
**To disable Elastic IP address transfer**

Use the [disable-address-transfer](../../../cli/latest/reference/ec2/disable-address-transfer.md "../../../cli/latest/reference/ec2/disable-address-transfer.md") command.

```
aws ec2 disable-address-transfer --allocation-id `eipalloc-09ad461b0d03f6aaf`
```

PowerShell

###### To disable Elastic IP address transfer

Use the [Disable-EC2AddressTransfer](../../../powershell/latest/reference/items/Disable-EC2AddressTransfer.md "../../../powershell/latest/reference/items/Disable-EC2AddressTransfer.md") cmdlet.

```
Disable-EC2AddressTransfer -AllocationId `eipalloc-09ad461b0d03f6aaf`
```
