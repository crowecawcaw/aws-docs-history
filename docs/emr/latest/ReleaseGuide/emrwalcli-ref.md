

# Amazon EMR WAL (EMRWAL) CLI reference

The *EMRWAL Command Line Interface (EMRWAL CLI)* is a unified tool to manage your write-ahead log (WAL) for Amazon EMR. The EMRWAL CLI ships with EMR clusters when you enable WAL at the time that you create a cluster. For more information about enabling WAL, see [Write-ahead logs (WAL) for Amazon EMR](emr-hbase-wal.md).

The EMRWAL CLI includes the following commands:

**Topics**
+ [`createWorkspace`](#emrwalcli-ref-createworkspace)
+ [`deleteWal`](#emrwalcli-ref-deletewal)
+ [`deleteWorkspace`](#emrwalcli-ref-deleteworkspace)
+ [`listTagsForResource`](#emrwalcli-ref-listtagsforresource)
+ [`listWals`](#emrwalcli-ref-listwals)
+ [`listWorkspaces`](#emrwalcli-ref-listworkspaces)
+ [`tagResource`](#emrwalcli-ref-tagresource)
+ [`untagResource`](#emrwalcli-ref-untagresource)

## `createWorkspace`
<a name="emrwalcli-ref-createworkspace"></a>

The `createWorkspace` command creates a new Amazon EMR WAL workspace.

**Usage:**

```bash,sh,zsh
emrwal createWorkspace [-tags <tags>] [-e {{{endpoint}}}] [-r {{{Region}}}] -w {{{workspacename}}} [-h]
```

**Example:**

```bash,sh,zsh
emrwal createWorkspace -w {{examplews}}
```

## `deleteWal`
<a name="emrwalcli-ref-deletewal"></a>

The `deleteWals` command deletes the Amazon EMR WAL that you specify.

**Usage:**

```bash,sh,zsh
emrwal deleteWal [-e {{{endpoint}}}] [-r {{{Region}}}] [-w {{{workspacename}}}] [-p <tablePrefix>] [-n <walName>] [-N <fullName>] [-R] [-m] [-h]
```

**Example:**

```bash,sh,zsh
emrwal deleteWal -w {{examplews}} -p hbasetable -n {{examplewal}}
```

## `deleteWorkspace`
<a name="emrwalcli-ref-deleteworkspace"></a>

The `deleteWorkspace` command deletes the Amazon EMR WAL workspace that you specify.

**Usage:**

```bash,sh,zsh
emrwal deleteWorkspace [-e {{{endpoint}}}] [-r {{{Region}}}] -w {{{workspacename}}} [-h]
```

**Example:**

```bash,sh,zsh
emrwal deleteWorkspace -w {{examplews}}
```

## `listTagsForResource`
<a name="emrwalcli-ref-listtagsforresource"></a>

The `listTagsForResource` command lists all of the key-value pair tags for the Amazon EMR WAL workspace that you specify.

**Usage:**

```bash,sh,zsh
emrwal listTagsForResource -arn {{{resource-arn}}} [-e {{{endpoint}}}] [-r {{{Region}}}] [-h]
```

**Example:**

```bash,sh,zsh
emrwal listTagsForResource -arn arn:aws:emrwal::{{1234567891234}}:workspace/{{examplews}}
```

## `listWals`
<a name="emrwalcli-ref-listwals"></a>

The `listWals` command lists all of the Amazon EMR WALs in the workspace that you specify.

**Usage:**

```bash,sh,zsh
emrwal listWals [-nextToken {{{token-string}}}] [-pageSize {{{integer}}}] [-e {{{endpoint}}}] [-r {{{Region}}}] [-w {{{workspacename}}}] [-p <tablePrefix>] [-M {{{integer}}}] [-h]
```

**Example:**

```bash,sh,zsh
emrwal listWals -w {{examplews}}
```

## `listWorkspaces`
<a name="emrwalcli-ref-listworkspaces"></a>

The `listWorkspaces` command lists all of the Amazon EMR WAL workspaces that are available to you.

**Usage:**

```bash,sh,zsh
emrwal listWorkspaces [-nextToken {{{token-string}}}] [-pageSize {{{integer}}}] [-e {{{endpoint}}}] [-r {{{Region}}}] [-M {{{integer}}}] [-h]
```

**Example:**

```bash,sh,zsh
emrwal listWorkspaces
```

## `tagResource`
<a name="emrwalcli-ref-tagresource"></a>

The `tagResource` command assigns one or more key-value pair tags to the Amazon EMR WAL workspace that you specify.

**Usage:**

```bash,sh,zsh
emrwal tagResource -arn {{{resource-arn}}} -tags <tags> [-e {{{endpoint}}}] [-r {{{Region}}}] [-h]
```

**Example:**

```bash,sh,zsh
emrwal tagResource -arn arn:aws:emrwal::{{1234567891234}}:workspace/{{examplews}} -tags {{tag_key}}={{tag_value}}
```

## `untagResource`
<a name="emrwalcli-ref-untagresource"></a>

The `untagResource` command unassigns one or more key-value pair tags to the Amazon EMR WAL workspace that you specify.

**Usage:**

```bash,sh,zsh
emrwal untagResource -arn {{{resource-arn}}} -tagKeys <tagKeys> [-e {{{endpoint}}}] [-r {{{Region}}}] [-h]
```

**Example:**

```bash,sh,zsh
emrwal untagResource -arn arn:aws:emrwal::{{1234567891234}}:workspace/{{examplews}} -tagKeys {{tag_key}}
```