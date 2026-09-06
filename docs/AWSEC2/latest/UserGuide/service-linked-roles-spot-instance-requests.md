

# Service-linked role for Spot Instance requests
<a name="service-linked-roles-spot-instance-requests"></a>

Amazon EC2 uses service-linked roles for the permissions that it requires to call other AWS services on your behalf. A service-linked role is a unique type of IAM role that is linked directly to an AWS service. Service-linked roles provide a secure way to delegate permissions to AWS services because only the linked service can assume a service-linked role. For more information, see [Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in the *IAM User Guide*.

Amazon EC2 uses the service-linked role named **AWSServiceRoleForEC2Spot** to launch and manage Spot Instances on your behalf.

## Permissions granted by AWSServiceRoleForEC2Spot
<a name="service-linked-role-permissions-granted-by-AWSServiceRoleForEC2Spot"></a>

Amazon EC2 uses **AWSServiceRoleForEC2Spot** to complete the following actions:
+ `ec2:DescribeInstances` – Describe Spot Instances
+ `ec2:StopInstances` – Stop Spot Instances
+ `ec2:StartInstances` – Start Spot Instances

## Create the service-linked role
<a name="service-linked-role-creating-for-spot"></a>

Under most circumstances, you don't need to manually create a service-linked role. Amazon EC2 creates the **AWSServiceRoleForEC2Spot** service-linked role the first time you request a Spot Instance using the console.

If you had an active Spot Instance request before October 2017, when Amazon EC2 began supporting this service-linked role, Amazon EC2 created the **AWSServiceRoleForEC2Spot** role in your AWS account. For more information, see [A New Role Appeared in My Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared) in the *IAM User Guide*.

If you use the AWS CLI or an API to request a Spot Instance, you must first ensure that this role exists.

**To create **AWSServiceRoleForEC2Spot** using the console**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. On the **Select type of trusted entity** page, choose **EC2**, **EC2 - Spot Instances**, **Next: Permissions**.

1. On the next page, choose **Next:Review**.

1. On the **Review** page, choose **Create role**.

**To create **AWSServiceRoleForEC2Spot** using the AWS CLI**  
Use the [create-service-linked-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-service-linked-role.html) command as follows.

```
aws iam create-service-linked-role --aws-service-name spot.amazonaws.com
```

If you no longer need to use Spot Instances, we recommend that you delete the **AWSServiceRoleForEC2Spot** role. After this role is deleted from your account, Amazon EC2 will create the role again if you request Spot Instances.

## Grant access to customer managed keys for use with encrypted AMIs and EBS snapshots
<a name="spot-instance-service-linked-roles-access-to-cmks"></a>

If you specify an [encrypted AMI](AMIEncryption.md) or an encrypted Amazon EBS snapshot for your Spot Instances and you use a customer managed key for encryption, you must grant the **AWSServiceRoleForEC2Spot** role permission to use the customer managed key so that Amazon EC2 can launch Spot Instances on your behalf. To do this, you must add a grant to the customer managed key, as shown in the following procedure.

When providing permissions, grants are an alternative to key policies. For more information, see [Using Grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) and [Using Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

**To grant the **AWSServiceRoleForEC2Spot** role permissions to use the customer managed key**
+ Use the [create-grant](https://docs.aws.amazon.com/cli/latest/reference/kms/create-grant.html) command to add a grant to the customer managed key and to specify the principal (the **AWSServiceRoleForEC2Spot** service-linked role) that is given permission to perform the operations that the grant permits. The customer managed key is specified by the `key-id` parameter and the ARN of the customer managed key. The principal is specified by the `grantee-principal` parameter and the ARN of the **AWSServiceRoleForEC2Spot** service-linked role.

  ```
  aws kms create-grant \
      --region {{us-east-1}} \
      --key-id arn:aws:kms:{{us-east-1}}:{{444455556666}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}} \
      --grantee-principal arn:aws:iam::{{111122223333}}:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleForEC2Spot \
      --operations "Decrypt" "Encrypt" "GenerateDataKey" "GenerateDataKeyWithoutPlaintext" "CreateGrant" "DescribeKey" "ReEncryptFrom" "ReEncryptTo"
  ```