# Creating a channel from a

template

You can create a MediaLive channel by using a custom template or by using one of
the built-in templates that MediaLive provides.

###### Topics

- [Using built-in
  templates](#using-builtin-templates "#using-builtin-templates")
- [Using custom templates](#using-custom-templates "#using-custom-templates")
- [Creating a channel from
  a template](#create-channel-template-steps "#create-channel-template-steps")
- [Creating a custom
  template](#creating-custom-template "#creating-custom-template")

## Using built-in

templates

MediaLive includes built-in templates that you can access on the
console. Each template includes data for output groups and outputs, and
most importantly, data for encoding video to meet specific use cases (as
specified in the template description).

When you use a built-in template, all sections of the
**Create channel** page are populated with data
except for the inputs and output destinations sections.

Even though the templates are built-in, you can choose to edit the
existing fields and complete the empty fields.

## Using custom templates

You or another person in your organization may have created custom
MediaLive templates. A custom template might contain nearly all the data that is
required to create a complete channel, or it might contain only portions
of the data. To create a custom template, see [Creating a custom
template](#creating-custom-template "#creating-custom-template").

Typically, templates are created in order to be shared among
different users.

If your organization uses templates, you must obtain the templates
you will use from the person who created the templates. You must store
them in a folder on the computer where you are working on the MediaLive
console. This folder is the "custom template location." You perform this
task in your computer's filesystem, outside of MediaLive.

When you use a custom template, MediaLive populates all sections of the
**Create channel** page with data from the template,
except for the input data. Even if the template includes input data,
that data will not be pulled into the **Create
channel** page.

You can edit the existing fields and complete the empty fields as
needed.

## Creating a channel from

a template

###### To create a MediaLive channel from a template (console)

1. If you plan to use a custom template, make sure you have set up
   to use them. See [Using custom templates](#using-custom-templates "#using-custom-templates").
2. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
3. In the navigation pane, choose **Channels**. On
   the **Channels** page, choose **Create
   channel**.
4. On the **Create channel** page, in the
   **Channel and input details** section, in the
   **Channel template** section, do one of the
   following:
   - To use a built-in template: For
     **Template**, from the **Channel
     templates** section of the drop-down list, choose a
     template. (The **Existing channels** section
     does not list templates.)
   - To use a custom template: Choose **Select custom
     template**. Navigate to the "custom template" folder
     and choose the template. For information on the custom template
     location, see [Using custom templates](#using-custom-templates "#using-custom-templates").

5. Complete the fields, such as the input fields, that must always
   be completed. You can also edit other fields as needed. For more
   information, see [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

## Creating a custom

template

You create a custom MediaLive template by exporting the data from an existing
(and therefore validated) channel. MediaLive exports the data to a JSON file
that you can use on the console .

###### To create a custom template (console)

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Channels**. On
   the **Channels** page, choose the channel name (not
   the radio button).
3. In **Channel actions**, choose
   **Download custom template**. Follow the prompts
   to save the channel as a template. The template is a JSON file with
   the same name as the channel.
4. (Optional) Open the file in a suitable editor and make changes.
   For example, you can change field values, add fields, and remove
   fields. Be careful to maintain valid JSON.

You don’t need to remove the input attachments. When you use
this template in a new channel, MediaLive imports all the data except
for the input attachments. 5. Make the custom template available to the users who will need
them. Each user must store the template in a folder that is
accessible from the computer where the user will work on the MediaLive
console. This task is performed outside of MediaLive.

Users can use the template file on the MediaLive console.
