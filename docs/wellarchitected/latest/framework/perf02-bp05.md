

# PERF02-BP05 Use optimized hardware-based compute accelerators

 Some workloads run far faster on specialized hardware than on a general-purpose processor. Accelerators, such as GPUs and purpose-built chips, handle massively parallel work such as model training or media processing at a throughput CPUs cannot match. They cost more than general-purpose processors and only pay off when the application offloads work to them and keeps them busy. 

 **Desired outcome:** 
+  You run workloads that benefit from parallel hardware on accelerators, and you keep CPU-appropriate work on CPUs. 
+  You benchmark accelerated instances against general-purpose options before committing, and you can show the accelerator wins on performance or cost. 
+  You monitor accelerator utilization as a distinct signal, not just CPU and memory. 

 **Common anti-patterns:** 
+  Teams have not benchmarked a general-purpose instance against a purpose-built one that could deliver higher performance at lower cost. 
+  Teams do not monitor GPU utilization, so they cannot tell whether the hardware is being used. 
+  Teams leave accelerated instances running after the job finishes. 

 **Benefits of establishing this best practice:** 
+  Suitable workloads complete faster because parallel hardware handles work CPUs process serially. 
+  Cost per unit of work drops when a purpose-built accelerator outperforms a larger general-purpose fleet. 
+  Utilization stays high because accelerators run only while there is work for them. 
+  Performance keeps improving as you adopt optimized libraries and newer accelerator generations. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 GPUs excel at the massively parallel arithmetic behind rendering, transcoding, and machine learning. You can configure field programmable gate arrays (FPGAs) for custom operations, such as data pattern matching. Purpose-built chips target a single domain, such as machine learning training or inference, and trade generality for efficiency. 

 Before choosing an accelerator, benchmark your workload on general-purpose and accelerated instances to compare performance and cost. 

 Accelerated workloads such as rendering, transcoding, and training tend to be spiky, with intense use followed by idle time. For this pattern, consider alternatives to on-demand capacity, such as [Amazon EC2 Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html). 

 An accelerator only helps if the software uses it. Gains depend on drivers, runtime libraries, and application code that offload the right operations to the hardware. Keep them current and tune I/O so data reaches the accelerator without stalling. 

 On AWS, [accelerated computing instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html) provide GPUs and FPGAs. Purpose-built chips such as [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) and [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) target machine learning training and inference. The [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html) collects GPU utilization and memory metrics that standard instance metrics do not expose. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Confirm your application supports acceleration:** Verify that the workload has parallelizable operations and that its frameworks or libraries can offload them to an accelerator. 

1.  **Identify the accelerated instances that fit:** Match your requirements to the available [accelerated computing instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html), and benchmark the candidates against a general-purpose baseline on both performance and cost. 

1.  **Use purpose-built hardware where it applies:** For machine learning, evaluate [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) for training and [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) for inference, which target these tasks specifically. 

1.  **Collect accelerator utilization metrics:** Track accelerator-specific signals, such as utilization\_gpu and utilization\_memory with configuring the [CloudWatch agent for NVIDIA GPUs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html), so you can tell whether the hardware is actually being used. 

1.  **Optimize code, drivers, and settings:** Tune the application, I/O, and hardware settings so the accelerator stays fully fed, and keep drivers and performance libraries current. Check out [NVIDIA drivers for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html) and [GPU monitoring and optimization in the Deep Learning AMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu.html). 

1.  **Release capacity when idle:** Automate teardown of accelerated instances when the job completes, so expensive hardware does not run without work. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF02-BP01 Select the best compute options for your workload](perf02-bp01.md) 
+  [PERF02-BP02 Collect compute-related metrics](perf02-bp02.md) 
+  [PERF02-BP03 Configure and right-size compute resources](perf02-bp03.md) 

 **Related documents:** 
+  [Accelerated computing with Amazon EC2](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html) 
+  [Working with GPUs on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html) 
+  [How do I choose the appropriate Amazon EC2 instance type for my workload?](https://repost.aws/knowledge-center/ec2-instance-choose-type-for-workload) 

 **Related videos:** 
+  [AWS re:Invent 2024 - AWS accelerated computing enables customer success with generative AI](https://www.youtube.com/watch?v=8TNKVXfIUCo) 