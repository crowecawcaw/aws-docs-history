# Considerations for RDS Custom for Oracle database upgrades

If you plan to upgrade your database, consider the following:

- The currently supported operating system (OS) version is Oracle Linux 8. To
  continue receiving the latest security updates and patches from RDS Custom for Oracle, upgrade
  your DB instances to Oracle Linux 8 by specifying a CEV based on this OS. Oracle Database
  12c Release 1 (12.1), Oracle Database Release 2 (12.2), and Oracle Database 19c are the only
  releases that support Oracle Linux 8. To migrate to the latest Oracle Linux 8 AMI,
  upgrade your OS to the latest AMI. For more information, see [Upgrading an RDS Custom for Oracle DB instance](custom-upgrading-modify.md "custom-upgrading-modify.md").

Oracle Linux 7.9 ended support on Dec 31, 2024. To continue running Oracle Linux 7
after the end of support, purchase an Oracle Extended Support license. You're
responsible for security updates and must patch your RDS Custom for Oracle instances manually.
For more information, see [Lifetime
Support Policy: Coverage for Oracle Open Source Service
Offerings](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf "https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf").

- When you upgrade the database binaries in your primary DB instance, RDS Custom for Oracle upgrades
  your read replicas automatically. When you upgrade the OS, however, you must upgrade
  the read replicas manually.
- When you upgrade a container database (CDB) to a new database version, RDS Custom for Oracle
  checks that all PDBs are open or could be opened. If these conditions aren't met,
  RDS Custom stops the check and returns the database to its original state without
  attempting the upgrade. If the conditions are met, RDS Custom patches the CDB root
  first, and then patches all other PDBs (including `PDB$SEED`) in
  parallel.

After patching completes, RDS Custom attempts to open all PDBs. If any PDBs fail to
open, you receive the following event: `The following PDBs failed to open:
 `list-of-PDBs``. If RDS Custom fails to patch the
 CDB root or any PDBs, the instance is put into the `PATCH_DB_FAILED`
state.

- You might want to perform a major database version upgrade and a conversion of
  non-CDB to CDB at the same time. In this case, we recommend that you proceed as
  follows:
  1.  Create a new RDS Custom for Oracle DB instance that uses the Oracle multitenant
      architecture.
  2.  Plug in a non-CDB into your CDB root, creating it as a PDB. Make sure that
      the non-CDB is the same major version as your CDB.
  3.  Convert your PDB by running the `noncdb_to_pdb.sql` Oracle SQL
      script.
  4.  Validate your CDB instance.
  5.  Upgrade your CDB instance.
