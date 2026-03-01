# Envoy image

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

AWS App Mesh is a service mesh based on the [Envoy](https://www.envoyproxy.io/ "https://www.envoyproxy.io/") proxy.

![ECS Task/Kubernetes Pod with Proxy and Microservice Container communicating via ports 8080 and 8081.](images/proxy.png)
You must add an Envoy proxy to the Amazon ECS task, Kubernetes pod, or Amazon EC2 instance represented
by your App Mesh endpoint, such as a virtual node or virtual gateway. App Mesh vends an Envoy proxy
container image that is patched with the latest vulnerability and performance updates. App Mesh
tests each new Envoy proxy release against the App Mesh feature set before making a new image
available to you.

## Envoy image variants

App Mesh provides two variants of the Envoy proxy container image. The differences between
the two is how the Envoy proxy communicates to the App Mesh data plane and how the Envoy proxies
communicate with each other. One is a standard image, which communicates with the standard
App Mesh service endpoints. The other variant is FIPS-compliant, which communicates with the
App Mesh FIPS service endpoints and enforces FIPS cryptography in TLS communication between
App Mesh services.

You can choose either a Regional image from the list below or an image from our [public repository](https://gallery.ecr.aws/appmesh/aws-appmesh-envoy "https://gallery.ecr.aws/appmesh/aws-appmesh-envoy") named
`aws-appmesh-envoy`.

###### Important

- Starting from June 30, 2023, only Envoy image `v1.17.2.0-prod` or later
  is compatible for use with App Mesh. For current customers using an Envoy image before
  `v1.17.2.0`, although existing envoys will continue to be compatible, we
  strongly recommend migrating to the latest version.
- As a best practice, upgrading the Envoy version to the latest version on a regular
  basis is highly recommended. Only the latest Envoy version is validated with the most
  recent security patches, feature releases, and performance improvements.
- Version `1.17` was a significant update to Envoy. See [Updating/migrating to Envoy 1.17](1.md "1.md") for more details.
- Version `1.20.0.1` or later is `ARM64` compatible.
- For `IPv6` support, Envoy version `1.20` or later is
  required.

###### Note

FIPS is only available in Regions found in the US and Canada.

All [supported](../../../general/latest/gr/appmesh.md "../../../general/latest/gr/appmesh.md")
Regions can replace `Region-code` with any Region other than
`me-south-1`, `ap-east-1`, `ap-southeast-3`, `eu-south-1`, `il-central-1`, and `af-south-1`.

Standard

```
840364872350.dkr.ecr.`region-code`.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod
```

FIPS-compliant

```
840364872350.dkr.ecr.`region-code`.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod-fips
```

`me-south-1`

Standard

```
772975370895.dkr.ecr.me-south-1.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod
```

`ap-east-1`

Standard

```
856666278305.dkr.ecr.ap-east-1.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod
```

`ap-southeast-3`

Standard

```
909464085924.dkr.ecr.ap-southeast-3.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod
```

`eu-south-1`

Standard

```
422531588944.dkr.ecr.eu-south-1.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod
```

`il-central-1`

Standard

```
564877687649.dkr.ecr.il-central-1.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod
```

`af-south-1`

Standard

```
924023996002.dkr.ecr.af-south-1.amazonaws.com/aws-appmesh-envoy:v1.34.12.1-prod
```

`Public repository`

Standard

```
public.ecr.aws/appmesh/aws-appmesh-envoy:v1.34.12.1-prod
```

FIPS-compliant

```
public.ecr.aws/appmesh/aws-appmesh-envoy:v1.34.12.1-prod-fips
```

###### Note

We recommend allocating 512 CPU units and at least 64 MiB of memory to the Envoy
container. On Fargate the lowest amount of memory that you can set is 1024 MiB of memory.
Resource allocation to the Envoy container can be increased if container insights or other
metrics indicate insufficient resources due to higher load.

###### Note

All `aws-appmesh-envoy` image release versions starting from
`v1.22.0.0` are built as a distroless Docker image. We made this change so that
we could reduce the image size and reduce our vulnerability exposure in unused packages
present in the image. If you are building on top of aws-appmesh-envoy image and are relying
on some of the AL2 base packages (e.g. yum) and functionalities, then we suggest you copy
the binaries from inside an `aws-appmesh-envoy` image to build a new Docker image
with AL2 base.

Run this script to generate a custom docker image with the tag
`aws-appmesh-envoy:v1.22.0.0-prod-al2:`

```
cat << EOF > Dockerfile
FROM public.ecr.aws/appmesh/aws-appmesh-envoy:v1.22.0.0-prod as envoy

FROM public.ecr.aws/amazonlinux/amazonlinux:2
RUN yum -y update && \
    yum clean all && \
    rm -rf /var/cache/yum

COPY --from=envoy /usr/bin/envoy /usr/bin/envoy
COPY --from=envoy /usr/bin/agent /usr/bin/agent
COPY --from=envoy /aws_appmesh_aggregate_stats.wasm /aws_appmesh_aggregate_stats.wasm

CMD [ "/usr/bin/agent" ]
EOF

docker build -f Dockerfile -t aws-appmesh-envoy:v1.22.0.0-prod-al2 .
```

Access to this container image in Amazon ECR is controlled by AWS Identity and Access Management (IAM). As a result,
you must use IAM to verify that you have read access to Amazon ECR. For example, when using
Amazon ECS, you can assign an appropriate task execution role to an Amazon ECS task. If you use IAM
policies that limit access to specific Amazon ECR resources, make sure to verify that you allow
access to the Region specific Amazon Resource Name (ARN) that identifies the `aws-appmesh-envoy`
repository. For example, in the `us-west-2` Region, you allow access to the
following resource:
`arn:aws:ecr:us-west-2:840364872350:repository/aws-appmesh-envoy`. For more
information, see [Amazon ECR Managed Policies](../../../AmazonECR/latest/userguide/ecr_managed_policies.md "../../../AmazonECR/latest/userguide/ecr_managed_policies.md").
If you're using Docker on an Amazon EC2 instance, then authenticate Docker to the repository. For
more information, see [Registry
authentication](../../../AmazonECR/latest/userguide/Registries.md#registry_auth "../../../AmazonECR/latest/userguide/Registries.md#registry_auth").

We occasionally release new App Mesh features that depend on Envoy changes that have not
been merged to the upstream Envoy images yet. To use these new App Mesh features before the
Envoy changes are merged upstream, you must use the App Mesh-vended Envoy container image. For a
list of changes, see the [App Mesh GitHub
roadmap issues](https://github.com/aws/aws-app-mesh-roadmap/labels/Envoy%20Upstream "https://github.com/aws/aws-app-mesh-roadmap/labels/Envoy%20Upstream") with the `Envoy Upstream` label. We recommend that you use
the App Mesh Envoy container image as the best supported option.
