# Granted licenses in License Manager

Granted licenses are licenses for products that your organization purchased from [AWS Marketplace](../../../marketplace/latest/buyerguide/what-is-marketplace.md "../../../marketplace/latest/buyerguide/what-is-marketplace.md"), [AWS Data Exchange](../../../data-exchange/latest/userguide/what-is.md "../../../data-exchange/latest/userguide/what-is.md"), or directly
from a seller who integrated their software with managed entitlements. License administrators
can use AWS License Manager to govern the use of these licenses and to distribute rights of use, known
as entitlements, to specific AWS accounts.

Data licenses distributed to AWS Data Exchange products are available to the AWS
account through AWS Data Exchange. Before you can distribute licenses from AWS Marketplace, you must
enable subscription sharing. For more information, see [Sharing
subscriptions in an organization](../../../marketplace/latest/buyerguide/organizations-sharing.md "../../../marketplace/latest/buyerguide/organizations-sharing.md").

After a license administrator distributes an entitlement from an AWS Marketplace license to an AWS
account, and the recipient accepts and activates the granted license, the subscription is
available to the AWS account through AWS Marketplace. The account also has access to the product. For
example, if a license administrator purchases an Amazon Machine Image (AMI) from AWS Marketplace and
distributes an entitlement to your AWS account, you can launch Amazon EC2 instances from the AMI
using AWS Marketplace and Amazon EC2.

###### Topics

- [View your granted licenses](#granted-licenses-views "#granted-licenses-views")
- [Manage your granted licenses in License Manager](manage-granted-licenses.md "manage-granted-licenses.md")
- [Distribute License Manager entitlements](distribute-entitlement.md "distribute-entitlement.md")
- [Grant acceptance and activation in License Manager](grant-acceptance.md "grant-acceptance.md")
- [License status for grants in License Manager](grant-statuses.md "grant-statuses.md")
- [CloudWatch metrics for buyer accounts in License Manager](how-metrics-emit-buyers.md "how-metrics-emit-buyers.md")

## View your granted licenses

License Manager displays tabs to view and manage your granted licenses based on the
permissions you are authenticated with. The granted license page can display the
following tabs:

**My licenses**

This tab is available for any user that has access to view the granted
licenses in License Manager. The tab has a **My granted licenses**
section which includes information about each license such as the
**License ID** and **Product name**. From
this page you can view additional information about each license.

**License summary (for organization administrators)**

This tab is available only for organization administrators. The tab has a
**Totals** section which lists the total amount of products
and granted licenses across all accounts in your organization. It also shows a
**Products** section which includes a table detailing the
properties of each product, such as the **Product name** and
**Number of granted licenses**.

**Aggregated licenses (for organization administrators)**

This tab is available only for organization administrators. This tab has a
section detailing **Granted licenses for my organization** which
includes information about each license such as the **License
ID** and **Product name**. From this page you can
view additional information about each license.
