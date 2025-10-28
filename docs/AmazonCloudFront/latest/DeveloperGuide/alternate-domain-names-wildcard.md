# Use wildcards in alternate domain names

When you add alternate domain names, you can use the \* wildcard at the beginning of a
domain name instead of adding subdomains individually. For example, with an
alternate domain name of \*.example.com, you can use any domain name that ends with
example.com in your URLs, such as www.example.com, product-name.example.com,
marketing.product-name.example.com, and so on. The path to the object is the same
regardless of the domain name, for example:

- www.example.com/images/image.jpg
- product-name.example.com/images/image.jpg
- marketing.product-name.example.com/images/image.jpg
  Follow these requirements for alternate domain names that include wildcards:

- The alternate domain name must begin with an asterisk and a dot (\*.).
- You _cannot_ use a wildcard to replace part of a subdomain name, like this:
  \*domain.example.com.
- You cannot replace a subdomain in the middle of a domain name, like this:
  subdomain.\*.example.com.
- All alternate domain names, including alternate domain names that use wildcards,
  must be covered by the subject alternative name (SAN) on the certificate.
  A wildcard alternate domain name, such as \*.example.com, can include another alternate
  domain name that’s in use, such as example.com.
