# Create an instance profile for AWS PCS

Compute node groups require an instance profile when they are created. If you use the
AWS Management Console to create a role for Amazon EC2, the console automatically creates an instance profile and
gives it the same name as the role. For more information, see [Using instance
profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") in the _AWS Identity and Access Management User Guide_.

In the following procedure, you use the AWS Management Console to create a role for
Amazon EC2, which also creates the instance profile for your compute node groups.

###### To create the role and instance profile

- Navigate to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
- Under **Access management**, choose **Policies**.
  - Choose **Create policy**.
  - Under **Specify permissions**, for **Policy editor**,
    choose **JSON**.
  - Replace the contents of the text editor with the following:

  JSON

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

  - Choose **Next**.
  - Under **Review and create**, for **Policy name**, enter
    `AWSPCS-getstarted-policy`.
  - Choose **Create policy**.

- Under **Access management**, choose **Roles**.
- Choose **Create role**.
- Under **Select trusted entity**:
  - For **Trusted entity type**, select **AWS
    service**
  - Under **Use case**, select **EC2**.
    - Then, under **Choose a use case** for the specified service, choose
      **EC2**.

  - Choose **Next**.

- Under **Add permissions**:
  - In **Permissions policies**, search for **AWSPCS-getstarted-policy**.
  - Check the box beside **AWSPCS-getstarted-policy** to add it to the role.
  - In **Permissions policies**, search for **AmazonSSMManagedInstanceCore**.
  - Check the box beside **AmazonSSMManagedInstanceCore** to add it to the role.
  - Choose **Next**.

- Under **Name, review, and create**:
  - Under **Role details**:
    - For **Role name**, enter `AWSPCS-getstarted-role`.

  - Choose **Create role**.
