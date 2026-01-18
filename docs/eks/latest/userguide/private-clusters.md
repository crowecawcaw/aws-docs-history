**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy private clusters with limited internet access

This topic describes how to deploy an Amazon EKS cluster that is deployed on the AWS Cloud, but doesn’t have outbound internet access. If you have a local cluster on AWS Outposts, see [Create Amazon Linux nodes on AWS Outposts](eks-outposts-self-managed-nodes.md "eks-outposts-self-managed-nodes.md"), instead of this topic.

If you’re not familiar with Amazon EKS networking, see [De-mystifying cluster networking for Amazon EKS worker nodes](https://aws.amazon.com/blogs/containers/de-mystifying-cluster-networking-for-amazon-eks-worker-nodes "https://aws.amazon.com/blogs/containers/de-mystifying-cluster-networking-for-amazon-eks-worker-nodes"). If your cluster doesn’t have outbound internet access, then it must meet the following requirements:

## Cluster architecture requirements

- Your cluster must pull images from a container registry that’s in your VPC. You can create an Amazon Elastic Container Registry in your VPC and copy container images to it for your nodes to pull from. For more information, see [Copy a container image from one repository to another repository](copy-image-to-repository.md "copy-image-to-repository.md").
- Your cluster must have endpoint private access enabled. This is required for nodes to register with the cluster endpoint. Endpoint public access is optional. For more information, see [Cluster API server endpoint](cluster-endpoint.md "cluster-endpoint.md").

## Node requirements

- Self-managed Linux and Windows nodes must include the following bootstrap arguments before they’re launched. These arguments bypass Amazon EKS introspection and don’t require access to the Amazon EKS API from within the VPC.
  1.  Determine the value of your cluster’s endpoint with the following command. Replace `my-cluster` with the name of your cluster.

  ```
   aws eks describe-cluster --name my-cluster --query cluster.endpoint --output text
  ```

  An example output is as follows.

  ```
   https://EXAMPLE108C897D9B2F1B21D5EXAMPLE.sk1.region-code.eks.amazonaws.com
  ```

  2.  Determine the value of your cluster’s certificate authority with the following command. Replace `my-cluster` with the name of your cluster.

  ```
   aws eks describe-cluster --name my-cluster --query cluster.certificateAuthority --output text
  ```

  The returned output is a long string. 3. Replace the values of `apiServerEndpoint` and `certificateAuthority` in the NodeConfig object with the values returned in the output from the previous commands. For more information about specifying bootstrap arguments when launching self-managed Amazon Linux 2023 nodes, see [Create self-managed Amazon Linux nodes](launch-workers.md "launch-workers.md") and [Create self-managed Microsoft Windows nodes](launch-windows-workers.md "launch-windows-workers.md").

      + For Linux nodes:



      ```
       ---
      MIME-Version: 1.0
      Content-Type: multipart/mixed; boundary="BOUNDARY"

      --BOUNDARY
      Content-Type: application/node.eks.aws

      ---
      apiVersion: node.eks.aws/v1alpha1
      kind: NodeConfig
      spec:
        cluster:
          name: my-cluster
          apiServerEndpoint: [.replaceable]https://EXAMPLE108C897D9B2F1B21D5EXAMPLE.sk1.region-code.eks.amazonaws.com
          certificateAuthority: [.replaceable]Y2VydGlmaWNhdGVBdXRob3JpdHk=
          ...
      ```

      For additional arguments, see the [bootstrap script](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2/runtime/bootstrap.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2/runtime/bootstrap.sh") on GitHub.
      + For Windows nodes:


      ###### Note

      If you’re using custom service CIDR, then you need to specify it using the `-ServiceCIDR` parameter. Otherwise, the DNS resolution for Pods in the cluster will fail.



      ```
       -APIServerEndpoint cluster-endpoint -Base64ClusterCA certificate-authority
      ```

      For additional arguments, see [Bootstrap script configuration parameters](eks-optimized-windows-ami.md#bootstrap-script-configuration-parameters "eks-optimized-windows-ami.md#bootstrap-script-configuration-parameters").

- Your cluster’s `aws-auth`
  `ConfigMap` must be created from within your VPC. For more information about creating and adding entries to the `aws-auth`
  `ConfigMap`, enter `eksctl create iamidentitymapping --help` in your terminal. If the `ConfigMap` doesn’t exist on your server, `eksctl` will create it when you use the command to add an identity mapping.

## Pod requirements

- **Pod Identity** - Pods configured with EKS Pod Identity acquire credentials from the EKS Auth API. If there is no outbound internet access, you must create and use a VPC endpoint for the EKS Auth API: `com.amazonaws.region-code.eks-auth`. For more information about the EKS and EKS Auth VPC endpoints, see [Access Amazon EKS using AWS PrivateLink](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
- **IRSA** - Pods configured with [IAM roles for service accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md") acquire credentials from an AWS Security Token Service (AWS STS) API call. If there is no outbound internet access, you must create and use an AWS STS VPC endpoint in your VPC. Most AWS
  `v1` SDKs use the global AWS STS endpoint by default (`sts.amazonaws.com`), which doesn’t use the AWS STS VPC endpoint. To use the AWS STS VPC endpoint, you might need to configure your SDK to use the regional AWS STS endpoint (`sts.`region-code`.amazonaws.com`). For more information, see [Configure the AWS Security Token Service endpoint for a service account](configure-sts-endpoint.md "configure-sts-endpoint.md").
- Your cluster’s VPC subnets must have a VPC interface endpoint for any AWS services that your Pods need access to. For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md"). Some commonly-used services and endpoints are listed in the following table. For a complete list of endpoints, see [AWS services that integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md") in the [AWS PrivateLink Guide](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md").

We recommend that you [enable private DNS names](../../../vpc/latest/privatelink/interface-endpoints.md#enable-private-dns-names "../../../vpc/latest/privatelink/interface-endpoints.md#enable-private-dns-names") for your VPC endpoints, that way workloads can continue using public AWS service endpoints without issues.

| Service                                                                                          | Endpoint                                                                                                     |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Amazon EC2                                                                                       | com.amazonaws.`region-code`.ec2                                                                              |
| Amazon Elastic Container Registry (for pulling container images)                                 | com.amazonaws.`region-code`.ecr.api, com.amazonaws.`region-code`.ecr.dkr, and com.amazonaws.`region-code`.s3 |
| Amazon Application Load Balancers and Network Load Balancers                                     | com.amazonaws.`region-code`.elasticloadbalancing                                                             |
| (Optional) AWS X-Ray (required for tracing sent to AWS X-Ray)                                    | com.amazonaws.`region-code`.xray                                                                             |
| (Optional) Amazon SSM (required for the SSM Agent for node management tasks. Alternative to SSH) | com.amazonaws.`region-code`.ssm                                                                              |
| Amazon CloudWatch Logs (required for node and pod logs sent to Amazon CloudWatch Logs)           | com.amazonaws.`region-code`.logs                                                                             |
| AWS Security Token Service (required when using IAM roles for service accounts)                  | com.amazonaws.`region-code`.sts                                                                              |
| Amazon EKS Auth (required when using Pod Identity associations)                                  | com.amazonaws.`region-code`.eks-auth                                                                         |
| Amazon EKS                                                                                       | com.amazonaws.`region-code`.eks                                                                              |

- Any self-managed nodes must be deployed to subnets that have the VPC interface endpoints that you require. If you create a managed node group, the VPC interface endpoint security group must allow the CIDR for the subnets, or you must add the created node security group to the VPC interface endpoint security group.
- **EFS storage** - If your Pods use Amazon EFS volumes, then before deploying the [Store an elastic file system with Amazon EFS](efs-csi.md "efs-csi.md"), the driver’s [kustomization.yaml](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/deploy/kubernetes/overlays/stable/kustomization.yaml "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/deploy/kubernetes/overlays/stable/kustomization.yaml") file must be changed to set the container images to use the same AWS Region as the Amazon EKS cluster.
- Route53 does not support AWS PrivateLink. You cannot manage Route53 DNS records from a private Amazon EKS cluster. This impacts Kubernetes [external-dns](https://github.com/kubernetes-sigs/external-dns "https://github.com/kubernetes-sigs/external-dns").
- If you use the EKS Optimized AMI, you should enable the `ec2` endpoint in the table above. Alternatively, you can manually set the Node DNS name. The optimized AMI uses EC2 APIs to set the node DNS name automatically.
- You can use the [AWS Load Balancer Controller](aws-load-balancer-controller.md "aws-load-balancer-controller.md") to deploy AWS Application Load Balancers (ALB) and Network Load Balancers to your private cluster. When deploying it, you should use [command line flags](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/deploy/configurations/#controller-command-line-flags "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/deploy/configurations/#controller-command-line-flags") to set `enable-shield`, `enable-waf`, and `enable-wafv2` to false. [Certificate discovery](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/cert_discovery/#discover-via-ingress-rule-host "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/cert_discovery/#discover-via-ingress-rule-host") with hostnames from Ingress objects isn’t supported. This is because the controller needs to reach AWS Certificate Manager, which doesn’t have a VPC interface endpoint.

The controller supports network load balancers with IP targets, which are required for use with Fargate. For more information, see [Route application and HTTP traffic with Application Load Balancers](alb-ingress.md "alb-ingress.md") and [Create a network load balancer](network-load-balancing.md#network-load-balancer "network-load-balancing.md#network-load-balancer").

- [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md "https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md") is supported. When deploying Cluster Autoscaler Pods, make sure that the command line includes `--aws-use-static-instance-list=true`. For more information, see [Use Static Instance List](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md#use-static-instance-list "https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md#use-static-instance-list") on GitHub. The worker node VPC must also include the AWS STS VPC endpoint and autoscaling VPC endpoint.
- Some container software products use API calls that access the AWS Marketplace Metering Service to monitor usage. Private clusters do not allow these calls, so you can’t use these container types in private clusters.
