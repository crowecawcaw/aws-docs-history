# Use AWS CloudShell to work with AWS Identity and Access Management

AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the
AWS Management Console. You can run AWS CLI commands against AWS services (including AWS Identity and Access Management) using
your preferred shell (Bash, PowerShell or Z shell). And you can do this without needing to
download or install command line tools.

You [launch AWS CloudShell
from the AWS Management Console](../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options "../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options"), and the AWS credentials you used to sign in to the console are
automatically available in a new shell session. This pre-authentication of AWS CloudShell users allows
you to skip configuring credentials when interacting with AWS services such as IAM using
AWS CLI version 2 (pre-installed on the shell's compute environment).

## Obtain IAM permissions for AWS CloudShell

Using the access management resources provided by AWS Identity and Access Management, administrators can grant
permissions to IAM users so they can access AWS CloudShell and use the environment's
features.

The quickest way for an administrator to grant access to users is through an AWS managed
policy. An [AWS
managed policy](access_policies_managed-vs-inline.md#aws-managed-policies "access_policies_managed-vs-inline.md#aws-managed-policies") is a standalone policy that's created and administered by AWS. The
following AWS managed policy for CloudShell can be attached to IAM identities:

- `AWSCloudShellFullAccess`: Grants permission to use AWS CloudShell with full
  access to all features.

If you want to limit the scope of actions that an IAM user can perform with AWS CloudShell,
you can create a custom policy that uses the `AWSCloudShellFullAccess` managed
policy as a template. For more information about limiting the actions that are available to
users in CloudShell, see [Managing AWS CloudShell access and
usage with IAM policies](../../../cloudshell/latest/userguide/sec-auth-with-identities.md "../../../cloudshell/latest/userguide/sec-auth-with-identities.md") in the _AWS CloudShell User Guide_.

## Interact with IAM

After you launch AWS CloudShell from the AWS Management Console, you can immediately start to interact with
IAM using the command line interface.

###### Note

When using AWS CLI in AWS CloudShell, you don't need to download or install any additional
resources. Moreover, because you're already authenticated within the shell, you don't need
to configure credentials before making calls.

## Create an IAM group and add an IAM user to the group using AWS CloudShell

The following example uses CloudShell to create an IAM group, add an IAM user to
the group, and then verify that the command succeeded.

1. From the AWS Management Console, you can launch CloudShell by choosing the following options
   available on the navigation bar:
   - Choose the CloudShell icon.
   - Start typing "cloudshell" in Search box and then choose the CloudShell
     option.

2. To create an IAM group, enter the following command in the CloudShell command
   line. In this example we named the group _east_coast_:

```
aws iam create-group --group-name east_coast
```

If the call is successful, the command line displays a response from the service
similar to the following output:

```

        {
           "Group": {
               "Path": "/",
               "GroupName": "east_coast",
               "GroupId": "AGPAYBDBW4JBY3EXAMPLE",
               "Arn": "arn:aws:iam::111122223333:group/east_coast",
               "CreateDate": "2023-09-11T21:02:21+00:00"
            }
        }

```

3. To add a user to the group that you created, use the following command, specifying the
   group name and username. In this example we named the group _east_coast_ and the user _john_:

```
aws iam add-user-to-group --group-name east_coast --user-name john
```

4. To verify that the user is in the group, use the following command, specifying the
   group name. In this example we continue using the group _east_coast_ :

```
aws iam get-group --group-name east_coast
```

If the call is successful, the command line displays a response from the service
similar to the following output:

```

       {
         "Users": [
           {
               "Path": "/",
               "UserName": "john",
               "UserId": "AIDAYBDBW4JBXGEXAMPLE",
               "Arn": "arn:aws:iam::552108220995:user/john",
               "CreateDate": "2023-09-11T20:43:14+00:00",
               "PasswordLastUsed": "2023-09-11T20:59:14+00:00"
           }
         ],
         "Group": {
               "Path": "/",
               "GroupName": "east_coast",
               "GroupId": "AGPAYBDBW4JBY3EXAMPLE",
               "Arn": "arn:aws:iam::111122223333:group/east_coast",
               "CreateDate": "2023-09-11T21:02:21+00:00"
            }
        }

```
