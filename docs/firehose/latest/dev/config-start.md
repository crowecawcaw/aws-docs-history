# Configure and start the Agent

###### To configure and start the agent

1. Open and edit the configuration file (as superuser if using default file
   access permissions): `/etc/aws-kinesis/agent.json`

In this configuration file, specify the files ( `"filePattern"` )
from which the agent collects data, and the name of the Firehose stream (
`"deliveryStream"` ) to which the agent sends data. The file name
is a pattern, and the agent recognizes file rotations. You can rotate files or
create new files no more than once per second. The agent uses the file creation
time stamp to determine which files to track and tail into your Firehose stream.
Creating new files or rotating files more frequently than once per second does
not allow the agent to differentiate properly between them.

```
{
   "flows": [
        {
            "filePattern": "`/tmp/app.log*`",
            "deliveryStream": "`yourdeliverystream`"
        }
   ]
}
```

The default AWS Region is `us-east-1`. If you are using a different
Region, add the `firehose.endpoint` setting to the configuration
file, specifying the endpoint for your Region. For more information, see [Specify agent configuration settings](agent-config-settings.md "agent-config-settings.md"). 2. Start the agent manually:

```
`sudo service aws-kinesis-agent start`
```

3. (Optional) Configure the agent to start on system startup:

```
`sudo chkconfig aws-kinesis-agent on`
```

The agent is now running as a system service in the background. It continuously
monitors the specified files and sends data to the specified Firehose stream. Agent
activity is logged in `/var/log/aws-kinesis-agent/aws-kinesis-agent.log`.
