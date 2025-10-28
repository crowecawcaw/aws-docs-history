# Considerations for customizing images

When you customize Docker images, you can choose the exact runtime for your job at a
granular level. Consider these best practices when you use this feature. These include considerations for security, configuration,
and mounting an image:

- Security is a shared responsibility between AWS and you. You're responsible for
  security patching the binaries that you add to the image. Follow the [Amazon EMR on EKS security best practices](security-best-practices.md "security-best-practices.md"), especially
  [Get the latest security updates for custom images](security-best-practices.md#security-custom-image "security-best-practices.md#security-custom-image") and [Apply principle of least privilege](security-best-practices.md#security-least-privilege "security-best-practices.md#security-least-privilege").
- When you customize a base image, you must change the Docker user to
  `hadoop:hadoop` so that the jobs do not run with the root user.
- Amazon EMR on EKS mounts files on top of the configurations for the image, such as the
  `spark-defaults.conf`, at run time. To override these configuration files, we
  recommend that you use the `applicationOverrides` parameter during the job
  submission and not directly modify the files in the custom image.
- Amazon EMR on EKS mounts certain folders at run time. Any modifications that you make to these
  folders aren't available in the container. If you want to add an application or its
  dependencies for custom images, we recommend that you choose a directory that isn't part
  of the following predefined paths:
  - `/var/log/fluentd`
  - `/var/log/spark/user`
  - `/var/log/spark/apps`
  - `/mnt`
  - `/tmp`
  - `/home/hadoop`

- You can upload your customized image to any Docker-compatible repository, such as
  Amazon ECR, Docker Hub, or a private enterprise repository. For more information on how to
  configure the Amazon EKS cluster authentication with the selected Docker repository, see [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/ "https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/").
