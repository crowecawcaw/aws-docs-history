# Choosing a DLAMI instance type

More generally, consider the following when choosing an instance type for a DLAMI.

- If you're new to deep learning, then an instance with a single GPU might suit your needs.
- If you're budget conscious, then you can use CPU-only instances.
- If you're looking to optimize high performance and cost efficiency for deep learning model inference, then you can use instances with AWS Inferentia chips.
- If you're looking for a high performance GPU instance with an Arm64-based CPU architecture, then you can use the G5g instance type.
- If you're interested in running a pretrained model for inference and predictions, then you
  can attach an [Amazon Elastic Inference](../../../elastic-inference/latest/developerguide/what-is-ei.md "../../../elastic-inference/latest/developerguide/what-is-ei.md") to your Amazon EC2 instance. Amazon Elastic Inference gives you access to an accelerator with a
  fraction of a GPU.
- For high-volume inference services, a single CPU instance with a lot of
  memory, or a cluster of such instances, might be a better solution.
- If you're using a large model with a lot of data or a high batch size, then you need a larger
  instance with more memory. You can also distribute your model to a cluster of GPUs.
  You may find that using an instance with less memory is a better solution for you if
  you decrease your batch size. This may impact your accuracy and training
  speed.
- If you’re interested in running machine learning applications using NVIDIA Collective
  Communications Library (NCCL) requiring high levels of inter-node communications at scale,
  you might want to use [Elastic Fabric Adapter (EFA)](tutorial-efa-launching.md "tutorial-efa-launching.md").
  For more detail on instances, see [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

The following topics provide information about instance type considerations.

###### Important

The Deep Learning AMIs include drivers,
software, or toolkits developed, owned, or provided by NVIDIA Corporation.
You agree to use these NVIDIA drivers, software, or toolkits only on Amazon EC2 instances that include NVIDIA hardware.

###### Topics

- [Pricing for the DLAMI](#pricing "#pricing")
- [DLAMI Region Availability](#region "#region")
- [Recommended GPU Instances](gpu.md "gpu.md")
- [Recommended CPU Instances](cpu.md "cpu.md")
- [Recommended Inferentia Instances](inferentia.md "inferentia.md")
- [Recommended Trainium Instances](trainium.md "trainium.md")

## Pricing for the DLAMI

The deep learning frameworks included in the DLAMI are free, and each has its own open-source
licenses. Although the software included in the DLAMI is free, you still have to
pay for the underlying Amazon EC2 instance hardware.

Some Amazon EC2 instance types are labeled as free. It is possible to run the DLAMI on one
of these free instances. This means that using the DLAMI is entirely free when you only
use that instance's capacity. If you need a more powerful instance with more CPU cores,
more disk space, more RAM, or one or more GPUs, then you need an instance that is not in
the free-tier instance class.

For more information about instance choice and pricing, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

## DLAMI Region Availability

Each Region supports a different range of instance types and often an instance
type has a slightly different cost in different Regions. DLAMIs are not available in
every Region, but it is possible to copy DLAMIs to the Region of your choice. See
[Copying an AMI](../../../AWSEC2/latest/UserGuide/CopyingAMIs.md "../../../AWSEC2/latest/UserGuide/CopyingAMIs.md") for more information. Note the Region selection list and be sure you
pick a Region that's close to you or your customers. If you plan to use more than one
DLAMI and potentially create a cluster, be sure to use the same Region for all of nodes
in the cluster.

For a more info on Regions, visit [Amazon EC2 service endpoints](../../../general/latest/gr/ec2-service.md#ec2_region "../../../general/latest/gr/ec2-service.md#ec2_region").

###### Next Up

[Recommended GPU Instances](gpu.md "gpu.md")
