NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Starting a cutover

To launch a cutover instance for a single source server or multiple source servers, go to
the **Source servers** page and check the box to the left of each
server you want to cutover.

Open the **Test and cutover** menu.

Under **Cutover**, choose the **Launch
cutover instances** option.

The **Launch cutover instances for X** servers dialog appears. Choose **Launch** to begin the cutover.

In the **Source servers** page, the **Migration lifecycle** column shows **Cutover in
progress** and the **Next step** column shows
**Finalize cutover**.

The AWS Application Migration Service console indicates **Launch job started**
when the cutover has started.

Choose **View job details** on the dialog to view the specific
job for the cutover launch in the **Launch history** tab.

## Successful cutover launch indicators

You can tell that the cutover instance launch was started successfully through several
indicators on the **Source servers** page.

1. The **Alerts** column displays **Launched**.
2. The **Migration lifecycle** column displays **Cutover in progress**.
3. The **Data replication status** displays **Healthy**.
4. The **Next step column** displays **Finalize cutover**.
