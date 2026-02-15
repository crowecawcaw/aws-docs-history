**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Capability Kubernetes resources

After you enable a capability on your cluster, you will most often interact with it by creating and managing Kubernetes custom resources in your cluster.
Each capability provides its own set of custom resource definitions (CRDs) that extend the Kubernetes API with capability-specific functionality.

## Argo CD resources

When you enable the Argo CD capability, you can create and manage the following Kubernetes resources:

**Application**

Defines a deployment from a Git repository to a target cluster. `Application` resources specify the source repository, target namespace, and sync policy. You can create up to 1000 `Application` resources per Argo CD capability instance.

**ApplicationSet**

Generates multiple `Application` resources from templates, enabling multi-cluster and multi-environment deployments. `ApplicationSet` resources use generators to create `Application` resources dynamically based on cluster lists, Git directories, or other sources.

**AppProject**

Provides logical grouping and access control for `Application` resources. `AppProject` resources define which repositories, clusters, and namespaces `Application` resources can use, enabling multi-tenancy and security boundaries.

Example `Application` resource:

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/repo
    targetRevision: main
    path: manifests
  destination:
    server: https://kubernetes.default.svc
    namespace: production
```

For more information about Argo CD resources and concepts, see [Argo CD concepts](argocd-concepts.md "argocd-concepts.md").

## kro resources

When you enable the kro capability, you can create and manage the following Kubernetes resources:

**ResourceGraphDefinition (RGD)**

Defines a custom API that composes multiple Kubernetes and AWS resources into a higher-level abstraction. Platform teams create `ResourceGraphDefinition` resources to provide reusable patterns with guardrails.

**Custom resource instances**

After creating a `ResourceGraphDefinition` resource, you can create instances of the custom API defined by the `ResourceGraphDefinition`. kro automatically creates and manages the resources specified in the `ResourceGraphDefinition`.

Example `ResourceGraphDefinition` resource:

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
      replicas: integer
  resources:
    - id: deployment
      template:
        apiVersion: apps/v1
        kind: Deployment
        # ... deployment spec
    - id: service
      template:
        apiVersion: v1
        kind: Service
        # ... service spec
```

Example `WebApplication` instance:

```
apiVersion: v1alpha1
kind: WebApplication
metadata:
  name: my-web-app
  namespace: default
spec:
  name: my-web-app
  replicas: 3
```

When you apply this instance, kro automatically creates the `Deployment` and `Service` resources defined in the `ResourceGraphDefinition`.

For more information about kro resources and concepts, see [kro concepts](kro-concepts.md "kro-concepts.md").

## ACK resources

When you enable the ACK capability, you can create and manage AWS resources using Kubernetes custom resources.
ACK provides over 200 CRDs for more than 50 AWS services, allowing you to define AWS resources alongside your Kubernetes workloads, and manage dedicated AWS infrastructure resources with Kubernetes.

Examples of ACK resources:

**S3 Bucket**

`Bucket` resources create and manage Amazon S3 buckets with versioning, encryption, and lifecycle policies.

**RDS DBInstance**

`DBInstance` resources provision and manage Amazon RDS database instances with automated backups and maintenance windows.

**DynamoDB Table**

`Table` resources create and manage DynamoDB tables with provisioned or on-demand capacity.

**IAM Role**

`Role` resources define IAM roles with trust policies and permission policies for AWS service access.

**Lambda Function**

`Function` resources create and manage Lambda functions with code, runtime, and execution role configuration.

Example specification of a `Bucket` resource:

```
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: my-app-bucket
spec:
  name: my-unique-bucket-name-12345
  versioning:
    status: Enabled
  encryption:
    rules:
      - applyServerSideEncryptionByDefault:
          sseAlgorithm: AES256
```

For more information about ACK resources and concepts, see [ACK concepts](ack-concepts.md "ack-concepts.md").

## Resource limits

EKS Capabilities have the following resource limits:

**Argo CD usage limits**:

- Maximum 1000 `Application` resources per Argo CD capability instance
- Maximum 100 remote clusters configured per Argo CD capability instance

**Resource configuration limits**:

- Maximum 150 Kubernetes resources per `Application` resource in Argo CD
- Maximum 64 Kubernetes resources per `ResourceGraphDefinition` in kro

###### Note

These limits apply to the number of resources managed by each capability instance. If you need higher limits, you can deploy capabilities across multiple clusters.

## Next steps

For capability-specific tasks and advanced configuration, see the following topics:

- [ACK concepts](ack-concepts.md "ack-concepts.md") – Understand ACK concepts and resource lifecycle
- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") – Working with Argo CD capabilities for GitOps workflows
- [kro concepts](kro-concepts.md "kro-concepts.md") – Understand kro concepts and resource composition
