# Seeing `cannot change locale (en_US.utf-8) because it has an invalid name` in `slurm_resume.log`

This can occur if you have an unsuccessful `yum` installation process that left the locale settings in an inconsistent state. For
example, this can be caused when a user terminates the install process.

###### To verify the cause, take the following actions:

- Run `su - pcluster-admin`.

The shell shows an error, such as, `cannot change locale...no such file or directory`.

- Run `localedef --list`.

Returns an empty list or doesn't contain the default locale.

- Check the last `yum` command with `yum history` and `yum history info #ID`. Does the last ID have
  `Return-Code: Success`?

If the last ID doesn't have `Return-Code: Success`, the post-install scripts might not have run
successfully.
To fix the issue, try rebuilding the locale with `yum reinstall glibc-all-langpacks`. After the
rebuild, `su - pcluster-admin` doesn't show an error or warning if the issue is fixed.
