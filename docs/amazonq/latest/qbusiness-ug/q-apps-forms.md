# Data collection in Amazon Q Apps

###### Note

The Amazon Q Apps data collection feature is in preview and is subject to change.

A data collection app is an Amazon Q App with one or more form cards that collect multiple
pieces of information from app users. For example, you might use a data collection app to
conduct team surveys, organize project retrospectives, collect ideas for next year's goals,
or collect questions for a town hall. These apps can leverage generative AI to analyze the
collected data, identify common themes, summarize ideas, and provide actionable insights.

When creating a data collection app, you add one or more data collection form cards. You
can also add output cards that use generative AI to analyze or summarize participants' data.
For each form card, you add one or more text input fields. For example, a user can submit an
idea and the reason to prioritize. Forms can be configured to allow multiple submissions by
the same user. For example, users can submit multiple ideas for next year's goals.

After you share your app, you and other users can open it and start collecting data. When
anyone opens the app and starts a data collection, they become a data collection owner. An
owner can own only one active data collection per app. More than one user can start a data
collection for the same app. The data collection owner shares the data collection with
participants, controls access to the forms and data collection results, and controls when to
start and stop accepting submissions.

As the owner of a data collection, choose when reveal or hide the data from the form. For
example, your app might collect ideas from the team for next year. Based on the collected
data, you can choose to hold off on revealing the responses and any generative AI analysis
or summaries.

###### Topics

- [Permissions requirements](#qapps-forms-permissions "#qapps-forms-permissions")
- [Data collection concepts](qapps-forms-data-collection-concepts.md "qapps-forms-data-collection-concepts.md")
- [Creating a new Q App with a data collection form](qapps-forms-creating-app.md "qapps-forms-creating-app.md")
- [Starting a new data collection](qapps-forms-starting-new-data-collection.md "qapps-forms-starting-new-data-collection.md")

## Permissions requirements

For users to create and use data collection apps, the web experience IAM role for
your Amazon Q Business environment must have the following permissions for session
resources:

- qapps:GetQAppSessionMetadata
- qapps:UpdateQAppSessionMetadata
- qapps:ListQAppSessionData
- qapps:ExportQAppSessionData

For more information, including a policy example, see [IAM permissions for using Amazon Q Apps](deploy-q-apps-iam-permissions.md "deploy-q-apps-iam-permissions.md").
