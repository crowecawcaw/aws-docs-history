# SELinux on Red Hat Enterprise Linux and Rocky Linux

By default, Security Enhanced Linux (SELinux) is `enabled` and set to
`enforcing` mode for WorkSpaces Applications image builders and streaming instances
powered by Red Hat Enterprise Linux and Rocky Linux. In `enforcing` mode,
permission denials are enforced. SELinux is a collection of kernel features and
utilities to provide a strong, flexible, mandatory access control (MAC) architecture to
the major subsystems of the kernel.

SELinux provides an enhanced mechanism to enforce the separation of information based
on confidentiality and integrity requirements. This separation of information reduces
threats of tampering and bypassing of application security mechanisms. It also confines
damage that can be caused by malicious or flawed applications.

SELinux includes a set of sample security policy configuration files that's designed
to meet everyday security goals. For more information about SELinux features and
functionality, see [What is SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux "https://www.redhat.com/en/topics/linux/what-is-selinux")?
