

# The Amazon EC2 instances for your Elastic Beanstalk environment
<a name="using-features.managing.ec2"></a>

This topic explains the Amazon EC2 instances and the configuration options that affect your Elastic Beanstalk environment.

When you create a web server environment, AWS Elastic Beanstalk creates one or more Amazon Elastic Compute Cloud (Amazon EC2) virtual machines, known as *Instances*.

The instances in your environment are configured to run web apps on the platform that you choose. You can make changes to various properties and behaviors of your environment's instances when you create your environment or after it's already running. Or, you can already make these changes by modifying the source code that you deploy to the environment. For for more information, see [Configuration options](command-options.md).

**Note**  
The [Auto Scaling group](using-features.managing.as.md) in your environment manages the Amazon EC2 instances that run your application. When you make configuration changes that are described in this topic, the launch configuration also changes. The launch configuration is either an Amazon EC2 launch template or an Auto Scaling group launch configuration resource. This change requires [replacement of all instances](environments-updating.md). It also triggers either a [rolling update](using-features.rollingupdates.md) or [immutable update](environmentmgmt-updates-immutable.md), depending on which one is configured.

**EC2 instance purchasing options**  
Elastic Beanstalk supports several Amazon EC2 [instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html):
+ **On-Demand** — An *On-Demand Instance *is a pay-as-you-go resource—there's no long-term commitment required when you use it.
+ **Reserved** — A *Reserved Instance *is a pre-purchased billing discount applied automatically to matching On-Demand instances in your environment.
+ **Spot** — A *Spot Instance *is an unused Amazon EC2 instance that is available for less than the On-Demand price. You can enable and configure the allocation of Spot Instances in your environment. For more information, see [Auto Scaling your Elastic Beanstalk environment instances](using-features.managing.as.md).

**Topics**
+ [Amazon EC2 instance types](using-features.managing.ec2.instance-types.md)
+ [Configuring Amazon EC2 instances using the Elastic Beanstalk console](using-features.managing.ec2.console.md)
+ [Managing EC2 security groups](using-features.managing.ec2.instances.sg.md)
+ [Configuring Amazon EC2 security groups and instance types using the AWS CLI](using-features.managing.ec2.aws-cli.md)
+ [Configuring Amazon EC2 instances with namespace options](using-features.managing.ec2.namespace.md)
+ [Configuring the IMDS on your Elastic Beanstalk environment's instances](environments-cfg-ec2-imds.md)