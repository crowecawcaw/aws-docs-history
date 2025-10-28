# Best practices for Amazon ECS container images

A container image is a set of instructions on how to build the container. A container image
holds your application code and all the dependencies that your application code
requires to run. Application dependencies include the source code packages that your
application code relies on, a language runtime for interpreted languages, and binary
packages that your dynamically linked code relies on.

Use the following guidelines when you design and build your container
images:

- Make your container images complete by storing all application dependencies as static
  files inside the container image.

If you change something in the container image, build a new container image with the
changes.

- Run a single application process within a container.

The container lifetime is as long as the application process runs. Amazon ECS replaces crashed
processes and determines where to launch the replacement process. A complete
image makes the overall deployment more resilient.

- Make your application handle `SIGTERM`.

When Amazon ECS stops a task, it first sends a SIGTERM signal to the task to notify the
application that it needs to finish and shut down. Amazon ECS then sends a
`SIGKILL` message. When applications ignore the
`SIGTERM`, the Amazon ECS service must wait to send the
`SIGKILL` signal to terminate the process.

You need to identify how long it takes your application to complete its work, and ensure
that your applications handles the `SIGTERM` signal. The
application's signal handling needs to stop the application from taking new
work and complete the work that is in-progress, or save unfinished work to
storage outside of the task when the work takes too long to complete.

- Configure containerized applications to write logs to `stdout`
  and `stderr`.

Decoupling log handling from your application code gives you flexibility
to adjust log handling at the infrastructure level. One example of this is
to change your logging system. Instead of modifying your services, and
building and deploying a new container image, you can adjust the settings.

- Use tags to version your container images.

Container images are stored in a container registry. Each image in a registry is identified
by a tag. There's a tag called `latest`. This tag functions as a pointer to the
latest version of the application container image, similar to the `HEAD` in a git
repository. We recommend that you use the `latest` tag only for testing purposes. As
a best practice, tag container images with a unique tag for each build. We recommend that you
tag your images using the git SHA for the git commit that was used to build the image.

You don’t need to build a container image for every commit. However, we recommend that you
build a new container image each time you release a particular code commit to the production
environment. We also recommend that you tag the image with a tag that corresponds to the git
commit of the code that's inside the image. If you tagged the image with the git commit, you can
more quickly find which version of the code the image is running.

We also recommend that you turn on immutable image tags in Amazon Elastic Container Registry. With this setting,
you can't change the container image that a tag points at. Instead Amazon ECR
enforces that a new image must be uploaded to a new tag. For more
information, see [Image tag
mutability](../../../AmazonECR/latest/userguide/image-tag-mutability.md "../../../AmazonECR/latest/userguide/image-tag-mutability.md") in the _Amazon ECR User
Guide_.
When you architect your application to run on AWS Fargate, you must decide between
deploying multiple containers into the same task definition and deploying containers
separately in multiple task definitions. If the following conditions are required,
we recommend deploying multiple containers into the same task definition:

- Your containers share a common lifecycle (that is, they're launched and
  terminated together).
- Your containers must run on the same underlying host (that is, one
  container references the other on a localhost port).
- Your containers share resources.
- Your containers share data volumes.
  If these conditions aren't required, we recommend deploying containers separately in
  multiple task definitions. This allows you to scale, provision, and deprovision the
  containers separately.
