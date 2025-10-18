AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Create a Run Configuration

This step shows how you can a runner to run (and optionally, to debug) your code with a custom combination of file name, command line options, 
 debug mode, current working directory, and environment variables.

On the menu bar, choose **Run, Run Configurations, New Run Configuration**. On the run configuration
tab that is displayed, do the following:


1. In the box next to **Run** and **Restart**, type the name that will display on the **Run, Run Configurations** menu for this run configuration.
2. In the **Command** box, type any custom command line options you want to use.
3. To have this run configuration use the runner's predefined debugging settings, choose **Run in Debug Mode**. The bug icon will turn to green on a white background.
4. To have this run configuration use a specific working directory, choose **CWD**, choose the directory to use, and then choose **Select**.
5. To have this run configuration use specific environment variables, choose **ENV**, and then type the name and value of each environment variable.
To use this run configuration, open the file the corresponds to the code you want to run. Choose **Run, Run Configurations** on the menu bar,
and then choose this run configuration's name. In the run configuration tab that displays, choose **Runner: Auto**, choose the runner you want to use,
and then choose **Run**.

###### Note

Any run configuration you create applies only to the environment you created that run configuration in. To add that run configuration to a separate environment,
open the other environment, and then follow the preceding steps to create the same run configuration in that environment.
