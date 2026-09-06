

# Managed endpoints
<a name="managed-endpoints"></a>

Managed endpoints is an optional feature for responder gateways that allows RTB Fabric to distribute load directly across bidder hosts in your fleet. This feature bypasses the need for a separate load balancer by using RTB Fabric to send traffic directly to your responder application hosts.

Managed endpoints supports two infrastructure types for hosting your responder applications:
+ **Amazon Elastic Kubernetes Service (Amazon EKS) clusters** – RTB Fabric integrates with your EKS cluster to send traffic to your bidder application pods
+ **Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling groups** – RTB Fabric uses information from your Auto Scaling groups to determine the set of IP addresses to send traffic to

If you are interested in using managed endpoints for your responder gateway, please contact your AWS solution architect (SA).

## IAM role requirements
<a name="managed-endpoints-iam-requirements"></a>

To use managed endpoints, you must provide an IAM role that RTB Fabric can assume to interact with your infrastructure. RTB Fabric uses a service-linked role for most operations, but requires this additional role specifically for managed endpoint functionality.

**Important**  
When creating the IAM role, ensure that you add the required tag:  
**Tag key:** `RTBFabricManagedEndpoint`
**Tag value:** `true`

For Auto Scaling group managed endpoints, the IAM role must include the following permissions:
+ `autoscaling:DescribeAutoScalingGroups`
+ `ec2:DescribeInstanceStatus`
+ `ec2:DescribeInstances`
+ `ec2:DescribeAvailabilityZones`
+ `ec2:DescribeSubnets`

The role must also include a trust relationship that allows RTB Fabric to assume it:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "rtbfabric.amazonaws.com",
          "rtbfabric-endpoints.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Configuration requirements
<a name="managed-endpoints-configuration"></a>

The configuration requirements vary depending on your infrastructure type.

### Auto Scaling groups configuration
<a name="managed-endpoints-autoscaling-config"></a>

For Auto Scaling group managed endpoints, you must provide the following configuration:
+ **autoScalingGroupNames** – The names of the Auto Scaling groups where the instances responding to RTB bid requests belong to.
+ **roleArn** – The ARN of an IAM role allowing RTB Fabric to query the Auto Scaling groups in `autoScalingGroupNames` for the instances to send traffic to.

The IAM role must allow the services `rtbfabric.amazonaws.com` and `rtbfabric-endpoints.amazonaws.com` in its trust policy:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "rtbfabric.amazonaws.com",
          "rtbfabric-endpoints.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

The role must also allow the following permissions in its permissions policies:

```
{
   "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AsgEndpointsIpDiscovery",
            "Effect": "Allow",
            "Action": [
                "autoscaling:DescribeAutoScalingGroups",
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInstances",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeSubnets"
            ],
            "Resource": "*"
        }
    ]
}
```

**Tip**  
 For RTB Fabric to appropriately route traffic to healthy hosts, the provided ASG must **only** have hosts listed as IN\_USE if they are available to take traffic. Ensure that hosts which are unhealthy, inactive, or running other services are not set as IN\_USE in the provided ASG. You can enable application-level health checks to automatically route traffic only to healthy instances in your Auto Scaling groups. For more information, see [Health checks for Managed Endpoints](health-checks-for-managed-endpoints.md). 

### EKS endpoints configuration
<a name="managed-endpoints-eks-config"></a>

For EKS managed endpoints, you must provide the following configuration:
+ **roleArn** – The ARN of an IAM role allowing RTB Fabric to query the target IPs of EKS cluster to send traffic to.

The IAM role must allow the services `rtbfabric.amazonaws.com` and `rtbfabric-endpoints.amazonaws.com` in its trust policy:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "rtbfabric.amazonaws.com",
          "rtbfabric-endpoints.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

The role does not need to have any IAM policies attached to it, but must be associated with your EKS cluster's RBAC to authorize RTB Fabric to discover IP targets in the cluster. First, create the Kubernetes Role and RoleBinding:

```
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: rtbfabric-endpoints-role
  namespace: default
rules:
  - apiGroups: [""]
    resources: ["endpoints"]
    resourceNames: ["nginx-deployment"]
    verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: rtbfabric-endpoints-rolebinding
  namespace: default
subjects:
  - kind: User
    name: rtbfabric-integration
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: rtbfabric-endpoints-role
  apiGroup: rbac.authorization.k8s.io
```

Then, map the IAM role to the Kubernetes user using one of the following methods:

**Option 1: EKS access entries (recommended)**

For EKS clusters running Kubernetes 1.23 or later, use the EKS access entry API to map the IAM role. This is the recommended approach and is the default authentication mode for new EKS clusters.

```
$ aws eks create-access-entry \
--cluster-name {{my-cluster}} \
--principal-arn arn:aws:iam::{{242201309515}}:role/{{RtbFabricRoleForEksEndpointsManagedEndpoint}} \
--kubernetes-user rtbfabric-integration
```

**Option 2: aws-auth ConfigMap (legacy)**

**Note**  
The `aws-auth` ConfigMap method is deprecated for EKS clusters that use the EKS API authentication mode (which is the default for new clusters). If your cluster uses the `CONFIG_MAP` or `API_AND_CONFIG_MAP` authentication mode, you can still use this method. For more information, see [EKS access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon EKS User Guide*.

```
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles: |
    - rolearn: arn:aws:iam::{{242201309515}}:role/{{RtbFabricRoleForEksEndpointsManagedEndpoint}}
      username: rtbfabric-integration
```

## HTTPS considerations
<a name="managed-endpoints-https"></a>

**Note**  
The domain name must be allowlisted by the RTB Fabric team for your account before you can create your responder gateway. Contact customer support for allowlisting process.

RTB Fabric can terminate the TLS connection from the requester on your behalf and send your hosts HTTP traffic. However, if you require HTTPS from RTB Fabric managed endpoints to your bidder hosts, additional configuration is required:
+ **TLS certificates** – Each host must serve up a TLS certificate.
+ **Certificate Authority chain** – You must provide RTB Fabric with the Certificate Authority (CA) certificate chain so that RTB Fabric hosts can trust the TLS certificate from each bidder host.
+ **Domain name allowlisting** – You must provide RTB Fabric with a domain name that matches the SAN of the TLS certificate from each bidder host.