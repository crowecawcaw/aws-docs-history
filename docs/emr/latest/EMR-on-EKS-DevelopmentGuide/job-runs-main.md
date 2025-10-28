# Running Spark jobs with Amazon EMR on EKS

A _job run_ is a unit of work, such as a Spark jar, PySpark script, or
SparkSQL query, that you submit to Amazon EMR on EKS. This topic provides an overview of managing job
runs using the AWS CLI, viewing job runs using the Amazon EMR console, and troubleshooting common job
run errors.

Note that you can't run IPv6 Spark jobs on Amazon EMR on EKS

###### Note

Before you submit a job run with Amazon EMR on EKS, you must complete the steps in [Setting up Amazon EMR on EKS](setting-up.md "setting-up.md").

###### Topics

- [Running Spark jobs with StartJobRun](job-runs.md "job-runs.md")
- [Running Spark jobs with the Spark operator](spark-operator.md "spark-operator.md")
- [Running Spark jobs with spark-submit](spark-submit.md "spark-submit.md")
- [Using Apache Livy with Amazon EMR on EKS](job-runs-apache-livy.md "job-runs-apache-livy.md")
- [Managing Amazon EMR on EKS job runs](emr-eks-jobs-manage.md "emr-eks-jobs-manage.md")
- [Using job templates](job-templates.md "job-templates.md")
- [Using pod templates](pod-templates.md "pod-templates.md")
- [Using job retry policies](jobruns-using-retry-policies.md "jobruns-using-retry-policies.md")
- [Using Spark event log rotation](emr-eks-log-rotation.md "emr-eks-log-rotation.md")
- [Using Spark container log rotation](emr-eks-log-rotation-container.md "emr-eks-log-rotation-container.md")
- [Using vertical autoscaling with Amazon EMR Spark jobs](jobruns-vas.md "jobruns-vas.md")
