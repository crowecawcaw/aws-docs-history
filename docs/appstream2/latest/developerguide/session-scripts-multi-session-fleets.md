# Use Session Scripts on Multi-Session Fleets

When using session scripts on multi-session fleets, there are additional
requirements and considerations to ensure optimal performance and security.

## Requirements

On a single-session fleet, for a given instance, the
**SessionStart** and
**SessionTermination** hooks are guaranteed to run only one
time. This is because there is a 1:1 mapping of sessions to instances. When
using multi-session fleets, there is an N:M mapping of sessions to instances,
where each session runs its own **SessionStart** and
**SessionTermination** hook. This means that the
**SessionStart** and
**SessionTermination** hooks can be run many times on a
given instance, and in many different orderings. For the best experience, the
following should be true of your session scripts when used on multi-session
fleets:

- Scripts are idempotent.

When an action has already been performed, scripts should handle more
than one execution on the same instance with graceful handling.

- Scripts are independent.

Because scripts run per session, if one session is running
**SessionTermination** while another is running
**SessionStart**, they should not interfere with
each other, or with the experience of other sessions.

- Scripts are performant.

On multi-session instances, multiple sessions can be provisioned
concurrently. This means that there can be multiple concurrent
executions of the session scripts. Scripts should be efficient, not
consume excessive resources, and not impact the experience of other
users on the instance or the stability of the sessions.

Many of these requirements can be met by keeping session script logic focused
on the specific user session for which the script is running.

## Security Considerations

AppStream 2.0 images should not be configured to allow write permission to session
script files by any users. This introduces a critical attack vector for
malicious users, where they could modify script files. These files could then be
run as SYSTEM or another user, depending on your configuration.

###### Important

It is your responsibility to make sure that your AppStream 2.0 images are
configured securely. This is especially important for multi-session
instances, where multiple users are using the same instance. If images are
not configured securely, there is a security risk for all users of that
instance.

The following should be true of your images and session scripts files:

- Users do not have permission to modify session script files.
- Users do not have permission to modify the session script config.json.
  Default behavior on the image restricts access to administrators.

Session scripts executables should be stored in a secure location where they
are safe from modification at runtime.

If the service detects that a session script executable has been modified, it
will fail any subsequent executions of that hook on that instance, upload log
files to Amazon S3 (if Amazon S3 logging is enabled), and you will see the following
message:

**The session script was not executed because the executable was
modified after instance provisioning. Execution was skipped for
security.**

If your use case requires modifying the session script executable at run time
(for example, if you point to an EXE file which is modified by an automatic
update process at runtime), this will fail the above checks. In this case, use a
script to redirect execution to your modified executable. Leave the script
unmodified at runtime when the service performs security checks.

If your session script files are excessively large (more than 100 MB), this
can cause delays in instance and session provisioning, and the security checks
will take additional time (depending on instance type and available resources).
If your use case requires large session scripts, consider using smaller scripts
to redirect execution. This will improve instance and session provisioning
experiences.

Note that the service is only checking the executable defined in the session
scripts config.json, and this is only a fallback/best effort mechanism. It is
your responsibility to ensure that all code paths in session scripts executables
are secure and cannot be modified by end users.
