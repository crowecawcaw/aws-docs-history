Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Set up the AWS Command Line Interface (AWS CLI)

In this step, you download and configure the AWS CLI to use with Managed Service for Apache Flink.

###### Note

The getting started exercises in this guide assume that you are using
administrator credentials (`adminuser`) in your account to perform the
operations.

###### Note

If you already have the AWS CLI installed, you might need to upgrade to get the
latest functionality. For more information, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in the _AWS Command Line Interface User Guide_. To check the
version of the AWS CLI, run the following command:

```
aws --version
```

The exercises in this tutorial require the following AWS CLI version or
later:

```
aws-cli/1.16.63
```

###### To set up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see the following topics
   in the _AWS Command Line Interface User Guide_:
   - [Installing the
     AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md")
   - [Configuring the
     AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")

2. Add a named profile for the administrator user in the AWS CLI
   `config` file. You use this profile when executing the
   AWS CLI commands. For more information about named profiles, see [Named Profiles](../../../cli/latest/userguide/cli-multiple-profiles.md "../../../cli/latest/userguide/cli-multiple-profiles.md") in the
   _AWS Command Line Interface User Guide_.

```
[profile adminuser]
aws_access_key_id = `adminuser access key ID`
aws_secret_access_key = `adminuser secret access key`
region = `aws-region`
```

For a list of available AWS Regions, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_.

###### Note

The example code and commands in this tutorial use the
us-east-1 US East (N. Virginia) Region. To use a different Region,
change the Region in the code and commands for this tutorial to the Region
you want to use. 3. Verify the setup by entering the following help command at the command prompt:

```
aws help
```

After you set up an AWS account and the AWS CLI, you can try the next exercise, in which
you configure a sample application and test the end-to-end setup.

## Next step

[Create and run a Managed Service for Apache Flink application](get-started-exercise.md "get-started-exercise.md")
