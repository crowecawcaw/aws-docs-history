# Starting the Jupyter Notebook server on a DLAMI instance

After you [secure your Jupyter Notebook server with a password and
SSL](setup-jupyter-secure.md "setup-jupyter-secure.md"), you can start the server. Log in to your DLAMI instance and run the
following command that uses the SSL certificate that you created previously.

```
`$` jupyter notebook --certfile=~/ssl/mycert.pem --keyfile ~/ssl/mykey.key
```

With the server started, you can now connect to it via an SSH tunnel from your client computer.
When the server runs, you will see some output from Jupyter confirming that the server is running. At this point,
ignore the callout that you can access the server via a local host URL, because that won't work until you create the tunnel.

###### Note

Jupyter will handle switching environments for you when you switch frameworks using the
Jupyter web interface. For more information, see [Switching Environments with Jupyter](tutorial-jupyter.md#tutorial-jupyter-switching "tutorial-jupyter.md#tutorial-jupyter-switching").

###### Next step

[Connecting a client to the Jupyter Notebook server on a DLAMI
instance](setup-jupyter-connect.md "setup-jupyter-connect.md")
