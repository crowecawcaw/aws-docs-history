# Step 2: Run the Setup

Wizard

The Setup Wizard will install the components and dependencies for the Access
Console, and configure a single host to run all of the Access Console components.
For more information on how to use the Setup Wizard see [Using the Setup
Wizard](using-setup-wizard.md "using-setup-wizard.md").

## Running the

Setup Wizard in interactive mode

Interactive mode is the default setup mode for the Amazon DCV Access Console. It
will prompt you for information about the setup, including the DNS entries for
each host, the paths to the certificates, and information about the Broker. The
Wizard will generate the configuration files and save them to your specified
location.

1. Navigate to the folder where you extracted the Amazon DCV Access Console
   components.
2. Run the following command:

```
`$` python3 wizard.py --not-onebox
```

3. Answer the series of questions that appear.

These questions determine how to configure the Access Console.

The Setup Wizard will finish by validating the installation was successful,
then print the resolvable DNS of the host you provided. The Amazon DCV Access Console
will be accessible at that address and any user present on that host will be
able to login.

## Running

the Setup Wizard in non-interactive mode

Noninteractive mode is the manual setup mode for the Amazon DCV Access Console.
This setup allows more configuration in your setup process. You will need to
manually fill in the JSON file. For more information on modifying JSON
parameters, see [Loading a
JSON file](using-setup-wizard.md#loading-json-file "using-setup-wizard.md#loading-json-file").

1. Go to the file `wizard_input.json`. This is the JSON file
   provided with the Wizard.
2. Modify the following parameters:
   - `handler-address`– The resolvable DNS of the
     host that the Handler will be installed on.
   - `webclient-address`– The resolvable DNS of the
     host that the Webclient will be installed on.
   - `auth-server-address`– The resolvable DNS of the
     host that the Authentication Server will be installed on.
   - `broker-address`– The resolvable DNS of the host
     that the Broker is running on.
   - `broker-client-id`– The Broker Client ID
     that was registered.
   - `broker-client-password`– The Broker Client
     Password that was registered.
   - `show-cookie-link`– If you want to display a
     link to a cookie disclaimer on the sign-in page, set this
     parameter to `true`.
   - `cookie-link-target`– Set this to the link
     you want your users to follow for the cookie disclaimer. If you
     set `show-cookie-link` to `false`, leave
     it as is.
   - `show-privacy-link`– If you want to display
     a link to a privacy disclaimer on the sign in page, set this
     parameter to true `true`.
   - `privacy-link-target`– Set this to the link
     you want your users to follow for the privacy disclaimer. If you
     set `show-privacy-link` to `false`, leave
     it as is.
   - `handler-keystore-password`– The password
     used by the keystore on the Handler host. Leave it as
     `changeit` unless you have changed it.
   - `handler-keystore-path`– The path to the
     keystore file on the Handler host.
   - `auth-server-keystore-password`– The
     password used by the keystore on the Authentication Server host.
     Leave it as `changeit` unless you have changed
     it.
   - `auth-server-keystore-path`– The path to the
     keystore file on the Handler host.
   - `webclient-cert-path`– The path to the certificate on the Webclient
     host.
   - `webclient-cert-key-path`– The path to the
     certificate key on the Webclient host.
   - `pam-service-name`– The name of the service
     to use for PAM authentication on the Authentication Server host.
     If you are installing on a RedHat-based host, use
     `system-auth`. If you are using Ubuntu/Debian,
     use `common-auth`.
   - `mariadb-username`– The username of the
     MariaDB user you created in Step 1 (if you choose MariaDB as
     your datastore).
   - `mariadb-password`– The password you chose
     for the MariaDB user you created in Step 1 (if you choose
     MariaDB as your datastore).
