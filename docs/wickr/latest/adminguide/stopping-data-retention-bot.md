This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Stop the data retention bot for your Wickr network

The software running on the data retention bot will capture `SIGTERM`
signals and gracefully shutdown. Use the `docker stop `<container ID
 or container name>``command, as shown in the following
 example, to issue the`SIGTERM` command to the data retention bot Docker
image.

```
docker stop `compliance_1234567890_bot`
```
