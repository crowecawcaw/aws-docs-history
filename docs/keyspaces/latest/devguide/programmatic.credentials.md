# Create service-specific

credentials for programmatic access to Amazon Keyspaces

Service-specific credentials are similar to the traditional username and password that Cassandra uses for authentication
and access management.
Service-specific credentials enable IAM users to access a specific AWS
service. These long-term credentials can't be used to access other AWS services. They are
associated with a specific IAM user and can't be used by other IAM users.

###### Important

Service-specific credentials are long-term credentials associated with a
specific IAM user and can only be used for the service they were created
for. To give IAM roles or federated identities permissions to access all
your AWS resources using temporary credentials, you should use [AWS authentication with the SigV4
authentication plugin for Amazon Keyspaces](access.md "access.md").

Use one of the following procedures to generate service-specific
credentials.

Console

###### Create service-specific credentials using the

console

1. Sign in to the AWS Management Console and open the AWS Identity and Access Management console at
   [https://console.aws.amazon.com/iam/home](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home").
2. In the navigation pane, choose **Users**, and
   then choose the user that you created earlier that has Amazon Keyspaces
   permissions (policy attached).
3. Choose **Security Credentials**. Under
   **Credentials for Amazon Keyspaces**, choose
   **Generate credentials** to generate the
   service-specific credentials.

Your service-specific credentials are now available. This is
the only time you can download or view the password. You cannot
recover it later. However, you can reset your password at any
time. Save the user and password in a secure location, because
you'll need them later.

CLI

###### Create service-specific credentials using the AWS CLI

Before generating service-specific credentials, you need to
download, install, and configure the AWS Command Line Interface (AWS CLI):

1. Download the AWS CLI at [http://aws.amazon.com/cli](https://aws.amazon.com/cli "https://aws.amazon.com/cli").

###### Note

The AWS CLI runs on Windows, macOS, or Linux. 2. Follow the instructions for [Installing the AWS
CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") and [Configuring
the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the
_AWS Command Line Interface User Guide_. 3. Using the AWS CLI, run the following command to generate
service-specific credentials for the user `alice`, so
that she can access Amazon Keyspaces.

```
aws iam create-service-specific-credential \
    --user-name alice \
    --service-name cassandra.amazonaws.com

```

The output looks like the following.

```
{
    "ServiceSpecificCredential": {
        "CreateDate": "2019-10-09T16:12:04Z",
        "ServiceName": "cassandra.amazonaws.com",
        "**ServiceUserName**": "alice-at-111122223333",
        "**ServicePassword**": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "ServiceSpecificCredentialId": "ACCAYFI33SINPGJEBYESF",
        "UserName": "alice",
        "Status": "Active"
    }
}
```

In the output, note the values for `ServiceUserName` and
`ServicePassword`. Save these values in a secure
location, because you'll need them later.

###### Important

This is the only time that the `ServicePassword` will
be available to you.
