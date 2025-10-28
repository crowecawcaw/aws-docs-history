End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Debugging local simulations

You can debug your SimSpace Weaver Local apps with Microsoft Visual Studio.
For more information about how to debug with Visual Studio, see the
[Microsoft
Visual Studio documentation.](https://learn.microsoft.com/en-us/visualstudio/debugger/debugger-feature-tour "https://learn.microsoft.com/en-us/visualstudio/debugger/debugger-feature-tour")

###### To debug your local simulation

1. Make sure that your `schema.yaml` is in your working directory.
2. In **Visual Studio**, open the context
   menu for each app that you want to debug (such as `PathfindingSampleLocalSpatial` or
   `PathfindingSampleLocalView`) and set the working directory in the debugging section.
3. Open the context menu for the app you want to debug and select **Set as Startup project**.
4. Choose **F5** to start debugging the app.

The requirements to debug a simulation are the same as the requirements to run a simulation normally.
You must start the number of spatial apps specified in the schema. For example, if your schema specifies a
2x2 grid and you start a spatial app in debug mode, the simulation will not run until you start 3 more
spatial apps (in debug mode or not in debug mode).

To debug a custom app, you must first start your spatial apps and then start the custom app in the debugger.

Note that your simulation runs in lock step. As soon as an app reaches a breakpoint, all other apps will pause.
After you continue from that breakpoint, the other apps will continue.
