# Creating a pull through cache rule in Amazon ECR

For each upstream registry containing images that you want to cache in your Amazon ECR
private registry, you must create a pull through cache rule.

For upstream registries that require authentication with secrets, you must store the
credentials in a Secrets Manager secret. You can use an existing secret or create a new secret.
You can create the Secrets Manager secret in either the Amazon ECR console or the Secrets Manager console. To
create a Secrets Manager secret using the Secrets Manager console instead of the Amazon ECR console, see [Storing your upstream
repository credentials in an AWS Secrets Manager secret](pull-through-cache-creating-secret.md "pull-through-cache-creating-secret.md").

## Prerequisites

- Verify that you have the proper IAM permissions to create pull through cache rules. For
  information, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](pull-through-cache-iam.md "pull-through-cache-iam.md").
- For upstream registries that require authentication with secrets: If you want to use an
  existing secret, verify that the Secrets Manager secret meets the following
  requirements:
  - The name of the secret begins with `ecr-pullthroughcache/`. The AWS Management Console
    only displays Secrets Manager secrets with the `ecr-pullthroughcache/` prefix.
  - The account and Region that the secret is in must match the account and Region that the
    pull through cache rule is in.

## To create a pull

through cache rule (AWS Management Console)

The following steps show how to create a pull through cache rule and a Secrets Manager
secret using the Amazon ECR console. To create a secret using the Secrets Manager console, see [Storing your upstream
repository credentials in an AWS Secrets Manager secret](pull-through-cache-creating-secret.md "pull-through-cache-creating-secret.md").

1.  Open the Amazon ECR console at
    [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2.  From the navigation bar, choose the Region to configure your
    private registry settings in.
3.  In the navigation pane, choose **Private
    registry**, **Pull through
    cache**.
4.  On the **Pull through cache configuration**
    page, choose **Add rule**.
5.  On the **Step 1: Specify a source** page, for
    **Registry**, choose either Amazon ECR Public,
    Kubernetes, or Quay from the list of upstream registries and
    then choose **Next**.
6.  On the **Step 2: Specify a destination**
    page, for **Amazon ECR repository prefix**, specify
    the repository namespace prefix to use when caching images
    pulled from the source public registry and then choose
    **Next**. By default, a namespace is
    populated but a custom namespace can be specified as
    well.
7.  On the **Step 3: Review and create** page,
    review the pull through cache rule configuration and then choose
    **Create**.
8.  Repeat the previous step for each pull through cache you want
    to create. The pull through cache rules are created separately
    for each Region.
9.  Open the Amazon ECR console at
    [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
10. From the navigation bar, choose the Region to configure your
    private registry settings in.
11. In the navigation pane, choose **Private
    registry**, **Pull through
    cache**.
12. On the **Pull through cache configuration**
    page, choose **Add rule**.
13. On the **Step 1: Specify a source** page, for
    **Registry**, choose
    **Docker Hub**, **Next**.
14. On the **Step 2: Configure authentication**
    page, for **Upstream credentials**, you must
    store your authentication credentials for Docker Hub in an AWS Secrets Manager
    secret. You can specify an existing secret or use the Amazon ECR
    console to create a new secret.
    1. To use an existing secret, choose **Use an
       existing AWS secret**. For **Secret name** use the drop down
       to select your existing secret, and then choose **Next**.

    ###### Note

    The AWS Management Console only displays Secrets Manager secrets with
    names using the `ecr-pullthroughcache/`
    prefix. The secret must also be in the same account
    and Region that the pull through cache rule is
    created in. 2. To create a new secret, choose **Create an
    AWS secret**, do the following, then
    choose **Next**.

        1. For **Secret name**, specify
         a descriptive name for the secret. Secret names
         must contain 1-512 Unicode characters.
        2. For **Docker Hub email**, specify
         your Docker Hub email.
        3. For **Docker Hub access token**,
         specify your Docker Hub access token. For more
         information on creating a Docker Hub access token, see
         [Create and manage access tokens](https://docs.docker.com/security/for-developers/access-tokens/ "https://docs.docker.com/security/for-developers/access-tokens/") in the
         Docker documentation.

15. On the **Step 3: Specify a destination**
    page, for **Amazon ECR repository prefix**, specify
    the repository namespace to use when caching images pulled from
    the source public registry and then choose
    **Next**.

By default, a namespace is populated but a custom namespace
can be specified as well. 8. On the **Step 4: Review and create** page,
review the pull through cache rule configuration and then choose
**Create**. 9. Repeat the previous step for each pull through cache you want
to create. The pull through cache rules are created separately
for each Region.

1.  Open the Amazon ECR console at
    [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2.  From the navigation bar, choose the Region to configure your
    private registry settings in.
3.  In the navigation pane, choose **Private
    registry**, **Pull through
    cache**.
4.  On the **Pull through cache configuration**
    page, choose **Add rule**.
5.  On the **Step 1: Specify a source** page, for
    **Registry**, choose
    **GitHub Container Registry**, **Next**.
6.  On the **Step 2: Configure authentication**
    page, for **Upstream credentials**, you must
    store your authentication credentials for GitHub Container Registry in an AWS Secrets Manager
    secret. You can specify an existing secret or use the Amazon ECR
    console to create a new secret.
    1. To use an existing secret, choose **Use an
       existing AWS secret**. For **Secret name** use the drop down
       to select your existing secret, and then choose **Next**.

    ###### Note

    The AWS Management Console only displays Secrets Manager secrets with
    names using the `ecr-pullthroughcache/`
    prefix. The secret must also be in the same account
    and Region that the pull through cache rule is
    created in. 2. To create a new secret, choose **Create an
    AWS secret**, do the following, then
    choose **Next**.

        1. For **Secret name**, specify
         a descriptive name for the secret. Secret names
         must contain 1-512 Unicode characters.
        2. For **GitHub Container Registry
         username**, specify your GitHub Container
         Registry username.
        3. For **GitHub Container Registry access
         token**, specify your GitHub Container
         Registry access token. For more information on
         creating a GitHub access token, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens") in
         the GitHub documentation.

7.  On the **Step 3: Specify a destination**
    page, for **Amazon ECR repository prefix**, specify
    the repository namespace to use when caching images pulled from
    the source public registry and then choose
    **Next**.

By default, a namespace is populated but a custom namespace
can be specified as well. 8. On the **Step 4: Review and create** page,
review the pull through cache rule configuration and then choose
**Create**. 9. Repeat the previous step for each pull through cache you want
to create. The pull through cache rules are created separately
for each Region.

1.  Open the Amazon ECR console at
    [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2.  From the navigation bar, choose the Region to configure your
    private registry settings in.
3.  In the navigation pane, choose **Private
    registry**, **Pull through
    cache**.
4.  On the **Pull through cache configuration**
    page, choose **Add rule**.
5.  On the **Step 1: Specify a source** page, do
    the following.
    1. For **Registry**, choose
       **Microsoft Azure Container Registry**
    2. For **Source registry URL**, specify
       the name of your Microsoft Azure container registry and then choose
       **Next**.

    ###### Important

    You only need to specify the prefix, as the
    `.azurecr.io` suffix is populated on
    your behalf.

6.  On the **Step 2: Configure authentication**
    page, for **Upstream credentials**, you must
    store your authentication credentials for Microsoft Azure Container Registry in an AWS Secrets Manager
    secret. You can specify an existing secret or use the Amazon ECR
    console to create a new secret.
    1. To use an existing secret, choose **Use an
       existing AWS secret**. For **Secret name** use the drop down
       to select your existing secret, and then choose **Next**.

    ###### Note

    The AWS Management Console only displays Secrets Manager secrets with
    names using the `ecr-pullthroughcache/`
    prefix. The secret must also be in the same account
    and Region that the pull through cache rule is
    created in. 2. To create a new secret, choose **Create an
    AWS secret**, do the following, then
    choose **Next**.

        1. For **Secret name**, specify
         a descriptive name for the secret. Secret names
         must contain 1-512 Unicode characters.
        2. For **Microsoft Azure Container Registry username**,
         specify your Microsoft Azure Container Registry username.
        3. For **Microsoft Azure Container Registry access token**,
         specify your Microsoft Azure Container Registry access token. For more
         information on creating an Microsoft Azure Container Registry access token, see
         [Create token - portal](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-repository-scoped-permissions#create-token---portal "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-repository-scoped-permissions#create-token---portal") in the Microsoft Azure
         documentation.

7.  On the **Step 3: Specify a destination**
    page, for **Amazon ECR repository prefix**, specify
    the repository namespace to use when caching images pulled from
    the source public registry and then choose
    **Next**.

By default, a namespace is populated but a custom namespace
can be specified as well. 8. On the **Step 4: Review and create** page,
review the pull through cache rule configuration and then choose
**Create**. 9. Repeat the previous step for each pull through cache you want
to create. The pull through cache rules are created separately
for each Region.

1.  Open the Amazon ECR console at
    [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2.  From the navigation bar, choose the Region to configure your
    private registry settings in.
3.  In the navigation pane, choose **Private
    registry**, **Pull through
    cache**.
4.  On the **Pull through cache configuration**
    page, choose **Add rule**.
5.  On the **Step 1: Specify a source** page, for Registry,
    choose GitLab Container Registry, Next.
6.  On the **Step 2: Configure authentication**
    page, for **Upstream credentials**, you must
    store your authentication credentials for GitLab Container Registry in an AWS Secrets Manager
    secret. You can specify an existing secret or use the Amazon ECR
    console to create a new secret.
    1. To use an existing secret, choose **Use an
       existing AWS secret**. For
       **Secret name** use the drop down
       to select your existing secret, and then choose
       **Next**. For more information on
       creating a Secrets Manager secret using the Secrets Manager console, see
       [Storing your upstream
       repository credentials in an AWS Secrets Manager secret](pull-through-cache-creating-secret.md "pull-through-cache-creating-secret.md").

    ###### Note

    The AWS Management Console only displays Secrets Manager secrets with
    names using the `ecr-pullthroughcache/`
    prefix. The secret must also be in the same account
    and Region that the pull through cache rule is
    created in. 2. To create a new secret, choose **Create an
    AWS secret**, do the following, then
    choose **Next**.

        1. For **Secret name**, specify
         a descriptive name for the secret. Secret names
         must contain 1-512 Unicode characters.
        2. For **GitLab Container Registry username**,
         specify your GitLab Container Registry username.
        3. For **GitLab Container Registry access token**,
         specify your GitLab Container Registry access token. For more
         information on creating a GitLab Container Registry access token, see
         [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html "https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html"),
         [Group access tokens](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html "https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html"), or
         [Project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html "https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html"),
         in the GitLab documentation.

7.  On the **Step 3: Specify a destination**
    page, for **Amazon ECR repository prefix**, specify
    the repository namespace to use when caching images pulled from
    the source public registry and then choose
    **Next**.

By default, a namespace is populated but a custom namespace
can be specified as well. 8. On the **Step 4: Review and create** page,
review the pull through cache rule configuration and then choose
**Create**. 9. Repeat the previous step for each pull through cache you want
to create. The pull through cache rules are created separately
for each Region.

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region in which you want to
   configure your private registry settings.
3. In the navigation pane, choose **Private
   registry**, **Pull through
   cache**.
4. On the **Pull through cache configuration**
   page, choose **Add rule**.
5. On the **Step 1: Specify upstream** page, for
   **Registry**, choose **Amazon ECR Private** and
   **This account**. For **Region**, select the
   Region for the upstream Amazon ECR registry, and then choose **Next**.
6. On the **Step 2: Specify namespaces** page, for
   **Cache namespace**, choose whether to create
   pull through cache repositories with **A
   specific prefix** or **no
   prefix**. If you select **A
   specific prefix**, you must specify a prefix name to be
   used as part of the namespace for caching images from the upstream
   registry.
7. For **Upstream namespace**, choose whether to
   pull from **A specific prefix** that
   exists in the upstream registry. If you select **no prefix**, you can pull from any repository in the
   upstream registry. Specify the upstream repository prefix if
   prompted, and then choose **Next**.

###### Note

To learn more about customizing cache and upstream namespaces,
see [Customizing repository prefixes
for ECR to ECR pull through cache](pull-through-cache-private-wildcards.md "pull-through-cache-private-wildcards.md"). 8. On the **Step 3: Review and create** page,
review the pull through cache rule configuration and then choose
**Create**. 9. Repeat these steps for each pull through cache you want to create.
The pull through cache rules are created separately for each
Region.

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region to configure your
   private registry settings in.
3. In the navigation pane, choose **Private
   registry**, **Pull through
   cache**.
4. On the **Pull through cache configuration**
   page, choose **Add rule**.
5. On the **Step 1: Specify upstream** page, for
   **Registry**, choose **Amazon ECR Private** and
   **Cross account**. For **Region**, select the
   Region for the upstream Amazon ECR registry. For **Account**, specify
   the AWS account ID for the upstream Amazon ECR registry, and then choose **Next**.
6. On the **Step 2: Specify permissions** page, for
   **IAM role**, select a role to be used for cross account pull through cache access and then choose
   **Create**.

###### Note

Make sure that you select the IAM role which uses the permissions created in [IAM policies
required for cross-account ECR to ECR pull through cache](pull-through-cache-private.md#pull-through-cache-private-permissions "pull-through-cache-private.md#pull-through-cache-private-permissions"). 7. On the **Step 3: Specify namespaces** page, for
**Cache namespace**, choose whether to create
pull through cache repositories with **A
specific prefix** or **no
prefix**. If you select **A
specific prefix**, you must specify a prefix name to be
used as part of the namespace for caching images from the upstream
registry. 8. For **Upstream namespace**, choose whether to
pull from **A specific prefix** that
exists in the upstream registry. If you select **no prefix**, you can pull from any repository in the
upstream registry. Specify the upstream repository prefix if
prompted, and then choose **Next**.

###### Note

To learn more about customizing cache and upstream namespaces,
see [Customizing repository prefixes
for ECR to ECR pull through cache](pull-through-cache-private-wildcards.md "pull-through-cache-private-wildcards.md"). 9. On the **Step 4: Review and create** page,
review the pull through cache rule configuration and then choose
**Create**. 10. Repeat these steps for each pull through cache you want to create.
The pull through cache rules are created separately for each
Region.

## To create a pull through

cache rule (AWS CLI)

Use the [create-pull-through-cache-rule](../../../cli/latest/reference/ecr/create-pull-through-cache-rule.md "../../../cli/latest/reference/ecr/create-pull-through-cache-rule.md") AWS CLI command to create a pull through
cache rule for an Amazon ECR private registry. For upstream registries that require
authentication with secrets, you must store the credentials in an Secrets Manager secret. To
create a secret using the Secrets Manager console, see [Storing your upstream
repository credentials in an AWS Secrets Manager secret](pull-through-cache-creating-secret.md "pull-through-cache-creating-secret.md").

The following examples are provided for each supported upstream
registry.

The following example creates a pull through cache rule for the Amazon ECR
Public registry. It specifies a repository prefix of
`ecr-public`, which results in each repository created
using the pull through cache rule to have the naming scheme of
`ecr-public/`upstream-repository-name``.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `ecr-public` \
 --upstream-registry-url public.ecr.aws \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the
Kubernetes public registry. It specifies a repository prefix of
`kubernetes`, which results in each repository created
using the pull through cache rule to have the naming scheme of
`kubernetes/`upstream-repository-name``.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `kubernetes` \
 --upstream-registry-url registry.k8s.io \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the Quay
public registry. It specifies a repository prefix of `quay`,
which results in each repository created using the pull through cache
rule to have the naming scheme of
`quay/`upstream-repository-name``.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `quay` \
 --upstream-registry-url quay.io \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the Docker Hub
registry. It specifies a repository prefix of `docker-hub`,
which results in each repository created using the pull through cache
rule to have the naming scheme of
`docker-hub/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your Docker Hub credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `docker-hub` \
 --upstream-registry-url registry-1.docker.io \
 --credential-arn arn:aws:secretsmanager:`us-east-2`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the GitHub Container Registry.
It specifies a repository prefix of `github`, which results in
each repository created using the pull through cache rule to have the naming
scheme of
`github/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your GitHub Container Registry credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `github` \
 --upstream-registry-url ghcr.io \
 --credential-arn arn:aws:secretsmanager:`us-east-2`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the Microsoft Azure Container Registry.
It specifies a repository prefix of `azure`, which
results in each repository created using the pull through cache rule to
have the naming scheme of
`azure/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your Microsoft Azure Container Registry credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `azure` \
 --upstream-registry-url `myregistry`.azurecr.io \
 --credential-arn arn:aws:secretsmanager:`us-east-2`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the GitLab Container Registry.
It specifies a repository prefix of `gitlab`, which
results in each repository created using the pull through cache rule to
have the naming scheme of
`gitlab/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your GitLab Container Registry credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `gitlab` \
 --upstream-registry-url registry.gitlab.com \
 --credential-arn arn:aws:secretsmanager:`us-east-2`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the Amazon ECR
private registry for cross-Region within the same AWS account. It
specifies a repository prefix of `ecr`, which results in each
repository created using the pull through cache rule to have the naming
scheme of
`ecr/`upstream-repository-name``.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix ecr \
 --upstream-registry-url `aws_account_id`.dkr.ecr.`region`.amazonaws.com \
 --region `us-east-2``
```

The following example creates a pull through cache rule for the Amazon ECR private registry
for cross-Region within the same AWS account. It
specifies a repository prefix of `ecr`, which results in each
repository created using the pull through cache rule to have the naming
scheme of
`ecr/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the IAM role with
the permissions created in [Creating a pull through cache rule in Amazon ECR](pull-through-cache-creating-rule.md "pull-through-cache-creating-rule.md").

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix ecr \
 --upstream-registry-url `aws_account_id`.dkr.ecr.`region`.amazonaws.com \
 --custom-role-arn arn:aws:iam::`aws_account_id`:role/`example-role` \
 --region `us-east-2``
```

## Next steps

After you create your pull through cache rules, the following are the next
steps:

- Create a repository creation template. A repository creation template
  gives you control to define the settings to use for new repositories
  created by Amazon ECR on your behalf during a pull through cache action. For
  more information, see [Templates to control repositories created
  during a pull through cache or replication action](repository-creation-templates.md "repository-creation-templates.md").
- Validate your pull through cache rules. When validating a pull through
  cache rule, Amazon ECR makes a network connection with the upstream registry,
  verifies that it can access the Secrets Manager secret containing the credentials
  for the upstream registry, and that authentication was successful. For
  more information, see [Validating pull
  through cache rules in Amazon ECR](pull-through-cache-working-validating.md "pull-through-cache-working-validating.md").
- Start using your pull through cache rules. For more information, see
  [Pulling an image with a
  pull through cache rule in Amazon ECR](pull-through-cache-working-pulling.md "pull-through-cache-working-pulling.md").
