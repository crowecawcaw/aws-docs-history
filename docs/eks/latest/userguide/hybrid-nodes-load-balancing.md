**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure Services of type LoadBalancer for hybrid nodes

This topic describes how to configure Layer 4 (L4) load balancing for applications running on Amazon EKS Hybrid Nodes. Kubernetes Services of type LoadBalancer are used to expose Kubernetes applications external to the cluster. Services of type LoadBalancer are commonly used with physical load balancer infrastructure in the cloud or on-premises environment to serve the workload’s traffic. This load balancer infrastructure is commonly provisioned with an environment-specific controller.

AWS supports AWS Network Load Balancer (NLB) and Cilium for Services of type LoadBalancer running on EKS Hybrid Nodes. The decision to use NLB or Cilium is based on the source of application traffic. If application traffic originates from an AWS Region, AWS recommends using AWS NLB and the AWS Load Balancer Controller. If application traffic originates from the local on-premises or edge environment, AWS recommends using Cilium’s built-in load balancing capabilities, which can be used with or without load balancer infrastructure in your environment.

For Layer 7 (L7) application traffic load balancing, see [Configure Kubernetes Ingress for hybrid nodes](hybrid-nodes-ingress.md "hybrid-nodes-ingress.md"). For general information on Load Balancing with EKS, see [Best Practices for Load Balancing](../best-practices/load-balancing.md "../best-practices/load-balancing.md").

## AWS Network Load Balancer

You can use the [AWS Load Balancer Controller](aws-load-balancer-controller.md "aws-load-balancer-controller.md") and NLB with the target type `ip` for workloads running on hybrid nodes. When using target type `ip`, NLB forwards traffic directly to the pods, bypassing the Service layer network path. For NLB to reach the pod IP targets on hybrid nodes, your on-premises pod CIDRs must be routable on your on-premises network. Additionally, the AWS Load Balancer Controller uses webhooks and requires direct communication from the EKS control plane. For more information, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md").

- See [Route TCP and UDP traffic with Network Load Balancers](network-load-balancing.md "network-load-balancing.md") for subnet configuration requirements, and [Install AWS Load Balancer Controller with Helm](lbc-helm.md "lbc-helm.md") and [Best Practices for Load Balancing](../best-practices/load-balancing.md "../best-practices/load-balancing.md") for additional information about AWS Network Load Balancer and AWS Load Balancer Controller.
- See [AWS Load Balancer Controller NLB configurations](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/nlb/ "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/nlb/") for configurations that can be applied to Services of type `LoadBalancer` with AWS Network Load Balancer.

### Prerequisites

- Cilium installed following the instructions in [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md").
- Cilium BGP Control Plane enabled following the instructions in [Configure Cilium BGP for hybrid nodes](hybrid-nodes-cilium-bgp.md "hybrid-nodes-cilium-bgp.md"). If you do not want to use BGP, you must use an alternative method to make your on-premises pod CIDRs routable on your on-premises network, see [Routable remote Pod CIDRs](hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-pod-cidrs "hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-pod-cidrs") for more information.
- Helm installed in your command-line environment, see [Setup Helm instructions](helm.md "helm.md").
- eksctl installed in your command-line environment, see [Setup eksctl instructions](install-kubectl.md#eksctl-install-update "install-kubectl.md#eksctl-install-update").

### Procedure

1. Download an IAM policy for the AWS Load Balancer Controller that allows it to make calls to AWS APIs on your behalf.

```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/refs/heads/main/docs/install/iam_policy.json
```

2. Create an IAM policy using the policy downloaded in the previous step.

```
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json
```

3. Replace the values for cluster name (`CLUSTER_NAME`), AWS Region (`AWS_REGION`), and AWS account ID (`AWS_ACCOUNT_ID`) with your settings and run the following command.

```
eksctl create iamserviceaccount \
    --cluster=CLUSTER_NAME \
    --namespace=kube-system \
    --name=aws-load-balancer-controller \
    --attach-policy-arn=arn:aws:iam::AWS_ACCOUNT_ID:policy/AWSLoadBalancerControllerIAMPolicy \
    --override-existing-serviceaccounts \
    --region AWS_REGION \
    --approve
```

4. Add the eks-charts Helm chart repository. AWS maintains this repository on GitHub.

```
helm repo add eks https://aws.github.io/eks-charts
```

5. Update your local Helm repository to make sure that you have the most recent charts.

```
helm repo update eks
```

6. Install the AWS Load Balancer Controller. Replace the values for cluster name (`CLUSTER_NAME`), AWS Region (`AWS_REGION`), VPC ID (`VPC_ID`), and AWS Load Balancer Controller Helm chart version (`AWS_LBC_HELM_VERSION`) with your settings. You can find the latest version of the Helm chart by running `helm search repo eks/aws-load-balancer-controller --versions`. If you are running a mixed mode cluster with both hybrid nodes and nodes in AWS Cloud, you can run the AWS Load Balancer Controller on cloud nodes following the instructions at [AWS Load Balancer Controller](hybrid-nodes-webhooks.md#hybrid-nodes-mixed-lbc "hybrid-nodes-webhooks.md#hybrid-nodes-mixed-lbc").

```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --version `AWS_LBC_HELM_VERSION` \
  --set clusterName=`CLUSTER_NAME` \
  --set region=`AWS_REGION` \
  --set vpcId=`VPC_ID` \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller
```

7. Verify the AWS Load Balancer Controller was installed successfully.

```
kubectl get -n kube-system deployment aws-load-balancer-controller
```

```
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
aws-load-balancer-controller   2/2     2            2           84s
```

8. Define a sample application in a file named `tcp-sample-app.yaml`. The example below uses a simple NGINX deployment with a TCP port.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tcp-sample-app
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: public.ecr.aws/nginx/nginx:1.23
          ports:
            - name: tcp
              containerPort: 80
```

9. Apply the deployment to your cluster.

```
kubectl apply -f tcp-sample-app.yaml
```

10. Define a Service of type LoadBalancer for the deployment in a file named `tcp-sample-service.yaml`.

```
apiVersion: v1
kind: Service
metadata:
  name: tcp-sample-service
  namespace: default
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: external
    service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: ip
    service.beta.kubernetes.io/aws-load-balancer-scheme: internet-facing
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
```

11. Apply the Service configuration to your cluster.

```
kubectl apply -f tcp-sample-service.yaml
```

12. Provisioning the NLB for the Service may take a few minutes. Once the NLB is provisioned, the Service will have an address assigned to it that corresponds to the DNS name of the NLB deployment.

```
kubectl get svc tcp-sample-service
```

```
NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP                                                                    PORT(S)        AGE
tcp-sample-service   LoadBalancer   172.16.115.212   k8s-default-tcpsampl-xxxxxxxxxx-xxxxxxxxxxxxxxxx.elb.<region>.amazonaws.com   80:30396/TCP   8s
```

13. Access the Service using the address of the NLB.

```
curl k8s-default-tcpsampl-xxxxxxxxxx-xxxxxxxxxxxxxxxx.elb.<region>.amazonaws.com
```

An example output is below.

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
[...]
```

14. Clean up the resources you created.

```
kubectl delete -f tcp-sample-service.yaml
kubectl delete -f tcp-sample-app.yaml
```

## Cilium in-cluster load balancing

Cilium can be used as an in-cluster load balancer for workloads running on EKS Hybrid Nodes, which can be useful for environments that do not have load balancer infrastructure. Cilium’s load balancing capabilities are built on a combination of Cilium features including kube-proxy replacement, Load Balancer IP Address Management (IPAM), and BGP Control Plane. The responsibilities of these features are detailed below:

- **Cilium kube-proxy replacement**: Handles routing Service traffic to backend pods.
- **Cilium Load Balancer IPAM**: Manages IP addresses that can be assigned to Services of type `LoadBalancer`.
- **Cilium BGP Control Plane**: Advertises IP addresses allocated by Load Balancer IPAM to the on-premises network.

If you are not using Cilium’s kube-proxy replacement, you can still use Cilium Load Balancer IPAM and BGP Control Plane to allocate and assign IP addresses for Services of type LoadBalancer. If you are not using Cilium’s kube-proxy replacement, the load balancing for Services to backend pods is handled by kube-proxy and iptables rules by default in EKS.

### Prerequisites

- Cilium installed following the instructions in [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md") with or without kube-proxy replacement enabled. Cilium’s kube-proxy replacement requires running an operating system with a Linux kernel at least as recent as v4.19.57, v5.1.16, or v5.2.0. All recent versions of the operating systems supported for use with hybrid nodes meet this criteria, with the exception of Red Hat Enterprise Linux (RHEL) 8.x.
- Cilium BGP Control Plane enabled following the instructions in [Configure Cilium BGP for hybrid nodes](hybrid-nodes-cilium-bgp.md "hybrid-nodes-cilium-bgp.md"). If you do not want to use BGP, you must use an alternative method to make your on-premises pod CIDRs routable on your on-premises network, see [Routable remote Pod CIDRs](hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-pod-cidrs "hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-pod-cidrs") for more information.
- Helm installed in your command-line environment, see [Setup Helm instructions](helm.md "helm.md").

### Procedure

1. Create a file named `cilium-lbip-pool-loadbalancer.yaml` with a `CiliumLoadBalancerIPPool` resource to configure the Load Balancer IP address range for your Services of type LoadBalancer.
   - Replace `LB_IP_CIDR` with the IP address range to use for the Load Balancer IP addresses. To select a single IP address, use a `/32` CIDR. For more information, see [LoadBalancer IP Address Management](https://docs.cilium.io/en/stable/network/lb-ipam/ "https://docs.cilium.io/en/stable/network/lb-ipam/") in the Cilium documentation.
   - The `serviceSelector` field is configured to match against the name of the Service you will create in a subsequent step. With this configuration, IPs from this pool will only be allocated to Services with the name `tcp-sample-service`.

   ```
   apiVersion: cilium.io/v2alpha1
   kind: CiliumLoadBalancerIPPool
   metadata:
     name: tcp-service-pool
   spec:
     blocks:
     - cidr: "LB_IP_CIDR"
     serviceSelector:
       matchLabels:
         io.kubernetes.service.name: tcp-sample-service
   ```

2. Apply the `CiliumLoadBalancerIPPool` resource to your cluster.

```
kubectl apply -f cilium-lbip-pool-loadbalancer.yaml
```

3. Confirm there is at least one IP address available in the pool.

```
kubectl get ciliumloadbalancerippools.cilium.io
```

```
NAME               DISABLED   CONFLICTING   IPS AVAILABLE   AGE
tcp-service-pool   false      False         1               24m
```

4. Create a file named `cilium-bgp-advertisement-loadbalancer.yaml` with a `CiliumBGPAdvertisement` resource to advertise the load balancer IP address for the Service you will create in the next step. If you are not using Cilium BGP, you can skip this step. The load balancer IP address used for your Service must be routable on your on-premises network for you to be able to query the service in the final step.
   - The `advertisementType` field is set to `Service` and `service.addresses` is set to `LoadBalancerIP` to only advertise the `LoadBalancerIP` for Services of type `LoadBalancer`.
   - The `selector` field is configured to match against the name of the Service you will create in a subsequent step. With this configuration, only `LoadBalancerIP` for Services with the name `tcp-sample-service` will be advertised.

   ```
   apiVersion: cilium.io/v2alpha1
   kind: CiliumBGPAdvertisement
   metadata:
     name: bgp-advertisement-tcp-service
     labels:
       advertise: bgp
   spec:
     advertisements:
       - advertisementType: "Service"
         service:
           addresses:
             - LoadBalancerIP
         selector:
           matchLabels:
             io.kubernetes.service.name: tcp-sample-service
   ```

5. Apply the `CiliumBGPAdvertisement` resource to your cluster. If you are not using Cilium BGP, you can skip this step.

```
kubectl apply -f cilium-bgp-advertisement-loadbalancer.yaml
```

6. Define a sample application in a file named `tcp-sample-app.yaml`. The example below uses a simple NGINX deployment with a TCP port.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tcp-sample-app
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: public.ecr.aws/nginx/nginx:1.23
          ports:
            - name: tcp
              containerPort: 80
```

7. Apply the deployment to your cluster.

```
kubectl apply -f tcp-sample-app.yaml
```

8. Define a Service of type LoadBalancer for the deployment in a file named `tcp-sample-service.yaml`.
   - You can request a specific IP address from the load balancer IP pool with the `lbipam.cilium.io/ips` annotation on the Service object. You can remove this annotation if you do not want to request a specific IP address for the Service.
   - The `loadBalancerClass` spec field is required to prevent the legacy AWS Cloud Provider from creating a Classic Load Balancer for the Service. In the example below this is configured to `io.cilium/bgp-control-plane` to use Cilium’s BGP Control Plane as the load balancer class. This field can alternatively be configured to `io.cilium/l2-announcer` to use Cilium’s [L2 Announcements feature](https://docs.cilium.io/en/latest/network/l2-announcements/ "https://docs.cilium.io/en/latest/network/l2-announcements/") (currently in beta and not officially supported by AWS).

   ```
   apiVersion: v1
   kind: Service
   metadata:
     name: tcp-sample-service
     namespace: default
     annotations:
       lbipam.cilium.io/ips: `"LB_IP_ADDRESS"`
   spec:
     loadBalancerClass: io.cilium/bgp-control-plane
     ports:
       - port: 80
         targetPort: 80
         protocol: TCP
     type: LoadBalancer
     selector:
       app: nginx
   ```

9. Apply the Service to your cluster. The Service will be created with an external IP address that you can use to access the application.

```
kubectl apply -f tcp-sample-service.yaml
```

10. Verify the Service was created successfully and has an IP assigned to it from the `CiliumLoadBalancerIPPool` created in the previous step.

```
kubectl get svc tcp-sample-service
```

```
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
tcp-sample-service   LoadBalancer   172.16.117.76   `LB_IP_ADDRESS`   80:31129/TCP   14m
```

11. If you are using Cilium in kube-proxy replacement mode, you can confirm Cilium is handling the load balancing for the Service by running the following command. In the output below, the `10.86.2.x` addresses are the pod IP addresses of the backend pods for the Service.

```
kubectl -n kube-system exec ds/cilium -- cilium-dbg service list
```

```
ID   Frontend               Service Type   Backend
...
41   `LB_IP_ADDRESS`:80/TCP   LoadBalancer   1 => 10.86.2.76:80/TCP (active)
                                           2 => 10.86.2.130:80/TCP (active)
                                           3 => 10.86.2.141:80/TCP (active)
```

12. Confirm Cilium is advertising the IP address to the on-premises network via BGP. In the example below, there are five hybrid nodes, each advertising the `LB_IP_ADDRESS` for the `tcp-sample-service` Service to the on-premises network.

```
Node                   VRouter      Prefix             NextHop   Age     Attrs
mi-026d6a261e355fba7   `NODES_ASN`
                  `LB_IP_ADDRESS`/32   0.0.0.0   12m3s   [{Origin: i} {Nexthop: 0.0.0.0}]
mi-082f73826a163626e   `NODES_ASN`
                  `LB_IP_ADDRESS`/32   0.0.0.0   12m3s   [{Origin: i} {Nexthop: 0.0.0.0}]
mi-09183e8a3d755abf6   `NODES_ASN`
                  `LB_IP_ADDRESS`/32   0.0.0.0   12m3s   [{Origin: i} {Nexthop: 0.0.0.0}]
mi-0d78d815980ed202d   `NODES_ASN`
                  `LB_IP_ADDRESS`/32   0.0.0.0   12m3s   [{Origin: i} {Nexthop: 0.0.0.0}]
mi-0daa253999fe92daa   `NODES_ASN`
                  `LB_IP_ADDRESS`/32   0.0.0.0   12m3s   [{Origin: i} {Nexthop: 0.0.0.0}]
```

13. Access the Service using the assigned load balancerIP address.

```
curl `LB_IP_ADDRESS`

```

An example output is below.

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
[...]
```

14. Clean up the resources you created.

```
kubectl delete -f tcp-sample-service.yaml
kubectl delete -f tcp-sample-app.yaml
kubectl delete -f cilium-lb-ip-pool.yaml
kubectl delete -f cilium-bgp-advertisement.yaml
```
