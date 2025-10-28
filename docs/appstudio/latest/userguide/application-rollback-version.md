# Rolling back to a previously published version

Use the following procedure to roll back the Production environment of your App Studio app to a previously published version. Your application end users
will be impacted and see the rolled back version of your app after it is deployed. When you roll back an application, it also rolls back the component code to the version
from the previous publish time and affects the entire app deployment stack (user code, component configuration state). This means that any updates that App Studio made
to component code, such as field or other config changes, will be rolled back to ensure the rolled-back application version operates as it did when it was
originally published.

The in-progress version of your application in the Development environment is not affected when you roll back the published version.

Rolling back the published version of an application is helpful if you detect issues with a published app and need to immediately publish a previously working version,
or you want to publish a previous version and preserve the latest updates to the app in the Development environment.

###### Note

If you want to revert the Development environment of an app to a previously published version, you should revert the application. For more information,
see [Edit a previously published app version](applications-edit-previously-published-version.md "applications-edit-previously-published-version.md").

###### To roll back the Production environment version to a previously published app version

1. If necessary, navigate to the Development environment of your application by editing it. For more information, see
   [Editing or building an application](applications-edit.md "applications-edit.md").
2. Choose the version dropdown arrow at the top of the **Production** environment tile to see the available versions for rolling back. The
   dropdown contains versions published within the last 30 days. If this dropdown is disabled, it may be because an
   app publish is already in progress, and only one publish can happen at the same time.
3. Choose the version you want to roll back to.
4. Enter a reason for rolling back, and choose **Roll back**. The rollback publish will start and once completed, the
   Production environment of your application will be update to the chosen version.

###### Note

You can also roll forward to a previously published app version after you've rolled back.
