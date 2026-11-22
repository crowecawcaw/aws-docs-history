

# Engagements

An engagement is a construct in AWS Transform that gives you a single place to manage your migration and modernization engagements. An engagement brings together the people involved (for example, a customer and their partner), the AWS Transform workspaces where the work runs, and an engagement-scoped chat.

An engagement is separate from a workspace. A workspace is the AWS Transform resource where you run jobs, and it also acts as a permissions boundary for the people and resources inside it. An engagement is not a replacement for your workspaces. Instead, you can group one or more of your existing workspaces related to the same migration or modernization engagement, so you can manage the engagement holistically. Your workspaces keep their own settings, members, and roles.

Every engagement has its own engagement chat, which you open from the engagement page. Each chat is scoped to its engagement to keep information separate from your other engagements. The chat knows only about its own engagement and can access only that engagement's artifacts. It has no knowledge of any other engagement. A new engagement chat starts with fresh context. It doesn't carry over conversations from the general AWS Transform chat or from the engagement chat of any other engagement. As you keep chatting, the chat remembers your conversation, and that context stays within the engagement.

Depending on your use case, a specialized agent answers some requests in the engagement chat. For example, the AWS Migration Acceleration Program (MAP) has a specialized MAP agent that is integrated into AWS Transform engagements. AWS Transform passes your message to that agent, and the answer appears back in the same engagement chat.

## Connect your Partner Central account with AWS Transform (for partners)
<a name="transform-engagements-partner-connect"></a>

As a partner, you can manage your customer engagements in AWS Transform by connecting your Partner Central account with AWS Transform.

**To connect your Partner Central account**

1. In the AWS Transform console, go to **Service management**, **Settings**.

1. Under **Register as AWS partner with AWS Transform**, choose **Connect**.

1. Provide the account ID for your Partner Central account to complete the connection.

## Creating an engagement
<a name="transform-engagements-create"></a>

You access engagements from the AWS Transform menu.

**To create an engagement**

1. In AWS Transform, open **Engagements** from the menu.

1. Choose **Create Engagement**.

1. Provide the details of your engagement.

After you create the engagement, you can invite the other party to join it. Invitations work across AWS Transform tenants, and they work in both directions: a partner can invite a customer, and a customer can invite a partner that is registered with AWS Transform (see [Connect your Partner Central account with AWS Transform (for partners)](#transform-engagements-partner-connect)). Each party works in their own tenant and sees the engagement from their own point of view.

If you are a partner, choose **Invite client**, enter the AWS Transform tenant ID that your customer shares with you, and add a short description so your customer recognizes the invitation.

**To invite a client**

1. Navigate to the **Client details** tile on the engagement page and select **Invite client**.

1. Enter your customer's AWS Transform tenant ID. Your customer can find this information by signing in to AWS Transform and selecting their account menu in the top-right corner.

If you are an AWS customer, open the **Partners** tab and choose **Add partner**, enter the AWS Transform tenant ID that your partner shares with you, and add partner intent.

An engagement can have one partner and one customer. The invited party receives the invitation in their own AWS Transform tenant, in the **Engagements** section of the side panel. Until they accept, the invitation shows a **Pending** status. After they accept, the status changes to **Active** and they can see the engagement. A customer can withdraw an invitation that the partner has not accepted yet. To remove a partner who has already accepted the invitation, contact AWS Support. You cannot invite your own tenant: AWS Transform doesn't accept your own tenant ID as an invitation target. Make sure you ask the other party for their tenant ID, not your own.

The **Administrators** space lists your user details. You can also add other users from your AWS Transform tenant as administrators of the engagement.

On the **Workspaces** tab, you can attach the existing workspaces where you run AWS Transform jobs as part of this engagement. Choose **Add workspace**, and then select from the list of workspaces you already have. Attaching a workspace doesn't move or copy it, and it doesn't change its members or roles.

## Engagement termination
<a name="transform-engagements-terminate"></a>

To terminate an engagement, contact AWS Support. You must be able to sign in to an AWS account to open a support case. If you can't open a support case yourself, ask a person on your team who can, such as the account owner, and include the engagement details in the following list.

**To request that an engagement be terminated**

1. Open a support case with AWS Support.

1. Include the name of the engagement and the engagement ID. The engagement ID appears in the engagement side panel.

1. State that you want the engagement ended and name the account or tenant that is making the request.

1. Wait for confirmation from AWS Support that the request is complete.

After an engagement is terminated, your workspaces and jobs linked to that engagement are not affected. They remain available to the people who have access to them outside the engagement, and those people keep their access.