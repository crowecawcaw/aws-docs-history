# Linux containers on Fargate container image pull behavior for Amazon ECS

Every Fargate task runs on its own single use, single tenant instance. When you run
Linux containers on Fargate, container images or container image layers are not cached on
the instance. Therefore, for each container image defined in the task, the whole container
image needs to be pulled from the container image registry for each Fargate task. The time
it takes to pull the images is directly correlated to the time taken to start an Fargate
task.

Take the following into account to optimize the image pull time.

**Container image proximity**

To reduce the time it takes to download container images, locate the data as
close to the compute as possible. Pulling a container image over the internet or
across AWS Regions might impact the download time. We recommend that you store
the container image in the same Region where the task will run.
If you store the container image in Amazon ECR, use a VPC interface endpoint to
further reduce the image pull time. For more information, see [Amazon ECR interface VPC endpoints (AWS PrivateLink)](../../../AmazonECR/latest/userguide/vpc-endpoints.md "../../../AmazonECR/latest/userguide/vpc-endpoints.md") in the _Amazon ECR User Guide_.

**Container image size reduction**

The size of a container image directly impacts the download time. Reducing
the size of the container image or the number of container image layers, can
reduce the time it takes for an image to download. Lightweight base images (such
as the minimal Amazon Linux 2023 container image) can be significantly smaller than those
based on traditional operating system base images. For more information about
the minimal image, see [AL2023 Minimal container
image](../../../linux/al2023/ug/minimal-container.md "../../../linux/al2023/ug/minimal-container.md") in the _Amazon Linux 2023 User
Guide_.

**Alternative compression algorithms**

Container image layers are often compressed when pushed to a container
image registry. Compressing the container image layer reduces the amount of data
that has to be transferred across the network and stored in the container image
registry. After a container image layer has been downloaded to an instance by
the container runtime, that layer is decompressed. The compression algorithm
used and the amount of vCPUs available to the runtime impact the time it takes
to decompress the container image. On Fargate, you can increase the size of
the task or leverage the more performant zstd compression algorithm to reduce
the time taken for decompression. For more information, see [zstd](https://github.com/facebook/zstd "https://github.com/facebook/zstd") on GitHub. For
information about how to implement the images for Fargate, see [Reducing AWS Fargate Startup Times with zstd Compressed Container
Images](https://aws.amazon.com/blogs/containers/reducing-aws-fargate-startup-times-with-zstd-compressed-container-images/ "https://aws.amazon.com/blogs/containers/reducing-aws-fargate-startup-times-with-zstd-compressed-container-images/").

**Lazy Loading container images**

For large container images (> 250mb), it might be optimal to lazy load a
container image rather than downloading all of the container image. On
Fargate, you can use Seekable OCI (SOCI) to lazy load a container image from a
container image registry. For more information, see [soci-snapshotter](https://github.com/awslabs/soci-snapshotter "https://github.com/awslabs/soci-snapshotter") on GitHub and [Lazy loading container images using Seekable OCI (SOCI)](fargate-tasks-services.md#fargate-tasks-soci-images "fargate-tasks-services.md#fargate-tasks-soci-images").
