# Securing the Jupyter Notebook server on a DLAMI instance

To keep your Jupyter Notebook server secure, we recommend setting up a password and creating an SSL
certificate for the server. To configure a password and SSL, first [connect to your DLAMI instance](setup-connect.md "setup-connect.md"), and then follow these
instructions.

###### To secure the Jupyter Notebook server

1. Jupyter provides a password utility. Run the following command and enter your preferred password at the prompt.

```
`$` jupyter notebook password
```

The output will look something like this:

```
Enter password:
					Verify password:
					[NotebookPasswordApp] Wrote hashed password to /home/ubuntu/.jupyter/jupyter_notebook_config.json
```

2. Create a self-signed SSL certificate. Follow the prompts to fill out
   your locality as you see fit. You must enter `.` if you wish to leave a prompt
   blank. Your answers will not impact the functionality of the certificate.

```
`$` cd ~
					`$` mkdir ssl
					`$` cd ssl
					`$` openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mykey.key -out mycert.pem
```

###### Note

You might be interested in creating a regular SSL certificate that is third-party signed and
does not cause the browser to give you a security warning. This process is much more
involved. For more information, see [Securing a notebook server](https://jupyter-notebook.readthedocs.io/en/6.2.0/public_server.html#securing-a-notebook-server "https://jupyter-notebook.readthedocs.io/en/6.2.0/public_server.html#securing-a-notebook-server") in the Jupyter Notebook user documentation.

###### Next step

[Starting the Jupyter Notebook server on a DLAMI instance](setup-jupyter-start-server.md "setup-jupyter-start-server.md")
