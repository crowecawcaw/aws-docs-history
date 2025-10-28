# Set up resources required for MSK Connect

In this step you create the following resources that you need for this getting-started
scenario:

- An Amazon S3 bucket to serve as the destination that receives data from the
  connector.
- An MSK cluster to which you will send data. The connector will then
  read the data from this cluster and send it to the destination S3 bucket.
- An IAM policy that contains the permissions to write to the destination S3 bucket.
- An IAM role that allows the connector to write to the destination S3 bucket. You'll add the IAM policy that you create to this role.
- An Amazon VPC endpoint to make it possible to send data from the Amazon VPC that has the cluster and the connector to Amazon S3.

###### To create the S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. For the name of the bucket, enter a descriptive name such as
   `amzn-s3-demo-bucket-mkc-tutorial`.
4. Scroll down and choose **Create bucket**.
5. In the list of buckets, choose the newly created bucket.
6. Choose **Create folder**.
7. Enter `tutorial` for the name of the folder, then scroll
   down and choose **Create folder**.

###### To create the cluster

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. In the left pane, under **MSK Clusters**, choose
   **Clusters**.
3. Choose **Create cluster**.
4. In **Creation method**, choose **Custom create**.
5. For the cluster name enter `mkc-tutorial-cluster`.
6. In **Cluster type**, choose **Provisioned**.
7. Choose **Next**.
8. Under **Networking**, choose an Amazon VPC. Then select the
   Availability Zones and subnets that you want to use. Remember the IDs of the
   Amazon VPC and subnets that you selected because you need them later in this
   tutorial.
9. Choose **Next**.
10. Under **Access control methods** ensure that only
    **Unauthenticated access** is selected.
11. Under **Encryption** ensure that only
    **Plaintext** is selected.
12. Continue through the wizard and then choose **Create
    cluster**. This takes you to the details page for the cluster. On
    that page, under **Security groups applied**, find the security
    group ID. Remember that ID because you need it later in this tutorial.

###### To create an IAM policy with permissions to write to the S3 bucket

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In **Policy editor**, choose **JSON**, and then replace the JSON in the editor window with the following JSON.

In the following example, replace `<amzn-s3-demo-bucket-my-tutorial>` with the name of your S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowListBucket",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`<amzn-s3-demo-bucket-my-tutorial>`"
 },
 {
 "Sid": "AllowObjectActions",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject",
 "s3:AbortMultipartUpload",
 "s3:ListMultipartUploadParts",
 "s3:ListBucketMultipartUploads"
 ],
 "Resource": "arn:aws:s3:::`<amzn-s3-demo-bucket-my-tutorial>`/*"
 }
 ]
}`

```

For instructions about how to write secure policies, see [IAM access control](iam-access-control.md "iam-access-control.md"). 5. Choose **Next**. 6. On the **Review and create** page, do the following:

    1. For **Policy name**, enter a descriptive name, such as `mkc-tutorial-policy`.
    2. In **Permissions defined in this policy**, review and/or edit the permissions defined in your policy.
    3. (Optional) To help identify, organize, or search for the policy, choose **Add new tag** to add tags as key-value pairs. For example, add a tag to your policy with the key-value pair of `Environment` and `Test`.


    For more information about using tags, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the *IAM User Guide*.

7. Choose **Create policy**.

###### To create the IAM role that can write to the destination bucket

1.  On the navigation pane of the IAM console, choose **Roles**, and then choose **Create role**.
2.  On the **Select trusted entity** page, do the following:
    1. For **Trusted entity type**, choose **AWS service**.
    2. For **Service or use case**, choose **S3**.
    3. Under **Use case**, choose **S3**.

3.  Choose **Next**.
4.  On the **Add permissions** page, do the following:
    1. In the search box under **Permissions policies**, enter the name of the policy that you previously created for this tutorial. For example, **mkc-tutorial-policy**. Then, choose the box to the left of the policy name.
    2. (Optional) Set a [permissions boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but not service-linked roles. For information about setting a permissions boundary, see [Creating roles and attaching policies (console)](../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md "../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md") in the _IAM User Guide_.

5.  Choose **Next**.
6.  On the **Name, review, and create** page, do the following:
    1. For **Role name**, enter a descriptive name, such as `mkc-tutorial-role`.

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

###### To allow MSK Connect to assume the role

1. In the IAM console, in the left pane, under **Access
   management**, choose **Roles**.
2. Find the `mkc-tutorial-role` and choose it.
3. Under the role's **Summary**, choose the **Trust
   relationships** tab.
4. Choose **Edit trust relationship**.
5. Replace the existing trust policy with the following JSON.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "kafkaconnect.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

6. Choose **Update Trust Policy**.

###### To create an Amazon VPC endpoint from the cluster's VPC to Amazon S3

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. Under **Service Name** choose the **com.amazonaws.us-east-1.s3** service and the **Gateway** type.
5. Choose the cluster's VPC and then select the box to the left of the route table that is associated with the cluster's subnets.
6. Choose **Create endpoint**.
   **Next Step**

[Create custom plugin](mkc-create-plugin.md "mkc-create-plugin.md")
