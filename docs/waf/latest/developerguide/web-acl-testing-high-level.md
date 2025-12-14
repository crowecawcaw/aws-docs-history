**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Testing and tuning high-level steps

This section provides a checklist of the steps for testing changes to your web
ACL, including any rules or rule groups that it uses.

###### Note

To follow the guidance in this section, you need to understand how to create and manage
AWS WAF protections like protection packs (web ACLs), rules, and rule groups. That information is covered
in earlier sections of this guide.

###### To test and tune your protection pack (web ACL)

Perform these steps first in a test environment, then in production.

1. ###### Prepare for testing

Prepare your monitoring environment, switch your new AWS WAF protections to count mode for
testing, and create any resource associations that you need.

See [Preparing for testing your AWS WAF protections](web-acl-testing-prep.md "web-acl-testing-prep.md"). 2. ###### Monitor and tune in test and production environments

Monitor and adjust your AWS WAF protections first in a test or staging environment, then in
production, until you're satisfied that they can handle traffic as you need them
to.

See [Monitoring and tuning your AWS WAF protections](web-acl-testing-activities.md "web-acl-testing-activities.md"). 3. ###### Enable your protections in production

When you're satisfied with your test protections, switch them to production mode, clean up
any unnecessary testing artifacts, and continue monitoring.

See [Enabling your protections in production](web-acl-testing-enable-production.md "web-acl-testing-enable-production.md").
After you've finished implementing your changes, continue monitoring your web traffic and
protections in production to make sure that they're working as you want them to. Web
traffic patterns can change over time, so you might need to adjust the protections
occasionally.
