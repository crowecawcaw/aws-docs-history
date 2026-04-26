# Link to Kiro from Amazon SageMaker Unified Studio

You can use Open in Kiro link provided in Amazon SageMaker Unified Studio to access your SageMaker Space
in Kiro. When you choose this option, Amazon SageMaker Unified Studio will open Kiro on your system and
open your SageMaker space in Kiro.

###### Note

You must be using AWS Toolkit version 3.97 or higher for Open in Kiro to
function.

###### In Identity Center based domains:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your
   SSO credentials.
2. In the left navigation pane, under **IDEs**, choose
   **JupyterLab**.
3. Once your JupyterLab Notebook opens, choose Open in Kiro in the top right
   corner of the page.

###### In IAM-based domains:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your
   IAM credentials.
2. In the left navigating, choose JupyterLab
3. Once your JupyterLab Notebook opens, choose Open in Kiro in the top right
   corner of the page. This will establish a remote connection and open your
   SageMaker space in Kiro.

###### Note

The sessions initiated through Open in Kiro link do not automatically
reconnect if the remote session is interrupted. You will need create a new
remote connection using the Open in Kiro link in Amazon SageMaker Unified Studio. The sessions
established through this link can last for 12 hours if not interrupted.
