This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Installation of Wickr Enterprise embedded cluster

(standard)

Once you have the download instructions, download the Wickr Enterprise bundle to the
destination machine and unpack it.

```

curl -f "https://replicated.app/embedded/wickr-enterprise-ha/stable/6.52" -H "Authorization: [redacted]" -o wickr-enterprise-ha-stable.tgz
tar xvf wickr-enterprise-ha-stable.tgz

```

You now should have two files, `wickr-enterprise-ha` and
`license.yaml`. The `wickr-enterprise-ha` file is a binary
file that includes all the necessary pieces for installation of the Embedded Cluster, whereas the
`license.yaml` is your Wickr license that will be used to validate your
installation.

A basic installation can be performed at this stage by executing the
`wickr-enterprise-ha` file:

```

./wickr-enterprise-ha install --license license.yaml

```

Once the installation process begins, you are prompted to enter an Admin Console password.
Enter a secure password and ensure you save it as you will need it when accessing the KOTS Admin
Console to continue configuring your installation.

After the installation is complete, the output resembles the following:

```

   sudo ./wickr-enterprise-ha install --license license.yaml
? Set the Admin Console password (minimum 6 characters): *********
? Confirm the Admin Console password: *********
✔ Host files materialized!
✔ Host preflights succeeded!
✔ Node installation finished!
✔ Storage is ready!
✔ Embedded Cluster Operator is ready!
✔ Registry is ready!
✔ Application images are ready!
✔ Admin Console is ready!
Visit the Admin Console to configure and install wickr-enterprise-ha: http://192.168.1.100:30000


```

After the standard installation, proceed to the KOTS admin console URL provided in the
output using a web browser. For this example, the URL is `http://192.168.1.100:30000`.
However your URL will differ based on your networking configuration.
