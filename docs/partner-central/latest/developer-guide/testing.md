

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Testing in a sandbox
<a name="testing"></a>

Partners can use a sandbox to test and validate their AWS Partner Central API interactions in a secure and isolated environment, ensuring smooth operation before promoting their solution to the production environment. AWS offers a dynamic sandbox to AWS Partner Central API users that returns responses similar to the production environment. AWS does not provide a user interface to the sandbox environment. Therefore, partners need to rely on the programmatic responses to test their solutions.

## Access to the sandbox environment
<a name="access-sandbox"></a>

AWS does not provide a user interface to the sandbox environment. You access the sandbox only through the AWS Partner Central API. Before you can make any sandbox API calls, you must first register in the AWS (production) catalog through the Partner Central Console UI. In the Partner Central Console UI, you complete Know Your Business (KYB) and Identity Verification (IDV).

You must complete AWS catalog registration, including KYB and IDV, before you can access the sandbox. If you call `CreatePartner` in the `Sandbox` catalog before you complete this registration, the call fails.

Each request includes a `catalog` parameter, which determines the data environment. When you set `catalog` to `AWS`, the request references production data. When you set `catalog` to `Sandbox`, the request references sandbox data.

To set up sandbox access, complete the following steps in order:

1. Check whether a `Sandbox` partner account already exists. Call the `ListPartners` API with `catalog` set to `Sandbox`. Use the following request body:

   ```
   {
     "Catalog": "Sandbox"
   }
   ```

   Evaluate the response:
   + If the response returns a non-empty list, the account already exists and you do not need to register. Go to Step 4 to test the other APIs.
   + If the response returns an empty list, continue to Step 2.
**Note**  
If you migrated from PC2.0 to PC3.0, you might already have a `Sandbox` partner account that was auto-created during migration.

1. Complete AWS catalog registration. This registration is a prerequisite, and you complete it in the Partner Central Console UI. It is required because:
   + KYB and IDV are account-level checks.
   + You can complete these verifications only through the Console UI registration flow.
   + The `CreatePartner` API in any catalog fails if you have not completed KYB and IDV for the AWS account.

   For more information, see [Registering as an AWS Partner](https://docs.aws.amazon.com/partner-central/latest/getting-started/registering.html). Account linking is part of the setup, but it is not by itself sufficient for sandbox access. For more information, see [Linking your AWS account to AWS Partner Central account](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html).

1. Register in the sandbox using the `CreatePartner` API. After you complete AWS catalog registration, call `CreatePartner` with `catalog` set to `Sandbox`. Use the following request body:

   ```
   {
     "Catalog": "Sandbox",
     "ClientToken": "unique-idempotency-token",
     "LegalName": "Your Company Name",
     "PrimarySolutionType": "SOFTWARE_PRODUCTS",
     "AllianceLeadContact": {
       "FirstName": "Jane",
       "LastName": "Doe",
       "Email": "jane@example.com",
       "BusinessTitle": "VP Partnerships"
     },
     "EmailVerificationCode": "123456"
   }
   ```

   Note the following important details:
   + `EmailVerificationCode` – The sandbox disables email verification. It accepts any random 6-digit string (for example, `123456`) and sends no email.
   + `Tags` – Optional.

1. Begin testing the downstream APIs. The `Sandbox` partner account is now ready. All requests must include `catalog` set to `Sandbox`.

## Important details about the sandbox environment
<a name="important-details"></a>

1. Data refresh: Once per year, AWS refreshes the data in the sandbox environment (typically at the beginning of the year). After this refresh, you may lose some of the data in your testing environment.

1. Testing scope: The sandbox environment is typically used for functional testing and not for testing scalability or performance. 

**Topics**
+ [Access to the sandbox environment](#access-sandbox)
+ [Important details about the sandbox environment](#important-details)
+ [Testing in a sandbox for the AWS Partner Central Account API](testing-sandbox-account.md)
+ [Testing in a sandbox for the AWS Partner Central Selling API](testing-sandbox.md)
+ [Testing in a sandbox for the AWS Partner Central Benefits API](testing-sandbox-benefits.md)
+ [Testing in a sandbox for the AWS Partner Central Channel API](testing-sandbox-channel.md)
+ [Testing in a sandbox for the AWS Partner Central Revenue Measurement API](testing-sandbox-prm.md)