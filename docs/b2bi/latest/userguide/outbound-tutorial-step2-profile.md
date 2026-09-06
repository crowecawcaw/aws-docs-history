

# Step 2: Creating your business profile
<a name="outbound-tutorial-step2-profile"></a>

**Note**  
If you created a profile for inbound EDI processing, you can reuse it here. Profiles can be used across multiple trading capabilities and partnerships.

A profile stores your business contact information and serves as the foundation for all your AWS B2B Data Interchange activities. It represents your organization in trading partnerships and provides logging configuration for monitoring transformations.

**To create a business profile**

1. Open the AWS B2B Data Interchange console at [https://console.aws.amazon.com/b2bi/](https://console.aws.amazon.com/b2bi/).

1. In the navigation pane, choose **Profiles**.

1. Choose **Create profile**.

1. In the **Profile details** section, enter the profile information for your tutorial.

1. Leave **Logging** enabled (recommended for monitoring).

1. Optionally, add tags such as Environment: Tutorial and Department: Procurement.

1. Choose **Create profile**.

## Required fields
<a name="tutorial-profile-required-fields"></a>
+ Profile name
+ Business name
+ Email address
+ Phone number

## Example data for this tutorial
<a name="outbound-step2-configuration-summary"></a>
+ **Profile name**: **AcmeCorpOutboundProfile**
+ **Business name**: **Acme Corporation**
+ **Email**: **edi-outbound@acmecorp.example.com**
+ **Phone**: **\+1-555-012-4567**
+ **Additional tag**: Key: **Direction**, Value: **Outbound**