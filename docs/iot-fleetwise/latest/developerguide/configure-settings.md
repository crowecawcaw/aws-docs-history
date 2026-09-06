

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Configure your AWS IoT FleetWise settings
<a name="configure-settings"></a>

You can use the AWS IoT FleetWise console or API to configure settings for Amazon CloudWatch Logs metrics, Amazon CloudWatch Logs, and encrypt data with an AWS managed key.

With CloudWatch metrics, you can monitor AWS IoT FleetWise and other AWS resources. You can use CloudWatch metrics to collect and track metrics, such as to determine if there is an exceeded service limit. For more information about CloudWatch metrics, see [Monitor AWS IoT FleetWise with Amazon CloudWatch](monitoring-cloudwatch.md). 

With CloudWatch Logs, AWS IoT FleetWise sends log data to a CloudWatch log group, where you can use it to identify and mitigate any issues. For more information about CloudWatch Logs, see [Configure AWS IoT FleetWise logging](logging-cw.md).

With data encryption, AWS IoT FleetWise uses AWS managed keys to encrypt data. You can also choose to create and manage keys with AWS KMS. For more information about encryption, see [Data encryption in AWS IoT FleetWise](data-encryption.md).

## Configure settings (console)
<a name="configure-settings-cloud"></a>

If you aren't already signed in to your AWS account, sign in, then open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise/).

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. On the left pane, choose **Settings**.

1. In **Metrics**, choose **Enable**. AWS IoT FleetWise automatically attaches a CloudWatch managed policy to the service-linked role and enables CloudWatch metrics.

1. In **Logging**, choose **Edit**.

   1. In the **CloudWatch logging** section, enter the **Log group**.

   1. To save your changes, choose **Submit**.

1. In the **Encryption** section, choose **Edit**.

   1. Choose the type of key that you want to use. For more information, see [Key management in AWS IoT FleetWise](key-management.md).

      1. **Use AWS key** – AWS IoT FleetWise owns and manages the key.

      1. **Choose a different AWS Key Management Service key** – You manage AWS KMS keys that are in your account.

   1. To save your changes, choose **Submit**.

## Configure settings (AWS CLI)
<a name="configure-settings-cli"></a>

In the AWS CLI, register the account to configure settings.

### IAM permission setup for account registration
<a name="iam-permissions-register-account"></a>

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

1. To verify your settings, run the following command to retrieve the registration status.
**Note**  
The service-linked role is only used to publish AWS IoT FleetWise metrics to CloudWatch. For more information, see [Using service-linked roles for AWS IoT FleetWise](using-service-linked-roles.md).

   ```
   aws iotfleetwise get-register-account-status
   ```  
**Example response**  

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
+ `REGISTRATION_SUCCESS` – The AWS resource is successfully registered.
+ `REGISTRATION_PENDING` – AWS IoT FleetWise is processing the registration request. This process takes approximately five minutes to complete.
+ `REGISTRATION_FAILURE` – AWS IoT FleetWise can't register the AWS resource. Try again later.