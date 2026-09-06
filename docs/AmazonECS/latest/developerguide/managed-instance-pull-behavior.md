

# Amazon ECS Managed Instances container image pull behavior
<a name="managed-instance-pull-behavior"></a>

Container startup time depends on the size of the underlying container image. Larger images, such as full versions of Debian, Ubuntu, or Amazon Linux 2, take longer to start because they include more services than their slim counterparts (Debian-slim, Ubuntu-slim, Amazon-slim) or minimal base images such as Alpine.

When Amazon ECS launches a new Amazon ECS Managed Instances container instance, the local image cache is empty. The first task that runs on that container instance pulls the container image from the container repository to the local image cache. Subsequent tasks that use the same image on that container instance use the cached image instead of pulling it again.

The Amazon ECS agent on Amazon ECS Managed Instances automatically manages disk space on each container instance. When a task stops and no other running task uses the same container image, Amazon ECS starts a 15-minute cleanup timer for that image. If no new task that uses the image starts on that container instance within 15 minutes, the image is removed from the local image cache.

## Container image resolution
<a name="managed-instance-image-resolution"></a>

Amazon ECS resolves container image tags to image digests to ensure that all tasks in a service run the same image version. This behavior affects Amazon ECS Managed Instances bin packing and instance selection because Amazon ECS schedules a single task from the service first to retrieve the container image digest before scheduling the remaining tasks. For more information, see [Container image resolution](deployment-type-ecs.md#deployment-container-image-stability).