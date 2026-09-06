

# Use line magics
<a name="notebooks-spark-magics-line-magics"></a>

Magics that are on a single line are preceded by a percent sign (`%`) and are called line magic functions or line magics.

## %help
<a name="notebooks-spark-magics-help"></a>

Displays descriptions of the available magic commands.

![Using %help.](http://docs.aws.amazon.com/athena/latest/ug/images/notebooks-spark-magics-2.png)


## %list\_sessions
<a name="notebooks-spark-magics-list_sessions"></a>

Lists the sessions associated with the notebook. The information for each session includes the session ID, session status, and the date and time that the session started and ended.

![Using %list_sessions.](http://docs.aws.amazon.com/athena/latest/ug/images/notebooks-spark-magics-3.png)


## %session\_id
<a name="notebooks-spark-magics-session_id"></a>

Retrieves the current session ID.

![Using session_id.](http://docs.aws.amazon.com/athena/latest/ug/images/notebooks-spark-magics-4.png)


## %set\_log\_level
<a name="notebooks-spark-magics-set_log_level"></a>

Sets or resets the logger to use the specified log level. Possible values are `DEBUG`, `ERROR`, `FATAL`,`INFO`, and `WARN` or `WARNING`. Values must be uppercase and must not be enclosed in single or double quotes.

![Using %set_log_level.](http://docs.aws.amazon.com/athena/latest/ug/images/notebooks-spark-magics-5.png)


## %status
<a name="notebooks-spark-magics-status"></a>

Describes the current session. The output includes the session ID, session state, workgroup name, PySpark engine version, and session start time. This magic command requires an active session to retrieve session details.

Following are the possible values for status:

**CREATING** – The session is being started, including acquiring resources.

**CREATED** – The session has been started.

**IDLE** – The session is able to accept a calculation.

**BUSY** – The session is processing another task and is unable to accept a calculation.

**TERMINATING** – The session is in the process of shutting down.

**TERMINATED** – The session and its resources are no longer running.

**DEGRADED** – The session has no healthy coordinators.

**FAILED** – Due to a failure, the session and its resources are no longer running.

![Using %status.](http://docs.aws.amazon.com/athena/latest/ug/images/notebooks-spark-magics-6.png)
