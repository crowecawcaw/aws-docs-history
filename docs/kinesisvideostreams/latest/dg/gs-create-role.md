# Create an IAM role

The role that you create in this step can be assumed by AWS IoT in order to obtain
temporary credentials from the AWS Security Token Service (AWS STS). This is done when performing
credential authorization requests from the Amazon Kinesis Video Streams Edge Agent.

###### Create the service role for Amazon Kinesis Video Streams (IAM console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**, and then choose **Create
   role**.
3. Choose the **Custom trust policy** role type and paste
   the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {
 "Service": "credentials.iot.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
}`

```

4. Select the box next to the IAM policy that you created in [Create an IAM permissions policy](gs-iam-role.md "gs-iam-role.md").
5. Choose **Next**.
6. Enter a role name or role name suffix to help you identify the purpose of
   this role.

###### Example

**Example:**
`KvsEdgeAgentRole` 7. (Optional) For **Description**, enter a description for
the new role. 8. (Optional) Add metadata to the role by attaching tags as key/value
pairs.

For more information about using tags in IAM, see [Tagging
IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the IAM User Guide. 9. Review the role and then choose **Create role**.
