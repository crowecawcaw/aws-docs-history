# Rejection troubleshooting

When your registration is denied, the AWS End User Messaging SMS console displays a rejection reason. These
rejection reasons apply to all US registration types including 10DLC campaigns, Toll-Free
numbers, and Short Codes. Use this guide to identify your rejection, understand what went
wrong, and determine how to fix it.

Each entry shows the exact title displayed in the console, the API ENUM value returned
in the registration response, a description of the issue, what you need to fix, and whether
you can resubmit.

## Brand Identity

Issues with your brand registration, business verification, EIN, contact information, and brand-level compliance.

Brand Identity rejection reasons| Console title | ENUM value | Description | What to fix | Resubmittable |
| --- | --- | --- | --- | --- |
| Brand address invalid | `BRAND_ADDRESS_INVALID` | The brand's physical address cannot be verified. | Confirm the physical address is correct, complete, and matches public business records. Resubmit with the corrected address. | Yes |
| Invalid brand email | `BRAND_EMAIL_INVALID_OR_MISSING` | The brand's email address is missing or invalid. It must not be from a public domain provider such as Gmail, Yahoo, or Outlook. | Use a branded email domain associated with your business (for example, support@yourbusiness.com). | Yes |
| Public email domain | `BRAND_EMAIL_PUBLIC_DOMAIN` | The brand's email domain is from a public email provider. | Replace with an email address using your business domain. | Yes |
| Invalid brand business connection | `BRAND_INVALID_BUSINESS_CONNECTION` | The registered brand is an ISV, reseller, or government entity rather than the end brand whose name appears in messages. | Register the end brand – the business whose name the end user sees in messages. The brand must be the content provider. | Yes |
| Brand multi-use | `BRAND_MULTI_USE` | The same Employer Identification Number (EIN) is used for multiple brands. | Register only the minimum number of brands per EIN. Do not resubmit until brand registration is updated. | Yes |
| Non-compliant brand affiliation | `BRAND_NON_COMPLIANT_SWEEPSTAKES` | Brand or website references lead generation, affiliate marketing, gambling, illegal substances, third-party job boards, sweepstakes, or SHAFT content prohibited by mobile operators. | Remove prohibited content associations from your brand and website. If the rejection specifies content that does not apply to your business, open a technical support case. See [Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). | Depends on content |
| Non-compliant brand affiliation: high-risk financial | `BRAND_NON_COMPLIANT_HIGH_RISK_FINANCIAL` | Brand or website references high-risk financial services such as payday loans, short-term high-interest loans, third-party loan solicitation, cryptocurrency, or stocks and investing platforms. | Not eligible for resubmission under A2P 10DLC. If you believe this is in error, open a technical support case. See [Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). | No |
| Invalid brand phone number | `BRAND_PHONE_NUMBER_INVALID_OR_MISSING` | The brand's support phone number is missing or invalid. | Provide a valid, working support phone number and resubmit. | Yes |
| Spam or phishing association | `SPAM_OR_PHISHING_ASSOCIATION` | The campaign's phone number, business, traffic, or marketing has been flagged as spam or phishing, or the privacy policy indicates opt-in consent is shared with third parties. | Not eligible for resubmission. If you believe this is in error, open a technical support case. See [Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). | No |
| Brand unverified | `BRAND_UNVERIFIED` | The associated brand has not completed the registration process. | Complete your brand registration first, then resubmit your campaign. | Yes |
| Brand use case mismatch | `BRAND_USE_CASE_MISMATCH_POLITICAL` | Brand or website references content (charity or political) that does not match the campaign use case. | Align your campaign use case selection with the content on your website and in your brand registration. | Yes |
| Brand invalid vetting | `BRAND_VETTING_INVALID` | The brand's vetting score does not meet minimum requirements. | Ensure your brand information is accurate and complete to improve your vetting score. | Yes |
| DBA name mismatch | `BRAND_DBA_NAME_MISMATCH` | The DBA (Doing Business As) name does not match the legal business name on file. | Use the exact legal business name that matches your brand registration, or update your brand registration to include the DBA name. | Yes |
| Brand not TCR Authentication+ compliant | `BRAND_NOT_TCR_AUTH_PLUS_COMPLIANT` | Your brand has not completed the enhanced brand verification requirements. | Complete the Authentication+ brand verification process, which includes additional identity validation steps beyond standard registration. | Yes |
| Invalid business connection | `INVALID_BUSINESS_CONNECTION` | ISV or reseller – company information and service information or message samples do not match. | Register the end brand that consumers interact with, not the ISV or reseller. | Yes |
| Invalid multi business | `INVALID_MULTI_BUSINESS` | Same EIN used for multiple different brands. | Register only the minimum number of brands per EIN. | Yes |
| Invalid support email | `INVALID_SUPPORT_EMAIL` | Brand support email address is invalid. | Provide a valid branded email address. | Yes |
| Unofficial support email | `UNOFFICIAL_SUPPORT_EMAIL` | Unofficial email domain for what appears to be a large company. | Use the official corporate email domain for your brand. | Yes |

## Campaign Description

Issues with your campaign description, use case selection, message samples alignment, and campaign-level content.

Campaign Description rejection reasons| Console title | ENUM value | Description | What to fix | Resubmittable |
| --- | --- | --- | --- | --- |
| Campaign mismatch | `CAMPAIGN_MISMATCH` | The campaign description does not match the messaging use case, message samples, or both. | Update the campaign description, messaging use case, and message samples to be consistent, then resubmit. | Yes |
| Campaign mismatch: charity | `CAMPAIGN_MISMATCH_CHARITY` | The campaign description indicates charitable donations, but the use case is not set to Charity or samples do not match. | Set the use case to Charity and ensure all fields are consistent. | Yes |
| Campaign mismatch: political | `CAMPAIGN_MISMATCH_POLITICAL` | The campaign description indicates political messaging, but the use case is not set to Political or samples do not match. | Set the use case to Political and ensure all fields are consistent. | Yes |
| Campaign multi use | `CAMPAIGN_MULTI_USE` | The same or similar use case is repeated across multiple campaigns, indicating snowshoeing. | Register only one campaign per use case. Remove duplicate campaigns. | Yes |
| Campaign to brand mismatch | `CAMPAIGN_TO_BRAND_MISMATCH` | The company name in the campaign description does not match the registered brand name or DBA name. | Update the campaign description to use the registered brand name or DBA name. | Yes |
| Campaign unclear | `CAMPAIGN_UNCLEAR` | The campaign description does not sufficiently describe the service the message program provides. | Add more details explaining the purpose of your message program. If you are an ISV registering a direct offering, indicate that. | Yes |
| Campaign undeclared direct lending | `CAMPAIGN_UNDECLARED_DIRECT_LENDING` | The campaign appears to involve direct lending but the Direct lending content attribute was not selected. | Select the Direct lending or loan arrangement content attribute, even if the specific campaign use case does not directly relate to loan offering. | Yes |
| Campaign not qualified for use case | `CAMPAIGN_NOT_QUALIFIED_FOR_USE_CASE` | The campaign is not qualified for the requested use case. | Review the use case requirements and select an appropriate use case that matches your messaging program. | Yes |
| Non-English campaign content | `CAMPAIGN_NON_ENGLISH_CONTENT` | Campaign registration fields contain non-English language content. | Translate all fields to English. If messaging traffic will be in another language, provide English translations of sample messages. | Yes |
| Duplicate content across fields | `CAMPAIGN_TEMPLATE_REUSE` | The same text was reused across multiple campaign registration fields. | Provide distinct, field-specific content for each field, including different sample messages representing the range of messages your campaign sends. | Yes |
| Personal or P2P use case detected | `CAMPAIGN_NOT_QUALIFIED_P2P` | The campaign describes personal or peer-to-peer messaging, which is not permitted for A2P 10DLC. | Describe a clear business use case and the application or system that generates the messages. | Yes |
| Multiple brands in one campaign | `CAMPAIGN_MULTI_BRAND` | The campaign references multiple companies or brands. | Create separate campaigns for each brand. Ensure all fields within each campaign reference only one company. | Yes |
| Influencer use case not permitted | `CAMPAIGN_NOT_QUALIFIED_INFLUENCER` | Social influencer or public figure communications are not a permitted use case. | If the influencer operates a legitimate business, register under that business use case and provide business context. | Yes |
| Emergency alert use case not permitted | `CAMPAIGN_NOT_QUALIFIED_EMERGENCY_ALERT` | Emergency alert notifications are not permitted through A2P 10DLC. | If your messages are time-sensitive business notifications (such as security alerts), resubmit with a description that accurately reflects the business nature. | Yes |
| Campaign attributes mismatch | `CAMPAIGN_ATTRIBUTES_MISMATCH` | Website URL, campaign description, message flow, and sample messages do not consistently identify the same sender and use case. | Update all fields to be consistent. If registering on behalf of a customer, use the customer's website and brand information. | Yes |
| Campaign confirmation issues | `CAMPAIGN_CONFIRMATION_ISSUES` | Issues with the campaign confirmation mobile-terminated message. | Review and correct your campaign confirmation message details. | Yes |
| Alternative messaging solution recommended | `ALTERNATIVE_SOLUTION_RECOMMENDED` | 10DLC is not required for this use case – an alternative solution would be more appropriate. | Consider other messaging options that better align with your needs, such as toll-free numbers. | Yes |
| Unclear use case | `UNCLEAR_USE_CASE` | Campaign name, description, or opt-in workflow details are unclear. | Provide a clear, detailed campaign description explaining the purpose of your messaging program. | Yes |
| Use case mismatch | `USE_CASE_MISMATCH` | Use case and message samples are inconsistent. | Align your message samples with the declared use case. | Yes |
| Undeclared direct lending | `UNDECLARED_DIRECT_LENDING` | Campaign appears to be direct lending but the appropriate content attribute was not selected. | Select the Direct lending or loan arrangement content attribute. | Yes |
| Sample message(s) mismatch | `SAMPLE_MESSAGE_MISMATCH` | Sample messages do not contain the registered brand name or DBA name. | Include your registered brand name in the sample messages. | Yes |
| Sample messages use case mismatch | `SAMPLE_MESSAGE_USE_CASE_MISMATCH` | Sample messages do not match the declared use case. | Provide at least two different sample messages reflecting actual messages your campaign will send. Include your business name and opt-out instructions in at least one sample. Use brackets for templated fields (for example, [name], [order number]). | Yes |
| Sample messages use case mismatch: charity | `SAMPLE_MESSAGE_USE_CASE_MISMATCH_CHARITY` | Sample messages indicate charitable donations, but the use case is not set to Charity. | Set the use case to Charity or update sample messages to match the declared use case. | Yes |
| Sample messages use case mismatch: political | `SAMPLE_MESSAGE_USE_CASE_MISMATCH_POLITICAL` | Sample messages indicate political content, but the use case is not set to Political. | Set the use case to Political or update sample messages to match the declared use case. | Yes |
| Sample message(s) URL shortener | `SAMPLE_MESSAGE_SHORT_URL` | Sample messages contain public URL shorteners (such as bit.ly or tinyURL). | Public URL shorteners are not permitted in 10DLC message content. Use your full branded domain URL. | Yes |
| Sample messages(s) embedded phone number | `SAMPLE_MESSAGE_PHONE_NUMBER` | Use of embedded phone number is selected but not present in message samples. | Add the embedded phone number to the message samples, or deselect the embedded phone number option. | Yes |
| Message samples mismatch | `MESSAGE_SAMPLES_MISMATCH` | Company and message samples are inconsistent or message samples are missing. | Ensure sample messages are consistent with your brand and campaign description. | Yes |
| Embedded link issues | `EMBEDDED_LINK_ISSUES` | Sample messages include restricted content such as generic shortened URLs. | Remove public URL shorteners and use your full branded domain. | Yes |
| Embedded phone issues | `EMBEDDED_PHONE_ISSUES` | Issues with embedded phone numbers in the campaign. | Verify embedded phone number configuration matches your sample messages. | Yes |
| Help message mismatch | `HELP_MESSAGE_MISMATCH` | The company name or email domain in the HELP message does not match the registered brand name or DBA name. | Update the company name and support email domain in the HELP message to match your registered brand name. | Yes |
| Non-compliant help message | `HELP_MESSAGE_NON_COMPLIANT` | The HELP message does not contain a support contact (email, phone number, or support website URL). | Include the brand name and at least one support contact method in the HELP message reply. | Yes |
| Subscriber help issues | `SUBSCRIBER_HELP_ISSUES` | Issues with the campaign subscriber HELP response. | Review and correct your HELP message to include brand name and support contact information. | Yes |
| Non-compliant message samples | `NON_COMPLIANT_MESSAGE_SAMPLES` | Campaign cannot be approved because of the sample messages content. | Review sample messages for prohibited content and update accordingly. | Depends on content |
| Missing required field | `MISSING_REQUIRED_FIELD` | A required field is missing from the submission. | Complete all required fields and resubmit. | Yes |
| Invalid field value | `INVALID_FIELD_VALUE` | A submitted field value is invalid. | Correct the invalid field value and resubmit. | Yes |
| Missing conditional field | `MISSING_CONDITIONAL_FIELD` | A conditionally required field is missing. | Provide the required field based on your other selections and resubmit. | Yes |
| Conditional field not allowed | `CONDITIONAL_FIELD_NOT_ALLOWED` | A conditionally allowed field was submitted but is not allowed for your configuration. | Remove the field that does not apply to your registration type and resubmit. | Yes |
| Cannot update registration | `CANNOT_UPDATE_REGISTRATION` | Certain campaign fields cannot be modified after submission. | Create a new campaign registration with the desired changes. | No |
| Wait to resubmit registration | `WAIT_TO_RESUBMIT_REGISTRATION` | A campaign registration cannot be submitted while brand vetting is under review. | Wait for brand vetting to complete, then resubmit the campaign. | Yes |

## Website

Issues with your website URL, privacy policy, and terms and conditions.

Website rejection reasons| Console title | ENUM value | Description | What to fix | Resubmittable |
| --- | --- | --- | --- | --- |
| Invalid brand URL | `BRAND_URL_INVALID` | The brand website is missing, inaccessible, or online presence could not be validated. | Verify the URL is live, accessible, and relevant to your business. If the website is not yet live, indicate that in the campaign description. | Yes |
| Insufficient website content | `BRAND_URL_INSUFFICIENT_CONTENT` | The website does not contain sufficient information about the business or its messaging use case. | Ensure your website includes company name, contact information, description of services, privacy policy, and information about your SMS messaging program. | Yes |
| Website contains only a form | `BRAND_URL_FORM_ONLY` | The website contains only a form without adequate business context. | Provide a URL to a full business website with company details, service descriptions, and contact information, or add business context around the form. | Yes |
| High-risk domain reputation | `BRAND_URL_HIGH_RISK_DOMAIN` | The campaign website or URL has a poor domain reputation or is flagged in threat intelligence databases. | Not eligible for resubmission. Check your domain reputation using publicly available tools (such as Google Safe Browsing or VirusTotal) and remediate issues before registering a new campaign. If you believe this is in error, open a technical support case. See [Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). | No |
| Website requires authentication | `BRAND_URL_AUTHENTICATION_REQUIRED` | The website requires login or authentication and cannot be reviewed. | Provide a publicly accessible URL. If your primary service is behind a login, create a public page describing your business and messaging program. | Yes |
| Invalid URL | `INVALID_URL` | Website not provided or not working. | Provide a functional, publicly accessible website URL. | Yes |
| Privacy policy missing/inaccessible | `PRIVACY_POLICY_MISSING` | The privacy policy URL is unavailable or inaccessible. | Provide a working, publicly accessible privacy policy URL. | Yes |
| Non-compliant privacy policy | `PRIVACY_POLICY_NON_COMPLIANT` | The privacy policy references mobile opt-in data sharing with third parties or does not state that no mobile opt-in data will be shared. | Add an explicit statement that mobile opt-in data will not be shared with third parties for marketing or promotional purposes. | Yes |
| Privacy policy mismatch | `PRIVACY_POLICY_MISMATCH` | The privacy policy does not contain the registered brand name or DBA name. | Update the privacy policy to include your registered brand name. | Yes |
| Missing Terms and Conditions | `TERMS_AND_CONDITIONS_MISSING` | The Terms and Conditions URL is missing or inaccessible. | Provide a working, publicly accessible Terms and Conditions URL. | Yes |
| Non-compliant Terms and Conditions | `TERMS_AND_CONDITIONS_NON_COMPLIANT` | The Terms and Conditions are missing one or more required elements: carrier liability statement, message frequency disclosure, opt-out instructions, customer care contact, or HELP instructions. | Add all missing elements and resubmit. | Yes |
| Non-compliant Terms and Conditions: affiliate marketing | `TERMS_AND_CONDITIONS_NON_COMPLIANT_AFFILIATE_MARKETING` | The Terms and Conditions indicate affiliate marketing or lead generation. | Affiliate marketing is prohibited. Not eligible for resubmission under A2P 10DLC. | No |
| Non-compliant Terms and Conditions: carrier liability | `TERMS_AND_CONDITIONS_NON_COMPLIANT_CARRIER_LIABILITY` | Missing statement that US carriers are not liable for delayed or undelivered messages. | Add a carrier liability disclaimer to your Terms and Conditions. | Yes |
| Non-compliant Terms and Conditions: customer care info | `TERMS_AND_CONDITIONS_NON_COMPLIANT_CUSTOMER_CARE` | Missing customer care contact information. | Add customer care contact information (email, phone, or support URL). | Yes |
| Non-compliant Terms and Conditions: message frequency | `TERMS_AND_CONDITIONS_NON_COMPLIANT_MSG_FREQUENCY` | Missing message frequency disclosure. | Add message frequency information (for example, "Up to 4 messages per month"). | Yes |
| Non-compliant Terms and Conditions: opt-out instructions | `TERMS_AND_CONDITIONS_NON_COMPLIANT_OPT_OUT` | Missing opt-out instructions. | Add information on how end users can opt out (for example, "Reply STOP to cancel"). | Yes |
| Non-compliant Terms and Conditions: privacy policy | `TERMS_AND_CONDITIONS_NON_COMPLIANT_PRIVACY_POLICY` | Missing link to privacy policy. | Add a link to your privacy policy within the Terms and Conditions. | Yes |
| Non-compliant Terms and Conditions: use case description | `TERMS_AND_CONDITIONS_NON_COMPLIANT_USE_CASE` | Missing description of the campaign use case. | Add a description of the purpose of the message program. | Yes |
| Terms and Conditions mismatch | `TERMS_AND_CONDITIONS_MISMATCH` | The Terms and Conditions do not contain the registered brand name or DBA name. | Update the Terms and Conditions to include your registered brand name. | Yes |
| Terms and Conditions use case mismatch | `TERMS_AND_CONDITIONS_USE_CASE_MISMATCH` | The Terms and Conditions program description is not related to the campaign use case. | Update the Terms and Conditions to describe the correct use case. | Yes |
| Terms and conditions issues | `TERMS_AND_CONDITIONS_ISSUES` | General Terms and Conditions issues. | Review all Terms and Conditions requirements and ensure compliance. | Yes |

## Opt-In

Issues with your opt-in workflow, opt-in message, and consent collection mechanisms.

Opt-In rejection reasons| Console title | ENUM value | Description | What to fix | Resubmittable |
| --- | --- | --- | --- | --- |
| Opt-in workflow insufficient consent | `OPT_IN_WORKFLOW_CONSENT` | The opt-in workflow does not obtain sufficient consent. Express written consent is required for promotional content. Consent cannot be bundled as a required condition of service. | Detail all opt-in methods and provide links or hosted screenshots. Ensure opt-in data is not shared with unauthorized third parties. Separate marketing consent from transactional consent. | Yes |
| Opt-in workflow mismatch | `OPT_IN_WORKFLOW_MISMATCH` | The company name in the opt-in workflow does not match the registered brand name or DBA name. | Add the registered brand name or DBA name to the opt-in workflow. | Yes |
| Opt-in workflow missing | `OPT_IN_WORKFLOW_MISSING` | No opt-in workflow URL or image was provided, or the URL is inaccessible. The Message Flow must describe every way consent is collected and include required disclosures. | Describe every consent method (web, keyword, verbal, paper form, QR code). Include brand identification, message frequency, links to terms and privacy policy, "Message and data rates may apply" disclosure, and opt-out instructions. If not publicly accessible, provide hosted screenshots. | Yes |
| Opt-in workflow non compliant message and data rates disclosure | `OPT_IN_WORKFLOW_NON_COMPLIANT_DATA_RATES` | The opt-in workflow is missing the "Message and data rates may apply" disclosure. | Add the "Message and data rates may apply" disclosure to your opt-in workflow. | Yes |
| Opt-in workflow non-compliant HELP or STOP | `OPT_IN_WORKFLOW_NON_COMPLIANT_HELP_STOP` | The opt-in workflow does not contain HELP or STOP instructions. | Add instructions such as "Reply HELP for help" and "Reply STOP to cancel" to your opt-in workflow or Terms and Conditions. | Yes |
| Opt-in workflow non compliant message frequency disclosure | `OPT_IN_WORKFLOW_NON_COMPLIANT_MSG_FREQUENCY` | The opt-in workflow is missing the required message frequency disclosure. | Indicate the frequency at which messages will be sent (for example, "4 msgs/month" or "Message frequency varies"). | Yes |
| Opt-in workflow non compliant privacy policy | `OPT_IN_WORKFLOW_NON_COMPLIANT_PRIVACY_POLICY` | The opt-in workflow is missing a link to the privacy policy or a statement that mobile opt-in data will not be shared with third parties. | Add a direct link to your privacy policy. The privacy policy must explicitly state that no mobile information will be shared with third parties for marketing purposes. | Yes |
| Opt-in workflow non compliant terms and conditions | `OPT_IN_WORKFLOW_NON_COMPLIANT_TERMS_AND_CONDITIONS` | The opt-in workflow is missing required terms and conditions language or a link to complete terms. | Add a link to your complete terms and conditions. | Yes |
| Marketing consent not separated | `OPT_IN_WORKFLOW_CONSENT_MARKETING_NOT_SEPARATED` | Marketing consent is combined with informational or transactional consent. | Implement a distinct opt-in mechanism for marketing messages, separate from informational messaging consent. | Yes |
| Incomplete opt-in workflow details | `OPT_IN_WORKFLOW_INCOMPLETE` | One or more declared opt-in methods do not include complete workflow descriptions. | Provide full details for every opt-in method you selected, or remove opt-in types you do not actually use. | Yes |
| Non-compliant consent language | `OPT_IN_WORKFLOW_NON_COMPLIANT_CONSENT_LANGUAGE` | The opt-in flow is missing required consent agreement language. | Include: (1) the type of messages the consumer will receive, (2) message frequency, (3) "Message and data rates may apply" disclosure, and (4) opt-out instructions such as "Reply STOP to unsubscribe." | Yes |
| Opt-in checkbox missing or pre-selected | `OPT_IN_WORKFLOW_CHECKBOX_INVALID` | The opt-in checkbox is missing or appears to be pre-selected by default. | Include an unchecked checkbox specifically for SMS messaging consent that the consumer must actively select. It must be separate from general Terms of Service acceptance. | Yes |
| Opt-in data shared with third parties | `OPT_IN_DATA_SHARED_WITH_THIRD_PARTIES` | Opt-in consent data is being shared with third parties without proper disclosure. | Update your privacy policy to explicitly state that mobile opt-in data will not be shared with third parties. | Yes |
| Non-compliant opt-in | `NON_COMPLIANT_OPT_IN` | Opt-in process is not compliant or opt-in is not explicit. | Review all opt-in compliance requirements and ensure explicit consent is collected. | Yes |
| Unclear opt-in | `UNCLEAR_OPT_IN` | Website not provided or not working; opt-in call-to-action is incomplete. | Provide a complete call-to-action if opt-in is outside of your website. Include a working URL or hosted screenshots. | Yes |
| Opt-in workflow non compliant content: gambling | `OPT_IN_WORKFLOW_NON_COMPLIANT_CONTENT_GAMBLING` | Opt-in workflow indicates message content is related to gambling. | Gambling content is not permitted by mobile operators. | No |
| Opt-in workflow non compliant content: high risk financial. | `OPT_IN_WORKFLOW_NON_COMPLIANT_CONTENT_HIGH_RISK_FINANCIAL` | Opt-in workflow indicates message content is related to high-risk financial services. | High-risk financial services content is not permitted by mobile operators. | No |
| Opt-in workflow non compliant content: illegal substances. | `OPT_IN_WORKFLOW_NON_COMPLIANT_CONTENT_ILLEGAL_SUBSTANCES` | Opt-in workflow indicates message content is related to federally illegal substances. | Illegal substance content is not permitted by mobile operators. | No |
| Opt-in workflow non compliant content: SHAFT. | `OPT_IN_WORKFLOW_NON_COMPLIANT_CONTENT_SHAFT_AGE_GATE` | Opt-in workflow indicates message content contains SHAFT content (sex, hate, alcohol, firearms, tobacco/vape). | SHAFT content without an age gate is not permitted. If age-restricted (alcohol, firearms, tobacco), add a compliant age gate. Otherwise, this content is prohibited. | Depends on content |
| Opt-in message mismatch | `OPT_IN_MESSAGE_MISMATCH` | The company name in the opt-in message does not match the registered brand name or DBA name. | Update the company name in the opt-in message to match your registered brand name. | Yes |
| Missing opt-in message | `OPT_IN_MESSAGE_MISSING` | No opt-in message was provided. Recurring message programs must send an opt-in message with HELP and STOP instructions, message frequency, and "Message and data rates may apply" disclosure. | Add a compliant opt-in message with all required disclosures. | Yes |
| Non-compliant opt-in message | `OPT_IN_MESSAGE_NON_COMPLIANT` | The opt-in message is missing message frequency disclosure or "Message and data rates may apply" disclosure. | Include the frequency of messages and the "Message and data rates may apply" disclosure in your opt-in message. | Yes |
| Non-compliant opt-in message HELP and STOP | `OPT_IN_MESSAGE_NON_COMPLIANT_HELP_STOP` | The opt-in message does not contain HELP or STOP instructions. | Add instructions such as "Reply STOP to cancel" to your opt-in message. | Yes |

## Opt-Out

Issues with your opt-out message and opt-out handling.

Opt-Out rejection reasons| Console title | ENUM value | Description | What to fix | Resubmittable |
| --- | --- | --- | --- | --- |
| Opt-out message mismatch | `OPT_OUT_MESSAGE_MISMATCH` | The company name in the opt-out message does not match the registered brand name or DBA name. | Update the opt-out message to include your registered brand name or DBA name. | Yes |
| Non-compliant opt-out message | `OPT_OUT_MESSAGE_NON_COMPLIANT` | The opt-out message does not include acknowledgement of the opt-out request, confirmation that no further messages will be sent, or the brand name. | Include all three elements: (1) acknowledgement of the opt-out, (2) confirmation no further messages will be sent, (3) brand name. | Yes |
| Unclear opt-out | `UNCLEAR_OPT_OUT` | Opt-out details are unclear. | Provide clear opt-out instructions and a compliant opt-out confirmation message. | Yes |

## Age Gate

Issues with age verification requirements for age-restricted content (alcohol, firearms, tobacco/vape).

Age Gate rejection reasons| Console title | ENUM value | Description | What to fix | Resubmittable |
| --- | --- | --- | --- | --- |
| Campaign non-compliant content: missing age gate | `CAMPAIGN_NON_COMPLIANT_CONTENT_SHAFT_AGE_GATE` | Your campaign includes age-restricted content (alcohol, firearms, or tobacco/vape) but a compliant age gate was not found on your website or opt-in flow. | Add an age gate that requires the recipient to enter their day, month, and year of birth. A simple yes/no age confirmation is not sufficient. | Yes |
| Age gate issues | `AGE_GATE_ISSUES` | Campaign age gate issues. | Implement a compliant age gate mechanism requiring full date-of-birth entry before opt-in to messaging. | Yes |
| Non-compliant alcohol use case | `NON_COMPLIANT_USE_CASE_ALCOHOL` | Age-restricted alcohol content without a compliant age gate. | Add a compliant age gate requiring full date-of-birth entry (day, month, year). | Yes |
| Non-compliant tobacco use case | `NON_COMPLIANT_USE_CASE_TOBACCO` | Age-restricted tobacco or vape content without a compliant age gate. | Add a compliant age gate requiring full date-of-birth entry (day, month, year). | Yes |
| Non-compliant guns use case | `NON_COMPLIANT_USE_CASE_GUNS` | Firearms or ammunition content without a compliant age gate. | Add a compliant age gate requiring full date-of-birth entry (day, month, year). | Yes |

## Disallowed Content

Content categories that are prohibited by mobile operators. Campaigns with these rejections are generally not eligible for resubmission.

Disallowed Content rejection reasons| Console title | ENUM value | Description | What to fix | Resubmittable |
| --- | --- | --- | --- | --- |
| Campaign non-compliant content: affiliate marketing. | `CAMPAIGN_NON_COMPLIANT_CONTENT_AFFILIATE_MARKETING` | Message content involves lead generation or affiliate marketing. | Affiliate marketing and lead generation are prohibited by mobile operators. Consider alternative messaging approaches. | No |
| Campaign non-compliant content: gambling. | `CAMPAIGN_NON_COMPLIANT_CONTENT_GAMBLING` | Message content involves gambling. | Gambling content is prohibited by mobile operators. | No |
| Campaign non-compliant content: high-risk financial | `CAMPAIGN_NON_COMPLIANT_CONTENT_HIGH_RISK_FINANCIAL` | Message content involves high-risk financial services (payday loans, short-term high-interest loans, third-party loan solicitation, student loans, cryptocurrency, stocks, debt collection, debt consolidation, debt reduction, or credit repair). | Not eligible for resubmission. If you believe this is in error, open a technical support case. See [Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). | No |
| Campaign non-compliant content: illegal substances | `CAMPAIGN_NON_COMPLIANT_CONTENT_ILLEGAL_SUBSTANCES` | Message content involves federally illegal substances (such as cannabis). | Illegal substance content is prohibited by mobile operators. | No |
| Campaign non-compliant content: third party job boards. | `CAMPAIGN_NON_COMPLIANT_CONTENT_JOB_BOARDS` | Message content involves third-party job boards. | Third-party job board content is prohibited by mobile operators. | No |
| Campaign non-compliant content: SHAFT | `CAMPAIGN_NON_COMPLIANT_CONTENT_SHAFT` | Message content involves SHAFT content (sex, hate, alcohol, firearms, tobacco/vape) or marijuana/CBD. | Not eligible for resubmission. If you believe this is in error, open a technical support case. See [Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). | No |
| Campaign non-compliant content: sweepstakes | `CAMPAIGN_NON_COMPLIANT_CONTENT_SWEEPSTAKES` | Message content involves sweepstakes or sweepstakes-related messaging. | Sweepstakes content is prohibited by mobile operators. | No |
| Campaign non-compliant content: non-subscriber facing | `CAMPAIGN_NON_COMPLIANT_CONTENT_NON_SUBSCRIBER` | Use case or message samples appear to be for testing or non-subscriber-facing purposes. | 10DLC is only for production use cases. Register with the correct use case for subscriber-facing messaging. | Yes |
| Prohibited content: cannabis or CBD | `CAMPAIGN_NON_COMPLIANT_CONTENT_CANNABIS` | Campaign promotes, advertises, or helps the sale of cannabis, CBD, marijuana, or controlled substances. | Cannabis and CBD content is prohibited regardless of state-level legality. Consider alternative communication channels. | No |
| Non-compliant use case | `NON_COMPLIANT_USE_CASE` | Use case or message samples are considered restricted or disallowed by mobile operators. | Review your content against prohibited content categories and remove disallowed material. | Depends on content |
| Non-compliant affiliate marketing use case | `NON_COMPLIANT_USE_CASE_AFFILIATE_MARKETING` | Lead generation or affiliate marketing use case. | Affiliate marketing is prohibited by mobile operators. | No |
| Non-compliant gambling use case | `NON_COMPLIANT_USE_CASE_GAMBLING` | Gambling content. | Gambling is prohibited by mobile operators. | No |
| Non-compliant high risk financial use case | `NON_COMPLIANT_USE_CASE_HIGH_RISK_FINANCIAL` | High-risk financial services content. | High-risk financial content is prohibited by mobile operators. | No |
| Non-compliant SHAFT use case | `NON_COMPLIANT_USE_CASE_SHAFT` | SHAFT content (sex, hate, alcohol, firearms, tobacco/vape). | SHAFT content is prohibited by mobile operators. | No |
| Non-compliant testing use case | `NON_COMPLIANT_USE_CASE_TESTING` | Use case appears to be for testing rather than production. | 10DLC is only for production use cases. Describe your actual production messaging program. | Yes |
| Non-compliant cannabis use case | `NON_COMPLIANT_USE_CASE_CANNIBIS` | Cannabis content. | Cannabis content is prohibited by mobile operators. | No |
| Non-compliant hate use case | `NON_COMPLIANT_USE_CASE_HATE` | Hate content. | Hate content is prohibited by mobile operators. | No |
| Non-compliant message samples: gambling | `SAMPLE_MESSAGE_NON_COMPLIANT_CONTENT_GAMBLING` | Sample messages indicate gambling content. | Gambling content is not permitted by US carriers. | No |
| Non-compliant message samples: high-risk financial services | `SAMPLE_MESSAGE_NON_COMPLIANT_CONTENT_HIGH_RISK_FINANCIAL` | Sample messages indicate high-risk financial services content (loans, cryptocurrency). | High-risk financial content is not permitted by US carriers. | No |
| Non-compliant message samples: illegal substances | `SAMPLE_MESSAGE_NON_COMPLIANT_CONTENT_ILLEGAL_SUBSTANCES` | Sample messages indicate federally illegal substances (such as cannabis). | Illegal substance content is not permitted by US carriers. | No |
| Non-compliant message samples: third party job-boards | `SAMPLE_MESSAGE_NON_COMPLIANT_CONTENT_JOB_BOARDS` | Sample messages indicate third-party job board content. | Third-party job board content is not permitted by US carriers. | No |
| Non-compliant message samples: SHAFT | `SAMPLE_MESSAGE_NON_COMPLIANT_CONTENT_SHAFT` | Sample messages indicate SHAFT content (sex, hate, alcohol, firearms, tobacco/vape). | SHAFT content is not permitted by US carriers. | No |
| Non-compliant message samples: sweepstakes | `SAMPLE_MESSAGE_NON_COMPLIANT_CONTENT_SWEEPSTAKES` | Sample messages indicate sweepstakes content. | Sweepstakes content is not permitted by US carriers. | No |
| Campaign suspended | `REGISTRATION_SUSPENDED_BY_MNO` | Your campaign and associated origination entities have been suspended by a downstream partner or mobile carrier. | Open a technical support case for assistance in restoring your registration. See [Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). | No |
| Security review requirements not met | `SECURITY_REVIEW_FAILED` | This registration did not meet security review requirements. This decision is final. | You may consider alternative messaging solutions or submit a new application in the future. | No |
