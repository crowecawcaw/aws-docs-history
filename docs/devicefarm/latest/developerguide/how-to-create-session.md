# Creating a remote access session in AWS Device Farm

For information about remote access sessions, see [Sessions](sessions.md "sessions.md").

- [Prerequisites](#how-to-create-session-prerequisites "#how-to-create-session-prerequisites")
- [Create a test run (console)](#how-to-create-session-console "#how-to-create-session-console")
- [Next steps](#how-to-create-session-next-steps "#how-to-create-session-next-steps")

## Prerequisites

- Create a project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md"), and
  then return to this page.

## Create a session with the Device Farm console

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose
   **Projects**.
3. If you already have a project, choose it from the list. Otherwise, create a project by following the
   instructions in [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md").
4. On the **Remote access** tab, choose **Start a new
   session**.
5. Choose a device for your session. You can choose from the list of available devices or search for a
   device using the search bar at the top of the list. You can search by:
   - Name
   - Platform
   - Form factor
   - Fleet type

6. In **Session name**, enter a name for the session.
7. Choose **Confirm and start session**.

## Next steps

Device Farm starts the session as soon as the requested device is available, typically within a few minutes. The
**Device Requested** dialog box appears until the session starts. To cancel the session
request, choose **Cancel request**.

After a session starts, if you should close the browser or browser tab without stopping the session or if
the connection between the browser and the internet is lost, the session remains active for five minutes.
After that, Device Farm ends the session. Your account is charged for the idle time.

After the session starts, you can interact with the device in the web browser.
