# Use common Agent CLI commands

The following table provides a set of common use cases and corresponding commands for
working with the AWS Kinesis agent.

| Use case                                         | Command                                                        |
| ------------------------------------------------ | -------------------------------------------------------------- |
| Automatically start the agent on system start up | ``<br>`sudo chkconfig aws-kinesis-agent on`<br>``              |
| Check the status of the agent                    | ``<br>`sudo service aws-kinesis-agent status`<br>``            |
| Stop the agent                                   | ``<br>`sudo service aws-kinesis-agent stop`<br>``              |
| Read the agent's log file from this location     | ``<br>`/var/log/aws-kinesis-agent/aws-kinesis-agent.log`<br>`` |
| Uninstall the agent                              | ``<br>`sudo yum remove aws-kinesis-agent`<br>``                |
