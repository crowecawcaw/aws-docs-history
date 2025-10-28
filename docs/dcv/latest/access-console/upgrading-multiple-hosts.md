# Upgrading Amazon DCV Access Console on multiple hosts

To upgrade the Handler, Authentication Server, and Web Client components, you must run the following commands. The components
can be downloaded and extracted using the steps in [Prepare your environment](prepare-environment-multiple.md "prepare-environment-multiple.md").

###### Note

These components need to be downloaded to each host being used.

## Upgrading the Handler

###### RHEL, CentOS, Amazon Linux

1. Connect to the host you set up for the Handler.
2. Move the Handler `.rpm` file you downloaded to the host.
3. Stop the running service.

```
`$`  sudo systemctl stop dcv-access-console-handler
```

4. Upgrade the Handler component.

```
`$`  sudo yum install -y nice-dcv-access-console-handler*.rpm
```

5. Start the Handler component.

```
`$`  sudo systemctl daemon-reload
```

```
`$`  sudo systemctl restart dcv-access-console-handler
```

###### Ubuntu, Debian

1. Connect to the host you set up for the Handler.
2. Move the Handler `.deb` file you downloaded to the host
3. Stop the running service.

```
`$`  sudo systemctl stop dcv-access-console-handler
```

4. Upgrade the Handler component.

```
`$`  sudo apt install -y ./nice-dcv-access-console-handler*.deb
```

5. Start the Handler component.

```
`$`  sudo systemctl daemon-reload
```

```
`$`  sudo systemctl restart dcv-access-console-handler
```

## Upgrading the Authentication Server

###### RHEL, CentOS, Amazon Linux

1. Connect to the host you set up for the Authentication Server.
2. Move the Authentication Server `.rpm` you downloaded to the host.
3. Stop the running service.

```
`$`  sudo systemctl stop dcv-access-console-auth-server
```

4. Upgrade the Authentication Server component.

```
`$`  sudo yum install -y nice-dcv-access-console-auth-server*.rpm
```

5. Start the Authentication Server component.

```
`$`  sudo systemctl daemon-reload
```

```
`$`  sudo systemctl restart dcv-access-console-auth-server
```

###### Ubuntu, Debian

1. Connect to the host you set up for the Authentication Server.
2. Move the Authentication Server `.deb` you downloaded to the host.
3. Stop the running service.

```
`$`  sudo systemctl stop dcv-access-console-auth-server
```

4. Upgrade the Authentication Server component.

```
`$`  sudo apt install -y ./nice-dcv-access-console-auth-server*.deb
```

5. Start the Authentication Server component.

```
`$`  sudo systemctl daemon-reload
```

```
`$`  sudo systemctl restart dcv-access-console-auth-server
```

## Upgrading the Web Client

###### RHEL, CentOS, Amazon Linux

1. Connect to the host you set up for the Web Client.
2. Move the Web Client `.rpm` you downloaded to the host.
3. Stop the running service.

```
`$`  sudo systemctl stop dcv-access-console-web-client
```

4. Upgrade Web Client component.

```
`$`  sudo yum install -y nice-dcv-access-console-web-client*.rpm
```

5. Start the Web Client.

```
`$`  sudo systemctl daemon-reload
```

```
`$`  sudo systemctl restart dcv-access-console-web-client
```

###### Ubuntu, Debian

1. Connect to the host you set up for the Web Client.
2. Move the Web Client `.deb` you downloaded to the host.
3. Stop the running service.

```
`$`  sudo systemctl stop dcv-access-console-web-client
```

4. Uninstall the existing Web Client component.

```
`$`  sudo apt remove -y nice-dcv-access-console-web-client
```

5. Upgrade the Web Client component.

```
`$`  sudo apt install -y ./nice-dcv-access-console-web-client*.deb
```

6. Start the Web Client.

```
`$`  sudo systemctl daemon-reload
```

```
`$`  sudo systemctl restart dcv-access-console-web-client
```
