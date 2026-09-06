

# Set up in the Lambda console
<a name="setting-up-short"></a>

You can use the following method to create a profiling group with your Lambda function. This method automatically creates a proﬁling group when a profile is available to submit. This method is applicable for runtimes Python 3.8, Python 3.9, Java 8 on Amazon Linux 2 and Java 11 and Java 17 (Corretto). Alternatively, you can create a profiling group by following the instructions in [Setting up in the CodeGuru Profiler console](setting-up-long.md).

If you want to integrate with Lambda for an application with a different runtime, see [Profiling your Java applications that run on AWS Lambda](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/integrating-with-java.html#setting-up-lambda) or [Profiling your Python applications that run on AWS Lambda.](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/integrating-with-python.html#python-lambda). 

## Step 2: Enable CodeGuru Profiler
<a name="setting-up-step-2"></a>

A profiling group can profile one or more applications. Data is aggregated and displayed based on the whole profiling group.

For example, if you have a collection of microservices that handle restaurant recommendations, you can collect profile data and identify performance issues across all these microservices in a single profiling group named "Restaurant-Recommendations". 

**To enable profiling from the Lambda console**

1. Sign in to the AWS Management Console, and then open the Lambda console.

1. Choose your Lambda function. In the **Configuration** tab, choose **Monitoring and operation tools**. Choose **Edit**.

1. Enable **Code profiling** in the **Amazon CodeGuru Profiler** section. This creates a profiling group when a profile is available to submit.

**Note**  
If you want to delete your profiling group, visit the CodeGuru Profiler console. If you disable **Code profiling** in the Lambda console, your profiling group still exists.  
If the execution role of your Lambda function doesn’t have the required CodeGuru Profiler permissions such as [AmazonCodeGuruProfilerAgentAccess](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security-iam-awsmanpol.html#security-iam-awsmanpol-amazoncodeguruprofileragentaccess) or your function doesn’t have the required environment variables, the Lambda console attempts to add them.