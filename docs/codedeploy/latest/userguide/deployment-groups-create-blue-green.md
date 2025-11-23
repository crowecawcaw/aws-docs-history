# Create a deployment group for an

EC2/On-Premises blue/green deployment (console)

To use the CodeDeploy console to create a deployment group for a blue/green
deployment:

###### Warning

Do not follow these steps if:

- You do not have instances with the CodeDeploy agent installed that you want to
  replace during the blue/green deployment process. To set up your instances,
  follow the instructions in [Working with instances for CodeDeploy](instances.md "instances.md"), and then follow the steps in this
  topic.
- You want to create an application that uses a custom deployment
  configuration, but you have not yet created the deployment configuration.
  Follow the instructions in [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md"), and then follow the
  steps in this topic.
- You do not have a service role that trusts CodeDeploy with, at minimum, the
  trust and permissions described in [Step 2: Create a service role for
  CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"). To create and
  configure a service role, follow the instructions in [Step 2: Create a service role for
  CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"), and then follow
  the steps in this topic.
- You have not created a Classic Load Balancer or an Application Load Balancer in Elastic Load Balancing for the registration
  of the instances in your replacement environment. For more information, see
  [Set up a load balancer in ELB
  for CodeDeploy Amazon EC2 deployments](deployment-groups-create-load-balancer.md "deployment-groups-create-load-balancer.md").

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. On the **Applications** page, choose the name of the
application for which you want to create a deployment group. 4. On your application page, from the **Deployment groups** tab,
choose **Create deployment group**. 5. In **Deployment group name**, enter a name that describes the
deployment group.

###### Note

If you want to use the same settings used in another deployment group
(including the deployment group name, tags, Amazon EC2 Auto Scaling group names, and the
deployment configuration), choose those settings on this page. Although this
new deployment group and the existing deployment group have the same name,
CodeDeploy treats them as separate deployment groups, because they are associated
with separate applications. 6. In **Service role**, choose a service role that grants CodeDeploy
access to your target instance. 7. In **Deployment type** choose
**Blue/green**. 8. In **Environment configuration**, do the following:

    * Select the method to use to provide instances for your replacement
     environment. You have the following options:




    	+ **Automatically copy Amazon EC2 Auto Scaling group**: CodeDeploy
    	 creates an Amazon EC2 Auto Scaling group by copying one you specify.
    	+ **Manually provision instances**: You won't
    	 specify the instances for your replacement environment until you
    	 create a deployment. You must create the instances before you
    	 start the deployment. Instead, here you specify the instances
    	 you want to replace.
    * If you selected **Automatically copy Amazon EC2 Auto Scaling
     group**, optionally select **Add a termination hook to
     Amazon EC2 Auto Scaling groups** to have CodeDeploy install a termination hook
     into your Amazon EC2 Auto Scaling group when you create or update the deployment group.
     When this hook is installed, CodeDeploy will perform termination deployments.
     For more information, see [Enabling
     termination deployments during Amazon EC2 Auto Scaling scale-in events](integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors-hook-enable "integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors-hook-enable").

9. In **Agent configuration with Systems Manager**, specify how you would
   like to install and update the CodeDeploy agent on the instances in your deployment
   group. For more information on the CodeDeploy agent, see [Working with the CodeDeploy agent](../../../en_us/codedeploy/latest/userguide/codedeploy-agent.md "../../../en_us/codedeploy/latest/userguide/codedeploy-agent.md"). For more information about
   Systems Manager, see [What is Systems Manager?](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md")
   1. **Never**: Skip configuring the CodeDeploy installation
      with Systems Manager. Instances must have the agent installed to be used in
      deployments, so only choose this option if you will install the CodeDeploy
      agent another way.
   2. **Only once**: Systems Manager will install the CodeDeploy agent
      once on every instance in your deployment group.
   3. **Now and schedule updates**: Systems Manager will create an
      association with State Manager that installs the CodeDeploy agent on the
      schedule you configure. For more information about State Manager and
      associations, see [About State Manager](../../../systems-manager/latest/userguide/sysman-state-about.md "../../../systems-manager/latest/userguide/sysman-state-about.md").

10. Depending on your choice in step 8, do one of the following:
    - If you chose **Automatically copy Amazon EC2 Auto Scaling group**:
      In **Amazon EC2 Auto Scaling group**, choose or enter the name of the
      Amazon EC2 Auto Scaling group you want to use as a template for the Amazon EC2 Auto Scaling group that
      is created for the instances in your replacement environment. The number
      of currently healthy instances in the Amazon EC2 Auto Scaling group you select is
      created in your replacement environment.
    - If you chose **Manually provision instances**: Select
      **Amazon EC2 Auto Scaling groups**, **Amazon EC2 Auto Scaling
      intances**, or both to specify instances to add to this
      deployment group. Enter Amazon EC2 Auto Scaling tag values or Amazon EC2 Auto Scaling group names to
      identify the instances in your original environment (that is, the
      instances you want to replace or that are running the current
      application revision).

11. In **Load balancer**, select **Enable load
    balancing**, and then from the lists, select the Classic Load Balancers, Application Load Balancer
    target groups, and Network Load Balancer target groups that you want to register your
    replacement Amazon EC2 instances with. Each replacement instance will be registered
    with _all_ the selected Classic Load Balancers and target groups. You can
    select up to 10 Classic Load Balancers and 10 target groups, for a total of 20 items.

Traffic will be rerouted from the original to the replacement instances
according to your chosen **Traffic rerouting** and
**Deployment configuration** settings.

For more information about load balancers for CodeDeploy deployments, see [Integrating CodeDeploy with Elastic Load Balancing](integrations-aws-elastic-load-balancing.md "integrations-aws-elastic-load-balancing.md").

###### Warning

If you are configuring both Amazon EC2 Auto Scaling groups and ELB load balancers in this
deployment group, and you want to [attach the
load balancers to Amazon EC2 Auto Scaling groups](../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md "../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md"), we recommend completing this
attachment _before_ creating the CodeDeploy deployment from
this deployment group. Attempting to complete the attachment after creating
the deployment may cause all the instances to become deregistered from the
load balancers unexpectedly. 12. In **Deployment settings**, review the default options for
rerouting traffic to the replacement environment, which deployment configuration
to use for the deployment, and how instances in the original environment are
handled after the deployment.

If you want to change the settings, continue to the next step. Otherwise, skip
to step 14. 13. To change the deployment settings for the blue/green deployment, choose any of
the following settings.

| Setting                      | Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Traffic rerouting**        | • **Reroute traffic immediately**:<br>As soon as instances in the replacement environment<br>are provisioned and the latest application revision<br>is installed on them, they are registered with the<br>specified load balancers and target groups<br>automatically, causing traffic to be rerouted to<br>them. Instances in the original environment are then<br>deregistered.<br>• **I will choose whether to reroute<br>traffic**: Instances in the replacement<br>environment are not registered with the specified<br>load balancers and target groups unless you manually<br>reroute traffic. If the wait time you specify passes<br>without traffic being rerouted, the deployment<br>status is changed to Stopped. |
| **Deployment configuration** | Choose the rate at which instances in the replacement<br>environment are registered with the load balancers and target groups, such as<br>one at a time or all at once.<br>NoteAfter traffic is successfully routed to the<br>replacement environment, instances in the original<br>environment are deregistered all at once no matter which<br>deployment configuration was selected.<br>For more information, see [Working with deployment configurations in<br>CodeDeploy](deployment-configurations.md "deployment-configurations.md").                                                                                                                                                                                  |
| **Original instances**       | • **Terminate the original instances in the<br>deployment group**: After traffic is<br>rerouted to the replacement environment, the<br>instances that were deregistered from the load<br>balancers and target groups are terminated following the wait period<br>you specify.<br>• **Keep the original instances in the<br>deployment group running**: After traffic<br>is rerouted to the replacement environment, the<br>instances that were deregistered from the load<br>balancers and target groups are kept running.                                                                                                                                                                                                   |

14. (Optional) In **Advanced**, configure options you want to
    include in the deployment, such as Amazon SNS notification triggers, Amazon CloudWatch alarms,
    Amazon EC2 Auto Scaling options, or automatic rollbacks.

For information about specifying advanced options in deployment groups, see
[Configure advanced options
for a deployment group](deployment-groups-configure-advanced-options.md "deployment-groups-configure-advanced-options.md"). 15. Choose **Create deployment group**.
