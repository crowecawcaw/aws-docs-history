

# Amazon EC2 Spot role for AWS PCS
<a name="spot-role"></a>

If you want to create an AWS PCS compute node group that uses **Spot** as its purchase option, you must also have the **AWSServiceRoleForEC2Spot** service-linked role in your AWS account. You can use the following AWS CLI command to create the role. For more information, see [Create a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) and [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *AWS Identity and Access Management User Guide*.

```
aws iam create-service-linked-role --aws-service-name spot.amazonaws.com
```

**Note**  
 You receive the following error if your AWS account already has an `AWSServiceRoleForEC2Spot` IAM role.   

```
  An error occurred (InvalidInput) when calling the CreateServiceLinkedRole operation: Service role name AWSServiceRoleForEC2Spot has been taken in this account, please try a different suffix.
```