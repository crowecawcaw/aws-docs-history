# AWS Service Catalog and

AWS Organizations

Service Catalog enables you to create and manage catalogs of IT services that are approved for use on
AWS.

The integration of Service Catalog with AWS Organizations simplifies the sharing of portfolios and copying of
products across an organization. Service Catalog administrators can reference an existing organization
in AWS Organizations when sharing a portfolio, and they can share the portfolio with any trusted
organizational unit (OU) in the organization's tree structure. This eliminates the need to
share portfolio IDs, and for the receiving account to manually reference the portfolio ID
when importing the portfolio. Portfolios shared via this mechanism are listed in the
shared-to account in the administrator’s **Imported Portfolio** view in
Service Catalog.

For more information about Service Catalog, see the [_Service Catalog Administrator Guide_](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md").

Use the following information to help you integrate
AWS Service Catalog with AWS Organizations.

## Service-linked roles created when

you enable integration

AWS Service Catalog doesn't create any service-linked roles as part of enabling trusted
access.

## Service principals used to

grant permissions

To enable trusted access, you must specify the following service principal:

- `servicecatalog.amazonaws.com`

## Enabling trusted access with

Service Catalog

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Service Catalog console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Service Catalog console or
tools to enable integration with Organizations. This lets AWS Service Catalog perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Service Catalog. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Service Catalog console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the Service Catalog CLI or AWS SDK

Call one of the following commands or operations:

- AWS CLI: [aws
  servicecatalog enable-aws-organizations-access](../../../cli/latest/reference/servicecatalog/enable-aws-organizations-access.md "../../../cli/latest/reference/servicecatalog/enable-aws-organizations-access.md")
- AWS SDKs: [AWSServiceCatalog::EnableAWSOrganizationsAccess](../../../servicecatalog/latest/dg/API_EnableAWSOrganizationsAccess.md "../../../servicecatalog/latest/dg/API_EnableAWSOrganizationsAccess.md")

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Service Catalog** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Service Catalog** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Service Catalog that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Service Catalog as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal servicecatalog.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

Service Catalog

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

If you disable trusted access using AWS Organizations while you are using Service Catalog, it doesn't
delete your current shares, but it prevents you from creating new shares throughout your
organization. Current shares won't be in sync with your organization structure if it
changes after you call this action.

###### To disable trusted access using the Service Catalog CLI or AWS SDK

Call one of the following commands or operations:

- AWS CLI: [aws
  servicecatalog disable-aws-organizations-access](../../../cli/latest/reference/servicecatalog/disable-aws-organizations-access.md "../../../cli/latest/reference/servicecatalog/disable-aws-organizations-access.md")
- AWS SDKs: [DisableAWSOrganizationsAccess](../../../servicecatalog/latest/dg/API_DisableAWSOrganizationsAccess.md "../../../servicecatalog/latest/dg/API_DisableAWSOrganizationsAccess.md")

You can disable trusted access by using either the AWS Organizations console,
by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Service Catalog** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS Service Catalog** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Service Catalog that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Service Catalog as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal servicecatalog.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")
