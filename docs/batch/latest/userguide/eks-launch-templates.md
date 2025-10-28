# Customize Amazon EKS launch templates

AWS Batch on Amazon EKS supports launch templates. There are constraints on what your launch template can do.

###### Important

- For EKS AL2 AMIs, AWS Batch runs `/etc/eks/bootstrap.sh`. Don't run
  `/etc/eks/bootstrap.sh` in your launch template or cloud-init user-data
  scripts. You can add additional parameters besides the `--kubelet-extra-args`
  parameter to [bootstrap.sh](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2/runtime/bootstrap.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2/runtime/bootstrap.sh"). To do this, set the `AWS_BATCH_KUBELET_EXTRA_ARGS`
  variable in the `/etc/aws-batch/batch.config` file. See the following example for
  details.
- For EKS AL2023, AWS Batch utilizes the [NodeConfigSpec](https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec "https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec") from EKS to make instances join the EKS cluster. AWS Batch
  populates [ClusterDetails](https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#clusterdetails "https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#clusterdetails") in [NodeConfigSpec](https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec "https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec") for the EKS cluster and you don't need to specify them.

###### Note

We recommend that you do not set any of the follow [NodeConfigSpec](https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec "https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec") settings in the launch template as AWS Batch will override your values. For more information, see [Shared responsibility of the Kubernetes nodes](eks-ce-shared-responsibility.md "eks-ce-shared-responsibility.md").

- `Taints`
- `Cluster Name`
- `apiServerEndpoint`
- `certificatAuthority`
- `CIDR`
- Do not create a labels with the prefix `batch.amazonaws.com/`

###### Note

If the launch template is changed after [CreateComputeEnvironment](../APIReference/API_CreateComputeEnvironment.md "../APIReference/API_CreateComputeEnvironment.md") is called, [UpdateComputeEnvironment](../APIReference/API_UpdateComputeEnvironment.md "../APIReference/API_UpdateComputeEnvironment.md") must be called to evaluate the version of the launch template for
replacement.

###### Topics

- [Add kubelet extra arguments](#kubelet-extra-args "#kubelet-extra-args")
- [Configure the container runtime](#change-container-runtime "#change-container-runtime")
- [Mount an Amazon EFS volume](#mounting-efs-volume "#mounting-efs-volume")
- [IPv6 support](#eks-ipv6-support "#eks-ipv6-support")

## Add `kubelet` extra arguments

AWS Batch supports adding extra arguments to the `kubelet` command. For the
list of supported parameters, see [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/ "https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/") in the _Kubernetes documentation_. In the
following example for EKS AL2 AMIs, `--node-labels
 mylabel=helloworld` is added to the `kubelet` command
line.

```
MIME-Version: 1.0
      Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

      --==MYBOUNDARY==
      Content-Type: text/x-shellscript; charset="us-ascii"

      #!/bin/bash
      mkdir -p /etc/aws-batch

      echo AWS_BATCH_KUBELET_EXTRA_ARGS=\"`--node-labels mylabel=helloworld`\" >> /etc/aws-batch/batch.config

      --==MYBOUNDARY==--
```

For EKS AL2023 AMIs the file format is YAML. For the list of supported parameters, see
[NodeConfigSpec](https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec "https://awslabs.github.io/amazon-eks-ami/nodeadm/doc/api/#nodeconfigspec") in the _Kubernetes documentation_.
In the following example for EKS AL2023 AMIs, `--node-labels
 mylabel=helloworld` is added to the `kubelet` command
line.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: application/node.eks.aws

apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  kubelet:
    flags:
    - --`node-labels=mylabel=helloworld`

--==MYBOUNDARY==--
```

## Configure the container runtime

You can use the AWS Batch `CONTAINER_RUNTIME` environment variable to configure
the container runtime on a managed node. The following example sets the container runtime to
`containerd` when `bootstrap.sh` runs. For more information, see
[`containerd`](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd "https://kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd") in the _Kubernetes documentation_.

If you are using an optimized `EKS_AL2023` or `EKS_AL2023_NVIDIA`
AMI you do not need to specify the container runtime as only **containerd**
is supported.

###### Note

The `CONTAINER_RUNTIME` environment variable is equivalent to the
`--container-runtime` option of `bootstrap.sh`. For more
information, see [Options](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#options "https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#options") in the _Kubernetes
documentation_.

```
MIME-Version: 1.0
      Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

      --==MYBOUNDARY==
      Content-Type: text/x-shellscript; charset="us-ascii"

      #!/bin/bash
      mkdir -p /etc/aws-batch

      echo CONTAINER_RUNTIME=containerd >> /etc/aws-batch/batch.config

      --==MYBOUNDARY==--
```

## Mount an Amazon EFS volume

You can use launch templates to mount volumes to the node. In the following example, the
`cloud-config`
`packages` and `runcmd` settings are used. For more information, see
[Cloud config
examples](https://cloudinit.readthedocs.io/en/latest/topics/examples.html "https://cloudinit.readthedocs.io/en/latest/topics/examples.html") in the _cloud-init documentation_.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
- amazon-efs-utils

runcmd:
- file_system_id_01=fs-abcdef123
- efs_directory=/mnt/efs

- mkdir -p ${efs_directory}
- echo "${file_system_id_01}:/ ${efs_directory} efs _netdev,noresvport,tls,iam 0 0" >> /etc/fstab
- mount -t efs -o tls ${file_system_id_01}:/ ${efs_directory}

--==MYBOUNDARY==--
```

To use this volume in the job, it must be added in the [eksProperties](../APIReference/API_EksProperties.md "../APIReference/API_EksProperties.md") parameter to
[RegisterJobDefinition](../APIReference/API_RegisterJobDefinition.md "../APIReference/API_RegisterJobDefinition.md"). The following example is a large portion of the job
definition.

```
{
    "jobDefinitionName": "MyJobOnEks_EFS",
    "type": "container",
    "eksProperties": {
        "podProperties": {
            "containers": [
                {
                    "image": "public.ecr.aws/amazonlinux/amazonlinux:2",
                    "command": ["ls", "-la", "/efs"],
                    "resources": {
                        "limits": {
                            "cpu": "1",
                            "memory": "1024Mi"
                        }
                    },
                    "volumeMounts": [
                        {
                            "name": "`efs-volume`",
                            "mountPath": "`/efs`"
                        }
                    ]
                }
            ],
            "volumes": [
                {
                    "name": "`efs-volume`",
                    "hostPath": {
                        "path": "`/mnt/efs`"
                    }
                }
            ]
        }
    }
}
```

In the node, the Amazon EFS volume is mounted in the `/mnt/efs` directory. In the
container for the Amazon EKS job, the volume is mounted in the `/efs`
directory.

## IPv6 support

AWS Batch supports Amazon EKS clusters that have IPv6 addresses. No customizations are required for AWS Batch support.
However, before you begin, we recommend that you review the considerations and conditions that are outlined in
[Assigning IPv6 addresses to pods and
services](../../../eks/latest/userguide/cni-ipv6.md "../../../eks/latest/userguide/cni-ipv6.md") in the _Amazon EKS User Guide_.
