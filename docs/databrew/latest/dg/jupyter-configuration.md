# Configuring JupyterLab to use the extension

After you install JupyterLab, you need to configure it to secure data access and to enable server
extensions.

###### To configure a password and encryption

1. Set a password to protect the data that you plan to add in the extension.
   Jupyter provides a password utility. Run the following command and enter your
   preferred password at the prompt.

```
jupyter notebook password
```

The output looks something like the following.

```
Enter password:
Verify password:
[NotebookPasswordApp] Wrote hashed password to /home/ubuntu/.jupyter/jupyter_notebook_config.json
```

2. Enable encryption on the Jupyter server. If you install Jupyter on your local machine,
   and no one can access it over the network, you can skip this step.

To set up encryption with Transport Layer Security (TLS), create a certificate
customized for your environment. For more information, [Using Let's Encrypt](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#using-let-s-encrypt "https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#using-let-s-encrypt") in [Securing a server](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#securing-a-notebook-server "https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#securing-a-notebook-server") in the Jupyter documentation. 3. To start JupyterLab, run the following command at the command prompt.

```
jupyter lab
```

For more information, see [Starting
JupyterLab](https://JupyterLab.readthedocs.io/en/stable/getting_started/starting.html "https://JupyterLab.readthedocs.io/en/stable/getting_started/starting.html") in the JupyterLab documentation. 4. While JupyterLab is running, you can access it at a URL similar to the
following: [`http://localhost:`8888`/lab`](http://localhost:8888/lab "http://localhost:8888/lab").
If you set up encryption, use `https` instead of `http`.
If you customized the port, substitute your port number instead of
`8888`.
Use the following procedure to enable the third-party extensions.

###### To enable third-party extensions in JupyterLab

1. On the JupyterLab webpage, choose the **Extension Manager**
   icon in the menu at left.
2. Read the warning about the risks of running third-party extensions. Only
   install extensions from developers that you trust.
3. To enable third-party extensions in JupyterLab, choose
   **Enable**.
4. Follow the prompts to rebuild and reload JupyterLab.
