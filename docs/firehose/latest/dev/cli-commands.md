

# Use common Agent CLI commands
<a name="cli-commands"></a>

The following table provides a set of common use cases and corresponding commands for working with the AWS Kinesis agent. 


| Use case | Command | 
| --- | --- | 
| Automatically start the agent on system start up |  <pre>sudo chkconfig aws-kinesis-agent on</pre>  | 
| Check the status of the agent |  <pre>sudo service aws-kinesis-agent status</pre>  | 
| Stop the agent |  <pre>sudo service aws-kinesis-agent stop</pre>  | 
| Read the agent's log file from this location |  <pre>/var/log/aws-kinesis-agent/aws-kinesis-agent.log</pre>  | 
| Uninstall the agent |  <pre>sudo yum remove aws-kinesis-agent</pre>  | 