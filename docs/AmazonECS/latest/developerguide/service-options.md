# Best practices for Amazon ECS service parameters

To ensure that there's no application downtime, the deployment process is as
follows:

1. Start the new application containers while keeping the existing containers
   running.
2. Check that the new containers are healthy.
3. Stop the old containers.
   Depending on your deployment configuration and the amount of free, unreserved space
   in your cluster it may take multiple rounds of this to complete replace all old tasks
   with new tasks.

There are two service configuration options that you can use to modify the
number:

- `minimumHealthyPercent`: 100% (default)

The lower limit on the number of tasks for your service that must remain in
the `RUNNING` state during a deployment. This is a percentage of the
`desiredCount` rounded up to the nearest integer. This parameter
allows you to deploy without using additional cluster capacity.

- `maximumPercent`: 200% (default)

The upper limit on the number of tasks for your service that are allowed in
the `RUNNING` or `PENDING` state during a deployment. This
is a percentage of the `desiredCount` rounded down to the nearest
integer.

**Example: Default configuration options**

Consider the following service that has six tasks, deployed in a cluster that has room
for eight tasks total. The default service configuration options don't allow the deployment
to go below 100% of the six desired tasks.

The deployment process is as follows:

1. The goal is to replace the six tasks.
2. The scheduler starts two new tasks because the default settings require that
   there are six running tasks.

There are now six existing tasks and two new tasks. 3. The scheduler stops two of the existing tasks.

There are now four existing tasks and two new ones. 4. The scheduler starts two additional new tasks.

There are now four existing tasks and four new tasks. 5. The scheduler shuts down two of the existing tasks.

There are now two existing tasks and four new ones. 6. The scheduler starts two additional new tasks.

There are now two existing tasks and six new tasks 7. The scheduler shuts down the last two existing tasks.

There are now six new tasks.
In the above example, if you use the default values for the options, there is a 2.5
minute wait for each new task that starts. Additionally, the load balancer might have to
wait 5 minutes for the old task to stop.

**Example: Modify `minimumHealthyPercent`**

You can speed up the deployment by setting the `minimumHealthyPercent`
value to 50%.

Consider the following service that has six tasks, deployed in a cluster that has room
for eight tasks total. The deployment process is as follows:

1. The goal is to replace six tasks.
2. The scheduler stops three of the existing tasks.

There are still three existing tasks running which meets the
`minimumHealthyPercent` value. 3. The scheduler starts five new tasks.

There are three existing task tasks and five new tasks. 4. The scheduler stops the remaining three existing tasks.

There are five new tasks 5. The scheduler starts the final new tasks.

There are six new tasks.

**Example: Modify cluster free space**

You could also add additional free space so that you can run additional tasks.

Consider the following service that has six tasks, deployed in a cluster that has room for
ten tasks total. The deployment process is as follows:

1. The goal is to replace the existing tasks.
2. The scheduler stops three of the existing tasks,

There are three existing tasks. 3. The scheduler starts six new tasks.

There are the existing tasks and six new tasks 4. The scheduler stops the three existing tasks.

There are six new tasks.

**Recommendations**

Use the following values for the service configuration options when your tasks are
idle for some time and don't have a high utilization rate.

- `minimumHealthyPercent`: 50%
- `maximumPercent`: 200%
