# Tutorial: Check your account's Amazon ECS instance role

The Amazon ECS instance role and instance profile are automatically created for you in the
console first-run experience. However, you can follow these steps to check if your account
already has the Amazon ECS instance role and instance profile. The following steps also cover how to
attach the managed IAM policy.

###### Tutorial: Check for the `ecsInstanceRole` in

the IAM console

1.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane, choose **Roles**.
3.  Search the list of roles for `ecsInstanceRole`. If the role doesn't exist, use the following steps
    to create the role.

        1. Choose **Create Role**.
        2. For **Trusted entity type**, choose
         **AWS service**.
        3. For **Common use cases**, choose **EC2**.
        4. Choose **Next**.
        5. For **Permissions policies**, search for
         **AmazonEC2ContainerServiceforEC2Role**.
        6. Choose the check box next to **AmazonEC2ContainerServiceforEC2Role**,
         then choose **Next**.
        7. For **Role Name**, type `ecsInstanceRole` and choose
         **Create Role**.


        ###### Note

        If you use the AWS Management Console to create a role for Amazon EC2, the console creates an instance
         profile with the same name as the role.

    Alternatively, you can use the AWS CLI to create the `ecsInstanceRole` IAM role.
    The following example creates an IAM role with a trust policy and an AWS managed
    policy.

###### Tutorial: Create an IAM role and instance profile

(AWS CLI)

1. Create the following trust policy and save it in a text file that's named
   `ecsInstanceRole-role-trust-policy.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": { "Service": "ec2.amazonaws.com"},
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Use the [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to create the
   `ecsInstanceRole` role. Specify the trust policy file location in the
   `assume-role-policy-document` parameter.

```
`$` `aws iam create-role \
 --role-name ecsInstanceRole \
 --assume-role-policy-document file://ecsInstanceRole-role-trust-policy.json`
```

3. Use the [create-instance-profile](../../../cli/latest/reference/iam/create-instance-profile.md "../../../cli/latest/reference/iam/create-instance-profile.md") command to
   create an instance profile that's named `ecsInstanceRole`.

###### Note

You need to create roles and instance profiles as separate actions in the AWS CLI and AWS API.

```
`$` `aws iam create-instance-profile --instance-profile-name ecsInstanceRole`
```

The following is an example response.

```
{
    "InstanceProfile": {
        "Path": "/",
        "InstanceProfileName": "ecsInstanceRole",
        "InstanceProfileId": "AIPAT46P5RDITREXAMPLE",
        "Arn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceRole",
        "CreateDate": "2022-06-30T23:53:34.093Z",
        "Roles": [],    }
}
```

4. Use the [add-role-to-instance-profile](../../../cli/latest/reference/iam/add-role-to-instance-profile.md "../../../cli/latest/reference/iam/add-role-to-instance-profile.md") command to add the `ecsInstanceRole` role to
   the `ecsInstanceRole` instance profile.

```
aws iam add-role-to-instance-profile \
    --role-name ecsInstanceRole --instance-profile-name ecsInstanceRole
```

5. Use the [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command to attach the
   `AmazonEC2ContainerServiceforEC2Role` AWS managed policy to the `ecsInstanceRole`
   role.

```
`$` aws iam attach-role-policy \
    --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role \
    --role-name ecsInstanceRole
```
