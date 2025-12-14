**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Migrating a protection pack (web ACL): switchover

After you've verified your new protection pack (web ACL) settings, you can start to use it in place of your
AWS WAF Classic protection pack (web ACL).

###### To begin using your new AWS WAF protection pack (web ACL)

1. Associate the AWS WAF protection pack (web ACL) with the resources that you want to protect, following the
   guidance at [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md"). This automatically
   disassociates the resources from the old protection pack (web ACL).

The switch can take from a few seconds to a number of minutes to propagate. During this
time, some requests might be processed by the old protection pack (web ACL) and others by the
new protection pack (web ACL). Your resources will be protected throughout the switch, but you
might notice inconsistencies in request handling until it's complete. 2. Configure logging for the new protection pack (web ACL), following the guidance at [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md"). 3. (Optional) If your AWS WAF Classic protection pack (web ACL) is no longer associated with any
resources, consider removing it entirely from AWS WAF Classic. For information, see
[Deleting a Web ACL](classic-web-acl-deleting.md "classic-web-acl-deleting.md").
