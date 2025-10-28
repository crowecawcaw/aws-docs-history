# Configure your AWS IoT FleetWise settings

You can use the AWS IoT FleetWise console or API to configure settings for Amazon CloudWatch Logs metrics,
Amazon CloudWatch Logs, and encrypt data with an AWS managed key.

With CloudWatch metrics, you can monitor AWS IoT FleetWise and other AWS resources. You can use CloudWatch
metrics to collect and track metrics, such as to determine if there is an exceeded
service limit. For more information about CloudWatch metrics, see [Monitor AWS IoT FleetWise with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

With CloudWatch Logs, AWS IoT FleetWise sends log data to a CloudWatch log group, where you can use it to
identify and mitigate any issues. For more information about CloudWatch Logs, see [Configure AWS IoT FleetWise logging](logging-cw.md "logging-cw.md").

With data encryption, AWS IoT FleetWise uses AWS managed keys to encrypt data. You can also
choose to create and manage keys with AWS KMS. For more information about encryption, see
[Data encryption in AWS IoT FleetWise](data-encryption.md "data-encryption.md").

## Configure settings (console)

If you aren't already signed in to your AWS account, sign in, then open the [AWS IoT FleetWise
console](https://console.aws.amazon.com/iotfleetwise/ "https://console.aws.amazon.com/iotfleetwise/").

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the left pane, choose **Settings**.
3. In **Metrics**, choose
   **Enable**. AWS IoT FleetWise automatically attaches a CloudWatch
   managed policy to the service-linked role and enables CloudWatch metrics.
4. In **Logging**, choose **Edit**.
   1. In the **CloudWatch logging** section, enter the **Log group**.
   2. To save your changes, choose **Submit**.

5. In the **Encryption** section, choose **Edit**.
   1. Choose the type of key that you want to use. For more
      information, see [Key management in AWS IoT FleetWise](key-management.md "key-management.md").
      1. **Use AWS key** – AWS IoT FleetWise owns and manages the key.
      2. **Choose a different AWS Key Management Service key**
         – You manage AWS KMS keys that are in your
         account.

   2. To save your changes, choose **Submit**.

## Configure settings (AWS CLI)

In the AWS CLI, register the account to configure settings.

### IAM permission setup for account registration

To invoke the `RegisterAccount` API successfully, you need to include `iam:CreateServiceLinkedRole` in your IAM policy document. This API creates a service-linked role in your account that is used to publish AWS IoT FleetWise metrics to your CloudWatch. To verify whether the account is registered successfully, invoke the `GetRegisterAccountStatus` API and make sure the registration status is `REGISTRATION_SUCCESS`.

The following example shows a sample policy document for setting up permissions to `RegisterAccount` and `GetRegisterAccountStatus`:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iotfleetwise:RegisterAccount",
        "iotfleetwise:GetRegisterAccountStatus",
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

1. To configure settings, run the following command.

```
aws iotfleetwise register-account
```

2. To verify your settings, run
   the following command to retrieve the registration status.

###### Note

The service-linked role is only used to publish AWS IoT FleetWise metrics to CloudWatch. For more information, see [Using service-linked roles for
AWS IoT FleetWise](using-service-linked-roles.md "using-service-linked-roles.md").

```
aws iotfleetwise get-register-account-status
```

###### Example response

```
{
    "accountStatus": "REGISTRATION_SUCCESS",
    "creationTime": "2022-07-28T11:31:22.603000-07:00",
    "customerAccountId": "012345678912",
    "iamRegistrationResponse": {
        "errorMessage": "",
        "registrationStatus": "REGISTRATION_SUCCESS",
        "roleArn": "arn:aws:iam::012345678912:role/AWSIoTFleetwiseServiceRole"
    },
    "lastModificationTime": "2022-07-28T11:31:22.854000-07:00",
    }
}
```

The registration status can be one of the following:

- `REGISTRATION_SUCCESS` – The AWS resource is successfully
  registered.
- `REGISTRATION_PENDING` – AWS IoT FleetWise is processing the registration
  request. This process takes approximately five minutes to complete.
- `REGISTRATION_FAILURE` – AWS IoT FleetWise can't register the AWS resource.
  Try again later.
