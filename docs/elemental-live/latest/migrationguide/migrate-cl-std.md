# Migrating to AWS Elemental Live version 2.26

This procedure describes how to upgrade an appliance that is running AWS Elemental Live from a
version below x.26.0 and migrate them to version x.26.1 or higher.

###### Important

We strongly recommend that you test the entire migration procedure in your lab. This
strategy lets you test the migration process itself, and test the entire workflow on the
new software.

In this procedure, we show how to upgrade Elemental Live version 2.25.5 to version
2.26.0. Modify the commands you enter to match your versions.

###### Topics

- [Step A: Get ready for Elemental Live migration](migrate-worker-get-ready.md "migrate-worker-get-ready.md")
- [Step B: Prepare the Elemental Live node for
  migration](migrate-worker-prepare-node.md "migrate-worker-prepare-node.md")
- [Step C: Stop running events](migrate-worker-stop-channels.md "migrate-worker-stop-channels.md")
- [Step D: Create a Elemental Live backup](migrate-worker-backup.md "migrate-worker-backup.md")
- [Step E: Switch boot mode to UEFI](migrate-worker-boot-mode-uefi.md "migrate-worker-boot-mode-uefi.md")
- [Step F: Install RHEL 9 on an Elemental Live node](migrate-worker-rhel9.md "migrate-worker-rhel9.md")
- [Step G: Install worker software on an
  Elemental Live node](migrate-worker-install-software.md "migrate-worker-install-software.md")
- [Step H: Restore the database on a Elemental Live
  node](migrate-worker-install-restore.md "migrate-worker-install-restore.md")
- [Step I: Configure the Elemental Live node after
  migration](migrate-worker-rebuild-worker.md "migrate-worker-rebuild-worker.md")
