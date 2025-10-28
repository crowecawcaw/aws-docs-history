After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Step 2: Set Up the AWS Command Line Interface (AWS CLI)

Follow the steps to download and configure the AWS Command Line Interface (AWS CLI).

###### Important

You don't need the AWS CLI to perform the steps in the Getting Started exercise. However, some
of the exercises in this guide use the AWS CLI. You can skip this step and go to [Step 3: Create Your Starter Amazon Kinesis Data Analytics Application](get-started-exercise.md "get-started-exercise.md"), and then set up
the AWS CLI later when you need it.

###### To set up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see the following
   topics in the _AWS Command Line Interface User Guide_:
   - [Getting Set
     Up with the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md")
   - [Configuring
     the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")

2. Add a named profile for the administrator user in the AWS CLI config file.
   You use this profile when executing the AWS CLI commands. For more information
   about named profiles, see
   [Named Profiles](../../../cli/latest/userguide/cli-chap-getting-started.md#cli-multiple-profiles "../../../cli/latest/userguide/cli-chap-getting-started.md#cli-multiple-profiles")
   in the _AWS Command Line Interface User Guide_.

```
[profile adminuser]
aws_access_key_id = `adminuser access key ID`
aws_secret_access_key = `adminuser secret access key`
region = `aws-region`
```

For a list of available AWS Regions, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_. 3. Verify the setup by entering the following help command at the command prompt:

```
aws help
```

## Next Step

[Step 3: Create Your Starter Amazon Kinesis Data Analytics Application](get-started-exercise.md "get-started-exercise.md")
