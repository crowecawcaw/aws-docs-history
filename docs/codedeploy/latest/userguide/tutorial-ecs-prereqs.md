# Prerequisites

To complete this tutorial, you must first:

- Complete steps 2 and 3 in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md").
- Create an Application Load Balancer configured with two target groups and one listener. For information
  about creating a load balancer using the console, see [Set up a load balancer,
  target groups, and listeners for CodeDeploy Amazon ECS deployments](deployment-groups-create-load-balancer-for-ecs.md "deployment-groups-create-load-balancer-for-ecs.md"). For information about
  creating a load balancer using the AWS CLI, see [Step 1: Create an Application Load Balancer](../../../AmazonECS/latest/developerguide/create-blue-green.md#create-blue-green-loadbalancer "../../../AmazonECS/latest/developerguide/create-blue-green.md#create-blue-green-loadbalancer") in the _Amazon Elastic Container Service User
  Guide_. When you create your load balancer, make a note of the following for
  this tutorial:
  - The name of your load balancer.
  - The names of your target groups.
  - The port used by your load balancer's listener.

- Create an Amazon ECS cluster and service. For more information, see steps 2, 3, and 4 in
  [Tutorial: Creating a service using a blue/green deployment](../../../AmazonECS/latest/developerguide/create-blue-green.md "../../../AmazonECS/latest/developerguide/create-blue-green.md") in the
  _Amazon Elastic Container Service User Guide_. Make a note of the following for this
  tutorial:
  - The name of your Amazon ECS cluster.
  - The ARN of the the task definition used by your Amazon ECS service.
  - The name of the the container used by your Amazon ECS service.

- Create an Amazon S3 bucket for your AppSpec file.
