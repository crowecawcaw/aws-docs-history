# Session Context in Amazon WorkSpaces Applications

You can pass parameters to your streaming application by using either of the following
methods:

- Specify session content in the CreateStreamingURL WorkSpaces Applications API operation. For
  more information, see [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md").
- Add the sts:TagSession permission to your IAM role's trust policy and specify
  the session context as a SAML assertion in your SAML 2.0 identity provider's
  authentication response. For more information, see [Step 5: Create
  Assertions for the SAML Authentication Response](external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions "external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions") and [Step 5: Create
  Assertions for the SAML Authentication Response](external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions "external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions").
  If your image uses a version of the WorkSpaces Applications agent that was released on or after October
  30, 2018, the session context is stored within the image as a Windows or Linux
  environment variable. For information about specific environment variables, see "User
  and Instance Metadata for WorkSpaces Applications Fleets" in [Customize an Amazon WorkSpaces Applications Fleet to Optimize Your Users'
  Application Streaming Experience](customize-fleets.md "customize-fleets.md") .

###### Note

The session context parameter is visible to the user in the WorkSpaces Applications streaming URL.
We strongly recommend that you never put confidential or sensitive information in
the session context parameter. Because it is possible for users to modify the
streaming URL, we recommend performing additional validation to determine that the
session context is valid for the end user. For example, you can compare the session
context with other session information, such as user and instance metadata for
WorkSpaces Applications fleets.

WorkSpaces Applications does not perform validation on the session context parameter.

## Using Session Context to Pass

Parameters to a Streaming Application

In the following steps, you'll use session context to start a web browser and
automatically open a specific website. For instances running Windows, you'll use
Firefox. For instances running Linux, you'll use Chromium.

###### To use session context to launch a website

1. In the left navigation pane, choose **Images**,
   **Image Builder**.
2. Choose the image builder to use, verify that it is in the
   **Running** state, and choose
   **Connect**.
3. Log in to the image builder by choosing **Administrator**
   on the **Local User** tab.
4. Create a child folder of `C:\`. For this example, use
   `C:\Scripts`.
5. Create a Windows batch file in the new folder. For this example, create
   `C:\Scripts\session-context-test.bat` and add a
   script that launches Firefox with the URL from the session context.

Use the following script:

```
CD "C:\Program Files (x86)\Mozilla Firefox"
Start firefox.exe %APPSTREAM_SESSION_CONTEXT%
```

6. In Image Assistant, add `session-context-test.bat` and
   change the name to `Firefox`.

You do not need to add Firefox. This step requires that you add only the
batch file. 7. Create an image, fleet, and stack. For this example, use a fleet name of
`session-context-test-fleet` and a stack name of
`session-context-test-stack`. 8. After the fleet is running, you can call [create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") with the `session-context`
parameter, as shown in this example.

```
`aws appstream create-streaming-url --stack-name `session-context-test-stack` \
--fleet-name `session-context-test-fleet` \
--user-id `username` –-validity 10000 \
--application-id `firefox` --session-context "`www.amazon.com`"`
```

9. Open the streaming URL in a browser. The script file launches Firefox and
   loads `http://www.amazon.com`.

Similarly, you can perform the following steps to pass parameters to your Linux
streaming application.

###### To pass parameters to your Linux streaming application

1. In the left navigation pane, choose **Images**,
   **Image Builder**.
2. Choose the image builder to use, verify that it is in the
   **Running** state, and choose
   **Connect**.
3. Log in to the image builder by default as
   **ImageBuilderAdmin**.
4. Create a script file (for example, launch-chromium.sh) by running the
   following command:

**sudo vim /usr/bin/launch-chromium.sh** 5. Write the script and set executable permissions, such as the
following:

###### Note

#!/bin/bash and source /etc/profile are always required in the
script.

```
#!/bin/bash
source /etc/profile
/usr/bin/chromium-browser $APPSTREAM_SESSION_CONTEXT
```

6. Use the Image Assistant CLI to add launch-chromium.sh:

```
sudo AppStreamImageAssistant add-application \
--name `chromium` \
--absolute-app-path `/usr/bin/launch-chromium.sh`
```

7. Create an image, fleet, and stack. For this example, use a fleet name of
   `session-context-test-fleet` and a stack name of
   `session-context-test-stack`.
8. After the fleet is running, you can call [create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") with the `session-context`
   parameter, as shown in this example.

```
`aws appstream create-streaming-url --stack-name `session-context-test-stack` \
--fleet-name `session-context-test-fleet` \
--user-id `username` \
--application-id `chromium` --session-context "`www.amazon.com`"`
```

9. Open the streaming URL in a browser. The batch file launches Chromium and
   loads `http://www.amazon.com`.
