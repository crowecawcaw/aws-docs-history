# Provide agents with access to the

Amazon Connect Contact Control Panel (CCP)

###### Note

This is the URL to the CCP website:

- **https://`instance
 name`.my.connect.aws/ccp-v2/**
  This is the URL to the [agent workspace](#use-agent-workspace "#use-agent-workspace"):

- **https://`instance
name`.my.connect.aws/agent-app-v2/**

## Steps to ensure agents can access the CCP

Agents use the Contact Control Panel (CCP) to communicate with
contacts. But before agents can access the CCP and handle contacts, there are a few
things you need to do:

1. Ensure your network meets the requirements for using the CCP. For more information
   see [Set up your network to use the Amazon Connect Contact Control Panel
   (CCP)](ccp-networking.md "ccp-networking.md").
2. Ensure agents have the appropriate headsets and workstations. For more information
   see [Agent headset and workstation requirements for using
   the Contact Control Panel (CCP)](ccp-agent-hardware.md "ccp-agent-hardware.md").
3. Create a user name and password for agents to log into the CCP, by [adding agents to your instance](user-management.md "user-management.md").
4. At minimum, [assign them the
   Agent security profile](assign-security-profile.md "assign-security-profile.md"). This grants them
   permissions to access the CCP, which they use to manage contacts.
5. Provide the user name, password, and the CCP website link to your agents so they
   can log in.

We recommend telling agents to bookmark the URL to the CCP so they can readily
access it. 6. Train your agents on the CCP:

    * Watch [Training video: How to use the Contact Center Panel
     (CCP) in Amazon Connect](ccp-video-training.md "ccp-video-training.md")

## Agent workspace: Everything in one

place

Want your agents to handle contacts and access customer profiles, cases, and
knowledge all in one place? Use the [agent
workspace](agent-user-guide.md "agent-user-guide.md")!

The _agent workspace_ is a single web browser
interface that hosts the CCP, [Customer Profiles](ag-cp-select.md "ag-cp-select.md"), [Cases](search-cases.md "search-cases.md"), and [Amazon Q in Connect](search-for-answers.md "search-for-answers.md").

If you're using the CCP that is provided with Amazon Connect, after you enable
Customer Profiles, Cases, or Amazon Q in Connect, share the following URL with your agents so they can
access it in the agent workspace:

- **https://`instance
name`.my.connect.aws/agent-app-v2/**

For help finding your instance name, see [Find your Amazon Connect instance name](find-instance-name.md "find-instance-name.md").

## Grant microphone access in Chrome, Firefox, or

Edge

If agents experience problems with their microphone, they may need to grant microphone
access in their browser. Choose one of the following articles to get the steps
appropriate for your browser:

- [Use your
  camera and microphone in Chrome](https://support.google.com/chrome/answer/2693767?hl=en "https://support.google.com/chrome/answer/2693767?hl=en")
- [Firefox Page Info window](https://support.mozilla.org/en-US/kb/firefox-page-info-window "https://support.mozilla.org/en-US/kb/firefox-page-info-window")
- _How to allow a website to use your camera or microphone while
  browsing in Microsoft Edge_ in the article [Windows camera, microphone, and privacy](https://support.microsoft.com/en-us/windows/windows-camera-microphone-and-privacy-a83257bc-e990-d54a-d212-b5e41beba857 "https://support.microsoft.com/en-us/windows/windows-camera-microphone-and-privacy-a83257bc-e990-d54a-d212-b5e41beba857")

###### Important

A change introduced in Google Chrome version 64 may result in issues with
receiving calls if you are using an embedded Contact Control Panel (CCP) softphone
using the Amazon Connect Streams library. If you are experiencing issues with
your microphone when using Chrome version 64, you can resolve the issue by building
and deploying the latest version of the [Amazon Connect Streams API](https://github.com/aws/amazon-connect-streams/blob/master/Documentation.md#downloading-streams "https://github.com/aws/amazon-connect-streams/blob/master/Documentation.md#downloading-streams"), following the steps under
_Downloading Streams_.

You can also resolve the issue by using Firefox or Edge as your browser.

## How to get help for CCP issues

**Agents**: Contact your manager or the technical support
provided by your company.

**Amazon Connect Administrators**: See [Troubleshooting Issues with the Contact Control Panel
(CCP)](troubleshooting.md "troubleshooting.md") for detailed
troubleshooting steps. Or, log in to the [AWS Management Console](https://console.aws.amazon.com/console "https://console.aws.amazon.com/console") (https://console.aws.amazon.com/console)
using your AWS account. In the upper right corner of the page, choose
**Support**, and open a support ticket.
