# Amazon SageMaker Studio spaces

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

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

Spaces are used to manage the storage and resource needs of some Amazon SageMaker Studio
applications. Each space is composed of multiple resources and can be either private or
shared. Each space has a 1:1 relationship with an instance of an application. Every
supported application that is created gets its own space. The following applications in
Studio run on spaces:

- [Code Editor in Amazon SageMaker Studio](code-editor.md "code-editor.md")
- [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md")
- [Amazon SageMaker Studio Classic](studio.md "studio.md")
  A space is composed of the following resources:

- A storage volume.
  - For Studio Classic, the space is connected to the shared Amazon Elastic File System (Amazon EFS)
    volume for the domain.
  - For other applications, a distinct Amazon Elastic Block Store (Amazon EBS) volume is attached to
    the space. All applications are given their own Amazon EBS volume. Applications
    do not have access to the Amazon EBS volume of other applications. For more
    information about Amazon EBS volumes, see [Amazon Elastic Block Store (Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md").

- The application type of the space.
- The image that the application is based on.
  Spaces can be either private or shared:

- Private: Private spaces are scoped to a single user
  in a domain. Private spaces cannot be shared with other users. All applications that
  support spaces also support private spaces.
- Shared: Shared spaces are accessible by all users in
  the domain. For more information about
  shared spaces, see [Collaboration with shared spaces](domain-space.md "domain-space.md").
  Spaces can be created in domains that use either AWS IAM Identity Center or AWS Identity and Access Management (IAM)
  authentication. The following sections give general information about how to access spaces.
  For specific information about creating and accessing a space, see the documentation for the
  respective application type of the space that you're creating.

For information about viewing, stopping, or deleting your applications, instances, or
spaces, see [Stop and delete your Studio running
applications and spaces](studio-updated-running-stop.md "studio-updated-running-stop.md").

###### Topics

- [Launch spaces](studio-updated-spaces-access.md "studio-updated-spaces-access.md")
- [Collaboration with shared spaces](domain-space.md "domain-space.md")
