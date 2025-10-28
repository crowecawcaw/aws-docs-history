# Step 5 –

Configure the connection to the AWS PCS cluster

To establish a connection to the AWS PCS cluster, launch `sackd` as a system service
by following these steps.

###### Note

If you use Slurm 25.05 or later, you can use a script to set up your login node
to connect to multiple clusters instead.
For more information, see [Connecting a standalone login node to multiple
clusters in AWS PCS](multi-cluster-login-script.md "multi-cluster-login-script.md").

1. Set up the environment file for the `sackd` service with the command that
   follows. Before running the command, replace `ip-address` and
   `port` with the values retrieved from endpoints in [Step 1](working-with_login-nodes_standalone_get-addr.md "working-with_login-nodes_standalone_get-addr.md").

```
sudo echo "SACKD_OPTIONS='--conf-server=`ip-address`:`port`'" > /etc/sysconfig/sackd
```

2. Create a `systemd` service file for managing the `sackd`
   process.

```
sudo cat << EOF > /etc/systemd/system/sackd.service
[Unit]
Description=Slurm auth and cred kiosk daemon
After=network-online.target remote-fs.target
Wants=network-online.target
ConditionPathExists=/etc/sysconfig/sackd

[Service]
Type=notify
EnvironmentFile=/etc/sysconfig/sackd
User=slurm
Group=slurm
RuntimeDirectory=slurm
RuntimeDirectoryMode=0755
ExecStart=/opt/aws/pcs/scheduler/slurm-25.05/sbin/sackd --systemd \$SACKD_OPTIONS
ExecReload=/bin/kill -HUP \$MAINPID
KillMode=process
LimitNOFILE=131072
LimitMEMLOCK=infinity
LimitSTACK=infinity

[Install]
WantedBy=multi-user.target
EOF

```

3. Set ownership of the `sackd` service file.

```
sudo chown root:root /etc/systemd/system/sackd.service && \
    sudo chmod 0644 /etc/systemd/system/sackd.service
```

4. Enable the `sackd` service.

```
sudo systemctl daemon-reload && sudo systemctl enable sackd
```

5. Start the `sackd` service.

```
sudo systemctl start sackd
```
