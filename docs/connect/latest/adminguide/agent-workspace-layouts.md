

# Choose a layout for the agent workspace
<a name="agent-workspace-layouts"></a>

A layout controls how components and applications are arranged on the agent workspace. Amazon Connect Customer provides two layouts: Classic, which matches the original layout of the agent workspace, and Modern, which optimizes screen space for different channels.

You can set a different layout for each workspace, and assign a workspace to different agents. If you do not choose a layout or assign a workspace to an agent, they will continue to see the original layout of the agent workspace. For more information, see [Assign an agent workspace layout to agents](assign-agent-workspace-layout.md).

## Classic layout
<a name="agent-workspace-layouts-classic"></a>

The Classic layout matches the original layout of the agent workspace. The contact list, contact controls, and applications look and behave similarly to how they do in the original layout.

![The Classic layout of the agent workspace during a chat.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-classic-unlabeled.png)


The Classic layout has five components, numbered in the following image:

1. The **header bar**, where agents change their status, update their settings, and sign out.

1. The **contact list**, which lists an agent's active contacts.

1. The **contact controls**, which agents use to handle calls, chats, emails, and tasks.

1. **Application tabs**, which hold first-party applications such as Cases and Customer Profiles, and third-party applications.

1. **Agent assist**, which provides proactive, real-time recommendations.

![The Classic layout of the agent workspace, with five numbered callouts.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-classic.png)


The Classic layout differs from the original layout of the agent workspace in four ways:
+ The status toggle, device settings, and sign-out button are located in the header bar, not above the contact list. For more information, see [Access settings in the Classic and Modern layouts](#agent-workspace-layouts-settings).
+ The contact controls are wider for chat and email contacts by default.
+ The contact controls keep their width when an agent switches between contacts on different channels.
+ Agents can resize agent assist.

## Modern layout
<a name="agent-workspace-layouts-modern"></a>

The Modern layout offers a different placement of components and applications in order to optimize screen space for agents handling contacts of different channels.

![The Modern layout of the agent workspace during a chat.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern-unlabeled.png)


The Modern layout has six components, numbered in the following image:

1. The **header bar**, where agents change their status, update their settings, and sign out.

1. The **contact list**, which lists an agent's active contacts.

1. The **contact control bar**, which holds the primary contact controls.

1. The **contact controls**, which include controls specific to each channel, including video calls, chats, emails, and tasks.

1. **Application tabs**, which hold first-party applications such as Cases and Customer Profiles, and third-party applications.

1. **Agent assist**, which provides proactive, real-time recommendations.

![The Modern layout of the agent workspace during a chat, with six numbered callouts.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern.png)


### Voice calls
<a name="agent-workspace-layouts-modern-voice"></a>

During a voice call, the contact control bar contains all the voice call controls, including **Mute**, **Hold**, **Transfer**, and **End call**. Agents have the full area beneath the contact control bar to use applications and agent assist. Contact controls appear for a voice call only during after contact work, when a transcript is available, and when video calling is enabled.

![The Modern layout during a voice call, with call actions in the contact control bar.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern-voice.png)


When an agent transfers a call, the list of participants and their controls opens from the contact control bar.

![The Modern layout during a transfer, with the participants list open below the contact control bar.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern-transfer.png)


### Chats, emails, and tasks
<a name="agent-workspace-layouts-modern-text"></a>

During a chat, email, or task, the contact controls appear to the left of the applications. Compared to the Classic layout, agents have a taller, wider area to read and respond.

![The Modern layout during an email, with the email reply open at full height beside applications.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern-email.png)


### Two or more contacts
<a name="agent-workspace-layouts-modern-contact-list"></a>

The contact list appears only when an agent has two or more active contacts. The contact list collapses to a list of icons, one for each contact, and with an icon specific to its channel. Agents can expand the contact list to see the contact names, and for chat contacts, a preview of the most recent message.

![The Modern layout with the contact list expanded, showing a chat and an email.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern-contact-list.png)


![The Modern layout with the contact list collapsed to icons, and a preview of a chat contact open beside its icon.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern-contact-list-collapsed.png)


### Collapsible components
<a name="agent-workspace-layouts-modern-panels"></a>

Agents can expand, collapse, and resize the contact list, the contact controls, and agent assist.

### No active contacts
<a name="agent-workspace-layouts-modern-no-contacts"></a>

When an agent has no active contacts, the contact control bar shows a welcome message. Agents can use applications without an active contact, or they can start a new contact with the buttons at the top right.

![The Modern layout with no active contacts, showing a welcome message and buttons to start a new contact.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-modern-no-contacts.png)


## Access settings in the Classic and Modern layouts
<a name="agent-workspace-layouts-settings"></a>

In both layouts, agents can open the drop-down menu in the header bar to change their language, their choice of light or dark mode, and sign out.

![The User settings menu open from the header bar, with Language, Theme mode, Device settings, Download logs, and Sign out.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-user-settings.png)


Choosing **Device settings** opens a dialog where agents can update their camera, speaker, microphone, ringer, and other device settings.

![The Device settings dialog, with video and audio device options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/agent-workspace-layout-device-settings.png)


## Preview a layout
<a name="agent-workspace-layouts-preview"></a>

Both layouts are AWS-managed views. To preview a layout before you assign it, go to **UI Management** > **Views**, then open **Agent Workspace - Classic** or **Agent Workspace - Modern** in the UI builder.