# Step 4: Create an IAM instance

profile for your Amazon EC2 instances

###### Note

If you are using the Amazon ECS or AWS Lambda
compute platform , skip this step.

Your Amazon EC2 instances need permission to access the Amazon S3 buckets or GitHub repositories where
the applications are stored. To launch Amazon EC2 instances that are compatible with CodeDeploy, you must
create an additional IAM role, an _instance profile_. These instructions
show you how to create an IAM instance profile to attach to your Amazon EC2 instances. This role
gives the CodeDeploy agent permission to access the Amazon S3 buckets or GitHub repositories where your applications
are stored.

You can create an IAM instance profile with the AWS CLI, the IAM console, or the IAM
APIs.

###### Note

You can attach an IAM instance profile to an Amazon EC2 instance as you launch it or to a
previously launched instance. For more information, see [Instance profiles](../../../IAM/latest/UserGuide/roles-usingrole-instanceprofile.md "../../../IAM/latest/UserGuide/roles-usingrole-instanceprofile.md").

###### Topics

- [Create an IAM instance
  profile for your Amazon EC2 instances (CLI)](#getting-started-create-iam-instance-profile-cli "#getting-started-create-iam-instance-profile-cli")
- [Create an IAM instance
  profile for your Amazon EC2 instances (console)](#getting-started-create-iam-instance-profile-console "#getting-started-create-iam-instance-profile-console")

## Create an IAM instance

profile for your Amazon EC2 instances (CLI)

In these steps, we assume you have already followed the instructions in the first three
steps of [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md").

1. On your development machine, create a text file named
   `CodeDeployDemo-EC2-Trust.json`. Paste the following content,
   which allows Amazon EC2 to work on your behalf:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ec2.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "ec2.cn-north-1.amazonaws.com",
 "ec2.cn-northwest-1.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. In the same directory, create a text file named
   `CodeDeployDemo-EC2-Permissions.json`. Paste the following
   content:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

###### Note

We recommend that you restrict this policy to only those Amazon S3 buckets your Amazon EC2
instances must access. Make sure to give access to the Amazon S3 buckets that contain the
CodeDeploy agent. Otherwise, an error might occur when the CodeDeploy agent is installed or updated
on the instances. To grant the IAM instance profile access to only some CodeDeploy resource kit
buckets in Amazon S3, use the following policy, but remove the lines for buckets you want to
prevent access to:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:Get*",
        "s3:List*"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket/*",
        "arn:aws:s3:::aws-codedeploy-us-east-2/*",
        "arn:aws:s3:::aws-codedeploy-us-east-1/*",
        "arn:aws:s3:::aws-codedeploy-us-west-1/*",
        "arn:aws:s3:::aws-codedeploy-us-west-2/*",
        "arn:aws:s3:::aws-codedeploy-ca-central-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-west-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-west-2/*",
        "arn:aws:s3:::aws-codedeploy-eu-west-3/*",
        "arn:aws:s3:::aws-codedeploy-eu-central-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-central-2/*",
        "arn:aws:s3:::aws-codedeploy-eu-north-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-south-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-south-2/*",
        "arn:aws:s3:::aws-codedeploy-il-central-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-east-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-northeast-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-northeast-2/*",
        "arn:aws:s3:::aws-codedeploy-ap-northeast-3/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-2/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-3/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-4/*",
        "arn:aws:s3:::aws-codedeploy-ap-south-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-south-2/*",
        "arn:aws:s3:::aws-codedeploy-me-central-1/*",
        "arn:aws:s3:::aws-codedeploy-me-south-1/*",
        "arn:aws:s3:::aws-codedeploy-sa-east-1/*"
      ]
    }
  ]
}
```

###### Note

If you want to use [IAM authorization](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-authorization "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-authorization") or Amazon Virtual Private Cloud (VPC) endpoints with CodeDeploy, you will need
to add more permissions. See [Use CodeDeploy with
Amazon Virtual Private Cloud](vpc-endpoints.md "vpc-endpoints.md") for more information. 3. From the same directory, call the **create-role** command to create an
IAM role named `CodeDeployDemo-EC2-Instance-Profile`, based on the
information in the first file:

###### Important

Be sure to include `file://` before the file name. It is required in this
command.

```
aws iam create-role --role-name CodeDeployDemo-EC2-Instance-Profile --assume-role-policy-document file://CodeDeployDemo-EC2-Trust.json
```

4. From the same directory, call the **put-role-policy** command to give
   the role named `CodeDeployDemo-EC2-Instance-Profile` the permissions based on
   the information in the second file:

###### Important

Be sure to include `file://` before the file name. It is required in this
command.

```
aws iam put-role-policy --role-name CodeDeployDemo-EC2-Instance-Profile --policy-name CodeDeployDemo-EC2-Permissions --policy-document file://CodeDeployDemo-EC2-Permissions.json
```

5. Call the **attach-role-policy** to give the role Amazon EC2 Systems Manager permissions
   so that SSM can install the CodeDeploy agent. This policy is not needed if you plan to
   install the agent from the public Amazon S3 bucket with the command line. Learn more about
   [installing the
   CodeDeploy agent](codedeploy-agent-operations-install.md "codedeploy-agent-operations-install.md").

```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore --role-name CodeDeployDemo-EC2-Instance-Profile
```

6. Call the **create-instance-profile** command followed by the
   **add-role-to-instance-profile** command to create an IAM instance
   profile named `CodeDeployDemo-EC2-Instance-Profile`. The instance
   profile allows Amazon EC2 to pass the IAM role named
   `CodeDeployDemo-EC2-Instance-Profile` to an Amazon EC2 instance when the
   instance is first launched:

```
aws iam create-instance-profile --instance-profile-name CodeDeployDemo-EC2-Instance-Profile
aws iam add-role-to-instance-profile --instance-profile-name CodeDeployDemo-EC2-Instance-Profile --role-name CodeDeployDemo-EC2-Instance-Profile
```

If you need to get the name of the IAM instance profile, see [list-instance-profiles-for-role](../../../cli/latest/reference/iam/list-instance-profiles-for-role.md "../../../cli/latest/reference/iam/list-instance-profiles-for-role.md") in the IAM section of the _AWS CLI Reference_.

You've now created an IAM instance profile to attach to your Amazon EC2 instances. For more
information, see [IAM roles for
Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md") in the _Amazon EC2 User Guide_.

## Create an IAM instance

profile for your Amazon EC2 instances (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the IAM console, in the navigation pane, choose **Policies**,
   and then choose **Create policy**.
3. On the **Specify permissions** page, choose
   **JSON**.
4. Remove the example `JSON` code.
5. Paste the following code:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

###### Note

We recommend that you restrict this policy to only those Amazon S3 buckets your Amazon EC2
instances must access. Make sure to give access to the Amazon S3 buckets that contain the
CodeDeploy agent. Otherwise, an error might occur when the CodeDeploy agent is installed or updated
on the instances. To grant the IAM instance profile access to only some CodeDeploy resource kit
buckets in Amazon S3, use the following policy, but remove the lines for buckets you want to
prevent access to:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:Get*",
        "s3:List*"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket/*",
        "arn:aws:s3:::aws-codedeploy-us-east-2/*",
        "arn:aws:s3:::aws-codedeploy-us-east-1/*",
        "arn:aws:s3:::aws-codedeploy-us-west-1/*",
        "arn:aws:s3:::aws-codedeploy-us-west-2/*",
        "arn:aws:s3:::aws-codedeploy-ca-central-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-west-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-west-2/*",
        "arn:aws:s3:::aws-codedeploy-eu-west-3/*",
        "arn:aws:s3:::aws-codedeploy-eu-central-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-central-2/*",
        "arn:aws:s3:::aws-codedeploy-eu-north-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-south-1/*",
        "arn:aws:s3:::aws-codedeploy-eu-south-2/*",
        "arn:aws:s3:::aws-codedeploy-il-central-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-east-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-northeast-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-northeast-2/*",
        "arn:aws:s3:::aws-codedeploy-ap-northeast-3/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-2/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-3/*",
        "arn:aws:s3:::aws-codedeploy-ap-southeast-4/*",
        "arn:aws:s3:::aws-codedeploy-ap-south-1/*",
        "arn:aws:s3:::aws-codedeploy-ap-south-2/*",
        "arn:aws:s3:::aws-codedeploy-me-central-1/*",
        "arn:aws:s3:::aws-codedeploy-me-south-1/*",
        "arn:aws:s3:::aws-codedeploy-sa-east-1/*"
      ]
    }
  ]
}
```

###### Note

If you want to use [IAM authorization](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-authorization "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-authorization") or Amazon Virtual Private Cloud (VPC) endpoints with CodeDeploy, you will need
to add more permissions. See [Use CodeDeploy with
Amazon Virtual Private Cloud](vpc-endpoints.md "vpc-endpoints.md") for more information. 6. Choose **Next**. 7. On the **Review and create** page, in the **Policy
name** box, type
`CodeDeployDemo-EC2-Permissions`. 8. (Optional) For **Description**, type a description for the policy. 9. Choose **Create policy**. 10. In the navigation pane, choose **Roles**, and then choose
**Create role**. 11. Under **Use case**, choose the
**EC2** use case. 12. Choose **Next**. 13. In the list of policies, select the check box next to the policy you just created
(**CodeDeployDemo-EC2-Permissions**). If necessary, use the search box
to find the policy. 14. To use Systems Manager to install or configure the CodeDeploy agent, select the check box
next to **AmazonSSMManagedInstanceCore**. This AWS managed policy
enables an instance to use Systems Manager service core functionality. If necessary, use
the search box to find the policy. This policy is not needed if you plan to install the
agent from the public Amazon S3 bucket with the command line. Learn more about [installing the CodeDeploy
agent](codedeploy-agent-operations-install.md "codedeploy-agent-operations-install.md"). 15. Choose **Next**. 16. On the **Name, review, and create** page, in **Role name**,
enter a name for the service role (for example,
`CodeDeployDemo-EC2-Instance-Profile`), and then choose **Create role**.

You can also enter a description for this service role in
**Role description**.

You've now created an IAM instance profile to attach to your Amazon EC2 instances. For more
information, see [IAM roles for
Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md") in the _Amazon EC2 User Guide_.
