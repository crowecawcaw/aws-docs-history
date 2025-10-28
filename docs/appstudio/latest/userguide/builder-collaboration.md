# Building an app with multiple users

Multiple users can work on a single App Studio app, however only one user can edit an app at one time. See the
following sections to information about inviting other users to edit an app, and the behavior when multiple users try to edit an
app at the same time.

## Invite builders to edit an app

Use the following instructions to invite other builders to edit an App Studio app.

###### To invite other builders to edit an app

1. If necessary, navigate to the application studio of your application.
2. Choose **Share**.
3. In the **Development** tab, use the text box to search for and select groups or individual
   users that you want to invite to edit the app.
4. For each user or group, choose the dropdown and select the permissions to give to that user or group.
   - **Co-owner**: Co-owners have the same permissions as app owners.
   - **Edit only**: Users with the **Edit only** role have the
     same permissions as owners and co-owners, except for the following:
     - They cannot invite other users to edit the app.
     - They cannot publish the app to the Testing or Production environments.
     - They cannot add data sources to the app.
     - They cannot delete or duplicate the app.

## Attempting to edit an app that is being edited by another user

A single App Studio app can only be edited by one user at a time. See the following example to understand what happens
when multiple users try to edit an app at the same time.

In this example, `User A` is currently editing an app, and has shared it with `User B`. `User B` then attempts to
edit the app that is being edited by `User A`.

When `User B` tries to edit the app, a dialog box will appear informing them that `User A` is currently editing the app, and that
continuing will kick `User A` out of the application studio, and all changes will be saved. `User B` can choose to cancel and let `User A`
continue, or continue and enter the application studio to edit the app. In this example, they choose to edit the app.

When `User B` chooses to edit the app, `User A` receives a notification that `User B` has started editing the app, and their
session has ended. Note that if `User A` had the app open in an inactive browser tab, they may not receive the notification. In this case, if they try to
come back to the app and try to make an edit, they will receive an error message and be guided to refresh the page, which will return them to the list of applications.
