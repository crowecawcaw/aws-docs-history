

# Troubleshooting AWS KMS permissions
<a name="security_iam_troubleshoot"></a>

When authorizing access to a KMS key, AWS KMS evaluates the following:
+ The [key policies](determining-access-key-policy.md) of the KMS key. Every KMS key has a `default` key policy. A KMS key that is shared through AWS Resource Access Manager (AWS RAM) also has an `AWS_RAM` key policy, which AWS RAM creates and manages. AWS KMS evaluates both key policies together. For more information about how AWS KMS evaluates the two key policies, see [How permissions are evaluated](key-sharing-ram.md#key-sharing-ram-evaluation). Key policies are always defined in the AWS account and Region that owns the KMS key. 
+ All [IAM policies](determining-access-iam-policies.md) that are attached to the user or role making the request. IAM policies that govern a principal's use of a KMS key are always defined in the principal's AWS account.
+ All [grants](determining-access-grants.md) that apply to the KMS key.
+ Other types of policies that might apply to the request to use the KMS key, such as [AWS Organizations service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html#orgs_manage_policies_scp) and [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html#edit-vpc-endpoint-policy). These policies are optional and allow all actions by default, but you can use them to restrict permissions otherwise given to principals.

AWS KMS evaluates these policy mechanisms together to determine whether access to the KMS key is allowed or denied. To do this, AWS KMS uses a process similar to the one depicted in the following flowchart. The following flowchart provides a visual representation of the policy evaluation process.

![Flowchart that describes the policy evaluation process](https://docs.aws.amazon.com/kms/latest/developerguide/images/updated-kms-authz-diagram.png)


This flowchart is divided into two parts. The parts appear to be sequential, but they are typically evaluated at the same time.
+ *Use authorization* determines whether you are permitted to use a KMS key based on its key policies, IAM policies, grants, and other applicable policies.
+ *Key trust* determines whether you should trust a KMS key that you are permitted to use. In general, you trust the resources in your AWS account. But, you can also feel confident about using KMS keys in a different AWS account if a grant or IAM policy in your account allows you to use the KMS key.

You can use this flowchart to discover why a caller was allowed or denied permission to use a KMS key. You can also use it to evaluate your policies and grants. For example, the flowchart shows that a caller can be denied access by an explicit `DENY` statement, or by the absence of an explicit `ALLOW` statement, in the key policy, IAM policy, or grant.

If a KMS key has an `AWS_RAM` key policy, an explicit `Deny` statement in the `default` key policy overrides an `Allow` statement in the `AWS_RAM` key policy. For example, suppose that the `default` key policy denies `kms:Encrypt` to an account that the `AWS_RAM` key policy allows to use the KMS key. Principals in that account can't use the KMS key to encrypt data. The `AWS_RAM` key policy contains only `Allow` statements, because AWS RAM managed permissions can only allow actions. Changes to key policies are eventually consistent, so a change might take a short time to take effect. For more information about eventual consistency, see [AWS KMS eventual consistency](accessing-kms.md#programming-eventual-consistency).

If you are denied access to a KMS key that is shared through AWS RAM, also check the following:

**The resource share**  
Consumers of a resource share can use the permissions in the managed permission of the resource share, which AWS RAM adds to the `AWS_RAM` key policy. Make sure that the KMS key and the caller's account are in a resource share, and that its managed permission includes the action. If the KMS key was shared with an account outside the owner's organization, the account must accept the invitation from AWS RAM. For more information about sharing KMS keys through AWS RAM, see [Sharing KMS keys with AWS RAM](key-sharing-ram.md).

**The `AWS_RAM` key policy**  
Principals in the account that owns the KMS key can view the `AWS_RAM` key policy by calling `GetKeyPolicy` with the `PolicyName` parameter set to `AWS_RAM`. Principals in other accounts can't view the key policies of the KMS key.

**IAM policies in the consumer account**  
Like any KMS key in another account, a shared KMS key requires IAM policies in the consumer account that allow its principals to use the KMS key. The IAM policies are effective only for actions that the key's key policies allow the consumer account. For more information about IAM policies for KMS keys in other accounts, see [Step 2: Add IAM policies in the external account](key-policy-modifying-external-accounts.md#cross-account-iam-policy).

**Recent changes**  
Like other changes to AWS KMS resources, changes to a resource share, and to the `AWS_RAM` key policy that AWS RAM writes, are eventually consistent. A change might not take effect immediately. For more information about eventual consistency, see [AWS KMS eventual consistency](accessing-kms.md#programming-eventual-consistency).

The flowchart can explain some common permission scenarios.

**Topics**
+ [Example 1: User is denied access to a KMS key in their AWS account](#example-no-iam)
+ [Example 2: User assumes role with permission to use a KMS key in a different AWS account](#example-cross-acct)

## Example 1: User is denied access to a KMS key in their AWS account
<a name="example-no-iam"></a>

Alice is an IAM user in the 111122223333 AWS account. She was denied access to a KMS key in same AWS account. Why can't Alice use the KMS key?

In this case, Alice is denied access to the KMS key because there is no key policy, IAM policy, or grant that gives her the required permissions. The key policy of the KMS key allows the AWS account to use IAM policies to control access to the KMS key, but no IAM policy gives Alice permission to use the KMS key.

![Flowchart that describes the policy evaluation process](https://docs.aws.amazon.com/kms/latest/developerguide/images/kms-auth-flow-Alice.png)


Consider the relevant policies for this example.
+ The KMS key that Alice wants to use has the [default key policy](key-policy-default.md). This policy [allows the AWS account](key-policy-default.md#key-policy-default-allow-root-enable-iam) that owns the KMS key to use IAM policies to control access to the KMS key. This key policy satisfies the *Does the key policy ALLOW the callers account to use IAM policies to control access to the key?* condition in the flowchart.

------
#### [ JSON ]

****  

  ```json
  {
    "Version":"2012-10-17",		 	 	 
    "Id" : "key-test-1",
    "Statement" : [ {
      "Sid" : "DelegateToIAMPolicies",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "arn:aws:iam::{{111122223333}}:root"
      },
      "Action" : "kms:*",
      "Resource" : "*"
    } ]
  }
  ```

------
+ However, no key policy, IAM policy, or grant gives Alice permission to use the KMS key. Therefore, Alice is denied permission to use the KMS key.

## Example 2: User assumes role with permission to use a KMS key in a different AWS account
<a name="example-cross-acct"></a>

Bob is a user in account 1 (111122223333). He is allowed to use a KMS key in account 2 (444455556666) in [cryptographic operations](kms-cryptography.md#cryptographic-operations). How is this possible?

**Tip**  
When evaluating cross-account permissions, remember that the key policy is specified in the KMS key's account. The IAM policy is specified in the caller's account, even when the caller is in a different account. For details about providing cross-account access to KMS keys, see [Allowing users in other accounts to use a KMS key](key-policy-modifying-external-accounts.md).
+ The key policy for the KMS key in account 2 allows account 2 to use IAM policies to control access to the KMS key. 
+ The key policy for the KMS key in account 2 allows account 1 to use the KMS key in cryptographic operations. However, account 1 must use IAM policies to give its principals access to the KMS key.
+ An IAM policy in account 1 allows the `Engineering` role to use the KMS key in account 2 for cryptographic operations.
+ Bob, a user in account 1, has permission to assume the `Engineering` role.
+ Bob can trust this KMS key, because even though it is not in his account, an IAM policy in his account gives him explicit permission to use this KMS key.

![Flowchart that describes the policy evaluation process](https://docs.aws.amazon.com/kms/latest/developerguide/images/kms-auth-flow-Bob.png)


Consider the policies that let Bob, a user in account 1, use the KMS key in account 2.
+ The key policy for the KMS key allows account 2 (444455556666, the account that owns the KMS key) to use IAM policies to control access to the KMS key. This key policy also allows account 1 (111122223333) to use the KMS key in cryptographic operations (specified in the `Action` element of the policy statement). However, no one in account 1 can use the KMS key in account 2 until account 1 defines IAM policies that give the principals access to the KMS key.

  In the flowchart, this key policy in account 2 satisfies the *Does the key policy ALLOW the caller's account to use IAM policies to control access to the key?* condition. 

------
#### [ JSON ]

****  

  ```json
  {
      "Id": "key-policy-acct-2",
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "PermissionUseIAMpolicies",
              "Effect": "Allow",
              "Principal": {
                  "AWS": "arn:aws:iam::444455556666:root"
              },
              "Action": "kms:*",
              "Resource": "*"
          },
          {
              "Sid": "AllowAccount1UseThisKMSKeys",
              "Effect": "Allow",
              "Principal": {
                  "AWS": "arn:aws:iam::{{111122223333}}:root"
              },
              "Action": [
                  "kms:Encrypt",
                  "kms:Decrypt",
                  "kms:ReEncryptFrom",
                  "kms:ReEncryptTo",
                  "kms:GenerateDataKey",
                  "kms:GenerateDataKeyWithoutPlaintext",
                  "kms:DescribeKey"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

------
+ An IAM policy in the caller's AWS account (account 1, 111122223333) gives the principal permission to perform cryptographic operations using the KMS key in account 2 (444455556666). The `Action` element delegates to the principal the same permissions that the key policy in account 2 gave to account 1. To give these permission to the `Engineering` role in account 1, [this inline policy is embedded](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html) in the `Engineering` role.

  Cross-account IAM policies like this one are effective only when the key policy for the KMS key in account 2 gives account 1 permission to use the KMS key. Also, account 1 can only give its principals permission to perform the actions that the key policy gave to the account.

  In the flowchart, this satisfies the *Does an IAM policy allow the caller to perform this action?* condition.

------
#### [ JSON ]

****  

  ```json
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "kms:Encrypt",
                  "kms:Decrypt",
                  "kms:ReEncryptFrom",
                  "kms:ReEncryptTo",
                  "kms:GenerateDataKey",
                  "kms:GenerateDataKeyWithoutPlaintext",
                  "kms:DescribeKey"
              ],
              "Resource": [
              "arn:aws:kms:us-west-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab"
              ]
          }
      ]
  }
  ```

------
+ The last required element is the definition of the `Engineering` role in account 1. The `AssumeRolePolicyDocument` in the role allows Bob to assume the `Engineering` role.

  ```json
  {
      "Role": {
          "Arn": "arn:aws:iam::111122223333:role/Engineering",
          "CreateDate": "2019-05-16T00:09:25Z",
          "AssumeRolePolicyDocument": {
              "Version": "2012-10-17",		 	 	 
              "Statement": {
                  "Principal": {
                      "AWS": "arn:aws:iam::111122223333:user/bob"
                  },
                  "Effect": "Allow",
                  "Action": "sts:AssumeRole"
              }
          },
          "Path": "/",
          "RoleName": "Engineering",
          "RoleId": "AROA4KJY2TU23Y7NK62MV"
      }
  }
  ```