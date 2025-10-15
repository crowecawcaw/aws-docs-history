# Concepts and terminology for Deadline Cloud

To help you get started with AWS Deadline Cloud, this topic explains some of its key concepts and
 terminology.



**Budget manager**

Budget manager is part of the Deadline Cloud monitor. Use the budget manager to create and
 manage budgets. You can also use it to limit activities to stay within
 budget.



**Deadline Cloud Client Library**

The Client Library includes a command line interface and library for managing
 Deadline Cloud. Functionality includes submitting job bundles based on the Open Job
 Description specification to Deadline Cloud, downloading job attachment outputs, and
 monitoring your farm using the command line interface.



**Digital content creation application (DCC)**

Digital content creation applications (DCCs) are third-party products where
 you create digital content. Examples of DCCs are Maya,
 Nuke, and Houdini. Deadline Cloud provides job
 submitter integrated plugins for specific DCCs.



**Farm**

A farm is a where your project resources are located. It consists of queues
 and fleets.



**Fleet**

A fleet is a group of worker nodes that do the rendering. Worker nodes process
 jobs. A fleet can be associated to multiple queues, and a queue can be
 associated to multiple fleets.



**Instance**

Fleets use instances for CPU resources. An instance is an Amazon EC2 performance 
 instance. Deadline Cloud uses On-Demand and Spot instances. 



**On-Demand instance**

On-Demand instances are priced by the second, have no long-term commitment, 
 and will not be interrupted.



**Spot instance**

Spot instances are unreserved capacity that you can use at a discounted price,
 but may be interrupted by On-Demand requests.



**Wait and Save**

The Wait and Save feature provides delayed job scheduling for lower cost and can
 be interrupted by On-Demand and Spot requests. Wait and Save is only available
 within Deadline Cloud service-managed fleets.


Wait and Save is for managing the execution of visual computing workloads in 
 AWS Deadline Cloud. See [AWS service terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/")
 for details.



**Job**

A job is a rendering request. Users submit jobs. Jobs contain specific job
 properties that are outlined as steps and tasks.



**Job attachments**

A job attachment is a Deadline Cloud feature that you can use to manage inputs and
 outputs for jobs. Job files are uploaded as job attachments during the rendering
 process. These files can be textures, 3D models, lighting rigs, and other
 similar items.



**Job priority**

Job priority is the approximate order that Deadline Cloud processes a job in a queue.
 You can set the job priority between 1 and 100, jobs with a higher number
 priority are generally processed first. Jobs with the same priority are
 processed in the order received.



**Job properties**

Job properties are settings that you define when submitting a render job. Some
 examples include frame range, output path, job attachments, renderable camera,
 and more. The properties vary based on the DCC that the render is submitted
 from.



**Job template**

A job template defines the runtime environment and all processes that run as
 part of a Deadline Cloud job.



**Queue**

A queue is where submitted jobs are located and scheduled to be rendered. A
 queue must be associated with a fleet to create a successful render. A queue can
 be associated with multiple fleets.



**Queue-fleet association**

When a queue is associated with a fleet, there is a queue-fleet association.
 Use an association to schedule workers from a fleet to jobs in that queue. You
 can start and stop associations to control scheduling of work.



**Session**

A session is an ephemeral runtime environment on a worker host created to run a
 set of tasks from the same job. The session ends when the worker host finishes
 running tasks for that job.


The session provides a way to configure the environment with resources shared
 across multiple task runs, such as defining environment variables or starting
 a background process or container.



**Session action**

A session action is a discrete unit of work executed by a worker within 
 a session. It can encompass the core task run operations of a task, or it might 
 include preparatory steps such as environment setup and post-execution processes
 like tear-down and cleanup.



**Step**

A step is one particular process to run in the job.



**Deadline Cloud submitter**

A Deadline Cloud submitter is a digital content creation (DCC) plugin. Artists use it
 to submit jobs from a third-party DCC interface that they are familiar
 with.



**Tags**

A tag is a label that you can assign to an AWS resource. Each tag consists
 of a key and an optional value that you define.


With tags, you can categorize your AWS resources in different ways. For
 example, you could define a set of tags for your accountâs Amazon EC2 instances that
 help you track each instanceâs owner and stack level.


You can also categorize your AWS resources by purpose, owner, or
 environment. This approach is useful when you have many resources of the same
 type. You can quickly identify a specific resources based on the tags that
 you've assigned to it.



**Task**

A task is a single component of a render step.



**Usage-based licensing (UBL)**

Usage-based licensing (UBL) is an on-demand licensing model that is available
 for select third-party products. This model is pay as your go, and you are
 charged for the number of hours and minutes that you use.



**Usage explorer**

Usage explorer is a feature of Deadline Cloud monitor. It provides an approximate estimate of
 your costs and usage.



**Worker**

Workers belong to fleets and run Deadline Cloud assigned tasks to complete steps and
 jobs. Workers store the logs from task operations in Amazon CloudWatch Logs. Workers can also
 use the job attachments feature to sync inputs and outputs to an Amazon Simple Storage Service (Amazon S3)
 bucket.
