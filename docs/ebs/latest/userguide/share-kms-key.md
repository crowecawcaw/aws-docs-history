

# Share the KMS key used to encrypt a shared Amazon EBS snapshot
<a name="share-kms-key"></a>

When you share an encrypted snapshot, you must also share the customer managed key used to encrypt the snapshot. You can apply cross-account permissions to a customer managed key either when it is created or at a later time.

Users of your shared customer managed key who are accessing encrypted snapshots must be granted permissions to perform the following actions on the key:
+ `kms:DescribeKey`
+ `kms:CreateGrant`
+ `kms:GenerateDataKey`
+ `kms:GenerateDataKeyWithoutPlaintext`
+ `kms:ReEncrypt`
+ `kms:Decrypt`

**Tip**  
To follow the principle of least privilege, do not allow full access to `kms:CreateGrant`. Instead, use the `kms:GrantIsForAWSResource` condition key to allow the user to create grants on the KMS key only when the grant is created on the user's behalf by an AWS service.

For more information about controlling access to a customer managed key, see [ Using key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

**To share customer managed key using the AWS KMS console**

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. Choose **Customer managed keys** in the navigation pane.

1. In the **Alias** column, choose the alias (text link) of the customer managed key that you used to encrypt the snapshot. The key details open in a new page.

1. In the **Key policy** section, you see either the *policy view* or the *default view*. The policy view displays the key policy document. The default view displays sections for **Key administrators**, **Key deletion**, **Key Use**, and **Other AWS accounts**. The default view displays if you created the policy in the console and have not customized it. If the default view is not available, you'll need to manually edit the policy in the policy view. For more information, see [Viewing a Key Policy (Console)](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-viewing.html#key-policy-viewing-console) in the *AWS Key Management Service Developer Guide*.

   Use either the policy view or the default view, depending on which view you can access, to add one or more AWS account IDs to the policy, as follows:
   + (Policy view) Choose **Edit**. Add one or more AWS account IDs to the following statements: `"Allow use of the key"` and `"Allow attachment of persistent resources"`. Choose **Save changes**. In the following example, the AWS account ID `444455556666` is added to the policy.

     ```
     {
       "Sid": "Allow use of the key",
       "Effect": "Allow",
       "Principal": {"AWS": [
         "arn:aws:iam::{{111122223333}}:user/{{KeyUser}}",
         "arn:aws:iam::{{444455556666}}:root"
       ]},
       "Action": [
         "kms:Encrypt",
         "kms:Decrypt",
         "kms:ReEncrypt*",
         "kms:GenerateDataKey*",
         "kms:DescribeKey"
       ],
       "Resource": "*"
     },
     {
       "Sid": "Allow attachment of persistent resources",
       "Effect": "Allow",
       "Principal": {"AWS": [
         "arn:aws:iam::{{111122223333}}:user/{{KeyUser}}",
         "arn:aws:iam::{{444455556666}}:root"
       ]},
       "Action": [
         "kms:CreateGrant",
         "kms:ListGrants",
         "kms:RevokeGrant"
       ],
       "Resource": "*",
       "Condition": {"Bool": {"kms:GrantIsForAWSResource": true}}
     }
     ```
   + (Default view) Scroll down to **Other AWS accounts**. Choose **Add other AWS accounts** and enter the AWS account ID as prompted. To add another account, choose **Add another AWS account** and enter the AWS account ID. When you have added all AWS accounts, choose **Save changes**.