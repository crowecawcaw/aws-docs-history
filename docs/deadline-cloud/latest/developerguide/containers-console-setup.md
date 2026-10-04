

# Set up container support in the console
<a name="containers-console-setup"></a>

This topic shows the key console controls for setting up container support. For the complete step-by-step procedure, prerequisites, and verification steps, see [Container support for service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/fleet-container-support.html) in the *Deadline Cloud User Guide*.

## Configure the queue environment
<a name="containers-console-queue-environment"></a>

When you create or edit a queue, choose **Docker** as the environment type under **Default queue environment**. Select an Amazon ECR repository and image tag from your account, or enter a complete image URI manually. The console composes the full image URI and attaches the `AmazonEC2ContainerRegistryReadOnly` managed policy to the queue role so workers can pull the image.

![Console showing the Default queue environment section with Docker selected as the environment type, an ECR repository and image tag chosen, and the composed container image URI.](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/container-queue-environment.png)


## Associate the queue with a fleet
<a name="containers-console-fleet-association"></a>

When you create or edit a fleet, associate it with a Docker-enabled queue. The console confirms that container support is enabled for the fleet and shows the Docker Engine configuration. After this step, the fleet and queue are ready to run container workloads together.

![Console showing the Associate queues with fleet step with a Docker-enabled queue selected and a banner confirming that container support is enabled for the fleet.](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/container-fleet-associate-queue.png)
