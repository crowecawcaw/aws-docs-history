

# Release an Elastic IP address
<a name="using-instance-addressing-eips-releasing"></a>

If you no longer need an Elastic IP address, we recommend that you release it. The Elastic IP address to release must not be currently associated with an AWS resource.

------
#### [ Console ]

**To release an Elastic IP address**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Elastic IPs**.

1. Select the Elastic IP address to release and choose **Actions**, **Release Elastic IP addresses**.

1. Choose **Release**.

------
#### [ AWS CLI ]

**To release an Elastic IP address**  
Use the [release-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/release-address.html) AWS CLI command.

```
aws ec2 release-address --allocation-id {{eipalloc-64d5890a}}
```

------
#### [ PowerShell ]

**To release an Elastic IP address**  
Use the [Remove-EC2Address](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2Address.html) cmdlet.

```
Remove-EC2Address -AllocationId {{eipalloc-64d5890a}}
```

------

After you release your Elastic IP address, you might be able to recover. The following rules apply:
+ You can't recover an Elastic IP address if it has been allocated to another AWS account, or if it will result in your exceeding your Elastic IP address limit.
+ You can't recover tags associated with an Elastic IP address.

------
#### [ AWS CLI ]

**To recover an Elastic IP address**  
Use the [allocate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-address.html) command.

```
aws ec2 allocate-address \
    --domain vpc \
    --address {{203.0.113.3}}
```

------
#### [ PowerShell ]

**To recover an Elastic IP address**  
Use the [New-EC2Address](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Address.html) cmdlet.

```
New-EC2Address `
    -Address {{203.0.113.3}} `
    -Domain vpc `
    -Region {{us-east-1}}
```

------