# Build a Blender Docker image for GPU rendering on Deadline Cloud

The
[blender-aswf-ci-base](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/containers/blender/blender-aswf-ci-base "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/containers/blender/blender-aswf-ci-base")
example on the GitHub website builds a Docker image that packages Blender with the
[deadline-cloud-for-blender](https://github.com/aws-deadline/deadline-cloud-for-blender "https://github.com/aws-deadline/deadline-cloud-for-blender")
adaptor and GPU support (CUDA/OptiX) for rendering on Deadline Cloud
service-managed fleets. The base image is
`aswf/ci-base:2026` (Rocky Linux 8, CUDA 12.9, VFX Platform
2026).

You can use this image for the following purposes:

- Run Blender Cycles GPU renders on Deadline Cloud service-managed
  fleets.
- Bundle third-party Blender addons into the image at build
  time by placing addon `.zip` files in the
  `plugins/` directory before building.
  Build the image:

```
docker build -t blender-aswf:4.5.0 .
```

Push to Amazon Elastic Container Registry (Amazon ECR) and deploy the full stack (queue, fleet, and queue
environment) with the included AWS CloudFormation (CloudFormation) template:

```
aws cloudformation deploy \
    --template-file cloudformation.yaml \
    --stack-name blender-aswf-ci-base-stack \
    --parameter-overrides \
        FarmId=farm-... \
        ECRImageURI=`account-id`.dkr.ecr.`region`.amazonaws.com/`repo`:4.5.0 \
        FleetRoleArn=arn:aws:iam::`account-id`:role/FleetRole \
        QueueRoleArn=arn:aws:iam::`account-id`:role/QueueRole \
        JobAttachmentsBucket=`my-deadline-bucket`
```

The queue role needs Amazon ECR pull permissions
(`ecr:BatchGetImage`, `ecr:GetDownloadUrlForLayer`,
and `ecr:GetAuthorizationToken`) to pull the container image at
runtime.

GPU rendering is automatic when the fleet has GPU instances. The queue
environment conditionally adds `--gpus all --runtime=nvidia`
based on whether the host has an NVIDIA GPU. CPU-only instances fall back
to Cycles CPU rendering.

For a job bundle that renders Blender scenes, see
[Render Blender scenes on Deadline Cloud](examples-jb-blender-render.md "examples-jb-blender-render.md").
