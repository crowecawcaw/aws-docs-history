**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Migrate from EKS Fargate to EKS Auto Mode

This topic walks you through the process of migrating workloads from EKS Fargate to Amazon EKS Auto Mode using `kubectl`.
The migration can be performed gradually, allowing you to move workloads at your own pace while maintaining cluster stability and application availability throughout the transition.

The step-by-step approach outlined below enables you to run EKS Fargate and EKS Auto Mode side by side during the migration period.
This dual-operation strategy helps ensure a smooth transition by allowing you to validate workload behavior on EKS Auto Mode before completely decommissioning EKS Fargate.
You can migrate applications individually or in groups, providing flexibility to accommodate your specific operational requirements and risk tolerance.

## Comparing Amazon EKS Auto Mode and EKS with AWS Fargate

Amazon EKS with AWS Fargate remains an option for customers who want to run EKS, but Amazon EKS Auto Mode is the recommended approach moving forward.
EKS Auto Mode is fully Kubernetes conformant, supporting all upstream Kubernetes primitives and platform tools like Istio, which Fargate is unable to support.
EKS Auto Mode also fully supports all EC2 runtime purchase options, including GPU and Spot instances, enabling customers to leverage negotiated EC2 discounts and other savings mechanisms
These capabilities are not available when using EKS with Fargate.

Furthermore, EKS Auto Mode allows customers to achieve the same isolation model as Fargate, using standard Kubernetes scheduling capabilities to ensure each EC2 instance runs a single application container.
By adopting Amazon EKS Auto Mode, customers can unlock the full benefits of running Kubernetes on AWS — a fully Kubernetes-conformant platform that provides the flexibility to leverage the entire breadth of EC2 and purchasing options while retaining the ease of use and abstraction from infrastructure management that Fargate provides.

## Prerequisites

Before beginning the migration, ensure you have

- Set up a cluster with Fargate. For more information, see [Get started with AWS Fargate for your cluster](fargate-getting-started.md "fargate-getting-started.md").
- Installed and connected `kubectl` to your cluster. For more information, see [Set up to use Amazon EKS](setting-up.md "setting-up.md").

## Step 1: Check the Fargate cluster

1. Check if the EKS cluster with Fargate is running:

```
 kubectl get node
```

```
NAME STATUS ROLES AGE VERSION
fargate-ip-192-168-92-52.ec2.internal Ready <none> 25m v1.30.8-eks-2d5f260
fargate-ip-192-168-98-196.ec2.internal Ready <none> 24m v1.30.8-eks-2d5f260
```

2. Check running pods:

```
 kubectl get pod -A
```

```
NAMESPACE NAME READY STATUS RESTARTS AGE
kube-system coredns-6659cb98f6-gxpjz 1/1 Running 0 26m
kube-system coredns-6659cb98f6-gzzsx 1/1 Running 0 26m
```

3. Create a deployment in a file called `deployment_fargate.yaml`:

```
 apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
      annotations:
        eks.amazonaws.com/compute-type: fargate
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

4. Apply the deployment:

```
 kubectl apply -f deployment_fargate.yaml
```

```
deployment.apps/nginx-deployment created
```

5. Check the pods and deployments:

```
 kubectl get pod,deploy
```

```
NAME                                    READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-5c7479459b-6trtm   1/1     Running   0          61s
pod/nginx-deployment-5c7479459b-g8ssb   1/1     Running   0          61s
pod/nginx-deployment-5c7479459b-mq4mf   1/1     Running   0          61s

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   3/3     3            3           61s
```

6. Check the node:

```
 kubectl get node -owide
```

```
NAME                                    STATUS  ROLES  AGE VERSION             INTERNAL-IP     EXTERNAL-IP OS-IMAGE       KERNEL-VERSION                  CONTAINER-RUNTIME
fargate-ip-192-168-111-43.ec2.internal  Ready   <none> 31s v1.30.8-eks-2d5f260 192.168.111.43  <none>      Amazon Linux 2 5.10.234-225.910.amzn2.x86_64  containerd://1.7.25
fargate-ip-192-168-117-130.ec2.internal Ready   <none> 36s v1.30.8-eks-2d5f260 192.168.117.130 <none>      Amazon Linux 2 5.10.234-225.910.amzn2.x86_64  containerd://1.7.25
fargate-ip-192-168-74-140.ec2.internal  Ready   <none> 36s v1.30.8-eks-2d5f260 192.168.74.140  <none>      Amazon Linux 2 5.10.234-225.910.amzn2.x86_64  containerd://1.7.25
```

## Step 2: Enable EKS Auto Mode on the cluster

1. Enable EKS Auto Mode on your existing cluster using the AWS CLI or Management Console. For more information, see [Enable EKS Auto Mode on an existing cluster](auto-enable-existing.md "auto-enable-existing.md").
2. Check the nodepool:

```
 kubectl get nodepool
```

```
NAME              NODECLASS   NODES   READY   AGE
general-purpose   default     1       True    6m58s
system            default     0       True    3d14h
```

## Step 3: Update workloads for migration

Identify and update the workloads you want to migrate to EKS Auto Mode.

To migrate a workload from Fargate to EKS Auto Mode, apply the annotation `eks.amazonaws.com/compute-type: ec2`.
This ensures that the workload will not be scheduled by Fargate, despite the Fargate profile,
and will be caught up by the EKS Auto Mode NodePool.
For more information, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md").

1. Modify your deployments (for example, the `deployment_fargate.yaml` file) to change the compute type to `ec2`:

```
 apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
      annotations:
        eks.amazonaws.com/compute-type: ec2
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

2. Apply the deployment. This change allows the workload to be scheduled on the new EKS Auto Mode nodes:

```
 kubectl apply -f deployment_fargate.yaml
```

3. Check that the deployment is running in the EKS Auto Mode cluster:

```
 kubectl get pod -o wide
```

```
NAME                               READY   STATUS    RESTARTS   AGE     IP               NODE                  NOMINATED NODE   READINESS GATES
nginx-deployment-97967b68d-ffxxh   1/1     Running   0          3m31s   192.168.43.240   i-0845aafcb51630ffb   <none>           <none>
nginx-deployment-97967b68d-mbcgj   1/1     Running   0          2m37s   192.168.43.241   i-0845aafcb51630ffb   <none>           <none>
nginx-deployment-97967b68d-qpd8x   1/1     Running   0          2m35s   192.168.43.242   i-0845aafcb51630ffb   <none>           <none>
```

4. Verify there is no Fargate node running and deployment running in the EKS Auto Mode managed nodes:

```
 kubectl get node -owide
```

```
NAME                STATUS ROLES  AGE   VERSION             INTERNAL-IP     EXTERNAL-IP OS-IMAGE                                         KERNEL-VERSION CONTAINER-RUNTIME
i-0845aafcb51630ffb Ready  <none> 3m30s v1.30.8-eks-3c20087 192.168.41.125  3.81.118.95 Bottlerocket (EKS Auto) 2025.3.14 (aws-k8s-1.30) 6.1.129        containerd://1.7.25+bottlerocket
```

## Step 4: Gradually migrate workloads

Repeat Step 3 for each workload you want to migrate.
This allows you to move workloads individually or in groups, based on your requirements and risk tolerance.

## Step 5: Remove the original fargate profile

Once all workloads have been migrated, you can remove the original `fargate` profile.
Replace `<fargate profile name>` with the name of your Fargate profile:

```
 aws eks delete-fargate-profile --cluster-name eks-fargate-demo-cluster --fargate-profile-name <fargate profile name>
```

## Step 6: Scale down CoreDNS

Because EKS Auto mode handles CoreDNS, you scale the `coredns` deployment down to 0:

```
 kubectl scale deployment coredns -n kube-system —-replicas=0
```
