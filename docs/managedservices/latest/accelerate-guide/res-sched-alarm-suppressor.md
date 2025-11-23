# Alarm suppressor in AMS Resource Scheduler

AMS Resource Scheduler comes with a CloudWatch Alarm suppressor, that is deployed as separate Lambda function named `AMSAlarmSuppressor` that
suppresses alarms for instances that are behind an ELB, Application Load Balancer, or Network Load Balancer. The function runs every 5 minutes,
retrieves all alarms present in the account and groups them based on namespace; for example, `AWS/ELB`, `AWS/ApplicationELB`,
`AWS/NetworkELB`. For each group of alarms the suppressor finds the load balancer name and/or target group (for ALB/NLB) from alarm dimensions,
finds the instances that are registered with the load balancer and/or target group, and checks the instance state to discover if the instances are
scheduled by AMS Resource Scheduler. If instances are scheduled by Resource Scheduler, and are stopped by Resource Scheduler, the suppressor then marks
the alarms to disable them. If at least one instance in the registered instance list is running, suppressor marks corresponding alarms to enable the alarms
that are marked for enabling, and disable alarms that are marked for disabling. Logs for this are stored in the `/aws/lambda/AMSAlarmSuppressor` log group.
