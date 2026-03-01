# Known limitations for the Amazon Q Business Confluence (Server/Data Center) connector

The Amazon Q Confluence (Server/Data Center) connector has the following known
limitation:

- Because Amazon Q Business uses email addresses as unique identifiers, each user
  must have a unique email address.
- The Confluence (Server/Data Center) connector may not accurately differentiate
  between Confluence users with duplicate email addresses when mapping access
  control lists (ACLs). This can lead to inconsistent search results, in which a
  user might be able to see restricted content intended for one Confluence user
  with a shared email, but not other restricted content intended for a different
  Confluence user with the same email.
