

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Launching test and cutover instances
<a name="launching-target-servers"></a>

AWS Transform MGN allows you to launch test and cutover instances in AWS. Before launching instances, you must configure your Launch settings. The following documentation explains how to configure Launch settings and how to launch Test and cutover instances using the configured settings.

Launch settings determine how your test and cutover instances are launched in AWS. Through Launch settings, you can fully customize your test and cutover instances by configuring key metrics, such as the subnet within which the instance is launched, the instance type to be used, licence transfers, replication status, and a variety of other settings. MGN ensures that your test and cutover instances constantly abide by the latest AWS security, instance, and other updates by using EC2 launch templates. EC2 launch templates always use the latest EC2 instance and technology. They integrate with AWS Transform MGN to give you full control over every single setting within your test and cutover instance. Once you have configured your instance's launch settings, you can launch them directly through the MGN console. During the launch process, either during test or cutover instance launch, the AWS replication agent is removed from the test or cutover instance, and does not run on it.

**Topics**
+ [Preparing for test and cutover instance launch](launch-preparation.md)
+ [Launch settings](launch-settings.md)
+ [Launching test instances](launching-test-servers.md)
+ [Launching cutover instances](launch-cutover.md)
+ [Review launch history](jobs.md)