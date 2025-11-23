# Using Amazon ECR Images with Amazon EKS

You can use your Amazon ECR images with Amazon EKS.

When referencing an image from Amazon ECR, you must use the full
`registry/repository:tag` naming for the image. For example,
``aws_account_id`.dkr.ecr.`region`.amazonaws.com``/`my-repository`:`latest``.

## Required IAM permissions

If you have Amazon EKS workloads hosted on managed nodes, self-managed nodes, or AWS Fargate, review the following:

- Amazon EKS workloads hosted on managed or self-managed nodes: The Amazon EKS worker node
  IAM role (`NodeInstanceRole`) is required. The Amazon EKS worker node IAM
  role must contain the following IAM policy permissions for Amazon ECR.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer",
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

If you used `eksctl` or the CloudFormation templates in [Getting
Started with Amazon EKS](../../../eks/latest/userguide/getting-started.md "../../../eks/latest/userguide/getting-started.md") to create your cluster and worker node groups,
these IAM permissions are applied to your worker node IAM role by
default.

- Amazon EKS workloads hosted on AWS Fargate: Use the Fargate pod
  execution role, which provides your pods permission to pull images from private
  Amazon ECR repositories. For more information, see [Create a Fargate pod execution role](../../../eks/latest/userguide/fargate-getting-started.md#fargate-sg-pod-execution-role "../../../eks/latest/userguide/fargate-getting-started.md#fargate-sg-pod-execution-role").
