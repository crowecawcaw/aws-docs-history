# Disconnect from the EC2 Serial

Console

If you no longer need to be connected to your instance's EC2 Serial Console, you can
disconnect from it. When you disconnect from the serial console, any shell session running on
the instance will continue to run. If you want to end the shell session, you'll need to end it
before disconnecting from the serial console.

###### Considerations

- The serial console connection typically lasts for 1 hour unless you disconnect from
  it. However, during system maintenance, Amazon EC2 will disconnect the serial console
  session.
- It takes 30 seconds to tear down a session after you've disconnected from the serial
  console in order to allow a new session.
  The way to disconnect from the serial console depends on the client.

###### Browser-based client

To disconnect from the serial console, close the serial console in-browser terminal
window.

###### Standard OpenSSH client

To disconnect from the serial console, use the following command to close the SSH
connection. This command must be run immediately following a new line.

```
~.
```

The command that you use for closing an SSH connection might be different depending on the
SSH client that you're using.
