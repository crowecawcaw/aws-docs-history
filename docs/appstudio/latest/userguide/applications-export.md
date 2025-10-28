# Exporting applications

You can export a snapshot of your application to share it with other App Studio instances. When you
export an app, a snapshot is created from the Development environment of the app, and an import code is generated. The
import code can then be used to import the application into other App Studio instances, where it can be viewed and built.

Exported apps can be imported into instances in any AWS Region supported by App Studio.

###### To export an application

1. In the navigation pane, choose **My applications** in the **Build** section to navigate
   to a list of your applications.
2. Choose the dropdown in the **Actions** column of the application you want to export.
3. Choose **Export**.
4. The procedure for generating and sharing an import code varies depending on whether or not an import code has already been created for the app.
   - If an import code hasn't been created:
     1. In **Application import permissions**, specify which instances can import the exported app. You can give import permissions to all instances, or add specific App Studio instances
        by entering their instance IDs. Separate multiple instance IDs with a comma.

     To find your instance ID, navigate to your instance's account settings by choosing **Account settings** in the App Studio console. 2. Choose **Generate import code**. 3. Copy and share the generated import code.

   - If an import code has already been created:
     1. To share the currently exported app, copy and share the existing import code. To create a new exported app with the latest changes to your app, choose **Generate new code**. You can
        also update the import permissions if needed.
