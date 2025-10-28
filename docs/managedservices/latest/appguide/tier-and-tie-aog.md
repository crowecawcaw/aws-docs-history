# Tier and Tie App Deployments in AMS

A Tier and Tie deployment is where you create, configure, and deploy the resources of
a stack independently using separate RFCs, and use the IDs of the stack components as
you progress to associate them with each other.

For example, to deploy a _high availability_
(redundant) website behind a load balancer, and a database, using a Tier and Tie
approach, submit RFCs for a database, and a load balancer, and two EC2
instances or an Auto Scaling group, and configure the EC2 instances or Auto Scaling
group with the ID of the ELB that you created.

After the resources deploy, you can submit a security group create change to
allow the resources to talk to the database. For details about creating security groups, see
[Create Security
Group](../ctref/deployment-advanced-security-group-create.md "../ctref/deployment-advanced-security-group-create.md").
