# Managing Resolver on Outpost

To manage Resolver on Outpost, perform the applicable procedure.

###### Topics

- [Editing Resolver on Outpost](#outpost-edit-resolver "#outpost-edit-resolver")
- [Viewing Resolver on Outpost status](#outpost-view-resolver-status "#outpost-view-resolver-status")
- [Deleting Resolver on Outpost](#outpost-delete-resolver "#outpost-delete-resolver")

## Editing Resolver on Outpost

To edit a Resolver on Outpost, perform the following procedure.

###### To edit a

Resolver on Outpost

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the checkmark next to the Resolver that is in operational state and
   choose **Edit**.
5. You can edit the following information:
   - The Resolver name
   - The instance type
   - The number of instances

6. After you are done editing, choose **Save
   changes**.

## Viewing Resolver on Outpost status

To view the status for Resolver on Outpost, perform the following procedure.

###### To view the status for

an inbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the checkmark next to the Resolver that is in operational state and
   choose **View details**.
5. The **Status** column in the
   **Resolver on Outpost** page, contains one of the following
   values:

**Creating**

The Resolver on Outpost is in the process of being created.

**Operational**

The Resolver on Outpost is correctly configured.

**Updating**

The Resolver on Outpost is updating instance types.

**Action needed**

This Resolver is unhealthy and can't be automatically recovered.
To resolve the problem, we recommend that you make sure the
instance AWS Outposts can support Resolver on Outpost.

**Deleting**

The Resolver on Outpost is in the process of being deleted.

**Failed creation**

The creation of Resolver on Outpost failed.

**Failed deletion**

The deletion of Resolver on Outpost failed. To fix this issue, try again
in a few minutes.

## Deleting Resolver on Outpost

###### Note

Before you can delete a Resolver on Outpost, you must first delete any endpoints
associated with it.

To delete a Resolver on Outpost, perform the following procedure.

###### To delete a Resolver on Outpost

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the check box next to the Resolver that is in operational state and
   choose **Delete**.
5. In the **Delete Resolver** dialog box, enter
   `delete` in the text box, and choose
   **Delete**.
