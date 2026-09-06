

# Enabling the DataBrew extension for JupyterLab
<a name="jupyter-enabling-databrew"></a>

After you have a secure installation of JupyterLab with extensions enabled, install the DataBrew extension so you can run DataBrew in your notebook. 

**To install the extensions for DataBrew (console)**

1. To start JupyterLab, run the following command at the command prompt.

   ```
   jupyter lab
   ```

1. On the JupyterLab webpage, choose the **Extension Manager** icon in the menu at left. 

1. Search for the DataBrew extension by entering "**brew**" for **Search** at top left. 

1. Locate **aws\_glue\_databrew\_jupyter** in the list, but don't click it. If you click the highlighted name of the extension, a new browser window opens with the [aws\_glue\_databrew\_jupyter](https://github.com/aws/aws-glue-databrew-jupyter-extension#readme) page on GitHub. 

1. To install the DataBrew extension, choose one of the following:
   + At the command line, run `jupyter labextension install aws_glue_databrew_jupyter`.
   + Choose **Install** at the bottom of the extension card, underneath "**aws\_glue\_databrew\_jupyter**" in gray lettering. 

   DataBrew extension is compatible with JupyterLab version 1.2 and 2.x.

1. To verify that it installed, run `jupyter labextension list`. The output should look something like the following.

   ```
   JupyterLab v2.2.9
   Known labextensions:
      app dir: /usr/local/share/jupyter/lab  # varies by OS
           aws_glue_databrew_jupyter v1.0.1  enabled  OK
   ```

1. Rebuild JupyterLab by using one of the following:
   + At the command prompt, run `jupyter lab build`.
   + In the webpage, choose **Rebuild** at top left.

1. When the build is complete, do one of the following:
   + At the command prompt, run `jupyter lab`.
   + In the webpage, choose **Reload** on the **Build Complete** message.

1. In the JupyterLab webpage, close the **Extension Manager** by choosing its icon in the menu at left. 

   To open the extension, choose **Launch AWS Glue DataBrew** from the **Other** section on the **Launcher** tab. The extension uses your current AWS CLI configuration for access keys and AWS region settings. 

After you complete the setup, you can use the **AWS Glue DataBrew** tab to interact with DataBrew from within JupyterLab. 