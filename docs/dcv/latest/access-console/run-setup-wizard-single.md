# Step 2: Run the Setup

Wizard

The Setup Wizard will install the components and dependencies for the Access
Console, and configure a single host to run all of the Access Console components.
For more information on how to use the Setup Wizard see [Using the Setup
Wizard](using-setup-wizard.md "using-setup-wizard.md").

## Running the

Setup Wizard in interactive mode

Interactive mode is the default setup mode for the Amazon DCV Access Console. It
will guide you through the setup process and validate the installation when
done.

1. Navigate to the folder where you extracted the Amazon DCV Access Console
   components.
2. Run the following command:

```
`$` python3 wizard.py --is-onebox
```

3. Answer the series of questions that appear. These questions determine
   how to configure the Access Console.

The Setup Wizard will finish by validating that the installation was
successful. It will then print the resolvable DNS of the host you provided. The
Amazon DCV Access Console will be accessible at that address and any user present on
that host will be able to log in.

## Running the

Setup Wizard in non-interactive mode

Non-interactive mode is the manual setup mode for the Amazon DCV Access Console. This setup
allows more configuration in your setup process. You will need to manually fill
in the JSON file. See [Modifying setup wizard parameters](using-setup-wizard.md#modifying-parameters "using-setup-wizard.md#modifying-parameters") for more details.

1. Go to the file `onebox_wizard_input.json`. This is the JSON
   file provided with the Wizard.
2. Do one of the following:

If the Broker is configured on the same host as you are installing
the Access Console components, update the following
parameters:

    * `onebox-address`– The resolvable DNS of the host
     that the components are being installed on.
    * `register-with-broker`– Configure to
     true.
    * `show-cookie-link`– If you want to display a link to a cookie
     disclaimer sign-in on the page, set this parameter to
     `true`.
    * `cookie-link-target`– Set this to the link
     you want your users to follow for the cookie disclaimer. If you
     set `show-cookie-link` to `false`, leave
     it as is.
    * `show-privacy-link`– If you want to display
     a link to a privacy disclaimer on the sign in page, set this
     parameter to true `true`.
    * `privacy-link-target`– Set this to the link
     you want your users to follow for the privacy disclaimer. If you
     set `show-privacy-link` to `false`, leave
     it as is.
    * `mariadb-username`– A username you would
     like to use with MariaDB (if you choose MariaDB as your
     datastore).
    * `mariadb-password`– A password you would
     like to use the with MariaDB user (if you choose MariaDB as your
     datastore).
    * `admin-user`– The username of a user to
     grant administrative privileges for the Access Console.

If the Broker is configured on a different host from where you are
installing the Access Console components, update the following
parameters:

    * `onebox-address`– The resolvable DNS of the host
     that the components are being installed on.
    * `broker-address`– The resolvable DNS of the host
     that the Broker is running on.
    * `broker-client-id`– The Broker Client ID
     that was registered.
    * `broker-client-password`– The Broker Client
     Password that was registered.
    * `show-cookie-link`– If you want to display a
     link to a cookie disclaimer on the sign in page, set this
     parameter to `true`.
    * `cookie-link-target`– Set this to the link
     you want your users to follow for the cookie disclaimer. If you
     set `show-cookie-link` to `false`, leave
     it as is.
    * `show-privacy-link`– If you want to display
     a link to a privacy disclaimer on the sign in page, set this
     parameter to true `true`.
    * `privacy-link-target`– Set this to the link
     you want your users to follow for the privacy disclaimer. If you
     set `show-privacy-link` to `false`, leave
     it as is.
    * `mariadb-username`– A username you would
     like to use with MariaDB (if you choose MariaDB as your
     datastore).
    * `mariadb-password`– A password you would
     like to use the with MariaDB user (if you choose MariaDB as your
     datastore).
    * `admin-user`– The username of a user to
     grant administrative privileges for the Access Console.
