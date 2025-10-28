# HTTP topic rule destination

overview

An HTTP topic rule destination refers to a web service that supports a
confirmation URL and one or more data collection URLs. The HTTP topic rule
destination resource contains the confirmation URL of your web service. When
you configure an HTTP topic rule action, you specify the actual URL of the
endpoint that should receive the data along with the web service's
confirmation URL. After your destination is confirmed, the topic rule sends
the result of the SQL statement to the HTTPS endpoint (and not to the
confirmation URL).

An HTTP topic rule destination can be in one of the following
states:

ENABLED

The destination has been confirmed and can be used by a rule
action. A destination must be in the `ENABLED` state
for it to be used in a rule. You can only enable a destination
that's in DISABLED status.

DISABLED

The destination has been confirmed but it can't be used by a
rule action. This is useful if you want to temporarily prevent
traffic to your endpoint without having to go through the
confirmation process again. You can only disable a destination
that's in ENABLED status.

IN_PROGRESS

Confirmation of the destination is in progress.

ERROR

Destination confirmation timed out.

After an HTTP topic rule destination has been confirmed and enabled, it
can be used with any rule in your account.

The following sections describe common actions on HTTP topic rule
destinations.
