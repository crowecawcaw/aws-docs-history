

# Sessions
<a name="sessions"></a>

Sessions displays all virtual desktops created within Research and Engineering Studio. From the Sessions page, you can filter and view session information or create a new session.

![Sessions page of admin console with numbered annotations showing functionality](http://docs.aws.amazon.com/res/latest/ug/images/res-sessions.jpg)


1. Use the menu to filter results by sessions created or updated within a specified time frame.

1. Select a session and use the Actions menu to:

   1. Resume Session(s)

   1.  Stop/Hibernate Session(s)

   1. Force Stop/Hibernate Session(s)

   1. Reboot Session(s) – Restarts selected sessions. This action is also available for sessions in ERROR state, allowing administrators to recover errored VDIs.

   1. Terminate Session(s)

   1. Force Terminate Session(s)

   1. Session(s) Health

   1. Create Software Stack

1.  Choose **Create Session** to create a new session.

1. Search for a session by name and filter by state and operating system.

1. Select the **Session Name** to view more details.

## Create a session
<a name="create-session"></a>

1. Choose **Create Session**. The Launch New Virtual Desktop modal opens. 

1. Enter details for the new session.

1. (Optional.) Turn on **Show Advanced Options** to provide additional details such as subnet ID and DCV session type. 
**Virtual session type deprecated**  
Starting with the 2026.06 release, the *Virtual* session type is no longer supported. All sessions now use the *Console* session type. If your configuration or automation specifies the Virtual session type, update it to use Console.

1. Choose **Submit**.   
![Details of admin console page with fields to be filled out to launch a new virtual desktop](http://docs.aws.amazon.com/res/latest/ug/images/res-createsession.jpg)

## Session details
<a name="session-details"></a>

From the **Sessions** list, select the ** Session Name** to view session details. 

![Admin console page with view of session details](http://docs.aws.amazon.com/res/latest/ug/images/res-viewsessiondetails.png)
