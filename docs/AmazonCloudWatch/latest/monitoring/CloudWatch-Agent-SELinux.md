# Set up the CloudWatch agent with security-enhanced Linux
 (SELinux)

If your system has security-enhanced Linux (SELinux) enabled, you must apply the
 appropriate security policies to ensure that the CloudWatch agent runs in a confined domain. 


## Prerequisites


Before you can configure SELinux for the agent, check the following
 **prerequisites**:


###### To complete the prerequisites for using the CloudWatch agent with SELinux

1. If you haven't done so, install the following SELinux policy development
 packages:



```
sudo yum update
sudo yum install -y selinux-policy-devel policycoreutils-devel rpm-build git
```
2. Run the following command to check your system's SELinux status:



```
sestatus
```

Example output:



```
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   permissive
Mode from config file:          permissive
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      33
```

If you find that SELinux is currently disabled, do the following:


	1. Open the SELinux file by entering the following command:
	
	
	
	```
	sudo vi /etc/selinux/config
	```
	2. Set the `SELINUX` parameter to either `permissive` or
	 `enforcing`. For example:
	
	
	
	```
	SELINUX=enforcing
	```
	3. Save the file and reboot the system to apply the changes.
	
	
	
	```
	sudo reboot
	```
3. Ensure that the CloudWatch agent is running as a `systemd` service. This is
 required to use it within a confined SELinux domain.



```
sudo systemctl status amazon-cloudwatch-agent
```

If the agent is correctly configured, the output should indicate that it is
 `active (running)` and `enabled` at startup.

## Configure SELinux for the agent


After you complete the prerequisites, you can configure SELinux.


###### To configure SELinux for the CloudWatch agent

1. Clone the SELinux policy for the CloudWatch agent by entering the following
 command:



```
git clone https://github.com/aws/amazon-cloudwatch-agent-selinux.git
```
2. Navigate to the cloned repository and then update the script permissions by entering
 the following commands:



```
cd amazon-cloudwatch-agent-selinux  
chmod +x amazon_cloudwatch_agent.sh
```
3. Use `sudo` to run the SELinux policy installation script by entering the
 following command. During execution, the script prompts you to enter `y` or
 `n` to allow automatic restart. This restart ensures that the agent
 transitions into the correct SELinux domain.



```
sudo ./amazon_cloudwatch_agent.sh
```
4. If the CloudWatch agent hasn't been restarted yet, restart it to ensure that it
 transitions to the correct SELinux domain:



```
sudo systemctl restart amazon-cloudwatch-agent
```
5. Verify that CloudWatch Agent is running in the confined domain by entering the following
 command:



```
ps -efZ | grep amazon-cloudwatch-agent
```

If the agent is correctly confined, the output should indicate a SELinux-confined
 domain instead of `unconfined_service_t`.


The following is an example of output when the agent is correctly confined.



```
system_u:system_r:confined_t:s0 root 1234 1 0 12:00 ? 00:00:10 /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent
```

After SELinux is configured, you can proceed to configure the agent to collect metrics,
 logs, and traces. For more information, see [Manually create or edit the
 CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md").
