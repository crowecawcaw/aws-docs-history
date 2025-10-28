# Running jobs using

`kubectl`

###### Note

Training job auto resume requires Kubeflow Training Operator release version
`1.7.0`, `1.8.0`, or `1.8.1`.

Note that you should install Kubeflow Training Operator in the clusters using a Helm
chart. For more information, see [Installing
packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md "sagemaker-hyperpod-eks-install-packages-using-helm-chart.md"). Verify if the
Kubeflow Training Operator control plane is properly set up by running the following
command.

```
`kubectl get pods -n kubeflow`
```

This should return an output similar to the following.

```
NAME                                             READY   STATUS    RESTARTS   AGE
training-operator-658c68d697-46zmn               1/1     Running   0          90s
```

**To submit a training job**

To run a training jobs, prepare the job configuration file and run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply "https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply") command as follows.

```
`kubectl apply -f `/path/to/training_job.yaml``
```

**To describe a training job**

To retrieve the details of the job submitted to the EKS cluster, use the following
command. It returns job information such as the job submission time, completion time,
job status, configuration details.

```
`kubectl get -o yaml `training-job` -n `kubeflow``
```

**To stop a training job and delete EKS
resources**

To stop a training job, use kubectl delete. The following is an example of stopping
the training job created from the configuration file
`pytorch_job_simple.yaml`.

```
`kubectl delete -f `/path/to/training_job.yaml``
```

This should return the following output.

```
pytorchjob.kubeflow.org "training-job" deleted
```

**To enable job auto-resume**

SageMaker HyperPod supports job auto-resume functionality for Kubernetes jobs, integrating
with the Kubeflow Training Operator control plane.

Ensure that there are sufficient nodes in the cluster that have passed the
SageMaker HyperPod health check. The nodes should have the taint
`sagemaker.amazonaws.com/node-health-status` set to
`Schedulable`. It is recommended to include a node selector in the job
YAML file to select nodes with the appropriate configuration as follows.

```
sagemaker.amazonaws.com/node-health-status: Schedulable
```

The following code snippet is an example of how to modify a Kubeflow PyTorch job YAML
configuration to enable the job auto-resume functionality. You need to add two
annotations and set `restartPolicy` to `OnFailure` as
follows.

```
apiVersion: "kubeflow.org/v1"
kind: PyTorchJob
metadata:
    name: pytorch-simple
    namespace: kubeflow
    `annotations: { // config for job auto resume
 sagemaker.amazonaws.com/enable-job-auto-resume: "true"
 sagemaker.amazonaws.com/job-max-retry-count: "2"
 }`
spec:
  pytorchReplicaSpecs:
  ......
  Worker:
      replicas: 10
      `restartPolicy: OnFailure`
      template:
          spec:
              nodeSelector:
                  sagemaker.amazonaws.com/node-health-status: Schedulable
```

**To check the job auto-resume status**

Run the following command to check the status of job auto-resume.

```
`kubectl describe pytorchjob -n kubeflow `<job-name>``
```

Depending on the failure patterns, you might see two patterns of Kubeflow training job
restart as follows.

**Pattern 1**:

```
Start Time:    2024-07-11T05:53:10Z
Events:
  Type     Reason                   Age                    From                   Message
  ----     ------                   ----                   ----                   -------
  Normal   SuccessfulCreateService  9m45s                  pytorchjob-controller  Created service: pt-job-1-worker-0
  Normal   SuccessfulCreateService  9m45s                  pytorchjob-controller  Created service: pt-job-1-worker-1
  Normal   SuccessfulCreateService  9m45s                  pytorchjob-controller  Created service: pt-job-1-master-0
  Warning  PyTorchJobRestarting     7m59s                  pytorchjob-controller  PyTorchJob pt-job-1 is restarting because 1 Master replica(s) failed.
  Normal   SuccessfulCreatePod      7m58s (x2 over 9m45s)  pytorchjob-controller  Created pod: pt-job-1-worker-0
  Normal   SuccessfulCreatePod      7m58s (x2 over 9m45s)  pytorchjob-controller  Created pod: pt-job-1-worker-1
  Normal   SuccessfulCreatePod      7m58s (x2 over 9m45s)  pytorchjob-controller  Created pod: pt-job-1-master-0
  Warning  PyTorchJobRestarting     7m58s                  pytorchjob-controller  PyTorchJob pt-job-1 is restarting because 1 Worker replica(s) failed.
```

**Pattern 2**:

```
Events:
  Type    Reason                   Age    From                   Message
  ----    ------                   ----   ----                   -------
  Normal  SuccessfulCreatePod      19m    pytorchjob-controller  Created pod: pt-job-2-worker-0
  Normal  SuccessfulCreateService  19m    pytorchjob-controller  Created service: pt-job-2-worker-0
  Normal  SuccessfulCreatePod      19m    pytorchjob-controller  Created pod: pt-job-2-master-0
  Normal  SuccessfulCreateService  19m    pytorchjob-controller  Created service: pt-job-2-master-0
  Normal  SuccessfulCreatePod      4m48s  pytorchjob-controller  Created pod: pt-job-2-worker-0
  Normal  SuccessfulCreatePod      4m48s  pytorchjob-controller  Created pod: pt-job-2-master-0
```
