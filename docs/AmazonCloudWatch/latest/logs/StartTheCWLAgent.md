# Start the CloudWatch Logs agent

If the CloudWatch Logs agent on your EC2 instance did not start automatically after installation,
or if you stopped the agent, you can use the following procedure to start the agent.

###### To start the agent

1. Connect to your EC2 instance. For more information, see [Connect to Your
   Instance](../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md "../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md") in the _Amazon EC2 User Guide_.

For more information about connection issues, see [Troubleshooting Connecting to Your Instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md") in the
_Amazon EC2 User Guide_. 2. At a command prompt, type the following command:

```
sudo service awslogs start
```

If you are running Amazon Linux 2, type the following command:

```
sudo service awslogsd start
```
