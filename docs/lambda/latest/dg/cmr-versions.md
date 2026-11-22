

# Runtime versions

A runtime version holds the contents of a customer-managed runtime. You publish it from a container image in Amazon Elastic Container Registry (Amazon ECR). Each time you update your runtime, for example to apply a patch, you publish a new runtime version. This topic is for runtime publishers. It explains how runtime versions work and how to manage them.

For an overview of customer-managed runtimes, see [Customer-managed runtimes](runtimes-customer-managed.md).

## How runtime versions work
<a name="cmr-publish-versions-about"></a>

A runtime version is a child of a runtime. An image in Amazon ECR defines what each version contains. Versions are immutable. After you create a version, you can't change its image or capabilities. To change the runtime, you create a new version.

Each version has two identifiers:
+ **Version name** – A name that you choose when you create the version, such as `v8.3.1`. For more information, see [Version names](#cmr-publish-versions-names).
+ **Version ARN** – An Amazon Resource Name (ARN) that Lambda builds from the runtime ARN and the version name. The format is `arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}}/version/{{version-name}}`.

  For example: `arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1`

No function uses a new version until you point a runtime alias to it. As a result, you can test a new version before you release it. How you test depends on whether this is the first version of the runtime:
+ **First version** – Every function that uses a customer-managed runtime must specify a runtime alias. Before you can test the first version, create a test alias, such as `dev`, that points to it. Then create a test function that uses that alias, and invoke the function. For more information, see [Create a runtime alias](cmr-aliases.md#cmr-aliases-create) and [Create a function that uses a customer-managed runtime](cmr-using.md#cmr-using-create).
+ **Later versions** – Pin a test function to the new version with the **Manual** runtime update mode. You can also point a test alias that only your test functions use, such as `dev`, to the new version. For more information, see [Using a customer-managed runtime](cmr-using.md) and [Deploying runtime updates](cmr-deploy-updates.md).

To release the version, point an alias to it. For more information, see [Runtime aliases](cmr-aliases.md).

After you create a runtime version, you can change only its release notes. For more information, see [Update release notes](#cmr-publish-versions-update-notes).

## Version names
<a name="cmr-publish-versions-names"></a>

You choose a name for each runtime version. The name is part of the version ARN. Names must meet the following requirements:
+ Contain 1–128 characters
+ Contain only uppercase and lowercase letters, numbers, underscores (`_`), periods (`.`), and hyphens (`-`)
+ Start and end with a letter, number, or underscore
+ Be unique within the runtime

We recommend names that show the order of your releases. Common schemes include the following:
+ **Semantic versioning** – For example, `v8.3.1`. Use this scheme when names track the language or your own release numbers.
+ **Date-based versioning** – For example, `2026-01-25.1`. Use this scheme when you rebuild the runtime on a schedule, such as for security patches.

## How Lambda processes your container image
<a name="cmr-publish-versions-image-processing"></a>

When you create a version, you give the URI of an image in Amazon ECR. The URI can use a tag, such as `companyphp8:v8.3.1`, or a digest. Lambda then does the following:

1. Resolves the URI to an image digest, and returns it in the `ResolvedUri` field. The version always uses this digest. If you later move the tag to a new image, the version doesn't change.

1. Reads the platforms from the image manifest, and returns them in the `Platforms` field. Lambda uses them to find the supported architectures.

1. Reads the compatibility settings from the image. For more information, see [Runtime version compatibility](#cmr-publish-versions-compatibility).

1. Ingests and optimizes the image for use with functions. During this step, the version is in the `CREATING` state. When it's done, the version moves to `ACTIVE` or `FAILED`.

The `ResolvedUri`, `Platforms`, and `Compatibility` fields appear as soon as you create the version. They don't change when the version becomes `ACTIVE`.

## Supported architectures
<a name="cmr-publish-versions-architectures"></a>

Lambda reads the supported [instruction set architectures](foundation-arch.md) from the image. You don't set them yourself.
+ **Single-architecture image** – The version supports one architecture: `x86_64` or `arm64`.
+ **Multi-architecture image** – If the URI points to a manifest list (image index) with both architectures, the version supports `x86_64` and `arm64`. Lambda uses the image that matches each function's architecture.

A version shows architectures in two fields, which use different names:
+ `Platforms` – Lists each platform in the image manifest. The `Architecture` value uses Open Container Initiative (OCI) names, such as `amd64` and `arm64`.
+ `Compatibility.Architectures` – Lists the architectures in Lambda terms, such as `x86_64` and `arm64`. The OCI name `amd64` is the same as `x86_64` in Lambda.

A new version can support different architectures than earlier versions. For example, you can add `arm64` by publishing a multi-architecture version. However, you can point an alias to a version only if the version supports at least the architectures that the alias declares. For more information, see [Alias compatibility](cmr-aliases.md#cmr-aliases-compatibility). For instructions on building multi-architecture images, see [Building runtime images](cmr-building-images.md).

## Runtime version compatibility
<a name="cmr-publish-versions-compatibility"></a>

Each version has a `Compatibility` object. It shows which features and architectures the version works with, such as the integration model, the supported architectures, and whether functions on [Lambda Managed Instances](lambda-managed-instances.md) can use the version. Lambda reads these values from the labels and platforms in the version's container image. If the image doesn't declare an integration model, Lambda uses `RuntimeAPI`. For more information about the labels that set a runtime's compatibility, see [Architectures and feature compatibility](cmr-building-images.md#cmr-building-images-capabilities).

You can't set the `Compatibility` object in the `CreateRuntimeVersion` request, and you can't change it after you create the version. The `Compatibility` object is read-only on a version. To change a version's compatibility, build a new image and publish a new version.

To view a version's compatibility, use the `get-runtime-version` command and check the `Compatibility` field. For more information, see [View runtime versions](#cmr-publish-versions-view).

## Runtime version states
<a name="cmr-publish-versions-states"></a>

The `State` field shows the status of a version. The following table describes each state.


**Runtime version states**  

| State | Description | 
| --- | --- | 
| CREATING | Lambda is processing the image. You can't point an alias to the version or edit its release notes yet. | 
| ACTIVE | The version is ready. You can point an alias to it, pin a function to it, and edit its release notes. | 
| FAILED | Lambda couldn't process the image. You can't use the version. For more information, see [If the version fails](#cmr-publish-versions-troubleshoot). | 
| PENDING\_DELETION | The version is scheduled for deletion. Functions can't use it, and you can't modify it. You can restore it until the waiting period ends. For more information, see [Resources scheduled for deletion](cmr-delete.md#cmr-delete-pending). | 
| DELETING | Lambda is deleting the version. | 

An alias can point only to an `ACTIVE` version. Wait until the version is `ACTIVE` before you point an alias to it.

When you delete a version, Lambda schedules it for deletion and permanently deletes it after a waiting period that you choose, from 7 to 30 days. The default is 30 days. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

## Amazon ECR requirements
<a name="cmr-publish-versions-ecr"></a>

The image for a runtime version must meet the following requirements:
+ **Repository location** – The Amazon ECR repository must be in the same AWS Region as the runtime. The repository can be in a different AWS account. To use a runtime in more than one Region, replicate the image to a repository in each Region. For more information, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).
+ **Lambda access** – The repository policy must grant the Lambda service principal permission to read the image. For instructions, see [Grant Lambda access to your Amazon ECR repository](#cmr-publish-versions-grant-ecr).
+ **Image retention** – You must keep the image in Amazon ECR while the version exists. If you delete the image, functions that use the version become `Inactive`. This change can take up to 24 hours. Existing execution environments continue to handle invocations, but invocations that require a cold start fail. Deleting the repository or removing Lambda's access to the image has the same effect. The functions recover automatically after you restore the image. The version refers to the image by digest (`ResolvedUri`), so the restored image must have an identical digest. For more information, see [Container images and charges](cmr-delete.md#cmr-delete-ecr). Standard Amazon ECR storage charges apply. Lambda doesn't charge for runtime versions. For more information, see [Amazon ECR pricing](https://aws.amazon.com/ecr/pricing/).
+ **Image size** – For the maximum size of a runtime image, see [Customer-managed runtimes](gettingstarted-limits.md#cmr-quotas) in [Lambda quotas](gettingstarted-limits.md).

Runtime consumers don't need access to your Amazon ECR images. They need only permission to use the runtime. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Required permissions
<a name="cmr-publish-versions-iam"></a>

To manage runtime versions, your IAM identity needs the following permissions:
+ `lambda:CreateRuntimeVersion` – Create a runtime version.
+ `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` on the Amazon ECR repository that contains the image – Create a runtime version from the image. The resource is the repository ARN, for example `arn:aws:ecr:us-east-1:123456789012:repository/companyphp8`.
+ `lambda:GetRuntimeVersion` – View a runtime version.
+ `lambda:ListRuntimeVersions` – List the versions of a runtime.
+ `lambda:UpdateRuntimeVersion` – Edit the release notes of a version.
+ `lambda:DeleteRuntimeVersion` – Delete a runtime version.

To create a runtime version, you need both Amazon ECR actions in addition to `lambda:CreateRuntimeVersion`. This requirement also applies to dry runs. Your identity needs these Amazon ECR permissions even after you grant Lambda access in the repository policy. If your identity lacks either Amazon ECR action, the request fails.

To grant Lambda access to your repository, you also need `ecr:SetRepositoryPolicy`. For more information about permissions, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Prerequisites
<a name="cmr-publish-versions-prerequisites"></a>

Before you start, you need the following:
+ A runtime. For instructions, see [Creating a runtime](cmr-create.md).
+ A runtime image pushed to an Amazon ECR repository. For instructions, see [Building runtime images](cmr-building-images.md).
+ The AWS CLI, if you use the command line. The examples use a runtime and an Amazon ECR repository named `companyphp8` in `us-east-1`.

## Grant Lambda access to your Amazon ECR repository
<a name="cmr-publish-versions-grant-ecr"></a>

Lambda must be able to read your runtime image from Amazon ECR. To allow this, add a repository policy for the Lambda service principal. You do this one time for each repository.

Lambda uses `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` to read the image. Lambda also needs `ecr:DescribeImages` when functions that use the runtime run on [Lambda Managed Instances](lambda-managed-instances.md).

**To grant Lambda access to an Amazon ECR repository (AWS CLI)**

1. Create a file named `ecr-policy.json` with the following content:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "LambdaReadAccess",
         "Effect": "Allow",
         "Principal": {
           "Service": "lambda.amazonaws.com"
         },
         "Action": [
           "ecr:BatchGetImage",
           "ecr:DescribeImages",
           "ecr:GetDownloadUrlForLayer"
         ],
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "123456789012"
           },
           "ArnLike": {
             "aws:SourceArn": "arn:aws:lambda:us-east-1:123456789012:runtime/*"
           }
         }
       }
     ]
   }
   ```

   The conditions restrict access to runtimes in your account. The value of `aws:SourceArn` is the runtime ARN, not the runtime version ARN.

1. Run the following command to apply the policy to your repository:

   ```bash
   aws ecr set-repository-policy \
     --repository-name companyphp8 \
     --policy-text file://ecr-policy.json \
     --region us-east-1
   ```

The command returns the repository name and policy. If the repository has a policy, this command replaces it. To keep your current statements, add the `LambdaReadAccess` statement to your policy instead. For more information, see [Setting a private repository policy statement](https://docs.aws.amazon.com/AmazonECR/latest/userguide/set-repository-policy.html) in the *Amazon Elastic Container Registry User Guide*.

## Create a runtime version
<a name="cmr-publish-versions-create"></a>

You can create a runtime version by using the Lambda console or the AWS CLI. Before you use the version, wait until it's `ACTIVE`.

### Create a runtime version (console)
<a name="cmr-publish-versions-create-console"></a>

**To create a runtime version (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime, and then choose the **Versions** tab.

1. Choose **Create version**.

1. For **Runtime version name**, enter a name for the version. The version name must be unique for this runtime.

1. For **Image source**, do one of the following:
   + To use an image in your account, make sure that **Owned by you** is selected. Choose **Browse ECR**, and then select the Amazon ECR repository and the runtime version image.
   + To use an image that another account shared with you, select **Shared with you**, and then paste the URI of the container image.

1. Optionally, enter **Release notes** for the runtime version.

1. Choose **Create version**.

The new runtime version starts in the `CREATING` state. After Lambda ingests and processes the Amazon ECR image, the version moves to the `ACTIVE` state and is ready to use.

### Create a runtime version (AWS CLI)
<a name="cmr-publish-versions-create-cli"></a>

**To create a runtime version (AWS CLI)**

1. (Optional) To check the request without creating a version, add the `--dry-run` option:

   ```bash
   aws lambda-core create-runtime-version \
     --runtime-name companyphp8 \
     --name v8.3.1 \
     --image-uri 123456789012.dkr.ecr.us-east-1.amazonaws.com/companyphp8:v8.3.1 \
     --dry-run
   ```

   A dry run checks the image URI, that the image exists, that Lambda can access it, and that the version name is valid and not in use. If the checks pass, the command returns the version details that Lambda would create, but doesn't create the version. A dry run doesn't check that the runtime exists.

1. To create the version, run the `create-runtime-version` command:

   ```bash
   aws lambda-core create-runtime-version \
     --runtime-name companyphp8 \
     --name v8.3.1 \
     --image-uri 123456789012.dkr.ecr.us-east-1.amazonaws.com/companyphp8:v8.3.1 \
     --release-notes "Updates PHP to 8.3.1 and applies the latest OS security patches."
   ```

   The command uses the following options:
   + `--runtime-name` – The name or ARN of the runtime.
   + `--name` – The name of the new version.
   + `--image-uri` – The image URI in Amazon ECR, with a tag or a digest.
   + `--release-notes` – (Optional) What changed in this version.

   The following example shows the output for a multi-architecture image. The version is `CREATING`.

   ```json
   {
       "Name": "v8.3.1",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1",
       "ResolvedUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/companyphp8@sha256:9b2c4e7a1d3f5a8c6e0b2d4f6a8c0e2b4d6f8a0c2e4b6d8f0a2c4e6b8d0f2a4c",
       "State": "CREATING",
       "ReleaseNotes": "Updates PHP to 8.3.1 and applies the latest OS security patches.",
       "Platforms": [
           {
               "Architecture": "amd64",
               "Os": "linux",
               "Digest": "sha256:3e5a7c9b1d2f4a6c8e0b1d3f5a7c9e1b3d5f7a9c1e3b5d7f9a1c3e5b7d9f1a3e"
           },
           {
               "Architecture": "arm64",
               "Os": "linux",
               "Digest": "sha256:7c1e3a5b9d2f4c6e8a0b2d4f6c8e0a2b4d6f8c0e2a4b6d8f0c2e4a6b8d0f2c4e"
           }
       ],
       "Compatibility": {
           "IntegrationModels": [
               "RuntimeAPI"
           ],
           "Architectures": [
               "x86_64",
               "arm64"
           ],
           "ManagedInstances": "Supported"
       },
       "Created": "2026-10-05T10:53:38.719Z",
       "LastModified": "2026-10-05T10:53:39.260Z"
   }
   ```

1. To wait until the version is ready, run the following command:

   ```bash
   aws lambda-core wait runtime-version-active \
     --runtime-name companyphp8 \
     --name v8.3.1
   ```

   The command returns when the version is `ACTIVE`. If the version fails, the command returns an error.

1. To confirm the state, run the `get-runtime-version` command:

   ```bash
   aws lambda-core get-runtime-version \
     --runtime-name companyphp8 \
     --name v8.3.1 \
     --query State
   ```

   You should see the following output:

   ```json
   "ACTIVE"
   ```

When the version is `ACTIVE`, you can test it with a pinned function, and then point an alias to it. For more information, see [Next steps](#cmr-publish-versions-next-steps).

### If the version fails
<a name="cmr-publish-versions-troubleshoot"></a>

If Lambda can't process the image, the version enters the `FAILED` state. You can't use a failed version. To fix it, check the following:
+ The repository policy grants Lambda permission to read the image. For more information, see [Grant Lambda access to your Amazon ECR repository](#cmr-publish-versions-grant-ecr).
+ The image meets the requirements in [Amazon ECR requirements](#cmr-publish-versions-ecr).
+ The image is a valid runtime image. For more information, see [Building runtime images](cmr-building-images.md).

After you fix the issue, create a new version with a new name. You can delete the failed version. Its name stays reserved until Lambda permanently deletes it. After that, you can reuse the name. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

## View runtime versions
<a name="cmr-publish-versions-view"></a>

To view a version, including its platforms, run the `get-runtime-version` command:

```bash
aws lambda-core get-runtime-version \
  --runtime-name companyphp8 \
  --name v8.3.1
```

The output has the same fields as the output of `create-runtime-version`.

To list all versions of a runtime, run the `list-runtime-versions` command:

```bash
aws lambda-core list-runtime-versions \
  --runtime-name companyphp8
```

You should see output similar to the following:

```json
{
    "Items": [
        {
            "Name": "v8.3.1",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1",
            "ResolvedUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/companyphp8@sha256:9b2c4e7a1d3f5a8c6e0b2d4f6a8c0e2b4d6f8a0c2e4b6d8f0a2c4e6b8d0f2a4c",
            "State": "ACTIVE",
            "ReleaseNotes": "Updates PHP to 8.3.1 and applies the latest OS security patches.",
            "Compatibility": {
                "IntegrationModels": [
                    "RuntimeAPI"
                ],
                "Architectures": [
                    "x86_64",
                    "arm64"
                ],
                "ManagedInstances": "Supported"
            },
            "Created": "2026-10-05T10:53:38.719Z",
            "LastModified": "2026-10-05T10:53:46.031Z"
        }
    ]
}
```

The list output doesn't include the `Platforms` field. To see the platforms of a version, use `get-runtime-version`.

## Update release notes
<a name="cmr-publish-versions-update-notes"></a>

You can change only the release notes of a version. The version must be `ACTIVE`. The new notes replace the old ones.

------
#### [ Console ]

**To update release notes (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime, and then choose the **Versions** tab.

1. Select the check box next to the runtime version to update.

1. Choose **Version actions**, and then choose **Edit release notes**.

1. In the **Edit release notes for {{version}}** dialog box, edit the release notes.

1. Choose **Save**.

------
#### [ AWS CLI ]

To update the release notes, run the `update-runtime-version` command:

```bash
aws lambda-core update-runtime-version \
  --runtime-name companyphp8 \
  --name v8.3.1 \
  --release-notes "Updates PHP to 8.3.1 and applies OS security patches from October 2026."
```

The output shows the new notes in the `ReleaseNotes` field.

------

## Delete runtime versions
<a name="cmr-publish-versions-delete"></a>

You can delete versions that you don't need. You can't delete a version while a runtime alias points to it. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

## Next steps
<a name="cmr-publish-versions-next-steps"></a>

After your runtime version is `ACTIVE`, see the following topics:
+ To test the version with a function pinned to it, see [Using a customer-managed runtime](cmr-using.md).
+ To point a runtime alias to the version, see [Runtime aliases](cmr-aliases.md).
+ To roll out the version and monitor it, see [Deploying runtime updates](cmr-deploy-updates.md).