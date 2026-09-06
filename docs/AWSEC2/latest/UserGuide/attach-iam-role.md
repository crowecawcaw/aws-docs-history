

# Attach an IAM role to an instance
<a name="attach-iam-role"></a>

You can create an IAM role and attach it to an instance during or after launch. You can also replace or detach IAM roles.

**Creating and attaching an IAM role during instance launch (Recommended)**

1. During EC2 instance launch, expand **Advanced details**.

1. In the **IAM instance profile** section, choose **Create new IAM role**.

1. An inline role creation form opens, allowing you to:
   + Specify **Role name** (for example, `EC2-S3-Access-Role`)
   + Define permissions by selecting AWS managed policies or creating custom policies for your instance

     For example, to grant S3 access, select the `AmazonS3ReadOnlyAccess` managed policy
   + Review the trust policy that allows `ec2.amazonaws.com` to assume the role
   + Add optional tags for metadata

1. Choose **Create role**.

   The newly created role is automatically selected and will be attached to your instance through an instance profile when the instance launches.

**Note**  
When you create a role using the console during instance launch, an instance profile with the same name as the role is automatically created. The instance profile is a container that passes IAM role information to the instance at launch.

**Important**  
You can only attach one IAM role to an instance, but you can attach the same role to many instances.
Associate least privilege IAM policies that restrict access to the specific API calls the application requires.

For more information about creating and using IAM roles, see [Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*.

**Attaching an existing IAM role during instance launch**  
To attach an existing IAM role to an instance at launch using the Amazon EC2 console, expand **Advanced details**. For **IAM instance profile**, select the IAM role from the dropdown list.

**Note**  
If you created your IAM role using the IAM console, the instance profile was created for you and given the same name as the role. If you created your IAM role using the AWS CLI, API, or an AWS SDK, you might have given your instance profile a different name than the role.

You can attach an IAM role to an instance that is running or stopped. If the instance already has an IAM role attached, you must replace it with the new IAM role.

------
#### [ Console ]<a name="attach-iam-role-console"></a>

**To attach an IAM role to an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance.

1. Choose **Actions**, **Security**, **Modify IAM role**.

1. For **IAM role**, select the IAM instance profile.

1. Choose **Update IAM role**.

------
#### [ AWS CLI ]
<a name="attach-iam-role-instance-cli"></a>
**To attach an IAM role to an instance**  
Use the [associate-iam-instance-profile](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-iam-instance-profile.html) command to attach the IAM role to the instance. When you specify the instance profile, you can use either the Amazon Resource Name (ARN) of the instance profile, or you can use its name.

```
aws ec2 associate-iam-instance-profile \
    --instance-id {{i-1234567890abcdef0}} \
    --iam-instance-profile Name="{{TestRole-1}}"
```

------
#### [ PowerShell ]

**To attach an IAM role to an instance**  
Use the [Register-EC2IamInstanceProfile](https://docs.aws.amazon.com/powershell/latest/reference/items/Register-EC2IamInstanceProfile.html) cmdlet.

```
Register-EC2IamInstanceProfile `
    -InstanceId {{i-1234567890abcdef0}} `
    -IamInstanceProfile_Name {{TestRole-1}}
```

------

To replace the IAM role on an instance that already has an attached IAM role, the instance must be running. You can do this if you want to change the IAM role for an instance without detaching the existing one first. For example, you can do this to ensure that API actions performed by applications running on the instance are not interrupted.

------
#### [ Console ]<a name="replace-iam-role-console"></a>

**To replace an IAM role for an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance.

1. Choose **Actions**, **Security**, **Modify IAM role**.

1. For **IAM role**, select the IAM instance profile.

1. Choose **Update IAM role**.

------
#### [ AWS CLI ]<a name="replace-iam-role-cli"></a>

**To replace an IAM role for an instance**

1. If required, use the [describe-iam-instance-profile-associations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-iam-instance-profile-associations.html) command to get the association ID.

   ```
   aws ec2 describe-iam-instance-profile-associations \
       --filters Name=instance-id,Values={{i-1234567890abcdef0}} \
       --query IamInstanceProfileAssociations.AssociationId
   ```

1. Use the [replace-iam-instance-profile-association](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-iam-instance-profile-association.html) command. Specify the association ID for the existing instance profile and the ARN or name of the new instance profile.

   ```
   aws ec2 replace-iam-instance-profile-association \
       --association-id {{iip-assoc-0044d817db6c0a4ba}} \
       --iam-instance-profile Name="{{TestRole-2}}"
   ```

------
#### [ PowerShell ]

**To replace an IAM role for an instance**

1. If required, use the [Get-EC2IamInstanceProfileAssociation](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IamInstanceProfileAssociation.html) cmdlet to get the association ID.

   ```
   (Get-EC2IamInstanceProfileAssociation -Filter @{Name="instance-id"; Values="{{i-0636508011d8e966a}}"}).AssociationId
   ```

1. Use the [Set-EC2IamInstanceProfileAssociation](https://docs.aws.amazon.com/powershell/latest/reference/items/Set-EC2IamInstanceProfileAssociation.html) cmdlet. Specify the association ID for the existing instance profile and the ARN or name of the new instance profile.

   ```
   Set-EC2IamInstanceProfileAssociation `
       -AssociationId {{iip-assoc-0044d817db6c0a4ba}} `
       -IamInstanceProfile_Name {{TestRole-2}}
   ```

------

You can detach an IAM role from an instance that is running or stopped.

------
#### [ Console ]<a name="detach-iam-role-console"></a>

**To detach an IAM role from an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance.

1. Choose **Actions**, **Security**, **Modify IAM role**.

1. For **IAM role**, choose **No IAM Role**.

1. Choose **Update IAM role**.

1. When promoted for confirmation, enter **Detach**, and then choose **Detach**.

------
#### [ AWS CLI ]<a name="detach-iam-role-cli"></a>

**To detach an IAM role from an instance**

1. If required, use [describe-iam-instance-profile-associations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-iam-instance-profile-associations.html) to get the association ID for the IAM instance profile to detach.

   ```
   aws ec2 describe-iam-instance-profile-associations \
       --filters Name=instance-id,Values={{i-1234567890abcdef0}} \
       --query IamInstanceProfileAssociations.AssociationId
   ```

1. Use the [disassociate-iam-instance-profile](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-iam-instance-profile.html) command.

   ```
   aws ec2 disassociate-iam-instance-profile --association-id {{iip-assoc-0044d817db6c0a4ba}}
   ```

------
#### [ PowerShell ]

**To detach an IAM role from an instance**

1. If required, use [Get-EC2IamInstanceProfileAssociation](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IamInstanceProfileAssociation.html) to get the association ID for the IAM instance profile to detach.

   ```
   (Get-EC2IamInstanceProfileAssociation -Filter @{Name="instance-id"; Values="i-0636508011d8e966a"}).AssociationId
   ```

1. Use the [Unregister-EC2IamInstanceProfile](https://docs.aws.amazon.com/powershell/latest/reference/items/Unregister-EC2IamInstanceProfile.html) cmdlet.

   ```
   Unregister-EC2IamInstanceProfile -AssociationId {{iip-assoc-0044d817db6c0a4ba}}
   ```

------