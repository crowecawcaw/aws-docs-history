

# Container support for service-managed fleets
<a name="fleet-container-support"></a>

Container support lets a Linux service-managed fleet run job actions inside Docker images. The default Docker queue environment pulls images from Amazon ECR. You can customize the queue environment to authenticate to and pull from another container registry provider. For details, see [Customize a Docker queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/containers-queue-environment.html#containers-queue-customize) in the *Deadline Cloud Developer Guide*.

You select the image in the queue environment, and Deadline Cloud installs and configures rootless Docker on the fleet's workers. The service starts one container for each job session and stops it when the session ends.

## How container support works
<a name="fleet-container-how-it-works"></a>

Container support divides configuration between the fleet and queue:


| Resource | Configuration | Purpose | 
| --- | --- | --- | 
| Fleet | Docker software add-on on a Linux service-managed fleet | Installs rootless Docker and optional GPU integration on each worker | 
| Queue | Docker default queue environment and an Amazon ECR image URI | Pulls the image and runs environment and task actions in a session container | 
| Queue-fleet association | A container queue associated with a Docker-enabled fleet | Routes container jobs only to workers that provide Docker | 

Deadline Cloud runs Docker in rootless mode. Container actions run as the unprivileged `job-user` identity and don't provide root access to the worker.

The default queue environment mounts the job session directory at the same path inside the container. Embedded files, job attachments, and configured output paths therefore remain available to job actions.

When a fleet has GPU instances, Deadline Cloud configures Container Device Interface (CDI) support. The queue environment makes the GPU available to the container without requiring privileged container access.

## Prerequisites
<a name="fleet-container-prerequisites"></a>

Before you begin, you need the following resources:
+ An Deadline Cloud farm.
+ A Linux service-managed fleet, or permission to create one. Container support isn't available for Windows.
+ A queue role and fleet role that you can update.
+ A tagged image in an Amazon ECR private repository. For instructions, see [Building, tagging, and pushing a container image](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/containers-build-push.html) in the *Deadline Cloud Developer Guide*.

## Configure the fleet and queue
<a name="fleet-container-configure"></a>

**To configure container support**

1. Sign in to the AWS Management Console and open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home).

1. Open your farm, choose **Fleets**, and create or edit a service-managed fleet.

1. For the fleet operating system, choose **Linux**.

1. Under **Additional configurations**, find **Container support**. Select **Enable Docker (installs Docker Engine, configures ECR pull access)**.

1. Choose or create the fleet role. The console attaches the `AmazonEC2ContainerRegistryReadOnly` AWS managed policy so workers can pull images from Amazon ECR.

1. (Optional) Under **Storage capabilities**, choose **Persistent storage** to preserve Docker layers and application caches across worker lifecycle events. For details, see [Persistent storage for service-managed fleets](volumes.md).

1. Finish creating or updating the fleet.

1. Create or edit a queue. Under **Default queue environment**, for **Environment type**, choose **Docker**.

1. For **Container image URI**, select an Amazon ECR repository and image tag, or enter a complete image URI in the following format:

   ```
   {{account-id}}.dkr.ecr.{{region}}.amazonaws.com/{{repository}}:{{tag}}
   ```

1. Choose or create the queue role. The console attaches the `AmazonEC2ContainerRegistryReadOnly` managed policy so the queue environment can authenticate to Amazon ECR and pull the image.

1. Associate the queue with the Docker-enabled fleet.

## Verify container support
<a name="fleet-container-verify"></a>

After the fleet becomes active, verify the following settings:
+ The fleet's **Software add-ons** value includes **Docker**.
+ The queue uses the Docker default environment and displays the selected image URI.
+ The queue is associated only with Linux service-managed fleets that have Docker enabled.

Updating a fleet doesn't replace workers that are already running. To apply the Docker software add-on to every worker immediately, drain and restart the fleet as described in [Update a fleet configuration](smf-update-config.md).

## Next steps
<a name="fleet-container-next-steps"></a>

To automate the fleet and role setup, see [Creating a Docker-enabled fleet with the AWS CLI](fleet-container-support-cli.md).

For image workflows, portable job templates, queue environment internals, storage mounts, and security guidance, see [Run portable jobs in containers](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/containers.html) in the *Deadline Cloud Developer Guide*.