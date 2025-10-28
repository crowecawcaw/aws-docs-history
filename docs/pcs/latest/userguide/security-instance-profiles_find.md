# Find instance profiles used with AWS PCS

1. If you don't know the exact names of your IAM roles for AWS PCS,
   use the following AWS CLI command to list the IAM roles that meet the AWS PCS name requirements.

```
aws iam list-roles --query "Roles[?starts_with(RoleName, 'AWSPCS') || contains(Path, '/aws-pcs/')].[RoleName]" --output text
```

2. Use the following AWS CLI command to list the instance profiles associated with
   a specific IAM role. Replace `role-name` with the name of an IAM role
   that meets AWS PCS name requirements.

```
aws iam list-instance-profiles-for-role --role-name `role-name`
```
