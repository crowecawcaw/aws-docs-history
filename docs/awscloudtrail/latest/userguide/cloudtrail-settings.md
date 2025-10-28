# Configure CloudTrail settings

You can use the **Settings** page on the CloudTrail console to configure and
review CloudTrail settings, such as managing delegated administrators for an AWS Organizations organization
and viewing any service-linked channels created for your account.

**To access the **Settings** page**

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. Choose **Settings** in the left navigation pane of the CloudTrail
   console.
3. Review and update your settings as needed.

The following settings are available:

    * [Organization delegated
     administrators](cloudtrail-delegated-administrator.md "cloudtrail-delegated-administrator.md") – If you have an AWS Organizations organization, you
     can view CloudTrail delegated administrators, add delegated administrators (up to
     three maximum), and remove delegated administrators. Only the organization's
     management account can add or remove delegated administrators.


    The organization's management account can assign any account within the
     organization to act as a CloudTrail delegated administrator to manage the
     organization's trails and event data stores on behalf of the
     organization.
    * [Viewing service-linked channels](cloudtrail-service-linked-channels.md "cloudtrail-service-linked-channels.md") – You can
     view any service-linked channels created for your account.


    AWS services can create a service-linked channel to receive CloudTrail events
     on your behalf. The AWS service creating the service-linked channel
     configures advanced event selectors for the channel and specifies whether
     the channel applies to all AWS Regions, or a single AWS Region.
