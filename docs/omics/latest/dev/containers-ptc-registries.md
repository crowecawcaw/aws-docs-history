

# Using third-party registries supported by pull through cache
<a name="containers-ptc-registries"></a>

You can use Amazon ECR pull through cache rules to synchronize repositories in a supported upstream registry with your Amazon ECR private repositories. For more information, see [Sync an upstream registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html) in the *Amazon Elastic Container Registry User Guide*.

When you create the cache, pull through cache creates the image repository in your private registry and keeps it synchronized with the upstream image.

HealthOmics supports pull through cache for the following upstream registries:
+ Amazon ECR Public
+ Kubernetes container image registry
+ Quay
+ Docker Hub
+ Microsoft Azure Container Registry
+ GitHub Container Registry
+ GitLab Container Registry

For registries that pull through cache doesn't support, HealthOmics copies the images into your Amazon ECR private repositories. For more information, see [Using third-party registries not supported by pull through cache](containers-non-ptc-registries.md).

Benefits of using Amazon ECR pull through cache include:

1. You avoid having to manually migrate container images to Amazon ECR or to synchronize updates from the third party repository.

1. Workflows access the synchronized container images in your private repository, which is more reliable than downloading content at run time from a public registry.

1. Because Amazon ECR pull through caches use a predictable URI structure, the HealthOmics service can automatically map the Amazon ECR private URI with the upstream registry URI. You aren't required to update and replace URI values in the workflow definition.

## Configuring pull through cache
<a name="ecr-pull-through-configure"></a>

Amazon ECR provides a registry for your AWS account in each Region. Make sure you create the Amazon ECR configuration in the same region where you plan to run the workflow.

Before you use containers from Amazon ECR pull through cache, create a pull through cache rule, set up permissions, and create repository templates. The following sections describe these configuration tasks.

**Topics**
+ [Step 1: Creating a pull through cache rule](#create-ecr-ptc)
+ [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc)
+ [Step 3: Creating repository templates](#repo-create-templates-ptc)

### Step 1: Creating a pull through cache rule
<a name="create-ecr-ptc"></a>

Create an Amazon ECR pull through cache rule for each upstream registry that has images you want to cache. A rule specifies a mapping between an upstream registry and the Amazon ECR private repository.

For an upstream registry that requires authentication, you provide your credentials using AWS Secrets Manager.

**Note**  
Don't change a pull through cache rule while an active run is using the private repository. The run could fail or, more critically, result in your pipeline using unexpected images.

For more information, see [Creating a pull through cache rule](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-creating-rule.html) in the *Amazon Elastic Container Registry User Guide*.

#### Creating a pull through cache rule using the console
<a name="create-ecr-ptc-console"></a>

To configure pull through cache, follow these steps using the Amazon ECR console:

**Part 1: Choosing the upstream registry**

1. Open the [Amazon ECR console](https://console.aws.amazon.com/ecr/).

1. In the navigation pane, under **Private registry**, expand **Features & Settings**, then choose **Pull through cache**.

1. On the **Pull through cache** page, choose **Add rule**.

1. In the **Upstream registry** panel, choose the upstream registry to sync with your private registry, then choose **Next**.

1. If the upstream registry requires authentication, on the next page, specify the Secrets Manager secret that contains your credentials. Choose **Next**.

**Part 2: Specifying namespaces and creating the rule**

1. Under **Specify namespaces**, in the **Cache namespace** panel, choose whether to create the private repositories using a specific repository prefix or with no prefix. If you choose to use a prefix, specify the prefix name in **Cache repository prefix**.

1. In the **Upstream namespace** panel, choose whether to pull from upstream repositories using a specific repository prefix or with no prefix. If you choose to use a prefix, specify the prefix name in **Upstream repository prefix**.

   The **Namespace example** panel shows an example pull request, upstream URL, and the URL of the cache repository that is created.

1. Choose **Next**.

1. Review the configuration and choose **Create** to create the rule.

#### Creating a pull through cache rule using the AWS CLI
<a name="create-ecr-ptc-cli"></a>

Use the Amazon ECR **create-pull-through-cache-rule** command to create a pull through cache rule. For upstream registries that require authentication, store the credentials in a Secrets Manager secret.

The following examples show how to create a rule for each supported upstream registry.

------
#### [ Amazon ECR Public ]

The following example creates a pull through cache rule for the Amazon ECR Public registry. It specifies a repository prefix of `ecr-public`, so each repository that the rule creates uses the naming scheme `ecr-public/{{upstream-repository-name}}`.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{ecr-public}} \
     --upstream-registry-url public.ecr.aws \
     --region {{us-east-1}}
```

------
#### [ Kubernetes container image registry ]

The following example creates a pull through cache rule for the Kubernetes public registry. It specifies a repository prefix of `kubernetes`, so each repository that the rule creates uses the naming scheme `kubernetes/{{upstream-repository-name}}`.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{kubernetes}} \
     --upstream-registry-url registry.k8s.io \
     --region {{us-east-1}}
```

------
#### [ Quay ]

The following example creates a pull through cache rule for the Quay public registry. It specifies a repository prefix of `quay`, so each repository that the rule creates uses the naming scheme `quay/{{upstream-repository-name}}`.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{quay}} \
     --upstream-registry-url quay.io \
     --region {{us-east-1}}
```

------
#### [ Docker Hub ]

The following example creates a pull through cache rule for the Docker Hub registry. It specifies a repository prefix of `docker-hub`, so each repository that the rule creates uses the naming scheme `docker-hub/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your Docker Hub credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{docker-hub}} \
     --upstream-registry-url registry-1.docker.io \
     --credential-arn arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-1}}
```

------
#### [ GitHub Container Registry ]

The following example creates a pull through cache rule for the GitHub Container Registry. It specifies a repository prefix of `github`, so each repository that the rule creates uses the naming scheme `github/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your GitHub Container Registry credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{github}} \
     --upstream-registry-url ghcr.io \
     --credential-arn arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-1}}
```

------
#### [ Microsoft Azure Container Registry ]

The following example creates a pull through cache rule for the Microsoft Azure Container Registry. It specifies a repository prefix of `azure`, so each repository that the rule creates uses the naming scheme `azure/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your Microsoft Azure Container Registry credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{azure}} \
     --upstream-registry-url {{myregistry}}.azurecr.io \
     --credential-arn arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-1}}
```

------
#### [ GitLab Container Registry ]

The following example creates a pull through cache rule for the GitLab Container Registry. It specifies a repository prefix of `gitlab`, so each repository that the rule creates uses the naming scheme `gitlab/{{upstream-repository-name}}`. You must specify the full Amazon Resource Name (ARN) of the secret containing your GitLab Container Registry credentials.

```
aws ecr create-pull-through-cache-rule \
     --ecr-repository-prefix {{gitlab}} \
     --upstream-registry-url registry.gitlab.com \
     --credential-arn arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{ecr-pullthroughcache/example1234}} \
     --region {{us-east-1}}
```

------

You can use the **get-run-task** AWS CLI command to retrieve information about the container image used for a specific task:

```
aws omics get-run-task --id {{run-id}} --task-id {{task-id}}
```

The output includes the following information about the container image:

```
"imageDetails": {
    "image": "string",
    "imageDigest": "string",
    "sourceImage": "string",
    ...
}
```

### Step 2: Setting up permissions for the upstream registry
<a name="reg-ecr-ptc"></a>

Use registry permissions to allow HealthOmics to use the pull through cache and to pull the container images into the Amazon ECR private registry. Add an Amazon ECR Registry policy to the registry that provides the containers used in runs. 

The following policy grants permission for the HealthOmics service to create repositories with the specified pull through cache prefixes and to initiate upstream pulls into these repositories. 

1. Open the [Amazon ECR console](https://console.aws.amazon.com/ecr/).

1. In the navigation pane, under **Private registry**, expand **Registry permissions**, then choose **Generate statement**.

1. On the top right side, choose JSON. Enter a policy similar to the following:

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

For more information about the policies for Amazon ECR pull through cache, see [Policies for Amazon ECR pull through cache](permissions-ecr.md#permissions-ecr-ptc).

### Step 3: Creating repository templates
<a name="repo-create-templates-ptc"></a>

To use pull through caching in HealthOmics, the Amazon ECR repository must have a repository creation template. The template defines configuration settings for when you or Amazon ECR create a private repository for an upstream registry. 

Each template contains a repository namespace prefix, which Amazon ECR uses to match new repositories to a specific template. Templates specify the configuration for all repository settings including resource-based access policies, tag immutability, encryption, and lifecycle policies.

For more information, see [Repository creation templates](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-creation-templates.html) in the *Amazon Elastic Container Registry User Guide*.

To create a repository creation template, follow these steps using the Amazon ECR console:

**Part 1: Defining the template**

1. Open the [Amazon ECR console](https://console.aws.amazon.com/ecr/).

1. In the navigation pane, under **Private registry**, expand **Features and settings**, then choose **Repository creation templates**.

1. Choose **Create template**.

1. In **Template details**, choose **Pull through cache**.

1. Choose whether to apply this template to a specific prefix or to all repositories that don't match another template.

   If you choose **A specific prefix**, enter the namespace prefix value in **Prefix**. You specified this prefix when you created the pull through cache rule.

1. Choose **Next**.

**Part 2: Adding the repository creation configuration**

1. On the **Add repository creation configuration** page, for **Repository permissions**, use one of the sample policy statements, or enter one similar to the following example:

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

1. (Optional) Add repository settings such as lifecycle policy and tags. Amazon ECR applies these rules for all container images created for pull through cache that use the specified prefix.

1. Choose **Next**.

1. Review the configuration and choose **Create** to create the template.

After you configure pull through cache, you can create a new workflow or workflow version to use the containers from configured registries. For more information, see [Adding private or third-party containers during workflow creation](containers-workflow-creation.md).