

# Move to the Advanced tier
<a name="nx-notify-scale-tiers"></a>

All new configurations start on the Basic tier, which provides immediate access with conservative limits designed for getting started and low-volume use cases. The Basic tier supports a daily message limit of 200 messages per configuration, 1 transaction per second (TPS), and 30 pre-approved low-risk countries, and allows long codes, toll-free numbers, and sender IDs. The Advanced tier removes the daily message limit, raises throughput to 25 TPS, supports all available countries, adds short codes, and allows configurable country allow and block rules. SMS Protect is mandatory on both tiers.

To upgrade from Basic to Advanced, you complete tier upgrade verification by demonstrating that you have a legitimate end-user consent mechanism in place. You select your opt-in method (verbal or digital form), provide proof of opt-in (a call script or IVR flow for verbal consent, or a screenshot or URL of the form or page for digital consent), and provide information about your business and use case. Your opt-in process must include links to your terms and conditions and privacy policy pages.

Before you request the upgrade, make sure your messaging meets the mobile carrier requirements that the reviewer checks. Your terms and conditions, privacy policy, and opt-in flow must each include specific required language, and you must provide customer support contact information. For the exact requirements and copy-ready examples, see [Compliance and mobile carrier prerequisites](nx-notify-scale-compliance.md). Prepare these pages first, because the upgrade review validates them and a submission that is missing the required language is rejected.

You request the upgrade from the console or with the AWS CLI. Upon approval, the configuration tier is automatically upgraded.

------
#### [ Console ]

**To upgrade a configuration to the Advanced tier**

1. Open the AWS End User Messaging SMS console and choose your Notify configuration.

1. Choose the **Tier upgrade** tab, and then choose **Upgrade to Advanced**.

1. Complete the brand verification form with your opt-in method and your proof of opt-in.

1. Submit the request.

------
#### [ AWS CLI ]

The tier upgrade process uses the existing registration system.

1. Create a brand verification registration.

   ```
   $ aws pinpoint-sms-voice-v2 create-registration \
   > --registration-type MANAGED_ROUTES_BRAND_VERIFICATION
   ```

1. Complete the registration fields with `put-registration-field-value`.

1. Submit the registration.

   ```
   $ aws pinpoint-sms-voice-v2 submit-registration-version \
   > --registration-id {{reg-1234567890abcdef0}}
   ```

------

Upgrade requests are reviewed using a combination of automated processing and human review. Reviewers validate that your opt-in mechanism is genuine, that end users are clearly consenting to receive messages, and that your use case aligns with code verification messaging. Most requests are processed within 3 to 5 business days. The `TierUpgradeStatus` field on your configuration shows the current status: `BASIC`, `PENDING_UPGRADE`, `ADVANCED`, or `REJECTED`.