# Amazon SageMaker Debugger UI in Amazon SageMaker Studio Classic Experiments

Use the Amazon SageMaker Debugger Insights dashboard in Amazon SageMaker Studio Classic Experiments to analyze your model
performance and system bottlenecks while running training jobs on Amazon Elastic Compute Cloud (Amazon EC2)
instances. Gain insights into your training jobs and improve your model training performance
and accuracy with the Debugger dashboards. By default, Debugger monitors system metrics (CPU,
GPU, GPU memory, network, and data I/O) every 500 milliseconds and basic output tensors
(loss and accuracy) every 500 iterations for training jobs. You can also further customize
Debugger configuration parameter values and adjust the saving intervals through the Studio Classic
UI or using the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

###### Important

If you're using an existing Studio Classic app, delete the app and restart to use the
latest Studio Classic features. For instructions on how to restart and update your
Studio Classic environment, see [Update Amazon SageMaker AI
Studio Classic](studio-tasks-update.md "studio-tasks-update.md").

###### Topics

- [Open the Amazon SageMaker Debugger Insights dashboard](debugger-on-studio-insights.md "debugger-on-studio-insights.md")
- [Amazon SageMaker Debugger Insights dashboard
  controller](debugger-on-studio-insights-controllers.md "debugger-on-studio-insights-controllers.md")
- [Explore the Amazon SageMaker Debugger Insights
  dashboard](debugger-on-studio-insights-walkthrough.md "debugger-on-studio-insights-walkthrough.md")
- [Shut down the Amazon SageMaker Debugger Insights
  instance](debugger-on-studio-insights-close.md "debugger-on-studio-insights-close.md")
