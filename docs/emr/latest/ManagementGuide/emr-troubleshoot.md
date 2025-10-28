# Troubleshoot Amazon EMR clusters

An EMR cluster runs in a complex ecosystem that comprises open-source software, custom application code, and AWS services. When a problem occurs with any of these parts, the cluster might fail or take longer than you expect for it to complete. The following topics can help you identify cluster issues and how to fix them.

###### Topics

- [What tools are available for
  troubleshooting an Amazon EMR cluster?](emr-troubleshoot-tools.md "emr-troubleshoot-tools.md")
- [View and restart Amazon EMR and application
  processes (daemons)](emr-process-restart-stop-view.md "emr-process-restart-stop-view.md")
- [Collections of common errors in Amazon EMR](emr-troubleshoot-errors.md "emr-troubleshoot-errors.md")
- [Troubleshoot an Amazon EMR cluster that has failed with an error code](emr-troubleshoot-failed.md "emr-troubleshoot-failed.md")
- [Troubleshoot a slow Amazon EMR cluster](emr-troubleshoot-slow.md "emr-troubleshoot-slow.md")
- [Troubleshoot common issues when using Amazon EMR with AWS Lake Formation](emr-troubleshoot-lf.md "emr-troubleshoot-lf.md")
  Guidance on troubleshooting [Spark applications on EMR](https://aws.github.io/aws-emr-best-practices/docs/bestpractices/Applications/Spark/troubleshooting/ "https://aws.github.io/aws-emr-best-practices/docs/bestpractices/Applications/Spark/troubleshooting/").

When you are developing a new Hadoop application, we recommend that you enable debugging
and process a small but representative subset of your data to test the application. You may also
want to run the application step-by-step to test each step separately. For more information, see [Configure Amazon EMR cluster logging and debugging](emr-plan-debugging.md "emr-plan-debugging.md") and [Step 5: Test the Amazon EMR cluster step by
step](emr-troubleshoot-failed-5-test-steps.md "emr-troubleshoot-failed-5-test-steps.md").
