# Step 1: Prepare your

environment

The Amazon DCV Access Console has three components Handler, Web Client, and
Authentication Server. These components can be installed on multiple hosts. See
Amazon DCV Access Console [Requirements](requirements.md "requirements.md") to ensure your setup meets the requirements.

## Preparing the

components and the Setup Wizard

1. Connect to the host on which you intend to install the Amazon DCV Access
   Console components.
2. Create a directory where you will save the installation files.

```
`$` mkdir dcv-access-console
```

```
`$` cd dcv-access-console
```

3. The Amazon DCV Access Console packages are digitally signed with a secure GPG signature.
   To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key.
   To do so, open a terminal window and import the Amazon DCV GPG key by entering:
   - For all Linux distributions except Ubuntu::

   ```
   `$` sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   - For Ubuntu:

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   ```
   `$` gpg --import NICE-GPG-KEY
   ```

4. Download the packaged components.
   - For Rocky8 (x86_64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-el8-x86_64.tgz
   ```

   - For Rocky8 (ARM aarch64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-el8-aarch64.tgz
   ```

   - For Amazon Linux 2023, RHEL9, CentOS9, Rocky9 (x86_64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-el9-x86_64.tgz
   ```

   - For Amazon Linux 2023, RHEL9, CentOS9, Rocky9 (ARM aarch64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-el9-aarch64.tgz
   ```

   - For Ubuntu22 (x86_64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-ubuntu2204-x86_64.tgz
   ```

   - For Ubuntu22 (ARM aarch64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-ubuntu2204-aarch64.tgz
   ```

   - For Ubuntu24 (x86_64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-ubuntu2404-x86_64.tgz
   ```

   - For Ubuntu24 (ARM aarch64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-ubuntu2404-aarch64.tgz
   ```

5. Unzip the packaged components.

```
`$` tar -xf nice-dcv-access-console-*.tgz
```

6. Run `ls`, and you should see the following
   components.
   - **Handler**, **Web Client**,
     and **Authentication** components – These
     components end in `.rpm` or `.deb`
     depending on your distribution.
   - **Setup Wizard Script** – This is a Python
     script called `wizard.py` to setup the Amazon DCV Access
     Console.
   - **Setup Wizard Folder** – This folder
     `access_console_config_wizard` contains the
     supporting files for the Setup Wizard.
   - **Setup Wizard JSON Files** – These two
     `.json` files can be used by the Setup Wizard to
     pre-populate setup parameters. One called
     `wizard_input.json` and one called
     `onebox_wizard_input.json`. These can be used by
     the Setup Wizard to populate setup options.

7. Ensure that the Setup Wizard is set up properly.

```
`$` python3 wizard.py --help
```

## Preparing the

hosts

For users to visit the Amazon DCV Access Console, the hosts that the
components are installed on needs to be accessible via port 443. Make sure that
your host can accept incoming requests on that port from the IP address(es) your
users will be connecting from. See [Networking and connectivity](networking-connectivity.md "networking-connectivity.md") for more
details.

Since we will be using SSL, each host will require a DNS entry pointing to it,
and a certificate for that DNS entry.

### Preparing the

Handler host

This is the host that will communicate with the Session Manager Broker,
and will keep track of the state of the Amazon DCV Access Console.

1. Verify the host is able to accept requests from the users on port
2.
3. Verify the host is able to send requests to the Session Manager Broker
   on the Broker’s `client-to-broker-connector-https-port`
   (port 8443 by default).
4. Take note of the public DNS.
5. Load your certificate onto the instance and take note of the path to
   the **certificate file**, **key
   file**, and **keystore** file.

If you do not already have a certificate, you can create one. For more
information, see [Generating a self-signed
certificate](generate-certs.md "generate-certs.md").

### Preparing the

Authentication Server host

This is the host that will provide the Access Console login page, and
create the authorization token the Web Client and Handler use to validate
requests.

1. Verify the host is able to accept requests on port 443 from the
   addresses that your users will be connecting from. Most likely, this
   will be any address.
2. Take note of the public DNS.
3. Load your certificate onto the instance and take note of the path
   to the **certificate file**, **key
   file**, and **keystore** file.

If you do not already have a certificate, you can create one. For
more information, see [Generating a self-signed
certificate](generate-certs.md "generate-certs.md").

### Preparing the

Web Client host

This is the host that will serve as web application that admins and users
will use to connect to the Amazon DCV Access Console.

The Web Client host should also be able to send requests to the hosts the
Handler and the Authentication Server are running on. By default, when
running on separate hosts, the Handler and Authentication Server run on port
443, although this can be customized.

1. Verify the host is able to accept requests on port 443 from the
   addresses that your users will be connecting from. Most likely, this
   will be any address.
2. Take note of the public DNS.
3. Load your certificate onto the instance and take note of the path
   to the **certificate file**, **key
   file**, and **keystore** file.

If you do not already have a certificate, you can create one. For
more information, see [Generating a self-signed
certificate](generate-certs.md "generate-certs.md").
