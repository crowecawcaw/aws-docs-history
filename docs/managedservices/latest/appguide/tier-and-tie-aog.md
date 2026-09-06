

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Tier and Tie App Deployments in AMS
<a name="tier-and-tie-aog"></a>

A Tier and Tie deployment is where you create, configure, and deploy the resources of a stack independently using separate RFCs, and use the IDs of the stack components as you progress to associate them with each other.

For example, to deploy a *high availability* (redundant) website behind a load balancer, and a database, using a Tier and Tie approach, submit RFCs for a database, and a load balancer, and two EC2 instances or an Auto Scaling group, and configure the EC2 instances or Auto Scaling group with the ID of the ELB that you created.

After the resources deploy, you can submit a security group create change to allow the resources to talk to the database. For details about creating security groups, see [Create Security Group](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-security-group-create.html).