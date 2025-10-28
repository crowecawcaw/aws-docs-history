# Set up in the Lambda console

You can use the following method to create a profiling group with your Lambda function.
This method automatically creates a proﬁling group when a profile is available to submit. This
method is applicable for runtimes Python 3.8, Python 3.9, Java 8 on Amazon Linux 2 and Java 11
and Java 17 (Corretto). Alternatively, you can create a profiling group by following the
instructions in [Setting up in
the CodeGuru Profiler console](setting-up-long.md "setting-up-long.md").

If you want to integrate with Lambda for an application with a different runtime, see [Profiling
your Java applications that run on AWS Lambda](integrating-with-java.md#setting-up-lambda "integrating-with-java.md#setting-up-lambda") or [Profiling your
Python applications that run on AWS Lambda.](integrating-with-python.md#python-lambda "integrating-with-python.md#python-lambda").

## Step 1: Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up
for all services in AWS, including CodeGuru Profiler. You're charged only for the services that you
use.

If you have an AWS account already, move on to the next task. If you don't have an AWS
account, use the following procedure to create one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Step 2: Enable CodeGuru Profiler

A profiling group can profile one or more applications. Data is aggregated and displayed
based on the whole profiling group.

For example, if you have a collection of microservices that handle restaurant
recommendations, you can collect profile data and identify performance issues across all
these microservices in a single profiling group named "Restaurant-Recommendations".

###### To enable profiling from the Lambda console

1. Sign in to the AWS Management Console, and then open the Lambda console.
2. Choose your Lambda function. In the **Configuration** tab, choose
   **Monitoring and operation tools**. Choose
   **Edit**.
3. Enable **Code profiling** in the **Amazon CodeGuru Profiler**
   section. This creates a profiling group when a profile is available to submit.

###### Note

If you want to delete your profiling group, visit the CodeGuru Profiler console. If you disable
**Code profiling** in the Lambda console, your profiling group still
exists.

If the execution role of your Lambda function doesn’t have the required CodeGuru Profiler permissions such
as [AmazonCodeGuruProfilerAgentAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoncodeguruprofileragentaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-amazoncodeguruprofileragentaccess") or your function doesn’t have the required
environment variables, the Lambda console attempts to add them.
