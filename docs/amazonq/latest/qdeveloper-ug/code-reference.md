# Using code references

Amazon Q learns, in part, from open-source projects. Sometimes, a suggestion it's giving you
may be similar to publicly available code. Code references include information
about the source Amazon Q used to generate a recommendation.

###### Topics

- [View and update code references](#show-code-reference "#show-code-reference")
- [Turn code references off and on](#toggle-code-reference "#toggle-code-reference")
- [Opt out of code with references](#opt-out-code-reference "#opt-out-code-reference")

## View and update code references

With the reference log, you can view references to code recommendations that are
similar to publicly available code. You can also update and edit code recommendations suggested by
Amazon Q.

Choose your IDE to see steps for how to view and update code references.

Visual Studio Code
To display the Amazon Q reference log in VS Code, use the following
procedure.

1. Make sure you are using the latest version of both VS Code and the
   Amazon Q extension.
2. In VS Code, choose **Amazon Q** from the
   component tray at the bottom of the IDE window.

The Amazon Q task bar opens at the top of the IDE window. 3. Choose **Open Code Reference Log**.

The code reference log tab opens. Any references to code recommendations are listed.

The following image shows the open Amazon Q task bar and code reference log tab.

![The Amazon Q code reference log in Visual Studio Code.](images/VSC-coderef.png)

JetBrains
To display the Amazon Q reference log in JetBrains IDEs, use the following
procedure.

1. Make sure you are using the latest version of both your JetBrains IDE and
   the Amazon Q plugin.
2. In JetBrains, choose **Amazon Q** from the
   status bar at the bottom of the IDE window.

The Amazon Q task bar opens above the status bar. 3. Choose **Open Code Reference Log**.

The code reference log tab opens. Any references to code recommendations are listed.

The following image shows the open Amazon Q task bar and code reference log tab.

![The Amazon Q code reference log in JetBrains.](images/JB-coderef.png)

Eclipse
To display the Amazon Q reference log in Eclipse IDEs, use the following
procedure.

1. Make sure you are using the latest version of both the Eclipse IDE and the
   Amazon Q plugin.
2. In your Eclipse IDE, choose the **Amazon Q** icon
   in the top right corner of the IDE.
3. With the Amazon Q chat tab open, choose the ellipsis icon in the top
   right corner of the tab. The Amazon Q task bar opens.

The following image shows the Amazon Q task bar in an Eclipse IDE.

![The Amazon Q task bar in an Eclipse IDE.](images/eclipse-taskbar.png) 4. Choose **Open Code Reference Log**.

The code reference log tab opens. Any references to code recommendations are listed.

Toolkit for Visual Studio
When Amazon Q suggests code that contains a reference in the Toolkit for Visual Studio, the
reference type appears in the suggestion description.

![Code snippet showing a function to create a DynamoDB table with 'Products' as the table name.](images/visual-studio-view-code-suggestions.png)

All accepted suggestions that contain references are captured in the reference log.

To access the reference log, choose the AWS icon, then select **Open Code Reference Log**.

A list of accepted suggestions that contain references will appear. This list includes:

- The location where the suggestion was accepted. Double clicking on this will take you to that location in your code.
- The associated license
- The referenced source code
- The fragment of code attributed to the reference

![CodeWhisperer Reference Log output showing accepted recommendation with MIT license.](images/vstudio-reference-log2.png)

AWS Cloud 9
When you use Amazon Q with AWS Cloud 9, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. On the AWS Cloud 9 console, in the upper left corner, choose the AWS Cloud 9
   logo.
2. From the dropdown menu, choose
   **Preferences**.

On the right side of the console, the
**Preferences** tab will open. 3. On the **Preferences** tab, under
**Project Settings**, under
**Extensions**, select **AWS
Toolkit**. 4. Select or deselect **Amazon Q: Include Suggestions With
Code References**.

Lambda
Amazon Q in Lambda does not support code references. When you use
Amazon Q with Lambda, any code suggestions with references are
omitted.

SageMaker AI Studio
To display the Amazon Q reference log in SageMaker AI Studio, use the following
procedure.

1. At the bottom of the SageMaker AI Studio window, open the Amazon Q
   panel.
2. Choose **Open Code Reference Log**.

JupyterLab
To display the Amazon Q reference log in JupyterLab, use the following
procedure.

1. At the bottom of the JupyterLab window, open the Amazon Q
   panel.
2. Choose **Open Code Reference Log**.

AWS Glue Studio Notebook
To display the Amazon Q reference log in AWS Glue Studio Notebook, use the following
procedure.

1. At the bottom of the AWS Glue Studio Notebook window, open the Amazon Q
   panel.
2. Choose **Open Code Reference Log**.

## Turn code references off and on

In most IDEs, code references are on by default. Choose your IDE to see steps for how
to turn code references off or on.

Visual Studio Code
When you use Amazon Q with VS Code, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. Make sure you are using the latest version of both VS Code and the
   Amazon Q extension.
2. In VS Code, choose **Amazon Q** from the
   component tray at the bottom of the IDE window.

The Amazon Q task bar opens at the top of the IDE window. 3. Choose **Open Settings**. The settings tab opens with the options
related to Amazon Q displayed. 4. Select or deselect the box next to **Show Code With References**.

JetBrains
When you use Amazon Q with your JetBrains IDE, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. Make sure you are using the latest version of both your JetBrains IDE and
   the Amazon Q plugin.
2. In JetBrains, choose **Amazon Q** from the
   status bar at the bottom of the IDE window.

The Amazon Q task bar opens above the status bar. 3. Choose **Open Settings**. The settings window opens with the options
related to Amazon Q displayed. 4. Select or deselect the box next to **Show Code With References**.

Eclipse
When you use Amazon Q with Eclipse, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. Make sure you are using the latest version of both the Eclipse IDE and the
   Amazon Q plugin.
2. Open **Settings** in your Eclipse IDE.
3. Choose **Amazon Q** from the left navigation bar.
4. Select or deselect the box next to **Show Code With References**.
5. Choose **Apply** to save your changes.

Toolkit for Visual Studio
When you use Amazon Q in the Toolkit for Visual Studio, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. Make sure you are using the latest version of the
   Toolkit for Visual Studio.
2. Open **Options** in Visual Studio.
3. Choose **AWS Toolkit** from the left navigation bar, and then choose
   **Amazon Q**.
4. From the dropdown next to
   **Include Suggestions With References**, select True or False.
5. Choose **OK** to save your changes.

AWS Cloud 9
When you use Amazon Q with AWS Cloud 9, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. On the AWS Cloud 9 console, in the upper left corner, choose the AWS Cloud 9
   logo.
2. From the dropdown menu, choose
   **Preferences**.

On the right side of the console, the
**Preferences** tab will open. 3. On the **Preferences** tab, under
**Project Settings**, under
**Extensions**, select **AWS
Toolkit**. 4. Select or deselect **Amazon Q: Include Suggestions With
Code References**.

Lambda
Amazon Q in Lambda does not support code references. When you use
Amazon Q with Lambda, any code suggestions with references are
omitted.

SageMaker AI Studio
When you use Amazon Q with SageMaker AI Studio, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. From the top of the SageMaker AI Studio window choose
   **Settings**.
2. From the **Settings** dropdown, choose
   **Advanced Settings Editor**.
3. In the Amazon Q dropdown, select or deselect the box next to
   **Enable suggestions with code
   references**.

JupyterLab
When you use Amazon Q with JupyterLab, code references are on by
default.

To turn them off, or to turn them back on later, use the following
procedure.

1. From the top of the JupyterLab window choose
   **Settings**.
2. From the **Settings** dropdown, choose
   **Advanced Settings Editor**.
3. In the Amazon Q dropdown, select or deselect the box next to
   **Enable suggestions with code
   references**.

AWS Glue Studio Notebook

1. From the bottom of the AWS Glue Studio Notebook window choose **Amazon Q**.
2. From the pop-up menu, toggle the switch next to **Code with references**.

###### Note

Pausing code references will be valid only for the duration of the current AWS Glue Studio Notebook.

## Opt out of code with references

In some IDEs, you can opt out of receiving suggestions with
references at the administrator level.

Choose your IDE to see steps for opting out as an administrator.

Visual Studio Code
If you are an enterprise administrator, you can opt out of suggestions
with code references for your entire organization. If you do this,
individual developers in your organization will not be able to opt back in
through the IDE. Those developers will be able to select and deselect the
box discussed in the previous section, but it will have no effect if you have opted out at the
enterprise level.

To opt out of suggestions with references at the enterprise level, use the
following procedure.

1. In the Amazon Q Developer console, choose **Settings**.
2. In the **Amazon Q Developer account details** pane, choose
   **Edit**.
3. On the Edit details page, in the **Advanced settings** pane, deselect
   **Include suggestions with code
   references**.
4. Choose **Save changes**.

JetBrains
If you are an enterprise administrator, you can opt out of suggestions
with code references for your entire organization. If you do this,
individual developers in your organization will not be able to opt back in
through the IDE. Those developers will be able to select and deselect the
box discussed in the previous section, but it will have no effect if you have opted out at the
enterprise level.

To opt out of suggestions with references at the enterprise level, use the
following procedure.

1. In the Amazon Q Developer console, choose **Settings**.
2. In the **Amazon Q Developer account details** pane, choose
   **Edit**.
3. On the Edit details page, in the **Advanced settings** pane, deselect
   **Include suggestions with code
   references**.
4. Choose **Save changes**.

Eclipse
If you are an enterprise administrator, you can opt out of suggestions
with code references for your entire organization. If you do this,
individual developers in your organization will not be able to opt back in
through the IDE. Those developers will be able to select and deselect the
box discussed in the previous section, but it will have no effect if you have opted out at the
enterprise level.

To opt out of suggestions with references at the enterprise level, use the
following procedure.

1. In the Amazon Q Developer console, choose **Settings**.
2. In the **Amazon Q Developer account details** pane, choose
   **Edit**.
3. On the Edit details page, in the **Advanced settings** pane, deselect
   **Include suggestions with code
   references**.
4. Choose **Save changes**.

Toolkit for Visual Studio
To opt out of suggestions with references at the enterprise level, use the
following procedure.

1. You can get to the code references setting in one of two ways:
   1. Choose the Amazon Q icon at the edge of the window, and then choose **Options...**
   2. Go to **Tools** -> **AWS Toolkit** -> **Amazon Q**

2. Change the toggle to **True** or
   **False**, depending on whether you want to
   include suggestions with references.

AWS Cloud 9
Amazon Q in AWS Cloud 9 does not support opting out of code suggestions with
references at the enterprise level.

To opt out at the individual developer level, see Toggling code
references.

Lambda
Amazon Q in Lambda does not support code references. When you use
Amazon Q with Lambda, any code suggestions with references are
omitted.

SageMaker AI Studio
Amazon Q does not support opting out of code suggestions with references
at the enterprise level in SageMaker AI Studio.

JupyterLab
Amazon Q does not support opting out of code suggestions with references
at the enterprise level in JupyterLab.

AWS Glue Studio Notebook
Amazon Q does not support opting out of code suggestions with references
in AWS Glue Studio Notebook.
