# Configuring user settings for Amazon WorkSpaces Secure Browser

On the **Step 3: Select user settings** page, complete the following steps
to choose which features your users can access from the top navigation bar during their session,
and then choose **Next**:

1. Under **Branding customization**, you can customize the sign-in and loading screens that appear to your end users by modifying visual elements, text content, and terms of service. For more information, see [Branding customization in Amazon WorkSpaces Secure Browser](branding-customization.md "branding-customization.md"). **This is optional.**
2. Under **Permissions**, choose whether to enable the extension for single
   sign-on. For more information, see [Managing the single sign-on extension in Amazon WorkSpaces Secure Browser](allow-extension.md "allow-extension.md").
3. For **Allow users to print to a local device from their web
   portal**, choose **Allowed** or **Not
   allowed**.
4. For **Allow users to deeplink to their web portal**, choose
   **Allowed** or **Not Allowed**. For more information
   about deep links, see [Deep links in Amazon WorkSpaces Secure Browser](deep-links.md "deep-links.md").
5. For **Allow users to use local authentication in their portal session**, choose
   **Allowed** or **Not Allowed**. For more information
   about web authentication, see [Enabling WebAuthn redirection support in Amazon WorkSpaces Secure Browser](web-authentication.md "web-authentication.md").
6. Under **Toolbar controls**, choose the settings that you want under
   **Features**.
7. Under **Settings**, manage the toolbar presentation view at start of the
   session including toolbar state (docked or detached), theme (dark or light mode), icon
   visibility, and maximum display resolution for the session. Leave these settings
   unconfigured to grant end users full control over these options. For more information,
   see [Managing toolbar controls in Amazon WorkSpaces Secure Browser](toolbar-controls.md "toolbar-controls.md").
8. For **Session timeouts**, specify the following:
   - For **Disconnect timeout in minutes**, choose the amount of time that
     a streaming session remains active after users disconnect. If users try to reconnect to the
     streaming session after a disconnection or network interruption within this time interval,
     they are connected to their previous session. Otherwise, they are connected to a new session
     with a new streaming instance.

   If a user ends the session, the disconnect timeout does not apply. Instead, the user is
   prompted to save any open documents, and then is immediately disconnected from the streaming
   instance. The instance the user was using is then terminated.
   - For **Idle disconnect timeout in minutes**, choose the amount of time
     that users can be idle (inactive) before they are disconnected from their streaming session
     and the **Disconnect timeout in minutes** time interval begins. Users are
     notified before they are disconnected due to inactivity. If they try to reconnect to the
     streaming session before the time interval specified in **Disconnect timeout in
     minutes** has elapsed, they are connected to their previous session. Otherwise,
     they are connected to a new session with a new streaming instance. Setting this value to 0
     disables it. When this value is disabled, users are not disconnected due to
     inactivity.

   ###### Note

   Users are considered idle when they stop providing keyboard or mouse input during
   their streaming session. File uploads and downloads, audio in, audio out, and pixels
   changing do not qualify as user activity. If users continue to be idle after the time
   interval in **Idle disconnect timeout in minutes** elapses, they are
   disconnected.
