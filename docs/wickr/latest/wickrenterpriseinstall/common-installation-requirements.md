This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Additional Common Installation Requirements

**IP Hostname Installations**

If your installation requires an IP based hostname, there are some additional configuration
options. These instructions are specific for IP based hostnames, and it is recommended you follow
the other instructions for the basic setup listed above.

In the KOTS admin panel, complete the following steps.

1. Set the **Hostname** to the IP you will be using.
2. Under **Certificates**, select **Upload a Certificate**.
   Then, generate a self-signed certificate following the instructions for an IP based
   certificate. For more information, see [Generating a self-signed certificate](tls-certificate-settings.md#generating-self-signed-certificate "tls-certificate-settings.md#generating-self-signed-certificate").
3. Upload the `.crt` file for the Certificate and the
   `.key` file for the Private key
4. For the Certificate Chain, upload the `.crt` file again.
5. Check **Set a pinned certificate** checkbox.
6. Upload the `.crt` for the **Pinned
   Certificate**.
7. Under **Calling**, uncheck **Automatically discover server public
   IP addresses** and **Use host primary IP address for Calling
   traffic** checkboxes.
8. Under **Calling**, put the IP address of the hostname in the
   **Hostname Override** text box.
9. Under **Advanced Options**, check the **Configure Ingress
   Controller** checkbox. A new configuration section called
   **Ingress** appears below.
10. Under **Ingress**, select **Single Node Embedded
    Cluster**.
11. Under **Ingress**, enter the IP for the 'public' interface on the Wickr
    server. This may be different than the IP used as your hostname. See additional information on
    this value in the basic configuration steps.
12. Under **Ingress**, check **Use wildcard
    hostname**.
    **SELinux Enforcing Mode**

If you require the use of SELinux in enforcing mode, modify the default data directory used
to install the embedded cluster. It is recommended to use `/opt` as it has been tested
to work with most SELinux policies for this use case.

```

mkdir /opt/wickr
./wickr-enterprise-ha install --license license.yaml --data-dir /opt/wickr --ignore-host-preflights

```

The replicated embedded clusters default installation preflight checks will attempt to
validate that SELinux is in permissive mode and fail if SELinux is in Enforcing. To bypass this,
it is required to use the `--ignore-host-preflights` command line argument. When
using the command line option, there is a prompt similiar to the one below. Enter
**Yes** when prompted.

```

✗  1 host preflight failed

•  SELinux must be disabled or run in permissive mode. To run SELinux in permissive mode, edit /etc/selinux/config, change the line
'SELINUX=enforcing' to 'SELINUX=permissive', save the file, and reboot. You can run getenforce to verify the change."

? Are you sure you want to ignore these failures and continue installing? Yes

```

**AirGap installations**

The embedded cluster installation option for Wickr Enterprise supports airgapped
installations. Additional configuration and enablements for your license are required. Contact
support if you are interested in using Wickr Enterprise embedded cluster in an airgapped
environment.

When performing an airgap installation, the download instructions differ from the standard
installation method. They should resemble the following:

```

curl -f "https://replicated.app/embedded/wickr-enterprise-ha/stable/6.52?airgap=true" -H "Authorization: [redacted]" -o wickr-enterprise-ha-stable.tgz

```

Download the bundle to a machine that has internet access, then transfer it to your
airgapped environment using your preferred data transportation method. Once the bundle is
transferred, extract it as you would with any standard installation bundle. A third file
`wickr-enterprise-ha.airgap`, containing all the associated Wickr
Enterprise application service images will be included.

```

tar xvf wickr-enterprise-ha-stable.tgz

```

During installation, it is necessary to set the `--airgap-bundle` command
line argument after extraction; otherwise, the process follows the standard installation
procedure.

```

./wickr-enterprise-ha install --license license.yaml --airgap-bundle wickr-enterprise-ha.airgap

```

**Updating an airGapped embedded cluster**

To update an AirGapped Embedded cluster, complete the following steps.

1. Download the new embedded cluster package from Replicated, and transfer it to the host
   machine using your standard data transfer methods for your airgapped environment. After the new
   bundle is on the host machine, extract the tarball:

```

tar xvf wickr-enterprise-ha-stable.tgz

```

2. Run the update using the new binary and airgap bundle:

```

./wickr-enterprise-ha update --airgap-bundle wickr-enterprise-ha.airgap
✔  Application images are ready!
✔  Finished!

```

3. Start the KOTS admin console, and login to the provided URL using your standard methods
   of accessing the KOTS admin console

```

./wickr-enterprise-ha admin-console

```

4.  Once logged in to the KOTS Admin Console, find the **Latest Available
    Update** on the left under **Version** , and then press the
    **Go to Version history** button.
5.  Choose **Deploy** for the new version under **Available
    Updates**. Walk through the screens:

        1. Change any configuration options, scroll down, and then choose
         **Next**.
        2. Verify no preflight checks failed, choose **Next: Confirm and
         deploy**.
        3. Choose **Deploy**.

    **Additional notes on the Wickr Enterprise embedded cluster**

- **NAMESPACE**: Unlike most Wickr Enterprise installations, the embedded
  cluster installation installs the Wickr assets to the _kotsadm_ namespace
  in kubernetes and not _wickr_. Modify any scripts or commands you have saved
  that use `-n wickr` for kubectl, helm or any other utility to use `-n
kotsadm` instead.
- **Interacting with the Kubernetes Cluster**: From the host machine, use
  the `./wickr-enterprise-ha` binary to create a shell with appropriate
  variables set to interact with the Kubernetes installation by running
  **./wickr-enterprise-ha shell**. This will provide the kubectl utility within
  the shell's PATH and set the appropriate kube config to the local installation.
