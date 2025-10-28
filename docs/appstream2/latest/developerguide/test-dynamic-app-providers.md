# Test Dynamic App Providers

(Optional)

After you enable your dynamic app provider on an image builder, you can test
the provider to verify that it functions as expected. To do so, perform the
following steps before you finish creating the image.

###### To test dynamic app providers

1. Do one of the following:
   - If you are already connected to the image builder on which you
     enabled dynamic app providers and you are logged on as**Administrator,** you must switch to an account that
     does not have local administrator permissions on the image
     builder. To do so, in the upper right corner of the image
     builder session toolbar, choose **Admin
     Commands**, **Switch User**.

   ![Admin Commands dropdown menu with Switch User option highlighted.](images/admin-commands-switch-user.png)
   - If you are not already connected to the image builder, connect
     by either [using the
     AppStream 2.0 console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only) or [creating a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or AppStream 2.0 client
     connections).

   ###### Note

   When you are prompted to sign in, choose
   **Directory User**, and sign in with a
   domain account that does not have local administrator
   permissions on the image builder.

2. On the image builder desktop, open Image Assistant, if it is not
   already open.
3. On the **Test Apps** page, if you specified any
   applications in the image that are not from the dynamic app provider,
   they display first in the list. It may take a few moments for
   applications from dynamic app providers to appear in the list.
4. Choose an application from the list and open it to verify that it
   functions as expected.
5. After you finish testing, in the lower right corner of the
   **Test Apps** page, choose **Switch
   user**.
6. Choose **Administrator**, and log back into the image
   builder.
7. Follow the necessary steps in Image Assistant to finish creating your
   image. For information about how to create an image, see [Tutorial: Create a Custom AppStream 2.0 Image by Using the
   AppStream 2.0 Console](tutorial-image-builder.md "tutorial-image-builder.md").

AppStream 2.0 automatically optimizes the agents that are specified in the
**Agents.json** configuration file.
