# Modify your idle shutdown time limit

Users may be able to modify the idle shutdown time limit if the admin gives access when adding
support for idle shutdown. If support for idle shutdown is added, there may be a limit applied to
the maximum time for idle shutdown. A user can set the value anywhere between the lower limit and
upper limit.

1. Launch Amazon SageMaker Studio by following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. From the **Applications** section, select the application type to update
   the idle shutdown time for.
3. Select the space to update.
4. Update **Idle shutdown (mins)** with your desired value.

###### Note

If idle shutdown is set when applications are running, they must be restarted for idle
shutdown settings to take effect.
