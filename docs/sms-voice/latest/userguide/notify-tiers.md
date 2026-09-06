

# Notify tiers
<a name="notify-tiers"></a>

Notify offers two service tiers with different capabilities and limits. All new configurations start on the Basic tier. You can upgrade to the Advanced tier after completing tier upgrade verification.

## Basic tier
<a name="notify-tiers-basic"></a>

Basic tier provides immediate access to Notify with conservative limits designed for getting started and low-volume use cases.


**Basic tier capabilities**  

| Capability | Basic tier | 
| --- | --- | 
| Access | Immediate after configuration creation | 
| Daily message limit | 200 messages | 
| Transactions per second (TPS) | 1 TPS | 
| Supported countries | 30 pre-approved low-risk countries | 
| Identity types | Long codes, toll-free, sender IDs | 
| SMS Protect | Mandatory (cannot be disabled) | 
| Country configuration | Fixed (pre-approved list only) | 
| Default spend limit | See [Notify spend limits](notify-spend-limits.md) | 
| Customer-owned identity support | Yes (optional pool association) | 

## Advanced tier
<a name="notify-tiers-advanced"></a>

Advanced tier unlocks higher limits, premium identities, and configurable country rules after tier upgrade verification.


**Advanced tier capabilities**  

| Capability | Advanced tier | 
| --- | --- | 
| Access | After tier upgrade verification | 
| Daily message limit | Unlimited | 
| Transactions per second (TPS) | 25 | 
| Supported countries | All supported countries | 
| Identity types | Short codes, long codes, toll-free, sender IDs | 
| SMS Protect | Mandatory | 
| Country configuration | Configurable allow/block rules | 
| Default spend limit | See [Notify spend limits](notify-spend-limits.md) | 
| Customer-owned identity support | Yes (optional pool association) | 

## Upgrading to Advanced tier
<a name="notify-tier-upgrade"></a>

To upgrade from Basic to Advanced tier, you must complete tier upgrade verification by demonstrating that you have a legitimate end-user consent mechanism in place.

### What you need to provide
<a name="notify-tier-upgrade-requirements"></a>

Opt-in method  
Select how you collect consent from your end users:  
+ **Verbal** – Consent collected via phone call (for example, customer service call or IVR confirmation).
+ **Digital form** – Consent collected via digital interaction (for example, web signup form, mobile app account creation, checkout checkbox, or terms acceptance).

Proof of opt-in  
Provide evidence of your consent collection process:  
+ For verbal opt-in: Call script or IVR flow showing where consent is obtained.
+ For digital opt-in: Screenshot or URL of the form or page where users give consent.

Business documentation  
Provide information about your business and use case.

**Important**  
Your opt-in process must include links to your terms and conditions and privacy policy pages. For the required language and examples, see [Notify mobile carrier prerequisites](notify-compliance.md).

### Opt-in examples
<a name="notify-tier-upgrade-optin-examples"></a>

**Verbal opt-in (IVR or customer service call)**  
"To verify your identity, we'll send a one-time verification code to your mobile phone. By providing your phone number, you consent to receive this automated text message. Message and data rates may apply. Message frequency varies. Reply HELP for help or STOP to cancel. Do you consent to receive this verification code?"

**Digital form opt-in (web or mobile app)**  
"By entering my phone number and clicking 'Send Code,' I consent to receive an automated one-time verification code from [Your Brand] at the number provided. Message and data rates may apply. Message frequency varies. Reply HELP for help, STOP to cancel. Terms of use \| Privacy policy"

**Note**  
These examples follow CTIA Messaging Principles and Best Practices for informational messaging. OTP verification codes are considered informational (not promotional) because the user initiates the request. While STOP/HELP disclosures are technically optional for single transactional messages, including them is recommended for carrier compliance, especially when using US short codes.

### How to request an upgrade
<a name="notify-tier-upgrade-request"></a>

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, choose **Notify configurations**.

1. Select your configuration and choose the **Tier upgrade** tab.

1. Choose **Upgrade to Advanced**.

1. Complete the brand verification form with your opt-in method and proof.

1. Submit the request.

------
#### [ AWS CLI ]

The tier upgrade process uses the existing registration system:

1. Create a brand verification registration:

```
aws pinpoint-sms-voice-v2 create-registration \
  --registration-type MANAGED_ROUTES_BRAND_VERIFICATION
```

2. Complete the registration fields using `put-registration-field-value`.

3. Submit the registration:

```
aws pinpoint-sms-voice-v2 submit-registration-version \
  --registration-id {{reg-1234567890abcdef0}}
```

Upon approval, the Notify configuration tier is automatically upgraded.

------

### Review process
<a name="notify-tier-upgrade-review"></a>

Upgrade requests are reviewed using a combination of automated processing and human review. Reviewers validate that your opt-in mechanism is genuine, end users are clearly consenting to receive messages, and your use case aligns with code verification messaging.

Most requests are processed within 3–5 business days.


**Upgrade review outcomes**  

| Outcome | Description | 
| --- | --- | 
| Approved | Your configuration is upgraded to Advanced tier. | 
| More information needed | Additional documentation is required. You'll receive details on what's needed. | 
| Rejected | The request did not meet verification requirements. You can resubmit with updated information. | 

### Tracking upgrade status
<a name="notify-tier-upgrade-status"></a>

The `TierUpgradeStatus` field on your Notify configuration shows the current status:


**TierUpgradeStatus values**  

| Status | Description | 
| --- | --- | 
| BASIC | No upgrade has been requested. The configuration is at Basic tier. | 
| PENDING\_UPGRADE | An upgrade request has been submitted and is under review. | 
| ADVANCED | The upgrade was approved. The configuration is at Advanced tier. | 
| REJECTED | The upgrade request was rejected. You can submit a new registration with corrected information. | 

## Your compliance responsibilities
<a name="notify-tiers-compliance"></a>

Regardless of tier, you are responsible for:
+ **Obtaining consent** – Get appropriate consent from recipients before sending messages. For code verification, this typically means the user initiated the action that triggers the OTP (for example, logging in, creating an account, or resetting a password).
+ **Complying with applicable laws** – Follow legal requirements for your use case and destination countries, including the Telephone Consumer Protection Act (TCPA) in the US, GDPR in the EU, and other applicable regulations.
+ **Following carrier policies** – Comply with carrier policies that apply to your messaging. AWS will make reasonable efforts to notify you of changes to carrier policies.

For more information, see [Notify mobile carrier prerequisites](notify-compliance.md).