AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with Builders, Runners, and Debuggers in the
 AWS Cloud9 IDE

A *builder* instructs the AWS Cloud9 Integrated Development Environment (IDE) how to build a project's
 files. A *runner* instructs the AWS Cloud9 IDE how to run files of a specific
 type. A runner can use a *debugger* to help find any problems in the source
 code of the files.

You can use the AWS Cloud9 IDE to build, run, and debug your code in the following ways:


* Use a builder to build your project's files. For more information, see [Build Your Project's Files](#build-run-debug-build "#build-run-debug-build").
* Use a runner to run (and optionally, to debug) your code. For more information, see
 [Built-In Build, Run, and Debug
 Support](#build-run-debug-supported "#build-run-debug-supported") and [Run Your Code](#build-run-debug-run "#build-run-debug-run").
* Change a built-in runner to run (and optionally, to debug) your code in a different
 way from how it was originally defined. For more information, see [Change a Built-In Runner](build-run-debug-change-runner.md "build-run-debug-change-runner.md").
* Use a runner to run (and optionally, to debug) your code with a custom combination of
 file name, command line options, debug mode, current working directory, and environment
 variables. For more information, see [Create a Run Configuration](build-run-debug-create-run-config.md "build-run-debug-create-run-config.md").
* Create your own builder or runner. For more information, see [Create a Builder or
 Runner](#build-run-debug-create-builder-runner "#build-run-debug-create-builder-runner").

## Built-In Build, Run, and Debug Support


The AWS Cloud9 IDE provides built-in support for building, running, and debugging code for several languages. For a complete list, see [Language Support](language-support.md "language-support.md").


Built-in build support is available on the menu bar with the **Run**, **Build System** and **Run**, **Build** menu commands.
To add support for a programming language or tool that isn't listed, see [Create a Builder or Runner](#build-run-debug-create-builder-runner "#build-run-debug-create-builder-runner").


Built-in run support is available with the **Run** button, and on the menu bar with the **Run**, **Run With** and
**Run**, **Run Configurations** menu commands. To add support for a programming language or tool
that isn't listed, see
[Create a Builder or Runner](#build-run-debug-create-builder-runner "#build-run-debug-create-builder-runner") and [Create a Run Configuration](build-run-debug-create-run-config.md "build-run-debug-create-run-config.md").


Built-in debug support is available through the **Debugger** window. To display the **Debugger** window, choose the **Debugger** button.
If the **Debugger** button is not visible, choose **Window**, **Debugger** on the menu bar.


## Build Your Project's Files



1. Open a file that corresponds to the code you want to build.
2. On the menu bar, choose **Run, Build System**, and then choose the name of the builder to use,
if it isn't already chosen.
If the builder you want to use isn't listed, stop this procedure, complete the steps in [Create a Builder or Runner](#build-run-debug-create-builder-runner "#build-run-debug-create-builder-runner"),
and then return to this procedure.
3. Choose **Run, Build**.

## Run Your Code



1. Open a file that corresponds to the code you want to run, if the file isn't already open and selected.
2. On the menu bar, choose one of the following:




	* To run the code with the closest matching built-in runner, choose **Run, Run**. If AWS Cloud9
	cannot find one, this command is disabled.
	* To run the code with the run configuration that AWS Cloud9 last used, choose **Run, Run Last**.
	* To run the code with a specific runner, choose **Run, Run With**, and then choose the name
	of the runner. If the runner you want to use isn't listed,
	stop this procedure, complete the steps in [Create a Builder or Runner](#build-run-debug-create-builder-runner "#build-run-debug-create-builder-runner"), and then return to this procedure.
	* To run the code with a specific runner with a custom combination of file name, command line options, debug mode, current working directory, and environment
	variables, choose **Run, Run Configurations**, and then choose the run configuration's name.
	In the run configuration tab that is displayed, choose
	**Runner: Auto**, choose the runner you want to use, and then choose **Run**. If
	the runner you want to use isn't listed, stop this procedure,
	complete the steps in [Create a Builder or Runner](#build-run-debug-create-builder-runner "#build-run-debug-create-builder-runner"), and then return to this procedure.

## Debug Your Code



1. On the run configuration tab for your code, choose **Run in Debug Mode**. The bug icon turns to green on a white background. For more information,
see [Run Your Code](#build-run-debug-run "#build-run-debug-run") and [Create a Run Configuration](build-run-debug-create-run-config.md "build-run-debug-create-run-config.md").
2. Set any breakpoints in your code you want to pause at during the run, as follows:




	1. Open each file that you want to set a breakpoint in.
	2. At each point in a file where you want to set a breakpoint, choose the blank area in the gutter
	to the left of the line number. A red circle appears.
	
	
	To remove a breakpoint, choose the existing breakpoint in the gutter.
	
	
	To disable a breakpoint instead of removing it, in the **Debugger** window, in **Breakpoints**, clear the box that corresponds
	to the breakpoint you want to disable. To enable the breakpoint again, select the box you cleared.
	
	
	To disable all breakpoints at once, in the **Debugger** window, choose **Deactivate All Breakpoints**. To enable all breakpoints again,
	choose **Activate All Breakpoints**.
	
	
	If the **Debugger** window isn't visible, choose the **Debugger** button. If the
	**Debugger** button isn't visible,
	on the menu bar choose **Window**, **Debugger**.
3. Set any watch expressions for which you want to get the value at the point where a run pauses, as follows:




	1. In the **Debugger** window, in **Watch Expressions**, choose **Type an expression here**.
	2. Type the expression you want to watch, and then press `Enter`.
	
	
	To change an existing watch expression, right-click the watch expression, and then choose **Edit Watch Expression**. Type the change, and then press `Enter`.
	
	
	To remove an existing watch expression, right-click the watch expression, and then choose **Remove Watch Expression**.
4. Run your code as described in [Run Your Code](#build-run-debug-run "#build-run-debug-run").

Whenever a run pauses, you can also pause your pointer on any displayed piece of code (for example,
a variable) to show any available information about it in a tooltip.


## Create a Builder or Runner


This step shows how you can create your own builder or runner.



1. To create a builder, on the menu bar, choose **Run, Build System, New Build System**. To create a runner, on the menu bar,
choose **Run, Run With, New Runner**.
2. On the builder tab (labeled **My Builder.build**) or runner tab (labeled **My Runner.run**)
that is displayed, define the builder or runner.
See [Define a Builder or Runner](build-run-debug-define-builder-runner.md "build-run-debug-define-builder-runner.md").
3. After you define the builder or runner, choose **File, Save As**.
 For a builder, save the file with the `.build` extension in the
 `my-environment/.c9/builders` directory, where
 `my-environment` is the name of your environment. For a runner, save
 the file with the `.run` file extension in the
 `my-environment/.c9/runners` directory, where
 `my-environment` is the name of your environment. The file name you
 specify will be the name that is displayed on the **Run, Build
 System** menu (for a builder) or the **Run, Run With**
 menu (for a runner). Therefore, unless you specify a different file name, by default
 the display name will be **My Builder** (for a builder) or
 **My Runner** (for a runner).

To use this builder or runner, see [Build Your Project's Files](#build-run-debug-build "#build-run-debug-build") or [Run Your Code](#build-run-debug-run "#build-run-debug-run").


###### Note

Any builder or runner you create applies only to the environment you created that builder or runner in. To add that run builder or runner to a separate environment,
open the other environment, and then follow the preceding steps to create the same builder or runner in that environment.
