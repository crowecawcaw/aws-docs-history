# Technical FAQ—versioning and backward compatibility

**Q: What is a payload in Amazon Web Services
(AWS) data exchange?**

A payload is a structured piece of
data formatted in JSON, sent either inbound to AWS or outbound from
AWS. Each key in this JSON structure is referred to as a
_field_, and each field has an associated
_value._

**Q: How is the payload version determined?**

Payload version is specified within the
`version` field of the payload itself. Payloads
adhering to field definition v13 are considered Payload Version 1.0,
while those following the format defined in field definition v14 or
higher are referred to as Payload Version 2.0.

**Q: What does backward compatibility mean in
this context, and how is it handled?**

Backward compatibility ensures that existing opportunities don’t fail when
new and mandatory fields are introduced in newer payload versions.
AWS maintains this by auto-assigning default values to fields
required in the new version. You might notice values in the AWS Partner Network (APN) Customer Engagement (ACE) UI that you
did not explicitly provide through the Customer Relationship
Management (CRM) Integration. Details and conditions for each field
are explained in the field description or additional details about
the field.

**Q: Is backward compatibility a permanent
feature?**

No. Backward compatibility is time-bound,
designed to provide flexibility for you to plan and implement
upcoming changes. It stops working beyond a specified cut-off date,
which will be announced later in the year as part of a wider launch.

**Q: What happens when I start
sending payloads with version 2.0?**

Once you send a payload with version 2.0, the system assumes that all necessary
changes have been implemented, and validations for the new payload
version apply to all subsequent changes. It’s essential that you don't
implement features partially between version 1.0 and version
2.0 payloads.

**Q: Can I revert back to payload
version 1.0 after updating to version 2.0?**

No. Transitioning to payload version 2.0 is a one-way process. Once
you update to version 2.0, you can't revert back to version
1.0 of the payload.
