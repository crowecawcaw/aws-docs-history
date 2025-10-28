# Maintenance updates for Amazon Q Business

Amazon Q Business periodically performs maintenance updates on its resources.
Maintenance most often involves updates to the Amazon Q Business index for security
fixes, bug fixes, and other performance enhancements.

Maintenance updates can either be performed automatically by the service on your behalf,
or have to manually applied to your Amazon Q Business resources. If a manual
maintenance update is required, you must apply it as soon as it is available. If a manual
maintenance update is optional, we recommend that you apply it to your Amazon Q Business resources as soon as possible.

Maintenance updates can also have designated maintenance windows. In most cases, the
service will inform you of the maintenance update window designated for your Amazon Q Business resources. To minimize the impact of the maintenance on your
application, you can reschedule this window by contacting AWS [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Amazon Q Business index updates

When your Amazon Q Business index requires an update, you will receive
notifications about the update on the Amazon Q Business console or through
emails.

Usually, an Amazon Q Business index maintenance update will involve the
following:

- Queries will continue to run and work as expected on documents already
  existing in the index. All other functionality will continue working as
  expected.
- Data and access control list (ACL) syncs for Amazon Q Business
  connectors, and documents uploaded directly to an Amazon Q Business
  application, will be paused. This will be the case no matter how the documents
  are added to the index—using the console or through the API.
- The status of indexed documents will remain **In
  progress** for up to 1 day. If you use the API, using the
  `UpdateIndex` operation will return a 409 status code with the
  following message: `Index can't be updated at this time due to ongoing
maintenance activity. Try again later.`
- All in-progress documents will be synced when the planned maintenance is
  complete. No data loss will occur.
- For Amazon Q Business applications encrypted with a customer managed KMS
  key, you'll see CloudTrail events for the following APIs while maintenance is going
  on:
  - CreateGrant
  - GenerateDataKey
  - Decrypt

All these accesses are authorized use by the Amazon Q Business service and are
required for the maintenance activity.
