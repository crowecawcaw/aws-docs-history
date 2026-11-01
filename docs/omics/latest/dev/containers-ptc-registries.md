

# Using third-party registries supported by pull through cache
<a name="containers-ptc-registries"></a>

You can use Amazon ECR pull through cache rules to synchronize repositories in a supported upstream registry with your Amazon ECR private repositories. For more information, see [Sync an upstream registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html) in the *Amazon Elastic Container Registry User Guide*.

The first time an image is pulled, pull through cache creates the image repository in your private registry and keeps it synchronized with the upstream image, as long as the repository's image tags stay mutable.

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

1. Because Amazon ECR pull through caches use a predictable URI structure, you can keep the upstream image URIs in your workflow definition and add a container registry map that resolves them to your cache repositories. For more information, see [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map).

**Topics**
+ [Prerequisites](#ecr-ptc-prerequisites)
+ [Configuring pull through cache](#ecr-pull-through-configure)
+ [Re-running the configuration](#rerun-ecr-ptc)
+ [Troubleshooting pull through cache](#ecr-ptc-troubleshooting)

## Prerequisites
<a name="ecr-ptc-prerequisites"></a>

If an upstream registry requires authentication, the AWS Secrets Manager secret must be in the same AWS account and Region as the pull through cache rule. When you create the rule, pass `--credential-arn` the secret's ARN exactly as Secrets Manager returns it, including the suffix that Secrets Manager appends to the name. The Secrets Manager **create-secret** and **describe-secret** responses both return it. The example ARNs in this topic abbreviate the secret name.


| Upstream registry | Registry URL | Secrets Manager secret required | 
| --- | --- | --- | 
| Amazon ECR Public | `public.ecr.aws` | No | 
| Kubernetes container image registry | `registry.k8s.io` | No | 
| Quay | `quay.io` | No | 
| Docker Hub | `registry-1.docker.io` | Yes | 
| Microsoft Azure Container Registry | `{{registry-name}}.azurecr.io` | Yes | 
| GitHub Container Registry | `ghcr.io` | Yes | 
| GitLab Container Registry | `registry.gitlab.com` | Yes | 

The secret name must begin with `ecr-pullthroughcache/`. For the other requirements, see [Storing your upstream repository credentials in an AWS Secrets Manager secret](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-creating-secret.html) in the *Amazon Elastic Container Registry User Guide*.

## Configuring pull through cache
<a name="ecr-pull-through-configure"></a>

Amazon ECR provides a registry for your AWS account in each Region. Make sure you create the Amazon ECR configuration in the same region where you plan to run the workflow.

Complete the following configuration tasks in order. Step 4 applies only if your workflow definition uses the upstream image URIs.

**Topics**
+ [Step 1: Creating a pull through cache rule](#create-ecr-ptc)
+ [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc)
+ [Step 3: Creating repository templates](#repo-create-templates-ptc)
+ [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map)
+ [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc)

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

Make sure `Resource` covers every cache repository prefix that you created, and set the Region and the AWS account in each repository ARN to the registry that you are configuring, because a registry policy applies only to its own Region and account.

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

1. Save the policy.

To attach the policy with the AWS CLI instead, save it to a file, then use the Amazon ECR **put-registry-policy** command:

```
aws ecr put-registry-policy \
     --policy-text file://{{registry-policy-file}}.json \
     --region {{region}}
```

**Important**  
**put-registry-policy** replaces the entire registry policy. If your registry already has a policy, retrieve it with **get-registry-policy**, add the HealthOmics statement, and put the combined policy back.

For more information about the policies for Amazon ECR pull through cache, see [Policies for Amazon ECR pull through cache](permissions-ecr.md#permissions-ecr-ptc).

### Step 3: Creating repository templates
<a name="repo-create-templates-ptc"></a>

To use pull through caching in HealthOmics, the Amazon ECR repository must have a repository creation template. The template defines configuration settings for when you or Amazon ECR create a private repository for an upstream registry. 

Each template contains a repository namespace prefix, which Amazon ECR uses to match new repositories to a specific template. Templates specify the configuration for all repository settings including resource-based access policies, tag immutability, encryption, and lifecycle policies.

For more information, see [Repository creation templates](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-creation-templates.html) in the *Amazon Elastic Container Registry User Guide*.

**Note**  
Create the template before the first run that uses the prefix. A prefix with no template of its own, and no `ROOT` template, gets no repository policy, so HealthOmics can't pull its cached images. Leave tag mutability at `MUTABLE`, so that Amazon ECR can refresh a cached image when the upstream tag changes. For repositories that already exist, see [Updating repositories created before the template](#ecr-ptc-troubleshoot-template-late).

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

To create the template with the AWS CLI instead, save the repository policy from the preceding procedure to a file, then use the Amazon ECR **create-repository-creation-template** command with `--prefix` set to the cache repository prefix from your pull through cache rule. The description is optional:

```
aws ecr create-repository-creation-template \
     --prefix {{ecr-repository-prefix}} \
     --applied-for PULL_THROUGH_CACHE \
     --repository-policy file://{{repository-policy-file}}.json \
     --image-tag-mutability MUTABLE \
     --description "{{description}}" \
     --region {{region}}
```

If a template already exists for the prefix, **create-repository-creation-template** fails with TemplateAlreadyExistsException. Update the existing template in place instead:

```
aws ecr update-repository-creation-template \
     --prefix {{ecr-repository-prefix}} \
     --applied-for PULL_THROUGH_CACHE \
     --repository-policy file://{{repository-policy-file}}.json \
     --image-tag-mutability MUTABLE \
     --region {{region}}
```

**Important**  
**update-repository-creation-template** replaces each value that you pass, so `--applied-for` and `--repository-policy` overwrite the existing list and policy rather than merging with them. Retrieve the current template with **describe-repository-creation-templates**, merge your changes, and pass the complete values.

Amazon ECR is configured, but the HealthOmics configuration isn't finished. If your workflow definition uses the upstream image URIs, continue to [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map): without a container registry map, the run fails after it starts. Otherwise, continue to [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc).

### Step 4: Adding a container registry map (if your workflow uses upstream URIs)
<a name="ecr-ptc-registry-map"></a>

The image URIs in your workflow definition decide whether you need a container registry map:


| Image URIs in your workflow definition | Registry map | 
| --- | --- | 
| The upstream URIs, in the form `{{upstream-registry-url}}/{{upstream-repository-name}}:{{tag}}` | Add a map. The map tells HealthOmics which cache repository prefix belongs to which upstream registry, because HealthOmics doesn't read your pull through cache rules. | 
| The Amazon ECR private URIs of your cache repositories, in the form `{{account-id}}.dkr.ecr.{{region}}.amazonaws.com/{{ecr-repository-prefix}}/{{upstream-repository-name}}:{{tag}}` | You don't need a map. HealthOmics uses each URI as given. | 

An image name written without a registry host is a Docker Hub short name, which counts as an upstream URI and needs a map.

If your definition uses both kinds of URI, add a map for the images that use the upstream URIs.

**Important**  
With the upstream URIs, `StartRun` succeeds even if the map is missing or has no mapping for an image's upstream registry. HealthOmics validates each image when it creates the task that uses it, so the run fails after it starts. Both cases give the failure reason INVALID\_ECR\_IMAGE\_URI, and the run's status message distinguishes them. A mapping that resolves an image to a cache repository that doesn't exist instead gives ECR\_REPOSITORY\_NOT\_FOUND.

Mirror your pull through cache rule in the mapping: set `upstreamRegistryUrl` to the rule's upstream registry URL, `ecrRepositoryPrefix` to its cache repository prefix, and `upstreamRepositoryPrefix` to its upstream repository prefix if the rule uses one.

If your cache repositories are in a different AWS account from the workflow, set `ecrAccountId` to the account that owns the cache repositories, and add the cross-account policies described in [Policies for cross-account Amazon ECR access](permissions-ecr.md#permissions-cross-account). `ecrAccountId` defaults to the workflow's own account.

**Note**  
For Docker Hub, set `upstreamRegistryUrl` to `registry-1.docker.io`, the value in [Prerequisites](#ecr-ptc-prerequisites). HealthOmics treats `registry-1.docker.io` and `docker.io` as the same host, so that one mapping also covers image URIs written with `docker.io`.  
HealthOmics also expands a short Docker Hub name before it matches the mapping: `ubuntu:22.04` becomes `docker.io/library/ubuntu:22.04`, and `myorg/image:tag` becomes `docker.io/myorg/image:tag`. HealthOmics inserts `library/` only when the image name in your definition has no slash. The expanded name also determines the cache repository path, so `ubuntu:22.04` resolves to `{{ecr-repository-prefix}}/library/ubuntu:22.04` in your private registry.

You supply the map when you create the workflow or the workflow version. For the map format and the rules that decide which mappings your workflow needs, see [Registry mappings](containers-workflow-creation.md#ecr-pull-through-registry-mapping). For image mappings, see [Image mappings](containers-workflow-creation.md#ecr-pull-through-mapping-format). After you add the map, continue to [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc).

### Step 5: Verifying your pull through cache configuration
<a name="verify-ecr-ptc"></a>

Run the **aws ecr** commands in the account that owns the cache repositories, because **get-registry-policy** and **describe-repository-creation-templates** always read the calling account's registry, and run the **aws omics** commands in the account that owns the workflow. Use the Region where you run your workflows for both. The three checks in the following procedure are independent, so run all of them and collect every problem before you go back to fix them. The registry map check after the procedure applies once you have created the workflow or workflow version, as described in [Adding private or third-party containers during workflow creation](containers-workflow-creation.md). The end-to-end check after it also requires a started run.

1. Confirm that the pull through cache rule exists and points at the expected upstream registry:

   ```
   aws ecr describe-pull-through-cache-rules \
        --region {{region}}
   ```

   Each rule that you created appears with its `ecrRepositoryPrefix` and `upstreamRegistryUrl`. A rule that sets an upstream repository prefix also shows `upstreamRepositoryPrefix`, and a rule that uses a credential also shows `credentialArn`; Amazon ECR omits each of those fields when the rule doesn't set it. An empty `pullThroughCacheRules` list means that no rule exists in this Region. Return to [Step 1: Creating a pull through cache rule](#create-ecr-ptc).

   If the rule uses a credential, also confirm that Amazon ECR can read the secret and sign in to the upstream registry:

   ```
   aws ecr validate-pull-through-cache-rule \
        --ecr-repository-prefix {{ecr-repository-prefix}} \
        --region {{region}}
   ```

   The output includes `"isValid": true` when authentication succeeds, and otherwise names the reason in `failure`. If the command fails with PullThroughCacheRuleNotFoundException, no rule uses that prefix. An AccessDeniedException means that your caller lacks the `ecr:ValidatePullThroughCacheRule` permission, which read-only policies don't always include, not that the rule is wrong. For more information, see [Validating pull through cache rules](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-working-validating.html) in the *Amazon Elastic Container Registry User Guide*.

1. Confirm that the registry policy grants HealthOmics access:

   ```
   aws ecr get-registry-policy \
        --region {{region}}
   ```

   The `policyText` value in the output, which Amazon ECR returns JSON-escaped, must contain the statement from [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc), granting `omics.amazonaws.com` both `ecr:CreateRepository` and `ecr:BatchImportUpstreamImage`, individually or through a wildcard, and covering every cache repository prefix that you created. A prefix is covered by a `Resource` entry that matches the cache repositories under it, such as a repository ARN ending in the prefix followed by `/*`, a repository ARN ending in `/*` alone, or a `Resource` of `*`. An ARN that ends at the prefix itself, with no `/*`, covers nothing: a cache repository name always has a path under the prefix. An ARN that names a Region or AWS account other than this registry's own covers nothing either, as described in [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc). If no statement covers a prefix, or if the command fails with RegistryPolicyNotFoundException, return to [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc) and make sure that you saved the policy.

1. Confirm that a repository creation template exists for each cache repository prefix. Pass all of the prefixes that you created:

   ```
   aws ecr describe-repository-creation-templates \
        --prefixes {{ecr-repository-prefix-1}} {{ecr-repository-prefix-2}} \
        --region {{region}}
   ```

   For each prefix, the template that Amazon ECR applies to its cache repositories — identified in the next paragraph — must have `PULL_THROUGH_CACHE` in `appliedFor` and a `repositoryPolicy` that grants `omics.amazonaws.com` the pull actions from [Step 3: Creating repository templates](#repo-create-templates-ptc), `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer`. A non-empty policy isn't enough: confirm the principal as well as the actions.

   Amazon ECR applies the template whose prefix is the longest match for the repository, or a `ROOT` template if no prefix matches. Run the command without `--prefixes` to see every template, because `--prefixes` matches each prefix exactly rather than by path, so neither a `ROOT` template nor a template on a longer prefix appears in the filtered output. Return to that step for any prefix whose applicable template is missing or fails either requirement. `imageTagMutability` doesn't affect whether HealthOmics can pull the image, but a template that sets it to anything other than `MUTABLE` stops Amazon ECR refreshing a cached image when the upstream tag moves, as described in [Step 3: Creating repository templates](#repo-create-templates-ptc).

   If any cache repositories existed before you created the template, also confirm the repository policy on each of them, as described in [Updating repositories created before the template](#ecr-ptc-troubleshoot-template-late).

If your definition uses the upstream URIs, confirm the registry map that you added in [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map). A map belongs to the workflow or the workflow version that you supplied it with, so check the one your runs use: the version that you pass as `--workflow-version-name` to **start-run**, or the workflow if your runs don't name one. For a run that already exists, `workflowVersionName` in the **get-run** output names its version.

For a workflow:

```
aws omics get-workflow \
     --id {{workflow-id}} \
     --region {{region}}
```

For a workflow version:

```
aws omics get-workflow-version \
     --workflow-id {{workflow-id}} \
     --version-name {{version-name}} \
     --region {{region}}
```

Check the `containerRegistryMap` value in the output. If it has no map, the response omits the field. Confirm that `status` is `ACTIVE`: if it is still `CREATING`, wait and retry, and if it is `FAILED`, the reason is in `statusMessage`. You can't change a map in place, so if it is missing or wrong, create a new workflow version as described in [Re-running the configuration](#rerun-ecr-ptc).

To confirm end-to-end that a run used a cached image, read the outcome of a run that uses the cache. A run that has already finished works, including one that failed, but a cancelled run may never have resolved its images; start a run only if you don't have one yet:

```
aws omics get-run \
     --id {{run-id}} \
     --region {{region}}
```

The `resourceDigests` field in the output, when the run reports one, records resources that the run resolved, including its container images. An entry whose key is an Amazon ECR private URI under your cache repository prefix, with a `sha256` digest as its value, confirms that the run resolved that image to your cache. This is the quickest check, and it works even for a run that failed for an unrelated reason.

If the run stopped without succeeding, `failureReason` and `statusMessage` together tell you whether this configuration is involved. Check these before you look at the run's tasks, because a run that fails on an image may create no tasks at all:
+ ECR\_REPOSITORY\_NOT\_FOUND, ECR\_IMAGE\_NOT\_FOUND or ECR\_PERMISSION\_ERROR for an image URI under one of your cache repository prefixes – continue to [Troubleshooting pull through cache](#ecr-ptc-troubleshooting). One of those reasons for a URI that isn't under one of your prefixes is an Amazon ECR problem with that repository rather than a pull through cache problem, because no cache rule applies to it. For a repository that you manage in Amazon ECR yourself, give HealthOmics access with a repository policy, as described in [Create a resource policy for the Amazon ECR repository](permissions-ecr.md#permissions-resource-policy).
+ INVALID\_ECR\_IMAGE\_URI – the registry map is missing, it has no mapping for the image's upstream registry, its `upstreamRepositoryPrefix` doesn't cover the image's path, or the image URI isn't valid. Read the status message to tell these apart, and check the URI before you change the map. See [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map).
+ CANNOT\_START\_CONTAINER\_ERROR or IMAGE\_VERIFICATION\_FAILURE for an image URI under one of your prefixes – the image reached your cache repository but the task couldn't use it. If you changed or recreated the cache rule, a stale cached image can cause this; see [Changing a cache rule while a run is active](#ecr-ptc-troubleshoot-rule-change). Otherwise the cached image itself is the problem rather than this configuration, and the upstream image or the task that uses it is where to look.
+ Any other failure reason, or none at all as a cancelled run reports – the run stopped for a reason unrelated to this configuration. For the run statuses and the other failure reasons, see [Get run information](getinfo-about-runs.md) and [Run failure reasons](workflows-run-errors.md).

Not every run reports `resourceDigests`, and a run that hasn't resolved its images yet has no entry for them. If the field or the entry is missing, or if you want to confirm which image an individual task pulled, list the run's tasks:

```
aws omics list-run-tasks \
     --id {{run-id}} \
     --region {{region}}
```

An empty `items` list on a run that is still going means that HealthOmics hasn't created the tasks yet, so wait and list them again. On a run that has stopped it means that no task was ever created: for a failed run the preceding failure reasons explain why, and a run cancelled before it started has nothing to confirm, so use a different run. Otherwise, retrieve the image details for one of the tasks, using a `taskId` from the preceding output:

```
aws omics get-run-task \
     --id {{run-id}} \
     --task-id {{task-id}} \
     --region {{region}} \
     --query imageDetails
```

In `imageDetails`, `sourceImage` is the image URI from your workflow definition, and `image` is the Amazon ECR private URI that the task pulled. An `image` value under your cache repository prefix, in the private-URI form shown in [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map) and possibly with an image digest appended, confirms that the task used your pull through cache. `imageDetails` can be empty, for a task that hasn't pulled its image yet and for some tasks that have already finished. A task with no image details recorded has none in the run manifest log either, so check another task of the same run. If no task in a completed run recorded them, you can still confirm that the image is cached, as described in [Resolving a missing or incomplete registry policy](#ecr-ptc-troubleshoot-registry-policy). That confirms the configuration rather than which image a particular task pulled, because an earlier run may have populated the cache.

After a run completes, its run manifest log repeats this image information, so you can check the run's tasks at once instead of calling **get-run-task** for each one. In each task's record the field named `originalImage` corresponds to `sourceImage` here, and `image` is the same value as above. For where to find the log, see [Monitoring HealthOmics with CloudWatch Logs](monitoring-cloudwatch-logs.md), and for the rest of a task's record, see [Get run information](getinfo-about-runs.md).

After you configure pull through cache, you can create a new workflow or workflow version to use the containers from configured registries. For more information, see [Adding private or third-party containers during workflow creation](containers-workflow-creation.md).

## Re-running the configuration
<a name="rerun-ecr-ptc"></a>

You can repeat these steps, for example to add a prefix or to correct a policy. The create commands fail with a non-zero exit code when the resource already exists, without changing it. **put-registry-policy** doesn't fail, but it replaces the whole registry policy, as described in [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc).
+ Pull through cache rule – **create-pull-through-cache-rule** fails with PullThroughCacheRuleAlreadyExistsException. If the registry that you are adding needs authentication, create its Secrets Manager secret first, as described in [Prerequisites](#ecr-ptc-prerequisites).
+ Registry permissions policy – add a `Resource` entry for each new cache repository prefix, as described in [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc); a policy that enumerates prefixes individually won't cover a new one. Confirm the coverage with **get-registry-policy**, as described in [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc).
+ Repository creation template – create a template for a cache repository prefix that doesn't have one, and update the existing template to change a prefix that already has one, both as described in [Step 3: Creating repository templates](#repo-create-templates-ptc). Running update against another prefix's template overwrites that template. To bring repositories that Amazon ECR already created up to date, see [Updating repositories created before the template](#ecr-ptc-troubleshoot-template-late).
+ Container registry map – you supply the map when you create a workflow or workflow version, and **update-workflow** and **update-workflow-version** can't change it. Before you create a version, have the complete map ready: a new version doesn't inherit the previous version's map, so list every mapping that the workflow still needs, not only the new one. **create-workflow-version** takes the whole version rather than just the map, so you also need the workflow definition and the version's other parameters, as described in [Create a workflow version](workflows-version-create.md). Then create the version with the updated map, as described in [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map), and start your runs against that version. A run that doesn't name a version uses the workflow's default version, which keeps the map it was created with, so it fails the same way as before. For more information, see [Default workflow version](workflows-default-version.md).

## Troubleshooting pull through cache
<a name="ecr-ptc-troubleshooting"></a>

The following configuration problems cause a run to fail when you use containers from pull through cache. If your workflow definition uses the upstream image URIs and a run fails with INVALID\_ECR\_IMAGE\_URI, start with the registry map, as described in [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map). For other run failure reasons, see [Run failure reasons](workflows-run-errors.md).

Run the **aws ecr** commands in this section in the same account as in [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc), or pass `--registry-id {{ecr-account-id}}`. Use the repository names exactly as **describe-repositories** returns them: a cache repository name is the cache repository prefix followed by the upstream repository path, which for a Docker Hub short name includes the `library/` segment described in [Step 4: Adding a container registry map (if your workflow uses upstream URIs)](#ecr-ptc-registry-map).

### Resolving a missing or incomplete registry policy
<a name="ecr-ptc-troubleshoot-registry-policy"></a>

**Symptom**—The run fails for the image URI with one of the following failure reasons:
+ ECR\_REPOSITORY\_NOT\_FOUND – the cache repository doesn't exist in your private registry.
+ ECR\_IMAGE\_NOT\_FOUND – the cache repository exists, but the image was never imported into it.
+ ECR\_PERMISSION\_ERROR – Amazon ECR denies access.

If the cache repository is missing, the following command returns no repository for the prefix:

```
aws ecr describe-repositories \
     --region {{region}} \
     --query "repositories[?starts_with(repositoryName, '{{ecr-repository-prefix}}/')]"
```

An empty result for a prefix that nothing has pulled from yet is expected and isn't a configuration problem on its own. When a run has failed for the image URI, a missing repository usually means that Amazon ECR couldn't create it. If the repository exists, confirm whether the image reached it:

```
aws ecr describe-images \
     --repository-name {{cache-repository-name}} \
     --image-ids imageTag={{tag}} \
     --region {{region}}
```

A returned image means that the tag is cached. ImageNotFoundException means that the repository exists but that tag isn't in it, and RepositoryNotFoundException means that the repository name is wrong or that nothing has pulled through the prefix yet. Pass `--image-ids`: without it, the command reports every tag in the repository, so another tag's presence can look like success for the tag that your run needs.

**Cause**—The registry policy doesn't grant HealthOmics what it needs: there is no policy, the policy is missing an action, or its `Resource` list doesn't cover this cache prefix.

**Solution**—Add or correct the registry policy as described in [Step 2: Setting up permissions for the upstream registry](#reg-ecr-ptc), and confirm it as described in [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc). If the registry policy already covers the cache repository prefix, the registry policy isn't the problem. For ECR\_IMAGE\_NOT\_FOUND, where the repository exists but the image never arrived, the upstream import failed: confirm the rule's credential with **validate-pull-through-cache-rule**, as described in [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc). For ECR\_PERMISSION\_ERROR on a repository that exists, continue to [Resolving a missing repository creation template or repository policy](#ecr-ptc-troubleshoot-template). Then start the run again.

### Resolving a missing repository creation template or repository policy
<a name="ecr-ptc-troubleshoot-template"></a>

**Symptom**—The cache repository exists with the imported image, and the run still fails with ECR\_PERMISSION\_ERROR for the image URI.

**Cause**—No repository creation template matches the cache repository prefix, the template doesn't include `PULL_THROUGH_CACHE` in `appliedFor`, or the template has no repository policy. The repository therefore has no policy that lets HealthOmics pull from it.

**Solution**—Create or update the template as described in [Step 3: Creating repository templates](#repo-create-templates-ptc). Because the repositories already exist, also apply the policy to them, as described in [Updating repositories created before the template](#ecr-ptc-troubleshoot-template-late).

### Updating repositories created before the template
<a name="ecr-ptc-troubleshoot-template-late"></a>

**Symptom**—You created or corrected the repository creation template, **describe-repository-creation-templates** shows it as correct, and a run still fails with an Amazon ECR access error for the same image. Confirm the missing policy on an affected repository:

```
aws ecr get-repository-policy \
     --repository-name {{cache-repository-name}} \
     --region {{region}}
```

The `policyText` value must grant `omics.amazonaws.com` at least the actions that the template's repository policy grants. If the repository has no policy at all, the command fails with RepositoryPolicyNotFoundException. If it fails with RepositoryNotFoundException, the repository name is wrong or the repository doesn't exist yet.

**Cause**—A template applies only when Amazon ECR creates a repository, so repositories created before you added the template have no repository policy for HealthOmics.

**Solution**—Bring the existing repositories up to date in one of the following ways.

**Warning**  
Deleting a repository also deletes every cached image in it, and you can't undo it. Don't delete a repository while a run is using it.
+ Set the policy on each existing repository directly. Save the template's repository policy to a file, then run the following command for each affected repository:

  ```
  aws ecr set-repository-policy \
       --repository-name {{cache-repository-name}} \
       --policy-text file://{{repository-policy-file}}.json \
       --region {{region}}
  ```
+ Delete each affected repository. Pull through cache recreates it from the template the next time a task pulls the image, so the cached image isn't available until that pull completes.

  ```
  aws ecr delete-repository \
       --repository-name {{cache-repository-name}} \
       --force \
       --region {{region}}
  ```

### Changing a cache rule while a run is active
<a name="ecr-ptc-troubleshoot-rule-change"></a>

**Symptom**—After you change or recreate a pull through cache rule, a run that is already using the affected repository can fail with CANNOT\_START\_CONTAINER\_ERROR or IMAGE\_VERIFICATION\_FAILURE, or can complete using an image that you didn't expect.

**Cause**—The cache repository prefix now resolves to a different upstream repository, while runs are already pulling from the repositories that the old rule created.

**Solution**—Wait for the active runs to finish before you change the rule, as the note in [Step 1: Creating a pull through cache rule](#create-ecr-ptc) describes. To confirm which image a task actually used, check `imageDetails` in the **get-run-task** output, as described in [Step 5: Verifying your pull through cache configuration](#verify-ecr-ptc). If a run used a stale cached image, delete that image from the cache repository so that the next pull refreshes it from the upstream registry.