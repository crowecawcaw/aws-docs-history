# Enable Google Drive for Your WorkSpaces Applications

Users

Before enabling Google Drive, you must do the following:

- Have an active Google Workspace account with a valid organizational domain
  and users in the domain to use with WorkSpaces Applications.
- Configure an WorkSpaces Applications stack with an associated fleet.

The fleet must use an image that uses a version of the WorkSpaces Applications agent
released on or after May 31, 2018. For more information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md "agent-software-versions.md"). The fleet must also have access to
the internet.

- Add Amazon WorkSpaces Applications as a trusted app in one or more domains associated with
  your Google Workspace account. You can enable Google Drive for up to 10
  domains.
- Have a Windows-based stack. (Linux-based stacks are not supported).
  Follow these steps to add Amazon WorkSpaces Applications as a trusted app in your Google Workspace
  domains.

###### To add Amazon WorkSpaces Applications as a trusted app in your Google Workspace domains

1. Sign in to the Google Workspace Admin console at [https://admin.google.com/](https://admin.google.com/ "https://admin.google.com/").
2. In the left navigation sidebar, choose **Security**,
   **Access and data control**, **API controls**.
3. At the top of the page, in the **App access control**
   section, choose **MANAGE THIRD-PARTY APP ACCESS**.
4. Choose **Add app**, and then choose
   **OAuth App Name Or Client ID**.
5. Enter the Amazon WorkSpaces Applications OAuth client ID for your AWS Region, and then
   choose **SEARCH**. For a list of client IDs, see the table
   that follows this procedure.
6. In the search results, choose Amazon WorkSpaces Applications, and then choose
   **Select**.
7. In the **Client ID** page, under **OAuth Client
   ID**, verify that the correct ID appears in the list, and then
   select the check box to the left of the ID.
8. On the lower right of the page, choose **SELECT**.
9. Configure which organizational units in your Google Workspace organization
   should gain access.
10. Under **Access to Google Data**, choose **Trusted: Can
    access all Google services**, and then choose
    **CONTINUE**.
11. Review that the selections made are correct, then when you are satisfied,
    choose **FINISH**.
12. Verify that the Amazon WorkSpaces Applications app, with the correct OAuth ID, appears in the
    list of connected apps.

| Amazon WorkSpaces Applications OAuth2 client IDs | Region                                                                                                                                                                                                                                                                                                                                                                                      | Amazon WorkSpaces Applications OAuth client ID |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| US East (N. Virginia)                            | `266080779488-15n5q5nkiclp6m524qibnmhmbsg0hk92.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| US East (Ohio)                                   | `723951369598-6tvdlf52g2qh0qa141o4k1avasvnj51i.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| US West (Oregon)                                 | `1026466167591-i4jmemrggsjomp9tnkkcs5tniggfiujb.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                 |
| Asia Pacific (Mumbai)                            | `325827353178-coqs1c374mf388ctllrlls374dc1bmb2.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Asia Pacific (Seoul)                             | `562383781419-am1i2dnvt050tmdltsvr36i8l2js40dj.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Asia Pacific (Singapore)                         | `856871139998-4eia2n1db5j6gtv4c1rdte1fh1gec8vs.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Asia Pacific (Sydney)                            | `151535156524-b889372osskprm4dt1clpm53mo3m9omp.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Asia Pacific (Tokyo)                             | `922579247628-qpl9kpihg3hu5dul2lphbjs4qbg6mjm2.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Canada (Central)                                 | `872792838542-t39aqh72jv895c89thtk6v83sl6jugm2.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Europe (Frankfurt)                               | `643727794574-1se5360a77i84je9j3ap12obov1ib76q.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Europe (Ireland)                                 | `599492309098-098muc7ofjfo9vua5rm5u9q2k3mlok3j.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| Europe (London)                                  | `682555519925-usbn2sk1ffgo8odgf23nj66ri71na0k5.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |
| AWS GovCloud (US-East)                           | `20306576244-gqqkappmhhv9fj06sdk7as60he89e7ce.apps.googleusercontent.com`<br>NoteFor more information about using WorkSpaces Applications in<br>the AWS GovCloud (US) Regions, see [Amazon WorkSpaces Applications](../../../govcloud-us/latest/UserGuide/govcloud-appstream2.md "../../../govcloud-us/latest/UserGuide/govcloud-appstream2.md") in the _AWS GovCloud (US) User<br>Guide_.  |
| AWS GovCloud (US-West)                           | `996065833880-litfkb2vfd7c65nt7s24r7t8le5bc9bl.apps.googleusercontent.com`<br>NoteFor more information about using WorkSpaces Applications in<br>the AWS GovCloud (US) Regions, see [Amazon WorkSpaces Applications](../../../govcloud-us/latest/UserGuide/govcloud-appstream2.md "../../../govcloud-us/latest/UserGuide/govcloud-appstream2.md") in the _AWS GovCloud (US) User<br>Guide_. |
| South America (São Paulo)                        | `891888628791-1ltbtedva29esqvqadiatlj4htcgcjfo.apps.googleusercontent.com`                                                                                                                                                                                                                                                                                                                  |

Follow these steps to enable Google Drive for your WorkSpaces Applications users.

###### To enable Google Drive while creating a stack

- Follow the steps in [Create a Stack in Amazon WorkSpaces Applications](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md"), make sure that
  **Enable Google Drive** is selected, and that you have
  specified at least one organizational domain associated with your Google
  Workspace account.

###### To enable Google Drive for an existing stack

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and
   select the stack for which to enable Google Drive.
3. Below the stacks list, choose **Storage** and select
   **Enable Google Drive for Google Workspace**.
4. In the **Enable Google Drive for Google Workspace**
   dialog box, in **Google Workspace domain name**, type the
   name of at least one organizational domain that is associated with your
   Google Workspace account. To specify another domain, choose **Add
   another domain**, and type the name of the domain.
5. After you add domain names, choose **Enable**.

###### Note

For guidance that you can provide your users to help them get started with
using Google Drive during WorkSpaces Applications streaming sessions, see [Use Google Drive](google-drive-end-user.md "google-drive-end-user.md").
