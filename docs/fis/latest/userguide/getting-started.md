# Create a scheduler role

An execution role is an IAM role that AWS FIS assumes in order
to interact with EventBridge scheduler and for Event Bridge scheduler to Start FIS
Experiment. You attach permission policies to this role to grant EventBridge
Scheduler access to invoke FIS Experiment. The following steps describe how to
create a new execution role and a policy to allow EventBridge to Start an
Experiment.

######

Create scheduler role using the AWS CLI

This is IAM role that is needed for Event Bridge to be able to schedule
experiment on behalf of the customer.

1. Copy the following assume role JSON policy and save it locally as `fis-execution-role.json`. This trust policy allows EventBridge Scheduler
   to assume the role on your behalf.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "scheduler.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. From the AWS Command Line Interface (AWS CLI), enter the following command to
   create a new role. Replace `FisSchedulerExecutionRole` with the name
   you want to give this role.

```
aws iam create-role --role-name FisSchedulerExecutionRole --assume-role-policy-document file://fis-execution-role.json
```

If successful, you'll see the following output:

```
{
    "Role": {
        "Path": "/",
        "RoleName": "FisSchedulerExecutionRole",
        "RoleId": "AROAZL22PDN5A6WKRBQNU",
        "Arn": "arn:aws:iam::123456789012:role/FisSchedulerExecutionRole",
        "CreateDate": "2023-08-24T17:23:05+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "scheduler.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    }
}

```

3. To create a new policy that allows EventBridge Scheduler to invoke the
   experiment, copy the following JSON and save it locally as `fis-start-experiment-permissions.json`. The following policy allows
   EventBridge Scheduler to call the `fis:StartExperiment` action on all
   experiment templates in your account. Replace the `*` at the end of `"arn:aws:fis:*:*:experiment-template/*"`
   with the ID of your experiment template if you want to limit the role to a single experiment template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "fis:StartExperiment",
 "Resource": [
 "arn:aws:fis:*:*:experiment-template/*",
 "arn:aws:fis:*:*:experiment/*"
 ]
 }
 ]
}`

```

4. Run the following command to create the new permission policy. Replace `FisSchedulerPolicy` with the name you want to give this policy.

```
aws iam create-policy --policy-name FisSchedulerPolicy --policy-document file://fis-start-experiment-permissions.json
```

If successful, you'll see the following output. Note the policy ARN. You use
this ARN in the next step to attach the policy to our execution role.

```
{
    "Policy": {
        "PolicyName": "FisSchedulerPolicy",
        "PolicyId": "ANPAZL22PDN5ESVUWXLBD",
        "Arn": "arn:aws:iam::123456789012:policy/FisSchedulerPolicy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2023-08-24T17:34:45+00:00",
        "UpdateDate": "2023-08-24T17:34:45+00:00"
    }
}

```

5. Run the following command to attach the policy to your execution role.
   Replace `your-policy-arn` with the ARN of the policy you created in
   the previous step. Replace `FisSchedulerExecutionRole` with the name
   of your execution role.

```
aws iam attach-role-policy --policy-arn your-policy-arn --role-name FisSchedulerExecutionRole
```

The `attach-role-policy` operation doesn't return a response on
the command line. 6. You can restrict the scheduler to only run AWS FIS experiment templates that have a
specific tag value. For example, the following policy grants the `fis:StartExperiment` permission for all AWS FIS experiments, but
restricts the scheduler to only run experiment templates that are tagged `Purpose=Schedule`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "fis:StartExperiment",
 "Resource": "arn:aws:fis:*:*:experiment/*"
 },
 {
 "Effect": "Allow",
 "Action": "fis:StartExperiment",
 "Resource": "arn:aws:fis:*:*:experiment-template/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Purpose": "Schedule"
 }
 }
 }
 ]
}`

```
