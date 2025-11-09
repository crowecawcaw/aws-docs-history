# Run GPU jobs

GPU jobs help you to run jobs that use an instance's GPUs.

The following Amazon EC2 GPU-based instance types are supported. For more information, see [Amazon EC2 G3 Instances](https://aws.amazon.com/ec2/instance-types/g3/ "https://aws.amazon.com/ec2/instance-types/g3/"), [Amazon EC2 G4 Instances](https://aws.amazon.com/ec2/instance-types/g4/ "https://aws.amazon.com/ec2/instance-types/g4/"), [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/"),[Amazon EC2 G6 Instances](https://aws.amazon.com/ec2/instance-types/g6/ "https://aws.amazon.com/ec2/instance-types/g6/") , [Amazon EC2 P2 Instances](https://aws.amazon.com/ec2/instance-types/p2/ "https://aws.amazon.com/ec2/instance-types/p2/"), [Amazon EC2 P3 Instances](https://aws.amazon.com/ec2/instance-types/p3/ "https://aws.amazon.com/ec2/instance-types/p3/"), [Amazon EC2 P4d Instances](https://aws.amazon.com/ec2/instance-types/p4/ "https://aws.amazon.com/ec2/instance-types/p4/"), [Amazon EC2 P5 Instances](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/"), [Amazon EC2 P6 Instances](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/"), [Amazon EC2 Trn1 Instances](https://aws.amazon.com/ec2/instance-types/trn1/ "https://aws.amazon.com/ec2/instance-types/trn1/"), [Amazon EC2 Trn2 Instances](https://aws.amazon.com/ec2/instance-types/trn2/ "https://aws.amazon.com/ec2/instance-types/trn2/"), [Amazon EC2 Inf1 Instances](https://aws.amazon.com/ec2/instance-types/inf1/ "https://aws.amazon.com/ec2/instance-types/inf1/"), [Amazon EC2 Inf2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/ "https://aws.amazon.com/ec2/instance-types/inf2/"), [Amazon EC2 Dl1 Instances](https://aws.amazon.com/ec2/instance-types/dl1/ "https://aws.amazon.com/ec2/instance-types/dl1/"), and [Amazon EC2 Dl2 Instances](https://aws.amazon.com/ec2/instance-types/dl2q/ "https://aws.amazon.com/ec2/instance-types/dl2q/").

| Instance type    | GPUs | GPU memory | vCPUs | Memory   | Network bandwidth |
| ---------------- | ---- | ---------- | ----- | -------- | ----------------- |
| g3s.xlarge       | 1    | 8 GiB      | 4     | 30.5 GiB | 10 Gbps           |
| g3.4xlarge       | 1    | 8 GiB      | 16    | 122 GiB  | Up to 10 Gbps     |
| g3.8xlarge       | 2    | 16 GiB     | 32    | 244 GiB  | 10 Gbps           |
| g3.16xlarge      | 4    | 32 GiB     | 64    | 488 GiB  | 25 Gbps           |
| g4dn.xlarge      | 1    | 16 GiB     | 4     | 16 GiB   | Up to 25 Gbps     |
| g4dn.2xlarge     | 1    | 16 GiB     | 8     | 32 GiB   | Up to 25 Gbps     |
| g4dn.4xlarge     | 1    | 16 GiB     | 16    | 64 GiB   | Up to 25 Gbps     |
| g4dn.8xlarge     | 1    | 16 GiB     | 32    | 128 GiB  | 50 Gbps           |
| g4dn.12xlarge    | 4    | 64 GiB     | 48    | 192 GiB  | 50 Gbps           |
| g4dn.16xlarge    | 1    | 16 GiB     | 64    | 256 GiB  | 50 Gbps           |
| g5.xlarge        | 1    | 24 GiB     | 4     | 16 GiB   | Up to 10 Gbps     |
| g5.2xlarge       | 1    | 24 GiB     | 8     | 32 GiB   | Up to 10 Gbps     |
| g5.4xlarge       | 1    | 24 GiB     | 16    | 64 GiB   | Up to 25 Gbps     |
| g5.8xlarge       | 1    | 24 GiB     | 32    | 128 GiB  | 25 Gbps           |
| g5.16xlarge      | 1    | 24 GiB     | 64    | 256 GiB  | 25 Gbps           |
| g5.12xlarge      | 4    | 96 GiB     | 48    | 192 GiB  | 40 Gbps           |
| g5.24xlarge      | 4    | 96 GiB     | 96    | 384 GiB  | 50 Gbps           |
| g5.48xlarge      | 8    | 192 GiB    | 192   | 768 GiB  | 100 Gbps          |
| g5g.xlarge       | 1    | 16 GiB     | 4     | 8 GiB    | Up to 10 Gbps     |
| g5g.2xlarge      | 1    | 16 GiB     | 8     | 16 GiB   | Up to 10 Gbps     |
| g5g.4xlarge      | 1    | 16 GiB     | 16    | 32 GiB   | Up to 10 Gbps     |
| g5g.8xlarge      | 1    | 16 GiB     | 32    | 64 GiB   | 12 Gbps           |
| g5g.16xlarge     | 2    | 32 GiB     | 64    | 128 GiB  | 25 Gbps           |
| g5g.metal        | 2    | 32 GiB     | 64    | 128 GiB  | 25 Gbps           |
| g6.xlarge        | 1    | 24 GiB     | 4     | 16 GiB   | Up to 10 Gbps     |
| g6.2xlarge       | 1    | 24 GiB     | 8     | 32 GiB   | Up to 10 Gbps     |
| g6.4xlarge       | 1    | 24 GiB     | 16    | 64 GiB   | Up to 25 Gbps     |
| g6.8xlarge       | 1    | 24 GiB     | 32    | 128 GiB  | 25 Gbps           |
| g6.16xlarge      | 1    | 24 GiB     | 64    | 256 GiB  | 25 Gbps           |
| g6.12xlarge      | 4    | 96 GiB     | 48    | 192 GiB  | 40 Gbps           |
| g6.24xlarge      | 4    | 96 GiB     | 96    | 384 GiB  | 50 Gbps           |
| g6.48xlarge      | 8    | 192 GiB    | 192   | 768 GiB  | 100 Gbps          |
| g6e.xlarge       | 1    | 48 GiB     | 4     | 32 GiB   | Up to 20 Gbps     |
| g6e.2xlarge      | 1    | 48 GiB     | 8     | 64 GiB   | Up to 20 Gbps     |
| g6e.4xlarge      | 1    | 48 GiB     | 16    | 128 GiB  | 20 Gbps           |
| g6e.8xlarge      | 1    | 48 GiB     | 32    | 256 GiB  | 25 Gbps           |
| g6e.16xlarge     | 1    | 48 GiB     | 64    | 512 GiB  | 35 Gbps           |
| g6e.12xlarge     | 4    | 192 GiB    | 48    | 384 GiB  | 100 Gbps          |
| g6e.24xlarge     | 4    | 192 GiB    | 96    | 768 GiB  | 200 Gbps          |
| g6e.48xlarge     | 8    | 384 GiB    | 192   | 1536 GiB | 400 Gbps          |
| gr6.4xlarge      | 1    | 24 GiB     | 16    | 128 GiB  | Up to 25 Gbps     |
| gr6.8xlarge      | 1    | 24 GiB     | 32    | 256 GiB  | 25 Gbps           |
| p2.xlarge        | 1    | 12 GiB     | 4     | 61 GiB   | High              |
| p2.8xlarge       | 8    | 96 GiB     | 32    | 488 GiB  | 10 Gbps           |
| p2.16xlarge      | 16   | 192 GiB    | 64    | 732 GiB  | 20 Gbps           |
| p3.2xlarge       | 1    | 16 GiB     | 8     | 61 GiB   | Up to 10 Gbps     |
| p3.8xlarge       | 4    | 64 GiB     | 32    | 244 GiB  | 10 Gbps           |
| p3.16xlarge      | 8    | 128 GiB    | 64    | 488 GiB  | 25 Gbps           |
| p3dn.24xlarge    | 8    | 256 GiB    | 96    | 768 GiB  | 100 Gbps          |
| p4d.24xlarge     | 8    | 320 GiB    | 96    | 1152 GiB | 400 Gbps          |
| p4de.24xlarge    | 8    | 640 GiB    | 96    | 1152 GiB | 400 Gbps          |
| p5.48xlarge      | 8    | 640 GiB    | 192   | 2 TiB    | 3200 Gbps         |
| p5e.48xlarge     | 8    | 1128 GiB   | 192   | 2 TiB    | 3200 Gbps         |
| p5en.48xlarge    | 8    | 1128 GiB   | 192   | 2 TiB    | 3200 Gbps         |
| p6-b200.48xlarge | 8    | 1440 GiB   | 192   | 2 TiB    | 100 Gbps          |
| trn1.2xlarge     | 1    | 32 GiB     | 8     | 32 GiB   | Up to 12.5 Gbps   |
| trn1.32xlarge    | 16   | 512 GiB    | 128   | 512 GiB  | 800 Gbps          |
| trn1n.32xlarge   | 16   | 512 GiB    | 128   | 512 GiB  | 1600 Gbps         |
| trn2.48xlarge    | 16   | 1.5 TiB    | 192   | 2 TiB    | 3.2 Tbps          |
| inf1.xlarge      | 1    | 8 GiB      | 4     | 8 GiB    | Up to 25 Gbps     |
| inf1.2xlarge     | 1    | 8 GiB      | 8     | 16 GiB   | Up to 25 Gbps     |
| inf1.6xlarge     | 4    | 32 GiB     | 24    | 48 GiB   | 25 Gbps           |
| inf1.24xlarge    | 16   | 128 GiB    | 96    | 192 GiB  | 100 Gbps          |
| inf2.xlarge      | 1    | 32 GiB     | 4     | 16 GiB   | Up to 15 Gbps     |
| inf2.8xlarge     | 1    | 32 GiB     | 32    | 128 GiB  | Up to 25 Gbps     |
| inf2.24xlarge    | 6    | 192 GiB    | 96    | 384 GiB  | 50 Gbps           |
| inf2.48xlarge    | 12   | 384 GiB    | 192   | 768 GiB  | 100 Gbps          |
| dl1.24xlarge     | 8    | 256 GiB    | 96    | 768 GiB  | 400 Gbps          |
| dl2q.24xlarge    | 8    | 128 GiB    | 96    | 768 GiB  | 100 Gbps          |

###### Note

For GPU jobs AWS Batch only supports instance types that have NVIDIA GPUs. For example, the
[`G4ad`](https://aws.amazon.com/ec2/instance-types/g4/#Amazon_EC2_G4ad_instances "https://aws.amazon.com/ec2/instance-types/g4/#Amazon_EC2_G4ad_instances") family is not supported for GPU scheduling. You can still use [`G4ad`](https://aws.amazon.com/ec2/instance-types/g4/#Amazon_EC2_G4ad_instances "https://aws.amazon.com/ec2/instance-types/g4/#Amazon_EC2_G4ad_instances") on AWS Batch by defining only the vcpu and memory requirements in the
job definition, then accessing the host GPUs directly through customization in an Amazon EC2 [launch template user data](launch-templates.md#lt-user-data.title "launch-templates.md#lt-user-data.title") with an Amazon ECS or Amazon EKS compute
optimized AMI, or a customized AMI for using AMD GPUs.

Instance types that use an ARM64 architecture are supported for GPU jobs on custom AMIs
provided to AWS Batch or Amazon EC2 user data to access the GPUs by customized code and configurations.
For example, the [`G5g`](https://aws.amazon.com/ec2/instance-types/g5g/ "https://aws.amazon.com/ec2/instance-types/g5g/")
instance family.

The [resourceRequirements](job_definition_parameters.md#ContainerProperties-resourceRequirements "job_definition_parameters.md#ContainerProperties-resourceRequirements") parameter for the job
definition specifies the number of GPUs to be pinned to the container. This number of GPUs isn't available to any
other job that runs on that instance for the duration of that job. All instance types in a compute environment that
run GPU jobs must be from the `p3`, `p4`, `p5`, `p6`, `g3`, `g3s`,
`g4`, `g5`, or `g6` instance families. If this isn't done a GPU job might get stuck
in the `RUNNABLE` status.

Jobs that don't use the GPUs can be run on GPU instances. However, they might cost more to run on the GPU
instances than on similar non-GPU instances. Depending on the specific vCPU, memory, and time needed, these non-GPU
jobs might block GPU jobs from running.

###### Topics

- [Create a GPU-based Kubernetes cluster on Amazon EKS](create-gpu-cluster-eks.md "create-gpu-cluster-eks.md")
- [Create an Amazon EKS GPU job definition](create-eks-gpu-job-definition.md "create-eks-gpu-job-definition.md")
- [Run a GPU job in your Amazon EKS cluster](run-gpu-job-eks-cluster.md "run-gpu-job-eks-cluster.md")
