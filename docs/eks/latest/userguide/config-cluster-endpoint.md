**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure network access to cluster API server endpoint

You can modify your cluster API server endpoint access using the AWS Management Console or AWS CLI in the following sections.

## Configure endpoint access - AWS console

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose the name of the cluster to display your cluster information.
3. Choose the **Networking** tab and choose **Manage endpoint access**.
4. For **Private access**, choose whether to enable or disable private access for your cluster’s Kubernetes API server endpoint. If you enable private access, Kubernetes API requests that originate from within your cluster’s VPC use the private VPC endpoint. You must enable private access to disable public access.
5. For **Public access**, choose whether to enable or disable public access for your cluster’s Kubernetes API server endpoint. If you disable public access, your cluster’s Kubernetes API server can only receive requests from within the cluster VPC.
6. (Optional) If you’ve enabled **Public access**, you can specify which addresses from the internet can communicate to the public endpoint. Select **Advanced Settings**. Enter a CIDR block, such as `203.0.113.5/32`. The block cannot include [reserved addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses "https://en.wikipedia.org/wiki/Reserved_IP_addresses"). You can enter additional blocks by selecting **Add Source**. There is a maximum number of CIDR blocks that you can specify. For more information, see [View and manage Amazon EKS and Fargate service quotas](service-quotas.md "service-quotas.md"). If you specify no blocks, then the public API server endpoint receives requests from all IP addresses for both `IPv4` (`0.0.0.0/0`) and additionally `IPv6` (`::/0`) for dual-stack `IPv6` cluster. If you restrict access to your public endpoint using CIDR blocks, we recommend that you also enable private endpoint access so that nodes and Fargate Pods (if you use them) can communicate with the cluster. Without the private endpoint enabled, your public access endpoint CIDR sources must include the egress sources from your VPC. For example, if you have a node in a private subnet that communicates to the internet through a NAT Gateway, you will need to add the outbound IP address of the NAT gateway as part of an allowed CIDR block on your public endpoint.
7. Choose **Update** to finish.

## Configure endpoint access - AWS CLI

Complete the following steps using the AWS CLI version `1.27.160` or later. You can check your current version with `aws --version`. To install or upgrade the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md").

1. Update your cluster API server endpoint access with the following AWS CLI command. Substitute your cluster name and desired endpoint access values. If you set `endpointPublicAccess=true`, then you can (optionally) enter single CIDR block, or a comma-separated list of CIDR blocks for `publicAccessCidrs`. The blocks cannot include [reserved addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses "https://en.wikipedia.org/wiki/Reserved_IP_addresses"). If you specify CIDR blocks, then the public API server endpoint will only receive requests from the listed blocks. There is a maximum number of CIDR blocks that you can specify. For more information, see [View and manage Amazon EKS and Fargate service quotas](service-quotas.md "service-quotas.md"). If you restrict access to your public endpoint using CIDR blocks, it is recommended that you also enable private endpoint access so that nodes and Fargate Pods (if you use them) can communicate with the cluster. Without the private endpoint enabled, your public access endpoint CIDR sources must include the egress sources from your VPC. For example, if you have a node in a private subnet that communicates to the internet through a NAT Gateway, you will need to add the outbound IP address of the NAT gateway as part of an allowed CIDR block on your public endpoint. If you specify no CIDR blocks, then the public API server endpoint receives requests from all (0.0.0.0/0) IP addresses and additionally `IPv6` (`::/0`) for dual-stack `IPv6` cluster.

###### Note

The following command enables private access and public access from a single IP address for the API server endpoint. Replace `203.0.113.5/32` with a single CIDR block, or a comma-separated list of CIDR blocks that you want to restrict network access to.

```
 aws eks update-cluster-config \
    --region region-code \
    --name my-cluster \
    --resources-vpc-config endpointPublicAccess=true,publicAccessCidrs="203.0.113.5/32",endpointPrivateAccess=true
```

An example output is as follows.

```
 {
    "update": {
        "id": "e6f0905f-a5d4-4a2a-8c49-EXAMPLE00000",
        "status": "InProgress",
        "type": "EndpointAccessUpdate",
        "params": [
            {
                "type": "EndpointPublicAccess",
                "value": "true"
            },
            {
                "type": "EndpointPrivateAccess",
                "value": "true"
            },
            {
                "type": "publicAccessCidrs",
                "value": "[\"203.0.113.5/32\"]"
            }
        ],
        "createdAt": 1576874258.137,
        "errors": []
    }
}
```

2. Monitor the status of your endpoint access update with the following command, using the cluster name and update ID that was returned by the previous command. Your update is complete when the status is shown as `Successful`.

```
 aws eks describe-update \
    --region region-code \
    --name my-cluster \
    --update-id e6f0905f-a5d4-4a2a-8c49-EXAMPLE00000
```

An example output is as follows.

```
 {
    "update": {
        "id": "e6f0905f-a5d4-4a2a-8c49-EXAMPLE00000",
        "status": "Successful",
        "type": "EndpointAccessUpdate",
        "params": [
            {
                "type": "EndpointPublicAccess",
                "value": "true"
            },
            {
                "type": "EndpointPrivateAccess",
                "value": "true"
            },
            {
                "type": "publicAccessCidrs",
                "value": "[\"203.0.113.5/32\"]"
            }
        ],
        "createdAt": 1576874258.137,
        "errors": []
    }
}
```

📝 [Edit this page on GitHub](https://github.com/search?q=repo%3Aawsdocs%2Famazon-eks-user-guide+%5B%23config-cluster-endpoint%5D&type=code "https://github.com/search?q=repo%3Aawsdocs%2Famazon-eks-user-guide+%5B%23config-cluster-endpoint%5D&type=code")
