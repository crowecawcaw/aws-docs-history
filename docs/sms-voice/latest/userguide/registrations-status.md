# Check a registration's status in AWS End User Messaging SMS

Your registration will be in one of these different
statuses:

- **AUTHENTICATION_REQUIRED** – You need to complete
  two-factor authentication for your registration.
- **CLOSED** – You deleted the resources and must also delete
  the registration for the number.
- **COMPLETE** – Your registration has been approved and you
  can start using the resource.
- **CREATED** – Your registration is created but not
  submitted.
- **DELETED** – Your registration has been deleted.
- **REVIEWING** – Your registration has been accepted and is
  being reviewed. You can't make any changes to your registration or any resources associated to the registration while it is in this state.
- **REQUIRES_UPDATES** – You must fix your registration and
  resubmit it. See [Edit a registration in AWS End User Messaging SMS](registrations-edit.md "registrations-edit.md") for more information. Fields that require
  updates display a warning icon and a brief description of the issue.
- **SUBMITTED** – Your registration has been submitted and is
  awaiting review.

###### Check your registration status

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Registrations**.
3. On the **Registrations** table, you can then view the
   registration **Status** of each registration.
