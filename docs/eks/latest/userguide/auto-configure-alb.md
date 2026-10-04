

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an IngressClass to configure an Application Load Balancer
<a name="auto-configure-alb"></a>

EKS Auto Mode automates routine tasks for load balancing, including exposing cluster apps to the internet.

 AWS suggests using Application Load Balancers (ALB) to serve HTTP and HTTPS traffic. Application Load Balancers can route requests based on the content of the request. For more information on Application Load Balancers, see [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) 

EKS Auto Mode creates and configures Application Load Balancers (ALBs). For example, EKS Auto Mode creates a load balancer when you create an `Ingress` Kubernetes object and configures it to route traffic to your cluster workload.

 **Overview** 

1. Create a workload that you want to expose to the internet.

1. Create an `IngressClassParams` resource, specifying AWS specific configuration values such as the certificate to use for SSL/TLS and VPC Subnets.

1. Create an `IngressClass` resource, specifying that EKS Auto Mode will be the controller for the resource.

1. Create an `Ingress` resource that associates an HTTP path and port with a cluster workload.

EKS Auto Mode will create an Application Load Balancer that points to the workload specified in the `Ingress` resource, using the load balancer configuration specified in the `IngressClassParams` resource.

## Prerequisites
<a name="_prerequisites"></a>
+ EKS Auto Mode Enabled on an Amazon EKS Cluster
+ Kubectl configured to connect to your cluster
  + You can use `kubectl apply -f <filename>` to apply the sample configuration YAML files below to your cluster.

**Note**  
EKS Auto Mode requires subnet tags to identify public and private subnets.  
If you created your cluster with `eksctl`, you already have these tags.  
Learn how to [Tag subnets for EKS Auto Mode](tag-subnets-auto.md).

## Step 1: Create a workload
<a name="_step_1_create_a_workload"></a>

To begin, create a workload that you want to expose to the internet. This can be any Kubernetes resource that serves HTTP traffic, such as a Deployment or a Service.

This example uses a simple HTTP service called `service-2048` that listens on port `80`. Create this service and its deployment by applying the following manifest, `2048-deployment-service.yaml`:

```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-2048
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: app-2048
  replicas: 2
  template:
    metadata:
      labels:
        app.kubernetes.io/name: app-2048
    spec:
      containers:
        - image: public.ecr.aws/l6m2t8p7/docker-2048:latest
          imagePullPolicy: Always
          name: app-2048
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: service-2048
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: NodePort
  selector:
    app.kubernetes.io/name: app-2048
```

Apply the configuration to your cluster:

```
kubectl apply -f 2048-deployment-service.yaml
```

The resources listed above will be created in the default namespace. You can verify this by running the following command:

```
kubectl get all -n default
```

## Step 2: Create IngressClassParams
<a name="_step_2_create_ingressclassparams"></a>

Create an `IngressClassParams` object to specify AWS specific configuration options for the Application Load Balancer. In this example, we create an `IngressClassParams` resource named `alb` (which you will use in the next step) that specifies the load balancer scheme as `internet-facing` in a file called `alb-ingressclassparams.yaml`.

```
apiVersion: eks.amazonaws.com/v1
kind: IngressClassParams
metadata:
  name: alb
spec:
  scheme: internet-facing
```

Apply the configuration to your cluster:

```
kubectl apply -f alb-ingressclassparams.yaml
```

## Step 3: Create IngressClass
<a name="_step_3_create_ingressclass"></a>

Create an `IngressClass` that references the AWS specific configuration values set in the `IngressClassParams` resource in a file named `alb-ingressclass.yaml`. Note the name of the `IngressClass`. In this example, both the `IngressClass` and `IngressClassParams` are named `alb`.

Use the `is-default-class` annotation to control if `Ingress` resources should use this class by default.

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: alb
  annotations:
    # Use this annotation to set an IngressClass as Default
    # If an Ingress doesn't specify a class, it will use the Default
    ingressclass.kubernetes.io/is-default-class: "true"
spec:
  # Configures the IngressClass to use EKS Auto Mode
  controller: eks.amazonaws.com/alb
  parameters:
    apiGroup: eks.amazonaws.com
    kind: IngressClassParams
    # Use the name of the IngressClassParams set in the previous step
    name: alb
```

For more information on configuration options, see [IngressClassParams Reference](#ingress-reference).

Apply the configuration to your cluster:

```
kubectl apply -f alb-ingressclass.yaml
```

## Step 4: Create Ingress
<a name="_step_4_create_ingress"></a>

Create an `Ingress` resource in a file named `alb-ingress.yaml`. The purpose of this resource is to associate paths and ports on the Application Load Balancer with workloads in your cluster. For this example, we create an `Ingress` resource named `2048-ingress` that routes traffic to a service named `service-2048` on port 80.

For more information about configuring this resource, see [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) in the Kubernetes Documentation.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: 2048-ingress
spec:
  # this matches the name of IngressClass.
  # this can be omitted if you have a default ingressClass in cluster: the one with ingressclass.kubernetes.io/is-default-class: "true"  annotation
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /*
            pathType: ImplementationSpecific
            backend:
              service:
                name: service-2048
                port:
                  number: 80
```

Apply the configuration to your cluster:

```
kubectl apply -f alb-ingress.yaml
```

## Step 5: Check Status
<a name="_step_5_check_status"></a>

Use `kubectl` to find the status of the `Ingress`. It can take a few minutes for the load balancer to become available.

Use the name of the `Ingress` resource you set in the previous step. For example:

```
kubectl get ingress 2048-ingress
```

Once the resource is ready, retrieve the domain name of the load balancer.

```
kubectl get ingress 2048-ingress -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

To view the service in a web browser, review the port and path specified in the `Ingress` resource.

## Step 6: Cleanup
<a name="_step_6_cleanup"></a>

To clean up the load balancer, use the following command:

```
kubectl delete ingress 2048-ingress
kubectl delete ingressclass alb
kubectl delete ingressclassparams alb
```

EKS Auto Mode will automatically delete the associated load balancer in your AWS account.

## IngressClassParams Reference
<a name="ingress-reference"></a>

The following table lists the fields that you can set in an `IngressClassParams` resource. The settings apply to all Ingresses that use the IngressClass.


| Field | Description | Example value | 
| --- | --- | --- | 
|  `scheme`  | Defines whether the ALB is internal or internet-facing |  `internet-facing`  | 
|  `loadBalancerName`  | Sets the name of the ALB. The name can be up to 32 characters. Overrides the `alb.ingress.kubernetes.io/load-balancer-name` annotation. |  `my-alb`  | 
|  `namespaceSelector`  | Restricts which namespaces can use this IngressClass |  `environment: prod`  | 
|  `group.name`  | Groups multiple Ingresses to share a single ALB |  `retail-apps`  | 
|  `ipAddressType`  | Sets the IP address type for the ALB. Valid values are `ipv4`, `dualstack`, and `dualstack-without-public-ipv4`. |  `dualstack`  | 
|  `subnets.ids`  | List of subnet IDs for ALB deployment |  `subnet-xxxx, subnet-yyyy`  | 
|  `subnets.matchTags`  | Tag filters to select subnets for ALB. Each filter has a `key` and a list of `values`. |  `key: Environment, values: [prod]`  | 
|  `certificateARNs`  | ARNs of SSL certificates to use |  ` arn:aws:acm:region:account:certificate/id`  | 
|  `sslPolicy`  | Sets the security policy for HTTPS listeners. Overrides the `alb.ingress.kubernetes.io/ssl-policy` annotation. |  `ELBSecurityPolicy-TLS13-1-2-2021-06`  | 
|  `inboundCIDRs`  | CIDR blocks that are allowed to access the ALB. Overrides the `alb.ingress.kubernetes.io/inbound-cidrs` annotation. |  `10.0.0.0/16, 192.168.0.0/24`  | 
|  `prefixListsIDs`  | IDs of managed prefix lists that are allowed to access the ALB. Overrides the `alb.ingress.kubernetes.io/security-group-prefix-lists` annotation. |  `pl-00000000, pl-11111111`  | 
|  `targetType`  | Sets the target type for target groups. Valid values are `instance` and `ip`. The default is `ip`. |  `instance`  | 
|  `tags`  | Custom tags for AWS resources |  `Environment: prod, Team: platform`  | 
|  `loadBalancerAttributes`  | Load balancer specific attributes |  `idle_timeout.timeout_seconds: 60`  | 
|  `listeners`  | Sets [listener attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ListenerAttribute.html) on listeners that your Ingresses define. Each entry matches a listener by `port` and `protocol` (`HTTP` or `HTTPS`) and lists `attributes` as `key` and `value` pairs. This field doesn’t create listeners. Overrides the `alb.ingress.kubernetes.io/listener-attributes.${Protocol}-${Port}` annotation for the same attribute key. |  `port: 443, protocol: HTTPS, attributes: routing.http.response.server.enabled: "false"`  | 
|  `minimumLoadBalancerCapacity.capacityUnits`  | Reserves a minimum capacity for the ALB, in load balancer capacity units (LCUs). Set to `0` to remove the reservation. Overrides the `alb.ingress.kubernetes.io/minimum-load-balancer-capacity` annotation. |  `1000`  | 
|  `ipamConfiguration.ipv4IPAMPoolId`  | ID of the Amazon VPC IP Address Manager (IPAM) pool that an internet-facing ALB uses for its public IPv4 addresses. Overrides the `alb.ingress.kubernetes.io/ipam-ipv4-pool-id` annotation. |  `ipam-pool-0123456789abcdef0`  | 

## Considerations
<a name="_considerations"></a>
+ You cannot use Annotations on an IngressClass to configure load balancers with EKS Auto Mode. IngressClass configuration should be done through IngressClassParams. However, you can use annotations on individual Ingress resources to configure load balancer behavior (such as `alb.ingress.kubernetes.io/security-group-prefix-lists` or `alb.ingress.kubernetes.io/conditions.*`).
+ To set [ListenerAttribute](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ListenerAttribute.html) values for all Ingresses in an IngressClass, use the `listeners` field in IngressClassParams. For more information, see [IngressClassParams Reference](#ingress-reference).
+ You must update the Cluster IAM Role to enable tag propagation from Kubernetes to AWS Load Balancer resources. For more information, see [Custom AWS tags for EKS Auto resources](auto-cluster-iam-role.md#tag-prop).
+ For information about associating resources with either EKS Auto Mode or the self-managed AWS Load Balancer Controller, see [Migration reference](migrate-auto.md#migration-reference).
+ For information about fixing issues with load balancers, see [Troubleshoot EKS Auto Mode](auto-troubleshoot.md).
+ For more considerations about using the load balancing capability of EKS Auto Mode, see [Load balancing](auto-networking.md#auto-lb-consider).

The following tables provide a detailed comparison of changes in IngressClassParams, Ingress annotations, and TargetGroupBinding configurations for EKS Auto Mode. These tables highlight the key differences between the load balancing capability of EKS Auto Mode and the open source load balancer controller, including API version changes, deprecated features, and updated parameter names.

### IngressClassParams
<a name="_ingressclassparams"></a>


| Previous | New | Description | 
| --- | --- | --- | 
|  `elbv2.k8s.aws/v1beta1`  |  `eks.amazonaws.com/v1`  | API version change | 
|  `spec.certificateArn`  |  `spec.certificateARNs`  | Support for multiple certificate ARNs | 
|  `spec.subnets.tags`  |  `spec.subnets.matchTags`  | Changed subnet matching schema | 
|  `spec.listeners.listenerAttributes`  |  `spec.listeners.attributes`  | Renamed field for listener attributes | 
|  `spec.PrefixListsIDs`  |  `spec.prefixListsIDs`  | Only the `prefixListsIDs` spelling is supported | 
|  `spec.sslRedirectPort`  | Not supported | Use the `alb.ingress.kubernetes.io/ssl-redirect` annotation on Ingress objects | 
|  `spec.wafv2AclArn`  | Not supported | Use the `alb.ingress.kubernetes.io/wafv2-acl-arn` annotation on Ingress objects | 
|  `spec.wafv2AclName`  | Not supported | Use the `alb.ingress.kubernetes.io/wafv2-acl-name` annotation on Ingress objects | 

### Ingress annotations
<a name="_ingress_annotations"></a>


| Previous | New | Description | 
| --- | --- | --- | 
|  `kubernetes.io/ingress.class`  | Not supported | Use `spec.ingressClassName` on Ingress objects | 
|  `alb.ingress.kubernetes.io/group.name`  | Not supported | Specify groups in IngressClass only | 
|  `alb.ingress.kubernetes.io/waf-acl-id`  | Not supported | Use WAF v2 instead | 
|  `alb.ingress.kubernetes.io/web-acl-id`  | Not supported | Use WAF v2 instead | 
|  `alb.ingress.kubernetes.io/dry-run-plan`  | Not supported | Dry-run plan is currently not supported | 
|  `alb.ingress.kubernetes.io/create-acm-cert`  | Not supported | ACM certificate creation is currently not supported | 
|  `alb.ingress.kubernetes.io/acm-pca-arn`  | Not supported | ACM PCA ARN is currently not supported | 
|  `alb.ingress.kubernetes.io/auth-type: oidc`  | Supported with additional RBAC | Grant the load balancer controller `get` access to the OIDC `Secret`. For more information, see [Grant the EKS Auto Mode load balancer controller access to a specific Secret](auto-managed-rbac-example.md). | 

### TargetGroupBinding
<a name="_targetgroupbinding"></a>


| Previous | New | Description | 
| --- | --- | --- | 
|  `elbv2.k8s.aws/v1beta1`  |  `eks.amazonaws.com/v1`  | API version change | 
|  `spec.targetType` optional |  `spec.targetType` required | Explicit target type specification | 
|  `spec.networking.ingress.from`  | Not supported | No longer supports NLB without security groups | 

To use the custom TargetGroupBinding feature, you must tag the target group with the eks:eks-cluster-name tag with cluster name to grant the controller the necessary IAM permissions. Be aware that the controller will delete the target group when the TargetGroupBinding resource or the cluster is deleted.