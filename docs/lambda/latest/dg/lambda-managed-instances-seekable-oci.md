

# Lazy-load container images with Seekable OCI (SOCI)
<a name="lambda-managed-instances-seekable-oci"></a>

For Lambda Event Functions deployed as container images on Lambda Managed Instances, Lambda downloads and unpacks the image on each instance before it starts an execution environment. For large images, this pull is the largest part of the time between publishing a function version or scaling out and the execution environment handling its first invocation. With Seekable OCI (SOCI), Lambda can start the execution environment before the whole image has been downloaded.

SOCI is an [open source technology](https://github.com/awslabs/soci-snapshotter) developed by AWS. It uses an index that maps each file in the image to its location in the image's layers. Lambda uses the index to fetch only the files on demand as your function reads them, instead of downloading and unpacking the full image before starting the container. Container images typically bundle broad sets of libraries and dependencies, not all of which are read during startup or any single invocation. Lazy loading takes advantage of this by fetching only what your function actually reads, reducing time to first invocation and making startup time much less sensitive to total image size. The benefit is largest for images of several gigabytes where your function reads only a subset of the content per invocation, such as images that package machine learning frameworks.

## How SOCI works on Lambda Managed Instances
<a name="lambda-managed-instances-seekable-oci-how-it-works"></a>

1. You create a SOCI index for your image and push it to Amazon ECR alongside the image. The result is an Open Container Initiative (OCI) image index that references two artifacts: your original image manifest and the SOCI index.

1. You create or update your function with an image URI that points to the image index. Lambda detects the SOCI index and enables lazy loading for that function's execution environments. You don't need to change any other function configuration.

1. Lambda fetches image content on demand. Files your initialization code reads are fetched during initialization. Files your handler reads for the first time are fetched during that invocation. Lambda does not download the remainder of the image in the background.

**Note**  
If your function reads a file for the first time during an invocation rather than during initialization, Lambda fetches that file at the first invocation, which increases that invocation's duration. To keep invocation durations consistent, import all libraries and read all files your function needs in your initialization code, not in the handler. We recommend testing your function with and without SOCI to compare startup time and invocation duration for your workload.

## Create a SOCI index for your image
<a name="lambda-managed-instances-seekable-oci-create-index"></a>

The following example runs on Amazon Linux 2023. It installs the SOCI snapshotter, containerd, and nerdctl, then creates a SOCI index for an existing image in Amazon ECR and pushes the result. Replace the placeholder values with your own. For other ways to create and push a SOCI index, see [Getting started with the SOCI snapshotter](https://github.com/awslabs/soci-snapshotter/blob/main/docs/getting-started.md) on GitHub.

```
sudo yum install -y soci-snapshotter containerd nerdctl
sudo systemctl start soci-snapshotter
sudo systemctl restart containerd

ACCOUNT_ID="111122223333"
REGION="us-east-2"
REPOSITORY_NAME="my-function"
ORIGINAL_IMAGE_TAG="v1"
SOCI_IMAGE_TAG="v1-soci"
REGISTRY="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"

aws ecr get-login-password --region $REGION | sudo nerdctl login -u AWS --password-stdin $REGISTRY

sudo nerdctl pull $REGISTRY/$REPOSITORY_NAME:$ORIGINAL_IMAGE_TAG
sudo nerdctl image convert --soci $REGISTRY/$REPOSITORY_NAME:$ORIGINAL_IMAGE_TAG $REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG
sudo nerdctl push --platform linux/arm64 $REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG
```

**Note**  
This example builds an `arm64` (AWS Graviton) image. Lambda supports only single-architecture container images, so your image must target a single instruction set architecture, and the `--platform` value must match your function's architecture. For more information, see [Selecting and configuring an instruction set architecture for your Lambda function](foundation-arch.md).

Use `$REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG` as the image URI when you create or update your function. Then publish a function version. Lambda resolves the function version to the image index and enables lazy loading.

## Requirements and limitations
<a name="lambda-managed-instances-seekable-oci-requirements"></a>

SOCI index version  
Lambda supports SOCI Index Manifest v2 only (media type `application/vnd.amazon.soci.index.v2+json`). Lambda doesn't support SOCI Index Manifest v1 indexes. The `nerdctl image convert --soci` command in the previous section produces a v2 index.

Image index format  
The image index must contain exactly two entries: the SOCI index and one OCI image manifest.

Image URI  
Point your function's image URI at the SOCI-indexed tag (for example, `my-function:v1-soci`), not at the original image tag. Lambda resolves the function version to the image index. To change the image or the index, push a new SOCI-indexed tag and update the function's image URI to it.

Availability  
SOCI is available only for container image functions running on Lambda Managed Instances.