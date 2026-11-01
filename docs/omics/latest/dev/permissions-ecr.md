

# Amazon ECR permissions
<a name="permissions-ecr"></a>

Before you can run a workflow in a container from your private Amazon ECR repository, you create a resource policy for the repository. The policy grants permission for the HealthOmics service to use the container. You add this resource policy to each private repository referenced by the workflow. 

**Note**  
The private repository and the workflow must be in the same region.

If different AWS accounts own the workflow and the repository, you need to configure cross-account permissions.

You don't need to grant additional repository access for shared workflows. However, you can create policies that allow or deny specific workflows access to the container image.

To use the Amazon ECR pull through cache feature, you need to create a registry permission policy.

To use container images from registries that Amazon ECR pull through cache (PTC) doesn't support, you add permissions to the service role, as described in [Service role policy for non-PTC container support](#permissions-ecr-non-ptc).

The following sections describe how to configure Amazon ECR resource permissions for these scenarios. For more information about permissions in Amazon ECR, see [ Private registry permissions in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html).

**Topics**
+ [Create a resource policy for the Amazon ECR repository](#permissions-resource-policy)
+ [Running workflows with cross-account containers](#permissions-cross-account-containers)
+ [Amazon ECR policies for shared workflows](#permissions-shared-workflows)
+ [Policies for Amazon ECR pull through cache](#permissions-ecr-ptc)
+ [Service role policy for non-PTC container support](#permissions-ecr-non-ptc)
+ [Verifying that HealthOmics can pull a container image](#permissions-ecr-verify)

## Create a resource policy for the Amazon ECR repository
<a name="permissions-resource-policy"></a>

Create a resource policy to allow the HealthOmics service to run a workflow using a container in the repository. The policy grants permission for the HealthOmics service principal to access the required Amazon ECR actions.

Follow these steps to create the policy:

1. Open the [private repositories](https://console.aws.amazon.com/ecr/private-registry/repositories) page in the Amazon ECR console and select the repository you're granting access to.

1. From the side bar navigation, select **Permissions**.

1. Choose **Edit**.

1. Choose **Edit policy JSON**.

1. Add the following policy statement and then select **Save**.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "omics workflow access",
               "Effect": "Allow",
               "Principal": {
                   "Service": "omics.amazonaws.com"
               },
               "Action": [
                   "ecr:GetDownloadUrlForLayer",
                   "ecr:BatchGetImage",
                   "ecr:BatchCheckLayerAvailability"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

## Running workflows with cross-account containers
<a name="permissions-cross-account-containers"></a>

If different AWS accounts own the workflow and the container, you need to configure the following cross-account permissions: 

1. Update the Amazon ECR policy for the repository to explicitly grant permission to the account that owns the workflow. 

1. Update the service role for the account that owns the workflow to grant it access to the container image.

The following example demonstrates an Amazon ECR resource policy that grants access to the account that owns the workflow.

In this example:
+ Workflow account ID: 111122223333
+ Container repository account ID: 444455556666 
+ Container name: samtools

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "omics.amazonaws.com"
            },
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowAccessToTheServiceRoleOfTheAccountThatOwnsTheWorkflow",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/DemoCustomer"
            },
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
        }
    ]
}
```

------

To complete the setup, add the following policy statement to the service role of the account that owns the workflow. The policy grants permission for the service role to access the “samtools” container image. Make sure to replace the account numbers, container name, and region with your own values.

```
{
    "Sid": "CrossAccountEcrRepoPolicy",
    "Effect": "Allow",
    "Action": ["ecr:BatchCheckLayerAvailability", "ecr:BatchGetImage", "ecr:GetDownloadUrlForLayer"],
    "Resource": "arn:aws:ecr:us-west-2:444455556666:repository/samtools"
}
```

## Amazon ECR policies for shared workflows
<a name="permissions-shared-workflows"></a>

**Note**  
HealthOmics automatically allows a shared workflow to access the Amazon ECR repository in the workflow owner's account, while the workflow is running in the subscriber's account. You don't need to grant additional repository access for shared workflows. For more information see [Sharing HealthOmics workflows](https://docs.aws.amazon.com/omics/latest/dev/sharing-workflows.html).

By default, subscriber don’t have access to the Amazon ECR repository to use the underlying containers. Optionally, you can customize access to the Amazon ECR repository by adding condition keys to the repository's resource policy. The following sections provide example policies.

### Restrict access to specific workflows
<a name="permissions-limit-workflows"></a>

You can list individual workflows in a condition statement, so only these workflow can use containers in the repository. The **SourceArn** condition key specifies the ARN of the shared workflow. The following example grants permission for the specified workflow to use this repository. 

------
#### [ JSON ]

****  

```
{  
  "Version":"2012-10-17",		 	 	 
  "Statement": [
     {
       "Sid": "OmicsAccessPrincipal",
       "Effect": "Allow",
       "Principal": {
         "Service": "omics.amazonaws.com"
       },
       "Action": [
         "ecr:GetDownloadUrlForLayer",
         "ecr:BatchGetImage",
         "ecr:BatchCheckLayerAvailability"
       ],
       "Resource": "*",
       "Condition": {
          "StringEquals": {
             "aws:SourceArn": "arn:aws:omics:{{us-east-1}}:{{111122223333}}:workflow/1234567"
          }
       }
     }
  ]
}
```

------

### Restrict access to specific accounts
<a name="permissions-limit-users"></a>

You can list subscriber accounts in a condition statement, so that only these accounts have permission to use containers in the repository. The **SourceAccount** condition key specifies the AWS account of the subscriber. The following example grants permission for the specified account to use this repository.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "OmicsAccessPrincipal",
      "Effect": "Allow",
      "Principal": {
        "Service": "omics.amazonaws.com"
      },
      "Action": [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:BatchCheckLayerAvailability"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{111122223333}}"
        }
      }
    }
  ]
}
```

------

You can also deny Amazon ECR permissions to specific subscribers, as shown in the following example policy.

------
#### [ JSON ]

****  

```
{
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "OmicsAccessPrincipal",
              "Effect": "Allow",
              "Principal": {
                  "Service": "omics.amazonaws.com"
              },
              "Action": [
                  "ecr:GetDownloadUrlForLayer",
                  "ecr:BatchGetImage",
                  "ecr:BatchCheckLayerAvailability"
              ],
              "Resource": "*",
              "Condition": {
                "StringNotEquals": {
                  "aws:SourceAccount": "{{111122223333}}"
                }
             }  
         }
      ]
  }
```

------

## Policies for Amazon ECR pull through cache
<a name="permissions-ecr-ptc"></a>

To use Amazon ECR pull through cache, you create a registry permission policy. You also create a repository creation template, which defines the permissions for the repositories created by Amazon ECR pull through cache.

The following sections include examples of these policies. For more information about pull through cache, see [ Sync an upstream registry with an Amazon ECR private registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-private.html) in the *Amazon Elastic Container Registry User Guide*.

### Registry permission policy
<a name="permissions-reg"></a>

To use Amazon ECR pull through cache, create a registry permission policy. The registry permissions policy provides control over replication and pull through cache permissions. 

For cross-account replication, you must explictly allow each AWS account that can replicate its repositories to your registry.

By default, when you create a pull through cache rule, any IAM principal that has permission to pull images from a private registry can also use the pull through cache rule. You can use registry permissions to further scope down these permissions to specific repositories.

Add a registry permission policy to the account that owns the container image. 

In the following example, the policy allows the HealthOmics service to create repositories for each upstream registry and to initiate upstream pull requests from the created repositories.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowPTCinRegPermissions",
            "Effect": "Allow",
            "Principal": {
                "Service": "omics.amazonaws.com"
            },
            "Action": [
                "ecr:CreateRepository",
                "ecr:BatchImportUpstreamImage"
            ],
            "Resource": [
                "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/ecr-public/*",
                "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/docker-hub/*"
            ] 
        }
    ]
}
```

------

### Repository creation template
<a name="permissions-repo-template"></a>

To use pull through cache in HealthOmics, the Amazon ECR repository must have a repository creation template. The template defines configuration settings for the private repositories created for an upstream registry. 

Each template contains a repository namespace prefix, which Amazon ECR uses to match new repositories to a specific template. Templates can specify the configuration for all repository settings including resource-based access policies, tag immutability, encryption, and lifecycle policies. For more information, see [Repository creation templates](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-creation-templates.html) in the *Amazon Elastic Container Registry User Guide*.

In the following example, the policy allows the HealthOmics service to initiate upstream pull requests from the upstream repositories.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "PTCRepoCreationTemplate",
            "Effect": "Allow",
            "Principal": {
                "Service": "omics.amazonaws.com"
            },
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Policies for cross-account Amazon ECR access
<a name="permissions-cross-account"></a>

For cross-account access, the owner of the private repository updates the registry permission policy and the repository creation template to allow access for the other account and that account's run role.

In the registry permission policy, add a policy statement to allow the other account's run role to access the Amazon ECR actions:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCrossAccountPTCinRegPermissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{123456789012}}:role/{{RUN_ROLE}}"},
            "Action": [
                "ecr:CreateRepository",
                "ecr:BatchGetImage",
                "ecr:BatchImportUpstreamImage"
            ],
            "Resource": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/{{path}}/*" 
        }
    ]
}
```

------

In the repository creation template, add a policy statement to allow the other account's run role to access the new container images. Optionally, you can add condition statements to limit access to specific workflows:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCrossAccountPTCinRepoCreationTemplate",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/{{RUN_ROLE}}"},
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:omics:us-east-1:{{444455556666}}:workflow/{{WORKFLOW_ID}}",
                    "aws:SourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```

------

Add permissions for two additional actions (CreateRepository and BatchImportUpstreamImage) in the run role and specify the resource that the run role can access. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CrossAccountPTCRunRolePolicy",
            "Effect": "Allow",
            "Action": [
                "ecr:CreateRepository",
                "ecr:BatchImportUpstreamImage",       
                "ecr:BatchCheckLayerAvailability", 
                "ecr:BatchGetImage", 
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage"
            ],
            "Resource": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}::repository/{path}/*"
        }
    ]
}
```

------

## Service role policy for non-PTC container support
<a name="permissions-ecr-non-ptc"></a>

With non-PTC container support, HealthOmics uses the service role that you pass to `StartRun` to copy images into your Amazon ECR repositories. In addition to the permissions in [Service roles for AWS HealthOmics](permissions-service.md), the service role needs permission to:
+ Create the destination repository if it doesn't exist (`ecr:CreateRepository`).
+ Check for a repository policy, and attach one if the repository has none (`ecr:GetRepositoryPolicy`, `ecr:SetRepositoryPolicy`).
+ Push the image (`ecr:InitiateLayerUpload`, `ecr:UploadLayerPart`, `ecr:CompleteLayerUpload`, `ecr:PutImage`).
+ Read the registry credential (`secretsmanager:GetSecretValue`).

The following example policy grants these permissions. Replace the Region, the account ID, {{ecr-repository-prefix}}, and the secret ARN with your values. Use the `ecrRepositoryPrefix` from your registry mapping.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EcrCopiedImages",
      "Effect": "Allow",
      "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchCheckLayerAvailability",
        "ecr:InitiateLayerUpload",
        "ecr:UploadLayerPart",
        "ecr:CompleteLayerUpload",
        "ecr:PutImage",
        "ecr:DescribeImages",
        "ecr:CreateRepository",
        "ecr:GetRepositoryPolicy",
        "ecr:SetRepositoryPolicy"
      ],
      "Resource": "arn:aws:ecr:us-east-1:111122223333:repository/{{ecr-repository-prefix}}/*"
    },
    {
      "Sid": "EcrAuthToken",
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    },
    {
      "Sid": "ReadRegistryCredential",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:omics-registry/seqera-EXAMPLE"
    }
  ]
}
```
+ `ecr:GetAuthorizationToken` doesn't support resource-level permissions, so it stays on `*`.
+ If you use more than one `ecrRepositoryPrefix`, or more than one non-PTC registry, add each repository ARN and each secret ARN.
+ If you set `ecrAccountId` in the registry mapping, use that account's ID in the Amazon ECR repository ARN.
+ If your secret is in a different account, use that account's secret ARN in the `secretsmanager:GetSecretValue` resource.
+ If your secret is encrypted with a customer managed AWS KMS key, also allow `kms:Decrypt` on that key.

## Verifying that HealthOmics can pull a container image
<a name="permissions-ecr-verify"></a>

Follow this procedure before you start a run to confirm that a container image is available in Amazon ECR and that HealthOmics can pull it. HealthOmics pulls the image while the run is in progress, so a permissions problem usually surfaces then rather than when you create the workflow or call `StartRun`.

The repository must be in the same AWS Region as the run, whether it is in the run's account or in another account. Run each command against that Region, and replace every placeholder with your own value. The commands read your Amazon ECR configuration, so your own IAM permissions need `ecr:GetRepositoryPolicy` and `ecr:DescribeImages`.

1. Find your case in the following table, which lists how an image reaches a run, where to grant access for it, and the principal that pulls it.

<a name="permissions-ecr-verify-principal-table"></a>
<table>
<thead>
  <tr><th>How the image reaches the run</th><th>Where to grant access</th><th>Principal that pulls</th></tr>
</thead>
<tbody>
  <tr><td>The repository is in the run's account, and you push the image</td><td>The repository policy, as in <a href="#permissions-resource-policy">Create a resource policy for the Amazon ECR repository</a></td><td>The HealthOmics service principal, <code>omics.amazonaws.com</code></td></tr>
  <tr><td>The repository is in another account</td><td>That account's repository policy, and the service role in the run's account, as in <a href="#permissions-cross-account-containers">Running workflows with cross-account containers</a></td><td>The HealthOmics service principal, and the service role that you pass to <code>StartRun</code></td></tr>
  <tr><td>Amazon ECR pull through cache fills the repository</td><td>The repository creation template, which supplies the policy of each repository that the cache creates, and the registry policy, which lets HealthOmics create those repositories and import images, both as in <a href="#permissions-ecr-ptc">Policies for Amazon ECR pull through cache</a></td><td>The HealthOmics service principal, and for a cross-account cache the service role that you pass to <code>StartRun</code></td></tr>
  <tr><td>HealthOmics copies the image, with non-PTC container support</td><td>The service role that copies the image, as in <a href="#permissions-ecr-non-ptc">Service role policy for non-PTC container support</a>, and the destination repository policy. If you set <code>ecrAccountId</code>, that account's registry and repository policies as well</td><td>The service role for the copy, and the HealthOmics service principal for the pull that follows</td></tr>
</tbody>
</table>


   A workflow that you share is the exception: the repository policy needs no statement for the subscriber's account, as described in [Amazon ECR policies for shared workflows](#permissions-shared-workflows).

1. Confirm that the image is available. The repository name includes any prefix that a pull through cache rule or a registry mapping adds, and any renaming from an image mapping.

   ```
   aws ecr describe-images \
        --repository-name {{repository-name}} \
        --image-ids imageTag={{tag}} \
        --region {{region}}
   ```

   To name the image by digest instead of by tag, use `--image-ids imageDigest=sha256:{{hex-digest}}`, where {{hex-digest}} is the part after `sha256:`. Use the digest when the run pins one, because a tag can move to a different image.

   For a repository in another account, add `--registry-id {{account-id}}` to this command, so that it reads that account's registry instead of your own. That account's repository policy must also grant you `ecr:DescribeImages`.

   If the image or the repository isn't there, decide whether that is expected. In the pull through cache and non-PTC cases, HealthOmics fills the repository during a run, so before the first run that needs the image:
   + With Amazon ECR pull through cache, Amazon ECR creates the repository and imports the image from the upstream registry on the first pull through the cache. A tag that the cache hasn't imported yet is imported the same way, even when the repository already exists. Whenever the image is absent, verify the registry policy and the repository creation template in [Policies for Amazon ECR pull through cache](#permissions-ecr-ptc) instead.
   + With non-PTC container support, HealthOmics copies the image during the run, so check the upstream image and the service role permissions in [Service role policy for non-PTC container support](#permissions-ecr-non-ptc), then confirm the copy at its destination URI after the run, as described in [Destination repository naming](containers-non-ptc-registries.md#ecr-non-ptc-destination).

1. Read the policy of the repository that holds the image.

   ```
   aws ecr get-repository-policy \
        --repository-name {{repository-name}} \
        --region {{region}}
   ```

   For a repository in another account, add `--registry-id {{account-id}}`, which also requires that account's repository policy to allow you `ecr:GetRepositoryPolicy`. An access-denied error from this command is about your own access, not about the access that HealthOmics has. For the command's response and errors, see [GetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRepositoryPolicy.html) in the *Amazon Elastic Container Registry API Reference*.

1. Confirm that the policy has an `Allow` statement that covers the repository, names the principal for your case, and grants the actions that a pull uses: `ecr:BatchGetImage`, `ecr:GetDownloadUrlForLayer`, and `ecr:BatchCheckLayerAvailability`. Grant all three in a policy that you write. A policy that a service created can grant fewer and still work. A wildcard that covers them also works.

   The following JSON policy statement passes this step. Replace each placeholder with your own value, where {{run-account-id}} is the account that the run is in:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "HealthOmicsPull",
         "Effect": "Allow",
         "Principal": {
           "Service": "omics.amazonaws.com"
         },
         "Action": [
           "ecr:BatchGetImage",
           "ecr:GetDownloadUrlForLayer",
           "ecr:BatchCheckLayerAvailability"
         ],
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{run-account-id}}",
             "aws:SourceArn": "arn:aws:omics:{{region}}:{{run-account-id}}:workflow/{{workflow-id}}"
           }
         }
       }
     ]
   }
   ```

   When the repository is in the run's account, a role there can instead be allowed by its own identity policy, so the repository policy doesn't need to name that role. A repository in another account must name the role, as in [Running workflows with cross-account containers](#permissions-cross-account-containers). Only the repository policy can allow the service principal.

   Then check any `Condition` on that statement against the values that HealthOmics sends. `aws:SourceArn` is the ARN of the workflow that the run uses, and `aws:SourceAccount` is the account that the run is in. A condition scoped to run ARNs instead of workflow ARNs blocks every pull.

   An explicit `Deny` that matches the principal blocks the pull whatever the `Allow` statements grant. For how AWS evaluates policies, see [Determining whether a request is allowed or denied](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow) in the *IAM User Guide*.

   For a repository that Amazon ECR pull through cache created, the policy normally grants only `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer`, from the repository creation template in [Repository creation template](#permissions-repo-template). Amazon ECR applies the template only when it creates the repository, so a template that changed later doesn't update the policy. Judge the repository's own policy, not the template. Those two actions are enough for a pull, so such a policy passes this step.

   If the repository has no policy at all, HealthOmics can't pull from it, unless HealthOmics copies the image in: HealthOmics attaches a policy to a repository that has none, and leaves an existing policy unchanged, as described in [Destination repository naming](containers-non-ptc-registries.md#ecr-non-ptc-destination).

1. If your case names a service role, confirm the identity side as well. The role's own policy must allow the same actions on the repository, as in [Service role policy for non-PTC container support](#permissions-ecr-non-ptc) for an image that HealthOmics copies, or [Running workflows with cross-account containers](#permissions-cross-account-containers) for a repository in another account. If you pass a session policy to `StartRun`, the run's permissions are the intersection of the role and that policy, so the session policy must allow these actions too, as described in [Use session policies to scope down permissions](permissions-service.md#permissions-service-sessionpolicy).

1. If every check passes, the policies allow the principal for your case to pull the image. They don't prove the pull, because only a run exercises them with the values that HealthOmics sends. Start a run that uses the image. If a pull problem remains, the run fails with ECR\_PERMISSION\_ERROR before it creates any task, so start with the run's failure reason. When HealthOmics copies the image, a copy failure fails the task as well, so check the task's failure reason too. Either way, work through your case again. For the error, see [Run failure reasons](workflows-run-errors.md).