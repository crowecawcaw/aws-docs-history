# RCS registration denial reasons

When a registration is denied, AWS End User Messaging provides a denial reason that
explains why the registration was not approved. The following table lists
all RCS registration denial reasons and the recommended action for each.

RCS registration denial reasons| Denial reason | Description | Recommended action |
| --- | --- | --- |
| `REQUIRES_OFFLINE_REVIEW` | This registration requires manual offline review. | Create a support case in the AWS Support Center.<br>Choose the RCS Agent assistance category and include your<br>registration ID. See<br>[Get help with registration issues through Support](registrations-request-support.md "registrations-request-support.md"). |
| `CANNOT_UPDATE_REGISTRATION` | Certain RCS agent fields cannot be modified on an<br>existing registration. | Create a new testing registration with the corrected<br>fields. |
| `IMAGE_URL_INACCESSIBLE` | The image URL provided is not publicly accessible. | Provide a URL that can be accessed without<br>authentication. Update the registration and resubmit. |
| `IMAGE_FORMAT_INVALID` | The image must be in JPEG or PNG format. | Upload an image in the correct format and resubmit. |
| `IMAGE_RESOLUTION_INVALID` | The image does not meet the required resolution. The<br>logo must be 224 x 224 pixels and the banner must be<br>1440 x 448 pixels. | Resize the image to the required dimensions and<br>resubmit. |
| `IMAGE_SIZE_EXCEEDED` | The image file size exceeds the allowed limit. The<br>logo must not exceed 50 KB and the banner must not<br>exceed 200 KB. | Reduce the file size and resubmit. |
| `ACCENT_COLOR_CONTRAST_INSUFFICIENT` | The accent color must have a contrast ratio of at<br>least 4.5:1 relative to white. | Choose a darker accent color that meets the contrast<br>requirement and resubmit. |
| `PRIVACY_POLICY_INACCESSIBLE` | The privacy policy URL provided is inaccessible or<br>invalid. | Provide a publicly accessible privacy policy URL and<br>resubmit. |
| `TERMS_AND_CONDITIONS_INACCESSIBLE` | The terms and conditions URL provided is inaccessible<br>or invalid. | Provide a publicly accessible terms and conditions URL<br>and resubmit. |
| `CONTACT_DETAILS_MISSING` | At least one contact method (phone, email, or website)<br>is required in the agent profile, and each contact value<br>must have a corresponding label. | Add at least one contact method to your agent profile.<br>Ensure each contact value has a corresponding label (for<br>example, if you provide a phone number, also provide a<br>phone label). Update the registration and resubmit. |
| `INVALID_FIELD_VALUE` | A field value does not match the expected format or<br>conflicts with an existing configuration on the RCS agent.<br>This commonly occurs when keyword response fields<br>(`complianceKeywords.stopResponse` or<br>`complianceKeywords.helpResponse`) do not match<br>the current keyword configuration on the agent. | Verify that all field values match the expected format.<br>For keyword fields:<br>1. Call `DescribeKeywords`<br>using the RCS agent ID to view the current<br>configuration.<br>2. Ensure your registration values match<br>exactly.<br>See [Keyword configuration must match the RCS agent](rcs-country-launch.md#rcs-country-launch-troubleshoot-keyword-match "rcs-country-launch.md#rcs-country-launch-troubleshoot-keyword-match"). |

For denial reasons that require AWS Support assistance, create a
support case in the [AWS
Support Center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase"). Include your AWS RCS Agent ID and registration ID
in the case description.
