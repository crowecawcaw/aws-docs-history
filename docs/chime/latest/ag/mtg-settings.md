**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Managing meeting settings

Manage your meeting settings from the Amazon Chime console.

## Meeting policy settings

Manage account policies in the Amazon Chime console under **Settings**,
**Meetings**. Choose from the following policy options.

**Enable shared control in screen sharing**

Choose whether users in your organization can grant shared control of
their computers while in meetings. Attendees who request shared control
of your users' computers receive an error message indicating that remote
control isn't available.

**Enable outbound calling to join meetings**

Turns on the Amazon Chime call me feature. Provides the option for meeting attendees
to join meetings by receiving a phone call from Amazon Chime.

## Meeting application settings

Manage meeting application access under **Settings**,
**Meetings** in the Amazon Chime console. You can choose the following
option:

**Allow users to sign in to Amazon Chime using the Amazon Chime Meetings App for Slack**

This option lets users in your organization sign in to Amazon Chime from the
Amazon Chime Meetings App for Slack. For more information, see [Setting up the Amazon Chime Meetings App for Slack](config-slack.md "config-slack.md").

## Meeting Region settings

To improve meeting quality and reduce latency, Amazon Chime processes meetings in the
optimal AWS Region for all participants. You can choose whether to let Amazon Chime
select the optimal Region for a meeting from all available Regions, or to use only
the Regions that you select.

You can update this setting from your account **Meetings**
settings at any time. From your **Meetings** settings, you can also
view the percentage of your Amazon Chime meetings that are being processed in each
Region.

###### To update meeting Region settings

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. On the **Accounts** page, select the name of your
   account.
3. In the navigation pane, choose **Settings**,
   **Meetings**.
4. For **Regions**, choose one of the following
   options:
   - Use all available Regions to ensure meeting
     quality – Allows Amazon Chime to optimize meeting
     processing for you.
   - Use only the Regions that I select
     – Allows you to select Regions from the dropdown menu.

5. Choose **Save**.
