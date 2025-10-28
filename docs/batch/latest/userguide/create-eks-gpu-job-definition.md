# Create an Amazon EKS GPU job definition

Only `nvidia.com/gpu` is supported at this time and resource value that you set must be a whole
number. You can’t use fractions of GPU. For more information, see [Schedule GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/ "https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/") in the _Kubernetes
documentation_.

To register a GPU job definition for Amazon EKS, run the following commands.

```
`$` `cat <<EOF > ./batch-eks-gpu-jd.json
{
 "jobDefinitionName": "MyGPUJobOnEks_Smi",
 "type": "container",
 "eksProperties": {
 "podProperties": {
 "hostNetwork": true,
 "containers": [
 {
 "image": "nvcr.io/nvidia/cuda:10.2-runtime-centos7",
 "command": ["nvidia-smi"],
 "resources": {
 "limits": {
 "cpu": "1",
 "memory": "1024Mi",
 "nvidia.com/gpu": "1"
 }
 }
 }
 ]
 }
 }
}
EOF`

`$` `aws batch register-job-definition --cli-input-json file://./batch-eks-gpu-jd.json`

```
