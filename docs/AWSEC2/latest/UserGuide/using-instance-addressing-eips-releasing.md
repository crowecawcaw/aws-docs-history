# Release an Elastic IP address

If you no longer need an Elastic IP address, we recommend that you release it. The Elastic
IP address to release must not be currently associated with an AWS resource.

Console

###### To release an Elastic IP address

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic IPs**.
3. Select the Elastic IP address to release and choose **Actions**,
   **Release Elastic IP addresses**.
4. Choose **Release**.

AWS CLI

###### To release an Elastic IP address

Use the [release-address](../../../cli/latest/reference/ec2/release-address.md "../../../cli/latest/reference/ec2/release-address.md") AWS CLI command.

```
aws ec2 release-address --allocation-id `eipalloc-64d5890a`
```

PowerShell

###### To release an Elastic IP address

Use the [Remove-EC2Address](../../../powershell/latest/reference/items/Remove-EC2Address.md "../../../powershell/latest/reference/items/Remove-EC2Address.md")
cmdlet.

```
Remove-EC2Address -AllocationId `eipalloc-64d5890a`
```

After you release your Elastic IP address, you might be able to recover. The following
rules apply:

- You can't recover an Elastic IP address if it has been allocated to another AWS
  account, or if it will result in your exceeding your Elastic IP address
  limit.
- You can't recover tags associated with an Elastic IP address.

AWS CLI

###### To recover an Elastic IP address

Use the [allocate-address](../../../cli/latest/reference/ec2/allocate-address.md "../../../cli/latest/reference/ec2/allocate-address.md")
command.

```
aws ec2 allocate-address \
    --domain vpc \
    --address `203.0.113.3`
```

PowerShell

###### To recover an Elastic IP address

Use the [New-EC2Address](../../../powershell/latest/reference/items/New-EC2Address.md "../../../powershell/latest/reference/items/New-EC2Address.md")
cmdlet.

```
New-EC2Address `
    -Address `203.0.113.3` `
    -Domain vpc `
    -Region `us-east-1`
```
