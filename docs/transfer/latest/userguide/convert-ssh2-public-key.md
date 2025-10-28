# Converting an SSH2 key to SSH public key

format

AWS Transfer Family only accepts SSH-formatted public keys. If you have an SSH2 public key,
you need to convert it. An SSH2 public key has the following format:

```
---- BEGIN SSH2 PUBLIC KEY ----
Comment: "rsa-key-20160402"
AAAAB3NzaC1yc2EAAAABJQAAAgEAiL0jjDdFqK/kYThqKt7THrjABTPWvXmB3URI
:
:
---- END SSH2 PUBLIC KEY ----
```

An SSH public key has the following format:

```
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAA...
```

Run the following command to convert an SSH2-formatted public key into an
SSH-formatted public key. Replace `ssh2-key` with the name
of your SSH2 key, and `ssh-key` with the name of your SSH
key.

```
ssh-keygen -i -f `ssh2-key`.pub > `ssh-key`.pub
```
