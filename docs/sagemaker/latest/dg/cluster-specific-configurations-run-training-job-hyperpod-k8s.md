# Running a training job on HyperPod k8s

SageMaker HyperPod Recipes supports submitting a training job to a GPU/Trainium
Kubernetes cluster. Before you submit the training job do one of the
following:

- Modify the `k8s.yaml` cluster configuration file
- Override the cluster configuration through the command line
  After you've done either of the preceding steps, install the corresponding
  environment.

## Configure the cluster using `k8s.yaml`

To submit a training job to a Kubernetes cluster, you specify
Kubernetes-specific configurations. The configurations include the cluster
namespace or the location of the persistent volume.

```
pullPolicy: Always
restartPolicy: Never
namespace: default
persistent_volume_claims:
  - null
```

1. `pullPolicy`: You can specify the pull policy when you
   submit a training job. If you specify "Always," the Kubernetes cluster
   always pulls your image from the repository. For more information, see
   [Image pull policy](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy "https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy").
2. `restartPolicy`: Specify whether to restart your training
   job if it fails.
3. `namespace`: You can specify the Kubernetes namespace where
   you're submitting the training job.
4. `persistent_volume_claims`: You can specify a shared volume
   for your training job for all training processes to access the files in
   the volume.
