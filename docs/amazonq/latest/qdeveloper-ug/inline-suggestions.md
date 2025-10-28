# Generating inline suggestions with Amazon Q Developer

Amazon Q can provide you with code recommendations in real time. As you write
code, Amazon Q automatically generates suggestions based on your existing code and comments.
Your personalized recommendations can vary in size and scope, ranging from a single line
comment to fully formed functions.

When you start typing out single lines of code or comments, Amazon Q makes suggestions
based on your current and previous inputs. Filenames are also taken into consideration.

Inline suggestions are automatically enabled when you download the Amazon Q extension. To
get started, start writing code, and Amazon Q will begin generating code suggestions.

You can also customize the suggestions Amazon Q generates to your software development
team's internal libraries, proprietary algorithmic techniques, and enterprise code style.
For more information on customizing suggestions, see [Customizing suggestions](customizations.md "customizations.md").

###### Topics

- [Pausing suggestions with Amazon Q](#toggling-suggestions "#toggling-suggestions")
- [Amazon Q code completion in action](#what-is-walkthrough "#what-is-walkthrough")
- [Generating inline suggestions in AWS coding environments](setting-up-AWS-coding-env.md "setting-up-AWS-coding-env.md")
- [Using shortcut keys](actions-and-shortcuts.md "actions-and-shortcuts.md")
- [Using code references](code-reference.md "code-reference.md")
- [Code examples](inline-suggestions-code-examples.md "inline-suggestions-code-examples.md")

## Pausing suggestions with Amazon Q

Choose your IDE to see steps for pausing and resuming inline code suggestions in Amazon Q.

Visual Studio Code

1. In VS Code, choose **Amazon Q** from the
   component tray at the bottom of the IDE window.

The Amazon Q task bar opens at the top of the IDE window. 2. Choose **Pause Auto-Suggestions** or **Resume
Auto-Suggestions**.

The following image shows the Amazon Q task bar in VS Code.

![The Amazon Q task bar in VS Code.](images/VSC-taskbar.png)

JetBrains

1. In your JetBrains IDE, choose **Amazon Q** from the
   status bar at the bottom of the IDE window.

The Amazon Q task bar opens above the status bar. 2. Choose **Pause Auto-Suggestions** or **Resume
Auto-Suggestions**.

The following image shows the Amazon Q task bar in a JetBrains IDE.

![The Amazon Q task bar in a JetBrains IDE.](images/JB-taskbar.png)

Eclipse

1. In your Eclipse IDE, choose the **Amazon Q** icon
   in the top right corner of the IDE.
2. With the Amazon Q chat tab open, choose the ellipsis icon in the top
   right corner of the tab. The Amazon Q task bar opens.

The following image shows the Amazon Q task bar in an Eclipse IDE.

![The Amazon Q task bar in an Eclipse IDE.](images/eclipse-taskbar.png) 3. Choose **Pause Auto-Suggestions** or **Resume
Auto-Suggestions**.

Visual Studio

1. From the edge of the window, choose the Amazon Q icon.
2. Select **Pause Auto-Suggesions** or **Resume Auto-Suggestions**

The following image shows the Amazon Q task bar in a Visual Studio.

![The Developer Tools menu in Visual Studio.](images/vstudio-toggle-suggestions.png)

AWS Cloud9
Amazon Q does not support toggling suggestions on and off in AWS Cloud9.

To stop receiving Amazon Q suggestions in AWS Cloud9, remove the IAM policy that gives
Amazon Q access to AWS Cloud9 from the role or user that you are using to access AWS Cloud9.

AWS Lambda
To deactivate or re-activate Amazon Q code suggestions in Lambda:

1. In the Lambda console, open the screen for a particular Lambda function.
2. In the **Code source** section, from the toolbar, choose **Tools**.
3. From the dropdown menu, choose **Amazon Q Code Suggestions.**

Amazon SageMaker AI Studio

1. In the SageMaker AI Studio console, choose Amazon Q from the bottom of the window.

The Amazon Q panel will open. 2. Choose **Pause Auto-Suggestions** or **Resume Auto-Suggestions**.

JupyterLab

1. In the JupyterLab console, choose Amazon Q from the bottom of the window.

The Amazon Q panel will open. 2. Choose **Pause Auto-Suggestions** or **Resume Auto-Suggestions**.

AWS Glue Studio Notebook

1. In the AWS Glue Studio Notebook console, choose Amazon Q from the bottom of the window.

The Amazon Q panel will open. 2. Choose **Pause Auto-Suggestions** or **Resume Auto-Suggestions**.

## Amazon Q code completion in action

This section demonstrates how Amazon Q can help you write a complete application. This
application creates an Amazon S3 bucket and a Amazon DynamoDB table, plus a unit test that validates
both tasks.

Here, Amazon Q helps the developer choose which libraries to import. Using the arrow
keys, the developer toggles through multiple suggestions.

![An example of the block completion feature.](images/whatis-demo-1.gif)

Here, the developer enters a comment, describing the code they intend to write on the
next line.

Amazon Q correctly anticipates the method to be called. The developer can accept the
suggestion with the tab key.

![alt_text](images/whatis-demo-2.png)

Here, the developer prepares to define constants.

Amazon Q correctly anticipates that the first constant will be `REGION` and
that its value will be `us-east-1`, which is the default.

![alt_text](images/whatis-demo-3.png)

Here, the developer prepares to write code that will open sessions between the user and
both Amazon S3 and DynamoDB.

Amazon Q, familiar with AWS APIs and SDKs, suggests the correct format.

![alt_text](images/whatis-demo-4.1.png)

The developer has merely written the name of the function that will create the bucket.
But based on that (and the context), Amazon Q offers a full function, complete with
try/except clauses.

Notice the use of `TEST_BUCKET_NAME, which is a constant declared earlier in the
 same file.`

![alt_text](images/whatis-demo-5.png)

The developer has only just begun to type in the name of the function that will create a
DynamoDB table. But Amazon Q can tell where this is going.

Notice that the suggestion accounts for the DynamoDB session created earlier, and even
mentions it in a comment.

![alt_text](images/whatis-demo-6.png)

The developer has done little more than write the name of the unit test class, when
Amazon Q offers to complete it.

Notice the built-in references to the two functions created earlier in the same
file.

The developer has only just begun to type in the name of the function that will create a
DynamoDB table. But Amazon Q can tell where this is going.

Notice that the suggestion accounts for the DynamoDB session created earlier, and even
mentions it in a comment.

![alt_text](images/whatis-demo-7.png)

Based only on a comment and the context, Amazon Q supplies the entire main
function.

![alt_text](images/whatis-demo-8.1.png)

All that's left is the main guard, and Amazon Q knows it.

Based only on a comment and the context, Amazon Q supplies the entire main
function.

![alt_text](images/whatis-demo-9.png)

Finally, the developer runs the unit test from the terminal of the same IDE where the
coding took place.

![alt_text](images/whatis-demo-10.png)
