

# IAM permissions required to sync an upstream registry with an Amazon ECR private registry
<a name="pull-through-cache-iam"></a>

In addition to the Amazon ECR API permissions needed to authenticate to a private registry and to push and pull images, the following additional permissions are needed to use pull through cache rules effectively.
+ `ecr:CreatePullThroughCacheRule` – Grants permission to create a pull through cache rule. This permission must be granted via an identity-based IAM policy.
+ `ecr:BatchImportUpstreamImage` – Grants permission to retrieve the external image and import it to your private registry. This permission can be granted by using the private registry permissions policy, an identity-based IAM policy, or by using the resource-based repository permissions policy. For more information about using repository permissions, see [Private repository policies in Amazon ECR](repository-policies.md).
+ `ecr:CreateRepository` – Grants permission to create a repository in a private registry. This permission is required if the repository storing the cached images doesn't already exist. This permission can be granted by either an identity-based IAM policy or the private registry permissions policy.

## Using registry permissions
<a name="pull-through-cache-registry-permissions"></a>

Amazon ECR private registry permissions may be used to scope the permissions of individual IAM entities to use pull through cache. If an IAM entity has more permissions granted by an IAM policy than the registry permissions policy is granting, the IAM policy takes precedence. For example, if user has `ecr:*` permissions granted, no additional permissions are needed at the registry level.

### To create a private registry permissions policy (AWS Management Console)
<a name="pull-through-cache-registry-permissions-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your private registry permissions statement in.

1. In the navigation pane, choose **Private registry**, **Registry permissions**.

1. On the **Registry permissions** page, choose **Generate statement**.

1. For each pull through cache permissions policy statement you want to create, do the following.

   1. For **Policy type**, choose **Pull through cache policy**.

   1. For **Statement id**, provide a name for the pull through cache statement policy.

   1. For **IAM entities**, specify the users, groups, or roles to include in the policy.

   1. For **Repository namespace**, select the pull through cache rule to associate the policy with.

   1. For **Repository names**, specify the repository base name to apply the rule for. For example, if you want to specify the Amazon Linux repository on Amazon ECR Public, the repository name would be `amazonlinux`.

### To create a private registry permissions policy (AWS CLI)
<a name="pull-through-cache-registry-permissions-cli"></a>

Use the following AWS CLI command to specify the private registry permissions using the AWS CLI.

1. Create a local file named `ptc-registry-policy.json` with the contents of your registry policy. The following example grants the `ecr-pull-through-cache-user` permission to create a repository and pull an image from Amazon ECR Public, which is the upstream source associated with the previously created pull through cache rule.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "PullThroughCacheFromReadOnlyRole",
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::{{111122223333}}:user/{{ecr-pull-through-cache-user}}"
         },
         "Action": [
           "ecr:CreateRepository",
           "ecr:BatchImportUpstreamImage"
         ],
         "Resource": "arn:aws:ecr:{{us-east-1}}:{{111122223333}}:repository/{{ecr-public}}/*"
       }
     ]
   }
   ```

------
**Important**  
The `ecr-CreateRepository` permission is only required if the repository storing the cached images doesn't already exist. For example, if the repository creation action and the image pull actions are being done by separate IAM principals such as an administrator and a developer.

1. Use the [put-registry-policy](https://docs.aws.amazon.com/cli/latest/reference/ecr/put-registry-policy.html) command to set the registry policy.

   ```
   aws ecr put-registry-policy \
        --policy-text file://{{ptc-registry.policy.json}}
   ```

## Next steps
<a name="pull-through-cache-next-steps"></a>

Once you are ready to start using pull through cache rules, the following are the next steps.
+ Create a pull through cache rule. For more information, see [Creating a pull through cache rule in Amazon ECR](pull-through-cache-creating-rule.md).
+ Create a repository creation template. A repository creation template gives you control to define the settings to use for new repositories created by Amazon ECR on your behalf during a pull through cache action. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](repository-creation-templates.md).