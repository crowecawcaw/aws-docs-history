

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# View style feedback as you type by installing Vale locally
<a name="vale-local"></a>

You can see style feedback as you type. This helps identify awkward writing and typos.

![View style feedback in VS Code](http://docs.aws.amazon.com/eks/latest/userguide/images/contribute-style-local.png)


 **Overview:** 
+ The Vale CLI loads style guides and runs them against source files.
+ The EKS Docs repo includes a vale configuration file that loads style guides and local rules.
+ The Vale extension for Visual Studio (VS) Code displays vale feedback inside the editor.

## Install Vale
<a name="_install_vale"></a>

Follow the instructions in the Vale CLI docs to [Install Vale with a Package Manager](https://vale.sh/docs/install#package-managers).

## Install VS Code Vale extension
<a name="_install_vs_code_vale_extension"></a>

1. Open VS Code.

1. Click the Extensions icon in the Activity Bar (or press Ctrl\+Shift\+X).

1. Search for "Vale".

1. Click Install on the "Vale VSCode" extension by Chris Chinchilla.

1. Reload VS Code when prompted.

## Sync Vale
<a name="_sync_vale"></a>

Vale uses the `.vale.ini` configuration file in your project root to determine which style rules to apply.

1. Open VS Code.

1. Click **View** > **Terminal** (or press Ctrl\+`).

1. Navigate to your project root directory if needed.

1. Run the command:

   ```
   vale sync
   ```

1. Wait for Vale to finish downloading and syncing style rules.

## View style feedback in VS Code
<a name="_view_style_feedback_in_vs_code"></a>

1. Open a Markdown or AsciiDoc file in VS Code.

1. The Vale extension will automatically check your text against the style rules.

1. Style issues will be underlined in the editor.

1. Hover over underlined text to see the specific style suggestion.

1. Fix issues by following the suggestions or consulting the style guide.