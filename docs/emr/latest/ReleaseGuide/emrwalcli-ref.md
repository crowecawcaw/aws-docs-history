# Amazon EMR WAL (EMRWAL) CLI reference

The _EMRWAL Command Line Interface (EMRWAL CLI)_
is a unified tool to manage your write-ahead log (WAL) for Amazon EMR. The EMRWAL CLI ships
with EMR clusters when you enable WAL at the time that you create a cluster. For more
information about enabling WAL, see [Write-ahead logs (WAL) for Amazon EMR](emr-hbase-wal.md "emr-hbase-wal.md").

The EMRWAL CLI includes the following commands:

###### Topics

- [createWorkspace](#emrwalcli-ref-createworkspace "#emrwalcli-ref-createworkspace")
- [deleteWal](#emrwalcli-ref-deletewal "#emrwalcli-ref-deletewal")
- [deleteWorkspace](#emrwalcli-ref-deleteworkspace "#emrwalcli-ref-deleteworkspace")
- [listTagsForResource](#emrwalcli-ref-listtagsforresource "#emrwalcli-ref-listtagsforresource")
- [listWals](#emrwalcli-ref-listwals "#emrwalcli-ref-listwals")
- [listWorkspaces](#emrwalcli-ref-listworkspaces "#emrwalcli-ref-listworkspaces")
- [tagResource](#emrwalcli-ref-tagresource "#emrwalcli-ref-tagresource")
- [untagResource](#emrwalcli-ref-untagresource "#emrwalcli-ref-untagresource")

## `createWorkspace`

The `createWorkspace` command creates a new Amazon EMR WAL workspace.

**Usage:**

```
emrwal createWorkspace [-tags <tags>] [-e `{endpoint}`] [-r `{Region}`] -w `{workspacename}` [-h]
```

**Example:**

```
emrwal createWorkspace -w `examplews`
```

## `deleteWal`

The `deleteWals` command deletes the Amazon EMR WAL that you specify.

**Usage:**

```
emrwal deleteWal [-e `{endpoint}`] [-r `{Region}`] [-w `{workspacename}`] [-p <tablePrefix>] [-n <walName>] [-N <fullName>] [-R] [-m] [-h]
```

**Example:**

```
emrwal deleteWal -w `examplews` -p hbasetable -n `examplewal`
```

## `deleteWorkspace`

The `deleteWorkspace` command deletes the Amazon EMR WAL workspace that you
specify.

**Usage:**

```
emrwal deleteWorkspace [-e `{endpoint}`] [-r `{Region}`] -w `{workspacename}` [-h]
```

**Example:**

```
emrwal deleteWorkspace -w `examplews`
```

## `listTagsForResource`

The `listTagsForResource` command lists all of the key-value pair tags
for the Amazon EMR WAL workspace that you specify.

**Usage:**

```
emrwal listTagsForResource -arn `{resource-arn}` [-e `{endpoint}`] [-r `{Region}`] [-h]
```

**Example:**

```
emrwal listTagsForResource -arn arn:aws:emrwal::`1234567891234`:workspace/`examplews`
```

## `listWals`

The `listWals` command lists all of the Amazon EMR WALs in the workspace
that you specify.

**Usage:**

```
emrwal listWals [-nextToken `{token-string}`] [-pageSize `{integer}`] [-e `{endpoint}`] [-r `{Region}`] [-w `{workspacename}`] [-p <tablePrefix>] [-M `{integer}`] [-h]
```

**Example:**

```
emrwal listWals -w `examplews`
```

## `listWorkspaces`

The `listWorkspaces` command lists all of the Amazon EMR WAL workspaces that
are available to you.

**Usage:**

```
emrwal listWorkspaces [-nextToken `{token-string}`] [-pageSize `{integer}`] [-e `{endpoint}`] [-r `{Region}`] [-M `{integer}`] [-h]
```

**Example:**

```
emrwal listWorkspaces
```

## `tagResource`

The `tagResource` command assigns one or more key-value pair tags to
the Amazon EMR WAL workspace that you specify.

**Usage:**

```
emrwal tagResource -arn `{resource-arn}` -tags <tags> [-e `{endpoint}`] [-r `{Region}`] [-h]
```

**Example:**

```
emrwal tagResource -arn arn:aws:emrwal::`1234567891234`:workspace/`examplews` -tags `tag_key`=`tag_value`
```

## `untagResource`

The `untagResource` command unassigns one or more key-value pair tags
to the Amazon EMR WAL workspace that you specify.

**Usage:**

```
emrwal untagResource -arn `{resource-arn}` -tagKeys <tagKeys> [-e `{endpoint}`] [-r `{Region}`] [-h]
```

**Example:**

```
emrwal untagResource -arn arn:aws:emrwal::`1234567891234`:workspace/`examplews` -tagKeys `tag_key`
```
