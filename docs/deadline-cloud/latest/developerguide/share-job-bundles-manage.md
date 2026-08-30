# Manage the bundles on your queue

To publish an updated version of a bundle, upload it again with the same name. The command
asks for confirmation before overwriting the existing archive. Teammates get the new version the
next time they download or submit the bundle. Their cached copy is refreshed when the archive
changes on the queue.

To remove a shared bundle from the queue for everyone, delete its `.ojd` file
from the `job-bundles/` folder in the queue's job attachments bucket. Deleting the
file requires Amazon S3 permissions on the bucket, so removing bundles is typically an administrator
task.

You can also manage the folder in Amazon S3 directly, for example to seed a queue with a set of
starter bundles from a deployment script. Place `.ojd` archives in the
`job-bundles/` folder, using subfolders to organize them if you want. Only
`.ojd` files are recognized as bundles, and the CLI commands only list bundles at the
top level of the folder. Bundles in subfolders appear in the job bundle browser.
