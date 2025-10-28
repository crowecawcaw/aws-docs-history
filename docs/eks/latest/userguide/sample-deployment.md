**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy a sample application on Linux

In this topic, you deploy a sample application to your cluster on linux nodes.

## Prerequisites

- An existing Kubernetes cluster with at least one node. If you don’t have an existing Amazon EKS cluster, you can deploy one using one of the guides in [Get started with Amazon EKS](getting-started.md "getting-started.md").
- `Kubectl` installed on your computer. For more information, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- `Kubectl` configured to communicate with your cluster. For more information, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md").
- If you plan to deploy your sample workload to Fargate, then you must have an existing [Fargate profile](fargate-profile.md "fargate-profile.md") that includes the same namespace created in this tutorial, which is `eks-sample-app`, unless you change the name. If you created a cluster with one of the gudes in [Get started with Amazon EKS](getting-started.md "getting-started.md"), then you’ll have to create a new profile, or add the namespace to your existing profile, because the profile created in the getting started guides doesn’t specify the namespace used in this tutorial. Your VPC must also have at least one private subnet.

Though many variables are changeable in the following steps, we recommend only changing variable values where specified. Once you have a better understanding of Kubernetes Pods, deployments, and services, you can experiment with changing other values.

## Create a namespace

A namespace allows you to group resources in Kubernetes. For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ "https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/") in the Kubernetes documentation. If you plan to deploy your sample application to [Simplify compute management with AWS Fargate](fargate.md "fargate.md"), make sure that the value for `namespace` in your [Define which Pods use AWS Fargate when launched](fargate-profile.md "fargate-profile.md") is `eks-sample-app`.

```
kubectl create namespace eks-sample-app
```

## Create a Kubernetes deployment

Create a Kubernetes deployment. This sample deployment pulls a container image from a public repository and deploys three replicas (individual Pods) of it to your cluster. To learn more, see [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/") in the Kubernetes documentation.

1. Save the following contents to a file named `eks-sample-deployment.yaml`. The containers in the sample application don’t use network storage, but you might have applications that need to. For more information, see [Use application data storage for your cluster](storage.md "storage.md").
   - The `amd64` or `arm64`
     `values` under the `kubernetes.io/arch` key mean that the application can be deployed to either hardware architecture (if you have both in your cluster). This is possible because this image is a multi-architecture image, but not all are. You can determine the hardware architecture that the image is supported on by viewing the [image details](https://gallery.ecr.aws/nginx/nginx "https://gallery.ecr.aws/nginx/nginx") in the repository that you’re pulling it from. When deploying images that don’t support a hardware architecture type, or that you don’t want the image deployed to, remove that type from the manifest. For more information, see [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/ "https://kubernetes.io/docs/reference/labels-annotations-taints/") in the Kubernetes documentation.
   - The `kubernetes.io/os: linux`
     `nodeSelector` means that if you had Linux and Windows nodes (for example) in your cluster, the image would only be deployed to Linux nodes. For more information, see [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/ "https://kubernetes.io/docs/reference/labels-annotations-taints/") in the Kubernetes documentation.

   ```
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: eks-sample-linux-deployment
     namespace: eks-sample-app
     labels:
       app: eks-sample-linux-app
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: eks-sample-linux-app
     template:
       metadata:
         labels:
           app: eks-sample-linux-app
       spec:
         affinity:
           nodeAffinity:
             requiredDuringSchedulingIgnoredDuringExecution:
               nodeSelectorTerms:
               - matchExpressions:
                 - key: kubernetes.io/arch
                   operator: In
                   values:
                   - amd64
                   - arm64
         containers:
         - name: nginx
           image: public.ecr.aws/nginx/nginx:1.23
           ports:
           - name: http
             containerPort: 80
           imagePullPolicy: IfNotPresent
         nodeSelector:
           kubernetes.io/os: linux
   ```

2. Apply the deployment manifest to your cluster.

```
kubectl apply -f eks-sample-deployment.yaml
```

## Create a service

A service allows you to access all replicas through a single IP address or name. For more information, see [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "https://kubernetes.io/docs/concepts/services-networking/service/") in the Kubernetes documentation. Though not implemented in the sample application, if you have applications that need to interact with other AWS services, we recommend that you create Kubernetes service accounts for your Pods, and associate them to AWS IAM accounts. By specifying service accounts, your Pods have only the minimum permissions that you specify for them to interact with other services. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md").

1. Save the following contents to a file named `eks-sample-service.yaml`. Kubernetes assigns the service its own IP address that is accessible only from within the cluster. To access the service from outside of your cluster, deploy the [AWS Load Balancer Controller](aws-load-balancer-controller.md "aws-load-balancer-controller.md") to load balance [application](alb-ingress.md "alb-ingress.md") or [network](network-load-balancing.md "network-load-balancing.md") traffic to the service.

```
apiVersion: v1
kind: Service
metadata:
  name: eks-sample-linux-service
  namespace: eks-sample-app
  labels:
    app: eks-sample-linux-app
spec:
  selector:
    app: eks-sample-linux-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

2. Apply the service manifest to your cluster.

```
kubectl apply -f eks-sample-service.yaml
```

## Review resources created

1. View all resources that exist in the `eks-sample-app` namespace.

```
kubectl get all -n eks-sample-app
```

An example output is as follows.

```
NAME                                               READY   STATUS    RESTARTS   AGE
pod/eks-sample-linux-deployment-65b7669776-m6qxz   1/1     Running   0          27m
pod/eks-sample-linux-deployment-65b7669776-mmxvd   1/1     Running   0          27m
pod/eks-sample-linux-deployment-65b7669776-qzn22   1/1     Running   0          27m

NAME                               TYPE         CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/eks-sample-linux-service   ClusterIP    10.100.74.8     <none>        80/TCP    32m

NAME                                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/eks-sample-linux-deployment 3/3     3            3           27m

NAME                                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/eks-sample-linux-deployment-776d8f8fd8    3         3         3       27m
```

In the output, you see the service and deployment that were specified in the sample manifests deployed in previous steps. You also see three Pods. This is because `3`
`replicas` were specified in the sample manifest. For more information about Pods, see [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/ "https://kubernetes.io/docs/concepts/workloads/pods/pod/") in the Kubernetes documentation. Kubernetes automatically creates the `replicaset` resource, even though it isn’t specified in the sample manifests. For more information about `ReplicaSets`, see [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/ "https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/") in the Kubernetes documentation.

###### Note

Kubernetes maintains the number of replicas that are specified in the manifest. If this were a production deployment and you wanted Kubernetes to horizontally scale the number of replicas or vertically scale the compute resources for the Pods, use the [Scale pod deployments with Horizontal Pod Autoscaler](horizontal-pod-autoscaler.md "horizontal-pod-autoscaler.md") and the [Adjust pod resources with Vertical Pod Autoscaler](vertical-pod-autoscaler.md "vertical-pod-autoscaler.md") to do so. 2. View the details of the deployed service.

```
kubectl -n eks-sample-app describe service eks-sample-linux-service
```

An example output is as follows.

```
Name:              eks-sample-linux-service
Namespace:         eks-sample-app
Labels:            app=eks-sample-linux-app
Annotations:       <none>
Selector:          app=eks-sample-linux-app
Type:              ClusterIP
IP Families:       <none>
IP:                10.100.74.8
IPs:               10.100.74.8
Port:              <unset>  80/TCP
TargetPort:        80/TCP
Endpoints:         192.168.24.212:80,192.168.50.185:80,192.168.63.93:80
Session Affinity:  None
Events:            <none>
```

In the previous output, the value for `IP:` is a unique IP address that can be reached from any node or Pod within the cluster, but it can’t be reached from outside of the cluster. The values for `Endpoints` are IP addresses assigned from within your VPC to the Pods that are part of the service. 3. View the details of one of the Pods listed in the output when you viewed the namespace in a previous step. Replace `776d8f8fd8-78w66` with the value returned for one of your Pods.

```
kubectl -n eks-sample-app describe pod eks-sample-linux-deployment-65b7669776-m6qxz
```

Abbreviated example output

```
Name:         eks-sample-linux-deployment-65b7669776-m6qxz
Namespace:    eks-sample-app
Priority:     0
Node:         ip-192-168-45-132.us-west-2.compute.internal/192.168.45.132
[...]
IP:           192.168.63.93
IPs:
  IP:           192.168.63.93
Controlled By:  ReplicaSet/eks-sample-linux-deployment-65b7669776
[...]
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
[...]
Events:
  Type    Reason     Age    From                                                 Message
  ----    ------     ----   ----                                                 -------
  Normal  Scheduled  3m20s  default-scheduler                                    Successfully assigned eks-sample-app/eks-sample-linux-deployment-65b7669776-m6qxz to ip-192-168-45-132.us-west-2.compute.internal
[...]
```

In the previous output, the value for `IP:` is a unique IP that’s assigned to the Pod from the CIDR block assigned to the subnet that the node is in. If you prefer to assign Pods IP addresses from different CIDR blocks, you can change the default behavior. For more information, see [Deploy Pods in alternate subnets with custom networking](cni-custom-network.md "cni-custom-network.md"). You can also see that the Kubernetes scheduler scheduled the Pod on the `Node` with the IP address `192.168.45.132`.

###### Tip

Rather than using the command line, you can view many details about Pods, services, deployments, and other Kubernetes resources in the AWS Management Console. For more information, see [View Kubernetes resources in the AWS Management Console](view-kubernetes-resources.md "view-kubernetes-resources.md").

## Run a shell on a Pod

1. Run a shell on the Pod that you described in the previous step, replacing `65b7669776-m6qxz` with the ID of one of your Pods.

```
kubectl exec -it eks-sample-linux-deployment-65b7669776-m6qxz -n eks-sample-app -- /bin/bash
```

2. From the Pod shell, view the output from the web server that was installed with your deployment in a previous step. You only need to specify the service name. It is resolved to the service’s IP address by CoreDNS, which is deployed with an Amazon EKS cluster, by default.

```
curl eks-sample-linux-service
```

An example output is as follows.

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
[...]
```

3. From the Pod shell, view the DNS server for the Pod.

```
cat /etc/resolv.conf
```

An example output is as follows.

```
nameserver 10.100.0.10
search eks-sample-app.svc.cluster.local svc.cluster.local cluster.local us-west-2.compute.internal
options ndots:5
```

In the previous output, `10.100.0.10` is automatically assigned as the `nameserver` for all Pods deployed to the cluster. 4. Disconnect from the Pod by typing `exit`. 5. Once you’re finished with the sample application, you can remove the sample namespace, service, and deployment with the following command.

```
kubectl delete namespace eks-sample-app
```

## Next Steps

After you deploy the sample application, you might want to try some of the following exercises:

- [Route application and HTTP traffic with Application Load Balancers](alb-ingress.md "alb-ingress.md")
- [Route TCP and UDP traffic with Network Load Balancers](network-load-balancing.md "network-load-balancing.md")
