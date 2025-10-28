This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Get the data retention logs for your

Wickr network

The software running on the data retention bot Docker image will output to log
files in the `/tmp/`<botname>`/logs`
directory. They will rotate to a maximum of 5 files. You can get the logs by running
the following command.

```
docker logs `<botname>`
```

Example:

```
docker logs `compliance_1234567890_bot`
```
