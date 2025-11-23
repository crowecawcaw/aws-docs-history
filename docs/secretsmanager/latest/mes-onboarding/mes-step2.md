# Step 2: Provide integration specifications

_Duration: Typically one to two weeks._

After reaching alignment with the Secrets Manager team, you need to provide the following
details to begin the onboarding process. These include essential details about your
service along with technical details.

The Secrets Manager team reviews these details. After they are confirmed, the team onboards you
as an integration partner.

You must provide all of the information to begin.

###### Prerequisite

You must be a member of the AWS Partner Network. For more information about the
benefits of being a member, see [Join
the AWS Partner Network](https://aws.amazon.com/partners/ "https://aws.amazon.com/partners/").

Share the following details with the Secrets Manager team:

- Your AWS Partner Network ID.
- The name of your service.
- A 50-word or less description of the use case for your secret.
- A 50-word summary of your secret type to help customers identify the secret
  that they are generating. If your service supports more than one secret type,
  each must be onboarded separately.
- The format of your secret. Secrets Manager uses the format to validate that customer
  provided secret metadata complies with your specific format. For example:

```
{
  "consumerKey":"<client ID>",
  "consumerSecret":"<client secret>",
  "baseUri":"https://<domain>.my.example.com",
  "appId":"<app ID>",
  "consumerId":"<consumer ID>"
}
```

- The defined rotation strategy for your secret. Your customer can choose from
  the supported rotation strategies when creating secrets.
  - [Single user rotation](secrets-manager-mes-onboarding.md#single-user "secrets-manager-mes-onboarding.md#single-user")
  - [Alternating users rotation (requires
    support for multiple active users)](secrets-manager-mes-onboarding.md#alternating-user "secrets-manager-mes-onboarding.md#alternating-user")

- The rotation configuration that Secrets Manager uses to run the rotation workflow.
  Typical configuration parameters are:
  - Sample Java code that has your specific rotation workflow logic to
    rotate the secret and update Secrets Manager.
  - The specific URL of the service endpoint that Secrets Manager invokes as part of
    the rotation workflow. Include availability and response time
    requirements. Also include Region-specific URLs if applicable.
  - Authentication mechanisms for AWS to access the URL.
  - The rotation schedule that customers can define for their secrets.
    This value is used as a default if the customer doesn't specify a value.
    Choose one of the following: 4 hrs | 7 days | 30 days.

- Help text and placeholder text for customer visible fields.
- Any additional service-specific details or requirements.
  Submit the information to the following email address:

- aws-secrets-mgr-partner-onboarding@amazon.com
  With the subject line:

- [Third-party software vendor name] partner onboarding request
