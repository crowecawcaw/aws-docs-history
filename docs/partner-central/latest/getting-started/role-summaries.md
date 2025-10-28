# AWS Partner Central roles

An AWS Partner Central role is an identity with specific permissions in AWS Partner Central. You can assign a new user a role when you invite them to register, and change role assignments on the **User management** page. This section describes roles and compares role capabilities.

###### Topics

- [Alliance lead](#alliance-lead "#alliance-lead")
- [Alliance team](#alliance-team "#alliance-team")
- [Standard user](#standard-user "#standard-user")
- [Channel user](#channel-user "#channel-user")
- [Cloud admin](#cloud-admin "#cloud-admin")
- [Marketing staff](#marketing-staff "#marketing-staff")
- [Technical staff](#technical-staff "#technical-staff")
- [ACE manager](#ace-manager "#ace-manager")
- [ACE user](#ace-user-staff "#ace-user-staff")
- [Role comparison](#role-comparison "#role-comparison")

## Alliance lead

When you create an AWS Partner Central account, you begin with one role that has complete access to all resources in the account: the alliance lead. The first user to create an account for your company is automatically assigned the alliance lead role. Only one user in your company account can be the alliance lead at one time. Only the alliance lead can reassign the role to another user.

The alliance lead is your company's primary account administrator.
They should have a business development or business leadership role with legal authority to accept the
AWS Partner Network terms and conditions on behalf of your company.

The alliance lead role can do the following:

- View and manage all of your company's account information in AWS Partner Central.
- Manage partner account information, including the partner scorecard, account details, and listing in the [AWS Partner Solutions Finder](https://partners.amazonaws.com/ "https://partners.amazonaws.com/") (for eligible AWS Partners only).
- Assign alliance team, ACE manager, ACE user, technical staff, or marketing staff roles to other users in your AWS Partner account.
- Remove users.
- Reassign the alliance lead role to another user.
- View certification details.
- View and edit opportunities and leads in ACE Pipeline Manager.

## Alliance team

The alliance team role shares administrative responsibility with the alliance lead. They serve as a secondary point of contact for communication regarding your company’s AWS Partner Network membership. An alliance team user supports the alliance lead by managing opportunities and leads in the ACE Pipeline Manager, submitting program applications, and monitoring your Partner scorecard. The alliance lead can assign the alliance team role to up to 20 users.

The alliance team user can do the following:

- Manage partner account information, including the partner scorecard, account details, and listing in the [AWS Partner Solutions Finder](https://partners.amazonaws.com/ "https://partners.amazonaws.com/") (for eligible partners only).
- Assign alliance team, ACE manager, ACE user, technical staff, or marketing staff roles to other users in your account.
- View certification details.
- View and edit opportunities and leads in ACE Pipeline Manager.
- Remove users.

## Standard user

The standard user role can sign in to your AWS Partner Central account, update
personal information, and complete AWS training and certification courses. Alliance lead and
alliance team users can grant standard users access to more resources by assigning them a
different role.

## Channel user

The channel user role is for users who help administer AWS Marketplace Channel Programs and report AWS accounts used for reselling. This role is necessary for users responsible for updating end-user information and program-management accounts on behalf of your organization. You can assign any number of users the channel user role.

In addition to standard user role permissions, the channel user can access the **Channel Management** page.

## Cloud admin

The user with the cloud admin role is your company's Identity and Access Management (IAM) administrator of your AWS
accounts and the primary point of contact for AWS Marketplace. The alliance lead can assign multiple users to the cloud admin role.
Only alliance lead or cloud admin users can reassign the cloud admin role to another user. The alliance lead user may assign themselves
the cloud admin role to link AWS Partner Central and AWS Marketplace accounts.

When you link your AWS Partner Central account to an AWS Marketplace seller account, AWS Marketplace creates an IAM role called
`cloud admin` in your account. It makes you the cloud admin role by default (if you were not already)
and associates the cloud admin IAM role to your AWS Partner Central account. The cloud admin role has IAM permissions to map AWS Partner Central users to IAM roles.

### Cloud admin role IAM permissions

The cloud admin role has the following IAM permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PassPartnerCentralRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/PartnerCentralRoleFor*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "Partnercentral-account-management.amazonaws.com"
 }
 }
 },
 {
 "Sid": "PartnerUserRoleAssociation",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "Partnercentral-account-management:AssociatePartnerUser",
 "Partnercentral-account-management:DisassociatePartnerUser"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Marketing staff

The marketing staff role can view and edit all areas of AWS Partner Central with marketing components, such as AWS Partner Marketing Central, AWS Partner Network (APN) Badge Manager, AWS Partner Solutions Finder, and AWS Partner References. Marketing staff users have a top of funnel view of leads and campaigns by AWS Region and campaign type. The role helps users identify the most effective marketing channels and prioritize market development fund (MDF) utilization. In addition, marketing staff users can participate in lead and opportunity management and provide details on the AWS Partner Program application to earn designations. The alliance lead can assign any number of users the marketing staff role.

The marketing staff role is ideal for users responsible for promotional campaigns or branding, such as:

- Members of a marketing team that build awareness for customer acquisition, maturation, and expansion based on Partner technical business strategies.
- Members of a marketing coordinator team responsible for operational marketing needs and editing campaign and lead-generation information.

The marketing staff role can do the following:

- Access AWS training and certification courses.
- Submit case studies.
- Access AWS Partner Marketing Central and AWS sponsorships.
- Create and build using the APN Marketing Toolkit.
- Create and edit your company listing in the AWS Partner Solutions Finder.
- View and edit public references.
- Use APN Badge Manager.
- View and edit leads and opportunities managed by the marketing staff role.
- Submit opportunities.
- View or edit opportunities submitted by all users.
- Accept, reject, view, and edit all opportunities and leads shared with all users.
- Transfer ownership of all opportunities and leads to other users.
- Perform bulk imports, exports, updates, and transfers of all opportunities and bulk exports and transfers of all leads.
- Update leads and opportunities on behalf of sales teams.
- Download pipeline data to create reports.

## Technical staff

The technical staff role can view and edit all AWS Partner Central resources with technical components, such as offerings, case studies, and Well-Architected workloads. AWS Partner Central provides these users with access to resources that build their AWS technical knowledge, including personalized recommendations on relevant training and certifications that match the organization’s profile and market needs. Technical staff users can participate in technical reviews of your organization's offerings and provide details on your AWS Partner program application to earn designations. The alliance lead can assign any number of users the technical staff role.

The technical staff role is for users who need to submit opportunities to AWS through the ACE Pipeline Manager and manage those opportunities throughout their lifecycle. This role is the best option for users responsible for managing a set of opportunities or leads without access to view or edit entries owned by other users. For example:

- Members of a product development team that build awareness for customer acquisition, maturation, and expansion based on Partner technical business strategies.
- Members of a presales technical team responsible for delivering proof-of-concept projects, managing implementations, and professional service engagements.
- Members of a technical team responsible for technical guidance for customer solutions including architecture, applications, software, and services.

The technical staff role can do the following:

- Access training and certification courses.
- Build offerings.
- Build technical validations.
- Build case studies.
- Build device listings.
- Build Well-Architected workloads.
- Create and edit program applications.

## ACE manager

The APN Customer Engagements (ACE) manager role can view and edit opportunities and leads in the ACE Pipeline Manager. Additionally, When AWS shares a lead with a partner, or requires more information about a partner-submitted opportunity, the ACE manager receives an automated email notification. The alliance lead can assign the ACE manager role to up to 20 users.

The ACE manager role is the ideal option for users responsible for managing or overseeing all AWS leads and opportunities in your organization without the additional access provided by the alliance team role. For example:

- Members of an operations team that manage data input and opportunities for sales teams.
- Members of a sales team that enter and manage lead and opportunity data.
- Members of a marketing team who want to oversee lead activity.

The ACE manager role provides users access to update all opportunities and leads in the ACE Pipeline Manager. It is important that new users review the ACE program documentation available on AWS Partner Central. For users who only need to manage the opportunities they actively own, the ACE user role is a more appropriate assignment.

The ACE manager role can do the following:

- Submit opportunities.
- View or edit opportunities submitted by all users.
- Accept, reject, view, and edit all opportunities and leads shared with all users.
- Transfer ownership of all opportunities and leads to other users.
- Perform bulk imports, exports, updates, and transfers of all opportunities and bulk exports and transfers of all leads.
- Update leads and opportunities on behalf of sales teams.
- Download pipeline data to create reports.

## ACE user

The ACE user role can access the **My Customers** tab in Partner Central to submit opportunities to the ACE Pipeline Manager. ACE users can access and manage only the opportunities and leads that they own. You can assign any number of users the ACE user role.

The ACE user role is for users who need to submit opportunities to AWS through the ACE Pipeline Manager and manage those opportunities throughout their lifecycle. This role is the best option for users responsible for managing a set of opportunities or leads without access to view or edit entries owned by other users.

To enable ACE users to link ACE opportunities to AWS Marketplace private offers, provide `AWSMarketplaceSellerFullAccess` or, minimally, `ListEntities/SearchAgreements` to the IAM role assigned to ACE users. For more information, refer to [Linking AWS Partner Central and AWS
accounts](linking-apc-aws-marketplace.md "linking-apc-aws-marketplace.md").

The ACE user role can do the following:

- Submit opportunities.
- View, edit, and update owned opportunities.
- Transfer owned opportunities and leads to other users.
- Perform bulk imports, exports, updates, and transfers of owned opportunities and bulk transfers of owned leads.

## Role comparison

Your role determines your access to AWS Partner Central resources and ability to perform tasks. The following table compares role abilities. It does not include the [Standard user](#standard-user "#standard-user") role, which has limited access in AWS Partner Central. A user with the standard user role can sign in, access their personal profile, and access AWS training courses.

| Task                                                                     | Alliance lead | Alliance team | Cloud admin | Marketing staff | Technical staff | ACE manager | ACE user |
| ------------------------------------------------------------------------ | ------------- | ------------- | ----------- | --------------- | --------------- | ----------- | -------- |
| Reassign alliance lead role                                              | ✓             |               |             |                 |                 |             |          |
| Assign ACE manager, ACE user, marketing staff, and technical staff roles | ✓             | ✓             | ✓           |                 |                 |             |          |
| Remove users                                                             | ✓             | ✓             | ✓           |                 |                 |             |          |
| Submit ACE opportunities                                                 | ✓             | ✓             |             | ✓               |                 | ✓           | ✓        |
| Manage all ACE opportunities and leads                                   | ✓             | ✓             |             | ✓               |                 | ✓           |          |
| Manage owned ACE opportunities and leads                                 | ✓             | ✓             |             | ✓               | ✓               | ✓           | ✓        |
| Manage AWS Partner Solution Finder listing                               | ✓             | ✓             |             | ✓               |                 |             |          |
| Access training and certification data                                   | ✓             | ✓             |             |                 |                 |             |          |
| Apply to an AWS Competency Program                                       | ✓             | ✓             |             |                 | ✓               |             |          |
| Manage offerings                                                         | ✓             | ✓             |             | ✓               | ✓               |             |          |
| Build Well-Architected workloads                                         | ✓             | ✓             |             |                 | ✓               |             |          |
| Build case studies                                                       | ✓             | ✓             |             | ✓               | ✓               |             |          |
| Build with the APN Marketing Toolkit                                     | ✓             | ✓             |             | ✓               |                 |             |          |
| Manage public references                                                 | ✓             | ✓             |             | ✓               |                 |             |          |
| Access APN Badge Manager                                                 | ✓             | ✓             |             | ✓               |                 |             |          |
| Manage program applications                                              | ✓             | ✓             |             |                 | ✓               |             |          |
