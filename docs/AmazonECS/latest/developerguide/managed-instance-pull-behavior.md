# Amazon ECS Managed Instances container image pull behavior

The time that it takes a container to start up varies, based on the underlying container
image. For example, a fatter image (full versions of Debian, Ubuntu, and Amazon2) might take
longer to start up because there are a more services that run in the containers compared to
their respective slim versions (Debian-slim, Ubuntu-slim, and Amazon-slim) or smaller base
images (Alpine).

When Amazon ECS starts a task that runs on Amazon ECS Managed Instances, Amazon ECS pulls the image remotely
only if it wasn't pulled by a previous task on the same container instance or if the cached
image was removed by the automated image cleanup process. Otherwise, the cached image on the
Amazon ECS Managed Instance is used. This ensures that no unnecessary image pulls are attempted.
