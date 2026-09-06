

# Create a registration using the AWS CLI in AWS End User Messaging SMS
<a name="registrations-sms-cli"></a>

The following section gives examples of how to create, populate, and submit a registration using the AWS CLI. For examples of how to create and submit a Toll-free phone number registration using python or shell script, see [Automate AWS End User Messaging US toll-free Number Registrations](https://aws.amazon.com/blogs/messaging-and-targeting/automate-us-tfn-registrations/). Registrations vary from country to country, some are single page forms while others, like 10DLC, may require multiple forms to be submitted in a specific order. Check the [individual registration](registrations.md) for details on order and if you need to upload any supporting documentation like a Letter of Authorization (LOA).

## Background
<a name="registrations-sms-cli-contextual"></a>

Some countries require you to register your company's identity to be able to purchase an origination identity and review the messages you send to recipients in their country.
+ The registration information you provide may be reviewed by a third-party. The third-party varies from country to country but could be a governmental regulatory agency or mobile carrier that perform the review. 
+ The amount of time the third-party company takes to review your registration varies by registration type.

## Prerequisites
<a name="registrations-sms-cli-prerequisite"></a>

Before you begin you must:
+ Install and configure the AWS CLI, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
+ An AWS account with [permissions](security-iam.md) to use AWS End User Messaging SMS in the target region.
+ A registrations **AssociationBehavior** specifies the order for when a registration can be associated with an origination identity and disassociated from an origination identity, see [SupportedAssociation](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SupportedAssociation.html). 
  + `ASSOCIATE_BEFORE_SUBMIT` The origination identity has to be supplied when submitting a registration.
  + `ASSOCIATE_ON_APPROVAL` This applies to all sender ID registrations. The sender ID will be automatically provisioned once the registration is approved.
  + `ASSOCIATE_AFTER_COMPLETE` This applies to phone number registrations when you must complete a registration first, then associate one or more phone numbers later.
**Important**  
Once you purchase an origination identity you are changed for it regardless of the registrations status, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).  
Once you submit your registration you can not make any changes to the registration or disassociate any resources with the registration until after it has been reviewed by a third party and returned back to you.

The following are additional resources for registrations.
+ [How to Build a Compliant SMS Opt-In Process](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-build-a-compliant-sms-opt-in-process-with-amazon-pinpoint/)
+ [10DLC Registration Best Practices to Send SMS with AWS End User Messaging](https://aws.amazon.com/blogs/messaging-and-targeting/10dlc-registration-best-practices-to-send-sms-with-amazon-pinpoint/)

## Check your registrations status (describe-registrations AWS CLI command)
<a name="registrations-sms-cli_next_steps"></a>

Once your registration has been submitted you can check its status using the [describe-registrations](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-registrations.html) command or [console](registrations-status.md).

If the registration's **AssociationBehavior** is `ASSOCIATE_AFTER_COMPLETE` you can purchase an origination identity and associate it with the registration, once the registration's status is set to **COMPLETE**.

If your registration's status is changed to **REQUIRES\_UPDATES** then you can find and [edit the flagged fields](registrations-edit.md) and resubmit the registration. For a list of registration rejection reasons, see [Gen-AI Feedback on Registrations](registrations-genai-feedback.md). If you require help from Support with your registration rejection you can [open a ticket](registrations-request-support.md).