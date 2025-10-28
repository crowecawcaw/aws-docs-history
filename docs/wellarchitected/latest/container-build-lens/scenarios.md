# Scenarios

This section includes a set of customer use cases, applications for AWS features and
services, reporting requirements, data structures, testing protocols, and workloads.

We will cover a series of scenarios that represent common patterns and strategies that are
used when designing and building containerized applications. We will present the assumptions we
made for each of these scenarios, the common drivers for the design, and a reference
architecture of how these scenarios should be implemented.

The [Container technology terminology](container-technology-terminology.md "container-technology-terminology.md") is a common component across the
scenarios in the whitepaper. A CI/CD pipeline consists of the tools and automation to deliver a
CI/CD strategy. The pipeline tools are general responsible for building code, running tests, and
deploying updated versions of applications automatically.

Building a continuous integration (CI) pipeline that builds your
containerized application and base images is critical to automating
the software development lifecycle. CI pipelines enable development
teams to automate the staging and building of the containerized
application and base container images to ensure that development
teams are focused on application development and not code
deployment.

###### Topics

- [Securing containerized build pipelines](securing-containerized-build-pipelines.md "securing-containerized-build-pipelines.md")
- [Improving containerized CI/CD pipelines from performance efficiency and cost perspective](improving-containerized-cicd-pipelines-from-performance-efficiency-and-cost-perspective.md "improving-containerized-cicd-pipelines-from-performance-efficiency-and-cost-perspective.md")
- [Improving performance for container image build process](improving-performance-for-container-image-build-process.md "improving-performance-for-container-image-build-process.md")
