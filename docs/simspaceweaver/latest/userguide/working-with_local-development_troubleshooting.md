End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Troubleshooting local development in SimSpace Weaver

- **Linux: xterm command not found / cannot open**
  - The local scripts assume the xterm command exists when running on Linux. If you do not have the xterm command or are running in an environment that does not support GUI, use the `--noappwindow` option when running the quick-start script.

- **No app windows are opening!**
  - This happens when the local simulation crashes immediately. To see the console output after the crash, use the `--noappwindow` or `--logfile` options when running the quick-start script.

- **The simulation isn’t ticking after the view app starts or view client connects!**
  - Running with the `—noappwindow` option typically resolves these kinds of issues. Otherwise, restarting a few times also has success (although at a much lower rate).
