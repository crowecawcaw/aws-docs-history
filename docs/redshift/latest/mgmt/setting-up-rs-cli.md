Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up the Amazon Redshift CLI

This section explains how to set up and run the AWS CLI command line tools for use in
managing Amazon Redshift. The Amazon Redshift command line tools run on the AWS Command Line Interface (AWS CLI), which in
turn uses Python ([https://www.python.org/](https://www.python.org "https://www.python.org")).
The AWS CLI can be run on any operating system that supports Python.

## Installing the AWS Command Line Interface

To begin using the Amazon Redshift command line tools, you first set up the AWS CLI, and then
you add configuration files that define the Amazon Redshift CLI options.

If you have already installed and configured the AWS CLI for another AWS service,
you can skip this procedure.

###### To install the AWS Command Line Interface

1. Go to [Install or
   update to the latest version of the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md"), and then follow the
   instructions for installing the AWS CLI.

For CLI access, you need an access key ID and a secret access key.
Use temporary credentials instead of long-term access keys when possible.
Temporary credentials include an access key ID, a secret access key, and a
security token that indicates when the credentials expire. For more information,
see [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_. 2. Create a file containing configuration information such as your access
keys, default region, and command output format. Then set the
`AWS_CONFIG_FILE` environment variable to reference that
file. For detailed instructions, go to [Configuring the AWS
command line interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the AWS Command Line Interface User Guide. 3. Run a test command to confirm that the AWS CLI interface is working. For
example, the following command should display help information for the
AWS CLI:

```
aws help
```

The following command should display help information for Amazon Redshift:

```
aws redshift help
```

For reference material on the Amazon Redshift CLI commands, go to [Amazon Redshift](../../../cli/latest/reference/redshift/index.md "../../../cli/latest/reference/redshift/index.md") in the AWS CLI
Reference.
