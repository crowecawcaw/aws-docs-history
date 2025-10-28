# Configuring launch settings in AWS Elastic Disaster Recovery

Launch settings determine how your drill and recovery instances are launched in AWS. They
are composed of DRS launch settings and EC2 launch template, allowing you to fully customize
your drill and recovery instances by configuring key metrics, such as the subnet within
which the instance will be launched, the instance type to be used, license transfers,
replication status, and a variety of other settings. AWS Elastic Disaster Recovery ensures that your drill and
recovery instances constantly abide by the latest AWS security, instance, and other updates
by utilizing EC2 launch templates. EC2 launch templates always use the latest EC2 instance
and technology. EC2 launch templates integrate with AWS Elastic Disaster Recovery in order to give you full
control over every single setting within your drill and recovery instance.

## Preparing for drill and recovery instance

launch

Prior to launching your instances, make sure that your environment is set up properly
to ensure successful launches. Check the following prior to continuing:

- Prepare your subnets for launch – Plan which subnets you will use to launch
  your drill and recovery instances. You will use these subnets in your EC2 launch
  template when you configure launch settings.
- Create security groups within the subnets – Create the security groups you
  want to use within your prepared subnets. You will set these security groups in
  your EC2 launch template when you configure launch settings.

###### Note

If you want to run a proof of concept, you can skip this step. AWS Elastic Disaster Recovery
will automatically use the default subnet and security groups. Ensure that
you have not deleted your default subnet.

###### Important

When launching a drill, recovery, or an in-AWS failback, you can launch up to 100 source servers in a single operation. Additional source servers can be launched in subsequent operations.

## Launch settings

Launch settings are a set of instructions that are comprised of two sections: DRS
launch settings and the EC2 launch template, that determine how a drill or recovery
instance is launched for each source server in AWS.

Launch settings, including the EC2 launch template, are automatically created each
time you add a source server to AWS Elastic Disaster Recovery.

You can modify the launch settings at any time, including before the source server has
completed its initial sync.

###### Note

- Any changes made to the launch settings only affect newly launched drill
  and recovery instances.
- For many customers, there is no need to modify the DRS launch settings or
  the EC2 launch template in order to launch drill or recovery instances.

You can change launch settings for a single server or for multiple servers in the AWS
DRS console. This allows you to make changes to multiple servers at once. You can also
modify launch settings for multiple servers via the AWS Elastic Disaster Recovery API.

To access the launch settings of a specific source server, go to the **Source servers** page and click the server's hostname. In the
individual server view navigate to the **Launch settings**
tab.

You can also access the launch settings of a single server by selecting a single
source server on the **Source servers** page and choosing
**Actions > Edit DRS launch settings** or **Actions > Edit EC2 launch template**.

The **Launch settings** tab is divided into two sections:

- DRS launch settings
- EC2 launch template

Learn more about Amazon EC2 launch templates in [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md").
