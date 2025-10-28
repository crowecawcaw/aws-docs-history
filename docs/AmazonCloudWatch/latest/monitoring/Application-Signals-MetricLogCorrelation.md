# Enable metric to log correlation

If you publish application logs to log groups in CloudWatch Logs, you can enable _metric to application log correlation_ in Application Signals. With
metric log correlation, the Application Signals console automatically displays the relevant log groups associated with a metric.

For example, suppose you notice a spike in a latency graph. You can choose a point on the graph to load the diagnostics information for that point in time.
The diagnostics information will show the relevant application log groups that are associated with the current service and metric. Then you can choose a button to
run a CloudWatch Logs Insights query on those log groups. Depending on the information contained in the application logs, this might help you to investigate the cause of the latency spike.

Depending on the architecture that your application runs on, you might have to also set an environment variable to enable metric to application log correlation.

- On Amazon EKS, no further steps are needed.
- On Amazon ECS, no further steps are needed.
- On Amazon EC2, see step 4 in the procedure in
  [Step 3: Instrument your application and start it](CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument "CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument").
