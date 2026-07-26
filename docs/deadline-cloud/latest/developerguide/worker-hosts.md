# Secure worker hosts

On customer-managed fleets, you configure the worker host operating system. The
following practices keep the worker agent, queue users, and their data separated from each
other on the host:

- Review host configuration scripts before you use them, and test configuration
  changes before rolling them out to your fleet. An incorrect configuration can make
  workers unstable or stop them from working.
- Don't use the same `jobRunAsUser` value with multiple queues unless
  jobs submitted to those queues are within the same security boundary.
- Don't set the queue `jobRunAsUser` to the name of the OS user that the
  worker agent runs as. For the reason, see [Run jobs as dedicated OS users](job-run-as-user.md "job-run-as-user.md").
- Grant queue users the least-privileged OS permissions required for the intended
  queue workloads. Ensure that they don't have filesystem write permissions to worker
  agent program files or other shared software.
- Ensure that only the root user on Linux, or the `Administrator`
  account on Windows, owns and can modify the worker agent program files.
- On Linux worker hosts, consider configuring a `umask` override in
  `/etc/sudoers` that allows the worker agent user to launch processes as
  queue users. This configuration helps ensure other users can't access files written
  to the queue.
- Restrict permissions to local DNS override configuration files
  (`/etc/hosts` on Linux and `C:\Windows\system32\etc\hosts`
  on Windows), and to route tables on worker host operating systems, so that worker
  traffic to Deadline Cloud can't be redirected.
- Regularly patch the operating system and all installed software. This approach
  includes software specifically used with Deadline Cloud such as submitters, adaptors, worker
  agents, OpenJD packages, and others.
- Use strong passwords for the Windows queue `jobRunAsUser`, and
  rotate the passwords regularly.
- Grant least-privileged access to the Windows password secrets, and delete
  unused secrets.
- Don't give the queue `jobRunAsUser` permission to schedule commands to
  run in the future:

  - On Linux, deny these accounts access to `cron` and
    `at`.
  - On Windows, deny these accounts access to the Windows task
    scheduler.
