#

Using topology-aware scheduling in Amazon SageMaker HyperPod task governance

Topology-aware scheduling in Amazon SageMaker HyperPod task governance
optimizes the training efficiency of distributed machine learning workloads by placing pods based on the physical network topology of your Amazon EC2 instances.
By considering the hierarchical structure of AWS infrastructure, including Availability Zones, network blocks, and physical racks, topology-aware scheduling ensures
that pods requiring frequent communication are scheduled in close proximity to minimize network latency. This intelligent placement is
particularly beneficial for large-scale machine learning training jobs that involve intensive pod-to-pod communication, resulting in
reduced training times and more efficient resource utilization across your cluster.

###### Note

To use topology-aware scheduling, make sure that your version of HyperPod task governance is v1.2.2-eksbuild.1 or higher.

Topology-aware scheduling supports the following instance types:

- ml.p3dn.24xlarge
- ml.p4d.24xlarge
- ml.p4de.24xlarge
- ml.p5.48xlarge
- ml.p5e.48xlarge
- ml.p5en.48xlarge
- ml.p6e-gb200.36xlarge
- ml.trn1.2xlarge
- ml.trn1.32xlarge
- ml.trn1n.32xlarge
- ml.trn2.48xlarge
- ml.trn2u.48xlarge
  Topology-aware scheduling integrates with your existing HyperPod workflows while providing flexible
  topology preferences through both kubectl YAML files and the HyperPod CLI.
  HyperPod task governance automatically configures cluster nodes with topology labels and works with HyperPod task governance policies and resource borrowing mechanisms,
  ensuring that topology-aware scheduling doesn't disrupt your current operational processes. With built-in support for both preferred and required topology specifications,
  you can fine-tune workload placement to match your specific performance requirements while maintaining the flexibility to fall back to standard
  scheduling when topology constraints cannot be satisfied.

By leveraging topology-aware labels in HyperPod, you can enhance their machine learning workloads through intelligent pod placement that
considers the physical network infrastructure. HyperPod task governance automatically optimizes pod scheduling based on the hierarchical data
center topology, which directly translates to reduced network latency and improved training performance for distributed ML tasks. This topology
awareness is particularly valuable for large-scale machine learning workloads, as it minimizes communication overhead by strategically placing
related pods closer together in the network hierarchy. The result is optimized communication network latency between pods, more efficient resource utilization,
and better overall performance for compute-intensive AI/ML applications, all achieved without you needing to manually manage complex network topology configurations.

The following are labels for the available topology network layers that HyperPod task governance can schedule pods in:

- topology.k8s.aws/network-node-layer-1
- topology.k8s.aws/network-node-layer-2
- topology.k8s.aws/network-node-layer-3
- topology.k8s.aws/ultraserver-id
  To use topology-aware scheduling, include the following labels in your YAML file:

- kueue.x-k8s.io/podset-required-topology - indicates that this job must have the required pods and that all pods in the nodes must be scheduled within the same topology layer.
- kueue.x-k8s.io/podset-preferred-topology - indicates that this job must have the pods, but that scheduling pods within the same topology layer is preferred but not required.
  HyperPod task governance will try to schedule the pods within one layer before trying the next topology layer.
  If resources don’t share the same topology label, the job will be suspended. The job will be in the waitlist.
  Once Kueue sees that there are enough resources, it will admit and run the job.

The following example demonstrates how to use the labels in your YAML files:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: test-tas-job
  namespace: hyperpod-ns-`team-name`
  labels:
    kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue
    kueue.x-k8s.io/priority-class: `PRIORITY_CLASS`-priority
spec:
  parallelism: 10
  completions: 10
  suspend: true
  template:
    metadata:
      labels:
        kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue
      annotations:
        kueue.x-k8s.io/podset-required-topology: "topology.k8s.aws/network-node-layer-3"
        or
        kueue.x-k8s.io/podset-preferred-topology: "topology.k8s.aws/network-node-layer-3"
    spec:
      nodeSelector:
        topology.k8s.aws/network-node-layer-3: `TOPOLOGY_LABEL_VALUE`
      containers:
        - name: dummy-job
          image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
          args: ["3600s"]
          resources:
            requests:
              cpu: "100"
      restartPolicy: Never
```

The following table explains the new parameters you can use in the kubectl YAML file.

| Parameter                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kueue.x-k8s.io/queue-name     | The name of the queue to use to run the job. The format of this queue-name must be `hyperpod-ns-`team-name`-localqueue`.                                                                                                                                                                                                                                                                                                                                                                            |
| kueue.x-k8s.io/priority-class | Lets you specify a priority for pod scheduling. This specification is optional.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| annotations                   | Contains the topology annotation that you attach to the job. Available topologies are _kueue.x-k8s.io/podset-required-topology_ and _kueue.x-k8s.io/podset-preferred-topology._ You can use either an annotation or nodeSelector, but not both at the same time.                                                                                                                                                                                                                                    |
| nodeSelector                  | Specifies the network layer that represents the layer of Amazon EC2 instance placement. Use either this field or an annotation, but not both at the same time. In your YAML file, you can also use the nodeSelector parameter to choose the exact layer for your pods. To get the value of your label, use the [DescribeInstanceTopology](../../../AWSEC2/latest/APIReference/API_DescribeInstanceTopology.md "../../../AWSEC2/latest/APIReference/API_DescribeInstanceTopology.md") API operation. | You can also use the HyperPod CLI to run your job and use topology aware scheduling. For more information about the HyperPod CLI, see [SageMaker HyperPod CLI commands](sagemaker-hyperpod-eks-hyperpod-cli-reference.md "sagemaker-hyperpod-eks-hyperpod-cli-reference.md"). ``hyp create hyp-pytorch-job \ --version 1.1 \ --job-name sample-pytorch-job \ --image 123456789012.dkr.ecr.us-west-2.amazonaws.com/ptjob:latest \ --pull-policy "Always" \ --tasks-per-node 1 \ --max-retry 1 \ --priority high-priority \ --namespace hyperpod-ns-`team-name` \ --queue-name hyperpod-ns-`team-name`-localqueue \ --preferred-topology-label topology.k8s.aws/network-node-layer-1`` The following is an example configuration file that you might use to run a PytorchJob with topology labels. The file is largely similar if you want to run MPI and Tensorflow jobs. If you want to run those jobs instead, remember to change the configuration file accordingly, such as using the correct image instead of PyTorchJob. If you’re running a PyTorchJob, you can assign different topologies to the master and worker nodes. PyTorchJob always has one master node, so we recommend that you use topology to support worker pods instead. ``apiVersion: kubeflow.org/v1 kind: PyTorchJob metadata: annotations: {} labels: kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue name: tas-test-pytorch-job namespace: hyperpod-ns-team-name spec: pytorchReplicaSpecs: Master: replicas: 1 restartPolicy: OnFailure template: metadata: labels: kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue spec: containers: <br>• command: <br>• python3 <br>• /opt/pytorch-mnist/mnist.py <br>• --epochs=1 image: docker.io/kubeflowkatib/pytorch-mnist:v1beta1-45c5727 imagePullPolicy: Always name: pytorch Worker: replicas: 10 restartPolicy: OnFailure template: metadata: # annotations: # kueue.x-k8s.io/podset-required-topology: "topology.k8s.aws/network-node-layer-3" labels: kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue spec: containers: <br>• command: <br>• python3 <br>• /opt/pytorch-mnist/mnist.py <br>• --epochs=1 image: docker.io/kubeflowkatib/pytorch-mnist:v1beta1-45c5727 imagePullPolicy: Always name: pytorch resources: limits: cpu: 1 requests: memory: 200Mi cpu: 1 #nodeSelector: #  topology.k8s.aws/network-node-layer-3: xxxxxxxxxxx`` To see the topologies for your cluster, use the [DescribeInstanceTopology](../../../AWSEC2/latest/APIReference/API_DescribeInstanceTopology.md "../../../AWSEC2/latest/APIReference/API_DescribeInstanceTopology.md") API operation. By default, the topologies are hidden in the AWS Management Console and Amazon SageMaker Studio. Follow these steps to see them in the interface that you’re using. **SageMaker Studio** 1. In SageMaker Studio, navigate to your cluster. 2. In the Tasks view, choose the options menu in the Name column, then choose **Manage columns**. 3. Select **Requested topology** and **Topology constraint** to add the columns to see the topology information in the list of Kubernetes pods. **AWS Management Console** 1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/"). 2. Under **HyperPod clusters**, choose **Cluster management**. 3. Choose the **Tasks** tab, then choose the gear icon. 4. Under instance attributes, toggle **Requested topology** and **Topology constraint**. 5. Choose **Confirm** to see the topology information in the table. |
