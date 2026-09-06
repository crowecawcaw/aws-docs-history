

# Troubleshooting Amazon ECS SpotInterruption errors
<a name="spot-interruption-errors"></a>

The `SpotInterruption` error has different reasons for Fargate and EC2s. 

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

## Fargate
<a name="fargate-spot-error"></a>

The `SpotInterruption` error occurs when there is no Fargate Spot capacity or when Fargate takes back Spot capacity.

You can have your tasks run in multiple Availability Zones to allow for more capacity.

## EC2
<a name="ec2-spot-error"></a>

This error occurs when there are no available Spot Instances or EC2 takes back Spot Instance capacity. 

You can have your instances run in multiple Availability Zones to allow for more capacity.