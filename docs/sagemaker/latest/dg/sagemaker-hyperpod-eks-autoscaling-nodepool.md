# Create a NodePool

The `NodePool` sets constraints on the nodes that can be created by
Karpenter and the pods that can run on those nodes. The `NodePool` can be
configured to do things like:

- Limit node creation to certain zones, instance types, and computer
  architectures.
- Define labels or taints to limit the pods that can run on nodes Karpenter
  creates.

###### Note

HyperPod provider supports a limited set of well-known Kubernetes and
Karpenter requirements explained below.

The following steps cover how to create a `NodePool`.

1. Create a YAML file named nodepool.yaml with your desired `NodePool`
   configuration.
2. You can use the sample configuration below.

Look for `Ready` under `Conditions` to indicate all
dependent resources are functioning properly.

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
 name: sample-np
spec:
 template:
   spec:
     nodeClassRef:
      group: karpenter.sagemaker.amazonaws.com
      kind: HyperpodNodeClass
      name: multiazc5
     expireAfter: Never
     requirements:
        - key: node.kubernetes.io/instance-type
          operator: Exists
```

3. Apply the `NodePool` to your cluster:

```
kubectl apply -f nodepool.yaml
```

4. Monitor the `NodePool` status to ensure the `Ready`
   condition in status is set to `True`:

```
kubectl get nodepool sample-np -oyaml
```

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: <nodepool-name>
  uid: <resource-uid>
  ...
spec:
  disruption:
    budgets:
    - nodes: 90%
    consolidateAfter: 0s
    consolidationPolicy: WhenEmptyOrUnderutilized
  template:
    spec:
      expireAfter: 720h
      nodeClassRef:
        group: karpenter.sagemaker.amazonaws.com
        kind: HyperpodNodeClass
        name: <nodeclass-name>
      requirements:
      - key: node.kubernetes.io/instance-type
        operator: Exists
status:
  conditions:
  - lastTransitionTime: "<timestamp>"
    message: ""
    observedGeneration: 2
    reason: ValidationSucceeded
    status: "True"
    type: ValidationSucceeded
  - lastTransitionTime: "<timestamp>"
    message: ""
    observedGeneration: 2
    reason: NodeClassReady
    status: "True"
    type: NodeClassReady
  - lastTransitionTime: "<timestamp>"
    message: ""
    observedGeneration: 2
    reason: Ready
    status: "True"
    type: Ready

```

**Supported Labels for Karpenter HyperPod
Provider**

These are the optional constraints and requirements you can specify in your
`NodePool` configuration.

| Requirement Type                                    | Purpose                                                           | Use Case/Supported Values                                                                                              | Recommendation                                                                                                              |
| --------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Instance Types (`node.kubernetes.io/instance-type`) | Controls which SageMaker instance types Karpenter can choose from | Instead of restricting to only ml.c5.xlarge, let Karpenter pick from all available types in your instance groups       | Leave this undefined or use Exists operator to give Karpenter maximum flexibility in choosing cost-effective instance types |
| Availability Zones (`topology.kubernetes.io/zone`)  | Controls which AWS availability zones nodes can be created in     | Specific zone names like us-east-1c. Use when you need pods to run in specific zones for latency or compliance reasons | n/a                                                                                                                         |
| Architecture (`kubernetes.io/arch`)                 | Specifies CPU architecture                                        | Only amd64 (no ARM support currently)                                                                                  | n/a                                                                                                                         |
