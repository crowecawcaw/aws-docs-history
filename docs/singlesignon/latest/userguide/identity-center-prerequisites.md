# IAM Identity Center prerequisites and

considerations

You can use IAM Identity Center for access to AWS managed applications only, AWS accounts only, or
both. If you are using IAM federation to manage access to AWS accounts, you can
continue to do so while using IAM Identity Center for application access.

Before enabling IAM Identity Center, consider the following:

- AWS Region

You first enable IAM Identity Center in a single, [supported](regions.md "regions.md") Region
for each instance of IAM Identity Center. If you want to use IAM Identity Center for single-sign on access to
AWS accounts, the Region must be accessible by all of the users in your
organization. If you plan to use IAM Identity Center for application access, be aware that some
AWS managed applications, such as Amazon SageMaker AI, can operate only in the Regions they
support. Also, most AWS managed applications require IAM Identity Center to be available in
the same Region as the application. This can be achieved by co-locating them in the same Region,
or when supported, by replicating the IAM Identity Center instance to the desired deployment Region of
an AWS managed application. For more
information, see [Considerations for choosing an
AWS Region](identity-center-region-considerations.md "identity-center-region-considerations.md").

- Application access only

You can use IAM Identity Center only for user access to applications such as Kiro, using
your existing identity provider. For more information, see [Using IAM Identity Center for user access to applications
only](identity-center-for-apps-only.md "identity-center-for-apps-only.md").

###### Note

Access to application resources is managed independently by the application
owner.

- Quota for IAM roles

IAM Identity Center creates IAM roles to give users permissions to account resources. For more
information, see [IAM roles created by IAM Identity Center](identity-center-and-iam-roles.md "identity-center-and-iam-roles.md").

- IAM Identity Center and AWS Organizations

AWS Organizations is recommended, but not required, for use with IAM Identity Center. If you haven't set up
an organization, you do not have to. If you've already set up AWS Organizations and are going to
add IAM Identity Center to your organization, make sure that all AWS Organizations features are enabled. For
more information, see [IAM Identity Center and AWS Organizations](identity-center-and-orgs.md "identity-center-and-orgs.md").
IAM Identity Center web interfaces, including the access portal and the IAM Identity Center console, are intended to be accessed by humans through supported web browsers. Compatible browsers include the latest three versions of Microsoft Edge, Mozilla Firefox, Google Chrome, and Apple Safari. Accessing these endpoints using non-browser based paths is not supported. For programmatic access to IAM Identity Center services, we recommend using the documented APIs available in the IAM Identity Center and Identity Store API reference guides.
