# Default redaction configuration in Amazon WorkSpaces Secure Browser

The default redaction configuration will automatically apply a confidence level and URL
enforcement for all built-in data types in the data protection settings. You have the option to
override the default configuration when adding a built-in data type.

Confidence levels allow you to fine-tune the redaction logic for built-in data types using
a combination of format, keywords, and unformatted text. Choose the level of strictness for how
redaction is applied, including High, Medium, or Low. The default value will apply to all data
types, unless an override is applied at the data type level. In general, start with a default
configuration of Medium, and refine by validating that the redaction is enforced as expected on
your sites.

| Confidence level | Description                                                                                          | Example                                                                                                                               |
| ---------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| High             | Requires a formatted text pattern match in order for content to be redacted.                         | SSN of 123-45-6798 would be redacted, while 123456789 would not.                                                                      |
| Medium           | Redaction considers both formatted and unformatted text, and adds keyword associate to<br>the logic. | SSN of 123-45-6798 would be redacted. 123456789 would be redacted if detected nearby a<br>keyword (such as "social security number"). |
| Low              | Redaction enforced for both formatted pattern + unformatted pattern without<br>keyword.              | SSN in either format<br>• 123-45-6798 and 123456789<br>• are redacted without requiring<br>keyword.                                   |

You must set the default redaction configuration for all data types. You can choose from
the following options:

- All URLs
- Specific URLs
- Advanced configuration
  The default value will apply to all data types, unless an override is applied at the data
  type level. URL enforcement uses similar logic to Chrome policy for managing allow and
  blocklists. For guidance using block and allow URLs, see [Allow or block
  access to websites](https://support.google.com/chrome/a/answer/7532419?hl=en#zippy=%2Clinux "https://support.google.com/chrome/a/answer/7532419?hl=en#zippy=%2Clinux"). For the best results, add URLs to these lists following Chrome's
  blocklist filter format. For more information, see [URL blocklist filter format](https://support.google.com/chrome/a/answer/9942583?_ga=2.44620960.505898626.1675896662-439274379.1675896662&visit_id=638114931513376779-3689089291&p=url_blocklist_filter_format&rd=1 "https://support.google.com/chrome/a/answer/9942583?_ga=2.44620960.505898626.1675896662-439274379.1675896662&visit_id=638114931513376779-3689089291&p=url_blocklist_filter_format&rd=1").
