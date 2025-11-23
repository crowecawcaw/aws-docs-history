# Set up a load balancer in ELB

for CodeDeploy Amazon EC2 deployments

Before you run any blue/green deployment, or an in-place deployment for which you want
to specify an optional load balancer in the deployment group, you must have created at
least one Classic Load Balancer, Application Load Balancer, or Network Load Balancer in ELB. For blue/green deployments, you use that load
balancer to register the instances that make up your replacement environment. Instances
in your original environment can optionally be registered with this same load balancer.
For in-place deployments, the load balancer is used to deregister instances that are
being worked on by CodeDeploy, and reregister them when the work is complete.

CodeDeploy supports blue/green and in-place deployment to Amazon EC2 instances behind muliple
load balancers. For example, assume you have 200 Amazon EC2 instances, where 100 of them are
registered with 2 Classic Load Balancers, and another 100 of them are registered with 4 target groups in
2 Application Load Balancers. In this scenario, CodeDeploy will allow you to do blue/green and in-place
deployments to all 200 instances, even though they're spread across 2 Classic Load Balancers, 2 Application Load Balancers,
and 4 target groups.

CodeDeploy supports up to 10 Classic Load Balancers and 10 target groups, for a total of 20 items.

To configure one or more Classic Load Balancers, follow the instructions in [Tutorial: Create a Classic Load Balancer](../../../elasticloadbalancing/latest/classic/elb-getting-started.md "../../../elasticloadbalancing/latest/classic/elb-getting-started.md") in
_User Guide for Classic Load Balancers_. Note the following:

- In **Step 2: Define Load Balancer**, in **Create LB Inside**, choose the same VPC you selected
  when you created your instances.
- In **Step 5: Register EC2 Instances with Your Load
  Balancer**, select the instances currently in your deployment group
  (in-place deployments) or that you have designated to be in your original
  environment (blue/green deployments).
- In **Step 7: Create and Verify Your Load
  Balancer**, make a note of the DNS address of your load
  balancer.

For example, if you named your load balancer `my-load-balancer`,
your DNS address appears in a format such as
`my-load-balancer-1234567890.us-east-2.elb.amazonaws.com`.
To configure one or more Application Load Balancers, follow the instructions in one of the following
topics:

- [Create an
  Application Load Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md")
- [Tutorial:
  Create an Application Load Balancer using the AWS CLI](../../../elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.md "../../../elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.md")
  To configure one or more Network Load Balancers, follow the instructions in one of the following
  topics:

- [Create a
  Network Load Balancer](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md")
- [Tutorial: Create a Network Load Balancer
  using the AWS CLI](../../../elasticloadbalancing/latest/network/network-load-balancer-cli.md "../../../elasticloadbalancing/latest/network/network-load-balancer-cli.md")
