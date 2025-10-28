# Step 2: Create an IAM role granting access to create topics on the Amazon MSK cluster

In this step, you perform two tasks. The first task is to create an IAM policy that grants access to create topics on the cluster and to send data to those topics. The second task is to create an IAM role and associate this policy with it. In a later step, you create a client machine that assumes this role and uses it to create a topic on the cluster and to send data to that topic.

###### To create an IAM policy that makes it possible to create topics and write to them

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In **Policy editor**, choose **JSON**, and then replace the JSON in the editor window with the following JSON.

In the following example, replace the following:

    * `region` with the code of the AWS Region where you created your cluster.
    * Example account ID, `123456789012`, with your AWS account ID.
    * `MSKTutorialCluster` and `MSKTutorialCluster`/`7d7131e1-25c5-4e9a-9ac5-ea85bee4da11-14`, with the name of your cluster and its ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:Connect",
 "kafka-cluster:AlterCluster",
 "kafka-cluster:DescribeCluster"
 ],
 "Resource": [
 "arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`MSKTutorialCluster`/`7d7131e1-25c5-4e9a-9ac5-ea85bee4da11-14`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:*Topic*",
 "kafka-cluster:WriteData",
 "kafka-cluster:ReadData"
 ],
 "Resource": [
 "arn:aws:kafka:`us-east-1`:`123456789012`:topic/`MSKTutorialCluster`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:AlterGroup",
 "kafka-cluster:DescribeGroup"
 ],
 "Resource": [
 "arn:aws:kafka:`us-east-1`:`123456789012`:group/`MSKTutorialCluster`/*"
 ]
 }
 ]
}`

```

For instructions about how to write secure policies, see [IAM access control](iam-access-control.md "iam-access-control.md"). 5. Choose **Next**. 6. On the **Review and create** page, do the following:

    1. For **Policy name**, enter a descriptive name, such as `msk-tutorial-policy`.
    2. In **Permissions defined in this policy**, review and/or edit the permissions defined in your policy.
    3. (Optional) To help identify, organize, or search for the policy, choose **Add new tag** to add tags as key-value pairs. For example, add a tag to your policy with the key-value pair of `Environment` and `Test`.


    For more information about using tags, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the *IAM User Guide*.

7. Choose **Create policy**.

###### To create an IAM role and attach the policy to it

1.  On the navigation pane, choose **Roles**, and then choose **Create role**.
2.  On the **Select trusted entity** page, do the following:
    1. For **Trusted entity type**, choose **AWS service**.
    2. For **Service or use case**, choose **EC2**.
    3. Under **Use case**, choose **EC2**.

3.  Choose **Next**.
4.  On the **Add permissions** page, do the following:
    1. In the search box under **Permissions policies**, enter the name of the policy that you previously created for this tutorial. Then, choose the box to the left of the policy name.
    2. (Optional) Set a [permissions boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but not service-linked roles. For information about setting a permissions boundary, see [Creating roles and attaching policies (console)](../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md "../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md") in the _IAM User Guide_.

5.  Choose **Next**.
6.  On the **Name, review, and create** page, do the following:
    1. For **Role name**, enter a descriptive name, such as `msk-tutorial-role`.

    ###### Important

    When you name a role, note the following:

        * Role names must be unique within your AWS account, and can't be made unique by case.


        For example, don't create roles named both `PRODROLE` and `prodrole`. When a role name is used in a policy or as part of an ARN, the role name is case sensitive, however when a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive.
        * You can't edit the name of the role after it's created because other entities might reference the role.

    2. (Optional) For **Description**, enter a description for the role.
    3. (Optional) To edit the use cases and permissions for the role, in **Step 1: Select trusted entities** or **Step 2: Add permissions** sections, choose **Edit**.
    4. (Optional) To help identify, organize, or search for the role, choose **Add new tag** to add tags as key-value pairs. For example, add a tag to your role with the key-value pair of `ProductManager` and `John`.

    For more information about using tags, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.

7.  Review the role, and then choose **Create role**.
    **Next Step**

[Step 3: Create a client machine](create-client-machine.md "create-client-machine.md")
