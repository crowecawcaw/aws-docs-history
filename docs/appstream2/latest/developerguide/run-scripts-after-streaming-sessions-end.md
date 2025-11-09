# Run Scripts After

Streaming Sessions End

You can also configure your scripts to run after users' streaming sessions end.
For example, you can run a script when users select **End Session**
from the WorkSpaces Applications toolbar, or when they reach the maximum allowed duration for the
session. You can also use these session scripts to clean up your WorkSpaces Applications environment
before a streaming instance is terminated. For example, you can use scripts to
release file locks or upload log files. When you run scripts after streaming
sessions end, the following process occurs:

![Flowchart showing WorkSpaces Applications session termination process with scripts and storage actions.](images/session-scripts-termination.png)

1. Your users' WorkSpaces Applications streaming session ends.
2. Your session termination scripts start.
3. The session termination scripts complete or time out.
4. Windows user logout occurs.
5. One or both of the following occur in parallel, if applicable:
   - If application settings persistence is enabled for your users, the
     application settings VHD file that stores your users' customizations
     and Windows settings is unmounted and uploaded to an Amazon S3 bucket in
     your account.
   - If persistent storage is enabled for your users, the storage
     connector completes a final synchronization and is unmounted.

6. The fleet instance is terminated.
