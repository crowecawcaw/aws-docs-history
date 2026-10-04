

# Publishing your product in AWS GovCloud (US)
<a name="govcloud-publishing"></a>

AWS Marketplace supports product listing in the AWS GovCloud (US) Regions. You can publish AMI-based and SaaS-based products in AWS GovCloud (US) to make them available to government agencies and customers with regulated workloads. This section describes the requirements and steps for publishing your product in AWS GovCloud (US).

## Requirements
<a name="govcloud-publishing-requirements"></a>

Before you can publish a product in AWS GovCloud (US), you must meet the following requirements:
+ You must be a U.S. entity incorporated and based on U.S. soil.
+ You must be a U.S. Person (U.S. Citizen or active Green Card holder).
+ You must be able to handle International Traffic in Arms Regulations (ITAR) export-controlled data.
+ You must have an active AWS GovCloud (US) account (also referred to as an AWS GovCloud (US) entitlement).
+ You must have a direct agreement with AWS as a Direct Customer.
+ You must comply with all applicable export control requirements.

**Note**  
Software vendors who want to be listed in the AWS GovCloud (US) Regions must sign up as a Direct Customer, whether or not they are resellers.

**Note**  
Each AWS GovCloud (US) account is linked 1:1 with a standard AWS account for billing, service, and support. You must have an existing standard AWS account before signing up for AWS GovCloud (US). AWS recommends creating a new, dedicated standard AWS account solely for AWS GovCloud (US) sign-up and billing.

For more information about signing up for a AWS GovCloud (US) account, see [AWS GovCloud (US) Sign Up](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-sign-up.html).

## Publishing an AMI product in AWS GovCloud (US)
<a name="govcloud-publishing-ami"></a>

To publish an AMI-based product in the AWS GovCloud (US) Region, you must request access to publish into the AWS GovCloud (US) Regions. This is a one-time request. After you are approved, you do not need to submit this request again for future AMI products.

1. Confirm that you meet the prerequisite in the [Requirements](#govcloud-publishing-requirements) section: you must already have an active AWS GovCloud (US) entitlement.

1. Submit a request through the AWS Marketplace Management Portal using the Support Form. In your request, include the following:
   + Your AWS account ID.
   + Your GovCloud account ID.
   + In the inquiry details, state that you are requesting access to publish into the AWS GovCloud (US) Regions.

1. Wait for your request to be reviewed by the AWS Marketplace operations team.

1. After you receive approval, you can submit your AMI product for publication in the AWS GovCloud (US) Regions following the standard product submission process. For AMI products submitted to AWS GovCloud (US), you must agree to the applicable export control requirements.

To find your AWS GovCloud (US) account ID, sign in to the AWS GovCloud (US) console. Choose *Support*, then *Support Center*. Your 12-digit account ID appears in the navigation pane. For more information, see [Your AWS GovCloud (US) account ID and its alias](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-account-id.html) in the *AWS GovCloud (US) User Guide*.

## Publishing a SaaS product in AWS GovCloud (US)
<a name="govcloud-publishing-saas"></a>

To publish a SaaS-based product in the AWS GovCloud (US) Region, you must request access to publish into the AWS GovCloud (US) Regions. This is a one-time request. After you are approved, you do not need to submit this request again for future SaaS products.

1. Confirm that you meet the prerequisite in the [Requirements](#govcloud-publishing-requirements) section: you must already have an active AWS GovCloud (US) entitlement.

1. Create a commercial SaaS product using the self-service listing experience in the AWS Marketplace Management Portal.
**Important**  
The new UI experience is not currently supported for creating GovCloud SaaS products.

1. Publish the listing to limited view.

1. After your listing successfully publishes to limited view, submit a support request through the AWS Marketplace Management Portal Support Form. Categorize the request as *Commercial Marketplace > GovCloud > Other support*. In your request, include the following:
   + Product Title
   + Product ID
   + Product Code

A member of the AWS Managed Seller Operations team will assist you with publishing your product in AWS GovCloud (US).

### Additional requirements for GovCloud SaaS products
<a name="govcloud-publishing-saas-additional-requirements"></a>

SaaS products offered exclusively in the AWS GovCloud (US) Regions must meet the following additional requirements:

Product title  
You must include "GovCloud" in the product title.

Architecture documentation  
You must explain the architectural boundaries between AWS GovCloud (US) and other AWS Regions. Describe the intended use cases for the product, and note any workloads that are not recommended. Submit architecture diagrams for review. AWS does not make these diagrams public.