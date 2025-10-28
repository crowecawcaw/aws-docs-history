# Amazon ECS standalone tasks

You can run your application as a task when you have an application that performs some
work, and then stops, for example a batch process. If you want to run a task one time, you
can use the console, AWS CLI, APIs, or SDKs.

If you need to run your application on a rate-based, cron-based, or one-time schedule, you
can create schedule using EventBridge Scheduler.

## Task workflow

When you launch Amazon ECS tasks (standalone tasks or by Amazon ECS services), a task is created
and initially moved to the `PROVISIONING` state. When a task is in the
`PROVISIONING` state, neither the task nor the containers exist because
Amazon ECS needs to find compute capacity for placing the task.

Amazon ECS selects the appropriate compute capacity for your task based on your launch type
or capacity provider configuration. You can use capacity providers and capacity provider
strategies with both the Fargate and EC2s. With Fargate, you don’t have to think about provisioning, configuring,
and scaling of your cluster capacity. Fargate takes care of all infrastructure
management for your tasks. For EC2, you can either manage your cluster
capacity by registering Amazon EC2 instances to your cluster, or you can use cluster auto
scaling to simplify your compute capacity management. Cluster auto scaling takes care of
dynamically scaling your cluster capacity, so that you can focus on running tasks. Amazon ECS
determines where to place the task based on the requirements you specify in the task
definition, such as CPU and memory, as well your placement constraints and strategies. For more information, see, [How Amazon ECS places tasks on container instances](task-placement.md "task-placement.md").

If you use a capacity provider with managed scaling enabled, tasks that can't be
started due to a lack of compute capacity are moved to the `PROVISIONING`
state rather than failing immediately. After finding the capacity for placing your task,
Amazon ECS provisions the necessary attachments (for example, Elastic Network Interfaces
(ENIs) for tasks in `awsvpc` mode). It uses the Amazon ECS container agent to pull
your container images, and then start your containers. After the provisioning completes
and the relevant containers have launched, Amazon ECS moves the task into
`RUNNING` state. For information about the task states, see [Amazon ECS task lifecycle](task-lifecycle-explanation.md "task-lifecycle-explanation.md").
