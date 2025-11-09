# Specify a Default Display

Language

There are two ways to specify the default display language for your users’ streaming
sessions. Use the WorkSpaces Applications default application and Windows settings feature, or configure
your image builder while signed in with an account that has local administrator
permissions. The procedure in this section describes how to specify a default display
language by using the WorkSpaces Applications default application and Windows settings feature.

###### Note

Changing the display language in Windows also automatically changes the user
locale and input method to match the language and region of the display language. If
you want all three settings to match, you do not need to separately change the user
locale or input method.

1.  Connect to the image builder that you want to use and sign in with the
    **Template User** account. To do so, do either of the
    following:

        * [Use the WorkSpaces Applications
         console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
        * [Create a
         streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client connections)


        ###### Note

        If the image builder that you want to connect to is joined to an
         Active Directory domain and your organization requires smart card
         sign in, you must create a streaming URL and use the WorkSpaces Applications client
         for the connection. For information about smart card sign in, see
         [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

    **Template User** lets you create default application and
    Windows settings for your users. For more information, see "Creating Default
    Application and Windows Settings for Your WorkSpaces Applications Users" in [Default Application and Windows Settings and Application Launch Performance in Amazon WorkSpaces Applications](customizing-appstream-images.md "customizing-appstream-images.md").

2.  On the image builder desktop, choose the Windows **Start**
    button, and choose **Control Panel**.
3.  Choose **Clock, Language, and Region**, then
    **Language**, **Add a language**.
4.  Choose a language, and choose **Add**.

###### Note

Currently, WorkSpaces Applications supports only **English (United
States)** and **Japanese**. 5. The language that you selected appears in the list of languages you added to
Windows. Choose the language that you just added. Then choose **Move
up** until the language appears at the top of the language
list. 6. Choose **Advanced Settings**. Under **Override for
Windows display language**, choose your language from the
list. 7. If you want to use the input method associated with the language that you
added, under **Override for default input method**, choose the
input method for the language. 8. Choose **Save**. When prompted to log off, choose
**Log off now**. 9. When prompted, log in again to the image builder as **Template
User**. Confirm that Windows is using the display language that you
selected. 10. In the upper right area of the image builder desktop, choose **Admin
Commands**, **Switch User**.

![Admin Commands dropdown menu with Switch User option highlighted.](images/admin-commands-switch-user.png) 11. When prompted, log in as **Administrator**. 12. If required, configure additional default regional or language settings.
Otherwise, on the image builder desktop, open Image Assistant and install and
configure applications for streaming. 13. In Step 2 of the Image Assistant process, choose **Save
settings**. 14. Follow the necessary steps in Image Assistant to finish creating your image.
For information about how to create an image, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the
WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md"). 15. Do one of the following:

    * Create a new fleet and choose your new image for the fleet. For
     information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md").
    * Update an existing fleet to use the new image.

16. Associate your fleet with the stack that is assigned to the users for whom you
    are configuring the default settings.

The default display language and associated user locale and input method
settings that you configured are applied to the fleet instances and user
streaming sessions that are launched from those instances.

Alternatively, you can configure a default display language while logged in to
the image builder as **Administrator**. If you chose different
display languages while you were logged in under the **Template
User** and **Administrator** accounts and you
chose **Save settings** in Step 2 of the Image Assistant
process, the **Template User** settings take precedence.

###### Note

Your users can change their user locale and input method from the default settings
that you configured. They can change to any one of 11 different supported locales
and nine different supported input methods. To do so, they can configure their
regional settings during application streaming sessions, as described in [Enable Your WorkSpaces Applications Users to Configure Their Regional
Settings](regional-settings.md "regional-settings.md"). Also, if a user
previously selected a user locale or input method when streaming from any fleet
instance in the same Region, those user-specified settings automatically override
any default user locale and input method that you specify through your image
builder.
