# Create a reverse DNS record for email on Amazon EC2

If you intend to send email to third parties from an EC2 instance, we recommend that you
provision one or more Elastic IP addresses and assign static reverse DNS records to the
Elastic IP addresses that you use to send email. This can help you avoid having your
email flagged as spam by some anti-spam organizations. AWS works with ISPs and
internet anti-spam organizations to reduce the chance that your email sent from these
addresses will be flagged as spam.

###### Considerations

- Before you create a reverse DNS record, you must set a corresponding forward DNS record
  (record type A) that points to your Elastic IP address.
- If a reverse DNS record is associated with an Elastic IP address, the Elastic IP address
  is locked to your account and cannot be released from your account until the record is
  removed.
- If you contacted Support to set up reverse DNS for an Elastic IP address, you can
  remove the reverse DNS, but you can't release the Elastic IP address because it is
  locked by Support. To unlock the Elastic IP address, contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). After the Elastic IP address
  is unlocked, you can release it.
- [AWS GovCloud (US) Region] You can't create a reverse DNS record. AWS
  must assign the static reverse DNS records for you. Open a support case
  to remove reverse DNS and email sending limitations. You must provide your
  Elastic IP addresses and reverse DNS records.

## Create a reverse DNS record

You can create a reverse DNS record for your Elastic IP address as follows.

Console

###### To create a reverse DNS record

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic IPs**.
3. Select the Elastic IP address and choose **Actions**,
   **Update reverse DNS**.
4. For **Reverse DNS domain name**, enter the domain name.
5. Enter `update` to confirm.
6. Choose **Update**.

AWS CLI

###### To create a reverse DNS record

Use the [modify-address-attribute](../../../cli/latest/reference/ec2/modify-address-attribute.md "../../../cli/latest/reference/ec2/modify-address-attribute.md") command.

```
aws ec2 modify-address-attribute \
    --allocation-id `eipalloc-abcdef01234567890` \
    --domain-name `example.com`
```

The following is example output.

```
{
    "Addresses": [
        {
            "PublicIp": "192.0.2.0",
            "AllocationId": "eipalloc-abcdef01234567890",
            "PtrRecord": "example.net.",
            "PtrRecordUpdate": {
                "Value": "example.com.",
                "Status": "PENDING"
            }
        }
    ]
}
```

PowerShell

###### To create a reverse DNS record

Use the [Edit-EC2AddressAttribute](../../../powershell/latest/reference/items/Edit-EC2AddressAttribute.md "../../../powershell/latest/reference/items/Edit-EC2AddressAttribute.md") cmdlet.

```
Edit-EC2AddressAttribute `
    -AllocationId '`eipalloc-abcdef01234567890`' `
    -DomainName '`example.com`' |
Format-List `
    AllocationId, PtrRecord, PublicIp,
    @{Name='PtrRecordUpdate';Expression={$_.PtrRecordUpdate | Format-List | Out-String}}
```

The following is example output.

```
AllocationId    : eipalloc-abcdef01234567890
PtrRecord       : example.net.
PublicIp        : 192.0.2.0
PtrRecordUpdate :
                  Reason :
                  Status : PENDING
                  Value  : example.com.
```

## Remove a reverse DNS record

You can remove a reverse DNS record from your Elastic IP address as follows.

If you receive the following error, you can submit a [Request to remove email
sending restrictions](https://repost.aws/knowledge-center/ec2-port-25-throttle "https://repost.aws/knowledge-center/ec2-port-25-throttle") to Support for assistance.

```
The address cannot be released because it is locked to your account.
```

Console

###### To remove a reverse DNS record

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic IPs**.
3. Select the Elastic IP address and choose **Actions**,
   **Update reverse DNS**.
4. For **Reverse DNS domain name**, clear the domain name.
5. Enter `update` to confirm.
6. Choose **Update**.

AWS CLI

###### To remove a reverse DNS record

Use the [reset-address-attribute](../../../cli/latest/reference/ec2/reset-address-attribute.md "../../../cli/latest/reference/ec2/reset-address-attribute.md") command.

```
aws ec2 reset-address-attribute \
    --allocation-id `eipalloc-abcdef01234567890` \
    --attribute `domain-name`
```

The following is example output.

```
{
    "Addresses": [
        {
            "PublicIp": "192.0.2.0",
            "AllocationId": "eipalloc-abcdef01234567890",
            "PtrRecord": "example.com.",
            "PtrRecordUpdate": {
                "Value": "example.net.",
                "Status": "PENDING"
            }
        }
    ]
}
```

PowerShell

###### To remove a reverse DNS record

Use the [Reset-EC2AddressAttribute](../../../powershell/latest/reference/items/Reset-EC2AddressAttribute.md "../../../powershell/latest/reference/items/Reset-EC2AddressAttribute.md")
cmdlet.

```
Reset-EC2AddressAttribute `
    -AllocationId 'eipalloc-abcdef01234567890' `
    -Attribute domain-name |
Format-List `
    AllocationId, PtrRecord, PublicIp,
    @{Name='PtrRecordUpdate';Expression={$_.PtrRecordUpdate | Format-List | Out-String}}
```

The following is example output.

```
AllocationId    : eipalloc-abcdef01234567890
PtrRecord       : example.com.
PublicIp        : 192.0.2.0
PtrRecordUpdate :
                  Reason :
                  Status : PENDING
                  Value  : example.net.
```
