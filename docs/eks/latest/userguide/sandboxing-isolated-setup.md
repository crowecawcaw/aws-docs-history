

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Run a pod in isolated mode

Isolated mode protects the node and other pods from a compromised container. The parent instance is trusted.

## Choose your setup path
<a name="sandboxing-isolated-choose-path"></a>

You run isolated and confidential pods on EKS in one of two ways. Both run the pod in a Nitro Sandbox and both use the same `runtimeClassName` in the pod spec. They differ only in how the nodes are prepared.

EKS Auto Mode (recommended)  
Auto Mode includes Nitro Sandbox support with no additional setup. You do not build or manage an AMI. Set `runtimeClassName: isolated-sandbox` (or `confidential-sandbox`) on the pod, and Auto Mode provisions a compatible node and runs the pod in a sandbox. This is the simplest path, and the rest of this topic uses it.  
**Set the Kubernetes version when you create the cluster**  
Nitro Sandboxes requires Kubernetes version 1.36 or later. If you create your cluster with `eksctl`, pass `--version`, because `eksctl` uses an older default version. For example:  

```bash
eksctl create cluster --name sandbox-demo --region us-west-2 --version 1.37 --enable-auto-mode
```

Managed or self-managed node groups  
Alternatively, if you run your own node groups outside of Auto Mode, build a custom AMI that includes the Nitro Sandbox runtime, and use a supported instance type. Nitro Sandboxes run on a subset of the instance types that support Nitro Enclaves; for the list, see [supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html#nitro-sandboxes-considerations) in the *Amazon EC2 User Guide*. Launch the nodes with Nitro Enclaves enabled (`EnclaveOptions.Enabled=true`) in the node group’s launch template. Choosing an instance type that supports Nitro Enclaves is not sufficient on its own; without Nitro Enclaves enabled, the node never advertises sandbox capacity. Join those nodes to the cluster, then set the same `runtimeClassName` on the pod. For the build steps, see [Create and update a Nitro Sandbox AMI](sandboxing-ami-create-update.md).

## Prerequisites
<a name="sandboxing-isolated-prerequisites"></a>
+ An Amazon EKS cluster. For the simplest experience, use EKS Auto Mode, which runs isolated and confidential pods without additional configuration.
+ For managed or self-managed node groups outside of Auto Mode, a custom AMI built with the Nitro Sandbox runtime, on a supported instance type. Nitro Sandboxes run on a subset of the instance types that support Nitro Enclaves; for the list, see [supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html#nitro-sandboxes-considerations) in the *Amazon EC2 User Guide*. Launch the nodes with Nitro Enclaves enabled (`EnclaveOptions.Enabled=true`) in the node group’s launch template; otherwise the node never advertises sandbox capacity. See [Create and update a Nitro Sandbox AMI](sandboxing-ami-create-update.md).

## Run a pod in isolated mode
<a name="sandboxing-isolated-run"></a>

Set `runtimeClassName: isolated-sandbox` in your pod spec:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  runtimeClassName: isolated-sandbox
  containers:
  - name: main
    image: public.ecr.aws/amazonlinux/amazonlinux:2023
    command: ["sleep", "3600"]
    resources:
      limits:
        cpu: "1"
        memory: 512Mi
```

Apply the manifest:

```bash
kubectl apply -f manifest.yaml
```

Verify the pod is running:

```bash
kubectl get pod my-app
```

The pod runs inside a Nitro Sandbox. From the workload’s perspective, the environment looks like a normal Linux container. No changes to your application code are required.

## What happens when a pod starts
<a name="sandboxing-isolated-pod-start"></a>

1. A Nitro Sandbox is created for the pod.

1. The Cedar policy attached to the pod is evaluated (if present).

1. The container images are loaded into the sandbox.

1. Containers start inside the sandbox.

Each pod gets its own Nitro Sandbox. Multiple containers within the same pod share a single sandbox.

## Run pods created by a workload controller
<a name="sandboxing-isolated-controllers"></a>

Deployments, StatefulSets, DaemonSets, ReplicaSets, Jobs, and CronJobs create pods from a pod template. Put `runtimeClassName` and every `sandbox.amazonaws.com/` annotation in the pod template, not on the controller object itself:
+  `spec.template.spec.runtimeClassName` 
+  `spec.template.metadata.annotations` 

**Set annotations on the pod template**  
An annotation on the controller’s own metadata is accepted and then ignored. For example, a `sandbox.amazonaws.com/` annotation set on a Deployment’s own `metadata.annotations`, rather than under `spec.template.metadata.annotations`, has no effect. Kubernetes does not copy it into the pods, so policy, network, and throttle annotations placed there have no effect.

Example Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
      annotations:
        sandbox.amazonaws.com/policy: "<base64 policy>"
    spec:
      runtimeClassName: isolated-sandbox
      containers:
      - name: main
        image: public.ecr.aws/amazonlinux/amazonlinux:2023
        command: ["sleep", "3600"]
        resources:
          limits:
            cpu: "1"
            memory: 512Mi
```

Verify that the created pods carry the runtime class:

```bash
kubectl get pods -l app=my-app \
  -o custom-columns='NAME:.metadata.name,RUNTIME:.spec.runtimeClassName'
```