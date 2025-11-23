# Customize from the AWS Control Tower console

To make these customizations to your landing zone, follow the steps given by the
AWS Control Tower console.

###### Select customized names during setup

- You can select your top-level OU names during setup. You can rename your OUs
  at any time using the AWS Organizations console, but making changes to your OUs in
  AWS Organizations may cause repairable [drift](drift.md "drift.md").
- You can select the names of your shared **Audit** and
  **Log Archive** accounts, but you cannot change the names
  after setup. (This is a one-time selection.)

###### Tip

Remember that renaming an OU in AWS Organizations does not update the corresponding
provisioned product in Account Factory. To update the provisioned product automatically
(and avoid drift), you must perform the OU operation through AWS Control Tower, including
creating, deleting, or re-registering an OU.

###### Select AWS Regions

- You can customize your landing zone by selecting specific AWS Regions for
  governance. Follow the steps in the AWS Control Tower console.
- You can select and de-select AWS Regions for governance when you update your
  landing zone.
- You can set the Region Deny control to **Enabled** or
  **Not enabled**, and control user access to most AWS
  services in ungoverned AWS Regions.
  For information about AWS Regions where CfCT has deployment limitations, see [Control limitations](control-limitations.md "control-limitations.md").

###### Customize by adding optional controls

- Strongly recommended and elective controls are optional, which means that you
  can customize the level of enforcement for your landing zone by choosing which ones
  to enable. [Optional controls](optional-controls.md "optional-controls.md") are not enabled by default.
- The optional [Data residency controls](data-residency-controls.md "data-residency-controls.md") allow you to customize the Regions
  in which you store and allow access to your data.
- The optional controls that are part of the integrated Security Hub standard allow you
  to scan your AWS Control Tower environment to check for security risks.
- The optional proactive controls allow you to check your CloudFormation resources before
  they are provisioned, to make sure the new resources will comply with your
  environment's control objectives.

###### Customize your AWS CloudTrail trails

- When you update your landing zone to version 3.0 or later, you can choose to
  opt into or opt out of organization-level CloudTrail trails managed by AWS Control Tower. You
  can change this selection any time you update your landing zone. AWS Control Tower
  creates an organization-level trail in your management account, and that trail
  enters active or inactive status, based on your choice. Landing zone 3.0 does
  not support account-level CloudTrail trails; however, if you require these, you can
  configure and manage your own trails. You may incur additional cost for
  duplicate trails.

###### Create customized member accounts in the console

- You can create AWS Control Tower member accounts that are customized, and you can
  update existing member accounts to add customizations, from the AWS Control Tower
  console. For more information, see [Customize accounts with Account Factory
  Customization (AFC)](af-customization-page.md "af-customization-page.md").
