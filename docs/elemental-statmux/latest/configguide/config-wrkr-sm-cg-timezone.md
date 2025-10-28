This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Set the Time Zone

Follow this procedure if you didn't set the time zone when you ran the install script
(via the `–t` prompt), or if you want to change the time zone. You must perform these
steps on each node in the cluster that needs the time zone updated.

###### To set the time zone (web interface)

1. On the AWS Elemental Statmux web interface, go to the **Settings** page and
   choose **General**.
2. In **Timezone**, choose your required time zone.
3. Choose **Update**.
   The web interface shows all activity with a timestamp for the specified time zone.

This setting does not affect activity via SSH or via the REST API.
