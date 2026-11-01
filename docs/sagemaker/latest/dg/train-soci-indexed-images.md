

# Speed up training job startup with SOCI-indexed images
<a name="train-soci-indexed-images"></a>

A training job downloads its container image before it runs your code. For large images, such as deep learning images, this adds minutes to every training job.

Seekable OCI (SOCI) is an open-source technology from AWS for loading container images on demand (*lazy loading*). For the project, see [soci-snapshotter](https://github.com/awslabs/soci-snapshotter) on the GitHub website.

How it works:
+ Most container runtimes download the whole image before they start the container, even though the container needs only a small part of it to start.
+ A SOCI index maps the files inside each layer of the image, so the runtime can read one file without downloading the whole layer.
+ You create the index from your existing image. You don't rebuild the image. The index is stored next to the image in Amazon ECR.
+ When the training job starts, the runtime downloads only the files needed to start the container. The rest is downloaded in the background as your code uses it.

SOCI-indexed images start Amazon SageMaker AI training containers in seconds, cutting GPU idle time during image pulls by up to 90%, with no impact on training performance.

To use it, reference a SOCI-indexed image in your `CreateTrainingJob` request. Nothing else in the training job changes.

**Topics**
+ [How it works](#train-soci-indexed-images-how)
+ [Considerations](#train-soci-indexed-images-considerations)
+ [Use a Deep Learning Container that includes a SOCI index](#train-soci-indexed-images-dlc)
+ [Create a SOCI index for your own image](#train-soci-indexed-images-create)
+ [Verify that an image includes a SOCI index](#train-soci-indexed-images-verify)
+ [Use a SOCI-indexed image in a training job](#train-soci-indexed-images-use)
+ [Permissions](#train-soci-indexed-images-permissions)
+ [Prevent job failures: check your code for Docker-specific assumptions](#train-soci-indexed-images-docker-assumptions)
+ [Related resources](#train-soci-indexed-images-related)

## How it works
<a name="train-soci-indexed-images-how"></a>

When you create a training job, SageMaker AI checks whether the image you specified has a SOCI index and behaves accordingly:


| Scenario | What happens | 
| --- | --- | 
| The image includes a SOCI index | SageMaker AI lazy-loads the image and starts your container before the full download completes | 
| The image has no SOCI index | Normal download - no change in behavior | 
| The index can't be read, or lazy loading doesn't succeed | The training job falls back to a standard download and continues running | 

Adding an index never prevents a training job from running. In either case the image download is reported in the training job's `Downloading` secondary status.

## Considerations
<a name="train-soci-indexed-images-considerations"></a>
+ **Where the image is stored**
  + Store the image in an Amazon ECR **private** repository.
  + Reference the image by **tag** (`repository:tag`). An image referenced by digest (`repository@sha256:…`) is downloaded normally.
  + An image pulled through a private Docker registry in your VPC (`TrainingRepositoryAccessMode` set to `Vpc`) is downloaded normally.
+ **Which index format is detected**
  + The tag must point to an image that contains a SOCI index v2 (see [SOCI Index Manifest v2](https://github.com/awslabs/soci-snapshotter/blob/main/docs/soci-index-manifest-v2.md) on the GitHub website). `nerdctl image convert --soci` and the Deep Learning Container `-soci` tags create this format.
  + A v1 index isn't detected. A v1 index is stored as a separate artifact next to the image, for example by `nerdctl push --snapshotter=soci` or `soci create`.
+ **When the time saved is smaller**
  + Files are downloaded the first time your code opens them.
  + If your code reads a large part of the image before training starts (for example, model weights stored in the image), that time moves from the download to the start of training.
+ **Large datasets**
  + In `File` input mode, the training job also waits for the dataset download. With a very large dataset, that wait can take longer than the image download.
  + Use `FastFile` or `Pipe` input mode to keep the benefit.

## Use a Deep Learning Container that includes a SOCI index
<a name="train-soci-indexed-images-dlc"></a>

AWS publishes SOCI-indexed variants of several Deep Learning Containers (DLCs), identified by a `-soci` suffix on the tag. To adopt lazy loading, change only the tag:

```
763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:2.9-gpu-py312-cu130-ubuntu22.04-sagemaker-v1-soci
```
+ For the current list, see the [Deep Learning Containers gallery](https://gallery.ecr.aws/deep-learning-containers) on the Amazon ECR Public Gallery website and [SOCI index for AWS Deep Learning Containers](https://aws.github.io/deep-learning-containers/tutorials/SOCI/) on the GitHub website.
+ An image you build `FROM` a DLC doesn't inherit the index. Index your final image as described in the next section.

## Create a SOCI index for your own image
<a name="train-soci-indexed-images-create"></a>

You need:
+ A Linux host, such as an Amazon EC2 instance running Amazon Linux 2023.
+ These tools on the host:
  + [containerd](https://containerd.io/) on the containerd website
  + [SOCI snapshotter](https://github.com/awslabs/soci-snapshotter) 0.10.0 or later, on the GitHub website
  + [nerdctl](https://github.com/containerd/nerdctl) 2.1.3 or later, on the GitHub website. Finch, which is built on nerdctl, can be used instead; see [Lazy loading](https://runfinch.com/docs/container-images/lazy-loading/) on the Finch website.
+ `sudo` to run the commands. Rootless mode isn't supported.
+ The push permissions in [Permissions](#train-soci-indexed-images-permissions) for the identity on the host.

The procedure creates an indexed copy of an existing image under a new tag; the original image, tag, and digest are unchanged.

**To create a SOCI index**

1. Set variables for your account, Region, repository, the tag to index, and the tag for the indexed image:

   ```
   ACCOUNT_ID="{{111122223333}}"
   REGION="{{us-east-1}}"
   REPOSITORY_NAME="{{repository-name}}"
   ORIGINAL_IMAGE_TAG="{{original-image-tag}}"
   SOCI_IMAGE_TAG="{{soci-indexed-image-tag}}"
   REGISTRY="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"
   ```

1. Install the tools and start the snapshotter (Amazon Linux 2023; for other distributions see the [SOCI snapshotter installation guide](https://github.com/awslabs/soci-snapshotter/blob/main/docs/install.md) on the GitHub website):

   ```
   sudo dnf install -y containerd soci-snapshotter nerdctl jq
   sudo systemctl start soci-snapshotter
   sudo systemctl restart containerd
   ```

1. Confirm that `soci` is listed under **Server → Plugins → Storage**:

   ```
   sudo nerdctl system info
   ```

1. Authenticate to Amazon ECR and pull the original image:

   ```
   aws ecr get-login-password --region "$REGION" | sudo nerdctl login -u AWS --password-stdin "$REGISTRY"
   sudo nerdctl pull "$REGISTRY/$REPOSITORY_NAME:$ORIGINAL_IMAGE_TAG"
   ```

1. Create and push the SOCI-indexed image:

   ```
   sudo nerdctl image convert --soci \
     "$REGISTRY/$REPOSITORY_NAME:$ORIGINAL_IMAGE_TAG" \
     "$REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG"
   sudo nerdctl push --platform linux/amd64 "$REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG"
   ```

   Layers below the minimum layer size aren't indexed and are downloaded normally when the container starts (`--soci-min-layer-size`, see the [nerdctl SOCI documentation](https://github.com/containerd/nerdctl/blob/main/docs/soci.md) on the GitHub website).

After the push:
+ The repository has two new artifacts, both shown on the repository's **Images** page in the Amazon ECR console:
  + The SOCI index.
  + An OCI image index manifest that links your image and the index under the new tag.
+ Amazon ECR doesn't create SOCI indexes on its own. To index images automatically on every push, deploy the [CFN ECR SOCI Index Builder](https://github.com/aws-ia/cfn-ecr-aws-soci-index-builder) on the GitHub website with `SociIndexVersion` set to `V2`. For details, see the [Index Builder documentation](https://awslabs.github.io/cfn-ecr-aws-soci-index-builder/) on the GitHub website. It runs from an Amazon EventBridge rule on Amazon ECR push events.

To run the indexed image on the host the way a training job runs it, and check your entry point for the patterns in [Prevent job failures: check your code for Docker-specific assumptions](#train-soci-indexed-images-docker-assumptions):

```
sudo nerdctl run --snapshotter soci --rm -it "$REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG" /bin/bash
```

## Verify that an image includes a SOCI index
<a name="train-soci-indexed-images-verify"></a>

```
aws ecr batch-get-image \
  --repository-name "$REPOSITORY_NAME" \
  --image-ids imageTag="$SOCI_IMAGE_TAG" \
  --accepted-media-types "application/vnd.oci.image.index.v1+json" \
  --query 'images[0].imageManifest' --output text | jq '.manifests[] | {mediaType, artifactType}'
```
+ **Indexed:** the output lists a child manifest whose `artifactType` begins with `application/vnd.amazon.soci.index.`
+ **Not indexed:** no such entry. Jobs that use the tag download the image normally.

## Use a SOCI-indexed image in a training job
<a name="train-soci-indexed-images-use"></a>

Set the indexed image as `TrainingImage` in [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html):

```
"AlgorithmSpecification": {
  "TrainingImage": "111122223333.dkr.ecr.us-east-1.amazonaws.com/repository-name:soci-indexed-image-tag",
  "TrainingInputMode": "File"
}
```

With the SageMaker Python SDK:

```
from sagemaker.train.model_trainer import ModelTrainer
from sagemaker.core.training.configs import Compute

trainer = ModelTrainer(
    training_image="111122223333.dkr.ecr.us-east-1.amazonaws.com/repository-name:soci-indexed-image-tag",
    role="arn:aws:iam::111122223333:role/execution-role-name",
    compute=Compute(instance_type="ml.g5.12xlarge", instance_count=2),
)
trainer.train()
```

## Permissions
<a name="train-soci-indexed-images-permissions"></a>
+ **To run a training job:** the execution role needs the same Amazon ECR actions as for any other image, listed in [CreateTrainingJob API: Execution Role Permissions](sagemaker-roles.md#sagemaker-roles-createtrainingjob-perms). Lazy loading needs no additional permissions.
  + `ecr:GetAuthorizationToken`
  + `ecr:BatchCheckLayerAvailability`
  + `ecr:GetDownloadUrlForLayer`
  + `ecr:BatchGetImage`
+ **To create and push indexes:** the identity on the build host needs pull and push permissions on the repository, for example:

```
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow", "Action": "ecr:GetAuthorizationToken", "Resource": "*" },
    {
      "Effect": "Allow",
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer",
        "ecr:InitiateLayerUpload",
        "ecr:UploadLayerPart",
        "ecr:CompleteLayerUpload",
        "ecr:PutImage"
      ],
      "Resource": "arn:aws:ecr:us-east-1:111122223333:repository/repository-name"
    }
  ]
}
```

See [Private repository policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-push-iam.html) in the *Amazon Elastic Container Registry User Guide*.

## Prevent job failures: check your code for Docker-specific assumptions
<a name="train-soci-indexed-images-docker-assumptions"></a>

SOCI-indexed images run on a containerd-based runtime, not on Docker:
+ Container behavior is the same.
+ Code that detects a container by looking for Docker-specific files can take a different path.
+ Review your entry point, framework launchers, and setup scripts for the patterns in the following table.


| Pattern | Why it matters | Recommendation | 
| --- | --- | --- | 
| Checking for the /.dockerenv file | Created by the Docker daemon; not part of any container standard | Set your own environment variable, or detect containerization without depending on a runtime | 
| Matching docker in /proc/self/cgroup or /proc/1/cgroup | Cgroup paths differ between runtimes and cgroup versions | Don't branch on the runtime name | 
| Deriving a container ID from a cgroup path or the host name format | Runtime-specific formats | Pass identifiers in as environment variables | 
| Calling the docker CLI or /var/run/docker.sock inside the container | Not available | Remove the dependency; SageMaker AI manages the container lifecycle | 
+ SageMaker AI mounts a `/.dockerenv` marker in the container so that existing checks keep working. Don't add new dependencies on it.
+ If you use the SageMaker distributed data parallel library (SMDDP) or `mpirun` launchers, use a current Deep Learning Container. Some earlier launcher versions relied on `/.dockerenv`.

## Related resources
<a name="train-soci-indexed-images-related"></a>
+ [Speed up processing job startup with SOCI-indexed images](processing-job-soci-indexed-images.md) - the same feature for processing jobs
+ [Speed up container startup with SOCI](soci-indexing.md) - SOCI indexing for Studio
+ [SOCI index for AWS Deep Learning Containers](https://aws.github.io/deep-learning-containers/tutorials/SOCI/) on the GitHub website
+ [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) in the API reference
+ [Pushing an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-push.html) and [Private registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html) in the *Amazon Elastic Container Registry User Guide*
+ [SOCI snapshotter](https://github.com/awslabs/soci-snapshotter) and [nerdctl](https://github.com/containerd/nerdctl) on the GitHub website, and [Finch documentation](https://runfinch.com/docs/) on the Finch website
+ [Under the hood: Lazy loading container images with Seekable OCI and AWS Fargate](https://aws.amazon.com/blogs/containers/under-the-hood-lazy-loading-container-images-with-seekable-oci-and-aws-fargate/) on the AWS Containers Blog