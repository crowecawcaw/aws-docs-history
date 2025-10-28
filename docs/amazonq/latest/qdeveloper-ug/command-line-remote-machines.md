# Setting up SSH for remote use

After installing Amazon Q CLI, you can configure remote Linux integration to enable command line functionality with Amazon Q on remote machines.

## Local macOS Integration

To enable SSH integration from your local macOS machine:

1. Open your terminal or command prompt.
2. Enable the local SSH integrations:

```
q integrations install ssh
```

## Remote Linux Integration

To configure the SSH integration on your remote Linux machine:

1. Edit your SSH server configuration:

```
sudo -e /etc/ssh/sshd_config
```

2. Add the following lines to the end of the config file:

```
AcceptEnv Q_SET_PARENT
AllowStreamLocalForwarding yes
```

3. Restart the SSH service:

```
sudo systemctl restart sshd
```

4. Disconnect from the SSH session and reconnect.
5. After reconnecting, log in to Amazon Q:

```
q login
```

6. Verify the installation:

```
q doctor
```

## Known limitations

If the Amazon Q desktop client quits while connected to a remote machine with SSH, an error message may print repeatedly:

```
connect to /var/folders/tg/u1vx4xfmvqav0oxfa4zfknaxiwmbsbr/T/cwrun/remote.sock port -2 failed: Connection refused
```

To stop the error, either exit the SSH session and reconnect or restart the Amazon Q desktop client.

## Troubleshooting

If you encounter issues with the SSH integration:

1. Run **q doctor** to identify and fix common issues
2. Ensure both local and remote configurations are correct
3. Check that your SSH server is properly configured to accept the required environment variables
4. Verify that you're using the correct version (standard or musl) for your system
