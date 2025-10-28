Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using AWS Security Token Service on a Snowball Edge

The AWS Security Token Service (AWS STS) helps you request temporary, limited-privilege credentials for
IAM users.

###### Important

For AWS services to work properly on a Snowball Edge, you must allow the ports for
the services. For details, see [Port requirements for AWS services on a Snowball Edge](port-requirements.md "port-requirements.md").

###### Topics

- [Using the AWS CLI and API operations on a Snowball Edge](#local-sts-specify-region "#local-sts-specify-region")
- [Supported AWS STSAWS CLI commands on a
  Snowball Edge](#local-sts-cli-commands "#local-sts-cli-commands")
- [Supported AWS STS API operations on a Snowball Edge](#sts-local-supported-apis "#sts-local-supported-apis")

## Using the AWS CLI and API operations on a Snowball Edge

When using the AWS CLI or API operations to issue IAM, AWS STS, Amazon S3, and Amazon EC2 commands
on Snowball Edge device, you must specify the `region` as "`snow`." You
can do this using `AWS configure` or within the command itself, as in the
following examples.

```
aws configure --profile snowballEdge
AWS Access Key ID [None]: defgh
AWS Secret Access Key [None]: 1234567
Default region name [None]: snow
Default output format [None]: json
```

Or

```
aws iam list-users --endpoint http://192.0.2.0:6078 --region snow --profile snowballEdge
```

###### Note

The access key ID and access secret key that are use locally on AWS Snowball Edge can't be
interchanged with the keys in the AWS Cloud.

## Supported AWS STSAWS CLI commands on a

Snowball Edge

Only the [assume-role](../../../cli/latest/reference/sts/assume-role.md "../../../cli/latest/reference/sts/assume-role.md") command is supported locally.

The following parameters are supported for `assume-role`:

- `role-arn`
- `role-session-name`
- `duration-seconds`

### Example command to assume a role on a Snowball Edge

To assume a role, use the following command.

```

    aws sts assume-role --role-arn `"arn:aws:iam::123456789012:role/example-role"` --role-session-name `AWSCLI-Session`  --endpoint `http://snow-device-IP-address`:7078

```

For more information about using the `assume-role` command, see
[How do I assume an
IAM role using the AWS CLI?](https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli "https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli")

For more information about using AWS STS, see [Using Temporary Security Credentials](../../../STS/latest/UsingSTS.md "../../../STS/latest/UsingSTS.md") in the
_IAM User Guide_.

## Supported AWS STS API operations on a Snowball Edge

Only the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API is supported locally.

The following parameters are supported for `AssumeRole`:

- `RoleArn`
- `RoleSessionName`
- `DurationSeconds`

###### Example of assuming a role

```
https://sts.amazonaws.com/
?Version=2011-06-15
&Action=AssumeRole
&RoleSessionName=session-example
&RoleArn=arn:aws:iam::123456789012:role/demo
&DurationSeconds=3600
```
