**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Managing machine learning models in Amazon Pinpoint

The **Machine learning models** page on the Amazon Pinpoint console provides a
single location for you to view, change, and manage Amazon Pinpoint configuration settings for all the
machine learning (ML) models that you've connected to your Amazon Pinpoint account in the current
AWS Region. By using this page, you can perform management tasks such as viewing, changing, and
deleting configuration settings for connections to ML models. You can also configure Amazon Pinpoint to
connect to and use data from additional ML models.

###### Topics

- [Viewing your collection of models](#ml-models-managing-view-all "#ml-models-managing-view-all")
- [Viewing the settings for a model](#ml-models-managing-open "#ml-models-managing-open")
- [Changing the settings for a model](#ml-models-managing-change "#ml-models-managing-change")
- [Copying a model](#ml-models-managing-copy "#ml-models-managing-copy")
- [Deleting a model](#ml-models-managing-delete "#ml-models-managing-delete")
  To learn how to add and configure a connection to a model, see [Setting up a recommender model in Amazon Pinpoint](ml-models-rm-setup.md "ml-models-rm-setup.md").

## Viewing your collection of models

The **Machine learning models** page displays a list of all the
configurations that you created to enable Amazon Pinpoint to connect to and use data from specific ML
models for your account. To browse the list or find specific configurations quickly, you can sort
and filter the list, choose which columns to display, and change other display settings for the
list.

###### To view your collection of ML models

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Machine learning models**. The
   **Machine learning models** page opens and displays the number of
   configurations in your collection and a list of those configurations.
3. To customize the list or find a specific configuration quickly, choose any of the
   following options:
   - To sort the list by a specific type of value, click the column heading for that value.
     To change the sort order from ascending to descending or vice versa, click the column heading
     again.
   - To apply a filter that displays only those configurations whose names contain specific
     text, enter the text in the **Search** box above the list. To remove the
     filter, choose **X** in the **Search** box.
   - To change the number of configurations that are displayed in the list, choose the
     settings icon at the top of the page. Then, for **Page size**, choose the
     number of configurations that you want to display, and choose **Save
     changes**.
   - To add or remove columns from the list, choose the settings icon at the top of the page.
     Then, for **Choose visible columns**, turn each column on or off, and choose
     **Save changes**.

## Viewing the settings for a model

By using the **Machine learning models** page, you can quickly find and
open a specific configuration to view its settings and other information. For example, you can
view a list of the attributes that the model provides for use in messages. After you open a
configuration to view its settings, you can also [change
the settings for the configuration](#ml-models-managing-change "#ml-models-managing-change").

###### To view the settings for an ML model

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Machine learning models**.
3. On the **Machine learning models** page, choose the configuration whose
   settings you want to view.

The configuration page opens and displays the current settings for the configuration.

## Changing the settings for a model

Before you change the configuration settings for an ML model, it's important to note that
Amazon Pinpoint automatically applies your changes to message templates that use the model. (It applies the
changes to both the active and latest versions of the template.) This means that your changes
also affect any messages that use those templates and haven't been sent yet, such as campaign
messages that are scheduled to be sent at a later time.

For this reason, your changes might prevent Amazon Pinpoint from sending messages that use the
configuration and haven't been sent yet. Or, your changes could cause those messages to display
in unexpected or unwanted ways. This depends on the configuration settings that you change. It
also depends on how you designed the templates that use the model.

If you change the configuration settings for an ML model, be sure to also review and make
the appropriate changes to any templates that use the current configuration for the model. For
example, if you delete an attribute, be sure to also remove or replace that attribute in every
template that uses the attribute. Also, be sure to make those changes to the appropriate versions
of each message template. For more information, see [Editing a message template](message-templates-managing-edit.md "message-templates-managing-edit.md").

If you don't want to apply your changes to existing templates and messages, you can [create a copy of the configuration](#ml-models-managing-copy "#ml-models-managing-copy"), and save the copy
with the changes that you want. You can then use the configuration copy in new templates, or
update existing templates to use the configuration copy.

###### To change the settings for an ML model

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Machine learning models**.
3. On the **Machine learning models** page, choose the configuration that
   you want to change. The configuration page opens and displays the current settings for the
   configuration.
4. Choose **Edit model**.
5. On the **Set up model** page, make your changes. You can change any of
   the settings, except the name of the configuration. To change the name of the configuration,
   you can [create a copy of the configuration](#ml-models-managing-copy "#ml-models-managing-copy"), save
   the copy with the name that you want, and then optionally [delete the original configuration](#ml-models-managing-delete "#ml-models-managing-delete").
6. When you finish changing these settings, choose **Next**.
7. On the **Add attributes** page, make your changes, and then choose
   **Next**.
8. On the **Review and publish** page, review the new settings and make sure
   that they're what you want. If they are, choose **Publish** to save your
   changes.

## Copying a model

To quickly create a new configuration that's similar to an existing configuration for an ML
model, you can create a copy of the configuration. You can then change settings for the
configuration copy, without changing the original configuration.

###### To copy an ML model

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Machine learning models**.
3. On the **Machine learning models** page, select the check box next to the
   configuration that you want to copy.
4. On the **Actions** menu, choose **Duplicate**.
5. For **Recommender model name**, enter a name for the configuration copy.
   The name has to begin with a letter or number. It can contain up to 128 characters. The
   characters can be letters, numbers, underscores (\_), or hyphens (‐).
6. When you finish entering the name, choose **Duplicate model**. The
   configuration page opens and displays the current settings for the configuration that you
   copied.
7. (Optional) To change the configuration copy, choose **Edit model**, and
   then make your changes. When you finish, choose **Publish**.

## Deleting a model

If you want to remove the configuration for an ML model from Amazon Pinpoint completely, you can
delete the configuration. When you delete a configuration, Amazon Pinpoint deletes all settings for the
configuration and the configuration becomes unavailable for use in both new and existing message
templates. You can't recover a configuration after you delete it.

###### Warning

If you delete a configuration, Amazon Pinpoint won't be able to send messages that use the
configuration and haven't been sent yet, such as campaign messages that are scheduled to be sent
at a later time. Before you delete a configuration, review and update the contents and settings
for message templates that use the configuration. Also, review any campaigns and journey
activities that use those templates, and update them as necessary.

If you delete a configuration, Amazon Pinpoint doesn't delete any resources or data that's used by the
configuration and stored in other AWS services. This includes Amazon Personalize solutions and campaigns,
and any AWS Lambda functions.

###### To delete an ML model

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Machine learning models**.
3. On the **Machine learning models** page, select the check box next to
   each configuration that you want to delete.
4. On the **Actions** menu, choose **Delete**.
5. In the window that appears, enter `delete` to confirm that you want
   to delete the selected configurations, and then choose **Delete
   models**.
