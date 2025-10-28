# Migrating to AWS Elemental Server version 2.18

This procedure describes how to upgrade an appliance that is running AWS Elemental Server
from a version below 2.18.0 and migrate them to version 2.18.0 or higher.

###### Important

We strongly recommend that you test the entire migration procedure in your lab. This
strategy lets you test the migration process itself, and test the entire workflow on the
new software.

In this procedure, we show how to upgrade AWS Elemental Server version 2.17.5 to version 2.18.0.
Modify the commands you enter to match your versions.

###### Topics

- [Step A: Get ready for AWS Elemental Server migration](migrate-server-218-get-ready.md "migrate-server-218-get-ready.md")
- [Step B: Prepare the AWS Elemental Server node for
  migration](migrate-server-218-prepare-node.md "migrate-server-218-prepare-node.md")
- [Step C: Stop running jobs](migrate-server-218-stop-jobs.md "migrate-server-218-stop-jobs.md")
- [Step D: Create an AWS Elemental Server backup](migrate-server-218-backup.md "migrate-server-218-backup.md")
- [Step E: Switch boot mode to UEFI](migrate-server-218-boot-mode-uefi.md "migrate-server-218-boot-mode-uefi.md")
- [Step F: Install RHEL 9 on a AWS Elemental Server node](migrate-server-218-rhel9.md "migrate-server-218-rhel9.md")
- [Step G: Install worker software on a
  AWS Elemental Server node](migrate-server-218-install-software.md "migrate-server-218-install-software.md")
- [Step H: Restore the database on a AWS Elemental Server
  node](migrate-server-218-install-restore.md "migrate-server-218-install-restore.md")
