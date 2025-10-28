# Usage reports in License Manager

Using AWS License Manager you can track the history of your self-managed licenses by scheduling
periodic snap shots of your license usage. By setting up usage reports License Manager will
automatically upload reports of your self-managed licenses to an S3 bucket based on your
specifications. Usage reports were formerly called report generators. You can set up
multiple usage reports to effectively track configurations of different license types in
your environment.

###### Note

AWS License Manager does not store your reports. License Manager reports are published directly to your S3
bucket. Once you delete a usage report, reports are no longer published to your S3
bucket.
