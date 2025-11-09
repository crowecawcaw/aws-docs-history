AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Custom templates

In addition to the templates that Migration Hub Journeys provides, you can create custom templates
from existing migration journeys. When you create a custom template from a journey, the
template gets the same phases, modules, tasks, and subtasks as the journey but without
the attachments or comments. The custom template resides in the same migration space as
the journey that you create it from, and members of that space can then create new
journeys from that custom template. You can also share the custom template with other
migration spaces.

###### To view custom templates

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration journey
   templates**.
3. Choose the **Custom templates** tab.

###### To create a custom template from a journey

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration
   journeys**.
3. In the list of migration journeys, choose the name of the journey from which
   you want to create a template.
4. Choose **Actions**, then choose **Create template
   from journey**.
5. (Optional) Replace the default template name with a name of your
   choosing.
6. (Optional) Expand the **Template sharing** section and enter
   the ARN of a migration space that you want to share the new template with. To
   share the template with more than one other migration space, choose
   **Add ARN**.
7. Choose **Create migration template**.

###### To share a custom template with a migration space

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration journey
   templates**.
3. Choose the **Custom templates** tab.
4. Select the template that you want to share.
5. Choose **Share template**.
6. Enter the ARN of the migration space that you want to share the template with.
   To share the template with more than one other migration space, choose
   **Add ARN** as many times as necessary, and enter the
   ARNs of all the migration spaces that you want to share the template
   with.
7. Choose **Share template**.

###### To create a journey from a custom template

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration journey
   templates**.
3. Choose the **Custom templates** tab.
4. Select the template that you want to use to create a journey.
5. Choose **Create migration journey**.
