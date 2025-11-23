# Recommended GPU Instances

We recommend a GPU instance for most deep learning purposes.
Training new models is faster on a GPU instance than a CPU instance.
You can scale sub-linearly when you have multi-GPU instances or if you use distributed training across many instances with GPUs.

The following instance types support the DLAMI. For information about GPU instance type
options and their uses, see [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") and select **Accelerated
Computing**.

###### Note

The size of your model should be a factor in choosing an instance. If your model exceeds an
instance's available RAM, choose a different instance type with enough memory for
your application.

- [Amazon EC2 P6-B200 Instances](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/") have up to 8 NVIDIA Blackwell B200 GPUs.
- [Amazon EC2 P6-B300 Instances](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/") have up to 8 NVIDIA Blackwell B300 GPUs.
- [Amazon EC2 P6e-GB200 Instances](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/") have up to 4 NVIDIA Blackwell GB200 GPUs.
- [Amazon EC2 P5e Instances](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/") have up to 8 NVIDIA Tesla H200 GPUs.
- [Amazon EC2 P5 Instances](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/") have up to 8 NVIDIA Tesla H100 GPUs.
- [Amazon EC2 P4 Instances](https://aws.amazon.com/ec2/instance-types/p4/ "https://aws.amazon.com/ec2/instance-types/p4/") have up to 8 NVIDIA Tesla A100 GPUs.
- [Amazon EC2 P3 Instances](https://aws.amazon.com/ec2/instance-types/p3/ "https://aws.amazon.com/ec2/instance-types/p3/") have up to 8 NVIDIA Tesla V100 GPUs.
- [Amazon EC2 G3 Instances](https://aws.amazon.com/ec2/instance-types/g3/ "https://aws.amazon.com/ec2/instance-types/g3/") have up to 4 NVIDIA Tesla M60 GPUs.
- [Amazon EC2 G4 Instances](https://aws.amazon.com/ec2/instance-types/g4/ "https://aws.amazon.com/ec2/instance-types/g4/") have up to 4 NVIDIA T4 GPUs.
- [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/") have up to 8 NVIDIA A10G GPUs.
- [Amazon EC2 G6 Instances](https://aws.amazon.com/ec2/instance-types/g6/ "https://aws.amazon.com/ec2/instance-types/g6/") have up to 8 NVIDIA L4 GPUs.
- [Amazon EC2 G6e Instances](https://aws.amazon.com/ec2/instance-types/g6e/ "https://aws.amazon.com/ec2/instance-types/g6e/") have up to 8 NVIDIA L40S Tensor Core GPUs.
- [Amazon EC2 G5g Instances](https://aws.amazon.com/ec2/instance-types/g5g/ "https://aws.amazon.com/ec2/instance-types/g5g/") have Arm64-based [AWS Graviton2 processors](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/").
  DLAMI instances provide tooling to monitor and optimize your GPU processes. For more
  information about monitoring your GPU processes, see [GPU Monitoring and Optimization](tutorial-gpu.md "tutorial-gpu.md").

For specific tutorials on working with G5g instances, see [The ARM64 DLAMI](tutorial-arm64.md "tutorial-arm64.md").

###### Next Up

[Recommended CPU Instances](cpu.md "cpu.md")
