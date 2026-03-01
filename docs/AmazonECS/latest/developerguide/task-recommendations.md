# Optimize Amazon ECS task launch time

In order to speed up your task launches, consider the following
recommendations.

- ###### Cache container images and binpack instances

If you use EC2, you can configure
the Amazon ECS container agent pull behavior to `ECS_IMAGE_PULL_BEHAVIOR`:
`prefer-cached`. The image is pulled remotely if there is no
cached image. Otherwise, the cached image on the instance is used. Automated
image cleanup is turned off for the container to ensure that the cached image
isn't removed. This reduces image pull-time for subsequent launches. The effect
of caching is even greater when you have a high task density in your container
instances, which you can configure using the `binpack` placement
strategy. Caching container images is especially beneficial for windows-based
workloads which usually have large (tens of GBs) container image sizes. When
using the `binpack` placement strategy, you can also consider using
Elastic Network Interface (ENI) trunking to place more tasks with the
`awsvpc` network mode on each container instance. ENI trunking
increases the number of tasks you can run on `awsvpc` mode. For
example, a c5.large instance that may support running only 2 tasks concurrently,
can run up to 10 tasks with ENI trunking.

- ###### Choose an optimal network mode

Although there are many instances where
`awsvpc` network mode is ideal, this network mode can inherently
increase task launch latency, because for each task in `awsvpc` mode,
Amazon ECS workflows need to provision and attach an ENI by invoking Amazon EC2 APIs which
adds an overhead of several seconds to your task launches. By contrast, a key
advantage of using `awsvpc` network mode is that each task has a
security group to allow or deny traffic. This means you have greater flexibility
to control communications between tasks and services at a more granular level.
If the deployment speed is your priority, you can consider using
`bridge` mode to speed up task launches. For more information,
see [Allocate a network interface for an Amazon ECS task](task-networking-awsvpc.md "task-networking-awsvpc.md").

- ###### Track your task launch lifecycle to find optimization opportunities

It is often difficult to know the amount of
time it takes for your application to start-up. Launching your container image,
running start-up scripts, and other configurations during application start-up
can take a surprising amount of time. You can use the Task metadata endpoint to
post metrics to track application start-up time from `StartedAt` in
the container metadata response to the `StartedAt` time for your task
or service. With this data, you can understand how your application is
contributing to the total launch time, and find areas where you can reduce
unnecessary application-specific overhead and optimize your container images.
For more information, see [Amazon ECS Auto scaling and capacity management best practices](capacity-availability.md "capacity-availability.md").

- ###### Choose an optimal instance type (for EC2)

Choosing the correct instance type is based on
the resource reservation (for example, CPU, memory) that you configure on your
task. Therefore, when sizing the instance, you can calculate how many tasks can
be placed on a single instance. A simple example of a well-placed task, is
hosting 4 tasks requiring 0.5 vCPU and 2GB of memory reservations in an m5.large
instance (supporting 2 vCPU and 8 GB memory). The reservations of this task
definition take full advantage of the instance’s resources.
