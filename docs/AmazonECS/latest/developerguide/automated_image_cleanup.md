# Automatic Amazon ECS task and image cleanup

Each time a task is placed on a container instance, the Amazon ECS container agent checks to
see if the images referenced in the task are the most recent of the specified tag in the
repository. If not, the default behavior allows the agent to pull the images from their
respective repositories. If you frequently update the images in your tasks and services,
your container instance storage can quickly fill up with Docker images that you are no
longer using and may never use again. For example, you may use a continuous integration and
continuous deployment (CI/CD) pipeline.

###### Note

The Amazon ECS agent image pull behavior can be customized using the
`ECS_IMAGE_PULL_BEHAVIOR` parameter. For more information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

Likewise, containers that belong to stopped tasks can also consume container instance
storage with log information, data volumes, and other artifacts. These artifacts are useful
for debugging containers that have stopped unexpectedly, but most of this storage can be
safely freed up after a period of time.

By default, the Amazon ECS container agent automatically cleans up stopped tasks and Docker
images that are not being used by any tasks on your container instances.

###### Note

The automated image cleanup feature requires at least version 1.13.0 of the Amazon ECS
container agent. To update your agent to the latest version, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

The following agent configuration variables are available to tune your automated task
and image cleanup experience. For more information about how to set these variables on
your container instances, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

`ECS_ENGINE_TASK_CLEANUP_WAIT_DURATION`

The default time to wait to delete containers for a stopped task. If the value is set to less than 1 second, the value is ignored. By default, this parameter is set to 3
hours, but you can reduce this period to as low as 1 second if you need to
for your application.

###### Note

The image cleanup process cannot delete an
image as long as there is a container that references it. After containers are removed, any unreferenced images become candidates for cleanup based on the image cleanup configuration parameters.

`ECS_DISABLE_IMAGE_CLEANUP`

If you set this variable to `true`, then automated image
cleanup is turned off on your container instance and no images are
automatically removed.

`ECS_IMAGE_CLEANUP_INTERVAL`

This variable specifies how frequently the automated image cleanup process
should check for images to delete. The default is every 30 minutes but you
can reduce this period to as low as 10 minutes to remove images more
frequently.

`ECS_IMAGE_MINIMUM_CLEANUP_AGE`

This variable specifies the minimum amount of time between when an image
was pulled and when it may become a candidate for removal. This is used to
prevent cleaning up images that have just been pulled. The default is 1
hour.

`ECS_NUM_IMAGES_DELETE_PER_CYCLE`

This variable specifies how many images may be removed during a single
cleanup cycle. The default is 5 and the minimum is 1.

When the Amazon ECS container agent is running and automated image cleanup is not turned
off, the agent checks for Docker images that are not referenced by running or stopped
containers at a frequency determined by the `ECS_IMAGE_CLEANUP_INTERVAL`
variable. If unused images are found and they are older than the minimum cleanup time
specified by the `ECS_IMAGE_MINIMUM_CLEANUP_AGE` variable, the agent removes
up to the maximum number of images that are specified with the
`ECS_NUM_IMAGES_DELETE_PER_CYCLE` variable. The least-recently referenced
images are deleted first. After the images are removed, the agent waits until the next
interval and repeats the process again.
