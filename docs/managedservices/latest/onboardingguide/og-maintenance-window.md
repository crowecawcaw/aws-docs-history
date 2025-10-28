# Maintenance Window

You will want to create a maintenance window that considers different application needs, different AWS Regions, and different stress periods.
Your maintenance window is when AMS will apply patching. Here are some guidelines:

- To limit the impact on users, plan your maintenance window according to the AWS Region where your environments are deployed.
- Schedule a window outside of regular business hours and when the least traffic is expected on production servers.
- Typically, infrastructure stacks require monthly updates.
- Schedule a maintenance window for at least 300 minutes. Operating system patching takes 60-90 minutes,
  infrastructure stack patching takes 180-300 minutes.
