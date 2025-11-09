# Prerequisites for Amazon Q customizations

Amazon Q customizations build upon the foundation of Amazon Q Developer Pro, and uses its
features.

To use Amazon Q customizations you must first follow the Amazon Q Developer Pro setup process
under [Getting started with Amazon Q Developer](getting-started-q-dev.md "getting-started-q-dev.md"). This
includes adding any users to your Amazon Q Developer Pro profile that you also wish to grant access
to Amazon Q Customizations.

## Authorizing your

administrator

When you use Amazon Q Customizations, your Amazon Q administrator must be authorized to access
your codebase, which you can store on Amazon S3 or through AWS CodeConnections. However, during the
standard setup process for Amazon Q Developer Pro, your AWS Organizations administrator does not provide
the Amazon Q administrator with access to those services.

This means that to create customizations, administrators need additional permissions.
For an example policy that grants the needed permissions, see [Allow administrators to
create customizations](id-based-policy-examples-admins.md#id-based-policy-examples-allow-customizations "id-based-policy-examples-admins.md#id-based-policy-examples-allow-customizations").

###### Note

If you are using GitHub as your data source, you can restrict usage to certain
repositories. See [Create a
connection to GitHub](../../../dtconsole/latest/userguide/connections-create-github.md "../../../dtconsole/latest/userguide/connections-create-github.md") in the _Developer Tools Console User
Guide_.

###### Note

The encryption key that you set up for Amazon Q Developer Pro is also used for
customizations.

## Preparing your data

It's important to create your customization using the best possible source material.
When preparing your data source, add code containing patterns that are encouraged on
your team. Avoid code containing anti-patterns, bugs, security vulnerabilities,
performance issues, and so forth.

To prepare your data source, follow these guidelines:

- Your data source must contain at least 2 MB, and at most 20 GB, of source code
  files  from supported languages. Any file in your data source that's larger than
  10 MB will be ignored.
- There is no limit on the number of files in your data source, but you must
  include at least 10 files for each language that you want your customization to
  support.
- File names and individual directory names must not exceed 255 characters.
  (Cumulatively, they can exceed 255 characters.) Exceeding these limits causes
  the customization creation to fail.
- In the Amazon S3 data  source, all source code must be placed within a directory
  and not at the root  level. Any files at the root level will be ignored.

###### Note

For information on supported languages for customizations and what file types are
used to create customizations, see
[Language support for customizations](q-language-ide-support.md#customization-language-support "q-language-ide-support.md#customization-language-support").

You can store information about the creation of your customizations in Amazon CloudWatch Logs. For more
information, see [Accessing customization-related
messages in Amazon CloudWatch Logs](customizations-optimize-accessing-logs.md "customizations-optimize-accessing-logs.md").
