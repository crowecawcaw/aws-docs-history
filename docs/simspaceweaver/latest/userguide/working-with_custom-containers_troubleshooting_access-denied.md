End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# AccessDeniedException when

uploading your image to Amazon Elastic Container Registry (Amazon ECR)

If you get an `AccessDeniedException` error when you try to
upload your container image to Amazon ECR, your IAM identity (user or role)
might not have the necessary permissions to use Amazon ECR.
You can attach the `AmazonEC2ContainerRegistryPowerUser` AWS
managed policy to your IAM identity and try again.
For more information about how to attach a policy, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.
