# Troubleshooting

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

If you are having trouble with Serverless Inference, refer to the following troubleshooting tips.

## Container issues

If the container you use for a serverless endpoint is the same one you used on an instance-based endpoint,
your container may not have permissions to write files. This can happen for the following reasons:

- Your serverless endpoint fails to create or update due to a ping health check failure.
- The Amazon CloudWatch logs for the endpoint show that the container is failing to write to some file or directory due to a permissions error.

To fix this issue, you can try to add read, write, and execute permissions for
`other` on the file or directory and then rebuild the container. You can perform the
following steps to complete this process:

1. In the Dockerfile you used to build your container, add the following command: `RUN chmod
o+rwX `<file or directory name>``
2. Rebuild the container.
3. Upload the new container image to Amazon ECR.
4. Try to create or update the serverless endpoint again.
