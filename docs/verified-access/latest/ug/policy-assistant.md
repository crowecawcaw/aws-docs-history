# Verified Access policy assistant

The Verified Access policy assistant is a tool in the Verified Access console that you can use to test and
develop your polices. It presents the endpoint policy, the group policy, and the trust context
on one screen, where you can test and make edits to the policies.

Trust context formats vary across different trust providers, and sometimes the Verified Access
administrator might not know the exact format a certain trust provider uses. That is why it can be
very helpful to see the trust context, and both the group and endpoint policies in one place
for testing and developing purposes.

The following sections describe the basics of using the policy editor.

###### Tasks

- [Step 1: Specify your resources](#specify-resources "#specify-resources")
- [Step 2: Test and edit policies](#test-and-edit "#test-and-edit")
- [Step 3: Review and apply changes](#review-and-commit "#review-and-commit")

## Step 1: Specify your resources

On the first page of the policy assistant, you specify the Verified Access endpoint
that you want to work with. You will also specify a user (identified by email address), and
optionally, the user’s name and/or a device identifier. By default, the most
recent authorization decision is extracted from the Verified Access logs for the specified user.
You can optionally choose the most recent allow _or_ deny decision
specifically.

Finally, the trust context, authorization decision, endpoint policy, and group
policy are all displayed on the next screen.

###### To open the policy assistant and specify your resources

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access instances**, then click
   the **Verified Access instance ID** for the instance you want to work
   with.
3. Choose **Launch policy assistant**.
4. For **User email address**, enter the email address of the user.
5. For **Verified Access endpoint**, select the endpoint that you want to edit
   and test policies for.
6. (Optional) For **Name**, provide the name of the user.
7. (Optional) Under **Device identifier**, provide the unique
   device identifier.
8. (Optional) For **Authorization result**, choose the type of recent
   authorization result you want to use. By default, the latest authorization result will
   be used.
9. Choose **Next**.

## Step 2: Test and edit policies

On this page you will be presented with the following information to work with:

- The trust context sent by your trust provider for the user and (optionally) the device
  that you specified in the previous step.
- The Cedar policy for the Verified Access endpoint specified in the previous step.
- The Cedar policy for the Verified Access group that the endpoint belongs to.

The Cedar policies for the Verified Access endpoint and group can be edited on this page, but the
trust context is static. You can now use this page to view the trust context along side the Cedar
policies.

Test the polices against the trust context by choosing the **Test
policies** button, and the authorization result will be displayed on the screen.
You can make edits to the policies and retest your changes, repeating the process as
needed.

After you are satisfied with the changes made to the policies, choose
**Next** to continue to the next screen of the policy assistant.

## Step 3: Review and apply changes

On the final page of the policy assistant, you will see the changes you made to the
policies highlighted for easy review. You can now review them a final time and choose
**Apply changes** to commit the changes.

You also have the option of going back to the previous page by choosing
**Previous**, or cancelling out of the policy assistant completely by
choosing **Cancel**.
