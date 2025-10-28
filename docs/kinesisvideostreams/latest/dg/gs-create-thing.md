# Create an AWS IoT thing and get AWS IoT Core

credentials

At this point you've created:

- An IAM permissions policy. See [Create an IAM permissions policy](gs-iam-role.md "gs-iam-role.md").
- An IAM role, with the permissions policy attached. See [Create an IAM role](gs-create-role.md "gs-create-role.md").
- An AWS IoT role alias for the IAM role. See [Create the AWS IoT role alias](gs-create-role-alias.md "gs-create-role-alias.md").
- An AWS IoT policy, currently unattached to any AWS resource. See [Create the AWS IoT policy](gs-create-policy.md "gs-create-policy.md").

###### To create and register an AWS IoT thing and get AWS IoT Core access credentials

1.  Register the device as an AWS IoT thing and generate the X.509 certificate
    for the device.
    1.  Sign in to the AWS Management Console and open the AWS IoT Core console at
        [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
    2.  Select the appropriate Region.
    3.  On the left navigation, select **All devices**,
        then choose **Things**.
    4.  Choose **Create things**.
    5.  Select **Create single thing**, then choose
        **Next**.
        1. **Step 1. Specify thing
           properties**

        Type a name for your thing, then choose
        **Next**. 2. **Step 2. Configure device
        certificate**

        Select **Auto-generate a new certificate
        (recommended)**, then choose
        **Next**. 3. **Step 3. Attach policies to
        certificate**

        Search for the permissions policy you created in [Create the AWS IoT policy](gs-create-policy.md "gs-create-policy.md").

        Select the check box next to your policy and choose
        **Create thing**.

    6.  In the window that appears, download the following files:

            * Device certificate. This is the X.509 certificate.
            * Public key file
            * Private key file
            * Amazon trust services endpoint (RSA 2048 bit key: Amazon
             Root CA 1)

        Make note of the location of each of these files for a later
        step.

    7.  Choose **Done**. On the next page, you see a note
        that your thing was successfully created.
    8.  Transfer the files downloaded above onto your AWS IoT thing, if not
        already there.

2.  Obtain the credential provider endpoint for your AWS account.

AWS CLI
Run the following command:

```
aws iot describe-endpoint --endpoint-type iot:CredentialProvider
```

AWS Management Console
In [AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md"), run the following command:

```
aws iot describe-endpoint --endpoint-type iot:CredentialProvider
```

Make note of this information for a later step. 3. Obtain the device data endpoint for your AWS account.

AWS CLI
Run the following command:

```
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

AWS Management Console
Do the following:

    1. Sign in to the AWS Management Console and open the AWS IoT Core
     console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
    2. In the left navigation, select
     **Settings**.
    3. Locate the **Device data
     endpoint**.

Make note of this information for a later step. 4. (Optional) Verify that your certificates were generated correctly.

Run the following command to validate that your items were generated
correctly.

```
curl --header "x-amzn-iot-thingname:`your-thing-name`" \
  --cert /`path`/`to`/`certificateID-certificate`.pem.crt \
  --key /`path`/`to`/`certificateID-private`.pem.key \
  --cacert /`path`/`to`/AmazonRootCA1.pem \
  https://`your-credential-provider-endpoint`/role-aliases/`your-role-alias-name`/credentials
```

For more information, see [How to use a certificate to get a security token](../../../iot/latest/developerguide/authorizing-direct-aws.md#authorizing-direct-aws.walkthrough "../../../iot/latest/developerguide/authorizing-direct-aws.md#authorizing-direct-aws.walkthrough").
