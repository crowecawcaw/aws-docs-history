AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Managing initialization scripts in the

AWS Cloud9 IDE

###### Important

AWS Cloud9 no longer supports the experimental feature that allowed users to
customize an initialization script. This script was automatically run in the IDE. Users can
continue to view, edit, and save the `init.js` file using the editor.
But, customized initialization scripts are no longer permitted to run and can't modify the
IDE's behavior.

If AWS Cloud9 detects that the `init.js` file has been modified, the following
message is displayed in the IDE:

**`Support for initialization scripts has been discontinued. The contents of this init.js file will no longer be executed on loading the AWS Cloud9 IDE.`**

If you need to run a custom initialization script for the IDE, [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

An _initialization script_ defines initialization code to run in your
IDE after all plugins are loaded. This applies across each AWS Cloud9 development environment that's associated with
your IAM user. AWS Cloud9 also continually scans for changes to the initialization script and
alerts users if a modification occurred.

## Open your initialization script

To open your initialization script, on the menu bar, choose **AWS Cloud9**, **Open Your Init Script**.

###### Important

You can edit and save the `init.js` file using the editor, but your
customized script isn't permitted to run in the IDE.
