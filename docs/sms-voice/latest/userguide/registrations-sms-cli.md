# Create a registration using the AWS CLI in

AWS End User Messaging SMS

The following section gives examples of how to create, populate, and submit a registration
using the AWS CLI. For examples of how to create and submit a Toll-free phone number
registration using python or shell script, see [Automate AWS End User Messaging US toll-free Number Registrations](https://aws.amazon.com/blogs/messaging-and-targeting/automate-us-tfn-registrations/ "https://aws.amazon.com/blogs/messaging-and-targeting/automate-us-tfn-registrations/").
Registrations vary from country to country, some are single page forms while others, like
10DLC, may require multiple forms to be submitted in a specific order. Check the [individual registration](registrations.md "registrations.md") for details on order and if you
need to upload any supporting documentation like a Letter of Authorization (LOA).

## Background

Some countries require you to register your company's identity to be able to purchase
an origination identity and review the messages you send to recipients in their
country.

- The registration information you provide may be reviewed by a third-party. The
  third-party varies from country to country but could be a governmental
  regulatory agency or mobile carrier that perform the review.
- The amount of time the third-party company takes to review your registration
  varies by registration type.

## Prerequisites

Before you begin you must:

- Install and configure the AWS CLI, see [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").
- An AWS account with [permissions](security-iam.md "security-iam.md") to use
  AWS End User Messaging SMS in the target region.
- A registrations **AssociationBehavior** specifies
  the order for when a registration can be associated with an origination identity
  and disassociated from an origination identity, see [SupportedAssociation](../../../pinpoint/latest/apireference_smsvoicev2/API_SupportedAssociation.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SupportedAssociation.md").
  - `ASSOCIATE_BEFORE_SUBMIT` The origination identity has to be supplied when
    submitting a registration.
  - `ASSOCIATE_ON_APPROVAL` This applies to all sender ID registrations. The sender ID
    will be automatically provisioned once the registration is
    approved.
  - `ASSOCIATE_AFTER_COMPLETE` This applies to phone number registrations when you must complete a registration first, then associate one or more phone numbers later.

###### Important

Once you purchase an origination identity you are changed for it regardless of the
registrations status, see [AWS End User
Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

Once you submit your registration you can not make any changes to the
registration or disassociate any resources with the registration until
after it has been reviewed by a third party and returned back to you.

The following are additional resources for registrations.

- [How to Build a Compliant SMS Opt-In Process](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-build-a-compliant-sms-opt-in-process-with-amazon-pinpoint/ "https://aws.amazon.com/blogs/messaging-and-targeting/how-to-build-a-compliant-sms-opt-in-process-with-amazon-pinpoint/")
- [10DLC Registration Best Practices to Send SMS with AWS End User Messaging](https://aws.amazon.com/blogs/messaging-and-targeting/10dlc-registration-best-practices-to-send-sms-with-amazon-pinpoint/ "https://aws.amazon.com/blogs/messaging-and-targeting/10dlc-registration-best-practices-to-send-sms-with-amazon-pinpoint/")

Use the [create-registration](../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration.md") command to create a new blank
registration. The **RegistrationType** parameter
determines the type of registration to create. If you don't know the value for the
type of registration you want to create then use the [describe-registration-type-definitions](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registration-type-definitions.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registration-type-definitions.md") command to
retrieve a list of all registration types.

The following examples show how to create a Toll-free number registration
form.

```
`$` aws pinpoint-sms-voice-v2 create-registration --registration-type US_TOLL_FREE_REGISTRATION --tags "Key=Name,Value=MyTFNRegistration"
```

On successful completion save the value of **RegistrationId** as it will be needed for other commands.

###### Note

To add a friendly name to your registration you must add a tag with the
**Key** set to `Name` and the
**Value** set to the friendly name to use.

You can also add tags to resources for billing purposes, see [Tag resources for billing](sms-billing-tag.md "sms-billing-tag.md").

The following example is partial output of the
`describe-registration-type-definitions` command. Because **AssociationBehavior** is set to `ASSOCIATE_BEFORE_SUBMIT`
the toll-free number must be purchased and associated with the registration before
the registration can be submitted for approval. For more information on **AssociationBehavior** and **DisassociationBehavior**, see [SupportedAssociation](../../../pinpoint/latest/apireference_smsvoicev2/API_SupportedAssociation.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SupportedAssociation.md").

```
{
    "RegistrationTypeDefinitions": [
        {
            "RegistrationType": "US_TOLL_FREE_REGISTRATION",
            "SupportedAssociations": [
                {
                    "ResourceType": "TOLL_FREE",
                    "IsoCountryCode": "US",
                    "AssociationBehavior": "ASSOCIATE_BEFORE_SUBMIT",
                    "DisassociationBehavior": "DISASSOCIATE_ALL_CLOSES_REGISTRATION"
                }
            ],
            "DisplayHints": {
                "Title": "US toll-free number registration"
            }
        },
...
```

Next you need to get the definitions for each field to know what the requirements
are, such as the maximum number of characters for the field.

Each registration is divided into sections and each section has one or more
fields. Use the [describe-registration-field-definitions](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registration-field-definitions.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registration-field-definitions.md") command to
retrieve all section and field definitions for a registration. You will need the
**FieldPath** for each field later to be able to
set its value. Also **FieldRequirement** is used to
determine if a field will be required or optional.

The following examples show how to retrieve field definitions for the Toll-free
registration form.

```
`$` aws pinpoint-sms-voice-v2 describe-registration-field-definitions --registration-type  US_TOLL_FREE_REGISTRATION
```

The following is partial output from the command:

```
{
    "RegistrationFieldDefinitions": [
        {
            "SectionPath": "companyInfo",
            "FieldPath": "companyInfo.companyName",
            "FieldType": "TEXT",
            "FieldRequirement": "REQUIRED",
            "TextValidation": {
                "MinLength": 1,
                "MaxLength": 100,
                "Pattern": "^(?=\\s*\\S)[\\s\\S]+$"
            },
            "DisplayHints": {
                "Title": "Company name",
                "ShortDescription": "Legal name which your company is registered under.",
                "ExampleTextValue": "Example Corp"
            }
        },
...
```

Depending on the registration you may be required to complete and attach a Letter
of Authorization (LOA), opt-in workflow, or another type of required document. Check
the [individual registration](registrations.md "registrations.md") for details and to
download any forms.

Use the [create-registration-attachment](../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration-attachment.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration-attachment.md") command to create
the registration attachment. You can either upload the file to an Amazon S3 bucket and
use the url or attach the document as part of the command. Use either **AttachmentUrl** or **AttachmentBody**, if both are specified then an exception is returned.
The maximum file size is 500KB and valid file extensions are PDF, JPEG, and PNG.

The following example shows how to create the registration attachment and use the
**AttachmentUrl** parameter.

```
`$` aws pinpoint-sms-voice-v2 create-registration-attachment --attachment-url s3://BucketName/FileName
```

On successful completion the command returns a **RegistrationAttachmentID** which is needed for other commands.

For more information on Amazon S3 commands such as creating a bucket or uploading a
file, see [Use high-level (s3) commands with the AWS
CLI](../../../cli/latest/userguide/cli-services-s3-commands.md "../../../cli/latest/userguide/cli-services-s3-commands.md").

Next you need to add values for all of the required fields returned from the
_Get the field definitions_ step, this includes any
attachments that you created. We recommend that you also complete any optional
fields where applicable to your use case. A field is required or optional depending
on the **FieldRequirement** value. Use the [put-registration-field-value](../../../cli/latest/reference/pinpoint-sms-voice-v2/put-registration-field-value.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/put-registration-field-value.md") command to set the
field values.

- The following examples show to add a value for the company name or text value.

```
`$` aws pinpoint-sms-voice-v2 put-registration-field-value --registration-id `RegID` --field-path `companyInfo.companyName` --text-value `AnyCompany`
```

In the preceding command replace the following:

    + Replace `RegID` with the registration id returned
     from the *Create a registration* step.
    + Replace `AnyCompany` with you company's
     name.

- The following examples show to add a value for a select field.

```
`$` aws pinpoint-sms-voice-v2 put-registration-field-value --registration-id `RegID` --field-path `messagingUseCase.monthlyMessageVolume` --text-choices `SelectValue`
```

In the preceding command replace the following:

    + Replace `RegID` with the registration id returned
     from the *Create a registration* step.
    + Replace `SelectValue` with one of the option
     values for the field.


    Use the [describe-registration-field-definitions](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registration-field-definitions.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registration-field-definitions.md")
     command to get the options for just one field:



    ```
    aws pinpoint-sms-voice-v2 describe-registration-field-definitions --registration-type  US_TOLL_FREE_REGISTRATION --field-paths `messagingUseCase.monthlyMessageVolume`
    ```


    ```
    {
        "RegistrationFieldDefinitions": [
            {
                "SectionPath": "messagingUseCase",
                "FieldPath": "messagingUseCase.monthlyMessageVolume",
                "FieldType": "SELECT",
                "FieldRequirement": "REQUIRED",
                "SelectValidation": {
                    "MinChoices": 1,
                    "MaxChoices": 1,
                    "Options": [
                        "10",
                        "100",
                        "1,000",
                        "10,000",
                        "100,000",
                        "250,000",
                        "500,000",
                        "750,000",
                        "1,000,000",
                        "5,000,000",
                        "10,000,000+"
                    ]
                },
                "DisplayHints": {
                    "Title": "Monthly SMS volume",
                    "ShortDescription": "Estimated number of SMS messages which will be sent from this toll-free number each month."
                }
            }
        ],
        "RegistrationType": "US_TOLL_FREE_REGISTRATION"
    }

    ```

- The following examples show how to add an attachment.

```
`$` aws pinpoint-sms-voice-v2 put-registration-field-value --registration-id `RegID` --field-path `messagingUseCase.optInImage` --registration-attachment-id `RegistrationAttachmentID`
```

In the preceding command replace the following:

    + Replace `RegID` with the registration id returned
     from the *Create a registration* step.
    + Replace `RegistrationAttachmentID` with the
     registration attachment id returned from the *Create
     attachments* step.

###### Note

Once you purchase an origination identity you are charged for it regardless of
registration status, see [AWS End User
Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

If the registration's **AssociationBehavior** is
`ASSOCIATE_AFTER_COMPLETE` then you do not need to purchase or
associate the origination identity until after the registration has been
submitted and approved.

Now you need to request an origination identity which will later be associated
with the registration. This example shows how to use the [request-phone-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.md") command to request a toll-free
phone number through the AWS CLI. Use the [request-sender-id](../../../cli/latest/reference/pinpoint-sms-voice-v2/request-sender-id.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/request-sender-id.md") to request a sender ID.

```
`$` aws pinpoint-sms-voice-v2 request-phone-number --iso-country-code US --message-type TRANSACTIONAL --number-capabilities SMS --number-type TOLL_FREE
```

On successful completion the command returns the phone number unique identifier
which is needed to associate the phone number with the registration.

###### Note

If the registration's **AssociationBehavior** is
`ASSOCIATE_AFTER_COMPLETE` then you do not need to purchase or
associate the origination identity until after the registration has been
submitted and approved.

To associate an origination identity to the registration use the [create-registration-association](../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration-association.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration-association.md") AWS CLI command.

```
`$` aws pinpoint-sms-voice-v2 create-registration-association --registration-id `RegID` --resource-id `PhoneNumberID`
```

In the preceding command replace the following:

- Replace `RegID` with the registration id returned
  from the _Create a registration_ step.
- Replace `PhoneNumberID` with the phone number id
  returned from the _Request an origination identity_
  step.

###### Note

This command is used to associate any applicable resource with the registration. For example, it can be used to associate a 10DLC campaign registration with a 10DLC brand registration.

Once you submit your registration you will not be able to make any changes to it.
Review you registration to make sure that all of your data is correct before
submitting it.

###### Important

Once you submit your registration you can not make any changes to the registration or
disassociated any resources from the registration until after it has been
reviewed by a third party and returned back to you.

To submit a registration with the AWS CLI use the [submit-registration-version](../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration-association.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/create-registration-association.md") command.

```
`$` aws pinpoint-sms-voice-v2 submit-registration-version --registration-id `RegID`
```

In the preceding command replace the following:

- Replace `RegID` with the registration id returned
  from the _Create a registration_ step.
  Once your registration has been submitted you can check its status using the
  [describe-registrations](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registrations.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-registrations.md") command or [console](registrations-status.md "registrations-status.md").

If the registration's **AssociationBehavior** is
`ASSOCIATE_AFTER_COMPLETE` you can purchase an origination identity
and associate it with the registration, once the registration's status is set to
**COMPLETE**.

If your registration's status is changed to **REQUIRES_UPDATES** then you can find and [edit the flagged fields](registrations-edit.md "registrations-edit.md") and resubmit the
registration. For a list of registration rejection reasons, see [Help with registration rejections](help-registration-rejection-reason.md "help-registration-rejection-reason.md"). If you require help from Support with
your registration rejection you can [open a ticket](registrations-request-support.md "registrations-request-support.md").
