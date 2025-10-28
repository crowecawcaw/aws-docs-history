# Change management modes

AWS Managed Services (AMS) uses change management mode to guardrail changes in AMS Advanced. The change management modes help you maintain high operational standards for the environment, and to
control risk and prevent adverse impact. AMS Advanced has different
modes that provide different levels of control and risk. All modes, except for Customer-Managed mode, are managed by AMS. The following are the available change management modes:

- RFC mode (formerly Standard CM mode): Provides a "request for change" (RFC) system and AMS-custom change types (CTs)
- Direct Change mode: Same as RFC mode plus use of AWS APIs and consoles to create AMS-managed resources
- AWS Service Catalog on AMS: Similar to Direct Change mode, but instead of using the AMS change management system (RFCs), you use
  AWS Service Catalog to create resources that AMS then manages.
- Developer mode: Same as Direct Change mode only the resources you create with AWS APIs and consoles are not AMS-managed—you are responsible for
  their management
- Self Service Provisioning (SSP) mode: Same as Developer mode except there is no access to the AMS change management system (no RFCs)
- Customer Managed mode: AMS provides you with a multi-account landing zone landing zone but all resource management is your responsibility
  The AWS Managed Services (AMS) change management system, using the change management (CM) API, provides operations to
  create and manage requests for change (RFCs) for both multi-account landing zone (MALZ) and single-account landing zone (SALZ) accounts.

A request for change (RFC) is a request created by either you or AMS through the
AMS interface to make a change to your managed environment and includes a change type (CT) ID for a particular operation.

The AMS change management (CM) API provides operations to create and manage
requests for change (RFCs). You can create, update, submit, approve, reject, and cancel
RFCs. The AMS operators can create, update, submit, approve, reject, cancel, and mark RFCs as closed.

For a list of AMS reserved prefixes not to be used in tag or other names, see
[Reserved prefixes](../userguide/ams-reserved-prefixes.md "../userguide/ams-reserved-prefixes.md").

For information on each change type, including schemas and examples, see the
[AMS Change Type Reference](../ctref/index.md "../ctref/index.md").

###### Note

All change management API calls are recorded in AWS CloudTrail. For more information,
see [Accessing your logs](../userguide/access-to-logs.md "../userguide/access-to-logs.md").
