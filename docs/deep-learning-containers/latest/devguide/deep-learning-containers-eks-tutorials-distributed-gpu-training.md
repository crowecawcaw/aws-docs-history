# Distributed GPU Training

This section is for running distributed training on multi-node GPU clusters.

###### Contents

- [Set
  up your cluster for distributed training](#deep-learning-containers-eks-tutorials-distributed-gpu-setup "#deep-learning-containers-eks-tutorials-distributed-gpu-setup")
- [PyTorch
  distributed GPU training](#deep-learning-containers-eks-tutorials-distributed-gpu-training-pytorch "#deep-learning-containers-eks-tutorials-distributed-gpu-training-pytorch")

## Set

up your cluster for distributed training

To run distributed training on EKS, you need the following components
installed on your cluster.

- The default installation of [Kubeflow](https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/ "https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/") with
  required components, such as PyTorch operators, and the NVIDIA plugin.
- MPI operators.

Download and run the script to install the required components in the
cluster.

```
$ wget -O install_kubeflow.sh https://raw.githubusercontent.com/aws/deep-learning-containers/master/test/dlc_tests/eks/eks_manifest_templates/kubeflow/install_kubeflow.sh
$ chmod +x install_kubeflow.sh
$ ./install_kubeflow.sh `<EKS_CLUSTER_NAME>` `<AWS_REGION>`
```

## PyTorch

distributed GPU training

This tutorial will guide you on distributed training with PyTorch on your
multi-node GPU cluster. It uses Gloo as the backend.

1. Verify that the PyTorch custom resource is installed.

```
`$` kubectl get crd
```

The output should include `pytorchjobs.kubeflow.org`. 2. Ensure that the NVIDIA plugin `daemonset` is running.

```
`$` kubectl get daemonset -n kubeflow
```

The output should should look similar to the following.

```

NAME                          DESIRED CURRENT READY UP-TO-DATE AVAILABLE NODE SELECTOR AGE
nvidia-device-plugin-daemonset   3         3      3        3        3    <none>  35h
```

3. Use the following text to create a gloo-based distributed data parallel
   job. Save it in a file named `distributed.yaml`.

```
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: `"kubeflow-pytorch-gpu-dist-job"`
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      restartPolicy: OnFailure
      template:
        spec:
          containers:
          - name: `"pytorch"`
            image: `"763104351884.dkr.ecr.us-east-1.amazonaws.com/aws-samples-pytorch-training:1.7.1-gpu-py36-cu110-ubuntu18.04-example"`
            args:
              - "--backend"
              - "gloo"
              - "--epochs"
              - "5"
    Worker:
      replicas: 2
      restartPolicy: OnFailure
      template:
        spec:
          containers:
          - name: `"pytorch"`
            image: `"763104351884.dkr.ecr.us-east-1.amazonaws.com/aws-samples-pytorch-training:1.7.1-gpu-py36-cu110-ubuntu18.04-example"`
            args:
              - "--backend"
              - "gloo"
              - "--epochs"
              - "5"
            resources:
              limits:
                nvidia.com/gpu: 1
```

4. Run a distributed training job with the pod file you just created.

```
`$` kubectl create -f distributed.yaml
```

5. You can check the status of the job using the following:

```
`$` kubectl logs kubeflow-pytorch-gpu-dist-job

```

To view logs continuously, use:

```
`$` kubectl logs -f `<pod>`
```
