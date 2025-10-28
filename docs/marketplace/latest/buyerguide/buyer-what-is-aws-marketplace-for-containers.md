# Container products in AWS Marketplace

###### Important

On March 1, 2026, AWS Marketplace will discontinue Quick Launch for Helm chart deployments on Amazon EKS. Existing deployments will continue running normally. You can still deploy using standard Helm commands or container images on Amazon ECS.

Container products are standalone products fulfilled as container images. Container products
can either be free or must be paid for using a seller-provided pricing option. Container
products can be used with multiple container runtimes and services, including [Amazon Elastic Container Service](../../../AmazonECS/latest/developerguide.md "../../../AmazonECS/latest/developerguide.md") (Amazon ECS), [Amazon Elastic Kubernetes Service](../../../eks/latest/userguide.md "../../../eks/latest/userguide.md")
(Amazon EKS), and even services running on your own infrastructure. For a complete list of supported
runtimes and services with more information about each, see [Supported services for container
products](#buyer-container-product-launch-environments "#buyer-container-product-launch-environments").

You can discover, subscribe to, and deploy container products on the AWS Marketplace website or in
the Amazon ECS console. You can deploy many products to Amazon ECS or Amazon EKS by using seller-supplied
deployment templates, such as task definitions or Helm charts. Or, you can access container
images directly from private [Amazon Elastic Container Registry](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md") (Amazon ECR) repositories
after you have subscribed to those products.

If a product has enabled Quick Launch, you can use it to quickly test container products on an Amazon EKS
cluster with just a few steps. Quick Launch uses AWS CloudFormation to create an Amazon EKS cluster and launch
container software on it. For more information about launching with Quick Launch, see [Launching container products with Quick Launch](quick-launch.md#buyer-launch-container-quicklaunch "quick-launch.md#buyer-launch-container-quicklaunch").

This section provides information about finding, subscribing to, and launching container
products in AWS Marketplace.

## Pricing models for paid

container products

Paid container products must have one or more pricing models. Like with any other paid
products in AWS Marketplace, you're billed for paid container products by AWS according to the
pricing model. The pricing model might be a fixed monthly fee or an hourly price, monitored in
seconds and prorated. Pricing details will be shown on the detail page and when you subscribe
to the product.

The supported pricing models for container products in AWS Marketplace are as follows:

- A fixed monthly charge that provides unlimited usage.
- An upfront charge for usage of the product for the duration of a long term
  contract.
- A pay-as-you-go model (typically hourly) based on usage of the product.
- A pay-up-front model with contract pricing.

For more information about each model, see [Container product pricing](../userguide/pricing-container-products.md "../userguide/pricing-container-products.md") in the _AWS Marketplace Seller Guide_.

## Supported services for container

products

The following list includes all of the supported services for container products in
AWS Marketplace. A _supported service_ is a container service or
environment where the product can be launched. A container product must include at least one
fulfillment option that includes a delivery method with instructions to launch to one or more
of the environments.

### Amazon ECS

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast container management service that you can
use to run, stop, and manage containers on a cluster. Your containers are defined in a task
definition that you use to run individual tasks or tasks within a service. In this context,
a service is a configuration that allows you to run and maintain a specified number of tasks
simultaneously in a cluster. You can run your tasks and services on a serverless
infrastructure that's managed by AWS Fargate. Alternatively, for more control over your
infrastructure, you can run your tasks and services on a cluster of Amazon EC2 instances that you
manage.

For more information about Amazon ECS, see [What is Amazon Elastic Container Service](../../../AmazonECS/latest/developerguide/Welcome.md "../../../AmazonECS/latest/developerguide/Welcome.md") in the
_Amazon Elastic Container Service Developer Guide_.

### Amazon EKS

Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service that you can use to run Kubernetes on AWS
without needing to install, operate, and maintain your own Kubernetes control plane or
nodes. Kubernetes is an open-source system for automating the deployment, scaling, and
management of containerized applications.

You can search for, subscribe to, and deploy third-party Kubernetes software using the
Amazon EKS console. For more information, see [Managing Amazon EKS add-ons](../../../eks/latest/userguide/managing-add-ons.md "../../../eks/latest/userguide/managing-add-ons.md") in
the _Amazon EKS User Guide_.

### Self-managed

Kubernetes

You can launch container products on self-managed Kubernetes clusters running in
EKS Anywhere, Amazon ECS Anywhere, Amazon EC2, or on-premises
infrastructure.

Amazon ECS Anywhere is a feature of Amazon ECS that you can use to run and manage
container workloads on customer managed infrastructure. Amazon ECS Anywhere builds
upon Amazon ECS to provide a consistent tooling and API experience across your container-based
applications.

For more information, see [Amazon ECS
Anywhere](https://aws.amazon.com/ecs/anywhere/ "https://aws.amazon.com/ecs/anywhere/").

EKS Anywhere is a service that you can use to create an Amazon EKS cluster on
customer managed infrastructure. You can deploy EKS Anywhere as an
unsupported local environment or as a production-quality environment that can become a
supported on-premises Kubernetes platform.

For more information about EKS Anywhere, see the [EKS Anywhere
documentation](https://anywhere.eks.amazonaws.com/docs/overview/ "https://anywhere.eks.amazonaws.com/docs/overview/").

## Overview of

containers and Kubernetes

Containers, such as Docker containers, are an open-source software technology that provides an additional layer of
abstraction and automation over virtualized operating systems such as Linux and Windows
Server. Just as virtual machines are instances of server images, containers are instances of
Docker container images. They wrap server application software in a file system that contains
everything it needs to run: code, runtime, system tools, system libraries, and so on. With
containers, the software always runs the same, regardless of its environment.

Analogous to Java virtual machines, containers require an underlying platform to provide a
translation and orchestration layer while being isolated from the operating system and each
other. There are different Docker-compatible runtimes and orchestration services that you can
use with Docker containers, including Amazon ECS, which is a highly scalable, high-performance
orchestration service for AWS, and Amazon EKS, which makes it easy to deploy, manage, and scale
containerized applications using [Kubernetes](../../../eks/latest/userguide.md "../../../eks/latest/userguide.md"), an open
source management and orchestration service.
