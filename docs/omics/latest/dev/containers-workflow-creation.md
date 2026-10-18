

# Adding private or third-party containers during workflow creation
<a name="containers-workflow-creation"></a>

When you create a new workflow, you can define the registry and image mappings required by your workflow. For more information, see [Create a private workflow](create-private-workflow.md). You can also update registry and image mappings when you create a new workflow version. For more information, see [Create a workflow version](workflows-version-create.md).

The following sections describe registry mappings and image mappings.

## Registry mappings
<a name="ecr-pull-through-registry-mapping"></a>

You define registry mappings to map between prefixes in your private Amazon ECR registry and the upstream registry names. One registry map can contain both pull through cache mappings and mappings for registries that HealthOmics copies from.

The following example maps Docker Hub, Quay, and Amazon ECR Public through pull through cache, and maps Seqera Containers (`community.wave.seqera.io`) with a credential so that HealthOmics copies its images.

```
{
    "registryMappings": [
        {
            "upstreamRegistryUrl": "registry-1.docker.io",
            "ecrRepositoryPrefix": "docker-hub"
        },
        {
            "upstreamRegistryUrl": "quay.io",
            "ecrRepositoryPrefix": "quay"
        },
        {
            "upstreamRegistryUrl": "public.ecr.aws",
            "ecrRepositoryPrefix": "ecr-public"
        },
        {
            "upstreamRegistryUrl": "community.wave.seqera.io",
            "ecrRepositoryPrefix": "wave-seqera",
            "credentialArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:omics-registry/seqera-EXAMPLE"
        }
    ]
}
```

The following rules apply to registry mappings:
+ `upstreamRegistryUrl` must exactly match the registry host at the start of the image URI. For example, a mapping for `wave.seqera.io` doesn't cover images on `community.wave.seqera.io`.
+ Every upstream registry host that the workflow references needs a mapping. Images that you reference by their private Amazon ECR URI don't need one.
+ Pull through cache mappings don't use `credentialArn`. If you add `credentialArn` to a pull through cache mapping, HealthOmics ignores it.
+ Mappings for registries that HealthOmics copies from must include `credentialArn`. If one of these mappings has no `credentialArn`, the workflow fails with an error that names the registry.
+ Keep `upstreamRepositoryPrefix` unset for Wave (`wave.seqera.io`).

`CreateWorkflow` and `CreateWorkflowVersion` are asynchronous. If the status is `FAILED`, the error appears in `statusMessage` in the `GetWorkflow` response for a workflow, or the `GetWorkflowVersion` response for a workflow version.

Provide the map inline with `containerRegistryMap`, or as an Amazon S3 URI with `containerRegistryMapUri`, not both. For CLI examples, see [Configure pull through cache mapping parameters](create-private-workflow.md#create-prefix-mapping-parameters) and [Configure non-pull through cache mapping parameters](create-private-workflow.md#create-non-ptc-mapping-parameters).

The run uses the registry map of the workflow or workflow version that you run, so you don't add anything to `StartRun`.

## Image mappings
<a name="ecr-pull-through-mapping-format"></a>

You define image mappings to map between the image names as defined in your private Amazon ECR workflows and the image names in the upstream registry.

You can use image mappings with registries that Amazon ECR pull through cache supports, such as Quay, and with registries that pull through cache doesn't support, such as Seqera. HealthOmics doesn't copy images for image mappings, so you keep your private repository in sync with the upstream registry yourself.

**Note**  
An image mapping takes precedence over registry mappings.

The following example shows mappings from private Amazon ECR images to a public genomics image and the latest Ubuntu image.

```
{
    "imageMappings": [
        {
            "sourceImage": "public.ecr.aws/aws-genomics/broadinstitute/gatk:4.6.0.2",
            "destinationImage": "111122223333.dkr.ecr.us-east-1.amazonaws.com/broadinstitute/gatk:4.6.0.2"
        },
        {
            "sourceImage": "ubuntu:latest",
            "destinationImage": "111122223333.dkr.ecr.us-east-1.amazonaws.com/custom/ubuntu:latest"
        }
    ]
}
```

For more information about using registry and image mappings when you create a workflow, see [Configure pull through cache mapping parameters](create-private-workflow.md#create-prefix-mapping-parameters).