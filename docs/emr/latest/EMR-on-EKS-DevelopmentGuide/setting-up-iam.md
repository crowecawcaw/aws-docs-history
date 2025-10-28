# Grant users access to Amazon EMR on EKS

For any actions that you perform on Amazon EMR on EKS, you need a corresponding IAM permission for
that action. You must create an IAM policy that allows you to perform the Amazon EMR on EKS actions
and attach the policy to the IAM user or role that you use.

This topic provides steps for creating a new policy and attaching it to a user. It also
covers the basic permissions that you need to set up your Amazon EMR on EKS environment. We recommend
that you refine the permissions to specific resources whenever possible based on your business
needs.

## Creating a new IAM policy and attaching it to a

user in the IAM console

###### Create a new IAM policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane of the IAM console, choose
   **Policies**.
3. On the **Policies** page, choose **Create
   Policy**.
4. In the **Create Policy** window, navigate to the **Edit
   JSON** tab. Create a policy document with one or more JSON statements as
   shown in the examples following this procedure. Next, choose **Review
   policy**.
5. On the **Review Policy** screen, enter your **Policy
   Name**, for example `AmazonEMROnEKSPolicy`. Enter an optional
   description, and then choose **Create policy**.

###### Attach the policy to a user or role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")
2. In the navigation pane, choose **Policies**.
3. In the list of policies, select the check box next to the policy created in the
   previous section. You can use the **Filter** menu and the search box to
   filter the list of policies.
4. Choose **Policy actions**, and then choose
   **Attach**.
5. Choose the user or role to attach the policy to. You can use the
   **Filter** menu and the search box to filter the list of principal
   entities. After choosing the user or role to attach the policy to, choose
   **Attach policy**.

## Permissions for managing virtual

clusters

To manage virtual clusters in your AWS account, create an IAM policy with the
following permissions. These permissions allow you to create, list, describe, and delete
virtual clusters in your AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "emr-containers.amazonaws.com"
 }
 },
 "Sid": "AllowIAMCreateservicelinkedrole"
 },
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:CreateVirtualCluster",
 "emr-containers:ListVirtualClusters",
 "emr-containers:DescribeVirtualCluster",
 "emr-containers:DeleteVirtualCluster"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEMRCONTAINERSCreatevirtualcluster"
 }
 ]
}`

```

Amazon EMR is integrated with Amazon EKS cluster access management (CAM),
so you can automate configuration of the necessary AuthN and AuthZ policies to run Amazon EMR Spark jobs in namespaces of Amazon EKS clusters. To do so, you must have the following permissions:

```
{
  "Effect": "Allow",
  "Action": [
    "eks:CreateAccessEntry"
  ],
  "Resource": "arn:`<AWS_PARTITION>`:eks:`<AWS_REGION>`:`<AWS_ACCOUNT_ID>`:cluster/`<EKS_CLUSTER_NAME>`"
},
{
  "Effect": "Allow",
  "Action": [
    "eks:DescribeAccessEntry",
    "eks:DeleteAccessEntry",
    "eks:ListAssociatedAccessPolicies",
    "eks:AssociateAccessPolicy",
    "eks:DisassociateAccessPolicy"
  ],
  "Resource": "arn:`<AWS_PARTITION>`:eks:`<AWS_REGION>`:`<AWS_ACCOUNT_ID>`:access-entry/`<EKS_CLUSTER_NAME>`/role/`<AWS_ACCOUNT_ID>`/AWSServiceRoleForAmazonEMRContainers/*"
}
```

For more information, see
[Automate enabling cluster access for Amazon EMR on EKS](setting-up-cluster-access.md#setting-up-cluster-access-cam-integration "setting-up-cluster-access.md#setting-up-cluster-access-cam-integration").

When the `CreateVirtualCluster` operation is invoked for the first time from
an AWS account, you also need the `CreateServiceLinkedRole` permissions to
create the service-linked role for Amazon EMR on EKS. For more information, see [Using service-linked roles for Amazon EMR on EKS](using-service-linked-roles.md "using-service-linked-roles.md").

## Permissions for submitting jobs

To submit jobs on the virtual clusters in your AWS account, create an IAM policy with
the following permissions. These permissions allow you to start, list, describe, and cancel
job runs for the all virtual clusters in your account. You should consider adding
permissions to list or describe virtual clusters, which allow you to check the state of the
virtual cluster before submitting jobs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:StartJobRun",
 "emr-containers:ListJobRuns",
 "emr-containers:DescribeJobRun",
 "emr-containers:CancelJobRun"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEMRCONTAINERSStartjobrun"
 }
 ]
}`

```

## Permissions for debugging and

monitoring

To get access to logs pushed to Amazon S3 and CloudWatch, or to view application event logs in the
Amazon EMR console, create an IAM policy with the following permissions. We recommend that you
refine the permissions to specific resources whenever possible based on your business
needs.

###### Important

If you haven't created an Amazon S3 bucket, you need to add `s3:CreateBucket`
permission to the policy statement. If you haven't created a log group, you need to add
`logs:CreateLogGroup` to the policy statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:DescribeJobRun",
 "elasticmapreduce:CreatePersistentAppUI",
 "elasticmapreduce:DescribePersistentAppUI",
 "elasticmapreduce:GetPersistentAppUIPresignedURL"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEMRCONTAINERSDescribejobrun"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowS3Getobject"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:Get*",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowLOGSGet"
 }
 ]
}`

```

For more information about how to configure a job run to push logs to Amazon S3 and CloudWatch, see
[Configure a job run to use S3 logs](emr-eks-jobs-CLI.md#emr-eks-jobs-s3 "emr-eks-jobs-CLI.md#emr-eks-jobs-s3") and [Configure a job run to use CloudWatch Logs](emr-eks-jobs-CLI.md#emr-eks-jobs-cloudwatch "emr-eks-jobs-CLI.md#emr-eks-jobs-cloudwatch").
