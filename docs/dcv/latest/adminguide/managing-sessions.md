# Managing Amazon DCV sessions

Once the Amazon DCV servers are set up and all your applications are installed, your clients access them through a secured session. Managing
these sessions for your client grants them access and sets the parameters for each session.

Before your clients can connect to one, you must create a Amazon DCV session on your Amazon DCV server. Clients can only connect to a Amazon DCV server if there's an
active session.

Every Amazon DCV session has the following attributes:

- **session ID** — Used to identify a specific session on the Amazon DCV server.
- **Owner** — The Amazon DCV user who created the session. By default, only an owner can connect to the
  session.
  Amazon DCV clients need this information to connect to the session.

###### Topics

- [Understanding Amazon DCV sessions](managing-sessions-intro.md "managing-sessions-intro.md")
- [Using the Command Line Tool to Manage Sessions](managing-sessions-cli.md "managing-sessions-cli.md")
- [Starting Amazon DCV sessions](managing-sessions-start.md "managing-sessions-start.md")
- [Stopping Amazon DCV sessions](managing-sessions-lifecycle-stop.md "managing-sessions-lifecycle-stop.md")
- [Viewing Amazon DCV sessions](managing-sessions-lifecycle-view.md "managing-sessions-lifecycle-view.md")
- [Managing active Amazon DCV sessions](managing-running-session.md "managing-running-session.md")
- [Setting session time zone](managing-session-time-zone.md "managing-session-time-zone.md")
- [Managing screen blanking on Linux](managing-screen-blanking.md "managing-screen-blanking.md")
- [Taking a screenshot in a Amazon DCV Session](managing-sessions-lifecycle-screenshot.md "managing-sessions-lifecycle-screenshot.md")
