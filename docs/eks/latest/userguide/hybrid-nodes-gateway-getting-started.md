**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Get started with EKS Hybrid Nodes gateway

This page walks you through the prerequisites, environment preparation, installation, verification, and removal of the Amazon EKS Hybrid Nodes gateway. For an introduction to the gateway and its architecture, see [Amazon EKS Hybrid Nodes gateway](hybrid-nodes-gateway-overview.md "hybrid-nodes-gateway-overview.md").

## Prerequisites

Before you install the Hybrid Nodes gateway, confirm that your environment meets the following requirements:

- **EKS cluster with Cilium CNI and VTEP support** — Your EKS cluster must use the EKS version of Cilium as the CNI on hybrid nodes, and Cilium VTEP must be enabled. For more information, see [Configure CNI for the Hybrid Nodes gateway](hybrid-nodes-gateway-cni.md "hybrid-nodes-gateway-cni.md").
- **AWS VPC CNI on cloud nodes** — The gateway nodes and other cloud nodes in the cluster must use the AWS VPC CNI. The gateway relies on VPC-native routing to forward traffic between the VPC and the VXLAN tunnel.
- **Hybrid connectivity** — A private connection between your VPC and on-premises environment is required. You can use AWS Direct Connect, AWS Site-to-Site VPN, or your own VPN solution. For more information, see [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md").
- **VXLAN traffic allowed** — The security groups attached to the gateway EC2 instances must allow inbound and outbound UDP traffic on port 8472. On the hybrid node side, the on-premises firewall rules must also permit UDP port 8472 traffic to and from the gateway node IP addresses.
- **IAM permissions for route table management** — The gateway requires the following EC2 actions to manage VPC route tables:

  - `ec2:DescribeRouteTables`
  - `ec2:CreateRoute`
  - `ec2:ReplaceRoute`
  - `ec2:DescribeInstances`

  You can grant these permissions using one of the following approaches:

  EKS Pod Identity (recommended)
  Use [EKS Pod Identity](pod-identities.md "pod-identities.md") to grant permissions only to the gateway pod’s service account.

        1. Install the EKS Pod Identity Agent add-on on your cluster if not already installed:



        ```
        aws eks create-addon \
          --cluster-name `CLUSTER_NAME` \
          --addon-name eks-pod-identity-agent
        ```
        2. Create an IAM role with the required EC2 permissions and a trust policy for EKS Pod Identity:



        ```
        cat > gateway-trust-policy.json << 'EOF'
        {
          "Version": "2012-10-17" ,
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": { "Service": "pods.eks.amazonaws.com" },
              "Action": ["sts:AssumeRole", "sts:TagSession"]
            }
          ]
        }
        EOF

        aws iam create-role \
          --role-name EKSHybridNodesGatewayRole \
          --assume-role-policy-document file://gateway-trust-policy.json

        aws iam put-role-policy \
          --role-name EKSHybridNodesGatewayRole \
          --policy-name HybridNodesGatewayRouteTable \
          --policy-document '{
            "Version": "2012-10-17" ,
            "Statement": [{
              "Effect": "Allow",
              "Action": [
                "ec2:DescribeRouteTables",
                "ec2:CreateRoute",
                "ec2:ReplaceRoute",
                "ec2:DescribeInstances"
              ],
              "Resource": "*"
            }]
          }'
        ```
        3. Create a pod identity association linking the IAM role to the gateway service account:



        ```
        aws eks create-pod-identity-association \
          --cluster-name `CLUSTER_NAME` \
          --namespace eks-hybrid-nodes-gateway \
          --service-account eks-hybrid-nodes-gateway \
          --role-arn `arn:aws:iam::ACCOUNT_ID:role/EKSHybridNodesGatewayRole`

        ```

  Node IAM role
  Attach an inline or managed policy with the required permissions to the IAM role associated with the gateway nodes' instance profile:

  ```
  aws iam put-role-policy \
    --role-name `NODE_ROLE_NAME` \
    --policy-name HybridNodesGatewayRouteTable \
    --policy-document '{
      "Version": "2012-10-17" ,
      "Statement": [{
        "Effect": "Allow",
        "Action": [
          "ec2:DescribeRouteTables",
          "ec2:CreateRoute",
          "ec2:ReplaceRoute",
          "ec2:DescribeInstances"
        ],
        "Resource": "*"
      }]
    }'
  ```

  All pods on the gateway nodes will have these permissions.

- **EKS Auto Mode (if using Auto Mode for gateway nodes)** — If you plan to use EKS Auto Mode to provision gateway nodes, Auto Mode must be enabled on your EKS cluster. For more information, see [Enable EKS Auto Mode](migrate-auto.md "migrate-auto.md").

## Prepare gateway nodes

The gateway requires at least two EC2 nodes for high availability. There are two supported node configuration options for the gateway:

- [EKS Auto Mode (recommended)](#hybrid-nodes-gateway-auto-mode-nodes "#hybrid-nodes-gateway-auto-mode-nodes") — Nodes are provisioned automatically using a `NodePool` and `NodeClass`. Source/destination check, labels, and taints are all configured declaratively.
- [Managed node groups](#hybrid-nodes-gateway-mng-nodes "#hybrid-nodes-gateway-mng-nodes") — You provision nodes using a managed node group or self-managed nodes. Labels can be configured through the managed node group API, and source/destination check can be disabled using a custom launch template with user data.

### EKS Auto Mode (recommended)

When using EKS Auto Mode, you must create a `NodePool` and `NodeClass` before installing the Helm chart. The NodePool provisions EC2 instances with the correct labels, taints, and source/destination check configuration. You do not need to manually provision or configure nodes.

Apply the following resources to your cluster, replacing the placeholder values:

- `YOUR_NODE_ROLE` — The name of the Node IAM Role used by EKS Auto Mode to provision nodes. This is the role you configured (or that EKS created) when you enabled Auto Mode on the cluster. For more information, see [Create a Node IAM Role for EKS Auto Mode](auto-create-node-role.md "auto-create-node-role.md").
- `YOUR_CLUSTER_NAME` — Your EKS cluster name.
- `SUBNET_ID_1`, `SUBNET_ID_2` — Subnet IDs in different Availability Zones where gateway nodes will be provisioned.

```
apiVersion: eks.amazonaws.com/v1
kind: NodeClass
metadata:
  name: hybrid-gateway
spec:
  advancedNetworking:
    sourceDestCheck: DisabledPrimaryENI
  role: `YOUR_NODE_ROLE`
  securityGroupSelectorTerms:
    - tags:
        aws:eks:cluster-name: `YOUR_CLUSTER_NAME`
  subnetSelectorTerms:
    - id: `SUBNET_ID_1`
    - id: `SUBNET_ID_2`
---
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: hybrid-gateway
spec:
  template:
    metadata:
      labels:
        hybrid-gateway-node: "true"
    spec:
      expireAfter: 336h
      nodeClassRef:
        group: eks.amazonaws.com
        kind: NodeClass
        name: hybrid-gateway
      requirements:
        - key: karpenter.sh/capacity-type
          operator: In
          values:
            - on-demand
        - key: eks.amazonaws.com/instance-category
          operator: In
          values:
            - c
            - m
            - r
        - key: eks.amazonaws.com/instance-generation
          operator: Gt
          values:
            - "4"
        - key: kubernetes.io/arch
          operator: In
          values:
            - amd64
        - key: kubernetes.io/os
          operator: In
          values:
            - linux
      taints:
        - key: hybrid-gateway-node
          effect: NoSchedule
      terminationGracePeriod: 24h0m0s
  disruption:
    budgets:
      - nodes: 10%
    consolidateAfter: 30s
    consolidationPolicy: WhenEmptyOrUnderutilized
```

Key fields in this configuration:

- `advancedNetworking.sourceDestCheck: DisabledPrimaryENI` — Disables EC2 source/destination check on the node’s primary ENI so the gateway can forward traffic that isn’t addressed to itself.
- `taints` — The `hybrid-gateway-node: NoSchedule` taint ensures only gateway pods with a matching toleration schedule on these nodes.
- `labels` — The `hybrid-gateway-node: "true"` label is used by the Helm chart’s node selector to target gateway pods to these nodes.
- `nodeClassRef` — Links the NodePool to the NodeClass with the source/destination check configuration.

### Managed node groups

When using managed node groups, create a dedicated node group for the gateway with the required labels, taints, and a custom launch template that disables source/destination check at launch.

#### Step 1: Create a launch template

Create a launch template with user data that disables source/destination check on the primary ENI when the instance boots:

```
# Create the launch template with user data to disable source/dest check
USERDATA=$(cat <<'SCRIPT' | base64 -w 0
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==BOUNDARY=="

--==BOUNDARY==
Content-Type: text/x-shellscript; charset="us-ascii"

#!/bin/bash
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 60")
MAC=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/mac)
ENI_ID=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  "http://169.254.169.254/latest/meta-data/network/interfaces/macs/${MAC}/interface-id")
REGION=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/placement/region)

aws ec2 modify-network-interface-attribute \
  --network-interface-id "$ENI_ID" \
  --no-source-dest-check \
  --region "$REGION"

--==BOUNDARY==--
SCRIPT
)

aws ec2 create-launch-template \
  --launch-template-name `YOUR_CLUSTER_NAME`-gateway-lt \
  --launch-template-data "{\"UserData\":\"${USERDATA}\",\"MetadataOptions\":{\"HttpTokens\":\"required\",\"HttpPutResponseHopLimit\":2}}"
```

###### Note

The node’s IAM role must have `ec2:ModifyNetworkInterfaceAttribute` permission for the user data script to succeed. The MIME multipart format ensures the user data runs alongside the EKS bootstrap script.

#### Step 2: Create the managed node group

Create a dedicated managed node group with the gateway label, taint, and the launch template from Step 1:

```
aws eks create-nodegroup \
  --cluster-name `YOUR_CLUSTER_NAME` \
  --nodegroup-name `YOUR_CLUSTER_NAME`-gateway-nodes \
  --subnets `SUBNET_ID_1 SUBNET_ID_2` \
  --node-role `YOUR_NODE_ROLE_ARN` \
  --instance-types `INSTANCE_TYPE` \
  --ami-type AL2023_x86_64_STANDARD \
  --scaling-config desiredSize=2,maxSize=2,minSize=2 \
  --labels hybrid-gateway-node=true \
  --taints "key=hybrid-gateway-node,effect=NO_SCHEDULE" \
  --launch-template "name=`YOUR_CLUSTER_NAME`-gateway-lt,version=1"
```

This creates a 2-node managed node group where:

- `--labels` sets `hybrid-gateway-node=true` so the Helm chart’s node selector targets these nodes.
- `--taints` adds a `NoSchedule` taint so only gateway pods with a matching toleration schedule on these nodes.
- `--launch-template` attaches the launch template that disables source/destination check at boot.

Use subnets in different Availability Zones for high availability.

## Install with Helm

### EKS Auto Mode

Run the following command to install the gateway with EKS Auto Mode:

```
helm install eks-hybrid-nodes-gateway \
  oci://public.ecr.aws/eks/eks-hybrid-nodes-gateway \
  --version 1.0.0 \
  --namespace eks-hybrid-nodes-gateway \
  --create-namespace \
  --set vpcCIDR=`VPC_CIDR` \
  --set podCIDRs=`POD_CIDRS` \
  --set routeTableIDs=`ROUTE_TABLE_IDS`

```

### Managed node groups or self-managed nodes

For managed node groups or self-managed nodes, set `autoMode.enabled=false`:

```
helm install eks-hybrid-nodes-gateway \
  oci://public.ecr.aws/eks/eks-hybrid-nodes-gateway \
  --version 1.0.0 \
  --namespace eks-hybrid-nodes-gateway \
  --create-namespace \
  --set autoMode.enabled=false \
  --set vpcCIDR=`VPC_CIDR` \
  --set podCIDRs=`POD_CIDRS` \
  --set routeTableIDs=`ROUTE_TABLE_IDS`

```

### Required Helm values

The following values are required for all installations:

| Value           | Description                                                                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `vpcCIDR`       | The CIDR block of your EKS cluster VPC (for example, `10.0.0.0/16`). Used for Cilium VTEP configuration so hybrid nodes route VPC-bound traffic through the gateway.                                                      |
| `podCIDRs`      | Comma-separated list of pod CIDRs used by Cilium on hybrid nodes (for example, `10.100.0.0/16,10.101.0.0/16`). The gateway creates VPC route table entries and VXLAN routes for these CIDRs.                              |
| `routeTableIDs` | Comma-separated list of VPC route table IDs to program (for example, `rtb-0abc1234def567890,rtb-0fed9876cba543210`). The gateway creates routes in these tables pointing hybrid pod CIDRs to the active gateway instance. |

For a complete list of configurable values, see [Amazon EKS Hybrid Nodes gateway configuration reference](hybrid-nodes-gateway-configuration.md "hybrid-nodes-gateway-configuration.md").

## Verify the installation

After installing the gateway, verify that it is running and healthy.

### Check pod status

Confirm that two gateway pods are running:

```
kubectl get pods -n eks-hybrid-nodes-gateway
```

You should see output similar to:

```
NAME                                        READY   STATUS    RESTARTS   AGE
eks-hybrid-nodes-gateway-5d4f6a7b8c-abc12   1/1     Running   0          2m
eks-hybrid-nodes-gateway-5d4f6a7b8c-def34   1/1     Running   0          2m
```

### Check leader election

Verify that one pod has acquired the leader election lease:

```
kubectl get lease -n eks-hybrid-nodes-gateway
```

The output shows the current leader in the `HOLDER` column:

```
NAME                     HOLDER                                      AGE
hybrid-gateway-leader    eks-hybrid-nodes-gateway-5d4f6a7b8c-abc12   2m
```

### Check health endpoint

Verify the health endpoint is responding on the leader pod using port-forwarding:

```
kubectl port-forward -n eks-hybrid-nodes-gateway `LEADER_POD_NAME` 8088:8088 &
curl -s http://localhost:8088/healthz
```

A healthy gateway returns an HTTP 200 response.

### Verify VPC route table entries

In the Amazon VPC console or using the AWS CLI, confirm that your VPC route tables contain entries for the hybrid pod CIDRs pointing to the leader gateway instance’s ENI:

```
aws ec2 describe-route-tables \
  --route-table-ids `ROUTE_TABLE_ID` \
  --query "RouteTables[].Routes[?DestinationCidrBlock=='POD_CIDR']"
```

Each hybrid pod CIDR should have a route with the `NetworkInterfaceId` set to the leader instance’s primary ENI.

## Uninstall

To remove the Hybrid Nodes gateway, run:

```
helm uninstall eks-hybrid-nodes-gateway --namespace eks-hybrid-nodes-gateway
```

###### Note

Uninstalling the Helm chart does not automatically remove the VPC route table entries created by the gateway. After uninstalling, manually delete the routes for your hybrid pod CIDRs from the VPC route tables to avoid routing traffic to instances that are no longer running the gateway. You can remove routes using the AWS CLI:

```
aws ec2 delete-route \
  --route-table-id `ROUTE_TABLE_ID` \
  --destination-cidr-block `POD_CIDR`

```

## Next steps

- [Amazon EKS Hybrid Nodes gateway configuration reference](hybrid-nodes-gateway-configuration.md "hybrid-nodes-gateway-configuration.md") — Customize Helm values, CLI flags, and leader election parameters.
- [Amazon EKS Hybrid Nodes gateway operations](hybrid-nodes-gateway-operations.md "hybrid-nodes-gateway-operations.md") — Monitor the gateway, understand failover behavior, and plan for scaling.
- [Amazon EKS Hybrid Nodes gateway troubleshooting](hybrid-nodes-gateway-troubleshooting.md "hybrid-nodes-gateway-troubleshooting.md") — Diagnose and resolve common issues.
