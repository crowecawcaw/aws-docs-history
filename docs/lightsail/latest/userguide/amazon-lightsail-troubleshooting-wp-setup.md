# Troubleshoot WordPress setup

issues on Lightsail instances

Two types of error messages can appear during the WordPress setup workflow in
Amazon Lightsail:

**Common errors**

These types of errors occur immediately after you choose **Create
certificate** in the final step of the workflow. These errors will
appear in a banner at the top of the Lightsail console. They're typically
caused by running the setup workflow on older WordPress instances, or by
submitting incorrect information. For example, selecting a DNS record that
doesn't point to the public IP address of your instance.

**Setup failures**

These types of errors occur within a few minutes after you complete the final
step in the workflow. These failure messages will appear in the **Set up
your WordPress website** section of the instance
**Connect** tab. These errors happen when the Let's Encrypt
HTTPS certificate cannot be configured on your instance.

Use the information in the following topics to help you diagnose and fix any errors that
you might encounter with the WordPress setup guided workflow.

###### Topics

- [Common errors](wp-setup-common-errors.md "wp-setup-common-errors.md")
- [Setup failures](wordpress-setup-failures.md "wordpress-setup-failures.md")
  For more information about the WordPress setup guided workflow in Amazon Lightsail, see
  [Configure your WordPress
  instance](amazon-lightsail-tutorial-launching-and-configuring-wordpress.md#set-up-wordpress-website "amazon-lightsail-tutorial-launching-and-configuring-wordpress.md#set-up-wordpress-website").
