

# Using third-party registries not supported by pull through cache
<a name="containers-non-ptc-registries"></a>

Your workflow can use container images from upstream registries that Amazon ECR pull through cache (PTC) doesn't support. The first time a task from your run needs one of these images, HealthOmics copies it from the upstream registry into a private Amazon ECR repository in your account and starts the task from the copy. Later tasks and runs reuse the copy, so the download happens only once. If several runs need the same image at the same time, for example, runs in a batch, HealthOmics copies the image once and the runs wait for that copy. Your workflow definition keeps the original upstream image URIs, so you don't pull, push, or rewrite image URIs yourself.

We recommend that you reference these images by digest or version instead of by tag. For more information, see [Use a digest or version instead of a tag for non-PTC images](containers-best-practices.md#containers-best-practices-non-ptc-pin).

HealthOmics supports the following upstream registries that PTC doesn't support:
+ Seqera Containers (`community.wave.seqera.io` and `wave.seqera.io`)
+ NVIDIA NGC (`nvcr.io`)
+ Google Container Registry (`gcr.io`)
+ Google Artifact Registry (`{{region}}-docker.pkg.dev`). Use the full regional host, for example `us-central1-docker.pkg.dev`.

**Topics**
+ [Configuring non-PTC container support](#configure-non-ptc)
+ [Destination repository naming](#ecr-non-ptc-destination)
+ [Considerations for non-PTC container support](#ecr-non-ptc-considerations)

## Configuring non-PTC container support
<a name="configure-non-ptc"></a>

Before you use containers from registries that PTC doesn't support, store your registry credentials and set up permissions for HealthOmics.

### Step 1: Store your registry credential in Secrets Manager
<a name="ecr-non-ptc-credential"></a>

HealthOmics authenticates and copies container images from upstream registries using your credentials. You store your credentials as a secret in the same AWS Region as your HealthOmics runs. You can also use a secret from a different AWS account or share your secret with another account. When you use a secret from a different AWS account, the service role that you pass to **StartRun** must be allowed to read the secret. For more information, see [Access Secrets Manager secrets from a different account](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples_cross.html) in the *Secrets Manager User Guide*.

Every supported registry needs a credential, including registries that allow anonymous pulls, such as `community.wave.seqera.io`.

The following tabs show the credential format and an example for each supported registry.

------
#### [ Seqera Containers and Wave ]

A JSON object with a single `accessToken` key that holds a Seqera Platform access token.

The following AWS CLI command creates a secret for Seqera Containers:

```
aws secretsmanager create-secret \
     --name {{omics-registry/seqera}} \
     --secret-string '{"accessToken":"{{seqera-platform-access-token}}"}' \
     --region {{us-east-1}}
```

------
#### [ NVIDIA NGC ]

A JSON object with `username` set to the literal `$oauthtoken` and `accessToken` set to your NGC API key.

The following AWS CLI command creates a secret for NVIDIA NGC:

```
aws secretsmanager create-secret \
     --name {{omics-registry/nvidia-ngc}} \
     --secret-string '{"username":"$oauthtoken","accessToken":"{{ngc-api-key}}"}' \
     --region {{us-east-1}}
```

When you create a secret for NVIDIA NGC, keep the `--secret-string` value in single quotes so that your shell doesn't expand `$oauthtoken`.

------
#### [ Google Container Registry and Google Artifact Registry ]

Create a JSON key for a Google Cloud service account that can read images from your registry, and save the key file (for example, `key.json`). For instructions, see [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete) in the Google Cloud documentation.

Set `username` to `_json_key` and `accessToken` to the contents of the key file as a single JSON string. The following AWS CLI command creates the secret and uses the `jq` tool to build the JSON string:

```
aws secretsmanager create-secret \
     --name {{omics-registry/google}} \
     --secret-string "$(jq -n --rawfile key {{key.json}} '{username: "_json_key", accessToken: $key}')" \
     --region {{us-east-1}}
```

------

You can record the Amazon Resource Name (ARN) of the secret from the response and use it as the `credentialArn` value in the registry mapping.

### Step 2: Grant permissions to the service role
<a name="ecr-non-ptc-run-role"></a>

HealthOmics uses the service role that you pass to `StartRun` to read the secret, create the destination repository, and push the copied image. The service role must be in the same AWS account as the run. Otherwise, HealthOmics rejects the role with the error IAM role does not match the requesting AWS account.

For the policy, see [Service role policy for non-PTC container support](permissions-ecr.md#permissions-ecr-non-ptc).

After you grant these permissions, add a registry mapping with the secret ARN as the `credentialArn`. For more information, see [Registry mappings](containers-workflow-creation.md#ecr-pull-through-registry-mapping).

## Destination repository naming
<a name="ecr-non-ptc-destination"></a>

You specify registry mappings when you create a workflow, and HealthOmics copies the images during a run. For more information, see [Adding private or third-party containers during workflow creation](containers-workflow-creation.md).

Each copied image lands at a URI that you can compute from the registry mapping:

```
{{account-id}}.dkr.ecr.{{region}}.amazonaws.com/{{ecrRepositoryPrefix}}/{{image-path}}:{{tag}}
```

`image-path` is the upstream image URI without the registry host, and without `upstreamRepositoryPrefix` if you set one. Keep `upstreamRepositoryPrefix` unset for Wave (`wave.seqera.io`). The account is the workflow's account, unless you set `ecrAccountId`. When you set `ecrAccountId`, HealthOmics creates the repository and pushes the copy in that account using your service role. The service role then needs the same Amazon ECR permissions on that account's repositories, and that account's registry and repository policies must allow it.

For example, `community.wave.seqera.io/library/samtools:1.22.1--eccb42ff8fb55509` with prefix `wave-seqera` lands at `111122223333.dkr.ecr.us-east-1.amazonaws.com/wave-seqera/library/samtools:1.22.1--eccb42ff8fb55509`.

To confirm that a copy succeeded, check that the image exists at its destination URI, for example with the following AWS CLI command:

```
aws ecr describe-images \
     --repository-name {{wave-seqera/library/samtools}} \
     --image-ids imageTag={{1.22.1--eccb42ff8fb55509}} \
     --region {{us-east-1}}
```

If the repository doesn't exist in the workflow's account, HealthOmics creates it. If the repository has no repository policy, HealthOmics attaches one that lets HealthOmics pull the image. If the repository already has a policy, HealthOmics leaves it unchanged, so include a statement that lets HealthOmics pull images. For an example, see [Create a resource policy for the Amazon ECR repository](permissions-ecr.md#permissions-resource-policy).

`ecrRepositoryPrefix/image-path` becomes an Amazon ECR repository name, so the prefix must use lowercase letters, numbers, and the characters `/`, `-`, `_`, and `.`.

If your workflows in the same account share an `ecrRepositoryPrefix`, they share the copied images. If you delete a copied image, it affects every workflow that uses that image with that prefix.

## Considerations for non-PTC container support
<a name="ecr-non-ptc-considerations"></a>

Consider the following when you use non-PTC container support:
+ Architecture – HealthOmics copies x86\_64 images only. ARM-based and multi-architecture images aren't supported.
+ Workflow sharing – Non-PTC container support isn't supported for shared workflows. When another account runs a workflow that you shared, HealthOmics ignores registry mappings that include `credentialArn`.
+ Image tags – HealthOmics copies the image that a tag, such as `latest`, points to and doesn't refresh the copy when the upstream content changes. To pick up the new content, delete the copied image from Amazon ECR. After you delete it, HealthOmics copies the image again from the upstream registry on the next run that needs it. If your workflow references a new tag or digest, HealthOmics copies that image the first time a task needs it.
+ Copy failures – If the registry credential is invalid, or the service role doesn't have the permissions that HealthOmics needs, the image copy fails, and the task and the run fail. If a copy of the image already exists in Amazon ECR, HealthOmics uses that copy and doesn't check the registry credential.