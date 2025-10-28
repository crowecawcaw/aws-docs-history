This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Change Folder for Database Backups

The default folder for backups is on the node at `/home/elemental/database_backups`.

We strongly advise that you mount a remote folder as the location for backups. In that way, if the hardware unit fails, you can restore the database from that remote folder.

###### To mount a remote folder

1. Choose a remote server in your organization and designate a folder for backups.
2. Mount that folder to the AWS Elemental Conductor File node, as described in [Add Mount Points to AWS Elemental Conductor File Nodes](config-cond-cf-cg-mount.md "config-cond-cf-cg-mount.md").
3. In **Path to Store Management** in the Conductor File's settings, type the path to the mount folder. The path will always start with `/data/mnt/`. For example: `/data/mnt/conductor1_backup`
