# Amazon ECS blue/green deployments

A blue/green deployment is a release methodology that reduces downtime and risk by running two identical production environments called blue and green. With Amazon ECS blue/green deployments, you can validate new service revisions before directing production traffic to them. This approach provides a safer way to deploy changes with the ability to quickly roll back if needed.

## Benefits

The following are benefits of using blue/green deployments:

- Reduces risk through testing with production traffic before switching production.
  You can validate the new deployment with test traffic before directing production
  traffic to it.
- Zero downtime deployments. The production environment remains available throughout the deployment process, ensuring continuous service availability.
- Easy rollback if issues are detected. If problems arise with the green deployment, you can quickly revert to the blue deployment without extended service disruption.
- Controlled testing environment. The green environment provides an isolated space to test new features with real traffic patterns before full deployment.
- Predictable deployment process. The structured approach with defined lifecycle stages makes deployments more consistent and reliable.
- Automated validation through lifecycle hooks. You can implement automated tests at various stages of the deployment to verify functionality.

## Terminology

The following are Amazon ECS blue/green deployment terms:

- Bake time - The duration when both blue and green service revisions are running simultaneously after the production traffic has shifted.
- Blue deployment - The current production service revision that you want to replace.
- Green deployment - The new service revision that you want to deploy.
- Lifecycle stages - A series of events in the deployment operation, such as "after production traffic shift".
- Lifecycle hook - A Lambda function that verifies the deployment at a specific lifecycle stage.
- Listener - A ELB resource that checks for connection requests using the
  protocol and port that you configure. The rules that you define for a listener
  determine how Amazon ECS routes requests to its registered targets.
- Rule - An ELB resource associated with a listener. A rule defines how requests are routed and consists of an action, condition, and priority.
- Target group - An ELB resource used to route requests to one or more registered targets (for example, EC2 instances). When you create a listener, you specify a target group for its default action. Traffic is forwarded to the target group specified in the listener rule.
- Traffic shift - The process Amazon ECS uses to shift traffic from the blue
  deployment to the green deployment. For Amazon ECS blue/green deployments, all
  traffic is shifted from the blue service to the green service at
  once.

## Considerations

Consider the following when choosing a deployment type:

- Resource usage: Blue/green deployments temporarily run both the blue and green service revisions simultaneously, which may double your resource usage during deployments.
- Deployment monitoring: Blue/green deployments provide more detailed deployment status information, allowing you to monitor each stage of the deployment process.
- Rollback: Blue/green deployments make it easier to roll back to the previous version if issues are detected, as the blue revision is kept running until the bake time expires.
- Network Load Balancer lifecycle hooks: If you use a Network Load Balancer for blue/green deployments, there is an additional 10 minutes for each lifecycle hook. This is because Amazon ECS makes sure that it is safe to shift traffic.
