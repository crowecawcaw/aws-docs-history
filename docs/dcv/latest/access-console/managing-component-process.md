# Managing the component processes

The Amazon DCV Access Console components, such as Authentication Server, Handler, Web Client,
run while processes on their hosts and can be managed using the command
`systemctl`. You can use this command to:

- Check the status of a component
- Stop a component
- Start a component
- Restart a component
  If your components are running on separate hosts, then each command must be executed on each corresponding host.

## Checking status of the components

To check the statuses of the components, run the following commands on the hosts that the components are installed on.

```
sudo systemctl status dcv-access-console-auth-server
sudo systemctl status dcv-access-console-handler
sudo systemctl status dcv-access-console-webclient
```

## Stopping the components

To stop the component processes, run the following commands on the hosts that the components are installed on.

```
sudo systemctl stop dcv-access-console-auth-server
sudo systemctl stop dcv-access-console-handler
sudo systemctl stop dcv-access-console-webclient
```

## Starting the components

To start the component processes, run the following commands on the hosts that the components are installed on.

```
sudo systemctl start dcv-access-console-auth-server
sudo systemctl start dcv-access-console-handler
sudo systemctl start dcv-access-console-webclient
```

## Restarting the components

To restart the component processes, run the following commands on the hosts that the components are installed on.

```
sudo systemctl restart dcv-access-console-auth-server
sudo systemctl restart dcv-access-console-handler
sudo systemctl restart dcv-access-console-webclient
```
