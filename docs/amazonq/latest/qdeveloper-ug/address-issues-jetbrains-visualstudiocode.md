# Address code issues in JetBrains and Visual Studio Code

To address a code issue in JetBrains and Visual Studio Code, you will either have the option to generate an in-place
fix or generate an explanation that you can use to manually update your code.

You can take the following actions:

- Generate an in-place code fix
- Explain the issue and get new code
- Ignore the issue, or ignore all similar issues

## Generate in place fixes for your file

Amazon Q can update your files in-place to automatically remediate a code issue it detected.

To automatically fix a code issue in your file:

JetBrains

1. In the **Problems** tool window, in the
   **Amazon Q Code Issues** tab, choose the
   code issue you want to address.
2. A panel opens with more information about the code issue.
   If applicable, you'll see details about the Amazon Q
   detector that was used to identify the code issue.
3. Along the bottom of the panel, choose **Fix**.
4. In the chat panel, Amazon Q provides a brief explanation
   of the fix and then applies an in-place fix in your code
   file.
5. You will see the code change in your file, and have the
   option to undo the change from the chat panel.

Visual Studio Code

1. In the **Code Issues** tab, choose the code issue you want to address.
2. Choose the wrench icon.

The following image shows the wrench icon for a code issue in Visual Studio Code.

![The wrench icon for a code issue in Visual Studio Code, used to generate a code fix.](images/code-review-fix-vsc.png) 3. In the chat panel, Amazon Q provides a brief explanation
of the fix and then applies an in-place fix in your code
file. 4. You will see the code change in your file, and have the
option to undo the change from the chat panel.

## Explain the code issue and get new code

Amazon Q can provide an in-depth explanation of a code issue and provide
remediation options with accompanying code for you to add to your files.

To get an explanation of a code issue:

JetBrains IDEs

1. In the **Problems** tool window, in the
   **Amazon Q Code Issues** tab, choose the
   code issue you want to address.
2. A panel opens with more information about the code issue.
   If applicable, you'll see details about the Amazon Q
   detector that was used to identify the code issue.
3. Along the bottom of the panel, choose **Explain**.
4. In the chat panel, Amazon Q provides details about the issue and
   suggests how to fix it, with code that you can insert into your
   file.
5. To update your file, follow Amazon Q’s instructions for where to add
   or replace code, and copy the provided code in the correct location in
   your file. Make sure to remove the vulnerable code when adding the updated code.

Visual Studio Code

1. In the **Code Issues** tab, choose the code issue you want to address.
2. Choose the magnifying glass icon.

The following image shows the magnifying glass icon for a code issue in Visual Studio Code.

![The magnifying glass icon for a code issue in Visual Studio Code, used to explain a code issue.](images/code-review-view-details-vsc.png) 3. In the chat panel, Amazon Q provides details about the issue and
suggests how to fix it, with code that you can insert into your
file. 4. To update your file, follow Amazon Q’s instructions for where to add
or replace code, and copy the provided code in the correct location in
your file. Make sure to remove the vulnerable code when adding the updated code.

## Ignore a code issue

If a detected code issue isn’t applicable, you can choose to ignore it, or
ignore it and all similar issues (issues with the same CWE). The issues will be removed from the Code
Issues tab.

To ignore a code issue:

JetBrains

1. In the **Problems** tool window, in the
   **Amazon Q Code Issues** tab, choose the
   code issue you want to ignore.
2. A panel opens with more information about the code issue.
   Along the bottom of the panel, choose
   **Ignore**. The code issue is removed
   from the Code Issue panel.
3. You can also choose **Ignore All** to
   ignore this and other code issues with the same CWE.

Visual Studio Code

1. In the **Code Issues** tab, choose the code issue you want to ignore.
2. Choose the ignore icon.

The following image shows the ignore icon for a code issue in Visual Studio Code.

![The ignore icon for a code issue in Visual Studio Code, used to ignore and close a code issue.](images/code-review-ignore-issue-vsc.png) 3. The code issue is removed from the Code Issue panel. 4. To ignore similar issues, choose the elipses icon, and then the choose
**Ignore Similar Issues** button that appears.
