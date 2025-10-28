# Container image pull behavior for EC2 and external instances on Amazon ECS

The time that it takes a container to start up varies, based on the underlying
container image. For example, a fatter image (full versions of Debian, Ubuntu, and
Amazon1/2) might take longer to start up because there are a more services that run in
the containers compared to their respective slim versions (Debian-slim, Ubuntu-slim, and
Amazon-slim) or smaller base images (Alpine).

When the Amazon ECS agent starts a task, it pulls the Docker image from its remote
registry, and then caches a local copy. When you use a new image tag for each
release of your application, this behavior is unnecessary.

The `ECS_IMAGE_PULL_BEHAVIOR` agent parameter determines the image pull
behavior. The following options are available:

- `ECS_IMAGE_PULL_BEHAVIOR`: `default`

The image will be pulled remotely. If the pull fails, the cached
image in the instance is used.

- `ECS_IMAGE_PULL_BEHAVIOR`: `always`

The image will be pulled remotely. If the pull fails, the task fails.
To speed up deployment, set the Amazon ECS agent parameter to one of the following
values:

- `ECS_IMAGE_PULL_BEHAVIOR`: `once`

The image is pulled remotely only if it wasn't pulled by a previous task
on the same container instance or if the cached image was removed by the
automated image cleanup process. Otherwise, the cached image on the instance
is used. This ensures that no unnecessary image pulls are attempted.

- `ECS_IMAGE_PULL_BEHAVIOR`: `prefer-cached`

The image is pulled remotely if there is no cached image. Otherwise, the
cached image on the instance is used. Automated image cleanup is turned off
for the container to ensure that the cached image isn't removed.
Setting the `ECS_IMAGE_PULL_BEHAVIOR` parameter to either of the
preceding values can save time because the Amazon ECS agent uses the existing downloaded
image. For larger Docker images, the download time might take 10-20 seconds to pull
over the network.
