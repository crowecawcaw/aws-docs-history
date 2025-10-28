# Monitor and apply a new firmware

update for AWS IoT ExpressLink

After you create a firmware update job as described in the previous section, the ExpressLink
module polls for firmware update jobs, receives and validates a job, and enters a state waiting
for the update to be accepted. The host application receives an OTA event that indicates a new
firmware image is available for the ExpressLink module.

1. Use the host terminal application to query the state of the job. Enter the command:

```
AT+OTA?
```

You should see the module respond with 'OK 1 `version`'
to verify that a module OTA firmware update was proposed. 2. To accept the new firmware update, use the host terminal application to issue the
command:

```
AT+OTA ACCEPT
```

3. The ExpressLink module should now start downloading the firmware update from
   the cloud. You can monitor the state of the job using the 'AT+OTA?' command.

When the download is complete and the image signature validation is successful,
the host terminal application receives an event that indicates the module is ready
to apply the new image. 4. Direct the module to apply the new image by issuing the command:

```
AT+OTA APPLY
```

5. The ExpressLink module now reboots and boots up with the new image. The host
   terminal application receives a 'STARTUP' event indicating the new image is
   booted. To see the event, issue the command:

```
AT+EVENT?
```

Note: the event queue is shown in FIFO order, so you may have to issue the
'AT+EVENT?' command multiple times, depending on how many events are in the queue. 6. Use the host terminal application to direct the module to reconnect to AWS IoT by
issuing the command:

```
AT+CONNECT
```

The ExpressLink module should now connect to AWS IoT, complete the self-test
and mark the image as valid (preventing any further rollback to the old image). 7. Return to the AWS IoT console and verify that the job status is marked as completed
and succeeded.
