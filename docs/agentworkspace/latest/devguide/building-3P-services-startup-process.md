# Agent workspace startup

process

Third-party services follow this process in the Amazon Connect agent
workspace:

![Agent workspace third-party service lifecycle flow chart.](images/building-3p-services-startup-process-1.png)

1. **Agent workspace startup**: When an agent logs in and the
   agent workspace starts loading, all configured services will begin their startup
   process.
   1. The configured InitializationTimeout will be in effect until the third-party service has officially connected to the agent workspace.

2. **Agent workspace loading**: The agent workspace will not fully load and
   become accessible to the agent until all services have successfully
   connected.
3. **Service startup**: Once connected, the logic within the
   onCreate handler will begin to run.
4. **Service runtime**: Once created, services continue running
   for the remainder of the agent workspace session.

###### Important

Services directly impact the agent workspace startup process. If any service fails to
start within its configured timeout, an error will be displayed which will prevent
agents from accessing the agent workspace.
