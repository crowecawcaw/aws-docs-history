# Using PAM authentication

Creating PAM users in JupyterHub on Amazon EMR is a two-step process. The first step is
to add users to the operating system running in the `jupyterhub`
container on the master node, and to add a corresponding user home directory for
each user. The second step is to add these operating system users as JupyterHub
users—a process known as _whitelisting_ in JupyterHub.
After a JupyterHub user is added, they can connect to the JupyterHub URL and provide
their operating system credentials for access.

When a user logs in, JupyterHub opens the notebook server
instance for that user, which is saved in the user's home directory on the master node, which is `/var/lib/jupyter/home/`username``. If a notebook server instance doesn't exist, JupyterHub spawns a notebook instance in the user's home directory. The following sections demonstrate how to add users individually to the
operating system and to JupyterHub, followed by a rudimentary bash script that adds
multiple users.

## Adding an operating system user to the container

The following example first uses the [useradd](https://linux.die.net/man/8/useradd "https://linux.die.net/man/8/useradd") command within the
container to add a single user, diego, and create a home directory for that
user. The second command uses [chpasswd](https://linux.die.net/man/8/chpasswd "https://linux.die.net/man/8/chpasswd") to establish a password of diego for this user. Commands
are run on the master node command line while connected using SSH. You could
also run these commands using a step as described earlier in [Administration by submitting steps](emr-jupyterhub-administer.md#emr-jupyterhub-administer-steps "emr-jupyterhub-administer.md#emr-jupyterhub-administer-steps").

```
sudo docker exec jupyterhub useradd -m -s /bin/bash -N diego
sudo docker exec jupyterhub bash -c "echo diego:diego | chpasswd"
```

## Adding a JupyterHub user

You can use the **Admin** panel in JupyterHub or the REST API
to add users and administrators, or just users.

###### To add users and administrators using the admin panel in JupyterHub

1. Connect to the master node using SSH and log in to
   https://`MasterNodeDNS`:9443 with an
   identity that has administrator permissions.
2. Choose **Control Panel**, **Admin**.
3. Choose **User**, **Add Users**, or choose **Admin**, **Add Admins**.

###### To add a user using the REST API

1. Connect to the master node using SSH and use the following command on the master node, or run
   the command as a step.
2. Acquire an administrative token to make API requests, and replace
   `AdminToken` in the following step with
   that token.
3. Use the following command, replacing `UserName` with an operating
   system user that has been created within the container.

```
curl -XPOST -H "Authorization: token `AdminToken`" "https://$(hostname):9443/hub/api/users/`UserName`
```

###### Note

You are automatically added as a JupyterHub non-admin user when you log in to the JupyterHub
web interface for the first time.

## Example: Bash script to add multiple users

The following sample bash script ties together the previous steps in this
section to create multiple JupyterHub users. The script can be run directly on
the master node, or it can be uploaded to Amazon S3 and then run as a step.

The script first establishes an array of user names, and uses the
`jupyterhub token` command to create an API token for the default
administrator, jovyan. It then creates an operating system user in the
`jupyterhub` container for each user, assigning an initial
password to each that is equal to their user name. Finally, it calls the REST
API operation to create each user in JupyterHub. It passes the token generated
earlier in the script and pipes the REST response to `jq` for easier
viewing.

```
# Bulk add users to container and JupyterHub with temp password of username
set -x
USERS=(shirley diego ana richard li john mary anaya)
TOKEN=$(sudo docker exec jupyterhub /opt/conda/bin/jupyterhub token jovyan | tail -1)
for i in "${USERS[@]}";
do
   sudo docker exec jupyterhub useradd -m -s /bin/bash -N $i
   sudo docker exec jupyterhub bash -c "echo $i:$i | chpasswd"
   curl -XPOST --silent -k https://$(hostname):9443/hub/api/users/$i \
 -H "Authorization: token $TOKEN" | jq
done
```

Save the script to a location in Amazon S3 such as
`s3://amzn-s3-demo-bucket/createjupyterusers.sh`. Then you can use
`script-runner.jar` to run it as a step.

### Example: Running the script when creating a cluster (AWS CLI)

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name="`MyJupyterHubCluster`" --release-label emr-5.36.2 \
--applications Name=JupyterHub --log-uri `s3://amzn-s3-demo-bucket/MyJupyterClusterLogs` \
--use-default-roles --instance-type m5.xlarge --instance-count `2` --ec2-attributes KeyName=`MyKeyPair` \
--steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,\
Jar=s3://`region`.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://amzn-s3-demo-bucket/createjupyterusers.sh"]
```

### Running the script on an existing cluster (AWS CLI)

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr add-steps --cluster-id `j-XXXXXXXX` --steps Type=CUSTOM_JAR,\
Name=CustomJAR,ActionOnFailure=CONTINUE,\
Jar=s3://`region`.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://amzn-s3-demo-bucket/createjupyterusers.sh"]
```
