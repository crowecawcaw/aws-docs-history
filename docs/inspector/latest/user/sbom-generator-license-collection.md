# Amazon Inspector SBOM Generator license collection

The Amazon Inspector SBOM Generator helps track license information in a software bill of materials (SBOM).
It collects license information from supported packages across operating systems and programming languages.
With standardized license expressions in your generated SBOM, you can understand your licensing obligations.

## Collect license information

###### Example command

The following example shows how to collect license information from a directory.

```

./inspector-sbomgen directory --path /path/to/your/directory/ --collect-licenses

```

###### SBOM component example

The following example shows a component entry in the generated SBOM.

```
"components": [
    {
      "bom-ref": "comp-2",
      "type": "application",
      "name": "sample-js-pkg",
      "version": "1.2.3",
      "licenses": [
        {
          "expression": "Apache-2.0 AND (MIT OR GPL-2.0-only)"
        }
      ],
      "purl": "pkg:npm/sample-js-pkg@1.2.3",
    }
  ]
```

## Supported packages

The following programming languages and operating system packages are supported for license collection.

| Target       | Package manager  | License information source                                                                                                                                                                                       | Type                 |
| ------------ | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Alma Linux   | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| Amazon Linux | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| CentOS       | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| Fedora       | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| OpenSUSE     | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| Oracle Linux | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| Photon OS    | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| RHEL         | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| Rocky Linux  | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| SLES         | RPM              | <br>• /usr/lib/sysimage/rpm/rpmdb.sqlite <br>• /usr/lib/sysimage/rpm/Packages <br>• /usr/lib/sysimage/rpm/Packages.db <br>• /var/lib/rpm/rpmdb.sqlite <br>• /var/lib/rpm/Packages <br>• /var/lib/rpm/Packages.db | OS                   |
| Alpine Linux | APK              | `/lib/apk/db/installed`                                                                                                                                                                                          | OS                   |
| Chainguard   | APK              | `/lib/apk/db/installed`                                                                                                                                                                                          | OS                   |
| Debian       | DPKG             | `/usr/share/doc/*/copyright`                                                                                                                                                                                     | OS                   |
| Ubuntu       | DPKG             | `/usr/share/doc/*/copyright`                                                                                                                                                                                     | OS                   |
| Node.js      | Javascript       | `node_modules/*/package.json`                                                                                                                                                                                    | Programing language  |
| PHP          | Composer package | <br>• `composer.lock` <br>• `/vendor/composer/installed.json`                                                                                                                                                    | Programing language  |
| Go           | Go               | `LICENSE`                                                                                                                                                                                                        | Programing language  |
| Python       | Python/Egg/Wheel | <br>• `.dist-info/METADATA` <br>• `.egg-info` <br>• `.egg-info/PKG-INFO`                                                                                                                                         | Programing language  |
| Ruby         | RubyGem          | `*.gemspec`                                                                                                                                                                                                      | Programing language  |
| Rust         | crate            | `Cargo.toml`                                                                                                                                                                                                     | Programming language | ### License expression standardization The SPDX license expressions format provides accurate representation of licensing terms found in open source software. The Amazon Inspector SBOM Generator standardizes all license information into SPDX license expressions through rules described in this section. The rules provide consistency and compatibility across licensing information. ###### SPDX short form identifier mapping All license names are mapped to SPDX short form identifiers. For example, `MIT License` is shortened to `MIT`. ###### Multiple license combination You can combine more than one license with the `AND` operator. The following is an example command showing how to format your command. `MIT AND Apache-2.0` ###### Custom license prefix Custom licenses are prefixed with `LicenseRef`, such as `LicenseRef-CompanyPrivate`. ###### Custom exception prefix Custom exceptions are prefixed with `AdditionRef-`, such as `AdditionRef-CustomException`. |
