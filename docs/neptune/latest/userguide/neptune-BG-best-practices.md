# Neptune Blue/Green solution best practices

- Before switching your green cluster over to production, it is worth
  thoroughly verifying that it is functioning properly. Check the consistency
  of the data and the configuration of the database. It is possible that some of the
  new engine versions require client upgrades as well. Check the engine release notes
  before you upgrade. It is worth testing all this in development, testing, and
  pre-production environments before starting a blue/green upgrade in production.
- It is best to perform the switch-over from the blue to the green server
  during your maintence window.
- To ensure that everything is working properly after upgrading and
  synchronizing, it's worth keeping your original cluster for some period of time
  before deleting it. It could prove useful if an unforseen issue arises.
- Avoid heavy write operations such as bulk loads when running the
  Neptune Blue/Green solution, because they can cause replication lag that introduces
  significant downtime. Ideally, the time between turning off writes to your blue cluster
  and turning them on for your green cluster is just a few moments.
