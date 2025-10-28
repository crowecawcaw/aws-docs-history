# Share an Amazon Bedrock chat agent app

A snapshot of an Amazon Bedrock in SageMaker Unified Studio chat agent app is a point-in-time capture of the app's
state, including its code, configuration, and any associated data.

You can share a snapshot with all members of your Amazon SageMaker Unified Studio domain, or with
specific users or groups in your Amazon SageMaker Unified Studio domain. When you first share a snapshot,
you get a share link to the snapshot that you can send to users. If you share the snapshot
with all users, Amazon SageMaker Unified Studio grants permission to a user, when they first open the
share link. Amazon SageMaker Unified Studio also adds the snapshot to the user's shared assets list. If
you share the snapshot with specific users and groups, the snapshot is immediately available
in their shared assets list. They can also use the share link to access the snapshot. By
default, sharing a snapshot is restricted to only those users or groups that you select.

When you share a chat agent app, Amazon SageMaker Unified Studio also publishes the chat agent app to the Amazon SageMaker AI Catalog.

When sharing occurs, Amazon Bedrock [deploys](app-deploy.md "app-deploy.md") the snapshot of
the chat agent app. When you first share a snapshot, Amazon Bedrock creates a new alias for the chat agent app and a new
version of the chat agent app that represents the snapshot. On subsequent shares, Amazon Bedrock creates a
new version of the app, and associates the alias with the new version. If necessary, You can
change the version that is associated with an alias. For more information, see [Modify the version of an Amazon Bedrock chat agent app](app-change-alias-version.md "app-change-alias-version.md") .

###### To share a chat agent app snapshot

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. Open the chat agent app that you want to share.
7. Choose **Share**.
8. In **App description** enter a short description for the chat agent app.
   Make sure that that the description lets users understand the purpose of the
   chat agent app.
9. Do one of the following:
   - If you want to share the chat agent app snapshot with all members of your
     Amazon SageMaker Unified Studio domain, select turn on **Grant access with
     link**.
   - If you want to share the chat agent app snapshot with specific Amazon SageMaker Unified Studio
     domain users or groups, do the following in **Share with specific
     users or groups**:
     1. For **Member type** choose **Individual
        user** or **Group**, depending on the
        type of member that you want share the chat agent app with.
     2. Search for the users or groups that you want to share the chat agent app with
        by entering the user name or group in the **Search by alias
        to invite members** text box.
     3. In the drop down list, select the matching user name or group that
        want to share the chat agent app with.
     4. Choose **Add** to add the user or group.

10. Choose **Share** to share the chat agent app.
11. When the success message appears, choose **Copy link** and send
    the link to the users that you are sharing the chat agent app snapshot with. If **Grant
    access with link** is off, the link only works for users that you have
    explicitly granted access to the chat agent app.
    As the chat agent app creator, you, and other members of the chat agent app project, can make changes to the chat agent app
    and share a fresh snapshot of the chat agent app. Only the latest snapshot is available to users. Users
    that you share a snapshot to can't make any changes to the snapshot.

To change who you share the chat agent app with, open the chat agent app, choose **Share** and
make your changes. Choose **Done** to complete the changes. If you are
sharing the snapshot with all users, turning off **Grant access with link**
restricts access to users that you have specifically share the snapshot with.

You can't stop sharing a snapshot without deleting the chat agent app. If you delete the chat agent app, the
snapshot is no longer shared and is removed from the Amazon SageMaker AI Catalog. If you want to deny
access to everyone, without deleting the chat agent app, edit the snapshot and remove all users and
groups. If you shared the snapshot with all users, turn off **Grant access with
link**. Note that Amazon SageMaker Unified Studio doesn't remove the snapshot from the
Amazon SageMaker AI Catalog.

If you need the share link later, share the chat agent app again and copy the share link. You can
also change the users that you share with the chat agent app with.

To see which chat agent apps you have shared, Open the app project, choose **Asset
gallery** and then **My apps**. Check the **Share
status** column for the chat agent app.
