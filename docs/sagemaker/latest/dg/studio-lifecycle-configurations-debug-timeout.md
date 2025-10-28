# Lifecycle

configuration timeout

There is a lifecycle configuration timeout limitation of 5 minutes. If a lifecycle
configuration script takes longer than 5 minutes to run, you get an error.

To resolve this error, make sure that your lifecycle configuration script
completes in less than 5 minutes.

To help decrease the runtime of scripts, try the following:

- Reduce unnecessary steps. For example, limit which conda environments to
  install large packages in.
- Run tasks in parallel processes.
- Use the nohup command in your script to make sure that hangup signals are
  ignored so that the script runs without stopping.
