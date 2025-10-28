# Tutorial: Creating writable

per-user subdirectories

After you create an EFS file system and mount it locally on your Amazon EC2
(EC2) instance, it exposes an empty directory called the `file system
 root`. One common use case for this file system root directory is to create a
"writable" subdirectory for each user you create on the EC2 instance and mount the
subdirectory on the user's home directory. All files and subdirectories the user creates in
their home directory are then created on the EFS file system.

###### Note

You can follow the [Getting started](getting-started.md "getting-started.md")
exercise to create and mount an EFS file system on your EC2 instance.

In the following steps, you create a user, create a subdirectory for the user, make the user the owner of the
subdirectory, and then mount the Amazon EFS subdirectory on the
user's home directory.

1. Create user mike:
   1. Log in to your EC2 instance. Using root privileges (in this case, using the
      `sudo` command), create the user and assign a password.

   For example, the following command creates the user `mike`.

   ```
   $ sudo useradd -c "Mike Smith" mike
   $ sudo passwd mike
   ```

   A home directory is also created for the user. For example,
   `/home/mike`.

2. Create a subdirectory under `EFSroot` for the user.

For example, the following command creates subdirectory `mike` under
`EFSroot`.

```
$  sudo mkdir /`EFSroot`/mike
```

You will need to replace `EFSroot` with your local directory
name. 3. The root user and root group are the owners of the subdirectory (you can verify this by
using the `ls -l` command). To enable full permissions for the user on this
subdirectory, grant ownership of the directory to the user.

For example:

```
$ sudo chown mike:mike /`EFSroot`/mike
```

4. Use the `mount` command to mount the subdirectory onto the user's home
   directory.

For example:

```
$  sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `mount-target-DNS`:/mike  /home/mike
```

The `mount-target-DNS` address identifies the remote
EFS file system root.
If you unmount this mount target, the user can't access the directory without remounting,
which requires root permissions.
