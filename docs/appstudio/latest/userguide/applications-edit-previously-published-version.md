# Edit a previously published app version

Use the following procedure to edit a previously published version of your App Studio application. After you choose to edit
the previously published version, you can edit the app in the Development environment, or publish it to Testing and
then Production.

###### Warning

The previously published version replaces the in-progress version
of the app in the Development environment. Any unpublished changes to your app will be lost.

Editing a previously published version is useful
in the case that you accidentally publish unwanted changes or changes that break the application for your users, and you want to further build or edit from
the previous app version.

###### Note

If you detect issues with a published app and need to immediately publish a previously working version, or you want to publish a
previous version but preserve the latest updates to the app in the Development environment, you should rollback the app instead. For more information,
see [Rolling back to a previously published version](application-rollback-version.md "application-rollback-version.md").

###### To edit a previously published app version

1. If necessary, navigate to the applicaiton studio of your application.
2. Choose the dropdown arrow next to the **Publish** button, and then choose **Publish Center**.
3. Choose **Version history** to see the list of previously published versions of the application.
4. Find the version you want to edit, and choose **Edit**.
5. Review the information, and choose **Revert**.
6. The version you chose to edit is now the current version in the Development environment. You can make changes to it, or publish it to the Testing
   environment as is by choosing **Publish**. Once published to Testing, you can publish again to the Production environment if desired.
