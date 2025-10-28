# Profiling your applications that run on AWS Lambda

To start CodeGuru Profiler in your application running on AWS Lambda, you can either update your Lambda
function configuration or modify your application code. The former option is available only
for Java 8 on Amazon Linux 2 and Java 11 and Java 17 (Corretto) runtimes, while the latter is available for all Java
runtimes.

If you enabled profiling in the Lambda console, you don't have to complete the procedure
outlined in the following sections. To learn more about enabling profiling from the Lambda
console, see [Set up in the Lambda console](setting-up-short.md "setting-up-short.md").

###### Note

You can profile your Lambda functions running in Java if they are called often enough for
CodeGuru Profiler to gather enough samples. CodeGuru Profiler collects data once per second, aggregated into
5-minute sampling buckets. For Lambda functions running for fewer than 5 minutes, your
application must run multiple times so CodeGuru Profiler can collect enough data. If it runs too
infrequently, CodeGuru Profiler can't generate enough data to provide recommendations and flame graphs.
For long-running Lambda applications, processing can take up to 15 minutes to display graphs
and information. If you are running your application in shorter durations, processing takes
longer to display information.

###### Topics

- [All Java runtimes](lambda-custom.md "lambda-custom.md")
- [Easier option for Java 8 on Amazon Linux 2 and Java 11 and Java 17 (Corretto)
  runtimes](lambda-simple.md "lambda-simple.md")
