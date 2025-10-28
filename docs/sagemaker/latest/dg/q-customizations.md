# Customize Amazon Q Developer in Amazon SageMaker Studio

applications

You can customize Amazon Q Developer in the JupyterLab and Code Editor applications in Amazon SageMaker Studio.
When you customize Q Developer, it provides suggestions and answers based on examples from
your codebase. If you use Amazon Q Developer Pro, you can load any customizations that you've created
with that service.

## Customize in JupyterLab

In JupyterLab, you can load any customizations that you've created with Amazon Q Developer Pro.
Or, in your JupyterLab space, you can customize Q Developer locally with files that you
upload to the space.

### To use customizations that you've

created in Amazon Q Developer Pro

When you load a customization, Q Developer provides suggestions based on the
codebase that you used to create the customization. Also, when you use the chat in
the **Amazon Q** panel, you interact with your customization.

For more information about setting up customizations, see [Customizing suggestions](../../../amazonq/latest/qdeveloper-ug/customizations.md "../../../amazonq/latest/qdeveloper-ug/customizations.md") in the _Amazon Q Developer User
Guide_.

###### To load your customization

Open your JupyterLab space and complete the following steps.

1. In the status bar at the bottom of JupyterLab, choose
   **Amazon Q**. A menu opens.
2. In the menu, choose **Other Features**. The
   **Amazon Q Features** tab opens in the main work
   area.
3. In the **Amazon Q Features** tab, under **Select
   Customization**, choose your Q Developer customization.
4. Interact with your customization in either of the following ways:
   - Create a notebook, and write code in it. As you do, Q Developer
     automatically provides tailored inline suggestions based on your
     customization.
   - Chat with Q Developer in the **Amazon Q** panel by
     following these steps:
     1. In the left sidebar in JupyterLab, choose the
        **Jupyter AI Chat**
        icon. The **Amazon Q** panel
        opens.
     2. Use the **Ask Amazon Q** chat box to
        interact with your customization.

### To customize Amazon Q Developer with files in

your JupyterLab space

In JupyterLab, you can customize Q Developer with files that you upload to your
space. Then, in the chat in the **Amazon Q** panel, you can use a
command to ask Q Developer about those files.

When you customize Q Developer with files in your space, the customization exists
only in your space. You can't load the customization elsewhere, such as in other
spaces or in the Amazon Q Developer console.

You can customize Q Developer with files in JupyterLab if you use either
Amazon Q Developer Pro or Amazon Q Developer at the Free tier.

###### To customize with your files

Open your JupyterLab space and complete the following steps.

1. Check whether your space is configured with the required embedding model.
   You can customize Q Developer in JupyterLab only if you use the default
   embedding model, which is **CodeSage :: codesage-small**.
   To check, do the following:
   1. In the left sidebar in JupyterLab, choose the **Jupyter
      AI Chat** icon. The **Amazon Q** panel
      opens.
   2. Choose the settings icon in the upper-right corner of the
      panel.
   3. For **Embedding model**, if necessary, choose
      **CodeSage :: codesage-small**, and choose
      **Save Changes**.
   4. In the upper-right corner of the panel, choose the back icon.

2. To upload files that you want to customize Q Developer with, in the
   **File Browser** panel, choose the **Upload
   Files** icon.
3. After you upload your files, in the **Ask Amazon Q** chat
   box, type `/learn `file path/``. Replace
   _file path/_ with the path to your files in your
   JupyterLab space. When Amazon Q finishes processing your files, it confirms
   with a chat message in the Amazon Q panel.
4. To ask Q Developer a question about your files, type `/ask` in
   the chat box, and follow the command with your question. Amazon Q generates an
   answer based on your files, and it responds in the chat.

For more information about the `/learn` and `/ask` commands,
such as their options and supported arguments, see [Learning about local data](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#learning-about-local-data "https://jupyter-ai.readthedocs.io/en/latest/users/index.html#learning-about-local-data") in the Jupyter AI user documentation. That
page explains how to use the commands with the Jupyternaut AI chatbot. JupyterLab
in Amazon SageMaker Studio supports the same command syntax.

## Customize in Code Editor

If you've created a customization in Amazon Q Developer Pro, you can load it in Code Editor. Then, when
Q Developer provides suggestions for your code, it bases them on the codebase that you
used to create the customization. Also, when you use the chat in the **Amazon Q:
Chat** panel, you interact with your customization.

###### To use customizations that you've created in Amazon Q Developer Pro

Open your Code Editor space and complete the following steps.

1. In the Code Editor menu, choose **View**, and choose
   **Command Pallette**.
2. In the command pallet, begin typing `>Amazon Q: Select
Customization`, and choose that option in the filtered list of
   commands when it appears. The command pallet shows your Q Developer
   customizations.
3. Choose your customization.
4. Interact with your customization in either of the following ways:
   - Create a Python file or a Jupyter notebook, and write code in it. As
     you do, Q Developer automatically provides tailored inline suggestions
     based on your customization.
   - Chat with Q Developer in the **Amazon Q** panel by
     following these steps:
     1. In the left sidebar in Code Editor, choose the
        **Amazon Q** icon. The **Amazon Q:
        Chat** panel opens.
     2. Use the chat box to interact with your customization.

For more information about the capabilities of Q Developer, see [Using
Amazon Q Developer in the IDE](../../../amazonq/latest/qdeveloper-ug/q-in-IDE.md "../../../amazonq/latest/qdeveloper-ug/q-in-IDE.md") in the _Amazon Q Developer User
Guide_.
