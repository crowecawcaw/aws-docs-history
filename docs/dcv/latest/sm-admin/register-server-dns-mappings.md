# register-server-dns-mappings

Register the DCV Servers - DNS names mappings coming from a JSON file.

## Syntax

```
sudo -u root dcv-session-manager-broker register-server-dns-mappings --file-path `file_path`
```

## Options

**`--file-path`**

The path of the file containing the DCV Servers - DNS names mappings.

Type: String

Required: Yes

## Example

The following example registers the DCV Servers - DNS names mappings from file /tmp/mappings.json.

**Command**

```
`sudo -u root dcv-session-manager-broker register-server-dns-mappings --file-path /tmp/mappings.json`
```

**Output**

```
 Successfully loaded 2 server id - dns name mappings from file /tmp/mappings.json
```
