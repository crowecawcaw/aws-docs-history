

# Mount your own file systems in your container
<a name="runtime-fuse-mounts"></a>

Amazon Bedrock AgentCore Runtime hosts your agent containers. The managed and bring-your-own configurations described earlier mount storage for you. If you’d rather run your own mount client, your container can mount file systems itself at runtime: run a FUSE client over the FUSE (Filesystem in Userspace) device (`/dev/fuse`), loop-mount a disk image over the loopback devices (`/dev/loop*`), or mount an NFS file system such as Amazon S3 Files or Amazon EFS.

**Note**  
Running your own mount client is available only for agent runtimes on platform version V2. For more information, see [Platform versions](runtime-how-it-works.md#runtime-platform-versions).

Your container can do the following:
+ Mount an Amazon S3 bucket with Mountpoint and work with objects as local files.
+ Scope each session to its own data in shared storage.
+ Loop-mount a disk image for a full POSIX file system, with in-place random writes, atomic renames, and file locking.
+ Mount an NFS file system with Amazon EFS or Amazon S3 Files to share it with other compute.

The examples that follow show how to set up each option. Each one uses a different base image and installs different tools, so build the image for the mount type you use.

## Mount an Amazon S3 bucket with Mountpoint
<a name="runtime-fuse-mounts-mountpoint"></a>

Use Mountpoint for Amazon S3 to present an S3 bucket as a directory. You can read and sequentially write (append) objects as files. Mountpoint can’t perform in-place random writes or rename existing objects. For a full POSIX file system, use a loopback mount (the next example).

In the following example, replace {{amzn-s3-demo-bucket}} with the name of your own bucket, and set the `S3_BUCKET` environment variable to the same bucket when you deploy.

The following Dockerfile bakes Mountpoint into the image and runs the container as root:

```
FROM public.ecr.aws/docker/library/python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
      wget fuse3 ca-certificates && \
    wget -q https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.deb && \
    apt-get install -y ./mount-s3.deb && rm mount-s3.deb && \
    rm -rf /var/lib/apt/lists/*
COPY agent.py requirements.txt ./
RUN pip install -r requirements.txt
USER 0
CMD ["python", "agent.py"]
```

Mounting requires root, so the container runs as `USER 0`. That root stays confined to your agent’s own microVM, which is dedicated to a single session and isolated from the host and from other sessions. To scope a single session’s access to its own data within shared storage, see [Session context keys](runtime-sessions.md#runtime-session-isolation).

The agent mounts the bucket on the first invocation, then writes and reads a file through the mount:

```
import os
import subprocess
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
BUCKET = os.environ["S3_BUCKET"]
MOUNT = "/mnt/s3"


@app.entrypoint
def handler(payload):
    try:
        if not os.path.ismount(MOUNT):
            os.makedirs(MOUNT, exist_ok=True)
            subprocess.run(["mount-s3", "--allow-overwrite", BUCKET, MOUNT], check=True)
        with open(f"{MOUNT}/hello.txt", "w") as f:
            f.write("written through FUSE\n")
        with open(f"{MOUNT}/hello.txt") as f:
            return {"content": f.read().strip()}
    except (subprocess.CalledProcessError, OSError) as e:
        return {"error": f"Failed to mount or access the bucket: {e}"}


if __name__ == "__main__":
    app.run()
```

Mountpoint is one FUSE client. Because the container exposes `/dev/fuse`, you can run others, such as `s3fs-fuse` for in-place writes over Amazon S3 or JuiceFS for full POSIX semantics over object storage with a separate metadata engine. Install the client in your image and run it the same way as Mountpoint.

## Scope each session to its own S3 prefix
<a name="runtime-session-isolation-s3"></a>

The earlier Mountpoint example grants the whole bucket. To restrict each session to only its own data, use the [session context keys](runtime-sessions.md#runtime-session-isolation) in the execution role policy. Store each session’s objects under a prefix named for its `runtimeSessionId`, such as `sessions/<runtimeSessionId>/`. To write under that prefix through a mount, pass `--prefix sessions/<runtimeSessionId>/` to `mount-s3` so the mount root maps to the session’s own prefix, rather than mounting the whole bucket at the root as the earlier example does. This execution role policy lets a session list, read, and write only its own prefix. Replace {{amzn-s3-demo-bucket}} with your bucket name.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket",
      "Condition": {
        "StringLike": {
          "s3:prefix": [
            "sessions/${aws:AgentCoreRuntimeSourceSid}/*",
            "sessions/${aws:AgentCoreRuntimeSourceSid}"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/sessions/${aws:AgentCoreRuntimeSourceSid}/*"
    }
  ]
}
```

In this policy:
+  {{amzn-s3-demo-bucket}} – Replace with the name of your bucket.
+  `${aws:AgentCoreRuntimeSourceSid}` – Resolves automatically to the invoking session’s `runtimeSessionId`.

When you invoke a session with `runtimeSessionId` `A`, it resolves the key to `A` and reaches only `sessions/A/`. A request for `sessions/B/` returns access denied. This works whether the session calls the S3 API directly or mounts the prefix with Mountpoint using the `--prefix` option. The `s3:ListBucket` statement lets a mount client list the prefix.

To scope by runtime instead of session, use `aws:AgentCoreRuntimeSourceArn` the same way.

**Note**  
The session ID goes into the IAM match and the storage prefix exactly as passed, so choose it carefully. Use a single opaque segment matching `^[A-Za-z0-9_-]{33,256}$`: 33 to 256 characters, with only letters, digits, underscore, and hyphen. Avoid `/`, which an IAM `*` matches across, and `.` or `..`, which can walk out of the prefix. A session ID is not a durable per-user identity, so use a unique one for each user and maintain the user-to-session mapping in your backend.

## Full POSIX storage with a loopback mount
<a name="runtime-fuse-mounts-loopback"></a>

A loopback mount treats a single disk image file as a real `ext4` file system, with full POSIX semantics: in-place random writes, atomic `rename`, and file locking.

The image file holds the whole file system, so you can also back up or move a working set as one object. Store the image as a single Amazon S3 object and restore it with one `PutObject` or `GetObject` call instead of syncing many files. Create or download the image, loop-mount it to read and write, then upload it when you’re done.

The following Python snippet, run inside your agent as root, creates a 64 MiB `ext4` image, mounts it, and uses it as a full POSIX file system:

```
import os
import subprocess

MOUNT = "/mnt/loop"
IMG = "/tmp/disk.img"

try:
    subprocess.run(["dd", "if=/dev/zero", f"of={IMG}", "bs=1M", "count=64"], check=True)
    subprocess.run(["mke2fs", "-t", "ext4", "-q", "-F", IMG], check=True)
    os.makedirs(MOUNT, exist_ok=True)
    subprocess.run(["mount", "-o", "loop", IMG, MOUNT], check=True)
    # Full POSIX works here: in-place random writes, rename, file locking, SQLite.
    # Upload IMG to Amazon S3 as a single object to back up the whole working set.
except (subprocess.CalledProcessError, OSError) as e:
    raise RuntimeError(f"Failed to create or mount the loopback file system: {e}")
```

Your container image must include the loopback and file system tools (for example, `util-linux` and `e2fsprogs`), and must run as `USER 0`.

## Mount an NFS file system with Amazon EFS or Amazon S3 Files
<a name="runtime-fuse-mounts-nfs"></a>

Amazon EFS and Amazon S3 Files present a shared file system over NFS. Mount either one from your container with the Amazon EFS utilities (`amazon-efs-utils`), which provide the `efs` and `s3files` mount types. Other compute can mount the same file system at the same time.

An NFS mount has three requirements:
+ The container runs as `USER 0`, because the mount needs root.
+ The runtime has VPC network access that can reach the file system’s mount target on TCP port 2049. Configure the runtime’s network mode for the VPC, subnets, and security group that reach the mount target.
+ The agent runtime execution role grants mount access. For S3 Files, attach the `AmazonS3FilesClientFullAccess` managed policy (or at minimum `s3files:ClientMount`).

The following Dockerfile installs the mount helpers and the NFS client:

```
FROM public.ecr.aws/amazonlinux/amazonlinux:2023
RUN dnf install -y amazon-efs-utils nfs-utils python3 python3-pip && \
    pip3 install bedrock-agentcore && \
    dnf clean all
COPY agent.py ./
USER 0
CMD ["python3", "agent.py"]
```

The following agent mounts an Amazon EFS file system on the first invocation, then writes and reads a file through the mount. Set the `EFS_FS_ID` environment variable to your file system ID when you deploy:

```
import os
import subprocess
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
FS_ID = os.environ["EFS_FS_ID"]
MOUNT = "/mnt/efs"


@app.entrypoint
def handler(payload):
    try:
        if not os.path.ismount(MOUNT):
            os.makedirs(MOUNT, exist_ok=True)
            subprocess.run(
                ["mount", "-t", "efs", "-o", "tls", f"{FS_ID}:/", MOUNT],
                check=True,
            )
        with open(f"{MOUNT}/hello.txt", "w") as f:
            f.write("written through NFS\n")
        with open(f"{MOUNT}/hello.txt") as f:
            return {"content": f.read().strip()}
    except (subprocess.CalledProcessError, OSError) as e:
        return {"error": f"Failed to mount or access the file system: {e}"}


if __name__ == "__main__":
    app.run()
```

To mount an Amazon S3 Files file system instead, use the `s3files` mount type with the same utilities, which adds IAM authentication: `mount -t s3files -o tls,iam <file-system-id>:/ /mnt/s3files`.