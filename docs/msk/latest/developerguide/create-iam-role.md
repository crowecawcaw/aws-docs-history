# Create an IAM role for topics on MSK Serverless

cluster

In this step, you perform two tasks. The first task is to create an IAM policy that
grants access to create topics on the cluster and to send data to those topics. The
second task is to create an IAM role and associate this policy with it. In a later
step, we create a client machine that assumes this role and uses it to create a topic on
the cluster and to send data to that topic.

###### To create an IAM policy that makes it possible to create topics and write to

them

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the navigation pane, choose **Policies**.
3. Choose **Create Policy**.
4. Choose the **JSON** tab, then replace the JSON in the editor
   window with the following JSON.

In the following example, replace the following:

    * `region` with the code of the AWS Region where you created your cluster.
    * Example account ID, `123456789012`, with your AWS account ID.
    * `msk-serverless-tutorial-cluster`/`c07c74ea-5146-4a03-add1-9baa787a5b14-s3` and `msk-serverless-tutorial-cluster` with your serverless cluster ID and topic name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:Connect",
 "kafka-cluster:DescribeCluster"
 ],
 "Resource": [
 "arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`msk-serverless-tutorial-cluster`/`c07c74ea-5146-4a03-add1-9baa787a5b14-s3`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:CreateTopic",
 "kafka-cluster:WriteData",
 "kafka-cluster:DescribeTopic"
 ],
 "Resource": [
 "arn:aws:kafka:`us-east-1`:`123456789012`:topic/`msk-serverless-tutorial-cluster`/*"
 ]
 }
 ]
}`

```

For instructions about how to write secure policies, see [IAM access control](iam-access-control.md "iam-access-control.md"). 5. Choose **Next: Tags**. 6. Choose **Next: Review**. 7. For the policy name, enter a descriptive name, such as
`msk-serverless-tutorial-policy`. 8. Choose **Create policy**.

###### To create an IAM role and attach the policy to it

1. On the navigation pane, choose **Roles**.
2. Choose **Create role**.
3. Under **Common use cases**, choose **EC2**, then choose
   **Next: Permissions**.
4. In the search box, enter the name of the policy that you previously created for this tutorial.
   Then select the box to the left of the policy.
5. Choose **Next: Tags**.
6. Choose **Next: Review**.
7. For the role name, enter a descriptive name, such as
   `msk-serverless-tutorial-role`.
8. Choose **Create role**.
   **Next Step**

[Create a client machine to access MSK
Serverless cluster](create-serverless-cluster-client.md "create-serverless-cluster-client.md")
