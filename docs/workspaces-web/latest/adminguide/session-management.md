# Using the session management dashboard in Amazon WorkSpaces Secure Browser

Use the session management dashboard on your WorkSpaces Secure Browser console to monitor and manage active and
complete sessions.

## Dashboard access

To access the dashboard, follow these steps.

###### To access the dashboard

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/ "https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/").
2. Choose **WorkSpaces Secure Browser**, **Web portals**, and choose your web
   portal.
3. Choose the **Session** tab or choose **View sessions** to open the dashboard in a split panel below.

## Dashboard filters

In the sessions panel, you can filter sessions by the following properties or values:

- **Status**
  - **Active** – Indicates a session is currently running. To
    terminate the session, see below.
  - **Terminated** – Indicates a session is no longer
    active.

- **Session ID**
- **Username**
- **Session start time**

## Terminate sessions

To terminate a session, follow these steps.

###### To terminate a session

1. On the sessions dashboard, select the session you want to stop.
2. Choose **Terminate**.
3. Disconnected users lose all state from the session. All open tabs, browser history, and
   files downloaded to the secure browser are recycled.

## Session history

The dashboard contains sessions from the last 35 days. You can use the CLI to list
sessions, with or without a filter. The session history is delivered as JSON, which
administrators can process, manage, and store in a separate repository.

The following are sample CLI commands for managing sessions in the US-West-2 (Oregon)
region.

To list all sessions for a web portal, run the following command:

**aws workspaces-web list-sessions --portal-arn
arn:aws:workspaces-web:us-west-2:<accountId>:portal/<portalId>**

To list all sessions for a specific user of a web portal, run the following command:

**aws workspaces-web list-sessions --portal-arn
arn:aws:workspaces-web:us-west-2:<accountId>:portal/<portalId> --username
<username>**
