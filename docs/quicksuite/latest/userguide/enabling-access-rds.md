# Authorizing connections from Amazon Quick Sight to Amazon RDS DB

instances

|                                                                 |
| --------------------------------------------------------------- |
| \*_Applies<br>to:_<br>• Enterprise Edition and Standard Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

For Amazon Quick Sight to connect to an Amazon RDS DB instance, you must create a new security group
for that DB instance. This security group contains an inbound rule authorizing access
from the appropriate IP address range for the Quick Suite servers in that
AWS Region. To learn more about authorizing Quick Suite connections, see [Manually
enabling access to an Amazon RDS instance in a VPC](../../../quicksight/latest/user/rds-vpc-access.md "../../../quicksight/latest/user/rds-vpc-access.md") or [Manually
enabling access to an Amazon RDS instance that is not in a VPC](../../../quicksight/latest/user/rds-classic-access.md "../../../quicksight/latest/user/rds-classic-access.md").

To learn more about authorizing Amazon Quick Sight connections manually, see [Manually
enabling access to an Amazon RDS instance in a VPC](../../../quicksight/latest/user/rds-vpc-access.md "../../../quicksight/latest/user/rds-vpc-access.md") or [Manually
enabling access to an Amazon RDS instance that is not in a Amazon VPC](../../../quicksight/latest/user/rds-classic-access.md "../../../quicksight/latest/user/rds-classic-access.md").

To create and assign a security group for an Amazon RDS DB instance, you must have AWS
credentials that permit access to that DB instance.

Enabling connection from Amazon Quick Suite servers to your instance is just one of several
prerequisites for creating a data set based on an AWS database data source. For more
information about what is required, see [Creating a dataset from a database](../../../quicksight/latest/user/create-a-database-data-set.md "../../../quicksight/latest/user/create-a-database-data-set.md").

###### Topics

- [Manually enabling Amazon Quick Sight access to an Amazon RDS
  instance in a VPC](#rds-vpc-access "#rds-vpc-access")
- [Manually enabling access from Amazon Quick Sight to an
  Amazon RDS instance that is not in a VPC](#rds-classic-access "#rds-classic-access")

## Manually enabling Amazon Quick Sight access to an Amazon RDS

instance in a VPC

Use the following procedure to enable Amazon Quick Sight access to an Amazon RDS DB instance in a
VPC. If your Amazon RDS DB instance is in subnet that is private (in relation to
Amazon Quick Suite) or that has Internet Gateways attached, see [Connecting to a VPC with Amazon Quick Suite](../../../quicksight/latest/user/working-with-aws-vpc.md "../../../quicksight/latest/user/working-with-aws-vpc.md").

###### To enable Amazon Quick Sight access to an Amazon RDS DB instance in a VPC

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**, locate the DB instance, and view
   its details. To do this, you click directly on its name (a hyperlink in the
   **DB identifier** column).
3. Locate **Port** and note the **Port**
   value. This can be a number or a range.
4. Locate **VPC** and note the **VPC**
   value.
5. Choose the **VPC** value to open the VPC console. In the
   Amazon VPC Management Console, choose **Security Groups** in the
   navigation pane.
6. Choose **Create Security Group**.
7. On the **Create Security Group** page, enter the security
   group information as follows:
   - For **Name tag** and **Group
     name**, enter
     `Amazon-QuickSight-access`.
   - For **Description**, enter
     `Amazon-QuickSight-access`.
   - For **VPC**, choose the VPC for your instance.
     This VPC is the one with the **VPC ID** that you
     noted previously.

8. Choose **Create**. On the confirmation page, note the
   **Security Group ID**. Choose
   **Close** to exit this screen.
9. Choose your new security group from the list, and then choose
   **Inbound Rules** from the tab list below.
10. Choose **Edit rules** to create a new rule.
11. On the **Edit inbound rules** page, choose **Add
    rule** to create a new rule.

Use the following values:

    * For **Type**, choose **Custom TCP
     Rule**.
    * For **Protocol**, choose
     **TCP**.
    * For **Port Range**, enter the port number or
     range of the Amazon RDS cluster. This port number (or range) is the one
     that you noted previously.
    * For **Source**, choose
     **Custom** from the list. Next to the word
     "Custom", enter the CIDR address block for the AWS Region where
     you plan to use Amazon Quick Suite.


    For example, for Europe (Ireland) you would enter
     Europe (Ireland)'s CIDR address block:
     `52.210.255.224/27`. For more information on the IP
     address ranges for Amazon Quick Suite in supported AWS Regions, see
     [AWS Regions, websites, IP address ranges,
     and endpoints](../../../quicksight/latest/user/regions.md "../../../quicksight/latest/user/regions.md").


    ###### Note

    If you have activated Amazon Quick Suite in multiple AWS Regions,
     you can create inbound rules for each Amazon Quick Suite endpoint
     CIDR. Doing this allows Amazon Quick Suite to have access to the Amazon RDS
     DB instance from any AWS Region defined in the inbound rules.

    Anyone who uses Amazon Quick Suite in multiple AWS Regions is
     treated as a single user. In other words, even if you are using
     Amazon Quick Suite in every AWS Region, both your Amazon Quick Suite
     subscription (sometimes called an 'account') and your users are
     global.

12. For **Description**, enter a useful description, for
    example "`Europe (Ireland) QuickSight`".
13. Choose **Save rules** to save your new inbound rule. Then
    choose **Close**.
14. Go back to the detailed view of the DB instance. Return the Amazon RDS console
    ([https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/")) and choose
    **Databases**.
15. Choose the DB identifier for the relevant RDS instance. Choose
    **Modify**. The same screen displays whether you choose
    Modify from the databases screen or the DB instance screen: **Modify
    DB Instance**.
16. Locate the **Network & Security** section (the third
    section from the top).

The currently assigned security group or groups are already chosen for
**Security Group**. Don't remove any of the existing
ones unless you are sure.

Instead, choose your new security group to add it to the other groups that
are selected. If you followed the name suggested previously, this group
might be named something similar to
**Amazon-QuickSight-access**. 17. Scroll to the bottom of the screen. Choose **Continue**.
and then choose **Modify DB Instance**. 18. Choose **Apply during the next scheduled maintenance**
(the screen indicates when this will occur).

Don't choose **Apply immediately**. Doing this also
applies any additional changes that are in the pending modifications queue.
Some of these changes might require downtime. If you bring the server down
outside the maintenance window, this can cause a problem for users of this
DB instance. Consult your system administrators before applying immediate
changes. 19. Choose **Modify DB Instance** to confirm your changes.
Then, wait for the next maintenance window to pass.

## Manually enabling access from Amazon Quick Sight to an

Amazon RDS instance that is not in a VPC

Use the following procedure to access an Amazon RDS DB instance that is not in a VPC.
You can associate a security group with a DB instance by using **Modify** on the RDS console, the `ModifyDBInstance` Amazon
RDS API, or the `modify-db-instance` AWS CLI command.

###### Note

This section included for backwards compatibility purposes.

###### To use the console to access an Amazon RDS DB instance that is not in a

VPC

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**, select the DB instance, and choose
   **Modify**.
3. Choose **Security Groups** in the navigation pane.
4. Choose **Create DB Security Group**.
5. Enter `Amazon-QuickSight-access` for the
   **Name** and **Description** values,
   and then choose **Create**.
6. The new security group is selected by default.

Select the details icon next to the security group, as shown
following. 7. For **Connection Type**, choose
**CIDR/IP**. 8. For **CIDR/IP to Authorize**, enter the appropriate CIDR
address block. For more information on the IP address ranges for
Amazon Quick Suite in supported AWS Regions, see [AWS
Regions, websites, IP address ranges, and endpoints](../../../quicksight/latest/user/regions.md "../../../quicksight/latest/user/regions.md"). 9. Choose **Authorize**. 10. Return to the **Instances** page of the Amazon RDS Management
Console, choose the instance that you want to enable access to, choose
**Instance Actions**, and then choose
**Modify**. 11. In the **Network & Security** section, the currently
assigned security group or groups already is chosen for **Security
Group**. Press CTRL and choose
**Amazon-QuickSight-access** in addition to the other
selected groups. 12. Choose **Continue**, and then choose **Modify DB
Instance**.
