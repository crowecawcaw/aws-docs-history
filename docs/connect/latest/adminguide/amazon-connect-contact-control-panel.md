

# Provide agents with access to the Connect Customer Contact Control Panel (CCP)
<a name="amazon-connect-contact-control-panel"></a>

**Note**  
This is the URL to the CCP website:   
**https://{{instance name}}.my.connect.aws/ccp-v2/**
This is the URL to the [agent workspace](#use-agent-workspace):  
**https://{{instance name}}.my.connect.aws/agent-app-v2/**

## Steps to ensure agents can access the CCP
<a name="setup-agents-on-ccp"></a>

Agents use the Contact Control Panel (CCP) to communicate with contacts. But before agents can access the CCP and handle contacts, there are a few things you need to do: 

1. Ensure your network meets the requirements for using the CCP. For more information see [Set up your network to use the Connect Customer Contact Control Panel (CCP)](ccp-networking.md).

1. Ensure agents have the appropriate headsets and workstations. For more information see [Agent headset and workstation requirements for using the Contact Control Panel (CCP)](ccp-agent-hardware.md).

1. Create a user name and password for agents to log into the CCP, by [adding agents to your instance](user-management.md).

1. At minimum, [assign them the **Agent** security profile](assign-security-profile.md). This grants them permissions to access the CCP, which they use to manage contacts. 

1. Provide the user name, password, and the CCP website link to your agents so they can log in. 

   We recommend telling agents to bookmark the URL to the CCP so they can readily access it.

1. Train your agents on the CCP:
   + Watch [Training video: How to use the Contact Center Panel (CCP) in Connect Customer](ccp-video-training.md)

## Agent workspace: Everything in one place
<a name="use-agent-workspace"></a>

Want your agents to handle contacts and access customer profiles, cases, and knowledge all in one place? Use the [agent workspace](agent-user-guide.md)\! 

The *agent workspace* is a single web browser interface that hosts the CCP, [Customer Profiles](ag-cp-select.md), [Cases](search-cases.md), and [agent assist](search-for-answers.md).

If you're using the CCP that is provided with Connect Customer, after you enable Customer Profiles, Cases, or agent assist, share the following URL with your agents so they can access it in the agent workspace:
+ **https://{{instance name}}.my.connect.aws/agent-app-v2/**

For help finding your instance name, see [Find your Connect Customer instance name](find-instance-name.md).

## Grant microphone access in Chrome, Firefox, or Edge
<a name="accessing-microphone"></a>

If agents experience problems with their microphone, they might need to grant microphone access in their browser. Choose one of the following articles to get the steps appropriate for your browser:
+ [Use your camera and microphone in Chrome](https://support.google.com/chrome/answer/2693767?hl=en)
+ [Firefox Page Info window](https://support.mozilla.org/en-US/kb/firefox-page-info-window)
+ *How to allow a website to use your camera or microphone while browsing in Microsoft Edge* in the article [Windows camera, microphone, and privacy](https://support.microsoft.com/en-us/windows/windows-camera-microphone-and-privacy-a83257bc-e990-d54a-d212-b5e41beba857)

**Important**  
A change introduced in Google Chrome version 64 might result in issues with receiving calls if you are using an embedded Contact Control Panel (CCP) softphone using the Connect Customer Streams library. If you are experiencing issues with your microphone when using Chrome version 64, you can resolve the issue by building and deploying the latest version of the [Connect Customer Streams API](https://github.com/aws/amazon-connect-streams/blob/master/Documentation.md#downloading-streams), following the steps under *Downloading Streams*.  
You can also resolve the issue by using Firefox or Edge as your browser.

## How to get help for CCP issues
<a name="how-to-get-help-for-ccp-issues"></a>

**Agents**: Contact your manager or the technical support provided by your company. 

**Connect Customer Administrators**: See [Troubleshooting Issues with the Contact Control Panel (CCP)](troubleshooting.md) for detailed troubleshooting steps. Or, log in to the [AWS Management Console](https://console.aws.amazon.com/console) (https://console.aws.amazon.com/console) using your AWS account. In the upper right corner of the page, choose **Support**, and open a support ticket.