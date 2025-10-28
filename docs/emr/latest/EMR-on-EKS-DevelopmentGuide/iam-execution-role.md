# Using job execution roles with Amazon EMR on EKS

To use the `StartJobRun` command to submit a job run on an EKS cluster, you must
first onboard a job execution role to be used with a virtual cluster. For more information, see
[Create a job execution role](creating-job-execution-role.md "creating-job-execution-role.md") in
[Setting up Amazon EMR on EKS](setting-up.md "setting-up.md"). You can also follow the instructions
in the [Create IAM Role for job execution](https://www.eksworkshop.com/advanced/430_emr_on_eks/prereqs/#create-iam-role-for-job-execution "https://www.eksworkshop.com/advanced/430_emr_on_eks/prereqs/#create-iam-role-for-job-execution") section of the Amazon EMR on EKS Workshop.

The following permissions must be included in the trust policy for the job execution
role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRoleWithWebIdentity"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:userid": "system:serviceaccount:`NAMESPACE`:emr-containers-sa-*-*-`AWS_ACCOUNT_ID`-`BASE36_ENCODED_ROLE_NAME`"
 }
 },
 "Sid": "AllowSTSAssumerolewithwebidentity"
 }
 ]
}`

```

The trust policy in the preceding example grants permissions only to an Amazon EMR managed
Kubernetes service account with a name that matches the
`emr-containers-sa-*-*-`AWS_ACCOUNT_ID`-`BASE36_ENCODED_ROLE_NAME``
pattern. Service accounts with this pattern will be automatically created at job submission, and
scoped to the namespace where you submit the job. This trust policy allows these service
accounts to assume the execution role and get the temporary credentials of the execution role.
Service accounts from a different Amazon EKS cluster or from a different namespace within the
same EKS cluster are restricted from assuming the execution role.

You can run the following command to automatically update the trust policy in the format
given above.

```
aws emr-containers update-role-trust-policy \
       --cluster-name `cluster` \
       --namespace `namespace` \
       --role-name `iam_role_name_for_job_execution`
```

**Controlling access to the execution role**

An administrator for your Amazon EKS cluster can create a multi-tenant Amazon EMR on EKS virtual cluster
to which an IAM administrator can add multiple execution roles. Because untrusted tenants can
use these execution roles to submit jobs that run arbitrary code, you might want to restrict
those tenants so that they can't run code that gains the permissions assigned to one or more of
these execution roles. To restrict the IAM policy attached to an IAM identity, the IAM
administrator can use the optional Amazon Resource Name (ARN) condition key
`emr-containers:ExecutionRoleArn`. This condition accepts a list of execution role
ARNs that have permissions to the virtual cluster, as the following permissions policy
demonstrates.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:StartJobRun"
 ],
 "Resource": [
 "arn:aws:emr-containers:*:*:/virtualclusters/`VIRTUAL_CLUSTER_ID`"
 ],
 "Condition": {
 "ArnEquals": {
 "emr-containers:ExecutionRoleArn": [
 "arn:aws:iam::*:role/`execution_role_name_1`",
 "arn:aws:iam::*:role/`execution_role_name_2`"
 ]
 }
 },
 "Sid": "AllowEMRCONTAINERSStartjobrun"
 }
 ]
}`

```

If you want to allow all execution roles that begin with a particular prefix, such as
`MyRole`, you can replace the condition operator `ArnEquals` with the
`ArnLike` operator, and you can replace the `execution_role_arn` value
in the condition with a wildcard `*` character. For example,
`arn:aws:iam::`AWS_ACCOUNT_ID`:role/MyRole*`. All other [ARN condition keys](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN") are also supported.

###### Note

With Amazon EMR on EKS, you can't grant permissions to execution roles
based on tags or attributes. Amazon EMR on EKS doesn't support tag-based access control (TBAC) or attribute-based
access control (ABAC) for execution roles.
