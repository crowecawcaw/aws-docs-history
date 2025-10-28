# Step 5: Test the Amazon EMR cluster step by

step

A useful technique when you are trying to track down the source of an error is to
restart the cluster and submit the steps to it one by one. This lets you check the
results of each step before processing the next one, and gives you the opportunity to
correct and re-run a step that has failed. This also has the advantage that you only
load your input data once.

###### To test a cluster step by step

1. Launch a new cluster, with both keep alive and termination protection
   enabled. Keep alive keeps the cluster running after it has processed all of its
   pending steps. Termination protection prevents a cluster from shutting down in
   the event of an error. For more information, see [Configuring an Amazon EMR cluster to continue or
   terminate after step execution](emr-plan-longrunning-transient.md "emr-plan-longrunning-transient.md") and [Using termination protection to protect your Amazon EMR clusters from
   accidental shut down](UsingEMR_TerminationProtection.md "UsingEMR_TerminationProtection.md").
2. Submit a step to the cluster. For more information, see [Submit work to an Amazon EMR cluster](emr-work-with-steps.md "emr-work-with-steps.md").
3. When the step completes processing, check for errors in the step log files.
   For more information, see [Step 4: Examine the Amazon EMR log files](emr-troubleshoot-failed-4.md "emr-troubleshoot-failed-4.md"). The fastest way to locate these
   log files is by connecting to the master node and viewing the log files there.
   The step log files do not appear until the step runs for some time, finishes, or
   fails.
4. If the step succeeded without error, run the next step. If there were errors,
   investigate the error in the log files. If it was an error in your code, make
   the correction and re-run the step. Continue until all steps run without error.
5. When you are done debugging the cluster, and want to terminate it, you will
   have to manually terminate it. This is necessary because the cluster was
   launched with termination protection enabled. For more information, see [Using termination protection to protect your Amazon EMR clusters from
   accidental shut down](UsingEMR_TerminationProtection.md "UsingEMR_TerminationProtection.md").
