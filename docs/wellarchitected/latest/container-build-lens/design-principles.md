# Design principles

The Well-Architected Framework identifies a set of general design
principles to facilitate good design in the cloud for building and
managing container images:

- **Minimize image size:**Reducing the container image size has
  many advantages, such as reducing the attack surface, improving scaling speed as containers
  start faster, and minimizing the amount of storage. One recommended way to achieve this is
  to reduce the number of dependencies and use multi-stage builds. In order to minimize the
  attack surface, only the necessary binaries to run the container should be included in the
  image. The same applies for data. Data should be stored in an external system and it is
  considered best practice to inject configuration data.
- **Build in multiple stages:**
  Builds of an application should be reproducible everywhere and
  all dependencies should be encapsulated. This can be achieved by
  using multi-stage builds. A multi-stage build is a mechanism to
  split the build-phase of the image from the final image that
  will be used to run the application. With this mechanism, you
  can split the build-phase from the final image that will be used
  to run the application.
- **Standardize across the
  business:**Based on a lean parent image, a team- or
  enterprise-wide image can be created that provides optimizations
  to all teams. An organization could potentially start with a
  lean image containing company-specific configurations, and teams
  start adding additional software that is necessary to run the
  different applications. The advantage of this approach is that
  it can help enforce security, quality, and compliance standards
  across multiple teams for the whole organization.
- **Validate and restrict
  versions:** Image tagging can be used to add additional
  meta-information to container images. This is useful for
  codifying version or stability information. For cost management
  purposes, it is recommended to add additional information like
  cost center or department to the tag name. The automatically
  created latest tag shouldn’t be used. A tagging strategy should
  produce immutable tags. Teams should avoid overwrite tags
  because this makes it hard to reproduce issues of specific
  application versions.
- **Implement an image scanning
  strategy:** It is important to scan container images
  regularly after they have been built to make sure no new or
  existing vulnerabilities have surfaced. There are two basic
  categories to consider when discussing image scanning - static
  scanning and dynamic scanning. After pushing code to a git
  repository, a CI/CD chain should automatically build the
  artifact, the container image, and scan it on push.
- **Containers are designed to perform
  stateless actions.** If your application is required to
  store its operational state, then store the state itself in a
  data store, and refer to it from the application running in your
  container. Same with source of truth data stores. The source of
  truth data should be stored outside of the container and your
  application should ingest only the data that is required to
  perform its desired actions.
