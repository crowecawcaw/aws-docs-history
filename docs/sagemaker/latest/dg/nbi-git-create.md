# Create a Notebook Instance with an Associated Git

Repository

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

You can associate Git repositories with a notebook instance when you create the
notebook instance by using the AWS Management Console, or the AWS CLI. If you want to use a CodeCommit
repository that is in a different AWS account than the notebook instance, set up
cross-account access for the repository. For information, see [Associate a CodeCommit Repository in a Different AWS
Account with a Notebook Instance](nbi-git-cross.md "nbi-git-cross.md").

###### Topics

- [Create a Notebook Instance with an
  Associated Git Repository (Console)](#nbi-git-create-console "#nbi-git-create-console")
- [Create a Notebook Instance with an
  Associated Git Repository (CLI)](nbi-git-create-cli.md "nbi-git-create-cli.md")

## Create a Notebook Instance with an

Associated Git Repository (Console)

###### To create a notebook instance and associate Git repositories in the

Amazon SageMaker AI console

1. Follow the instructions at [Create an Amazon SageMaker Notebook Instance for the
   tutorial](gs-setup-working-env.md "gs-setup-working-env.md").
2. For **Git repositories**, choose Git repositories to
   associate with the notebook instance.
   1. For **Default repository**, choose a
      repository that you want to use as your default repository. SageMaker AI
      clones this repository as a subdirectory in the Jupyter startup
      directory at `/home/ec2-user/SageMaker`. When you
      open your notebook instance, it opens in this repository. To
      choose a repository that is stored as a resource in your
      account, choose its name from the list. To add a new repository
      as a resource in your account, choose **Add a repository
      to SageMaker AI (opens the Add repository flow in a new
      window)** and then follow the instructions at Create a Notebook Instance with an
      Associated Git Repository (Console). To clone a public
      repository that is not stored in your account, choose
      **Clone a public Git repository to this notebook
      instance only**, and then specify the URL for that
      repository.
   2. For **Additional repository 1**, choose a
      repository that you want to add as an additional directory. SageMaker AI
      clones this repository as a subdirectory in the Jupyter startup
      directory at `/home/ec2-user/SageMaker`. To choose a
      repository that is stored as a resource in your account, choose
      its name from the list. To add a new repository as a resource in
      your account, choose **Add a repository to SageMaker AI (opens
      the Add repository flow in a new window)** and then
      follow the instructions at Create a Notebook Instance with an
      Associated Git Repository (Console). To clone a
      repository that is not stored in your account, choose
      **Clone a public Git repository to this notebook
      instance only**, and then specify the URL for that
      repository.

   Repeat this step up to three times to add up to three
   additional repositories to your notebook instance.
