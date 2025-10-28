End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# ServiceQuotaExceededException

You might receive the following error when you start a simulation:

```
An error occurred (ServiceQuotaExceededException) when calling the StartSimulation operation: Failed to start simulation due to: simulation quota has already been reached.
```

You will receive this error if you try to start a new simulation but your account
currently has the maximum number of simulations with a target status of STARTED.
This includes running simulations, failed simulations, and simulations that stopped
because they reached their maximum duration.
You can delete a stopped or failed simulation to allow you to start a new
simulation. If all of your simulations are running, you can stop and delete a running
simulation. You can also request an increase to your service quotas if you aren't
already at the request limit.
