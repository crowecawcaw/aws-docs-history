# Delete your key pair

You can delete a key pair, which removes the public key that is stored in Amazon EC2. Deleting
a key pair does not delete the matching private key.

When you delete a public key using the following methods, you're only deleting the public
key that you stored in Amazon EC2 when you [created](create-key-pairs.md#having-ec2-create-your-key-pair "create-key-pairs.md#having-ec2-create-your-key-pair") or [imported](create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws "create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws") the key pair. Deleting a public key doesn't remove the public key from any
instances to which you've added it, either when you launched the instance or later. It also
doesn't delete the private key on your local computer. You can continue to connect to
instances that you launched using a public key that you've deleted from Amazon EC2 as long as you
still have the private key (`.pem`) file.

###### Important

If you're using an Amazon EC2 Auto Scaling group (for example, in an Elastic Beanstalk environment), ensure that the
public key you're deleting is not specified in an associated launch template or launch
configuration. If Amazon EC2 Auto Scaling detects an unhealthy instance, it launches a replacement
instance. However, the instance launch fails if the public key cannot be found. For more
information, see [Launch templates](../../../autoscaling/ec2/userguide/launch-templates.md "../../../autoscaling/ec2/userguide/launch-templates.md") in the
_Amazon EC2 Auto Scaling User Guide_.

Console

###### To delete your public key on Amazon EC2

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Key Pairs**.
3. Select the key pair to delete and choose **Actions**,
   **Delete**.
4. In the confirmation field, enter `Delete` and then choose
   **Delete**.

AWS CLI

###### To delete your public key on Amazon EC2

Use the [delete-key-pair](../../../cli/latest/reference/ec2/delete-key-pair.md "../../../cli/latest/reference/ec2/delete-key-pair.md") command.

```
aws ec2 delete-key-pair --key-name `my-key-pair`
```

PowerShell

###### To delete your public key on Amazon EC2

Use the [Remove-EC2KeyPair](../../../powershell/latest/reference/items/Remove-EC2KeyPair.md "../../../powershell/latest/reference/items/Remove-EC2KeyPair.md") cmdlet.

```
Remove-EC2KeyPair -KeyName `my-key-pair`
```
