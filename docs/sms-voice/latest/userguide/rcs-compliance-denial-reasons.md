

# RCS registration denial reasons
<a name="rcs-compliance-denial-reasons"></a>

When a registration is denied, AWS End User Messaging provides a denial reason that explains why the registration was not approved. The following table lists all RCS registration denial reasons and the recommended action for each.


**RCS registration denial reasons**  

| Denial reason | Description | Recommended action | 
| --- | --- | --- | 
| REQUIRES\_OFFLINE\_REVIEW | This registration requires manual offline review. | Create a support case in the AWS Support Center. Choose the RCS Agent assistance category and include your registration ID. See [Get help with registration issues through Support](registrations-request-support.md). | 
| CANNOT\_UPDATE\_REGISTRATION | Certain RCS agent fields cannot be modified on an existing registration. | Create a new testing registration with the corrected fields. | 
| IMAGE\_URL\_INACCESSIBLE | The image URL provided is not publicly accessible. | Provide a URL that can be accessed without authentication. Update the registration and resubmit. | 
| IMAGE\_FORMAT\_INVALID | The image must be in JPEG or PNG format. | Upload an image in the correct format and resubmit. | 
| IMAGE\_RESOLUTION\_INVALID | The image does not meet the required resolution. The logo must be 224 x 224 pixels and the banner must be 1440 x 448 pixels. | Resize the image to the required dimensions and resubmit. | 
| IMAGE\_SIZE\_EXCEEDED | The image file size exceeds the allowed limit. The logo must not exceed 50 KB and the banner must not exceed 200 KB. | Reduce the file size and resubmit. | 
| ACCENT\_COLOR\_CONTRAST\_INSUFFICIENT | The accent color must have a contrast ratio of at least 4.5:1 relative to white. | Choose a darker accent color that meets the contrast requirement and resubmit. | 
| PRIVACY\_POLICY\_INACCESSIBLE | The privacy policy URL provided is inaccessible or invalid. | Provide a publicly accessible privacy policy URL and resubmit. | 
| TERMS\_AND\_CONDITIONS\_INACCESSIBLE | The terms and conditions URL provided is inaccessible or invalid. | Provide a publicly accessible terms and conditions URL and resubmit. | 
| CONTACT\_DETAILS\_MISSING | At least one contact method (phone, email, or website) is required in the agent profile, and each contact value must have a corresponding label. | Add at least one contact method to your agent profile. Ensure each contact value has a corresponding label (for example, if you provide a phone number, also provide a phone label). Update the registration and resubmit. | 
| INVALID\_FIELD\_VALUE | A field value does not match the expected format or conflicts with an existing configuration on the RCS agent. This commonly occurs when keyword response fields (complianceKeywords.stopResponse or complianceKeywords.helpResponse) do not match the current keyword configuration on the agent. | Verify that all field values match the expected format. For keyword fields: 1. Call `DescribeKeywords` using the RCS agent ID to view the current configuration.<br />2. Ensure your registration values match exactly. See [Keyword configuration must match the RCS agent](rcs-country-launch.md#rcs-country-launch-troubleshoot-keyword-match). | 

For denial reasons that require AWS Support assistance, create a support case in the [AWS Support Center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). Include your AWS RCS Agent ID and registration ID in the case description.