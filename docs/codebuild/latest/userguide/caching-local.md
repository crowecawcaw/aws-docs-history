# Local caching

Local caching stores a cache locally on a build host that is available to that build
host only. This is a good option for intermediate to large build artifacts because the
cache is immediately available on the build host. This is not the best option if your
builds are infrequent. This means that build performance is not impacted by network
transfer time.

If you choose local caching, you must choose one or more of the following cache modes:

- Source cache mode caches Git metadata for primary and secondary sources. After
  the cache is created, subsequent builds pull only the change between commits.
  This mode is a good choice for projects with a clean working directory and a
  source that is a large Git repository. If you choose this option and your
  project does not use a Git repository (AWS CodeCommit, GitHub, GitHub Enterprise
  Server, or Bitbucket), the option is ignored.
- Docker layer cache mode caches existing Docker layers. This mode is a good
  choice for projects that build or pull large Docker images. It can prevent the
  performance issues caused by pulling large Docker images down from the network.

###### Note

    + You can use a Docker layer cache in the Linux environment only.
    + The `privileged` flag must be set so that your project
     has the required Docker permissions.


    By default, Docker daemon is enabled for non-VPC builds. If you would like to use Docker
     containers for VPC builds, see [Runtime
     Privilege and Linux Capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities "https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities") on the Docker Docs website and enable privileged mode. Also, Windows does not support privileged mode.
    + You should consider the security implication before you use a
     Docker layer cache.

- Custom cache mode caches directories you specify in the buildspec file. This
  mode is a good choice if your build scenario is not suited to one of the other
  two local cache modes. If you use a custom cache:
  - Only directories can be specified for caching. You cannot specify
    individual files.
  - Symlinks are used to reference cached directories.
  - Cached directories are linked to your build before it downloads its
    project sources. Cached items overrides source items if they have the
    same name. Directories are specified using cache paths in the buildspec
    file. For more information, see [Buildspec syntax](build-spec-ref.md#build-spec-ref-syntax "build-spec-ref.md#build-spec-ref-syntax").
  - Avoid directory names that are the same in the source and in the
    cache. Locally-cached directories may override, or delete the contents
    of, directories in the source repository that have the same name.

###### Note

Local caching is not supported with the `LINUX_GPU_CONTAINER`
environment type and the `BUILD_GENERAL1_2XLARGE` compute type. For more
information, see [Build environment compute modes and types](build-env-ref-compute-types.md "build-env-ref-compute-types.md").

###### Note

Local caching is not supported when you configure CodeBuild to work with a VPC. For
more information on using VPCs with CodeBuild, see [Use AWS CodeBuild with Amazon Virtual Private Cloud](vpc-support.md "vpc-support.md").
