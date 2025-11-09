# Amazon EMR 7.6.0 - Hive

release notes

## Amazon EMR 7.6.0 -

Hive changes

| Type        | Description                                                              |
| ----------- | ------------------------------------------------------------------------ |
| Improvement | Added fast S3 prefix listing feature for ORC non ACID partitioned tables |
| Feature     | Add support for Magic Committers for Hive Write Queries on S3AFileSystem |

**Known issues**

- For Hive Insert Over-write queries with Amazon S3 Express One Zone as the output location, set
  the core-site config: `fs.s3a.directory.operations.purge.uploads` to `false`.

### Amazon EMR 7.6.0 -

New configurations

| Classification | Name                                                                    | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------- | ----------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hive-site      | `hive.exec.fast.s3.partition.discovery.enabled`                         | true    | Whether to use fast S3 partition discovery for split calculation. This will enable prefix based listing for supported file formats: ORC. Note that this<br>feature uses an S3 API parameter that the S3 Express One Zone storage class doesn't support. When using them, disable this feature.                                                                                                                                                                                              |
| hive-site      | `hive.exec.fast.s3.partition.discovery.max.thread.threshold`            | 128     | The maximum degree of parallelism for fast S3 partition discovery.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| hive-site      | `hive.exec.fast.s3.partition.discovery.parallelism`                     | 10      | The degree of parallelism of a single run of fast S3 partition discovery. This configuration only has an effect if `hive.exec.fast.s3.partition.discovery.enabled` is<br>set to `true`                                                                                                                                                                                                                                                                                                      |
| hive-site      | `hive.blobstore.output-committer.magic.track.commits.in.memory.enabled` | true    | Flag to toggle should Magic committer with Hive track all the pending commits in memory? The Magic committer has an<br>option to store the commit data in-memory which can speed up the TaskCommit operation by making fewer S3 calls. This<br>config overrides the Hadoop config `fs.s3a.committer.magic.track.commits.in.memory.enabled`                                                                                                                                                  |
| hive-site      | `hive.blobstore.output-committer.dp.skip.task.staging.dir.creation`     | true    | Flag to toggle should Magic committer create the dp staging paths in the blobstore? This flag is applicable only when<br>tracking commits in memory when Hive uses Magic Committer via `hive.blobstore.output-committer.magic.track.commits.in.memory.enabled`. By default, it is<br>set to true but it takes effect only if `hive.blobstore.output-committer.magic.track.commits.in.memory.enabled` is enabled and<br>saves additional S3 calls of create task attempt paths in blobstore. |
| hive-site      | `hive.blobstore.output-committer.magic.disable.fs.cache.for.llap`       | true    | Flag to toggle if blobstore FS caches should be disabled in write flows for LLAP when using Magic Committer. This flag comes into picture when LLAP is<br>enabled, and is by default set to true.                                                                                                                                                                                                                                                                                           |
