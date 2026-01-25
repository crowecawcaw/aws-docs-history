**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Set up AWS CLI

The [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") is a command line tool for working with AWS services, including Amazon EKS. It is also used to authenticate IAM users or roles for access to the Amazon EKS cluster and other AWS resources from your local machine. To provision resources in AWS from the command line, you need to obtain an AWS access key ID and secret key to use in the command line. Then you need to configure these credentials in the AWS CLI. If you haven’t already installed the AWS CLI, see [Install or update the latest version of the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the _AWS Command Line Interface User Guide_.

## To create an access key

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. For single-user or multiple-user accounts:
   - **Single-user account –**::
     In the top right, choose your AWS user name to open the navigation menu. For example, choose **`webadmin`**.
   - **Multiple-user account –**::
     Choose IAM from the list of services. From the IAM Dashboard, select **Users**, and choose the name of the user.

3. Choose **Security credentials**.
4. Under **Access keys**, choose **Create access key**.
5. Choose **Command Line Interface (CLI)**, then choose **Next**.
6. Choose **Create access key**.
7. Choose **Download .csv file**.

## To configure the AWS CLI

After installing the AWS CLI, do the following steps to configure it. For more information, see [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the _AWS Command Line Interface User Guide_.

1. In a terminal window, enter the following command:

```
aws configure
```

Optionally, you can configure a named profile, such as `--profile cluster-admin`. If you configure a named profile in the AWS CLI, you must **always** pass this flag in subsequent commands. 2. Enter your AWS credentials. For example:

```
Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: region-code
Default output format [None]: json
```

## To get a security token

If needed, run the following command to get a new security token for the AWS CLI. For more information, see [get-session-token](../../../cli/latest/reference/sts/get-session-token.md "../../../cli/latest/reference/sts/get-session-token.md") in the _AWS CLI Command Reference_.

By default, the token is valid for 15 minutes. To change the default session timeout, pass the `--duration-seconds` flag. For example:

```
aws sts get-session-token --duration-seconds 3600
```

This command returns the temporary security credentials for an AWS CLI session. You should see the following response output:

```
{
    "Credentials": {
        "AccessKeyId": "ASIA5FTRU3LOEXAMPLE",
        "SecretAccessKey": "JnKgvwfqUD9mNsPoi9IbxAYEXAMPLE",
        "SessionToken": "VERYLONGSESSIONTOKENSTRING",
        "Expiration": "2023-02-17T03:14:24+00:00"
    }
}
```

## To verify the user identity

If needed, run the following command to verify the AWS credentials for your IAM user identity (such as `ClusterAdmin`) for the terminal session.

```
aws sts get-caller-identity
```

This command returns the Amazon Resource Name (ARN) of the IAM entity that’s configured for the AWS CLI. You should see the following example response output:

```
{
    "UserId": "AKIAIOSFODNN7EXAMPLE",
    "Account": "01234567890",
    "Arn": "arn:aws:iam::01234567890:user/ClusterAdmin"
}
```

## Next steps

- [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md")
- [Quickstart: Deploy a web app and store data](quickstart.md "quickstart.md")
