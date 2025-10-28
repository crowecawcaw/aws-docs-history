End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 2: Set Up the AWS Command Line Interface

If you prefer to use Amazon Lex with the AWS Command Line Interface (AWS CLI), download and configure
it.

###### Important

You don't need the AWS CLI to perform the steps in the Getting Started exercises.
However, some of the later exercises in this guide use the AWS CLI. If you prefer to
start by using the console, skip this step and go to [Step 3:
Getting
Started (Console)](gs-console.md "gs-console.md"). Later, when you need the AWS CLI, return here to set
it up.

###### To set up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see the following topics
   in the _AWS Command Line Interface User Guide_:
   - [Getting Set Up
     with the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md")
   - [Configuring the
     AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")

2. Add a named profile for the administrator user to the end of the AWS CLI config
   file. You use this profile when executing AWS CLI commands. For more information
   about named profiles, see [Named
   Profiles](../../../cli/latest/userguide/cli-chap-getting-started.md#cli-multiple-profiles "../../../cli/latest/userguide/cli-chap-getting-started.md#cli-multiple-profiles") in the _AWS Command Line Interface User Guide_.

```
[profile adminuser]
aws_access_key_id = `adminuser access key ID`
aws_secret_access_key = `adminuser secret access key`
region = `aws-region`
```

For a list of available AWS Regions, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_. 3. Verify the setup by typing the Help command at the command prompt:

```
aws help
```

##

[Step 3:
Getting
Started (Console)](gs-console.md "gs-console.md")
