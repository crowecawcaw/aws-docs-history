# Best practices for landing zone updates

This section gives some considerations and best practices to keep in mind when you are
considering an upgrade of your landing zone version in AWS Control Tower. The change from the 2.0
landing zone version series into the 3.0 landing zone version series is especially
important. When you upgrade your landing zone, AWS Control Tower automatically moves you to the
latest available version.

###### Note

It is a best practice to update to the latest version of the landing zone.

###### Summary of best practices explained in this section

- **Best practice:** For security and audit reasons, we
  strongly recommend that you enable logging across the board, for all accounts, and
  send logging information to a centralized location. In AWS Control Tower, this centralized
  location is the **Log archive** account, which provides an Amazon S3 logging bucket.
- **Best practice:** If you opt out of the
  organization-level CloudTrail trail in AWS Control Tower, set up and manage your own trails.
- **Best practice:** When operating your AWS Control Tower
  environment, set up a testing environment.

###### Benefits for moving from 2.x landing zone versions to 3.x landing zone

versions

- Record AWS Config resources only in the home Region, which creates cost savings when you
  manage global resources
- Encrypt your AWS CloudTrail trail with your own KMS key
- Customize your log retention timeframe
- Enhanced mandatory controls
- Increased number of controls available
- Integrated with AWS Security Hub CSPM
- Python runtime updates

###### Caveats for moving from 2.x landing zone versions to 3.x landing zone versions

- With landing zone 3.0 and later, AWS Control Tower no longer supports account-level
  AWS CloudTrail trails that AWS manages.
- You have an option to choose an organization-level trail managed by AWS Control Tower, or
  to opt out of it and manage your own CloudTrail trails.
- Some potential exists for double costs, especially if some accounts within an OU
  are not enrolled in AWS Control Tower and have account-level trails of their own that you
  want to keep.

###### Considerations about choosing organization-level CloudTrail trails

- When you upgrade to 3.0 or later, AWS Control Tower deletes the account-level trails that
  it originally created, after 24 hours. [[Exception]](retain-account-trails.md "retain-account-trails.md")
- No data from these trails is lost. Your existing logs are preserved even when the
  trails are removed.
- AWS Control Tower creates a new path in the same Amazon S3 bucket for the trails, to
  differentiate account-level trails from organization-level trails.
  - An account trail log path is of this form:
    `/orgId/AWSLogs/...`
  - An organization trail log path is of this form:
    `/orgId/AWSLogs/orgId/...`

- Additional CloudTrail trails that you have deployed, trails not deployed by AWS Control Tower,
  are not touched.
- All accounts are included in the organization-level trail—including
  accounts not enrolled in AWS Control Tower—if the unenrolled accounts are part of a
  registered OU.
- Amazon CloudWatch alarms in linked accounts are not triggered.
- If you opt out of an organization-level trail, AWS Control Tower still creates the trail,
  but sets its status to **Off**.
- As a best practice, if you opt out of the organization-level trail in AWS Control Tower,
  you should set up and manage your own CloudTrail trails,

###### Benefits of organization-level trails

- The organization trail works across all accounts in the OU.
- The logged items are standardized and cannot be modified by account users.
  **Consider a testing environment**

When you upgrade your landing zone, AWS Control Tower makes changes only to the shared accounts and
the Foundational OU. It does not make changes to your workload accounts or OUs.
_However, as a best practice, when operating your AWS Control Tower environment, we
recommend that you set up a testing environment._ Within the isolated testing
environment, you can test the AWS Control Tower landing zone upgrades, as well as any changes you may
make to service control policies (SCPs), and you can test the controls that you wish to
apply to the environment. This recommendation is especially helpful if you are operating in
a regulated industry.

**Checklist for common errors when updating**

Here is a short list of tasks you can perform to avoid common errors when updating your AWS Control Tower landing zone from 2.x versions to 3.x versions.

###### Basic update checklist

- Check your landing zone:

– Go to the AWS Control Tower service, review the **Organizational units** and **Accounts** pages, and then confirm that your account state is set to **Registered** and **Enrolled**.

– If applicable, verify and confirm that the last run of your customizations pipeline was successful.

– Check the Amazon S3 centralized logging bucket in the **Audit** account, because any changes previously made to the bucket policy will be overwritten.

- Validate that any SCPs not owned by AWS Control Tower will not restrict
  the `AWSControlTowerExecution` role from performing actions in member accounts, or
  actions in the management account, for the administrative role that's performing the update.
