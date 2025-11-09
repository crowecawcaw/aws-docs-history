Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Stopping a Dev Environment

The `/projects` directory of a Dev Environment stores the files that are pulled
from the source repository and the devfile that is used to configure the Dev Environment. The
`/home` directory, which is empty upon Dev Environment creation, stores the files you
create while using your Dev Environment. Everything in the `/projects` and
`/home` directories of a Dev Environment is stored persistently, so you can stop
working in a Dev Environment if you need to switch to another Dev Environment, repository, or
project.

###### Warning

A Dev Environment will not timeout if any instances, including web browsers, remote shells,
and IDEs, remain connected. So, make sure to close all connected instances to avoid
incurring additional costs.

A Dev Environment will automatically stop if it is idle for the amount of time that was
selected in the **Timeout** fields during Dev Environment creation. You can stop
the Dev Environment before it goes idle. If you chose **No timeout** when you
created your Dev Environment, the Dev Environment will not stop automatically. Instead, it will run
continuously.

###### Warning

If you stop a Dev Environment that's associated with a deleted VPC connection, it can't be resumed.

###### To stop a Dev Environment from the Dev Environments

page

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to stop a Dev Environment.
3. In the navigation pane, choose **Code**.
4. Choose **Dev Environments**.
5. Choose the radio button for the Dev Environment you want to stop.
6. From the **Actions** menu, choose **Stop**.

###### Note

Compute use is billed only while the Dev Environment is running, but storage use is billed
for the entire time that the Dev Environment exists. Stop your Dev Environment when it is not in use
to stop compute billing.
