

# SEC06-BP03 Reduce manual management and interactive access

 Interactive login is the traditional way to configure, patch, and troubleshoot a server. A listening remote-access service is a path an unauthorized user can target, and manual steps invite human error and shared credentials. Capturing management actions as automation, and reserving direct access for emergencies, reduces the attack surface and the chance of an unintended change. 

 **Desired outcome:** 
+  Your scripts and automation documents (runbooks) capture the authorized actions on your compute resources. 
+  Your runbooks run automatically on change detection, or manually when human judgment is required. 
+  You allow direct access to compute resources only in emergencies, when automation cannot perform the task. 
+  You log and review every manual action, and the review feeds improvements to your automation. 

 **Common anti-patterns:** 
+  Operators reach instances interactively over SSH or RDP as a matter of routine. 
+  Instances maintain individual local logins, such as entries in /etc/passwd or Windows local users. 
+  A shared password or private key gives several people access to the same instance. 
+  Teams install software, change configurations, and apply patches manually. 
+  Engineers log in to instances to troubleshoot problems rather than collecting data through automation. 

 **Benefits of establishing this best practice:** 
+  Automated actions reduce the operational risk of unintended changes and misconfigurations. 
+  Removing SSH and RDP for routine access closes a common path for unauthorized actions. 
+  Runbooks define the full scope of authorized activity, which you can audit at a fine-grained level. 
+  Emergency-only access with logging keeps a clear record of the rare times a person touched a resource. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Say you installed an operating system, logged in to configure it, and returned over its lifetime to patch, reconfigure, and troubleshoot. That lifecycle requires a listening service such as SSH or RDP that an unauthorized user can probe. Manual steps cause incidents and data loss, and shared or distributed credentials add management overhead and weaken accountability. 

 In an outbound-connection model, a lightweight software component on the instance opens an encrypted channel outward to a managed service. The instance no longer listens for inbound sessions, so no port needs to be open. You can route the channel over a private network path instead of the public internet. Control moves from network reachability and key possession to identity and policy, with a central system deciding who runs which action, and under what conditions. 

 Most management tasks such as applying a patch, installing software, or changing a configuration, can run as a defined document with no person at a prompt. Reserve interactive sessions for cases where judgment is required, and log every command and its output. Recording automation invocations and session activity gives you an audit trail of who took action on your resources. 

 On AWS, [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) implements this pattern. The SSM Agent initiates the encrypted channel, so no instance needs to listen for inbound SSH or RDP, and you can configure it to [connect over a VPC endpoint](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html). Systems Manager decides which automations run, who runs them, and when. When an interactive session is unavoidable, [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) provides it and logs the activity, and [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) records the API calls. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Install the SSM Agent:** [Install AWS Systems Manager Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html) on your Amazon EC2 instances, and check whether it is already included and started as part of your base AMI. 

1.  **Grant the instance profile permission:** Verify that the IAM roles in your EC2 instance profiles include the [AmazonSSMManagedInstanceCore managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.html) so Systems Manager can manage the instance. 

1.  **Disable interactive remote-access services:** Turn off SSH, RDP, and other remote-access services on your instances by running scripts in the User Data section of your launch templates, or by building custom AMIs with EC2 Image Builder. 

1.  **Close inbound access at the network layer:** Confirm that security group ingress rules do not permit port 22/tcp (SSH) or port 3389/tcp (RDP), and detect and alert on misconfigured security groups with [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html). 

1.  **Define and scope automations:** Create automations, runbooks, and run commands in Systems Manager, and use IAM policies to define who can run them and under what conditions. Test them in a non-production environment, and invoke them instead of logging in to the instance. 

1.  **Provide logged interactive access for emergencies:** Use [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) when interactive access is necessary, and turn on session activity logging to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) or [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC06-BP05 Automate compute protection](sec06-bp05.md) 
+  [SEC06-BP01 Perform vulnerability management](sec06-bp01.md) 
+  [REL08-BP04 Deploy using immutable infrastructure](rel08-bp04.md) 

 **Related documents:** 
+  [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) 
+  [Manually install the SSM Agent on EC2 instances for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html) 
+  [Create a VPC endpoint for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html) 
+  [AmazonSSMManagedInstanceCore managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.html) 
+  [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) 

 **Related tools:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 