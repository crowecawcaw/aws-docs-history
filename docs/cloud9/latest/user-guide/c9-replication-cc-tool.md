AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Using the replication tool

AWS Cloud9 in CodeCatalyst provides a fully managed experience for interacting with AWS Cloud9. To
enable customers to try using AWS Cloud9 in CodeCatalyst, we have created a replication tool. After you copy and run the script in your AWS Cloud9 environment, follow the prompts to
run it and replicate your code resources from AWS Cloud9 to CodeCatalyst. For more information on
the replication tool and process, see [FAQ's
on the replication process](faqs-replication-tool.md "faqs-replication-tool.md") outlined below.

###### Note

This replication process will have no effect on your existing AWS Cloud9
environments. After the replication process is complete, you can delete the
Dev Environments, source repositories, project and space, and it will have no
affect on your AWS Cloud9 environment. This tool will only copy your code resources to
AWS Cloud9 in CodeCatalyst, it will not delete or configure your existing AWS Cloud9 environments.
This replication tool has been released to an initial select group of AWS accounts. As a result, it may not appear in certain AWS accounts.

###### Note

It is recommended that you sign up to Amazon CodeCatalyst and create a space
before you download the tool. For information about signing up to CodeCatalyst, see
[Signing up to Amazon CodeCatalyst and
creating a Space](c9-replication-cc.md#c9-replication-cc-space-creation "c9-replication-cc.md#c9-replication-cc-space-creation").

## Benefits of using AWS Cloud9 on Amazon CodeCatalyst

The following section outlines some of the performance benefits and enhanced features you will
experience when using AWS Cloud9 on CodeCatalyst:

- CodeCatalyst provides an integrated experience that enables you to use fully managed Dev Environments to manage the entire software development life cycle from a single location.
- Enhanced Amazon EBS volume size options at launch.
- Support for ephemeral environments and the ability to scale compute of your Dev Environment on demand.
- Custom AMI support that is available through the specification of custom images.
- Devfile support that enables you to describe configurations as code.

## Replicating your AWS Cloud9 code

resources in CodeCatalyst using the replication tool

The following procedure details how to copy and run the replication tool to
complete the replication process.

1. Copy the script below and ensure you run it within an AWS Cloud9
   environment:

```
curl https://dx5z5embsyrja.cloudfront.net -o /tmp/replicate-tool.tar.gz && tar --no-same-owner --no-same-permissions -xvf /tmp/replicate-tool.tar.gz -C /tmp && node /tmp/cloud9-replication-tools
```

2. _[Optional]_ The replication tool uses your
   AWS account ID for telemetry. The purpose of this is to help us better
   identify any issues you may encounter while using the tool. We emit
   telemetry events for `tool starts`, `tool fails`,
   `tool is cancelled by user`, `tool completes
successfully` and `tool creates a Dev Environment for the
user`. If you want to disable telemetry with the replication tool,
   see [Disabling telemetry for the
   replication tool](#disable-telemetry "#disable-telemetry") below.
3. After you copy and run the replication tool in your AWS Cloud9 environment,
   you will need to link your AWS account with an AWS Builder ID by navigating to
   the access URL in a browser and clicking _Allow_ within
   10 minutes. Please ensure you only open the link once, if you open it
   multiple times it will cause an error and you will need to start again. For
   more information about AWS Builder ID, see [Sign-in with
   AWS Builder ID](../../../signin/latest/userguide/sign-in-aws_builder_id.md "../../../signin/latest/userguide/sign-in-aws_builder_id.md") in the _AWS Sign-In User Guide_.
   This will grant the replication tool access to your code resources for the
   purpose of replicating them in CodeCatalyst.
4. Choose the Space that you want to use. If you have only one
   space, that space is selected. For more information about spaces, see [Spaces
   in CodeCatalyst](../../../codecatalyst/latest/userguide/spaces.md "../../../codecatalyst/latest/userguide/spaces.md") in the _Amazon CodeCatalyst User Guide_.
5. Choose if you want to replicate your code in CodeCatalyst or try it with a
   new Dev Environment. We recommend replicating your code directly in CodeCatalyst.
   For more information about Dev Environments, see [Dev Environments
   in CodeCatalyst](../../../codecatalyst/latest/userguide/devenvironment.md "../../../codecatalyst/latest/userguide/devenvironment.md") in the _Amazon CodeCatalyst User Guide_.
6. Enter a name for your project or press enter to use the default name
   provided.
7. When prompted, select how you want to copy your files to the new
   source repository in CodeCatalyst. You can choose to either push the root
   folder to a single CodeCatalyst repository, or push your sub-folders to
   distinct CodeCatalyst repositories.
8. After the tool is complete, navigate to the project within the CodeCatalyst
   console through the URL provided in the terminal message to access your
   code resources in CodeCatalyst.

After completing this procedure, your CodeCatalyst repository has the updated files
and commits that you just pushed. You can now create Dev Environments from this branch
and open them with AWS Cloud9.

## Disabling telemetry for the replication tool

The following steps outline how to set an environment variable to disable
telemetry for the replication tool.

1. Open a terminal in your AWS Cloud9 environment
2. Run either of the following commands:

```
export CLOUD9_REPLICATION_TOOL_TELEMETRY=off
```

or

```
export CLOUD9_REPLICATION_TOOL_TELEMETRY=0
```

3. Once you run one of the commands above, the environment variable will
   be set and telemetry for the replication tool will be disabled. After you
   have disabled telemetry you must copy and re-run the replication tool script
   again to begin the process.

## Replication tool feedback

If you encounter any issues, or want to give feedback on your experience using the replication tool, please create and submit a support case. For information on
creating a support case, see [Creating support cases and case
management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").

## Differences between AWS Cloud9 and Amazon CodeCatalyst

The following table outlines some of the differences between AWS Cloud9 and AWS Cloud9 on
CodeCatalyst.

| AWS Cloud9                                                                                         | AWS Cloud9 on Amazon CodeCatalyst                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Private VPC works very well with AWS Cloud9.                                                       | The use of private VPC is currently not supported for AWS Cloud9 on CodeCatalyst.                                                                                                                                                                                                                                                                                       |
| AWS Cloud9 supports pre-configured AWS managed credentials.                                        | Credentials need to be manually configured for AWS Cloud9 on CodeCatalyst.                                                                                                                                                                                                                                                                                              |
| It is possible to have intervals of 30 minutes to 7 days and to disable shutdowns with AWS Cloud9. | It is possible to have intervals of 15 minutes to 20 hours for AWS Cloud9 on CodeCatalyst and you can't disable shutdowns.                                                                                                                                                                                                                                              |
| AWS Cloud9 supports Ubuntu and AL2 OS platforms.                                                   | AWS Cloud9 on CodeCatalyst supports MDE Universal images and custom images which can include Ubuntu and AL2. For more information on this, see [Universal devfile images](../../../codecatalyst/latest/userguide/devenvironment-universal-image.md "../../../codecatalyst/latest/userguide/devenvironment-universal-image.md") in the _Amazon CodeCatalyst User Guide_. |
| Uploading and downloading is supported in AWS Cloud9                                               | Uploading and downloading is currently not supported for AWS Cloud9 on CodeCatalyst. Users will need to upload and download using Amazon S3 buckets.                                                                                                                                                                                                                    |
| Collaboration is available in AWS Cloud9                                                           | Collaboration is currently not available for AWS Cloud9 on CodeCatalyst.                                                                                                                                                                                                                                                                                                |
