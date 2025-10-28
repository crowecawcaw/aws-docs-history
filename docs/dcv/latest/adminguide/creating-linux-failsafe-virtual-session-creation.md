# Creating a Failsafe Virtual Session on Linux

A common strategy to verify if the session creation failure is tied to the startup of the desktop environment
consists in creating a minimal session. We will refer to this session as a "failsafe" session. If creating a
failsafe session works correctly, then we can deduce that your normal session fails because the default system
desktop environment fails to start. Conversely, if also the failsafe session fails, then the problem is more
likely to be related to the setup of Amazon DCV server.

A failsafe session typically consists of a desktop session containing only a simple window manager and a
terminal. This allows the user to check in case there are session creation issues related to the specific
session environment in use (typically gnome or KDE).

In order to create a failsafe session, you need to create an init script for the user, containing something as:

```
#!/bin/sh
metacity &
xterm

```

This will start the `metacity` window manager and launch an `xterm` terminal, as soon as the
`xterm` process is terminated the session will also terminate.

You can use another session manager or terminal of your choice provided that it is available on the
system.

###### Note

You must make sure that the script does not terminate immediately. For this you need to have a non
immediately terminating program launched by the end of the script. As the last command is terminated
(`xterm` in the example), the init session is terminated as well. At the same time, when you launch
another tool after the windows manager, you need to make sure it runs in background (by adding the
`&` in the example), to make sure that the next command is called.

Then you need to make sure that the init script is executable:

```
`$` chmod a+x `init.sh`
```

To create the session with the specified init script from the user shell, run this command, where
`init.sh` is the script previously created:

```
`$` dcv create-session dummy --init `init.sh`
```

To create a session for another user as superuser you can run this command instead:

```
`$` sudo dcv create-session test --user `user` --owner `user` --init `init.sh`
```

Finally, you can launch a test application such for example `dcvgltest` (only in case you have the
`nice-dcv-gltest` package installed) or `glxgears` to verify that an OpenGL or any other
application is correctly working.
