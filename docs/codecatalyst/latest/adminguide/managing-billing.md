Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Administering billing

Your CodeCatalyst space uses resources, such as Dev Environments and compute, that are charged
based on separate subscription tiers. To check your usage and to view pricing for each
subscription tier, see the **Billing** tab for your space.

You can view or change your CodeCatalyst subscription for your space. CodeCatalyst has the
following tiers available.

- Free
- Standard
- Enterprise
  For more information about billing and rates, see the [Amazon CodeCatalyst pricing page](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").

Additional considerations:

- All spaces are required to have a billing account, even if the usage does not
  exceed the Free tier.
- AWS is the billing provider for CodeCatalyst. The account you use for billing must be
  an AWS account.
- Billing is configured at the space level. Multiple AWS accounts can be
  associated with a space, but only one can be active for CodeCatalyst billing at a
  time. An AWS account can be used as a billing account for more than one space
  in CodeCatalyst. The AWS account that is specified as the billing account for your
  CodeCatalyst space has different quotas from other account connections for a
  space. For more information, see [Quotas](../userguide/quotas.md "../userguide/quotas.md") in the _CodeCatalyst User Guide_.
- You can view your CodeCatalyst charges on your AWS invoice, including current charges.
  Billing data is updated regularly on the AWS Management Console page for AWS Billing.
  Here is one possible flow to set up billing in CodeCatalyst.

Mary Major is a **Space administrator** for a CodeCatalyst
space. Mary works with the AWS administrator for the AWS account that was added to
her space in CodeCatalyst when it was created and so defaults as the billing account. Mary
can also specify a different account as a billing account for her space. Mary initially
set up her subscription to default to the Free tier. Mary knows that hitting the maximum can
halt services for the rest of her space on the Free tier, so she periodically reviews
usage for her space on the CodeCatalyst console **Billing** tab. Mary views
the pricing subscription for the Standard tier, and after the space grows in size, Mary
decides to use the CodeCatalyst billing page to change the subscription tier from the Free tier to
the Standard tier. Mary works with her AWS administrator to access her AWS invoice and
views the charges for usage beyond the Free tier in CodeCatalyst.
