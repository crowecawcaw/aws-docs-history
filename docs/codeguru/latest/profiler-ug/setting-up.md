# Setting up CodeGuru Profiler

An Amazon CodeGuru Profiler proﬁling group is a group of applications for which data is meant to be
aggregated and analyzed together. To create a proﬁling group, sign in to the AWS Management Console and set
permissions for the CodeGuru Profiler proﬁling agent.

The proﬁling agent collects runtime data from your applications. Data that the agent
collects is analyzed to provide flame graphs and hourly reports with recommendations for how you
can optimize your applications.

You can create a profiling group using your own application or the demo application. For
more information about using the demo application, see [Getting started with CodeGuru Profiler](getting-started.md "getting-started.md").

Before you can start using CodeGuru Profiler, you must complete setup. If your application runs on
AWS Lambda, then you can enable profiling from the Lambda console. If your application runs on a
platform other than Lambda, then you can complete the setup process in the CodeGuru Profiler console.

###### Topics

- [Set up in the Lambda console](setting-up-short.md "setting-up-short.md")
- [Set up in the CodeGuru Profiler console](setting-up-long.md "setting-up-long.md")
