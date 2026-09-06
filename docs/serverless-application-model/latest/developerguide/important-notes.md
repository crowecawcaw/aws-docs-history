

# Important reference notes for AWS SAM
<a name="important-notes"></a>

This section contains important notes and announcements for AWS Serverless Application Model (AWS SAM).

**Topics**
+ [Important notes for 2023](#important-notes-2023)

## Important notes for 2023
<a name="important-notes-2023"></a>

### October 2023
<a name="important-notes-2023-10"></a>

#### AWS SAM CLI discontinuing support for Python 3.7
<a name="important-notes-2023-10-python"></a>

*Published on 2023-10-20*

Python 3.7 received end-of-life status in June of 2023. The AWS SAM CLI will discontinue support for Python 3.7 on October 24, 2023. For more information, see the [announcement](https://github.com/aws/aws-sam-cli/issues/5889) at the *aws-sam-cli GitHub repository*.

This change impacts the following users:
+ If you use Python 3.7 and install the AWS SAM CLI through `pip`.
+ If you use the `aws-sam-cli` as a library and build your application with Python 3.7.

If you install and manage the AWS SAM CLI through another method, you are not affected.

For impacted users, we recommend that you upgrade your development environment to Python 3.8 or newer.

This change does not affect support for the Python 3.7 AWS Lambda runtime environment. For more information, see [Runtime deprecation policy](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy) in the *AWS Lambda Developer Guide*.