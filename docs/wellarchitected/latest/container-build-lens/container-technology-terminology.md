# Container technology terminology

- **Container** – Containers provide a standard way to package
  your application's code, configurations, and dependencies into a single object. Containers
  share an operating system installed on the host server and run as resource-isolated
  processes, ensuring quick, reliable, and consistent deployments, regardless of
  environment. A container is a runnable instance of an image (see [Deep Dive on Containers](https://aws.amazon.com/getting-started/deep-dive-containers/ "https://aws.amazon.com/getting-started/deep-dive-containers/") on AWS
  getting started resource center). While a container image is immutable, the container adds
  a read/write layer on top of the image to which your application can write information
  like temporary files or logs ([see Docker overview](https://docs.docker.com/get-started/overview/ "https://docs.docker.com/get-started/overview/")). When the container stops and is removed, the information
  written to the temporary read/write layer will be lost.
- **Container image** – Container
  images are read-only templates used to build out containers.
  Container images are immutable, meaning they cannot be changed
  once created. Container images are created using layers by
  reading a text file that is called a Dockerfile that contains
  all necessary information. You can find the
  [Dockerfile
  reference](https://docs.docker.com/engine/reference/builder/ "https://docs.docker.com/engine/reference/builder/") here.
- **Container runtime** – Software running on a container host
  (virtual machine or bare metal server) operating system that is responsible for running
  and managing containers. The container relies on the kernel of the host for all system
  calls.
- **Dockerfile** – A file or series of files containing
  commands that describe the content of a container image. Each command represents a layer
  on the Container image (see the _Container image layers_ definition).
- **Container build** – A container image built from a
  Dockerfile. This process results in a container image containing the necessary components
  to run your containerized application.
- **Base image** – A starting
  point container image that is used in the container build
  process to generate custom or new container images. This image
  has `FROM scratch` in the
  Dockerfile.
- **Parent image** – The images that are used to create your
  image. The parent images are referenced in the `FROM` command of your
  Dockerfile. It is common practice to reference a parent image rather than a base image.
- **Gold image** – A gold image is the standard image for an
  organization to start with. The gold image is used in different business units and defines
  a common baseline for cross-cutting concerns like configuration, networking, and logging.
  This pattern is similar to the [gold Amazon
  Machine Image (AMI)](https://aws.amazon.com/blogs/aws/automate-os-image-build-pipelines-with-ec2-image-builder/ "https://aws.amazon.com/blogs/aws/automate-os-image-build-pipelines-with-ec2-image-builder/") approach for Amazon Elastic Compute Cloud (Amazon EC2) instance AMIs.
- **Container image layers** – In an image, each layer
  represents an instruction in the Dockerfile. Layers are applied in sequence to the base
  image to create the final image. When an image is updated or rebuilt, only the layers that
  change will be updated, and unchanged layers are cached locally. The sizes of each layer
  add up to equal the size of the final image ([see Docker Glossary](https://docs.docker.com/glossary/ "https://docs.docker.com/glossary/")).
- **Container image scanning** – A process for security
  scanning for vulnerabilities in the container image.
- **Container registry** – A service used to store and
  distribute container images. Container images are versioned in container image
  repositories inside the registry. Accessing the content inside the registry is
  standardized in the Open Container Initiative (OCI) distribution specification. Modern
  registries also allow you to store related artifacts such as Helm charts or other
  application specification files (artifact spec support). Registries also control and limit
  access to content stored inside (Auth, RBAC, access logs) and partially also included
  vulnerability scanning features.
- **Continuous integration/Continuous delivery or deployment
  (CI/CD)** – CI refers to an automation strategy that makes sure new code
  changes to an app are built, tested, and pushed to a code repository with little to no
  manual intervention. Continuous delivery is a logical extension of CI in that it makes
  sure that any code change is deployed to the various environments for testing on a defined
  schedule. Continuous deployment takes continuous delivery a step further by making sure
  any changes pushed to the shared repository (repo) through the CI process are
  automatically pushed to production, assuming the changes pass all verification tests in
  previous stages of the build pipeline.
- **CI/CD pipeline** – A CI/CD pipeline consists of tooling and
  automation to deliver a CI/CD strategy.
- **Microservice** – An architectural and organizational
  approach to software development to speed up deployment cycles, foster innovation and
  ownership, improve maintainability and scalability of software applications, and scale
  organizations’ delivery software and services with an agile approach that helps teams work
  independently from each other.
- **Multi-stage build** – A multi-stage build is a mechanism to
  split the build-phase of the image from the final image that will be used to run the
  application.
