# Use line magics

Magics that are on a single line are preceded by a percent sign (`%`) and
are called _line magic functions_ or _line
magics_.

## %help

Displays descriptions of the available magic commands.

![Using %help.](images/notebooks-spark-magics-2.png)

## %list_sessions

Lists the sessions associated with the notebook. The information for each session
includes the session ID, session status, and the date and time that the session
started and ended.

![Using %list_sessions.](images/notebooks-spark-magics-3.png)

## %session_id

Retrieves the current session ID.

![Using session_id.](images/notebooks-spark-magics-4.png)

## %set_log_level

Sets or resets the logger to use the specified log level. Possible values are
`DEBUG`, `ERROR`, `FATAL`,`INFO`,
and `WARN` or `WARNING`. Values must be uppercase and must not
be enclosed in single or double quotes.

![Using %set_log_level.](images/notebooks-spark-magics-5.png)

## %status

Describes the current session. The output includes the session ID, session state,
workgroup name, PySpark engine version, and session start time. This magic command
requires an active session to retrieve session details.

Following are the possible values for status:

CREATING – The session is being started,
including acquiring resources.

CREATED – The session has been
started.

IDLE – The session is able to accept a
calculation.

BUSY – The session is processing another
task and is unable to accept a calculation.

TERMINATING – The session is in the process
of shutting down.

TERMINATED – The session and its resources
are no longer running.

DEGRADED – The session has no healthy
coordinators.

FAILED – Due to a failure, the session and
its resources are no longer running.

![Using %status.](images/notebooks-spark-magics-6.png)
