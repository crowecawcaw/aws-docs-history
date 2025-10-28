# Automatically update the minimum version of SSM and CloudWatch agents

The AMS Advanced _minimum version_ (of the SSM or CloudWatch agents) is the version that
has been tested by AMS service team and pre-approved for your operating system.
We try to stay proactive and run the latest stable and compatible version,
so the version number changes over time. You can find the current minimum version by raising a service request to AMS.

- **SSM Agent Management**

The Amazon SSM Agent is responsible for running remote commands on the instance.
The instance configuration automation ensures that the SSM Agent is running the minimum version.

- **Cloudwatch Agent Management**

The Amazon CloudWatch Agent is responsible for emitting OS logs and metrics. Automated instance configuration performs the following:

    + If needed, disables the legacy CloudWatch Log agent and migrates the configuration to the new unified CloudWatch agent
    + If your instance is running the legacy CloudWatch Log Agent, automated instance configuration disables the
     legacy CloudWatch Log agent service and migrates its configuration to the unified CloudWatch agent.
    + Customizes your CloudWatch configuration to emit appropriate logs and metrics.

Affected files and directories:

    + Windows




    	- %ProgramData%\Amazon\AmazonCloudWatchAgent\
    	- %ProgramData%\Amazon\AmazonCloudWatchAgent\Configs\
    + Linux




    	- /opt/aws/amazon-cloudwatch-agent/etc/
    	- /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d/
    	- /opt/aws/ams/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
