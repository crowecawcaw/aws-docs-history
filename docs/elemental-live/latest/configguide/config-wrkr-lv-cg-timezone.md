# Set the time zone

Follow this procedure if you didn't set the time zone when you ran the install script
(via the `–t` prompt), or if you want to change the time zone on the AWS Elemental Live node. You must perform these
steps on each node in the cluster that needs the time zone updated.

###### To set the time zone (web interface)

1. On the Elemental Live web interface, go to the **Settings** page and
   choose **General**.
2. In **Timezone**, choose your required time zone.
3. Choose **Update**.
   The web interface shows all activity with a timestamp for the specified time zone.

This setting does not affect activity via SSH or via the REST API.
