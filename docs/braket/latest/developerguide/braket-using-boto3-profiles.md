# Configure AWS CLI profiles for Boto3 and the

Braket SDK

The Amazon Braket SDK relies upon the default AWS CLI credentials,
unless you explicitly specify otherwise. We recommend that you keep the default when you
run on a managed Amazon Braket notebook because you must provide an IAM
role that has permissions to launch the notebook instance.

Optionally, if you run your code locally (on an Amazon EC2 instance, for example), you can
establish named AWS CLI profiles. You can give each profile a different permission set,
rather than regularly overwriting the default profile.

This section provides a brief explanation of how to configure such a CLI
`profile` and how to incorporate that profile into Amazon
Braket so that API calls are made with the permissions from that
profile.

###### In this section:

- [Step 1: Configure a local AWS CLI profile](#braket-using-boto3-profiles-step-1 "#braket-using-boto3-profiles-step-1")
- [Step 2: Establish a Boto3 session object](#braket-using-boto3-profiles-step-2 "#braket-using-boto3-profiles-step-2")
- [Step 3: Incorporate the Boto3
  session into the Braket AwsSession](#braket-using-boto3-profiles-step-3 "#braket-using-boto3-profiles-step-3")

## Step 1: Configure a local AWS CLI `profile`

It is beyond the scope of this document to explain how to create a user and how to
configure a non-default profile. For information on these topics, see:

- [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md")
- [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md")

To use Amazon Braket, you must provide this user — and the
associated CLI `profile` — with the necessary Braket permissions. For
instance, you can attach the **AmazonBraketFullAccess** policy.

## Step 2: Establish a Boto3 session object

In order to establish a Boto3 session object, utilize the following code example.

```
from boto3 import Session

# Insert CLI profile name here
boto_sess = Session(profile_name=`profile`)
```

###### Note

If the expected API calls have Region-based restrictions that
are not aligned with your `profile` default Region, you can specify a
Region for the Boto3 session as shown in the following example.

```
# Insert CLI profile name _and_ region
boto_sess = Session(profile_name=`profile`, region_name=`region`)
```

For the argument designated as `region`, substitute a value that
corresponds to one of the AWS Regions in which Amazon Braket is
available such as `us-east-1`, `us-west-1`, and so
forth.

## Step 3: Incorporate the Boto3

session into the Braket AwsSession

The following example shows how to initialize a Boto3 Braket session and
instantiate a device in that session.

```
from braket.aws import AwsSession, AwsDevice

# Initialize Braket session with Boto3 Session credentials
aws_session = AwsSession(boto_session=boto_sess)

# Instantiate any Braket QPU device with the previously initiated AwsSession
sim_arn = 'arn:aws:braket:::device/quantum-simulator/amazon/sv1'
device = AwsDevice(sim_arn, aws_session=aws_session)
```

After this setup is complete, you can submit quantum tasks to that instantiated
`AwsDevice` object (by calling the `device.run(…​)` command
for example). All API calls made by that device can use the IAM
credentials associated with the CLI profile that you previously designated as
`profile`.
