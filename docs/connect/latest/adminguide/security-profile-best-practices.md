# Best practices for Amazon Connect and Contact

Control Panel (CCP) security profiles

- Limit who has **Users - Edit or Create** permissions

People with these permissions pose a risk to your contact center because they
can do the following:

    + Reset passwords, including that of the administrator.
    + Grant other users permission to the Admin security profile. People
     assigned to the Admin security profile have full access to your contact
     center.

Doing these things would enable someone to lock out those who need to access
Amazon Connect, and allow in others who can steal customer data and damage your business.

To reduce the risk, as a best practice we recommend limiting the number of
people who have **Users - Edit or Create** permissions.

- [Use AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") to log the
  requests and responses of [UpdateUserIdentityInfo](../APIReference/API_UpdateUserIdentityInfo.md "../APIReference/API_UpdateUserIdentityInfo.md"). This enables you to track changes made to
  user information. Someone who has the ability to call the
  `UpdateUserIdentityInfo` API can change a user's email address to
  one owned by an attacker, and then reset the password through email.
- [Understand inherited
  permissions](inherited-permissions.md "inherited-permissions.md")

Some security profiles included inherited permissions: when you assign
dedicated permissions to one object, by default permissions are granted to
sub-objects. For example, when you grant dedicated permission to edit users, you
also grant them permission to list all security profiles for your Amazon Connect
instance. This is because to edit users, the person has access to the drop-down
list of security profiles.

Before assigning security profiles, review the list of inherited
permissions.

- **Understand the implications of [access
  control tags](tag-based-access-control.md "tag-based-access-control.md") before applying them to a security
  profile.** Applying access control tags is an advanced
  configuration feature that is supported by Amazon Connect and that follows the AWS
  shared responsibility model. Ensure that you have read the documentation and
  understand the implications of applying granular permission configurations. For
  more information, review the [AWS shared responsibilities
  model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").
- Track who accesses recordings.

In the **Analytics and Optimization** permission group, you
can enable a download icon for recorded conversations. When members of this
group go to **Analytics and optimization**, **Contact
search**, and then search contacts, they will see an icon to
download recordings.

###### Important

This setting isn't a security feature. **Users who
don't have this permission can still download recordings using other
less-discoverable ways**.

We recommend that you track who in your organization accesses
recordings.
