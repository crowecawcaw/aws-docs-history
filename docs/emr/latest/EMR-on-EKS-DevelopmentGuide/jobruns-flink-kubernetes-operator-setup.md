# Setting up the Flink Kubernetes

operator for Amazon EMR on EKS

Complete the following tasks to get set up before you install the Flink Kubernetes
operator on Amazon EKS. If you've already signed up for Amazon Web Services (AWS) and have used Amazon EKS, you
are almost ready to use Amazon EMR on EKS. Complete the following tasks to get set up for the Flink
operator on Amazon EKS. If you've already completed any of the prerequisites, you can skip those
and move on to the next one.

- [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  – If you've already installed the AWS CLI, confirm that you have the
  latest version.
- [Set up kubectl and eksctl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
  – eksctl is a command line tool that you use to communicate with Amazon EKS.
- [Install Helm](../../../eks/latest/userguide/helm.md "../../../eks/latest/userguide/helm.md") – The Helm package manager for Kubernetes helps
  you install and manage applications on your Kubernetes cluster.
- [Get started with Amazon EKS – eksctl](../../../eks/latest/userguide/getting-started-eksctl.md "../../../eks/latest/userguide/getting-started-eksctl.md")
  – Follow the steps to create a new Kubernetes cluster
  with nodes in Amazon EKS.
- [Choose an Amazon EMR release
  label](jobruns-flink-security-release-versions.md "jobruns-flink-security-release-versions.md") (release 6.13.0 or higher) – the Flink Kubernetes
  operator is supported with Amazon EMR releases 6.13.0 and higher.
- [Enable IAM Roles for
  Service Accounts (IRSA) on the Amazon EKS cluster](setting-up-enable-IAM.md "setting-up-enable-IAM.md").
- [Create a job
  execution role](creating-job-execution-role.md "creating-job-execution-role.md").
- [Update the trust policy
  of the job execution role](setting-up-trust-policy.md "setting-up-trust-policy.md") .
- Create an operator execution role. This step is optional. You can use the same role
  for Flink jobs and operator. If you want to have a different IAM role for your operator,
  you can create a separate role.
- Update the trust policy of the operator execution role. You must explicitly add one
  trust policy entry for the roles you want to use for the Amazon EMR Flink Kubernetes operator
  service account. You can follow this example format:

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
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "aws:userid": "system:serviceaccount:emr:emr-containers-sa-flink-operator"
 }
 },
 "Sid": "AllowSTSAssumerolewithwebidentity"
 }
 ]
}`

```
