# Troubleshoot Lightsail Connect errors

This guide explains the error codes you might see when connecting to a Lightsail instance
through the browser and what you can do to connect again. Find the error code you encountered in
the list below, and work through its steps.

## 512 (SERVER\_ERROR)

**What it means:** An unexpected error occurred and the
connection could not be completed.

**Likely cause:** An intermittent network or internet issue,
or a connection reset.

**What to do:**

- Ensure your internet connection is stable.
- Refresh the Lightsail Connect session.

## 514 (UPSTREAM\_TIMEOUT)

**What it means:** The connection timed out while waiting
for a response.

**Likely cause:** A network interruption during the
connection.

**What to do:**

- Ensure your internet connection is stable.
- Refresh the Lightsail Connect session.

## 515 (UPSTREAM\_ERROR)

**What it means:** The connection to your instance could
not be completed.

**Likely cause:** Your instance is low on resources or
still starting up and not ready to connect. It can also happen when your instance's firewall
rules block SSH/RDP. For more information about firewall rules, see
[Control instance traffic with firewalls in Lightsail](understanding-firewall-and-port-mappings-in-amazon-lightsail.md "understanding-firewall-and-port-mappings-in-amazon-lightsail.md").

**What to do:**

- If the instance was recently started or rebooted, wait a short time for the instance
  to be ready to connect, then try again.
- Verify your instance's firewall rules allow SSH/RDP from Lightsail Connect.

  - If a required rule is missing, add it by following these instructions:
    [Add firewall rules to Lightsail instances](amazon-lightsail-editing-firewall-rules.md "amazon-lightsail-editing-firewall-rules.md")
  - Retry the connection after adding the required rule.

- Reboot the instance following these instructions, then try again:
  [Start, stop, or reboot your Lightsail instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md "lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md")

## 516 (RESOURCE\_NOT\_FOUND)

**What it means:** Lightsail Connect cannot find your
instance.

**Likely cause:** Your instance may have been deleted, or
there is a temporary problem reaching it.

**What to do:**

- Confirm the instance still exists in the Lightsail console. If it was deleted,
  connect to a different instance.
- Wait a moment, then try connecting again.
- Check your instance's state in the Lightsail console. If it is still starting, wait
  until it is running, then try again. If it is stopped, start it and wait until it is
  running before connecting.
  [Start, stop, or reboot your Lightsail instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md "lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md")
- Reboot the instance, then reconnect.

## 519 (UPSTREAM\_NOT\_FOUND)

**What it means:** Lightsail could not reach your
instance.

**Likely cause:** The instance is not reachable, most often
because it is still starting up or is not yet responding.

**What to do:**

- If the instance recently started or restarted, wait a few minutes for it to finish
  starting, then try connecting again.
- Confirm the instance is running in the Lightsail console.

## 521 (SESSION\_CONFLICT)

**What it means:** Your session ended because another
session took over. Only one RDP session is allowed at a time.

**Root cause:** A second RDP session was opened to the same
instance, for example in another browser tab, and it took over from the first.

**What to do:**

- Close the session you do not want to use, then reconnect in the one you want to
  keep.
- Avoid opening multiple RDP sessions to the same Windows instance.

## 523 (SESSION\_CLOSED)

**What it means:** The session on your instance ended, so
the connection was closed.

**Likely cause:** Most commonly the instance was rebooted
or stopped. It can also be caused by the session being logged off.

**What to do:**

- If the instance is rebooting or stopping, wait for it to finish, then reconnect.
- If the instance remains unresponsive, reboot it and try again.
  [Start, stop, or reboot your Lightsail instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md "lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md")

## 524 (UPSTREAM\_NLA\_AUTHENTICATION\_FAILURE)

**What it means:** RDP authentication failed. The password
provided was rejected by your instance. You will typically see an "Invalid password"
message.

**Likely cause:** The instance password was changed and
the entered credentials no longer match.

**What to do:**

- Re-enter the correct current password for the instance.

  - If you recently changed the password, use the new one.

## 525 (CONNECTION\_DEADLINE\_EXCEEDED)

**What it means:** You reached the maximum amount of time
Lightsail Connect allows for a single session, so Lightsail Connect closed the connection
to your instance.

**Root cause:** The session reached the connection time
limit set by Lightsail Connect.

**What to do:**

- Reconnect to start a new session.

## 767 (UPSTREAM\_HOSTKEY\_MISMATCH)

**What it means:** The SSH host key presented by your
instance does not match the host key we have on file.

**Likely cause:** The SSH host key on the instance changed,
for example when keys were regenerated or manually changed.

**What to do:**

- If you recently made changes to your instance and expected its host key to change,
  this is expected. In the dialog, choose **Reset record** to update the
  host key Lightsail has on file; the connection then resumes automatically.
- If the dialog asks you to try again later, wait a few minutes, then reconnect.

## 768 (CLIENT\_BAD\_REQUEST)

**What it means:** The connection could not be started
because the request was not valid.

**Likely cause:** This is usually a temporary or
browser-side problem, not something wrong with your instance.

**What to do:**

- Refresh the browser tab and start the connection again from the instance's connect
  page.
- If the instance recently started or changed state, wait a minute or two, then try
  again.
  [Start, stop, or reboot your Lightsail instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md "lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md")

## 769 (CLIENT\_UNAUTHORIZED)

**What it means:** Authentication to the instance failed.
The SSH key presented was rejected by your instance.

**Likely cause:** You might see this shortly after an
instance is created, before the instance is ready to accept Lightsail Connect
sessions.

**What to do:**

- If you recently created or started the instance, wait a few minutes, then try
  connecting again.

## 771 (CLIENT\_FORBIDDEN)

**What it means:** Access to the connection was denied.

**Likely cause:** Usually a transient permission issue.

**What to do:**

- Wait a moment and try connecting again.

## 776 (CLIENT\_TIMEOUT)

**What it means:** Your browser stopped responding to the
Lightsail Connect server, so the connection was closed.

**Likely cause:** The browser throttled or froze the
background tab/window, which is common when the tab is minimized or left in the
background.

**What to do:**

- Keep the connection tab active and in the foreground.
- Reconnect to resume your session.
- Avoid letting the browser suspend the tab during long sessions.

## 797 (CLIENT\_TOO\_MANY)

**What it means:** You have opened too many concurrent
sessions. The maximum is five SSH sessions and one RDP session per instance.

**Root cause:** Opening additional sessions beyond the
allowed limit.

**What to do:**

1. Close existing sessions before opening new ones.
2. Ensure you stay within five SSH / one RDP session per instance.
