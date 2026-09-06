

# **eb clone**
<a name="eb3-clone"></a>

## Description
<a name="eb3-clonedescription"></a>

Clones an environment to a new environment so that both have identical environment settings.

**Note**  
By default, regardless of the solution stack version of the environment from which you create the clone, the **eb clone** command creates the clone environment with the most recent solution stack. You can suppress this by including the `--exact` option when you run the command.



**Important**  
Cloned Elastic Beanstalk environments do not carry over the security groups for ingress, leaving the environment open to all internet traffic. You’ll need to reestablish ingress security groups for the cloned environment.  
You can see resources that may not be cloned by checking the drift status of your environment configuration. For more information, see [Detect drift on an entire CloudFormation stack ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html) in the *AWS CloudFormation User Guide*.



## Syntax
<a name="eb3-clonesyntax"></a>

 **eb clone** 

 **eb clone {{environment-name}}** 

## Options
<a name="eb3-cloneoptions"></a>



|  Name  |  Description  | 
| --- | --- | 
| `-n` {{string}}<br />or<br />`--clone_name` {{string}} | Desired name for the cloned environment. | 
| `-c` {{string}}<br />or<br />`--cname` {{string}} | Desired CNAME prefix for the cloned environment. | 
| `--envvars` | Environment properties in a comma-separated list with the format {{name}}={{value}}.<br />Type: String<br />Constraints:+  Key-value pairs must be separated by commas. <br />+  Keys and values can contain any alphabetic character in any language, any numeric character, white space, invisible separator, and the following symbols: \_ . : / \+ \\ - @ <br />+  Keys can contain up to 128 characters. Values can contain up to 256 characters. <br />+  Keys and values are case sensitive. <br />+  Values cannot match the environment name. <br />+  Values cannot include either `aws:` or `elasticbeanstalk:`. <br />+  The combined size of all environment properties cannot exceed 4096 bytes.  | 
| `--exact` | Prevents Elastic Beanstalk from updating the solution stack version for the new clone environment to the most recent version available (for the original environment's platform). | 
| `--scale` {{number}} | The number of instances to run in the clone environment when it is launched. | 
| `--tags` {{name}}={{value}} | [Tags](using-features.tagging.md) for the resources in your environment in a comma-separated list with the format {{name}}={{value}}. | 
| `--timeout` | The number of minutes before the command times out. | 
| [Common options](eb3-cmd-options.md) |  | 

## Output
<a name="eb3-cloneoutput"></a>

If successful, the command creates an environment that has the same settings as the original environment or with modifications to the environment as specified by any **eb clone** options.

## Example
<a name="eb3-cloneexample"></a>

The following example clones the specified environment.

```
$ eb clone
Enter name for Environment Clone
(default is tmp-dev-clone):
Enter DNS CNAME prefix
(default is tmp-dev-clone):
Environment details for: tmp-dev-clone
  Application name: tmp
  Region: us-west-2
  Deployed Version: app-141029_144740
  Environment ID: e-vjvrqnn5pv
  Platform: 64bit Amazon Linux 2014.09 v1.0.9 running PHP 5.5
  Tier: WebServer-Standard-1.0
  CNAME: tmp-dev-clone.elasticbeanstalk.com
  Updated: 2014-10-29 22:00:23.008000+00:00
Printing Status:
2018-07-11 21:04:20    INFO: createEnvironment is starting.
2018-07-11 21:04:21    INFO: Using elasticbeanstalk-us-west-2-888888888888 as Amazon S3 storage bucket for environment data.
...
2018-07-11 21:07:10    INFO: Successfully launched environment: tmp-dev-clone
```