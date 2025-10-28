# Work with multi-architecture

images

Amazon EMR on EKS supports multi-architecture container images for Amazon Elastic Container Registry (Amazon ECR). For more
information, see [Introducing multi-architecture container images for Amazon ECR](https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr/ "https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr/").

Amazon EMR on EKS custom images support both AWS Graviton-based EC2 instances and
non-Graviton-based EC2 instances. The Graviton-based images are stored in the same image
repositories in Amazon ECR as non-Graviton-based images.

For example, to inspect the Docker manifest list for 6.6.0 images, run the following
command.

```
docker manifest inspect 895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-6.6.0:latest
```

Here is the output. The `arm64` architecture is for Graviton instance. The
`amd64` is for non-Graviton instance.

```
{
   "schemaVersion": 2,
   "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
   "manifests": [
      {
         "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
         "size": 1805,
         "digest": "xxx123:6b971cb47d11011ab3d45fff925e9442914b4977ae0f9fbcdcf5cfa99a7593f0",
         "platform": {
            "architecture": "arm64",
            "os": "linux"
         }
      },
      {
         "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
         "size": 1805,
         "digest": "xxx123:6f2375582c9c57fa9838c1d3a626f1b4fc281e287d2963a72dfe0bd81117e52f",
         "platform": {
            "architecture": "amd64",
            "os": "linux"
         }
      }
   ]
}
```

Take the following steps to create multi-architecture images:

1. Create a `Dockerfile` with the following contents so that you can pull
   the `arm64` image.

```
FROM --platform=arm64 895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-6.6.0:latest
USER root

RUN pip3 install boto3 // install customizations here
USER hadoop:hadoop

```

2. Follow the instructions at [Introducing multi-architecture container images for Amazon ECR](https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr/ "https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr/") to build a
   multi-architecture image.

###### Note

You must create `arm64` images on `arm64` instances.
Similarly, you must build `amd64` images on `amd64`
instances.

You can also build multi-architecture images without building on each specific
instance type with the Docker `buildx` command. For more information, see
[Leverage multi-CPU
architecture support](https://docs.docker.com/desktop/multi-arch/ "https://docs.docker.com/desktop/multi-arch/"). 3. After you build the multi-architecture image, you can submit a job with the same
`spark.kubernetes.container.image` parameter and point it to the image. In
a heterogeneous cluster with both AWS Graviton-based and non-Graviton-based EC2
instances, the instance determines the correct architecture image based on the instance
architecture that pulls the image.
