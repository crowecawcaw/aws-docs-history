# Use common Agent CLI commands

The following table provides a set of common use cases and corresponding commands for
working with the AWS Kinesis agent.

| Use case                                         | Command                                                  |
| ------------------------------------------------ | -------------------------------------------------------- |
| Automatically start the agent on system start up | `` `sudo chkconfig aws-kinesis-agent on` ``              |
| Check the status of the agent                    | `` `sudo service aws-kinesis-agent status` ``            |
| Stop the agent                                   | `` `sudo service aws-kinesis-agent stop` ``              |
| Read the agent's log file from this location     | `` `/var/log/aws-kinesis-agent/aws-kinesis-agent.log` `` |
| Uninstall the agent                              | `` `sudo yum remove aws-kinesis-agent` ``                |
