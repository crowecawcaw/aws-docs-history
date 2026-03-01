# Using the web experience to create and run Amazon Q Apps

After you enable Amazon Q Apps in the console, web experience users can then start
creating, running, and publishing their own purpose-built Q Apps.

Within the Amazon Q Business web experience, users can create an Amazon Q App from
an existing conversation or prompt. Users can simply generate Q Apps in a single step
from their conversation with Amazon Q Business or by describing their requirements
using natural language prompts.

To use the Amazon Q Business web experience, users must be granted access using
IAM Identity Center. You share the endpoint URL of your web experience page with your
users, who go to the URL and are authenticated to access the web experience. This
endpoint URL is in the **web experience settings** of your
application environment in the Amazon Q Business console. To create and run Amazon Q Apps,
users go to the web experience endpoint URL and then select **Apps**
from the navigation menu.

For users to create an Q App from a conversation, once in a conversation, they can
choose the **Create Amazon Q App** button to transform it into an app
for use.

Within **Apps**, users can try the example prompts by selecting the
**Amazon Q Apps Creator** in the web experience. Users can create,
edit, run, publish, and delete their apps. Users can also directly create an app by
describing their requirements using natural language prompts in the
**Amazon Q Apps Creator**.

An Amazon Q App is made up of a collection of cards. A card is a UI element in the web
experience that users can combine with other cards to create an app. Cards take a users'
inputs, support file uploads, connect to other cards, generate text outputs, and allow
actions through new and legacy [Amazon Q Business
built-in plugins](built-in-plugin.md "built-in-plugin.md") and [Amazon Q Business custom
plugins](custom-plugin.md "custom-plugin.md") (if activated), from within Q Apps. Users can select their
Amazon Q App to add, edit, or delete a card.

###### Note

For tips on using effective prompting with
Amazon Q Apps, see this [Community
Article](https://repost.aws/articles/ARQ4zf4VpwQ1OOFjmhOQLWVg "https://repost.aws/articles/ARQ4zf4VpwQ1OOFjmhOQLWVg") on AWS re:Post.

Text output and plugin cards contain _prompt_ instructions that
determine how Amazon Q Business is queried to generate a response. When your users
use the **Amazon Q Apps Creator**, relevant cards are auto-generated with
pre-filled prompts. Your users can further refine these prompts using simple, natural
language. When writing or editing a prompt for a card, users can reference other cards
using an _@ mention_ to select a card from the list of cards in the
app.

Users can also instruct the cards to reference your enterprise data in Amazon Q Business or, they can specify a data source
from a list of your available _data sources_ ([requires additional IAM permissions from the admin](deploy-experience-iam-role.md#deploy-data-source-iam-permissions "deploy-experience-iam-role.md#deploy-data-source-iam-permissions")). This
allows users to focus the Q App's output on a particular subset of your data, rather
than querying across the entire index. For example, an app that is built to summarize
weekly sales updates by geography can have the output cards with results from the data
source tied to a specific geography, rather than your company's entire data repository
or the LLM's foundational knowledge.

Users can then share the Amazon Q Apps that they have created with other web experience
users. To do this, they open their Amazon Q App and then choose
**Publish** to share it with other users through your company's
Amazon Q Apps library. When you publish an app, you can also assign helpful labels to it
to make them easier to group my subject matter or purpose.

To have your published Q Apps become
_Verified_, you'll need to work with your Amazon Q Business
administrators. Admins can review your published apps and update the status to
_Verified_ if they determine the app meets your organization's
criteria. When users access the Q Apps Library, they will see a distinct blue checkmark
icon on any apps that have been marked as **Verified** by
administrators. Verified apps are automatically surfaced to the top of the app list
within each category, making them easily discoverable.
. For more
information, see [Understanding and managing Verified Amazon Q Apps](verfied-apps-management.md "verfied-apps-management.md")

Published Amazon Q Apps are made available in the your Amazon Q Apps library. The creator
of an app can edit their own Amazon Q App and publish changes. This updates the app in the
library. Other users can copy and customize a published Amazon Q App and create a new
version. However, other users cannot edit the original app, only the creator can. Users
can also show their support for a useful Amazon Q App by selecting the like button for the
app in the library.

###### Note

If you update an Amazon Q App with a verified label, it will lose its verified
status until the admin re-applies the label. Maintaining an app's _Verified_ state requires ongoing collaboration with your administrators.
