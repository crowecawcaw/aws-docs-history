NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Manage selected waves

The **Actions** menu allows you to perform actions on selected
waves.

###### Note

A wave must have **all** of its associated servers in the
correct lifecycle for the desired action, otherwise it will be excluded.

Use this menu to perform the following actions:

- **Launch test instances** – Choose this option to launch test
  instances for this wave servers.
- **Mark as "Ready for cutover"** – Choose this option to finalize
  testing for this wave after you have completed all the necessary tests in preparation for
  cutover.

Once the **Mark servers as "Ready for cutover"** dialog will
appear, select whether you want to terminate the launched instances used for testing. It is
recommended to terminate these instances, as you will be charged for them even though you will
no longer need them. Check the **Yes, terminate launched instances
(recommended)** box and choose **Continue**.

- **Revert to "ready for testing"** – Choose this option to revert
  a finalized test for this wave if you want to run additional tests prior to initiating a
  cutover.

The **Revert testing** dialog will appear. Select whether
you want to terminate the launched instances used for testing. It is recommended to terminate
these instances, as you will be charged for them even though you will no longer need them.
Check the **Yes, terminate launched instances (recommended)** box
and choose **Revert**.

- **Launch cutover instances** – Choose this option to launch
  cutover instances for this wave servers after you have finalized all of your testing and are
  ready to initiate a cutover.
- **Finalize cutover** – Choose this option to finalize the cutover
  for this wave servers after you have successfully performed a cutover.

###### Note

This action does not uninstall the AWS Replication Agent from the source servers. When
you have completed the migration and want to uninstall the agent from your source servers, go
to **Source servers** page and select the relevant servers. Use
the **Disconnect from service** option under the **Actions** menu.

- **Revert to "ready for cutover"** – Choose this option to revert
  a finalized cutover for this wave if you encounter any issues or want to reverse the cutover
  for any reason.
- **Start data replication** – Choose this option to start
  replication of the wave source servers.

###### Note

This action is applicable if all the wave's associated servers are **Agentless snapshot based** and are in **Discovered** lifecycle state.

- **Archive waves** – Choose this option to archive the
  selected waves. You should only archive waves for which you have already performed a
  cutover.

###### Important

A wave can be archived only if all servers that are part of in one of these states:
archived, cutover or disconnected. If that is the case, the wave and its associated
applications will be archived. The servers that are not yet archived (but can be) will also
be archived.

- Archived waves will be removed from the main Waves page, but can still be accessed
  through the selector options.
