AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Change a Built-In Runner

This step shows how you can change a Built-In Runner to run (and optionally, to debug) your code in a different way from how it was originally defined.


1. On the menu bar, choose **Run, Run With**, and then choose the built-in runner you want to change.
2. Stop the runner from trying to run your code by choosing, **Stop** on the run configuration tab that displays.
3. Choose **Runner: My Runner**, where **My Runner** is the name of the runner you want to change, and then choose **Edit Runner**.
4. On the **My Runner.run** tab that is displayed, change the runner's current definition. See [Define a Builder or Runner](build-run-debug-define-builder-runner.md "build-run-debug-define-builder-runner.md").
5. Choose **File, Save As**. Save the file with the same name (**My Runner.run**) in the `my-environment/.c9/runners` directory, where `my-environment` is
the name of your AWS Cloud9 development environment.
###### Note

Any changes you make to a built-in runner apply only to the environment you made those changes in. To apply your changes to a separate environment,
open the other environment, and then follow the preceding steps to open, edit, and save those same changes to that built-in runner.
