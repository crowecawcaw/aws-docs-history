

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Stop the data retention bot for your Wickr network
<a name="stopping-data-retention-bot"></a>

The software running on the data retention bot will capture `SIGTERM` signals and gracefully shutdown. Use the `docker stop {{<container ID or container name>}}` command, as shown in the following example, to issue the `SIGTERM` command to the data retention bot Docker image.

```
docker stop {{compliance_1234567890_bot}}
```