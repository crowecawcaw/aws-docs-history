# Link to Cursor from Amazon SageMaker Unified Studio

You can use the Open in Cursor link provided in Amazon SageMaker Unified Studio to access your SageMaker
Space in Cursor. When you choose this option, Amazon SageMaker Unified Studio will open Cursor on your
system and open your SageMaker Space in Cursor.

###### Note

You must be using AWS Toolkit version 3.100 or higher for Open in Cursor to
function.

###### In Identity Center based domains:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your
   SSO credentials.
2. In the left navigation pane, under **IDEs**, choose
   **JupyterLab**.
3. Once your JupyterLab Notebook opens, choose Open in Cursor in the top
   right corner of the page.

###### In IAM-based domains:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your
   IAM credentials.
2. In the left navigation, choose JupyterLab.
3. Once your JupyterLab Notebook opens, choose Open in Cursor in the top
   right corner of the page. This will establish a remote connection and open
   your SageMaker Space in Cursor.

###### Note

The sessions initiated through Open in Cursor link do not automatically
reconnect if the remote session is interrupted. You will need to create a new
remote connection using the Open in Cursor link in Amazon SageMaker Unified Studio. The sessions
established through this link can last for 12 hours if not interrupted.
