Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Caching files between workflow runs

When file caching is enabled, the build and test actions save on-disk files to a cache and
restore them from that cache in subsequent workflow runs. Caching reduces the latency caused
by building or downloading dependencies that haven’t changed between runs. CodeCatalyst also
supports fallback caches, which can be used to restore partial caches containing some of the
needed dependencies. This helps reduce the latency impacts of a cache miss.

###### Note

File caching is only available with the Amazon CodeCatalyst [build](build-workflow-actions.md "build-workflow-actions.md") and [test](test-workflow-actions.md "test-workflow-actions.md") actions, and only when they are
configured to use the **EC2**
[compute type](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

###### Topics

- [About file caching](#workflows-caching.files "#workflows-caching.files")
- [Creating a cache](#workflows-caching.fallback "#workflows-caching.fallback")
- [File caching constraints](#workflows-caching.constraints "#workflows-caching.constraints")

## About file caching

File caching allows you to organize your data into multiple caches, which are each
referenced under the `FileCaching` property. Each cache saves a directory
specified by a given path. The specified directory will be restored in future workflow
runs. The following is an example YAML snippet for caching with multiple caches named
`cacheKey1` and `cacheKey2`.

```
Actions:
  BuildMyNpmApp:
    Identifier: aws/build@v1
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
        - Run: npm install
        - Run: npm run test
    Caching:
      FileCaching:
        cacheKey1:
          Path: file1.txt
          RestoreKeys:
             - restoreKey1
        cacheKey2:
          Path: /root/repository
          RestoreKeys:
             - restoreKey2
             - restoreKey3

```

###### Note

CodeCatalyst uses multilayered caching, which consists of a local cache and a remote cache.
When provisioned fleets or on-demand machines encounter a cache miss on a local cache,
dependencies will be restored from a remote cache. As a result, some action runs may
experience latency from downloading a remote cache.

CodeCatalyst applies cache access restrictions to ensure that an action in one workflow
cannot modify the caches from a different workflow. This protects each workflow from
others that might push incorrect data that impact builds or deployments. Restrictions
are enforced with cache-scopes which isolate caches to every workflow and branch
pairing. For example, `workflow-A` in branch `feature-A` has a
different file cache than `workflow-A` in sibling branch
`feature-B`.

Cache misses occur when a workflow looks for a specified file cache and is unable to
find it. This can occur for multiple reasons, such as when a new branch is created or
when a new cache is referenced and it hasn't been created yet. It can also occur when a
cache expires, which by default occurs 14 days after it was last used. To mitigate cache
misses and increase the rate of cache hits, CodeCatalyst supports fallback caches. Fallback
caches are alternate caches and provide an opportunity to restore partial-caches, which
can be an older version of a cache. A cache is restored by first searching for a match
under `FileCaching` for the property name, and if not found, evaluates
`RestoreKeys`. If there is a cache miss for both the property name and
all `RestoreKeys`, the workflow will continue to run, as caching is best
effort and not guaranteed.

## Creating a cache

You can use the following instructions to add a cache to your workflow.

Visual

###### To add a cache using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the action where you want to add
   your cache.
8. Choose **Configuration**.
9. Under **File caching - optional**, choose
   **Add cache** and enter information into the
   fields, as follows:

**Key**

Specify the name of your primary cache property name. Cache
property names must be unique within your workflow. Each action can
have up to five entries in `FileCaching`.

**Path**

Specify the associated path for your cache.

**Restore keys - optional**

Specify the restore key to use as a fallback when the
primary cache property can't be found. Restore key names must be
unique within your workflow. Each cache can have up to five entries
in `RestoreKeys`. 10. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 11. Choose **Commit**, enter a commit message, and
then choose **Commit** again.

YAML

###### To add a cache using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In a workflow action, add code similar to the following:

```
`action-name`:
  Configuration:
    Steps: ...
  Caching:
    FileCaching:
      `key-name`:
        Path: `file-path`
        # # Specify any additional fallback caches
        # RestoreKeys:
        #  - `restore-key`

```

8. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
9. Choose **Commit**, enter a commit message, and
   choose **Commit** again.

## File caching constraints

The following are the constraints for the property name and
`RestoreKeys`:

- Names must be unique within a workflow.
- Names are limited to alphanumeric characters (A-Z, a-z, 0-9), hyphens (-), and
  underscores (\_).
- Names can have up to 180 characters.
- Each action can have up to five caches in `FileCaching`.
- Each cache can have up to five entries in `RestoreKeys`.

The following are the constraints for paths:

- Asterisks (\*) are not allowed.
- Paths can have up to 255 characters.
