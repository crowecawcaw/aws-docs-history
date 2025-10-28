**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Creating a project

The procedure for creating a new project differs depending on whether your account
already contains projects in the current AWS Region.

The procedures in this section show you how to create a new project. If you've
never created a project in Amazon Pinpoint, complete the procedures in this
section.

If your Amazon Pinpoint account includes one or more existing projects, you should
complete the steps in [Option 2: Create and
configure a project (existing Amazon Pinpoint users)](#projects-manage-create-existing-user "#projects-manage-create-existing-user") instead.

###### To create a project

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. If this is your first time using Amazon Pinpoint, you see a page that introduces
   you to the features of the service.

In the **Get started** section, enter a name for your
project, and then choose **Create a project**. The
project name that you specify can contain up to 64 characters.

###### Note

You can't rename a project after it's been created. 3. On the **Configure features** page, choose a channel
to configure. For example, if you plan to use the project to send email,
choose the **Configure** button in the
**Email** section.

When you choose to set up a channel, you see options related to
configuring that channel. For example, if you choose to [set up the email channel](channels-email-setup.md "channels-email-setup.md"), you
see options related to verifying an email address. If you choose to
,
you see options related to setting your spending limit and default
message type.

###### Note

You can configure additional channels in this project later. You
aren't limited to only sending messages through the channel that you
configured during this process.
The procedures in this section show you how to create a project if your Amazon Pinpoint
account already includes one or more existing projects.

If your Amazon Pinpoint account doesn't contain any projects, you should complete the
steps in [Option 1: Create and configure
a project (new Amazon Pinpoint users)](#projects-manage-create-new-user "#projects-manage-create-new-user") instead.

###### To create a project

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose **Create
   a project**.
3. On the **Create a project** window, for
   **Project name**, enter a name for your project,
   and then choose **Create**. The project name that you
   specify can contain up to 64 characters.
4. On the **Configure features** page, choose a channel
   to configure. For example, if you plan to use the project to send email,
   choose the **Configure** button in the
   **Email** section.

When you choose to set up a channel, you see options related to
configuring that channel. For example, if you choose to [set up the email channel](channels-email-setup.md "channels-email-setup.md"), you
see options related to verifying an email address. If you choose to
[set up the SMS channel](channels-sms-setup.md "channels-sms-setup.md"),
you see options related to setting your spending limit and default
message type.

###### Note

You can configure additional channels in this project later. You
aren't limited to only sending messages through the channel that you
configured during this process.

If you prefer to set up channels later, choose **Skip this
step**.
