# Move an alternate domain name

If you try to add an alternate domain name to a standard distribution or distribution tenant, and the alternate domain
name is already associated with a different resource, you will get an error message.

For example, you will get the `CNAMEAlreadyExists` error message
(**`One or more of the CNAMEs you provided are already associated with a
 different resource`**) when you try to add www.example.com to a standard distribution or distribution tenant,
but that alternate domain name is already associated with a different resource.

In that case, you might want to move the existing alternate domain name from one resource
to another. This is the _source distribution_ and the
_target distribution_. You can move alternate domain
names between either standard distributions and/or distribution tenants.

To move the alternate domain name, see the following topics:

###### Topics

- [Set up the target
  standard distribution or distribution tenant](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md")
- [Find the source
  standard distribution or distribution tenant](alternate-domain-names-move-find-source.md "alternate-domain-names-move-find-source.md")
- [Move the alternate domain
  name](alternate-domain-names-move-options.md "alternate-domain-names-move-options.md")
