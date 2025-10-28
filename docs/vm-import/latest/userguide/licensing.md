# Licensing for your imported VMs

When you create a new VM Import task, you have two options for how to specify the
license type for the operating system. You can specify a value for either the
`--license-type` or the `--usage-operation` parameter.
Specifying a value for both parameters will return an error. You can use
`--usage-operation` to blend your operating system and SQL Server
licenses.

###### Important

AWS VM Import/Export strongly recommends specifying a value for either the
`--license-type` or `--usage-operation` parameter when you
create a new VM Import task. This ensures your operating system is licensed
appropriately and your billing is optimized. If you choose a license type that is
incompatible with your VM, the VM Import task fails with an error message. For more
information, see [Specify a licensing option for your
import](licensing-specify-option.md "licensing-specify-option.md").

###### Topics

- [Licensing considerations](licensing-considerations.md "licensing-considerations.md")
- [Specify a licensing option for your
  import](licensing-specify-option.md "licensing-specify-option.md")
