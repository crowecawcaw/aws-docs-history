# Global resources in

AWS CodeConnections

Connections are global resources, meaning that the resource is replicated across all
AWS Regions.

Although the connection ARN format reflects the Region name where it was created, the
resource is not constrained to any Region. The Region where the connection resource was
created is the Region where connection resource data updates are controlled. Examples of API
operations that control updates to connection resource data include creating a connection,
updating an installation, deleting a connection, or tagging a connection.

Host resources for connections are not globally available resources. You use host
resources only in the Region where they were created.

- You only have to create a connection once, and then you can use it in any
  AWS Region.
- If the Region where the connection was created is having issues, this impacts APIs
  that control connection resource data, but you can still successfully use the connection
  in every other Region.
- When you list connection resources in the console or CLI, the list shows all
  connection resources associated with your account across all Regions.
- When you list host resources in the console or CLI, the list shows host resources
  associated with your account in the selected Region only.
- When a connection with an associated host resource is listed or viewed with the CLI,
  the output returns the host ARN regardless of the configured CLI Region.
