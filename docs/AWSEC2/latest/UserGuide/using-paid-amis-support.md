# Use paid support for supported AWS Marketplace

offerings

Amazon EC2 also enables developers to offer support for software (or
derived AMIs). Developers can create support products that you can sign up to use.
During sign-up for the support product, the developer gives you a product code, which you must
then associate with your own AMI. This enables the developer to confirm that your
instance is eligible for support. It also ensures that when you run instances of the
product, you are charged according to the terms for the product specified by the developer.

###### Limitations

- After you set the product code attribute, it can't be changed or removed.
- You can't use a support product with Reserved Instances. You always pay the price that's
  specified by the seller of the support product.

AWS CLI

###### To associate a product code with your AMI

Use the [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md")
command.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --product-codes "`cdef1234abc567def8EXAMPLE`"
```

PowerShell

###### To associate a product code with your AMI

Use the [Edit-EC2ImageAttribute](../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md")
cmdlet.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -ProductCode "`cdef1234abc567def8EXAMPLE`"
```
