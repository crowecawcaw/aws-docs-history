# Associate DNS aliases with your file system

You can associate DNS aliases with existing FSx for Windows File Server file systems, when you create new
file systems, and when you create a new file system from a backup using the Amazon FSx console,
CLI, and API. If you are creating an alias with a different domain name, input the full name,
including parent domain, to associate an alias.

This procedure describes how to associate DNS aliases when creating a new file system
using the Amazon FSx console. For information about associating DNS aliases with existing file
systems, and details about using the CLI and API, see [Managing DNS aliases](managing-dns-aliases.md "managing-dns-aliases.md").

###### To associate DNS aliases when creating a new file system

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Follow the procedure for creating a new file system as described in [Step 5. Create your file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1") of the Getting
   Started section.
3. In the **Access - optional** section of the **Create file
   system** wizard, enter the DNS aliases that you want to associate with your
   file system.

Use the following guidelines when specifying DNS aliases:

    * Must be formatted as a fully qualified domain name (FQDN)
     ``hostname.domain``, for example,
     `accounting.example.com`.
    * Can contain alphanumeric characters and hyphens (‐).
    * Cannot start or end with a hyphen.
    * Can start with a numeric.

For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z),
regardless of how you specify them: as uppercase letters, lowercase letters, or the
corresponding letters in escape codes. 4. For **Maintenance preferences**, make any changes that you want. 5. In the **Tags - optional** section, add any tags that you need, and
then choose **Next**. 6. Review the file system configuration shown on the **Create file
system** page. Choose **Create file system** to create the file system.
