# Use scheduled actions to scale Amazon ECS services

With scheduled scaling, you can set up automatic scaling for your application
based on predictable load changes by creating scheduled actions that increase or
decrease the number of tasks at specific times. This allows you to scale your
application proactively to match predictable load changes.

These scheduled scaling actions allow you to optimize costs and performance. Your
application has a sufficient number of tasks to handle the mid-week traffic peak, but
does not over-provision the number of tasks at other times.

You can use scheduled scaling and scaling policies together to get the benefits of
proactive and reactive approaches to scaling. After a scheduled scaling action runs, the
scaling policy can continue to make decisions about whether to further scale the number
of tasks. This helps you ensure that you have a sufficient number of tasks to handle the
load for your application. While your application scales to match demand, current
capacity must fall within the minimum and maximum number of tasks that was set by your
scheduled action.

You can configure schedule scaling using the AWS CLI. For more information about scheduled scaling, see [Scheduled Scaling](../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md "../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md") in the _Application Auto Scaling User
Guide_.
