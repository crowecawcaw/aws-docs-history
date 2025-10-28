This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step C: Run the Redundancy Install Script

This install script configures Conductor redundancy.

1. On the primary Conductor, enter the following command to run the database redundancy install script.

```
[elemental@hostname ~]$ **sudo /opt/elemental\_se/.support\_utils/dbrepl configure dbrepl\_config.yml primary**
```

where <dbrepl_config> is the file that you created above. 2. You are prompted to restart the Conductor node.

```
[elemental@hostname ~]$ **sudo /etc/init.d/elemental\_se restart**
```

3. On the secondary Conductor, enter the following command to configure the secondary Conductor.

```
[elemental@hostname ~]$ **sudo /opt/elemental\_se/.support\_utils/dbrepl configure dbrepl\_config.yml secondary**
```

where <dbrepl_config> is the file you created above. 4. You are prompted to restart the Conductor node.

```
[elemental@hostname ~]$ **sudo /etc/init.d/elemental\_se restart**
```
