

# Using code references
<a name="code-reference"></a>

Amazon Q learns, in part, from open-source projects. Sometimes, a suggestion it's giving you may be similar to publicly available code. Code references include information about the source Amazon Q used to generate a recommendation.

**Topics**
+ [View and update code references](#show-code-reference)
+ [Turn code references off and on](#toggle-code-reference)
+ [Opt out of code with references](#opt-out-code-reference)

## View and update code references
<a name="show-code-reference"></a>

With the reference log, you can view references to code recommendations that are similar to publicly available code. You can also update and edit code recommendations suggested by Amazon Q.

Choose your IDE to see steps for how to view and update code references. 

------
#### [ Visual Studio Code ]

To display the Amazon Q reference log in VS Code, use the following procedure.

1. Make sure you are using the latest version of both VS Code and the Amazon Q extension. 

1. In VS Code, choose **Amazon Q** from the IDE component tray.

   The Amazon Q task bar opens. 

1. Choose **Open Code Reference Log**.

   The code reference log tab opens. Any references to code recommendations are listed.

The following image shows the open Amazon Q task bar and code reference log tab.

![The Amazon Q code reference log in Visual Studio Code.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/VSC-coderef.png)


------
#### [ JetBrains ]

To display the Amazon Q reference log in JetBrains IDEs, use the following procedure.

1. Make sure you are using the latest version of both your JetBrains IDE and the Amazon Q plugin. 

1. In JetBrains, choose **Amazon Q** from the IDE status bar.

   The Amazon Q task bar opens. 

1. Choose **Open Code Reference Log**.

   The code reference log tab opens. Any references to code recommendations are listed.

The following image shows the open Amazon Q task bar and code reference log tab.

![The Amazon Q code reference log in JetBrains.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/JB-coderef.png)


------
#### [ Eclipse ]

To display the Amazon Q reference log in Eclipse IDEs, use the following procedure.

1. Make sure you are using the latest version of both the Eclipse IDE and the Amazon Q plugin. 

1. In your Eclipse IDE, choose the **Amazon Q** icon in the IDE toolbar. 

1. With the Amazon Q chat tab open, choose the ellipsis icon in the chat panel header. The Amazon Q task bar opens.

   The following image shows the Amazon Q task bar in an Eclipse IDE.  
![The Amazon Q task bar in an Eclipse IDE.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/eclipse-taskbar.png)

1. Choose **Open Code Reference Log**.

   The code reference log tab opens. Any references to code recommendations are listed.

------
#### [ Toolkit for Visual Studio ]

When Amazon Q suggests code that contains a reference in the Toolkit for Visual Studio, the reference type appears in the suggestion description.

![Code snippet showing a function to create a DynamoDB table with 'Products' as the table name.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/visual-studio-view-code-suggestions.png)


All accepted suggestions that contain references are captured in the reference log.

To access the reference log, choose the AWS icon, then select **Open Code Reference Log**.

A list of accepted suggestions that contain references will appear. This list includes:
+ The location where the suggestion was accepted. Double clicking on this will take you to that location in your code.
+ The associated license
+ The referenced source code
+ The fragment of code attributed to the reference

![CodeWhisperer Reference Log output showing accepted recommendation with MIT license.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/vstudio-reference-log2.png)


------
#### [ AWS Cloud 9 ]

When you use Amazon Q with AWS Cloud 9, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. On the AWS Cloud 9 console, choose the AWS Cloud 9 logo.

1. From the dropdown menu, choose **Preferences**.

   The **Preferences** tab opens.

1. On the **Preferences** tab, under **Project Settings**, under **Extensions**, select **AWS Toolkit**.

1. Select or deselect **Amazon Q: Include Suggestions With Code References**.

------
#### [ Lambda ]

Amazon Q in Lambda does not support code references. When you use Amazon Q with Lambda, any code suggestions with references are omitted.

------
#### [ SageMaker AI Studio ]

To display the Amazon Q reference log in SageMaker AI Studio, use the following procedure.

1. In the SageMaker AI Studio window, open the Amazon Q panel.

1. Choose **Open Code Reference Log**.

------
#### [ JupyterLab ]

To display the Amazon Q reference log in JupyterLab, use the following procedure.

1. In the JupyterLab window, open the Amazon Q panel.

1. Choose **Open Code Reference Log**.

------
#### [ AWS Glue Studio Notebook ]

To display the Amazon Q reference log in AWS Glue Studio Notebook, use the following procedure.

1. In the AWS Glue Studio Notebook window, open the Amazon Q panel.

1. Choose **Open Code Reference Log**.

------

## Turn code references off and on
<a name="toggle-code-reference"></a>

In most IDEs, code references are on by default. Choose your IDE to see steps for how to turn code references off or on. 

------
#### [ Visual Studio Code ]

When you use Amazon Q with VS Code, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. Make sure you are using the latest version of both VS Code and the Amazon Q extension. 

1. In VS Code, choose **Amazon Q** from the IDE component tray.

   The Amazon Q task bar opens. 

1. Choose **Open Settings**. The settings tab opens with the options related to Amazon Q displayed.

1. Select or deselect the box next to **Show Code With References**.

------
#### [ JetBrains ]

When you use Amazon Q with your JetBrains IDE, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. Make sure you are using the latest version of both your JetBrains IDE and the Amazon Q plugin. 

1. In JetBrains, choose **Amazon Q** from the IDE status bar.

   The Amazon Q task bar opens. 

1. Choose **Open Settings**. The settings window opens with the options related to Amazon Q displayed. 

1. Select or deselect the box next to **Show Code With References**.

------
#### [ Eclipse ]

When you use Amazon Q with Eclipse, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. Make sure you are using the latest version of both the Eclipse IDE and the Amazon Q plugin. 

1. Open **Settings** in your Eclipse IDE.

1. Choose **Amazon Q** from the left navigation bar.

1. Select or deselect the box next to **Show Code With References**.

1. Choose **Apply** to save your changes.

------
#### [ Toolkit for Visual Studio ]

When you use Amazon Q in the Toolkit for Visual Studio, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. Make sure you are using the latest version of the Toolkit for Visual Studio. 

1. Open **Options** in Visual Studio.

1. Choose **AWS Toolkit** from the left navigation bar, and then choose **Amazon Q**.

1. From the dropdown next to **Include Suggestions With References**, select True or False.

1. Choose **OK** to save your changes.

------
#### [ AWS Cloud 9 ]

When you use Amazon Q with AWS Cloud 9, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. On the AWS Cloud 9 console, choose the AWS Cloud 9 logo.

1. From the dropdown menu, choose **Preferences**.

   The **Preferences** tab opens.

1. On the **Preferences** tab, under **Project Settings**, under **Extensions**, select **AWS Toolkit**.

1. Select or deselect **Amazon Q: Include Suggestions With Code References**.

------
#### [ Lambda ]

Amazon Q in Lambda does not support code references. When you use Amazon Q with Lambda, any code suggestions with references are omitted.

------
#### [ SageMaker AI Studio ]

When you use Amazon Q with SageMaker AI Studio, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. From the top of the SageMaker AI Studio window choose **Settings**.

1. From the **Settings** dropdown, choose **Advanced Settings Editor**.

1. In the Amazon Q dropdown, select or deselect the box next to **Enable suggestions with code references**.

------
#### [ JupyterLab ]

When you use Amazon Q with JupyterLab, code references are on by default.

To turn them off, or to turn them back on later, use the following procedure.

1. From the top of the JupyterLab window choose **Settings**.

1. From the **Settings** dropdown, choose **Advanced Settings Editor**.

1. In the Amazon Q dropdown, select or deselect the box next to **Enable suggestions with code references**.

------
#### [ AWS Glue Studio Notebook ]

1. In the AWS Glue Studio Notebook window, choose **Amazon Q**.

1. From the pop-up menu, toggle the switch next to **Code with references**.

**Note**  
Pausing code references will be valid only for the duration of the current AWS Glue Studio Notebook.

------

## Opt out of code with references
<a name="opt-out-code-reference"></a>

In some IDEs, you can opt out of receiving suggestions with references at the administrator level.

Choose your IDE to see steps for opting out as an administrator.

------
#### [ Visual Studio Code ]

If you are an enterprise administrator, you can opt out of suggestions with code references for your entire organization. If you do this, individual developers in your organization will not be able to opt back in through the IDE. Those developers will be able to select and deselect the box discussed in the previous section, but it will have no effect if you have opted out at the enterprise level.

To opt out of suggestions with references at the enterprise level, use the following procedure.

1. In the Amazon Q Developer console, choose **Settings**. 

1. In the **Amazon Q Developer account details** pane, choose **Edit**.

1. On the Edit details page, in the **Advanced settings** pane, deselect **Include suggestions with code references**.

1. Choose **Save changes**.

------
#### [ JetBrains ]

If you are an enterprise administrator, you can opt out of suggestions with code references for your entire organization. If you do this, individual developers in your organization will not be able to opt back in through the IDE. Those developers will be able to select and deselect the box discussed in the previous section, but it will have no effect if you have opted out at the enterprise level.

To opt out of suggestions with references at the enterprise level, use the following procedure.

1. In the Amazon Q Developer console, choose **Settings**. 

1. In the **Amazon Q Developer account details** pane, choose **Edit**.

1. On the Edit details page, in the **Advanced settings** pane, deselect **Include suggestions with code references**.

1. Choose **Save changes**.

------
#### [ Eclipse ]

If you are an enterprise administrator, you can opt out of suggestions with code references for your entire organization. If you do this, individual developers in your organization will not be able to opt back in through the IDE. Those developers will be able to select and deselect the box discussed in the previous section, but it will have no effect if you have opted out at the enterprise level.

To opt out of suggestions with references at the enterprise level, use the following procedure.

1. In the Amazon Q Developer console, choose **Settings**. 

1. In the **Amazon Q Developer account details** pane, choose **Edit**.

1. On the Edit details page, in the **Advanced settings** pane, deselect **Include suggestions with code references**.

1. Choose **Save changes**.

------
#### [ Toolkit for Visual Studio ]

To opt out of suggestions with references at the enterprise level, use the following procedure. 

1. You can get to the code references setting in one of two ways:

   1. Choose the Amazon Q icon at the edge of the window, and then choose **Options...**

   1. Go to **Tools** -> **AWS Toolkit** -> **Amazon Q**

1. Change the toggle to **True** or **False**, depending on whether you want to include suggestions with references.

------
#### [ AWS Cloud 9 ]

Amazon Q in AWS Cloud 9 does not support opting out of code suggestions with references at the enterprise level.

To opt out at the individual developer level, see Toggling code references.

------
#### [ Lambda ]

Amazon Q in Lambda does not support code references. When you use Amazon Q with Lambda, any code suggestions with references are omitted.

------
#### [ SageMaker AI Studio ]

Amazon Q does not support opting out of code suggestions with references at the enterprise level in SageMaker AI Studio.

------
#### [ JupyterLab ]

Amazon Q does not support opting out of code suggestions with references at the enterprise level in JupyterLab.

------
#### [ AWS Glue Studio Notebook ]

Amazon Q does not support opting out of code suggestions with references in AWS Glue Studio Notebook.

------