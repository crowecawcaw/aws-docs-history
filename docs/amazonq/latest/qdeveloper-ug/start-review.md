# Starting a code review with Amazon Q Developer

Amazon Q can review your entire file or codebase, or auto-review your code as you write it.

Before you get started, make sure you've installed Amazon Q in an IDE that supports code
reviews. For more information, see
[Installing the Amazon Q Developer extension or plugin in your IDE](q-in-IDE-setup.md "q-in-IDE-setup.md").

###### Topics

- [Review a file, project, or workspace](#project-review "#project-review")
- [Example tasks and prompts](#code-review-prompts "#code-review-prompts")
- [Review as you code](#auto-scan "#auto-scan")

## Review a file, project, or workspace

You can initiate a review from the chat panel to have Amazon Q review a particular
file or project. File and project reviews include both rule-based and generative
AI-powered reviews.

After Amazon Q completes a review, you can investigate the issue and get a code
fix to remediate the issue. For more information, see
[Addressing code issues](address-code-issues.md "address-code-issues.md").

To start a file or project review, complete the following steps for your IDE:

JetBrains

1. Open a file or project you want to review in your IDE.
2. Choose the Amazon Q icon to open the chat panel.
3. Using natural language, describe the type of code review you want to run.
   You can review only your recent code changes, or an entire file. Code
   changes are determined based on the output of the git diff command on your
   file. If applicable, Amazon Q will only review your code changes by default
   unless otherwise specified.
4. With your code project or file open in the IDE, you can enter things like:
   1. `Review my code changes` – Amazon Q will review any code changes in your codebase
   2. `Run a code review on this entire file` – Amazon Q will review all code in your file, not only changes
   3. `Review this repository` – Amazon Q will review your entire codebase, not only changesFor more detailed code review scenarios and associated prompts, see [Example prompts](#code-review-prompts "#code-review-prompts").

5. Amazon Q will begin reviewing your file or project. Once complete, it will
   summarize the highest priority issues and observations.
6. If any issues were detected, the **Code
   Issues** tab opens with a list
   of the issues Amazon Q found.
7. To learn more about a code issue, navigate to the **Code Issues**
   panel. From there, you can do the following:
   1. Select an issue to be redirected to the specific area of the
      file where the vulnerable or low-quality code was
      detected.
   2. To get an explanation of the code issue, choose the magnifying
      glass icon next to the name of the code issue. Amazon Q will
      provide details about the issue and suggest a remediation
      that you can insert into your code.
   3. To fix the code issue, choose the wrench icon next to the name
      of the code issue. Amazon Q will provide a brief explanation of
      the fix and then make an in-place fix in your code file. You
      will see the code change in your file, and have the option to
      undo the change from the chat panel.
   4. You can also use natural language to ask more about an issue, get
      an explanation of proposed fixes, or ask for alternative solutions.

8. For more information about addressing code issues, see [Addressing code issues with Amazon Q Developer](address-code-issues.md "address-code-issues.md").

Visual Studio Code

1. Open a file or project you want to review in your IDE.
2. Choose the Amazon Q icon to open the chat panel.
3. Using natural language, describe the type of code review you want to run.
   You can review only your recent code changes, or an entire file. Code
   changes are determined based on the output of the git diff command on your
   file. If applicable, Amazon Q will only review your code changes by default
   unless otherwise specified.
4. With your code project or file open in the IDE, you can enter things like:
   1. `Review my code changes` – Amazon Q will review any code changes in your codebase
   2. `Run a code review on this entire file` – Amazon Q will review all code in your file, not only changes
   3. `Review this repository` – Amazon Q will review your entire codebase, not only changesFor more detailed code review scenarios and associated prompts, see [Example prompts](#code-review-prompts "#code-review-prompts").

5. Amazon Q will begin reviewing your file or project. Once complete, it will
   summarize the highest priority issues and observations.
6. If any issues were detected, the **Code
   Issues** tab opens with a list
   of the issues Amazon Q found.
7. To learn more about a code issue, navigate to the **Code Issues**
   panel. From there, you can do the following:
   1. Select an issue to be redirected to the specific area of the
      file where the vulnerable or low-quality code was
      detected.
   2. To get an explanation of the code issue, choose the magnifying
      glass icon next to the name of the code issue. Amazon Q will
      provide details about the issue and suggest a remediation
      that you can insert into your code.
   3. To fix the code issue, choose the wrench icon next to the name
      of the code issue. Amazon Q will provide a brief explanation of
      the fix and then make an in-place fix in your code file. You
      will see the code change in your file, and have the option to
      undo the change from the chat panel.
   4. You can also use natural language to ask more about an issue, get
      an explanation of proposed fixes, or ask for alternative solutions.

8. For more information about addressing code issues, see [Addressing code issues with Amazon Q Developer](address-code-issues.md "address-code-issues.md").

Visual Studio

1. Open up a file from the project you want to scan in Visual Studio.
2. Choose the Amazon Q icon at the bottom of your file to open the
   Amazon Q task bar.
3. From the task bar, choose
   **Run Security Scan**. Amazon Q begins scanning your
   project.

In the following image, in Visual Studio, the user chooses the
**Amazon Q** icon, prompting a task bar from
which the user may choose **Run Security
Scan**.

![Visual Studio with the Amazon Q task bar showing "Run Security Scan" as a choice](images/VS-scans.png) 4. The status of your scan is updated in the Visual Studio output pane.
You're notified when the scan is complete.

For information about viewing and addressing findings, see
[Addressing code issues with Amazon Q Developer](address-code-issues.md "address-code-issues.md").

## Example tasks and prompts

There are several scenarios that you might be in when initiating a code review.
Following is an overview of some of the ways to initiate a code review and how to
prompt Amazon Q to run the review you want.

- To review just the code changes for a single file:
  - Open the file in your IDE and enter `Review my code`
  - Enter `Review the code in
<filename>`

- To review an entire code file:
  - Open a file without changes and enter `Review my code`
  - Open a file with changes and enter `Review my entire code file`
  - Enter `Review all the code in
<filename>`

- To review all code changes in your repository:
  - Open the repository in your IDE and enter `Review my code`

- To review your entire repository, not just the changes:
  - Open the repository in your IDE and enter `Review my repository`

## Review as you code

###### Note

Amazon Q auto-reviews are only available with a
[Amazon Q Developer Pro subscription](getting-started-q-dev.md "getting-started-q-dev.md").

Auto-reviews are rule-based reviews powered by [Amazon Q detectors](../../../codeguru/detector-library.md "../../../codeguru/detector-library.md") . Amazon Q automatically
reviews the file you are actively coding in, generating code issues as soon as they
are detected in your code. When Amazon Q performs auto reviews, it doesn’t generate
in-place code fixes.

Auto-reviews are enabled by default when you use Amazon Q. Use the following
procedure to pause or resume auto-reviews.

###### Pause and resume auto-reviews

To pause auto-reviews, complete the following steps.

1. Choose **Amazon Q** from the bottom of the IDE window.

The Amazon Q task bar opens. 2. Choose **Pause Auto-Reviews**. To resume auto-reviews,
choose **Resume Auto-Reviews**.
