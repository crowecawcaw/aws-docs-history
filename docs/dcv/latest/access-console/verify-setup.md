# Verifying the setup

At this point, the Amazon DCV Access Console should be accessible at the public DNS of the
Web Client host. Navigate to `https://`web client
DNS`` in your web browser. It should redirect to the DNS of the
Authentication Server.

If you chose to use PAM authentication, you should be able to log in using the
credentials of any user on the host the Authentication Server is running on.

If you chose to use Header-Based Authentication, you will need to modify your request
headers using an extension like **Requestly**. You should add a new
header with the name being what you chose with the Setup Wizard, and the value as the
username you want to log in as.

If you have issues, refer to [Troubleshooting](troubleshooting.md "troubleshooting.md").
