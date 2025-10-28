# Set up Amazon Connect Agent Workspace

to support agents shifting across AWS Regions

Perform the following steps to enable Amazon Connect Agent Workspace to embed the
Contact Control Panel from the replica AWS Region to the source Region, and
shift between them as agent's active Region changes.

If you have not yet created a replica of your source Amazon Connect instance or set up
a traffic distribution group, see [Get started with Amazon Connect Global
Resiliency](get-started-connect-global-resiliency.md "get-started-connect-global-resiliency.md").

1. Go to the AWS Amazon Connect console to retrieve the **Access
   URL** for your source instance. Make a note of the URL.
2. In the replica Region, AWS Amazon Connect console to retrieve the
   **Access URL** for your replica instance. Make a
   note of the URL.
3. In the same window for your replica Amazon Connect instance, in the left pane
   choose **Approved origins**.
4. Add domain for source instance **Access URL**, which
   you noted in step 1.

###### Note

Do not include a trailing **/** in the access
URL. 5. Repeat the above steps on your source instance: Go to
**Approved origins**, add the access URL for the
replica instance.

###### Note

Agents must set their status to **Available** after they
are shifted across Regions.
