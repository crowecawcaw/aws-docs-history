

# Building, tagging, and pushing a container image
<a name="containers-build-push"></a>

Build the image for the processor architecture used by your fleet. Linux service-managed fleets with the Docker software add-on use the `linux/amd64` platform. Give each image version a tag that identifies its contents, such as an application version or source revision.

## Prerequisites
<a name="containers-build-prerequisites"></a>

Install Docker and AWS CLI on your workstation. Create an Amazon ECR private repository and configure your AWS credentials with permission to push images to that repository.

## Build and push the image
<a name="containers-build-procedure"></a>

**To build and push a container image**

1. Set values for your AWS account, Region, repository, and image tag.

   ```
   REGION={{us-west-2}}
   ACCOUNT_ID={{123456789012}}
   REPOSITORY={{portable-job}}
   IMAGE_TAG={{1.0.0}}
   REGISTRY="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
   IMAGE_URI="${REGISTRY}/${REPOSITORY}:${IMAGE_TAG}"
   ```

1. From the directory that contains your Dockerfile, build the image.

   ```
   docker build --platform linux/amd64 \
       --tag "${REPOSITORY}:${IMAGE_TAG}" \
       .
   ```

1. Run an application-specific command to test the image locally.

   ```
   docker run --rm "${REPOSITORY}:${IMAGE_TAG}" {{test-command}}
   ```

1. Authenticate Docker to your private Amazon ECR registry.

   ```
   aws ecr get-login-password --region "${REGION}" | \
       docker login --username AWS --password-stdin "${REGISTRY}"
   ```

1. Apply the Amazon ECR image tag and push the image.

   ```
   docker tag "${REPOSITORY}:${IMAGE_TAG}" "${IMAGE_URI}"
   docker push "${IMAGE_URI}"
   ```

1. Retrieve the image digest and record it with your build output.

   ```
   aws ecr describe-images \
       --region "${REGION}" \
       --repository-name "${REPOSITORY}" \
       --image-ids imageTag="${IMAGE_TAG}" \
       --query 'imageDetails[0].imageDigest' \
       --output text
   ```

Use a fixed version tag or image digest for repeatable jobs. A mutable tag such as `latest` can resolve to different image contents across sessions.