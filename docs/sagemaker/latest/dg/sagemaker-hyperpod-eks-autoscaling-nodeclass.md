# Create a

NodeClass

###### Important

You must start with 0 nodes in your instance group and let Karpenter handle the
autoscaling. If you start with more than 0 nodes, Karpenter will scale them down to 0.

A node class (`NodeClass`) defines infrastructure-level settings that apply
to groups of nodes in your Amazon EKS cluster, including network configuration, storage
settings, and resource tagging. A `HyperPodNodeClass` is a custom
`NodeClass` that maps to pre-created instance groups in SageMaker HyperPod,
defining constraints around which instance types and Availability Zones are supported
for Karpenter's autoscaling decisions.

**Considerations for creating a node class**

- You can specify up to 10 instance groups in a `NodeClass`.
- If you choose to delete an instance group, we recommend removing it from your
  `NodeClass` before deleting it from your HyperPod
  cluster. If an instance group is deleted while it is used in a
  `NodeClass`, the `NodeClass` will be marked as not
  `Ready` for provisioning and won't be used for subsequent scaling
  operations until the instance group is removed from
  `NodeClass`.
- When you remove instance groups from a `NodeClass`, Karpenter will
  detect a drift on the nodes that were managed by Karpenter in the instance
  group(s) and disrupt the nodes based on your disruption budget controls.
- Subnets used by the instance group should belong to the same AZ. Subnets are
  specified either using `OverrideVpcConfig` at the instance group
  level or the cluster level. `VpcConfig` is used by default.
- Only on-demand capacity is supported at this time. Instance groups with
  Training plan or reserved capacity are not supported.
- Instance groups with `DeepHealthChecks (DHC)` are not supported.
  This is because a DHC takes around 60-90 minutes to complete and pods will
  remain in pending state during that time which can cause
  over-provisioning.
  The following steps cover how to create a `NodeClass`.

1. Create a YAML file (for example, nodeclass.yaml) with your
   `NodeClass` configuration.
2. Apply the configuration to your cluster using kubectl.
3. Reference the `NodeClass` in your `NodePool`
   configuration.
4. Here's a sample `NodeClass` that uses a ml.c5.xlarge and
   ml.c5.4xlarge instance types:

```
apiVersion: karpenter.sagemaker.amazonaws.com/v1
kind: HyperpodNodeClass
metadata:
  name: sample-nc
spec:
  instanceGroups:
    # name of InstanceGroup in HyperPod cluster. InstanceGroup needs to pre-created
    # MaxItems: 10
    - auto-c5-xaz1
    - auto-c5-4xaz2
```

5. Apply the configuration:

```
kubectl apply -f nodeclass.yaml
```

6. Monitor the NodeClass status to ensure the Ready condition in status is set to
   True:

```
kubectl get hyperpodnodeclass sample-nc -o yaml
```

```
apiVersion: karpenter.sagemaker.amazonaws.com/v1
kind: HyperpodNodeClass
metadata:
  creationTimestamp: "<timestamp>"
  name: sample-nc
  uid: <resource-uid>
spec:
  instanceGroups:
  - auto-c5-az1
  - auto-c5-4xaz2
status:
  conditions:
  // true when all IGs in the spec are present in SageMaker cluster, false otherwise
  - lastTransitionTime: "<timestamp>"
    message: ""
    observedGeneration: 3
    reason: InstanceGroupReady
    status: "True"
    type: InstanceGroupReady
  // true if subnets of IGs are discoverable, false otherwise
  - lastTransitionTime: "<timestamp>"
    message: ""
    observedGeneration: 3
    reason: SubnetsReady
    status: "True"
    type: SubnetsReady
  // true when all dependent resources are Ready [InstanceGroup, Subnets]
  - lastTransitionTime: "<timestamp>"
    message: ""
    observedGeneration: 3
    reason: Ready
    status: "True"
    type: Ready
  instanceGroups:
  - instanceTypes:
    - ml.c5.xlarge
    name: auto-c5-az1
    subnets:
    - id: <subnet-id>
      zone: <availability-zone-a>
      zoneId: <zone-id-a>
  - instanceTypes:
    - ml.c5.4xlarge
    name: auto-c5-4xaz2
    subnets:
    - id: <subnet-id>
      zone: <availability-zone-b>
      zoneId: <zone-id-b>
```
