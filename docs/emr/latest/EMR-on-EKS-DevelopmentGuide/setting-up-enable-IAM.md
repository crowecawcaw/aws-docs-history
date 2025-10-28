# Option 1: Enable EKS Pod Identity on the EKS Cluster

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles
provide credentials to Amazon EC2 instances. Amazon EKS Pod Identity provides credentials to your workloads with an additional EKS Auth API and an agent
pod that runs on each node.

Amazon EMR on EKS starts to support EKS pod identity since emr-7.3.0 release for the StartJobRun submission model.

For more information on EKS pod identities, refer to [Understand how EKS Pod
Identity works](../../../eks/latest/userguide/pod-id-how-it-works.md "../../../eks/latest/userguide/pod-id-how-it-works.md").

## Why EKS Pod Identities?

As part of EMR setup, the Job Execution Role needs to establish trust boundaries between an IAM role and service accounts in a
specific namespace (of EMR virtual clusters). With IRSA, this was achieved by updating the trust policy of the EMR Job Execution Role. However, due
to the 4096 character hard-limit on IAM trust policy length, there was a constraint to share a single Job Execution IAM Role across a maximum of twelve (12) EKS clusters.

With EMR’s support for Pod Identities, the trust boundary between IAM roles and service accounts are now being managed by the EKS team through EKS pod identity’s association APIs.

###### Note

The security boundary for EKS pod identity is still on service account level, not on pod level.

## Pod Identity Considerations

For information on the Pod Identity Limitations,
see [EKS Pod Identity considerations](../../../eks/latest/userguide/pod-identities.md#pod-id-considerations "../../../eks/latest/userguide/pod-identities.md#pod-id-considerations").

## Prepare EKS Pod Identity in EKS Cluster

### Check if the required permission exists in NodeInstanceRole

The node role `NodeInstanceRole` needs a permission for the agent to do the `AssumeRoleForPodIdentity` action in the EKS Auth API. You
can add the following to the [AmazonEKSWorkerNodePolicy](../../../aws-managed-policy/latest/reference/security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksworkernodepolicy "../../../aws-managed-policy/latest/reference/security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksworkernodepolicy"), which is defined in the Amazon EKS User
Guide, or use a custom policy.

If your EKS cluster was created with eksctl version higher than **0.181.0**, the AmazonEKSWorkerNodePolicy, including the required `AssumeRoleForPodIdentity` permission,
will be attached to the node role automatically. If the permission is not present, manually add the following permission to AmazonEKSWorkerNodePolicy that allows assuming a role for
pod identity. This permission is needed by the EKS pod identity agent to retrieve credentials for pods.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "eks-auth:AssumeRoleForPodIdentity"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEKSAUTHAssumeroleforpodidentity"
 }
 ]
}`

```

### Create EKS pod identity agent add-on

Use the following command to create EKS Pod Identity Agent add-on with the latest version:

```
aws eks create-addon --cluster-name cluster-name --addon-name eks-pod-identity-agent

kubectl get pods -n kube-system | grep 'eks-pod-identity-agent'
```

Use the following steps to create EKS Pod Identity Agent add-on from the Amazon EKS console:

1. Open the Amazon EKS console: [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left navigation pane, select **Clusters**, and then select the name of the cluster that you want to
   configure the EKS Pod Identity Agent add-on for.
3. Choose the **Add-ons** tab.
4. Choose **Get more add-ons**.
5. Select the box in the top right of the add-on box for EKS Pod Identity Agent and then choose **Next**.
6. On the **Configure selected add-ons settings** page, select any version in the **Version** drop-down list.
7. (Optional) Expand **Optional configuration settings** to enter additional configuration. For example, you can provide an alternative container
   image location and `ImagePullSecrets`. The JSON Schema with accepted keys is shown in **Add-on configuration schema**.

Enter the configuration keys and values in **Configuration values**. 8. Choose **Next**. 9. Confirm that the agent pods are running on your cluster via the CLI.

`kubectl get pods -n kube-system | grep 'eks-pod-identity-agent'`

An example output is as followings:

```
NAME                              READY   STATUS    RESTARTS      AGE
eks-pod-identity-agent-gmqp7      1/1     Running   1 (24h ago)   24h
eks-pod-identity-agent-prnsh      1/1     Running   1 (24h ago)   24h
```

This sets up a new DaemonSet in the `kube-system` namespace. The Amazon EKS Pod Identity Agent, running on each EKS node, uses
the [AssumeRoleForPodIdentity](../../../eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.md "../../../eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.md") action to retrieve temporary credentials from the EKS
Auth API. These credentials are then made available for the AWS SDKs that you run inside your containers.

For more information, check the pre-requisite in the public document: [Set up the Amazon EKS Pod Identity
Agent](../../../eks/latest/userguide/pod-id-agent-setup.md "../../../eks/latest/userguide/pod-id-agent-setup.md").

## Create a Job Execution Role

### Create or update job execution role that allows

EKS Pod Identity

To run workloads with Amazon EMR on EKS, you need to create an IAM role. We refer to this role as the job execution role in this documentation. For more information
about how to create the IAM role, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the user Guide.

Additionally, you must create an IAM policy that specifies the necessary permissions for the job execution role and then attach this policy to the role to
enable EKS Pod Identity.

For example, you have the following job execution role. For more information, see [Create a job execution role](creating-job-execution-role.md "creating-job-execution-role.md").

```
arn:aws:iam::111122223333:role/PodIdentityJobExecutionRole
```

###### Important

Amazon EMR on EKS automatically creates Kubernetes Service Accounts, based on your job execution role name. Ensure the role name is not too
long, as your job may fail if the combination of `cluster_name`, `pod_name`, and `service_account_name` exceeds
the length limit.

**Job Execution Role Configuration** – Ensure the job execution role is created with the below trust permission for
EKS Pod Identity. To update an existing job execution role, configure it to trust the following EKS service principal as an additional permission in the
trust policy. This trust permission can co-exist with existing IRSA trust policies.

```
cat >trust-relationship.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
            "Effect": "Allow",
            "Principal": {
                "Service": "pods.eks.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ]
        }
    ]
}
EOF
```

**User Permission**: Users require the `iam:PassRole` permission to execute `StartJobRun` API calls or submit jobs. This permission
enables users to pass the job execution role to EMR on EKS. Job administrators should have the permission by default.

Below is the permission needed for a user:

```
{
    "Effect": "Allow",
    "Action": "iam:PassRole",
    "Resource": "arn:aws:iam::111122223333:role/PodIdentityJobExecutionRole",
    "Condition": {
        "StringEquals": {
            "iam:PassedToService": "pods.eks.amazonaws.com"
        }
    }
}
```

To further restrict the user access to specific EKS clusters, add the AssociatedResourceArn attribute filter to the IAM policy. It limits the role
assumption to authorized EKS clusters, strengthening your resource-level security controls.

```
"Condition": {
        "ArnLike": {
            "iam:AssociatedResourceARN": [
                "arn:aws:eks:us-west-2:111122223333:cluster/*"
            ]
        }
```

## Set up EKS pod identity associations

### Prerequisite

Make sure the IAM Identity creating the pod identity association, such as an EKS admin user, has the permission `eks:CreatePodIdentityAssociation`
and `iam:PassRole`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "eks:CreatePodIdentityAssociation"
 ],
 "Resource": [
 "arn:aws:eks:*:*:cluster/*"
 ],
 "Sid": "AllowEKSCreatepodidentityassociation"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "pods.eks.amazonaws.com"
 }
 },
 "Sid": "AllowIAMPassrole"
 }
 ]
}`

```

### Create Associations for the role and EMR service account

Create EMR role associations through the AWS CLI
When you submit a job to a Kubernetes namespace, an administrator must create associations between the job execution role and the identity of the EMR
managed service account. Note that the EMR managed service account is automatically created at job submission, scoped to the namespace where
the job is submitted.

With the AWS CLI (above version 2.24.0), run the following command to create role associations with
pod identity.

Run the following command to create role associations with pod identity:

```
aws emr-containers create-role-associations \
        --cluster-name mycluster \
        --namespace mynamespace \
        --role-name JobExecutionRoleIRSAv2
```

Note:

- Each cluster can have a limit of 1,000 associations. Each job execution role - namespace mapping will require 3
  associations for job submitter, driver and executor pods.
- You can only associate roles that are in the same AWS account as the cluster. You can delegate access from another account
  to the role in this account that you configure for EKS Pod Identities to use. For a tutorial about delegating access and `AssumeRole`,
  see [IAM tutorial: Delegate access across AWS accounts
  using IAM roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md").

Create EMR role associations through Amazon EKS
EMR creates service account with certain naming pattern when a job is submitted. To make manual associations or integrate this workflow with the AWS SDK, follow
these steps:

Construct Service Account Name:

```
emr-containers-sa-spark-%(SPARK_ROLE)s-%(AWS_ACCOUNT_ID)s-%(BASE36_ENCODED_ROLE_NAME)s
```

The below examples creates a role associations for a sample Job execution role JobExecutionRoleIRSAv2.

**Example Role Associations:**

```
RoleName: JobExecutionRoleIRSAv2
Base36EncodingOfRoleName: 2eum5fah1jc1kwyjc19ikdhdkdegh1n26vbe
```

**Sample CLI command:**

```
# setup for the client service account (used by job runner pod)
# emr-containers-sa-spark-client-111122223333-2eum5fah1jc1kwyjc19ikdhdkdegh1n26vbe
aws eks create-pod-identity-association --cluster-name mycluster --role-arn arn:aws:iam::111122223333:role/JobExecutionRoleIRSAv2 --namespace mynamespace --service-account emr-containers-sa-spark-client-111122223333-2eum5fah1jc1kwyjc19ikdhdkdegh1n26vbe

# driver service account
# emr-containers-sa-spark-driver-111122223333-2eum5fah1jc1kwyjc19ikdhdkdegh1n26vbe
aws eks create-pod-identity-association --cluster-name mycluster --role-arn arn:aws:iam::111122223333:role/JobExecutionRoleIRSAv2 --namespace mynamespace --service-account emr-containers-sa-spark-driver-111122223333-2eum5fah1jc1kwyjc19ikdhdkdegh1n26vbe

# executor service account
# emr-containers-sa-spark-executor-111122223333-2eum5fah1jc1kwyjc19ikdhdkdegh1n26vbe
aws eks create-pod-identity-association --cluster-name mycluster --role-arn arn:aws:iam::111122223333:role/JobExecutionRoleIRSAv2 --namespace mynamespace --service-account emr-containers-sa-spark-executor-111122223333-2eum5fah1jc1kwyjc19ikdhdkdegh1n26vbe
```

Once you completed all the steps required for EKS pod identity, you can skip the following steps for IRSA setup:

- [Enable IAM Roles for Service Accounts (IRSA) on the EKS cluster](setting-up-enable-IAM.md "setting-up-enable-IAM.md")
- [Create a job execution role](creating-job-execution-role.md "creating-job-execution-role.md")
- [Update the trust policy of the job execution role](setting-up-trust-policy.md "setting-up-trust-policy.md")

You can skip directly to the following step: [Grant users access to Amazon EMR on EKS](setting-up-iam.md "setting-up-iam.md")

## Delete Role Associations

Whenever you delete a virtual cluster or a job execution role and you no longer want to give access to EMR to its service accounts, you
should delete the associations for the role. This is because EKS allows associations with non-existent resources (namespace and service account). Amazon EMR on EKS recommends deleting the associations
if the namespace is deleted or the role is no longer in use, to free up space for other associations.

###### Note

The lingering associations could potentially impact your ability to scale if you don’t delete them, as EKS has limitations on the number
of associations you can create (soft limit: 1000 associations per cluster). You can list pod identity associations in a given namespace to check if you
have any lingering associations that needs to be cleaned up:

```
aws eks list-pod-identity-associations --cluster-name mycluster --namespace mynamespace
```

With the AWS CLI (version 2.24.0 or higher), run the following emr-containers command to delete EMR’s role associations:

```
aws emr-containers delete-role-associations \
        --cluster-name mycluster \
        --namespace mynamespace \
        --role-name JobExecutionRoleIRSAv2
```

## Automatically Migrate Existing IRSA to Pod Identity

You can use the tool eksctl to migrate existing IAM Roles for Service Accounts (IRSA) to pod identity associations:

```
eksctl utils migrate-to-pod-identity \
    --cluster mycluster \
    --remove-oidc-provider-trust-relationship \
    --approve
```

Running the command without the `--approve` flag will only output a plan reflecting the migration steps, and no actual migration
will occur.

## Troubleshooting

### My job failed with NoClassDefinitionFound or ClassNotFound Exception

for Credentials Provider, or failed to get credentials provider.

EKS Pod Identity uses the Container Credentials Provider to retrieve the necessary credentials. If you have specified a custom credentials
provider, ensure it is working correctly. Alternatively, make sure you are using a correct AWS SDK version that supports the EKS Pod Identity. For more
information, refer to [Get started with Amazon EKS](../../../eks/latest/userguide/getting-started.md "../../../eks/latest/userguide/getting-started.md").

### Job failed with the "Failed to Retrieve Credentials Due to [x] Size Limit" error shown in

the eks-pod-identity-agent log.

EMR on EKS creates Kubernetes Service Accounts based on the job execution role name. If the role name is too long, EKS Auth will fail to retrieve credentials
because the combination of `cluster_name`, `pod_name`, and `service_account_name` exceeds the length limit. Identify which component
is taking up the most space and adjust the size accordingly.

### Job failed with "Failed to Retrieve Credentials xxx" error shown in the

eks-pod-identity log.

One possible cause of this issue could be that the EKS cluster is configured under private subnets without correctly configuring PrivateLink for the cluster.
Check if your cluster is in a private network and configure AWS PrivateLink to address the issue. For detailed instructions, refer to [Get started with Amazon EKS](../../../eks/latest/userguide/getting-started.md "../../../eks/latest/userguide/getting-started.md")..
