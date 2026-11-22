

# Skill package format and validation

A skill package is a ZIP archive of one skill that follows the [Agent Skills specification](https://agentskills.io/specification) on the Agent Skills website. ZIP is the only supported package format. AWS Agent Registry validates every package in the same way, whether you upload it or the registry synchronizes it from Amazon S3 or GitHub. The SKILL.md rules on this page also apply when the registry synchronizes only SKILL.md, through `skillMd.source`.

For the sizes, counts, and lengths that this page refers to, see [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits).

## Package layout
<a name="registry-skill-package-format-layout"></a>

These layout rules apply to a ZIP file that you build: a package that you upload, or a package object that the registry reads from Amazon S3. If you synchronize a full package from a GitHub folder, you don’t build the ZIP file. The registry builds it with SKILL.md at the root of the archive, so the folder’s name doesn’t have to match the skill’s `name`. Then the registry validates it against the other rules on this page. For more information, see [Synchronize a skill from GitHub](registry-skill-sync-github.md).

A package contains exactly one skill. Put its SKILL.md in one of the following places.

In the *root layout*, SKILL.md is at the root of the archive:

```text
my-skill.zip
├── SKILL.md
├── scripts/
│   └── extract.py
├── references/
│   └── REFERENCE.md
└── assets/
    └── report-template.md
```

In the *folder layout*, SKILL.md is inside a single top-level folder:

```text
my-skill.zip
└── my-skill/
    ├── SKILL.md
    ├── scripts/
    │   └── extract.py
    ├── references/
    │   └── REFERENCE.md
    └── assets/
        └── report-template.md
```

The following rules apply to the layout:
+ In the root layout, you can include any number of top-level files and folders, and the registry doesn’t compare `name` with any folder name.
+ In the folder layout, the archive has exactly one top-level entry: the folder. The `name` in the SKILL.md frontmatter must be the same as the folder name.
+ The package has no other SKILL.md, in any folder and in any letter case. A second SKILL.md would load as a second skill. For example, the registry rejects a package with a SKILL.md at its root and another at the top of a folder.
+ The SKILL.md file is named exactly `SKILL.md` or `skill.md`. The registry rejects other letter cases, such as `Skill.md`. A folder can’t contain both `SKILL.md` and `skill.md`.

## Create a package
<a name="registry-skill-package-format-create"></a>

Use a ZIP tool that writes standard archives, and include only the skill’s own files. The following `zip` command creates a package with the folder layout. Replace `my-skill` with the name of your skill folder:

```bash
zip -r -X my-skill.zip my-skill
```

The following commands create a package with the root layout. They change to the skill folder, and then create the ZIP file in its parent folder:

```bash
cd my-skill
zip -r -X ../my-skill.zip .
```

The following Python example builds the same folder-layout package with the `zipfile` module. It adds only regular files, with forward-slash paths and Deflate compression:

```python
import pathlib
import zipfile

skill_dir = pathlib.Path('my-skill')

with zipfile.ZipFile('my-skill.zip', 'w', compression=zipfile.ZIP_DEFLATED) as package:
    for path in sorted(skill_dir.rglob('*')):
        if path.is_file() and not path.is_symlink():
            package.write(path, path.as_posix())
```

Keep the following in mind when you create a package:
+ Some archive tools add entries that aren’t part of the skill, such as a `__MACOSX/` folder or a `.DS_Store` file. In the folder layout, an extra top-level entry makes the package fail validation. Remove these entries, or create the package from the command line.
+ The `zip` command stores the file that a symbolic link points to, unless you use the `-y` option. Because the registry rejects symbolic links, don’t use `-y`.
+ You can include binary files and nested archives. The registry doesn’t restrict file types.

## ZIP archive requirements
<a name="registry-skill-package-format-zip"></a>

A package must meet the following requirements. Most of them concern how the archive is written. If a package fails one of them, create it again with a ZIP tool that writes standard archives, as shown in [Create a package](#registry-skill-package-format-create).


| Requirement | Rule | 
| --- | --- | 
| Size, entries, and depth | The package, each file, and the total uncompressed size have maximum sizes. The number of entries (files and folders) and the folder depth also have maximums. For the limits, see [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits). | 
| Compression ratio | A file, or the whole package, that expands to more than 8 MiB can’t have a compression ratio higher than 100:1 (uncompressed size to compressed size). | 
| Entry types | The archive can contain only regular files and folders. The registry rejects symbolic links, named pipes, character and block devices, and sockets. | 
| Encryption | No entry can be encrypted. The registry rejects both traditional ZIP encryption and strong encryption. | 
| Compression | Each entry is either stored without compression or compressed with Deflate. A stored entry must record its size in its local header, not only in a data descriptor after its data. | 
| ZIP64 | The archive can’t use ZIP64 end-of-archive records. | 
| Archive | The package is a single ZIP file that starts with a ZIP local file header. The registry doesn’t accept split or spanned archives, and nothing can follow the end of the archive. | 
| Archive comment | You can include an archive comment, but it can’t contain ZIP record signatures. | 
| Consistency | Each entry’s local header and central directory record must agree on its name, compression method, and encryption. The declared sizes and CRC-32 checksums must match the entry’s data, and every entry must be listed in the central directory. | 

## File and folder names
<a name="registry-skill-package-format-paths"></a>

Every entry name must meet the following rules:
+ It’s a relative path that uses forward slashes. It can’t start with `/` or a drive letter such as `C:`.
+ It can’t contain a backslash, a null character, or a `..` segment, even one that would resolve to a path inside the package.
+ No two entries name the same path. The comparison ignores letter case and Unicode normalization, so `Scripts/run.sh` and `scripts/run.sh` are the same path.
+ If an entry has an Info-ZIP Unicode path extra field, its name in that field must be the same as the entry’s name. A name that the entry marks as UTF-8 must be valid UTF-8.
+ No part of the path is a name that Windows reserves for a device, in any letter case and with or without an extension. These names are `CON`, `PRN`, `AUX`, `NUL`, `CONIN$`, `CONOUT$`, `COM1` through `COM9`, and `LPT1` through `LPT9`, also with the superscript digits ¹, ², and ³. For example, the registry rejects `nul.sh`.
+ No part of the path ends with a period or a space. No part contains a control character, any of the characters `<`, `>`, `:`, `"`, `|`, and `?`, or an asterisk.

## SKILL.md requirements
<a name="registry-skill-package-format-skill-md"></a>

These rules apply to the SKILL.md in a package and to a SKILL.md that the registry synchronizes through `skillMd.source`.

### File format
<a name="registry-skill-package-format-skill-md-file"></a>
+ The file is UTF-8 text with no byte order mark.
+ The file starts with the frontmatter. The first line, from the first byte of the file, is `---`, with no blank lines or spaces before it. A second `---` line closes the frontmatter, and the frontmatter isn’t empty.
+ Lines end with LF or CRLF.

### YAML frontmatter
<a name="registry-skill-package-format-skill-md-yaml"></a>

The frontmatter is a single YAML mapping of keys to values. The registry rejects the following YAML features:
+ Anchors and aliases
+ Merge keys (`<<`)
+ Explicit tags, such as `!!str` 
+ Directives, such as `%YAML` 
+ Keys written with the explicit key indicator (`?`)
+ Document markers inside the frontmatter, or more than one YAML document
+ The same key more than once
+ The Unicode line break characters NEL (U\+0085), LS (U\+2028), and PS (U\+2029)
+ Mappings or lists nested more than 50 levels deep

In a SKILL.md that you synchronize through `skillMd.source` or send inline in `skillMd.data`, quote a `name` or `description` that YAML would read as a number, a Boolean, or null. For example, write `description: "true"`, not `description: true`. Otherwise, the registry rejects the value as not a string.

### Frontmatter fields
<a name="registry-skill-package-format-skill-md-fields"></a>

The following table lists the frontmatter fields and their rules.


| Field | Required | Rules | 
| --- | --- | --- | 
|  `name`  | Yes | A string of lowercase letters (a–z) and digits (0–9), in groups joined by single hyphens. It can’t start or end with a hyphen or contain two hyphens in a row. It can’t be a name that Windows reserves for a device, such as `con` or `nul`. In the folder layout, it must be the same as the folder name. It doesn’t have to be the same as the record’s name. | 
|  `description`  | Yes | A non-empty string. It can’t contain control characters other than line feed and tab, angle brackets (`<` and `>`), or invisible formatting characters such as zero-width spaces. You can use left-to-right and right-to-left marks. | 
|  `compatibility`  | No | A non-empty string. | 
|  `metadata`  | No | A mapping whose values are all strings. It can’t contain nested mappings or lists. | 
|  `allowed-tools`  | No | A string, or a list of strings. | 
|  `license`  | No | Not checked. | 
| Other keys | No | The registry accepts other keys. | 

The `name`, `description`, and `compatibility` fields have maximum lengths, and SKILL.md has a maximum size. For the limits, see [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits).

**Note**  
A SKILL.md that you write yourself, in `skillMd.data`, gets a lighter check when you send it. For what the registry checks, see [AgentSkills descriptors](registry-supported-record-types.md#registry-agentskills-descriptors). Text that passes that check can still fail when you later put it in a package or synchronize it. Make sure that it meets every rule on this page.

## How validation failures appear
<a name="registry-skill-package-format-failures"></a>

 AWS Agent Registry checks a package in two stages.

 **When it receives the request.** For an upload, the registry first checks that the content isn’t empty and isn’t larger than the maximum package size. It also checks that the content starts like a ZIP archive, and that it matches the `sha256` that you sent, if you sent one. If a check fails, the request fails with a `ValidationException`, and the registry doesn’t create or change the record. For example:
+  `The skill package is not a ZIP archive. Provide a valid ZIP archive and retry.` 
+  `artifact.sha256 does not match the SHA-256 of the supplied skill package.` 

A package that is much larger than the maximum package size can fail with a generic validation error, or with HTTP status 413. In that case, the error doesn’t mention the package size.

 **After the request returns.** The registry then opens the archive and applies every rule on this page, to an uploaded package and to a package that it synchronizes. If the package fails, the record moves to `CREATE_FAILED` or `UPDATE_FAILED`, and `statusReason` lists the problems:
+ The first reason is `The skill package failed validation.` 
+ Up to five problems follow. A problem that concerns one entry ends with `Entry:` and the entry’s path.
+ If there are more than five problems, `More problems were found.` follows the problems.
+ On a registry that is encrypted with a customer managed key, the registry doesn’t show entry names. When a listed problem concerns an entry, it adds the reason `Entry names are not shown because the registry uses a customer managed key.` 
+ If the registry left some findings out of its report, it adds the reason `Some findings were omitted from this report.` 
+ A problem that starts with `The package could not be fully checked:` means that the registry couldn’t finish a check and rejected the package for that reason.

Semicolons separate the reasons. For example:

```text
The skill package failed validation.; The entry is a symbolic link, which is not allowed. Entry: my-skill/scripts/run
```

A SKILL.md that you synchronize through `skillMd.source` and that breaks a rule fails the synchronization. The record’s `statusReason` names only the first rule that the SKILL.md breaks, after the prefix `agentSkillsDefinition.additionalData.skillMd:`.

To fix a failed record, correct the package or the source and update the record: upload the corrected package, or set `triggerSynchronization` to `true` to read the source again. While the record is in `UPDATE_FAILED` status, `GetRegistryRecord` keeps returning a download URL for the last package that passed validation. This doesn’t apply if the failed update switched between an uploaded package and a synchronized package. For more information, see [Packages during an update](registry-skill-packages.md#registry-skill-packages-update-in-progress). For other causes of `CREATE_FAILED` and `UPDATE_FAILED`, see [Skill package and skill synchronization errors](registry-troubleshooting.md#registry-troubleshooting-skills), [Troubleshoot an Amazon S3 source](registry-skill-sync-s3.md#registry-skill-sync-s3-errors), and [Troubleshoot a GitHub source](registry-skill-sync-github.md#registry-skill-sync-github-errors).

**Validation isn’t a malware scan**  
Validation checks the structure of the archive and the SKILL.md frontmatter. It doesn’t check what the files in a package do. Before an agent installs or runs a skill that it downloads from the registry, validate the skill in the same way as any other content from an external source. For more information, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).