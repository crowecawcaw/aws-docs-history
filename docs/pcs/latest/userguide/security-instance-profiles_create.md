# Create an instance profile for AWS PCS

AWS PCS console
Select **Create a basic profile** when you create a compute node group to have AWS PCS create one for you with the minimum required policy.

Amazon EC2 console
You can create an instance profile directly from the Amazon EC2 console. For more information, see [Using instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md")
in the _AWS Identity and Access Management User Guide_.

###### Important

Make sure to use the required prefix `AWSPCS` in the IAM role name.

AWS CLI

###### Setting up Basic instance profile using AWS CLI

###### Note

Replace `example-role` in the following examples with the name of your IAM role.

1. Create IAM role with `/aws-pcs/` as the path attribute
   or a name that starts with `AWSPCS`.
   1. Copy and paste the following content to a new text file named `trust_policy.json`.

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": [
    "ec2.amazonaws.com"
    ]
    },
    "Action": [
    "sts:AssumeRole"
    ]
    }
    ]
   }`

   ```

   2. Use 1 of the following commands to create the IAM role.

   ```
   aws iam create-role --path /aws-pcs/ --role-name `example-role` --assume-role-policy-document file://trust_policy.json
   ```

   or

   ```
   aws iam create-role --role-name `AWSPCS-example-role` --assume-role-policy-document file://trust_policy.json
   ```

2. **Attach permissions.**
   1. Copy and paste the following content to a new text file named `policy_document.json`.

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Action": [
    "pcs:RegisterComputeNodeGroupInstance"
    ],
    "Resource": "*",
    "Effect": "Allow"
    }
    ]
   }`

   ```

   2. Attach the policy document to the role. This command attaches the policy as an inline policy.

   ```
   aws iam put-role-policy \
       --role-name `example-role` \
       --policy-name pcsRegisterInstancePolicy \
       --policy-document file://policy_document.json
   ```

3. **Create an instance profile.
   Replace `example-profile` with the name
   of your instance profile.**

```
aws iam create-instance-profile --instance-profile-name `example-profile`
```

4. **Associate the IAM role with the instance profile.**

```
aws iam add-role-to-instance-profile \
   --instance-profile-name `example-profile` \
   --role-name `example-role`
```
