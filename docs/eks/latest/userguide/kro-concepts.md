**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# kro concepts

kro enables platform teams to create custom Kubernetes APIs that compose multiple resources into higher-level abstractions.
This topic walks through a practical example, then explains the core concepts you need to understand when working with the EKS Capability for kro.

## Getting started with kro

After creating the kro capability (see [Create a kro capability](create-kro-capability.md "create-kro-capability.md")), you can start creating custom APIs using ResourceGraphDefinitions in your cluster.

Here’s a complete example that creates a simple web application abstraction:

```
apiVersion: kro.run/v1alpha1
kind: ResourceGraphDefinition
metadata:
  name: webapplication
spec:
  schema:
    apiVersion: v1alpha1
    kind: WebApplication
    group: kro.run
    spec:
      name: string | required=true
      image: string | default="nginx:latest"
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
        selector:
          matchLabels:
            app: ${schema.spec.name}
        template:
          metadata:
            labels:
              app: ${schema.spec.name}
          spec:
            containers:
            - name: app
              image: ${schema.spec.image}
              ports:
              - containerPort: 80
  - id: service
    template:
      apiVersion: v1
      kind: Service
      metadata:
        name: ${schema.spec.name}
      spec:
        selector:
          app: ${schema.spec.name}
        ports:
        - protocol: TCP
          port: 80
          targetPort: 80
```

After applying this ResourceGraphDefinition, application teams can create web applications using your simplified API:

```
apiVersion: kro.run/v1alpha1
kind: WebApplication
metadata:
  name: my-app
spec:
  name: my-app
  replicas: 5
```

kro automatically creates the Deployment and Service with the appropriate configuration.
Since `image` isn’t specified, it uses the default value `nginx:latest` from the schema.

## Core concepts

###### Important

kro validates ResourceGraphDefinitions at creation time, not at runtime.
When you create an RGD, kro validates CEL syntax, type-checks expressions against actual Kubernetes schemas, verifies field existence, and detects circular dependencies.
This means errors are caught immediately when you create the RGD, before any instances are deployed.

### ResourceGraphDefinition

A ResourceGraphDefinition (RGD) defines a custom Kubernetes API by specifying:

- **Schema** - The API structure using SimpleSchema format (field names, types, defaults, validation)
- **Resources** - Templates for the underlying Kubernetes or AWS resources to create
- **Dependencies** - How resources relate to each other (automatically detected from field references)

When you apply an RGD, kro registers a new Custom Resource Definition (CRD) in your cluster.
Application teams can then create instances of your custom API, and kro handles creating and managing all the underlying resources.

For more information, see [ResourceGraphDefinition Overview](https://kro.run/docs/concepts/rgd/overview/ "https://kro.run/docs/concepts/rgd/overview/") in the kro documentation.

### SimpleSchema format

SimpleSchema provides a simplified way to define API schemas without requiring OpenAPI knowledge:

```
schema:
  apiVersion: v1alpha1
  kind: Database
  spec:
    name: string | required=true description="Database name"
    size: string | default="small" enum=small,medium,large
    replicas: integer | default=1 minimum=1 maximum=5
```

SimpleSchema supports `string`, `integer`, `boolean`, and `number` types with constraints like `required`, `default`, `minimum`/`maximum`, `enum`, and `pattern`.

For more information, see [SimpleSchema](https://kro.run/docs/concepts/rgd/schema/ "https://kro.run/docs/concepts/rgd/schema/") in the kro documentation.

### CEL expressions

kro uses Common Expression Language (CEL) to reference values dynamically and add conditional logic.
CEL expressions are wrapped in `${` and `}` and can be used in two ways:

**Standalone expressions** - The entire field value is a single expression:

```
spec:
  replicas: ${schema.spec.replicaCount}  # Expression returns integer
  labels: ${schema.spec.labelMap}        # Expression returns object
```

The expression result replaces the entire field value and must match the field’s expected type.

**String templates** - One or more expressions embedded in a string:

```
metadata:
  name: "${schema.spec.prefix}-${schema.spec.name}"  # Multiple expressions
  annotation: "Created by ${schema.spec.owner}"      # Single expression in string
```

All expressions in string templates must return strings.
Use `string()` to convert other types: `"replicas-${string(schema.spec.count)}"`.

**Field references** - Access instance spec values using `schema.spec`:

```
template:
  metadata:
    name: ${schema.spec.name}-deployment
    namespace: ${schema.metadata.namespace}  # Can also reference metadata
  spec:
    replicas: ${schema.spec.replicas}
```

**Optional field access** - Use `?` for fields that might not exist:

```
# For ConfigMaps or Secrets with unknown structure
value: ${configmap.data.?DATABASE_URL}

# For optional status fields
ready: ${deployment.status.?readyReplicas > 0}
```

If the field doesn’t exist, the expression returns `null` instead of failing.

**Conditional resources** - Include resources only when conditions are met:

```
resources:
- id: ingress
  includeWhen:
    - ${schema.spec.enableIngress == true}
  template:
    # ... ingress configuration
```

The `includeWhen` field accepts a list of boolean expressions.
All conditions must be true for the resource to be created.
Currently, `includeWhen` can only reference `schema.spec` fields.

**Transformations** - Transform values using ternary operators and functions:

```
template:
  spec:
    resources:
      requests:
        memory: ${schema.spec.size == "small" ? "512Mi" : "2Gi"}

    # String concatenation
    image: ${schema.spec.registry + "/" + schema.spec.imageName}

    # Type conversion
    port: ${string(schema.spec.portNumber)}
```

**Cross-resource references** - Reference values from other resources:

```
resources:
- id: bucket
  template:
    apiVersion: s3.services.k8s.aws/v1alpha1
    kind: Bucket
    spec:
      name: ${schema.spec.name}-data

- id: configmap
  template:
    apiVersion: v1
    kind: ConfigMap
    data:
      BUCKET_NAME: ${bucket.spec.name}
      BUCKET_ARN: ${bucket.status.ackResourceMetadata.arn}
```

When you reference another resource in a CEL expression, it automatically creates a dependency.
kro ensures the referenced resource is created first.

For more information, see [CEL Expressions](https://kro.run/docs/concepts/rgd/cel-expressions/ "https://kro.run/docs/concepts/rgd/cel-expressions/") in the kro documentation.

### Resource dependencies

kro automatically infers dependencies from CEL expressions—you don’t specify the order, you describe relationships.
When one resource references another using a CEL expression, kro creates a dependency and determines the correct creation order.

```
resources:
- id: bucket
  template:
    apiVersion: s3.services.k8s.aws/v1alpha1
    kind: Bucket
    spec:
      name: ${schema.spec.name}-data

- id: notification
  template:
    apiVersion: s3.services.k8s.aws/v1alpha1
    kind: BucketNotification
    spec:
      bucket: ${bucket.spec.name}  # Creates dependency: notification depends on bucket
```

The expression `${bucket.spec.name}` creates a dependency.
kro builds a directed acyclic graph (DAG) of all resources and their dependencies, then computes a topological order for creation.

**Creation order**: Resources are created in topological order (dependencies first).

**Parallel creation**: Resources with no dependencies are created simultaneously.

**Deletion order**: Resources are deleted in reverse topological order (dependents first).

**Circular dependencies**: Not allowed—kro rejects ResourceGraphDefinitions with circular dependencies during validation.

You can view the computed creation order:

```
kubectl get resourcegraphdefinition my-rgd -o jsonpath='{.status.topologicalOrder}'
```

For more information, see [Graph inference](https://kro.run/docs/concepts/rgd/dependencies-ordering/ "https://kro.run/docs/concepts/rgd/dependencies-ordering/") in the kro documentation.

## Composing with ACK

kro works seamlessly with the EKS Capability for ACK to compose AWS resources with Kubernetes resources:

```
resources:
# Create {aws} S3 bucket with ACK
- id: bucket
  template:
    apiVersion: s3.services.k8s.aws/v1alpha1
    kind: Bucket
    spec:
      name: ${schema.spec.name}-files

# Inject bucket details into Kubernetes ConfigMap
- id: config
  template:
    apiVersion: v1
    kind: ConfigMap
    data:
      BUCKET_NAME: ${bucket.spec.name}
      BUCKET_ARN: ${bucket.status.ackResourceMetadata.arn}

# Use ConfigMap in application deployment
- id: deployment
  template:
    apiVersion: apps/v1
    kind: Deployment
    spec:
      template:
        spec:
          containers:
          - name: app
            envFrom:
            - configMapRef:
                name: ${config.metadata.name}
```

This pattern lets you create AWS resources, extract their details (ARNs, URLs, endpoints), and inject them into your application configuration—all managed as a single unit.

For more composition patterns and advanced examples, see [kro considerations for EKS](kro-considerations.md "kro-considerations.md").

## Next steps

- [kro considerations for EKS](kro-considerations.md "kro-considerations.md") - Learn about EKS-specific patterns, RBAC, and integration with ACK and Argo CD
- [kro Documentation](https://kro.run/docs/overview "https://kro.run/docs/overview") - Comprehensive kro documentation including advanced CEL expressions, validation patterns, and troubleshooting
