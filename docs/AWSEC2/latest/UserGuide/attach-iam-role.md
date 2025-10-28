# Attach an IAM role to an instance

You can create an IAM role and attach it to an instance during or after launch.
You can also replace or detach IAM roles.

To attach an IAM role to an instance at launch using the Amazon EC2 console, expand
**Advanced details**. For **IAM instance profile**,
select the IAM role.

###### Note

If you created your IAM role using the IAM console, the instance
profile was created for you and given the same name as the role. If
you created your IAM role using the AWS CLI, API, or an AWS SDK,
you might have given your instance profile a different name than
the role.

You can attach an IAM role to an instance that is running or stopped. If the
instance already has an IAM role attached, you must replace it with the new
IAM role.

Console

###### To attach an IAM role to an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance.
4. Choose **Actions**, **Security**,
   **Modify IAM role**.
5. For **IAM role**, select the IAM instance
   profile.
6. Choose **Update IAM role**.

AWS CLI

###### To attach an IAM role to an instance

Use the [associate-iam-instance-profile](../../../cli/latest/reference/ec2/associate-iam-instance-profile.md "../../../cli/latest/reference/ec2/associate-iam-instance-profile.md") command to attach the IAM
role to the instance. When you specify the instance profile, you can use
either the Amazon Resource Name (ARN) of the instance profile, or you
can use its name.

```
aws ec2 associate-iam-instance-profile \
    --instance-id `i-1234567890abcdef0` \
    --iam-instance-profile Name="`TestRole-1`"
```

PowerShell

###### To attach an IAM role to an instance

Use the [Register-EC2IamInstanceProfile](../../../powershell/latest/reference/items/Register-EC2IamInstanceProfile.md "../../../powershell/latest/reference/items/Register-EC2IamInstanceProfile.md") cmdlet.

```
Register-EC2IamInstanceProfile `
    -InstanceId `i-1234567890abcdef0` `
    -IamInstanceProfile_Name `TestRole-1`
```

To replace the IAM role on an instance that already has an attached IAM role, the
instance must be running. You can do this if you want to change the IAM role for
an instance without detaching the existing one first. For example, you can do this
to ensure that API actions performed by applications running on the instance are not
interrupted.

Console

###### To replace an IAM role for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance.
4. Choose **Actions**, **Security**,
   **Modify IAM role**.
5. For **IAM role**, select the IAM instance
   profile.
6. Choose **Update IAM role**.

AWS CLI

###### To replace an IAM role for an instance

1. If required, use the [describe-iam-instance-profile-associations](../../../cli/latest/reference/ec2/describe-iam-instance-profile-associations.md "../../../cli/latest/reference/ec2/describe-iam-instance-profile-associations.md") command to get the association ID.

```
aws ec2 describe-iam-instance-profile-associations \
    --filters Name=instance-id,Values=`i-1234567890abcdef0` \
    --query IamInstanceProfileAssociations.AssociationId
```

2. Use the [replace-iam-instance-profile-association](../../../cli/latest/reference/ec2/replace-iam-instance-profile-association.md "../../../cli/latest/reference/ec2/replace-iam-instance-profile-association.md") command. Specify the
   association ID for the existing instance profile and the ARN or name
   of the new instance profile.

```
aws ec2 replace-iam-instance-profile-association \
    --association-id `iip-assoc-0044d817db6c0a4ba` \
    --iam-instance-profile Name="`TestRole-2`"
```

PowerShell

###### To replace an IAM role for an instance

1. If required, use the [Get-EC2IamInstanceProfileAssociation](../../../powershell/latest/reference/items/Get-EC2IamInstanceProfileAssociation.md "../../../powershell/latest/reference/items/Get-EC2IamInstanceProfileAssociation.md") cmdlet to get the association ID.

```
(Get-EC2IamInstanceProfileAssociation -Filter @{Name="instance-id"; Values="`i-0636508011d8e966a`"}).AssociationId
```

2. Use the [Set-EC2IamInstanceProfileAssociation](../../../powershell/latest/reference/items/Set-EC2IamInstanceProfileAssociation.md "../../../powershell/latest/reference/items/Set-EC2IamInstanceProfileAssociation.md") cmdlet. Specify the
   association ID for the existing instance profile and the ARN or name
   of the new instance profile.

```
Set-EC2IamInstanceProfileAssociation `
    -AssociationId `iip-assoc-0044d817db6c0a4ba` `
    -IamInstanceProfile_Name `TestRole-2`
```

You can detach an IAM role from an instance that is running or stopped.

Console

###### To detach an IAM role from an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance.
4. Choose **Actions**, **Security**,
   **Modify IAM role**.
5. For **IAM role**, choose **No IAM
   Role**.
6. Choose **Update IAM role**.
7. When promoted for confirmation, enter **Detach**,
   and then choose **Detach**.

AWS CLI

###### To detach an IAM role from an instance

1. If required, use [describe-iam-instance-profile-associations](../../../cli/latest/reference/ec2/describe-iam-instance-profile-associations.md "../../../cli/latest/reference/ec2/describe-iam-instance-profile-associations.md") to get the
   association ID for the IAM instance profile to detach.

```
aws ec2 describe-iam-instance-profile-associations \
    --filters Name=instance-id,Values=`i-1234567890abcdef0` \
    --query IamInstanceProfileAssociations.AssociationId
```

2. Use the [disassociate-iam-instance-profile](../../../cli/latest/reference/ec2/disassociate-iam-instance-profile.md "../../../cli/latest/reference/ec2/disassociate-iam-instance-profile.md") command.

```
aws ec2 disassociate-iam-instance-profile --association-id `iip-assoc-0044d817db6c0a4ba`
```

PowerShell

###### To detach an IAM role from an instance

1. If required, use [Get-EC2IamInstanceProfileAssociation](../../../powershell/latest/reference/items/Get-EC2IamInstanceProfileAssociation.md "../../../powershell/latest/reference/items/Get-EC2IamInstanceProfileAssociation.md") to get the association
   ID for the IAM instance profile to detach.

```
(Get-EC2IamInstanceProfileAssociation -Filter @{Name="instance-id"; Values="i-0636508011d8e966a"}).AssociationId
```

2. Use the [Unregister-EC2IamInstanceProfile](../../../powershell/latest/reference/items/Unregister-EC2IamInstanceProfile.md "../../../powershell/latest/reference/items/Unregister-EC2IamInstanceProfile.md") cmdlet.

```
Unregister-EC2IamInstanceProfile -AssociationId `iip-assoc-0044d817db6c0a4ba`
```
