**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Resource Composition with kro (Kube Resource Orchestrator)

**kro (Kube Resource Orchestrator)** is an open-source, Kubernetes-native project that allows you to define custom Kubernetes APIs using simple and straightforward configuration.
With kro, you can easily configure new custom APIs that create a group of Kubernetes objects and the logical operations between them.

With EKS Capabilities, kro is fully managed by AWS, eliminating the need to install, maintain, and scale kro controllers on your clusters.

## How kro Works

kro introduces a Custom Resource Definition (CRD) called `ResourceGraphDefinition` (RGD) that enables simple and streamlined creation of custom Kubernetes APIs.
When you create a `ResourceGraphDefinition`, kro uses native Kubernetes extensions to create and manage new APIs in your cluster.
From this single resource specification, kro will create and register a new CRD for you based on your specification and will adapt to manage your newly defined custom resources.

RGDs can include multiple resources, and kro will determine interdependencies and resource ordering, so you don’t have to.
You can use simple syntax to inject configuration from one resource to another, greatly simplifying compositions and removing the need for "glue" operators in your cluster.
With kro, your custom resources can include native Kubernetes resources as well as any Custom Resource Definitions (CRDs) installed in the cluster.

kro supports a single primary resource type:

- **ResourceGraphDefinition (RGD)**: Defines a Kubernetes custom resource, encapsulating one or more underlying native or custom Kubernetes resources

In addition to this resource, kro will create and manage the lifecycle of your custom resources created with it, as well as all of their constituent resources.

kro integrates seamlessly with AWS Controllers for Kubernetes (ACK), allowing you to compose workload resources with AWS resources to create higher-level abstractions.
This enables you to create your own cloud building blocks, simplifying resource management and enabling reusable patterns with default and immutable configuration settings based on your organizational standards.

## Benefits of kro

kro enables platform teams to create custom Kubernetes APIs that compose multiple resources into higher-level abstractions.
This simplifies resource management by allowing developers to deploy complex applications using simple, standardized, and versioned custom resources.
You define reusable patterns for common resource combinations, enabling consistent resource creation across your organization.

kro uses [Common Expression Language (CEL) in Kubernetes](https://kubernetes.io/docs/reference/using-api/cel/ "https://kubernetes.io/docs/reference/using-api/cel/") for passing values between resources and incorporating conditional logic, providing flexibility in resource composition.
You can compose both Kubernetes resources and AWS resources managed by ACK into unified custom APIs, enabling complete application and infrastructure definitions.

kro supports declarative configuration through Kubernetes manifests, enabling GitOps workflows and infrastructure as code practices that integrate seamlessly with your existing development processes.
As part of EKS Managed Capabilities, kro is fully managed by AWS, eliminating the need to install, configure, and maintain kro controllers on your clusters.

**Example: Creating a ResourceGraphDefinition**

The following example shows a simple `ResourceGraphDefinition` that creates a web application with a Deployment and Service:

```
 apiVersion: kro.run/v1alpha1
kind: ResourceGraphDefinition
metadata:
  name: web-application
spec:
  schema:
    apiVersion: v1alpha1
    kind: WebApplication
    spec:
      name: string
      replicas: integer | default=3
  resources:
    - id: deployment
      template:
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: ${schema.spec.name}
        spec:
          replicas: ${schema.spec.replicas}
    - id: service
      template:
        apiVersion: v1
        kind: Service
        metadata:
          name: ${schema.spec.name}
```

When users create instances of the `WebApplication` custom resource, kro automatically creates the corresponding Deployment and Service resources, managing their lifecycle along with the custom resource.

## Integration with Other EKS Managed Capabilities

kro integrates with other EKS Managed Capabilities.

- **AWS Controllers for Kubernetes (ACK)**: Use kro to compose ACK resources into higher-level abstractions, simplifying AWS resource management.
- **Argo CD**: Use Argo CD to manage the deployment of kro custom resources across multiple clusters, enabling GitOps workflows for your platform building blocks and application stacks.

## Getting Started with kro

To get started with the EKS Capability for kro:

1. [Create a kro capability resource](create-kro-capability.md "create-kro-capability.md") on your EKS cluster through the AWS Console, AWS CLI, or your preferred infrastructure as code tool.
2. Create ResourceGraphDefinitions (RGDs) that define your custom APIs and resource compositions.
3. Apply instances of your custom resources to provision and manage the underlying Kubernetes and AWS resources.
