NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Manage applications

The **Actions** menu allows you to perform actions on
selected applications.

###### Note

An application must have **all** of its
associated servers in the correct lifecycle for the desired action, otherwise it
will be excluded.

The **Actions** menu allows you to perform the
following actions:

- **Launch test instances** – Choose this option
  to launch test instances for this application servers.
- **Mark as "Ready for cutover"** – Choose this
  option to finalize testing for this application after you have completed all
  the necessary tests in preparation for cutover.

The **Mark servers as "Ready for cutover"**
dialog will appear. Select whether you want to terminate the launched
instances used for testing. It is recommended to terminate these instances,
as you will be charged for them even though you will no longer need them.
Check the **Yes, terminate launched instances
(recommended)** box and choose **Continue**.

- **Revert to "ready for testing"** – Choose this
  option to revert a finalized test for this application if you want to run
  further tests prior to initiating a cutover.

The **Revert testing** dialog will appear.
Select whether you want to terminate the launched instances used for
testing. It is recommended to terminate these instances, as you will be
charged for them even though you will no longer need them. Check the
**Yes, terminate launched instances
(recommended)** box and choose **Revert**.

- **Launch cutover instances** – Choose this
  option to launch cutover instances for this application servers after you
  have finalized all of your testing and are ready to initiate a cutover.
- **Finalize cutover** – Choose this option to
  finalize the cutover for this application servers after you have
  successfully performed a cutover.

###### Note

This action does not uninstall the AWS Replication Agent from the
source servers. When you have completed the migration and want to
uninstall the agent from your source servers, go to **Source servers** page and select the relevant
servers. Use the **Disconnect from
service** option under the **Actions** menu.

- **Revert to "ready for cutover"** – Choose this
  option to revert a finalized cutover for this application if you encounter
  any issues or want to reverse the cutover for any reason.
- **Start data replication** – Choose this option
  to start replicating the application source servers.

###### Note

This action is applicable if all the application associated servers
are **Agentless snapshot based** and are
in **Discovered** lifecycle state.

- **Add applications to wave** – Choose this
  option to associate the selected applications to a wave.
- **Archive applications** – Choose this option
  to archive the selected applications. You should only archive applications
  for which you have already performed a cutover.

###### Important

An application can be archived only if all servers that compose it are
in one of these states: archived, cutover, or disconnected. If that is
the case, the application will be archived and the servers that are not
yet archived (but can be) will also be archived.

Archived applications will be removed from the main applications page,
but can still be accessed through the selector options.
