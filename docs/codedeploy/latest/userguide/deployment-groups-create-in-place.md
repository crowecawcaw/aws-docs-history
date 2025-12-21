# Create a deployment group for an

in-place deployment (console)

To use the CodeDeploy console to create a deployment group for an in-place
deployment:

###### Warning

Do not follow these steps if:

- You have not prepared your instances to be used in the first CodeDeploy
  deployment of an application. To set up your instances, follow the
  instructions in [Working with instances for CodeDeploy](instances.md "instances.md"), and
  then follow the steps in this topic.
- You want to create a deployment group that uses a custom deployment
  configuration, but you have not yet created the deployment configuration.
  Follow the instructions in [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md"), and then follow the
  steps in this topic.
- You do not have a service role that trusts CodeDeploy with, at minimum, the
  trust and permissions described in [Step 2: Create a service role for
  CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"). To create and
  configure a service role, follow the instructions in [Step 2: Create a service role for
  CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"), and then follow
  the steps in this topic.
- You want to select a Classic Load Balancer, Application Load Balancer, or Network Load Balancer in ELB for the in-place
  deployment, but have not yet created it.

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. On the **Applications** page, choose the name of the
application for which you want to create a deployment group. 4. On your application page, from the **Deployment groups** tab,
choose **Create deployment group**. 5. In **Deployment group name**, enter a name that describes the
deployment group.

###### Note

If you want to use the same settings used in another deployment group
(including the deployment group name; tags, Amazon EC2 Auto Scaling group names, or both;
and the deployment configuration), specify those settings on this page.
Although this new deployment group and the existing deployment group have
the same name, CodeDeploy treats them as separate deployment groups, because they
are each associated with separate applications. 6. In **Service role**, choose a service role that grants CodeDeploy
access to your target instance. 7. In **Deployment type**, choose
**In-place**. 8. In **Environment configuration**, do the following:

    1. If you want to deploy your application to an Amazon EC2 Auto Scaling group, select
     **Amazon EC2 Auto Scaling groups**, and then choose the name of an
     Amazon EC2 Auto Scaling group to deploy your application revision to. When new Amazon EC2
     instances are launched as part of an Amazon EC2 Auto Scaling group, CodeDeploy can deploy
     your revisions to the new instances automatically. You can add up to 10
     Amazon EC2 Auto Scaling groups to a deployment group. For more information, see [Integrating CodeDeploy with Amazon EC2 Auto Scaling](integrations-aws-auto-scaling.md "integrations-aws-auto-scaling.md").
    2. If you selected **Amazon EC2 Auto Scaling groups**, optionally
     select **Add a termination hook to Auto Scaling groups** to
     have CodeDeploy install a termination hook into your Auto Scaling group when you
     create or update the deployment group. When this hook is installed,
     CodeDeploy will perform termination deployments. For more information, see
     [Enabling
     termination deployments during Auto Scaling scale-in events](integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors-hook-enable "integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors-hook-enable").
    3. If you want to tag your instances, select **Amazon EC2
     instances** or **On-premises instances**.
     In the **Key** and **Value** fields,
     enter the values of the key-value pair you used to tag the instances.
     You can tag up to 10 key-value pairs in a single tag group.


    	1. You can use wildcards in the **Value** field
    	 to identify all instances tagged in certain patterns, such as
    	 similar Amazon EC2 instance, cost center, and group names, and so on.
    	 For example, if you choose **Name** in the
    	 **Key** field and enter
    	 `GRP-*a` in the
    	 **Value** field, CodeDeploy identifies all
    	 instances that fit that pattern, such as
    	 `GRP-1a`,
    	 `GRP-2a`, and
    	 `GRP-XYZ-a`.
    	2. The **Value** field is case sensitive.
    	3. To remove a key-value pair from the list, choose the remove
    	 icon.As CodeDeploy finds instances that match each specified key-value pair or
     Amazon EC2 Auto Scaling group name, it displays the number of matching instances. To
     see more information about the instances, click the number.


    If you want to refine the criteria for the deployed-to instances,
     choose **Add tag group** to create an tag group. You
     can create up to three tag groups with up to 10 key-value pairs each.
     When you use multiple tag groups in a deployment group, only instances
     that are identified by all the tag groups are included in the deployment
     group. That means an instance must match at least one of the tags in
     each of the groups to be included in the deployment group.


    For information about using tag groups to refine your deployment
     group, see [Tagging Instances for Deployments](instances-tagging.md "instances-tagging.md").

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

10. In **Deployment configuration**, choose a deployment
    configuration to control the rate at which instances are deployed to, such as
    one at a time or all at once. For more information about deployment
    configurations, see [Working with deployment configurations in
    CodeDeploy](deployment-configurations.md "deployment-configurations.md").
11. (Optional) In **Load balancer**, select **Enable load
    balancing**, and then from the lists, select the Classic Load Balancers, Application Load Balancer
    target groups, and Network Load Balancer target groups to manage traffic to the instances during
    the CodeDeploy deployment. You can select up to 10 Classic Load Balancers and 10 target groups, for a
    total of 20 items. Make sure that the Amazon EC2 instances that you want to deploy to
    are registered with the selected load balancers (Classic Load Balancers) or target groups
    (Application Load Balancers and Network Load Balancers).

During a deployment, the original instances are deregistered from the selected
load balancers and target groups to prevent traffic from being routed to these
instances during the deployment. When the deployment is complete, each instance
is re-registered with _all_ the selected Classic Load Balancers and target
groups.

For more information about load balancers for CodeDeploy deployments, see [Integrating CodeDeploy with Elastic Load Balancing](integrations-aws-elastic-load-balancing.md "integrations-aws-elastic-load-balancing.md").

###### Warning

If you are configuring both Auto Scaling groups and an ELB load balancers in
this deployment group, and you want to [attach
load balancers to the Auto Scaling groups](../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md "../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md"), we recommend completing this
attachment _before_ creating the CodeDeploy deployment from
this deployment group. Attempting to complete the attachment after creating
the deployment may cause all the instances to become deregistered from the
load balancers unexpectedly. 12. (Optional) Expand **Advanced** and configure any options you
want to include in the deployment, such as Amazon SNS notification triggers, Amazon CloudWatch
alarms, Auto Scaling options, or automatic rollbacks.

For more information, see [Configure advanced options
for a deployment group](deployment-groups-configure-advanced-options.md "deployment-groups-configure-advanced-options.md"). 13. Choose **Create deployment group**.
