# Connecting to the master node and Notebook servers

JupyterHub administrators and notebook users must connect to the cluster master node
using an SSH tunnel and then connecting to web interfaces served by JupyterHub on the master node. For more information about
configuring an SSH tunnel and using the tunnel to proxy Web connections, see [Connect to the cluster](../ManagementGuide/emr-connect-master-node.md "../ManagementGuide/emr-connect-master-node.md") in
the _Amazon EMR Management Guide_.

By default, JupyterHub on Amazon EMR is available through **port
9443** on the master node. The internal JupyterHub proxy also serves
notebook instances through port 9443. JupyterHub and Jupyter web interfaces can be
accessed using a URL with the following pattern:

**https://**`MasterNodeDNS`**:9443**

You can specify a different port using the `c.JupyterHub.port` property in the `jupyterhub_config.py` file. For more information, see [Networking basics](http://jupyterhub.readthedocs.io/en/latest/getting-started/networking-basics.html "http://jupyterhub.readthedocs.io/en/latest/getting-started/networking-basics.html") in the JupyterHub documentation.

By default, JupyterHub on Amazon EMR uses a self-signed certificate for SSL encryption using
HTTPS. Users are prompted to trust the self-signed certificate when they connect. You
can use a trusted certificate and keys of your own. Replace the default certificate
file, `server.crt`, and key file `server.key` in the
`/etc/jupyter/conf/` directory on the master node with certificate and
key files of your own. Use the
`c.JupyterHub.ssl_key` and `c.JupyterHub.ssl_cert` properties
in the `jupyterhub_config.py` file to specify your SSL materials. For more information, see [Security settings](https://jupyterhub.readthedocs.io/en/latest/tutorial/getting-started/security-basics.html "https://jupyterhub.readthedocs.io/en/latest/tutorial/getting-started/security-basics.html") in the JupyterHub documentation. After you update `jupyterhub_config.py`, restart the container.
