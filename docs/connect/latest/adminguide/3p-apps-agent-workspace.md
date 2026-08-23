# Access third-party applications in the agent workspace

## Launch third-party applications

Agents access third-party applications in the agent workspace with the
**Apps** launcher, shown in the following image. The
launcher appears in the agent workspace after you [onboard](3p-apps.md "3p-apps.md") your third-party app.

![The Apps launcher in the agent workspace.](images/agent-workspace-apps-launcher.png)

The **Apps** launcher lists the applications that the agent
can access.

Agents can open applications when they don't have any contacts or while
handling a contact, such as a call, chat, or task. After an agent opens an app
for a contact, the app stays open until the contact closes.

## Required security profile permissions to access third-party applications

Agents need the following security profile permissions to access third-party
apps:

- **Contact Control Panel (CCP) - Access the
  CCP**
- Access to at least one third-party application: the application
  appears on the **Security profiles** page after you
  [onboard](3p-apps.md "3p-apps.md") it.

## Pin apps in the agent workspace

Agents can pin an app so that it stays open. On the app's tab, choose the more
options icon, and then choose **Pin tab**, as shown in the
following image.

![The Pin tab option on an app's tab in the agent workspace.](images/3p-apps-agent-workspace-pinned-1.png)

After an agent pins an app, the app stays open while the agent is idle and
opens automatically for incoming contacts. The app stays pinned for that user
and browser until the user clears the browser cookies.

An agent can unpin the tab at any time and then open and close the app as
needed.

The following image shows a third-party app named NoteTest pinned in the agent
workspace.

![A third-party note test app that is pinned to the agent workspace.](images/3p-apps-agent-workspace-notes-app.png)

The following image shows a third-party app named Maps pinned in the agent
workspace.

![A third-party maps app that is pinned to the agent workspace.](images/3p-apps-agent-workspace-maps-app.png)

## Important things to know

- On July 22, 2024, Google [announced](https://privacysandbox.com/news/privacy-sandbox-update/ "https://privacysandbox.com/news/privacy-sandbox-update/") that it no longer plans to deprecate third-party
  cookies. Instead, Google provides an opt-in mechanism for deprecating
  third-party cookies. Opting in might affect how third-party applications
  work. If you use third-party apps in the Connect Customer agent workspace on the
  Chrome browser, we recommend that you do one of the following:

  - **Temporary solution**: Update
    [Enterprise Chrome policies](https://support.google.com/chrome/a/answer/7679408?sjid=16745203858910744446-EU#upChromeBrsrBB117 "https://support.google.com/chrome/a/answer/7679408?sjid=16745203858910744446-EU#upChromeBrsrBB117"). Set the
    `BlockThirdPartyCookies` policy to
    `false` so that third-party cookie deprecation
    doesn't affect your agents.
  - **Permanent solution**: We
    recommend that app developers follow [best practices](https://developers.google.com/privacy-sandbox/3pcd "https://developers.google.com/privacy-sandbox/3pcd") that will continue to pass
    third-party cookies.

- You must have [integrated the
  application](3p-apps.md "3p-apps.md"), and the agent must have [access to the
  application](assign-security-profile-3p-apps.md "assign-security-profile-3p-apps.md") through a security profile. The agent must also
  have access to the CCP for the **Apps** launcher to
  appear.
