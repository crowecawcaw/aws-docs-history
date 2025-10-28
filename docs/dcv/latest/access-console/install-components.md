# Step 3: Install the

components

After preparing the Handler, Web Client, and Authentication Server components, you
must install them on the hosts you prepared.

## Installing the

Handler

###### RHEL, CentOS, Amazon Linux

1. Connect to the host you set up for the Handler.
2. Move the Handler `.rpm` you downloaded to the host in
   _Step 1: Prepare your environment_.
3. Move the `access-console-handler.properties` and
   `access-console-handler-secrets.properties` files created
   by the Setup Wizard to the host.
4. Install the Handler component.

```
`$` sudo yum install -y nice-dcv-access-console-handler*.rpm
```

5. Move the two `.properties` files to
   `/etc/dcv-access-console-handler/` and overwrite the
   existing files.

```
`$` sudo mv -f access-console-handler.properties /etc/dcv-access-console-handler/access-console-handler.properties
```

```
`$` sudo mv -f access-console-handler-secrets.properties /etc/dcv-access-console-handler/access-console-handler-secrets.properties
```

6. Do one of the following:
   - If you chose to use DynamoDB as the database, make sure that
     the instance has permission to access DynamoDB via the [Credential Provider Chain](../../../sdkref/latest/guide/standardized-credentials.md#credentialProviderChain "../../../sdkref/latest/guide/standardized-credentials.md#credentialProviderChain"), and then skip to the
     last step.
   - If you chose to use MariaDB, you must prepare the database by
     continuing to the next step.

7. Install MariaDB by doing one of the following:
   - For Amazon Linux 2023

   ```
   `$` sudo yum install -y mariadb105-server
   ```

   - For RHEL and CentOS

   ```
   `$` sudo yum install -y mariadb-server
   ```

8. Start and enable MariaDB.

```
`$` sudo systemctl start mariadb
```

```
`$` sudo systemctl enable mariadb
```

9. Set the **username**, **password**,
   and **database name** from the previous step.

```
MARIADB_USERNAME=`replace with username`
MARIADB_PASSWORD=`replace with password`
DATABASE_NAME=`replace with database name`
```

10. Create a new MariaDB user.

```
`$` sudo mysql -e "CREATE USER '$MARIADB_USERNAME'@'localhost' IDENTIFIED BY '${MARIADB_PASSWORD}'"
```

11. Create a new MariaDB database.

```
`$` sudo mysql -e "CREATE DATABASE $DATABASE_NAME;"
```

12. Grant the user full privileges on the database.

```
`$` sudo mysql -e "GRANT ALL PRIVILEGES ON $DATABASE_NAME.* TO '$MARIADB_USERNAME'@'localhost';"
```

13. Start and enable the Handler component.

```
`$` sudo systemctl start nice-dcv-access-console-handler
```

```
`$` sudo systemctl enable nice-dcv-access-console-handler
```

###### Ubuntu, Debian

1. Connect to the host you set up for the Handler.
2. Move the Handler `.deb` file you downloaded to the host in
   _Step 1: Prepare your environment_.
3. Move the `session-manager-handler.properties` and
   `session-manager-handler-secrets.properties` files
   created by the Setup Wizard to the host.
4. Install the Handler component.

```
`$` sudo apt install -y nice-dcv-access-console-handler*.deb
```

5. Move the two `.properties` files to
   `/etc/nice-dcv-access-console-handler/` and overwrite the
   existing files.

```
`$` sudo mv -f access-console-handler.properties /etc/dcv-access-console-handler/access-console-handler.properties
```

```
`$` sudo mv -f access-console-handler-secrets.properties /etc/dcv-access-console-handler/access-console-handler-secrets.properties
```

6. Do one of the following:
   - If you chose to use DynamoDB as the database, make sure that
     the instance has permission to access DynamoDB via the [Credential Provider Chain](../../../sdkref/latest/guide/standardized-credentials.md#credentialProviderChain "../../../sdkref/latest/guide/standardized-credentials.md#credentialProviderChain"), and then skip to the
     last step.
   - If you chose to use MariaDB, you must prepare the database by
     continuing to the next step.

7. Install MariaDB.

```
`$` sudo apt install -y mariadb-server
```

8. Start and enable MariaDB.

```
`$` sudo systemctl start mariadb
```

```
`$` sudo systemctl enable mariadb
```

9. Set the **username**, **password**,
   and **database name** from the previous step.

```
MARIADB_USERNAME=`replace with username`
MARIADB_PASSWORD=`replace with password`
DATABASE_NAME=`replace with database name`
```

10. Create a new MariaDB user.

```
`$` sudo mysql -e "CREATE USER '$MARIADB_USERNAME'@'localhost' IDENTIFIED BY '${MARIADB_PASSWORD}'"
```

11. Create a new MariaDB database.

```
`$` sudo mysql -e "CREATE DATABASE $DATABASE_NAME;"
```

12. Grant the user full privileges on the database.

```
`$` sudo mysql -e "GRANT ALL PRIVILEGES ON $DATABASE_NAME.* TO '$USERNAME'@'localhost';"
```

13. Start and enable the Handler component.

```
`$` sudo systemctl start dcv-access-console-handler
```

```
`$` sudo systemctl enable dcv-access-console-handler
```

## Installing the

Authentication Server

###### RHEL, CentOS, Amazon Linux

1. Connect to the host you set up for the Authentication Server.
2. Move the Authentication Server `.rpm` you downloaded in
   Step 1: Prepare your environment.
3. Move the `session-manager-auth-server.properties` and
   `session-manager-auth-server-secrets.properties` files
   created by the Setup Wizard to the host.
4. Install the Authentication Server component.

```
`$` sudo yum install -y nice-dcv-access-console-auth-server*.rpm
```

5. Move the two `.properties` files to
   `/etc/dcv-access-console-auth-server/` and overwrite the
   existing files.

```
`$` sudo mv -f access-console-auth-server.properties /etc/dcv-access-console-auth-server/access-console-auth-server.properties
```

```
`$` sudo mv -f access-console-auth-server-secrets.properties /etc/dcv-access-console-auth-server/access-console-auth-server-secrets.properties
```

6. Start and enable the Authentication Server.

```
`$` sudo systemctl start dcv-access-console-auth-server
```

```
`$` sudo systemctl enable dcv-access-console-auth-server
```

###### Ubuntu, Debian

1. Connect to the host you set up for the Authentication Server.
2. Move the Authentication Server `.deb` you downloaded to the
   host in _Step 1: Prepare your environment_.
3. Move the `access-console-auth-server.properties` and
   `access-console-auth-server-secrets.properties` files
   created by the Setup Wizard to the host.
4. Install the Authentication Server component.

```
`$` sudo apt install -y nice-dcv-access-console-auth-server*.deb
```

5. Move the two `.properties` files to
   `/etc/dcv-access-console-auth-server/` and overwrite the
   existing files.

```
`$` sudo mv -f access-console-auth-server.properties /etc/dcv-access-console-auth-server/access-console-auth-server.properties
```

```
`$` sudo mv -f access-console-auth-server-secrets.properties /etc/dcv-access-console-auth-server/access-console-auth-server-secrets.properties
```

6. Start and enable the Authentication Server.

```
`$` sudo systemctl start dcv-access-console-auth-server
```

```
`$` sudo systemctl enable dcv-access-console-auth-server
```

## Installing the Web

Client

###### RHEL, CentOS, Amazon Linux

1. Connect to the host you set up for the Web Client.
2. Move the Web Client `.rpm` you downloaded to the host in
   _Step 1: Prepare your environment_.
3. Move the `access-console-webclient.properties` and
   `access-console-webclient-secrets.properties` files created by the Setup Wizard to
   the host.
4. Move the `dcv-access-console.conf` file created by the
   Setup Wizard to the host.
5. Install the Web Client component.

```
`$` sudo yum install -y nice-dcv-access-console-webclient*.rpm
```

6. Move the two `.properties` files to
   `/etc/dcv-access-console-webclient/` and overwrite the
   existing files.

```
`$` sudo mv -f access-console-webclient.properties /etc/dcv-access-console-webclient/access-console-webclient.properties
```

```
`$` sudo mv -f access-console-webclient-secrets.properties /etc/dcv-access-console-webclient/access-console-weblcient-secrets.properties
```

7. Install NGINX.

```
`$` sudo yum install -y nginx
```

8. Move the `dcv-access-console.conf` file to
   `/etc/nginx/conf.d/dcv-access-console.conf`.

```
`$` sudo mv dcv-access-console.conf /etc/nginx/conf.d/dcv-access-console.conf
```

9. Change the permissions to match the default NGINX configuration
   file.

```
`$` sudo chmod --reference=/etc/nginx/nginx.conf /etc/nginx/conf.d/dcv-access-console.conf
```

```
`$` sudo chown --reference=/etc/nginx/nginx.conf /etc/nginx/conf.d/dcv-access-console.conf
```

10. If you are using SELinux, change the SELinux context to match the
    default NGINX configuration file.

```
`$` sudo chcon --reference=/etc/nginx/nginx.conf /etc/nginx/conf.d/dcv-access-console.conf
```

11. Start and enable the Web Client.

```
`$` sudo systemctl start dcv-access-console-ui-webclient
```

```
`$` sudo systemctl enable dcv-access-console-ui-webclient
```

12. Start and enable NGINX.

```
`$` sudo systemctl start nginx
```

```
`$` sudo systemctl enable nginx
```

###### Note

If you are using SELinux on the host, you need to enable the
`httpd_can_network_connect bool` in order for NGINX to
forward requests. To do this, run:

```
`$` sudo setsebool -P httpd_can_network_connect 1
```

###### Ubuntu, Debian

1. Connect to the host you set up for the Web Client.
2. Move the Web Client `.deb` you downloaded to the host in
   _Step 1: Prepare your environment_.
3. Move the `access-console-webclient.properties` and
   `access-console-webclient-secrets.properties` files created by the Setup Wizard to
   the host.
4. Move the `dcv-access-console.conf` file created by the
   Setup Wizard to the host.
5. Install the Web Client component.

```
`$` sudo apt install -y nice-dcv-access-console-webclient*.deb
```

6. Move the two `.properties` files to
   `/etc/dcv-access-console-webclient/` and overwrite the
   existing files.

```
`$` sudo mv -f access-console-webclient.properties /etc/dcv-access-console-webclient/access-console-webclient.properties
```

```
`$` sudo mv -f access-console-webclient-secrets.properties /etc/dcv-access-console-webclient/access-console-weblcient-secrets.properties
```

7. Install NGINX.

```
`$` sudo apt install -y nginx
```

8. Move the `dcv-access-console.conf` file to
   `/etc/nginx/conf.d/dcv-access-console.conf`.

```
`$` sudo mv dcv-access-console.conf /etc/nginx/conf.d/dcv-access-console.conf
```

9. Start and enable the Web Client.

```
`$` sudo systemctl start dcv-access-console-webclient
```

```
`$` sudo systemctl enable dcv-access-console-webclient
```

10. Start and enable NGINX.

```
`$` sudo systemctl start nginx
```

```
`$` sudo systemctl enable nginx
```
