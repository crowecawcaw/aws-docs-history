This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# KOTS admin console configuration

The KOTS admin console initially uses a self-signed certificate, which you'll need to allow
as an exception in your browser. Once you accept this exception, you are welcomed by the
Configuration Wizard for the KOTS admin console. This wizard guides you through additional
configuration steps for configuring the KOTS Admin Console's behavior, including the option to
add a custom certificate if necessary.

After initial configuration of the KOTS admin console is complete, you are prompted to
enter your admin console password that you created during the installation process. Upon your
first login you need to configure the cluster.

Choose **Continue** to proceed to the KOTS admin console for Wickr.

For a single node Embedded Cluster, choose **Continue** to proceed to the
KOTS admin console for Wickr. For multi-node installations, see [Multi-Node installation](multi-node-installation.md "multi-node-installation.md").

Once in the KOTS admin console, configure your installation according to your needs. When
utilizing the embedded cluster offering there are some key configuration settings that should be
set to ensure proper functionality of your Wickr Enterprise installation.

- **Hostname** - This is the hostname you use when communicating with the
  Wickr installation. Make sure you create appropriate DNS records for this domain to point to
  your Wickr Enterprise installation.
- Under **Advanced Options**, check the [ ] **Configure Ingress
  Controller** option to expose a configuration block for configuring the Kubernetes
  Ingress. In the **Ingress configuration block** , select **Single Node
  Embedded Cluster**, and then enter the "public" IP associated with your Wickr
  server in the text box labelled **Loadbalancer External IP (IPv4
  Only)**.

If you are unsure what this IP is, you can run the following command from the command line
on the Wickr server to determine this value: `ip route get 1.1.1.1|awk '{print
 $7}'`

- Under **Advanced Options**, check the **Enable Low Resource
  Mode** option.
- Under **Calling**, if you are using a single node Embedded Cluster, make
  sure **Require Calling Nodes** is deselected. Otherwise, if you have added a
  Calling node during the initial setup, make sure **Require Calling Nodes** is
  selected.
- If you want an all in one solution that does not utilize an external Database or S3
  Compatible storage for file sharing, select the **Internal** options for the
  following settings:
  - Database
  - S3 Storage Location

  The internal S3 storage location provides additional options for configuring storage
  capacity. It is recommended to start small and expand as necessary, since scaling down is not
  an option after provisioning.
  Once you have configured all the necessary features, scroll to the bottom of the
  configuration page, and choose **Save Config**. This will initiate some
  preflight host checks. Once the preflight checks are complete, choose **Deploy**
  to begin the Wickr Enterprise Installation.

Now you are ready to begin configuring your Wickr Enterprise installation. For more
information on configuring Wickr Enterprise, see [What is
Wickr Enterprise?](../enterpriseadminguide/what-is-wickr.md "../enterpriseadminguide/what-is-wickr.md").
