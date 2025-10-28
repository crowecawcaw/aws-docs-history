# Run the Amazon Kinesis Video Streams Edge Agent as a native process

Set up the Amazon Kinesis Video Streams Edge Agent as a systemd service. This is an optional step.

`systemd` is a systems and service manager on Linux devices.
`systemd` is the recommended way to manage the process, as it will
restart the Amazon Kinesis Video Streams Edge Agent in case the application encounters an error or the
device running the application loses power.

Do the following:

###### Run the Amazon Kinesis Video Streams Edge Agent as a native process

1. Create a new file in `/etc/systemd/system` and name it
   ``aws.kinesisvideo.edge-runtime-agent`.service`.

Paste the following:

```
[Unit]
Description=AWS Kinesis Video Streams edge agent
After=network.target
StartLimitBurst=`3`
StartLimitInterval=`30`

[Service]
Type=simple
Restart=`on-failure`
RestartSec=`10`
WorkingDirectory=/`download-location`/kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/`EdgeAgentVersion`
Environment="GST_PLUGIN_PATH=/`download-location`/kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/`EdgeAgentVersion`"
Environment="LD_LIBRARY_PATH=/`download-location`/kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/`EdgeAgentVersion`/lib"
`...`
Environment="AWS_IOT_CORE_DATA_ATS_ENDPOINT=`data-account-specific-prefix`.iot.`aws-region`.amazonaws.com"
ExecStart=/usr/lib/jvm/`java-11-amazon-corretto`/bin/java --add-opens java.base/jdk.internal.misc=ALL-UNNAMED -Dio.netty.tryReflectionSetAccessible=true -cp kvs-edge-agent.jar:libs.jar com.amazonaws.kinesisvideo.edge.controller.ControllerApp

[Install]
WantedBy=multi-user.target
```

For more information about the parameters accepted by `systemd`
service configuration file, see the [documentation](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#%5BUnit%5D%20Section%20Options "https://www.freedesktop.org/software/systemd/man/systemd.unit.html#%5BUnit%5D%20Section%20Options").

###### Note

Add required the environment variables at the `...`
location, as specified in [Build the Amazon Kinesis Video Streams Edge Agent](gs-build-agent.md "gs-build-agent.md"). 2. Reload the service files to include the new service.

Type `sudo systemctl daemon-reload`. 3. Start the service.

Type `sudo systemctl start
 `aws.kinesisvideo.edge-runtime-agent`.service`. 4. Check the status of the Amazon Kinesis Video Streams Edge Agent service to verify that it is
running.

Type `sudo systemctl status
 `aws.kinesisvideo.edge-runtime-agent`.service`.

The following is an example of the output that you will see.

```
aws.kinesisvideo.edge-runtime-agent.service - AWS Kinesis Video Streams edge agent
     Loaded: loaded (/etc/systemd/system/aws.kinesisvideo.edge-runtime-agent.service; disabled; vendor preset: enabled)
     Active: active (running) since Thu 2023-06-08 19:15:02 UTC; 6s ago
   Main PID: 506483 (java)
      Tasks: 23 (limit: 9518)
     Memory: 77.5M
        CPU: 4.214s
     CGroup: /system.slice/aws.kinesisvideo.edge-runtime-agent.service
             └─506483 /usr/lib/jvm/java-11-amazon-corretto/bin/java -cp kvs-edge-agent.jar:libs.jar com.amazonaws.kinesisvideo.edge.controller.ControllerApp
```

5. Inspect the logs for any errors.

Type `journalctl -e -u
 aws.kinesisvideo.edge-runtime-agent.service`. 6. Type `systemctl --help` for the full list of options to manage
the process using `systemctl`.

The following are some common commands to manage the
Amazon Kinesis Video Streams Edge Agent:

    * To restart, type `sudo systemctl restart
     `aws.kinesisvideo.edge-runtime-agent`.service`.
    * To stop, type `sudo systemctl stop
     `aws.kinesisvideo.edge-runtime-agent`.service`.
    * To automatically start on every device reboot, type `sudo
     systemctl enable
     `aws.kinesisvideo.edge-runtime-agent`.service`.
