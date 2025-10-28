# How applications are

loaded in Amazon Connect Agent Workspace

In Amazon Connect Agent Workspace, the agent workspace allows users to handle multiple contacts
concurrently. They will have only one contact selected at a time though, and the
workspace will update the experience based on the channel (call, chat, or task) of the
contact and the applications opened for that contact. When a user switches to another
contact, the set of application tabs are updated to what the user was doing last when
they were on the previous contact.

![Applications that have been onboarded will appear in the Agent applications menu.](images/integrating-with-agent-workspace-how-apps-load.png)
An application can be opened by the user selecting the app launcher icon in the top
right hand corner of the main workspace and select an application from the list. This
will load your app in a new application tab for the contact the user has active at that
time, or the idle state if the user doesn’t have any active contacts. There will be new
iframe created for each contact an application is opened with. That iframe will exist
until the application tab is closed, for example, a user clicking on the x on the tab or
the contact closing. At which point, the app will go through the destroy lifecycle
process which gives apps a chance to clean up any resources before the iframe is
unmounted from the DOM. The iframe will be hidden when a user selects another tab on the
same contact or switches to another contact. This means that at any one time there can
be multiple instances, for example, iframes, of the same application running for
different contacts.

The agent workspace has a Content Security Policy (CSP) that only allows specific
domains to be framed by setting [frame-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-src "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-src"). The domains configured in the _AccessUrl_ and
those added to _Approved Origins_ will be included in the agent
workspace’s CSP. Ensure that all domains that your app uses for top level pages are
included between _AccessUrl_ and _Approved
Origins_.

Events and data shared with an instance of an application will be for the contact the
application is opened under and the other applications opened on the same contact.
Events or data will not be shared between apps on different contacts.
