# Custom chat agents

Custom chat agents enable Amazon Quick Suite users to create tailored conversational
interfaces for specific business needs. Unlike the system chat agent, which is available
to all users with chat permissions by default, custom chat agents can be selectively
shared and configured by authorized users.

Users with chat agent creation capabilities can customize the chat agent's
personality, response style, and capabilities through a natural language interface, or
through the agent builder configuration flow. These users can also configure these chat
agents with specific knowledge sources (like spaces) and workflows (like actions) while
maintaining control over sharing and access permissions for each of those resources
separately. Or, chat agents can be left unlinked for general purpose use which allows
end users to use the agent with all or some of their resources.

Quick Suite admins must give users the permission to create chat agents. For
information on which roles can create chat agents, refer to the [Amazon Quick Suite pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/")
documentation. For information on how to provide or restrict access to these features,
see [Custom permissions](create-custom-permisions-profile.md "create-custom-permisions-profile.md") in the Quick Suite Admin
Guide.

###### Topics

- [Create and preview custom chat agents](#create-custom-agents "#create-custom-agents")
- [Share custom chat agents](#share-custom-agents "#share-custom-agents")
- [Update custom chat agents](#update-custom-agents "#update-custom-agents")
- [Manage access to a custom chat
  agent](#remove-access-custom-agents "#remove-access-custom-agents")
- [View chat agents](#view-agents "#view-agents")
- [View chat agent details](#view-agent-details "#view-agent-details")
- [Duplicate custom chat agents](#duplicate-agents "#duplicate-agents")
- [Delete chat agents](#delete-agents "#delete-agents")

## Create and preview custom chat agents

You can create custom chat agents in Amazon Quick Suite from the **Chat
agents** menu on the Amazon Quick Suite home page. You can preview and test
your chat agent as you build it. When you create a custom chat agent, you are
assigned as its owner by default. The following procedure outlines how to create a
custom chat agent.

Using natural language

###### To create a custom chat agent using a natural language

prompt

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**, and then select **Create chat
   agent**.
3. In **New chat agent**, do the
   following:
   1. In the text input box, enter a natural language
      description for what kind of chat agent you want to
      create. This is the prompt Amazon Quick Suite will use you
      create your chat agent. You can use the suggested sample
      instructions on the page to create your chat agent as
      well.
   2. Then, select **Generate**. Selecting
      **Generate** takes the instruction
      or goal provided and expands it into chat agent
      instructions and configurations. It also scans the
      user's available resources (spaces and action
      connectors) and finds the most relevant matches based on
      the chat agent intent provided. The expanded builder UI
      is opened with these configurations for the user to
      review, customize, test, and launch.

4. On the **Configure chat agent** page, make
   sure your chat agent has the right settings and customize your
   chat agent further. Click on **Update preview**
   to ensure all changes are saved before you try out the chat
   agent in preview.
5. When you're ready, select **Launch chat
   agent** to publish your custom chat agent to the
   chat agent library and use it in chat.

###### Note

    * Until you select **Launch chat
     agent**, your chat agent is not available
     in the chat agent library. If you exit the creation
     process without launching, the preview version will
     be deleted and the chat agent won't be saved.
    * When you launch a chat agent, it remains private
     by default. The chat agent only becomes available in
     other users' libraries after you share it. Once
     shared, subsequent edits and launches will publish
     changes to the same chat agent for all users who
     have access.

Using builder view directly

###### To create a custom chat agent using builder mode

1.  Log in to the Amazon Quick Suite console.
2.  From the left navigation menu, select **Chat
    agents**, and then select **Create chat
    agent**.
3.  In **Agent Creator**,select
    **Skip**. This opens up the chat agent
    configuration page from which you can build and customize your
    chat agent.
4.  Add a name for your custom chat agent. This is the name that
    your chat agent will be identified by.
5.  (Optional) Add a description for your custom chat agent that
    helps users understand the purpose of the chat agent.
6.  (Optional) Select an icon for your chat agent.
7.  In **Configure chat agent**, customize the
    following sections:
    1.  In **AGENT PERSONA**, configure your
        chat agent's personality, identity, tone, and response
        style:
        - For **Agent identity**
          – Define the identity of your chat agent.
          For example, you can give it instructions on what
          it's name and personality are. Amazon Quick Suite will
          use defaults if left blank.
        - For **Persona instructions**
          – Add instructions on how your chat agent
          interacts with users during chat. For example, you
          can define what your chat agent's primary tasks
          are. Amazon Quick Suite uses these to customize your
          chat agent's persona.

    2.  In **Communication style**, for
        **Pick a response style preset**
        – Choose a response style. You can choose between
        the following response style presets or add custom
        instructions:

            * **Executive** –
             Optimized for high-level business communication
             and strategic insights.
            * **Technical** –
             Optimized for detailed technical explanations and
             technical problem-solving.
            * **Creative** –
             Standard configuration for general-purpose
             interactions.

        Each preset has the following settings:

            * For **Tone** – Add a
             natural language prompt to define your agent's
             tone. Amazon Quick Suite will use it to customize your
             chat agent's persona.
            * For **Response format**
             – Add a natural language prompt to define
             your chat agent's response style. Amazon Quick Suite
             will use it to customize your chat agent's
             response style. Define the format of your chat
             chat agent's responses, for example: "Use bullet
             points for lists longer than 3 items".
            * For **Length** –
             Specify the length of your chat agent's responses.
             Define the length of your chat agent's responses,
             for example: "Keep answers under 100
             words".

        When you choose a preset to use, Amazon Quick Suite
        auto-populates the **Tone**,
        **Response format**, and
        **Length** instructions for your
        chat agent's responses based on the style chosen. You
        can further customize the existing prompts using natural
        language, or create new ones.

    3.  In **Reference documents**, upload
        files that remain active in your chat agent's memory to
        guide all interactions. For more information about how
        reference documents work with other context types, see
        [Types of agent context](quicksuite/latest/userguide/agent-knowledge-sources-best-practices.md "quicksuite/latest/userguide/agent-knowledge-sources-best-practices.md").
        - Select **Upload files** or
          drag and drop your documents to attach files that
          will guide your chat agent's responses.
        - You can attach documents of .pdf, .txt, .html,
          .md, .csv, .doc or .docx format. Upto 100,000
          characters of text will be extracted and accepted
          from documents uploaded.

8.  (Optional) In **Knowledge sources**, choose
    between the following options:
    - Continue without linking knowledge sources
      - Your chat agent will generate responses from
        large language model (LLM) knowledge and all
        Amazon Quick Suite resources the interacting user has
        access to. You can choose to select a specific
        knowledge source to focus on during chat. Choose
        this if you want to create a general purpose chat
        chat agent.

    - To link specific existing spaces
      - Select **Link**.
      - From the **Link spaces**
        modal, select the spaces you want to link to your
        chat agent, and then select
        **Link**.

      The system displays a success message to
      denote successful linking.

      If you link a chat agent to a knowledge
      source, your chat agent will generate responses
      from large language model (LLM) knowledge and data
      from linked resources only. You can add up to 1
      more knowledge source to this chat agent as
      temporray context during chat.

    - To create and link a new space
      - Select **Create**.
      - From the **Create space**
        window that opens, select the assets you want to
        add to your space and then select
        **Create**.

      If you link a chat agent to a knowledge
      source, your chat agent will generate responses
      from large language model (LLM) knowledge and data
      from linked resources only. You can add up to 1
      more knowledge source to this chat agent as
      temporray context during chat.

      ###### Note

      For more information on creating and using
      spaces, see [Working with spaces in
      Amazon Quick Suite](working-with-spaces.md "working-with-spaces.md").

      The system displays a success message to
      denote successful space creation. Return to the
      chat agent creation window.
      - In the chat agent creation window, from
        **Knowledge sources** select
        **Link**.
      - From the **Link spaces**
        modal, select the space you just created, and then
        select **Link**.

      The system displays a success message to
      denote successful linking.

9.  (Optional) In **Actions**, for
    **Actions** – Choose between the
    following options:
    - To link specific existing actions
      - Select **Link**.
      - From the **Link action
        connectors** modal, select the action
        connectors you want to link to your chat agent,
        and then select **Next**.
      - In **Actions** select the
        actions you want to add and then select
        **Link**.

      The system displays a success message to
      denote successful linking.

    - To create an action connector and link new
      actions
      - Select **Create**.
      - From the **Actions** home
        page, select **New
        action**.
      - From the **New action**
        window, for **Sources** select
        the action connector you want to add and then
        select **Next**.
      - In **Actions** review the
        actions available and then select
        **Next**.
      - In **Connection details**,
        enter the connection details needed and select
        **Add**.

      ###### Note

      For more information on creating and using
      action connectors, see [Actions in
      Amazon Quick Suite](qbs-actions.md "qbs-actions.md").

      The system displays a success message to
      denote successful action addition. Return to the
      chat agent creation window.
      - In the chat agent creation window, from
        **Actions** select
        **Link**.
      - From the **Link action
        connectors** modal, select the action
        connector you just created, and then select
        **Link**.

      The system displays a success message to
      denote successful linking.

10. In **Customization**, do the
    following:
    1. For **Welcome message** – Add
       a welcome message for your chat agent to display to your
       end user.
    2. For **Suggested prompts** –
       Add example prompts as conversation starters to inform
       your end users of the chat agents capabilities.

11. Select **Launch chat agent** to create your
    custom chat agent.

###### Note

    * Until you select **Launch chat
     agent**, your chat agent is not available
     in the chat agent library. If you exit the creation
     process without launching, the preview version will
     be deleted and the chat agent won't be saved.
    * When you launch a chat agent, it remains private
     by default. The chat agent only becomes available in
     other users' libraries after you share it. Once
     shared, subsequent edits and launches will publish
     changes to the same chat agent for all users who
     have access.

## Share custom chat agents

When you create a chat agent, you are assigned as its owner by default. You can
choose to share a chat agent you own with other Amazon Quick Suite users using the
following permissions:

- _Owner_ permissions – User can edit, share, use,
  and delete the chat agent.
- _Viewer_ permissions – User can view and use the
  chat agent.

You can also define access permissions for a chat agent globally, granting all
users access to a chat agent and then defining more granular access permissions for
specific users and groups.

The following procedure shows you how to share and assign permissions to chat
agents.

###### To share custom chat agents

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**
3. Then, from the **Actions** column for the chat agent you
   want to share, select the menu icon, and then select
   **Share**.
4. In the **Share chat agent** modal that opens, enter the
   user or group name you want to share the chat agent with. When the user or
   group name appears, select it. Repeat the action for all groups or users you
   want to share the chat agent with. The modal displays the users and groups
   you're adding.
5. Assign permissions and access information for each user or group you're
   sharing your chat agent with using the dropdown next to the user or group
   name. You can assign one of two roles:
   - **Owner** – User can edit,
     share, and delete the chat agent.
   - **Viewer** – User can view and
     use the chat agent.

6. Select **Share**.

## Update custom chat agents

You can update custom chat agents in Amazon Quick Suite from the
**Agents** menu on the Amazon Quick Suite home page. The following
procedure outlines how to do so.

###### Note

You can preview how your chat agent customizations updates perform, as you are
configuring the chat agent, in the preview chat interface. Make sure to select
**Update preview** before testing a change. Once all
changes are tested in preview, select **Launch** to publish the
changes to the chat agent currently in use.

###### To update a custom chat agent

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**
3. Then, from the **Actions** column for the chat agent you
   want to share, select the menu icon, and then select
   **Edit**. This creates a preview version of your chat
   agent to update and test before publishing.
4. In the **Edit agent**, update your chat agent settings,
   and then select **Launch**.

## Manage access to a custom chat

agent

If you're the owner of a chat agent, you can choose to change the user access
permissions for a chat agent. You can also remove user and group access to a chat
chat agent. The following procedure shows how.

###### To manage access to custom chat agents

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**
3. Then, from the **Actions** column for the chat agent you
   want to share, select the menu icon, and then select
   **Share**.
4. In the **Share chat agent** modal that opens, select the
   user and group you want to change permissions for. When the user or group
   name appears, select it and change the permissions. Repeat the action for
   all groups or users you want to change permissions for. The modal displays
   the users and group permissions you're changing. You can take the following
   three actions:
   - Change to **Owner** – User can
     edit, share, and delete the chat agent.
   - Change to **Viewer** – User
     can view and use the chat agent.
   - **Remove access** – Remove
     user or group access to a chat agent.

###### Note

You can also define access permissions to a chat agent globally,
granting all users access to a chat agent and then defining more
granular access permissions for specific users and groups. To do so,
choose **Settings** and then use **Global
settings** to turn this feature on or off. 5. Select **Share**.

## View chat agents

You can view a list of the chat agents you have created or have access to. The
following procedure shows how.

###### To view custom chat agents

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**
3. The chat agents you have created or have access to will be displayed on
   the **Chat agents** home page.

## View chat agent details

You can view the details of chat agents that are either created by you or shared
with you, including all spaces and actions attached to each chat agent.

###### To view chat agent details

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**
3. Then, from the list of chat agents, from the **Name**
   column, click on the name of the chat agent you want to view details for. A
   detail modal will open.

###### Note

You can also view chat agent details by navigating to the
**Actions** column for the chat agent you want to
share, selecting the menu icon, and then selecting **View chat
agent details**. 4. In the chat agent details modal that opens, you will see the following
details:

    1. **Description** – The description for the
     chat agent.
    2. **Instruction summary** – A summary of the
     instructions defined for the chat agent.
    3. **Created by** – Details on whether the
     chat agent was created by you or someone else.
    4. **Last modified** – The time the chat
     agent was last modified.
    5. Under **Capabilities**:




    	* **Knowledge** – The
    	 knowledge sources the chat agent is either attached to or
    	 has access to. If your chat agent is linked to a space,
    	 you'll be able to see which space it is linked to.
    	* **Actions** – The
    	 actions that the chat agent is attached or has access to.
    	 You can also view this by clicking on
    	 **info** next to the agent name in the
    	 chat UI agent selector.

## Duplicate custom chat agents

You can duplicate existing custom chat agents without building a chat agent from
scratch. Users can duplicate chat chat agents from the list page using the
**Duplicate** action button. When you duplicate a chat agent,
Amazon Quick Suite creates a new chat agent with name format "[Original name] (copy)",
which you can edit. All fields and configurations from the original chat agent are
copied to the new version of the chat agent. Once duplicated, you can assign custom
user access permissions to the duplicated chat agent and share it.

The following procedure outlines how to duplicate chat agents.

###### To duplicate custom chat agents

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**
3. Then, from the **Actions** column for the chat agent you
   want to share, select the menu icon, and then select
   **Duplicate**.

You will be redirected to a chat agent duplication modal with prepopulated
fields. 4. Make any changes you need to, including adding the right user and group
permissions, and linking it to the assets you want and then select
**Launch** to launch your duplicated chat agent.

## Delete chat agents

You can delete a Amazon Quick Suite chat agent you own. The following procedure shows
you how.

###### To delete a custom chat agent

1. Log in to the Amazon Quick Suite console.
2. From the left navigation menu, select **Chat
   agents**
3. Then, from the **Actions** column for the chat agent you
   want to share, select the menu icon, and then select
   **Delete**.
