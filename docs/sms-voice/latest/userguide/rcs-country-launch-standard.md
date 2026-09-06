

# Standard country launch registration
<a name="rcs-country-launch-standard"></a>

The following countries use the standard baseline registration form with no additional out-of-band requirements:
+ Colombia (CO)
+ Czech Republic (CZ)
+ Denmark (DK)
+ Dominican Republic (DO)
+ Guatemala (GT)
+ Italy (IT)
+ Norway (NO)
+ Poland (PL)
+ Slovakia (SK)
+ Sweden (SE)

For these countries, the entire registration process takes place in the AWS End User Messaging console or API. There are no additional emails to send, documents to sign, or third-party verifications to complete outside the console.

## Registration form fields
<a name="rcs-country-launch-standard-form"></a>

The standard baseline form collects the following information:

**Brand website** (required)  
Your brand's public website URL.

**Video URL** (required)  
A URL to a screen recording that demonstrates your RCS messaging experience. For detailed video requirements, see [Launch video requirements](rcs-compliance-video.md).

**Traffic origin** (required)  
Whether your messaging traffic originates domestically or internationally.

**ISV indicator** (required)  
Whether you are an Independent Software Vendor (ISV) sending messages on behalf of another company. If yes, you must provide additional details about the content provider (company name, company ID, website, legal entity type, and stock information if publicly traded).

**Primary contact** (required)  
Contact name, email address, and job title for the person responsible for this RCS registration.

**Agent details** (required)  
Brand name, service name, sender display name, use case category, agent description, logo image (224×224 PNG), banner image (1440×448 PNG/JPEG), accent color (hex code), contact information (phone, email, or website with labels), privacy policy URL, terms and conditions URL, monthly RCS volume estimate, and average per-user message frequency.

**Message samples** (required)  
Up to 10 sample messages that represent the types of RCS messages you intend to send. At least one sample is required.

**Opt-in workflow** (required)  
Description of how end users opt in to receive your messages, including the opt-in method, user experience flow description, and a screenshot of the opt-in process.

**Compliance keywords** (required)  
Your configured HELP response message, STOP response message, opt-in confirmation message, and opt-out details describing how users can stop receiving messages.

**Note**  
Most agent details fields are auto-populated from your testing agent configuration. Review and adjust them for the target country if needed (for example, localized descriptions or country-specific contact information).

After you submit the registration, the carrier review proceeds through the standard approval workflow. No additional action is required from you unless the registration enters the REQUIRES\_UPDATES state. For general compliance guidance, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).