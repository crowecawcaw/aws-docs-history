# Instance Types for Built-in

Algorithms

Most Amazon SageMaker AI algorithms have been engineered to take advantage of GPU computing
for training. Despite higher per-instance costs, GPUs train more quickly, making them
more cost effective. Exceptions are noted in this guide.

To learn about the supported EC2 instances, see [Instance details](https://aws.amazon.com/sagemaker-ai/pricing/#Instance_details "https://aws.amazon.com/sagemaker-ai/pricing/#Instance_details").

The size and type of data can have a great effect on which hardware configuration
is most effective. When the same model is trained on a recurring basis, initial
testing across a spectrum of instance types can discover configurations that are
more cost-effective in the long run. Additionally, algorithms that train most
efficiently on GPUs might not require GPUs for efficient inference. Experiment to
determine the most cost effectiveness solution. To get an automatic instance
recommendation or conduct custom load tests, use [Amazon SageMaker Inference Recommender](inference-recommender.md "inference-recommender.md").

For more information on SageMaker AI hardware specifications, see [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/ai/pricing/ "https://aws.amazon.com/sagemaker/ai/pricing/").

**UltraServers**

UltraServers connect multiple Amazon EC2 instances using a low-latency,
high-bandwidth accelerator interconnect. They are built to handle large-scale AI/ML workloads
that require significant processing power. For more information, see [Amazon EC2 UltraServers](https://aws.amazon.com/ec2/ultraservers/ "https://aws.amazon.com/ec2/ultraservers/"). To get started
with UltraServers, see [Reserve training plans for your training jobs or HyperPod clusters](reserve-capacity-with-training-plans.md "reserve-capacity-with-training-plans.md").

To get started with UltraServers on Amazon SageMaker AI,
[create a training plan](reserve-capacity-with-training-plans.md "reserve-capacity-with-training-plans.md"). Once your UltraServer is available in the training plan,
create a training job with the AWS Management Console, Amazon SageMaker AI API, or AWS CLI. Remember to specify the UltraServer
instance type that you purchased in the training plan.

An UltraServer can run one or multiple jobs at a time. UltraServers groups instances together, which
gives you some flexibility in terms of how to allocate your UltraServer capacity in your organization. As you configure
your jobs, also remember your organization's data security guidelines, as instances in one UltraServer
can access data for another job in another instance on the same UltraServer.

If you run into hardware failures in the UltraServer, SageMaker AI automatically tries to resolve the issue.
As SageMaker AI investigates and resolves the issue, you might receive notifications and actions through AWS Health Events
or AWS Support.

Once your training job finishes, SageMaker AI stops the instances, but they remain available in your training plan
if the plan is still active. To keep an instance in an UltraServer running after a job finishes, you can use
[managed warm pools](train-warm-pools.md "train-warm-pools.md").

If your training plan has enough capacity, you can even run training jobs across multiple UltraServers. By default, each
UltraServer comes with 18 instances, comprising of 17 instances and 1 spare instance. If you need more instances, you must buy more UltraServers.
When creating a training job, you can configure how jobs are placed across
UltraServers using the `InstancePlacementConfig` parameter.

If you don't configure job placement, SageMaker AI automatically allocates jobs to instances within your
UltraServer. This default strategy is based on best effort that prioritizes filling all of the instances
in a single UltraServer before using a different UltraServer. For example, if you request 14 instances and have 2
UltraServers in your training plan, SageMaker AI uses all of the instances in the first UltraServer.
If you requested 20 instances and have 2 UltraServers in your training plan, SageMaker AI will
will use all 17 instances in the first UltraServer and then use 3 from the second UltraServer. Instances
within an UltraServer use NVLink to communicate, but individual UltraServers use Elastic Fabric Adapter (EFA),
which might affect model training performance.
