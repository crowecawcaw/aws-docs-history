

# Granting registry permissions for pull through cache in Amazon ECR
<a name="registry-permissions-create-pullthroughcache"></a>

Amazon ECR private registry permissions may be used to scope the permissions of individual IAM entities to use pull through cache. If an IAM entity has more permissions granted by an IAM policy than the registry permissions policy is granting, the IAM policy takes precedence.

**To create a private registry permissions policy (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry permissions statement in.

1. In the navigation pane, choose **Private registry**, choose **Features & Settings**, and then choose ** Permissions**.

1. On the **Registry permissions** page, choose **Generate statement**.

1. For each pull through cache permissions policy statement you want to create, do the following.

   1. For **Policy type**, choose **Pull through cache policy**.

   1. For **Statement id**, provide a name for the pull through cache statement policy.

   1. For **IAM entities**, specify the users, groups, or roles to include in the policy.

   1. For **Cache namespace**, select the pull through cache rule to associate the policy with.

   1. For **Repository names**, specify the repository base name to apply the rule for. For example, if you want to specify the Amazon Linux repository on Amazon ECR Public, the repository name would be ` amazonlinux`.