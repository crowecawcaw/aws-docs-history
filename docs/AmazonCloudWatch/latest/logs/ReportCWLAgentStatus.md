# Report the CloudWatch Logs agent status

Use the following procedure to report the status of the CloudWatch Logs agent on your EC2 instance.

###### To report the agent status

1. Connect to your EC2 instance. For more information, see [Connect to Your
   Instance](../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md "../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md") in the _Amazon EC2 User Guide_.

For more information about connection issues, see [Troubleshooting Connecting to Your Instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md") in the
_Amazon EC2 User Guide_ 2. At a command prompt, type the following command:

```
sudo service awslogs status
```

If you are running Amazon Linux 2, type the following command:

```
sudo service awslogsd status
```

3. Check the **/var/log/awslogs.log** file for any errors,
   warnings, or issues with the CloudWatch Logs agent.
