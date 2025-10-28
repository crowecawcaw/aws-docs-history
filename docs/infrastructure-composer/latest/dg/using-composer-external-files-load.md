# Load a project with an external file reference in Infrastructure Composer

Follow the steps listed on this page to load an Infrastructure Composer project with an external file reference.

###### From the Infrastructure Composer console

1. Complete the steps listed in [Import an existing project template in the Infrastructure Composer console](using-composer-project-import-template.md "using-composer-project-import-template.md").
2. Confirm Infrastructure Composer prompts you to connect to the root folder of your project
   If your browser supports the File System Access API, Infrastructure Composer will
   prompt you to connect to the root folder of your project. Infrastructure Composer will
   open your project in **local sync** mode
   to support your external file. If the referenced external file is not supported, you will receive
   an error message. For more information about error messages, see [Troubleshooting](ref-troubleshooting.md "ref-troubleshooting.md").

###### From the Toolkit for VS Code

1. Complete the steps listed in [Access Infrastructure Composer from the AWS Toolkit for Visual Studio Code](setting-up-composer-access-ide.md "setting-up-composer-access-ide.md").
2. Open the template you want to view in Infrastructure Composer.
   When you access Infrastructure Composer from a template, Infrastructure Composer will automatically detect your external file. If the referenced
   external file is not supported, you will receive
   an error message. For more information about error messages, see [Troubleshooting](ref-troubleshooting.md "ref-troubleshooting.md").
