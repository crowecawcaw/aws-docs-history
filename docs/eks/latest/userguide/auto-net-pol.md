**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use Network Policies with EKS Auto Mode

Network policies allow you to control traffic flow at the IP address or port level within your Amazon EKS cluster. This topic explains how to enable and use network policies with EKS Auto Mode.

## Prerequisites

- An Amazon EKS cluster with EKS Auto Mode enabled
- kubectl configured to connect to your cluster

## Step 1: Enable Network Policy Controller

To use network policies with EKS Auto Mode, you first need to enable the Network Policy Controller by applying a ConfigMap to your cluster.

1. Create a file named `enable-network-policy.yaml` with the following content:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: amazon-vpc-cni
  namespace: kube-system
data:
  enable-network-policy-controller: "true"
```

2. Apply the ConfigMap to your cluster:

```
kubectl apply -f enable-network-policy.yaml
```

## Step 2: Enable Network Policies in Node Class

Before you can use network policies, you need to ensure that your Node Class is configured to support them. Follow these steps:

1. Create or edit a Node Class YAML file (e.g., `nodeclass-network-policy.yaml`) with the following content:

```
apiVersion: eks.amazonaws.com/v1
kind: NodeClass
metadata:
  name: network-policy-enabled
spec:
  # Enables network policy support
  networkPolicy: DefaultAllow
  # Optional: Enables logging for network policy events
  networkPolicyEventLogs: Enabled
  # Include other Node Class configurations as needed
```

2. Apply the Node Class configuration to your cluster:

```
kubectl apply -f nodeclass-network-policy.yaml
```

3. Verify that the Node Class has been created:

```
kubectl get nodeclass network-policy-enabled
```

4. Update your Node Pool to use this Node Class. For more information, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md").

Once your nodes are using this Node Class, they will be able to enforce network policies. You can now proceed to create and apply network policies to control traffic within your cluster. For all the node class configuration options, see [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md").

## Step 3: Create and test network policies

Your EKS Auto Mode cluster is now configured to support Kubernetes network policies. You can test this with the [Stars demo of network policy for Amazon EKS](network-policy-stars-demo.md "network-policy-stars-demo.md").
