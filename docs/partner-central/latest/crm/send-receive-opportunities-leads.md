# Synchronizing opportunity and lead data

To sync an opportunity or lead with APN, you must set the **Sync with Partner
Central** field to **True**. Additional fields for
integration include the **Last APN Sync Date** and **Eligible
to Sync with APN** fields. Standard opportunities and leads include those
fields. However, you set must create and map the fields for the corresponding object if
the source objects are set to custom.

- **Sync with Partner Central** – Included in the app
  for standard opportunities and leads. If you choose to map to custom objects,
  you must create and map this field as boolean.
- **Last Sync Date with APN** – Indicates the last time
  the record was successfully sent to APN or received from APN. This field is auto
  set when the record is successfully sent to APN or an update is received from
  APN.
- **Eligible to Sync with APN** – A formula field that
  determines if the record is targeted to be sent to APN in the next scheduled
  job. Calculated based on if the record was modified since the last time the
  outbound schedule ran, and it was updated by a user other than the designated
  integration user for the AWS Partner's organization.
