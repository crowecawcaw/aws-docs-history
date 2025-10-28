# Step 1: Prepare the

environment

The Amazon DCV Access Console has three components Handler, Web Client, and
Authentication Server. To streamline the setup process, you can install the
components on the same host. See Amazon DCV Access Console [Requirements](requirements.md "requirements.md") to ensure your setup meets the
requirements for setup on a single host.

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
   - For all Linux distributions except Ubuntu:

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
   - For Amazon Linux 2 (x86_64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-el7-x86_64.tgz
   ```

   - For Amazon Linux 2 (ARM aarch64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-el7-aarch64.tgz
   ```

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

   - For Ubuntu20 (x86_64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-ubuntu2004-x86_64.tgz
   ```

   - For Ubuntu20 (ARM aarch64)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-access-console-ubuntu2004-aarch64.tgz
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

## Preparing the host

For users to visit the Amazon DCV Access Console, the host that the
components are installed on needs to be accessible via port 443. Make sure that
your host can accept incoming requests on that port from the IP address(es) your
users will be connecting from. See the [Networking and connectivity](networking-connectivity.md "networking-connectivity.md") for more
details.

###### Note

If you are using SELinux on the host, you need to enable the
`httpd_can_network_connect bool` in order for NGINX to
forward requests. To do this, run

```
`$` sudo setsebool -P httpd_can_network_connect 1
```
