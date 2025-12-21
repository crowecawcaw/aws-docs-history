# Python runtime release information

###### Important

App Runner will end the support for **Python 3.7** and **Python 3.8**
on December 1, 2025. For recommendations and more information, see [End of support for managed runtime
versions](service-source-code.md#service-source-code.managed-platforms.eos "service-source-code.md#service-source-code.managed-platforms.eos").

This topic lists the full details for the Python runtime versions that App Runner supports.

| Supported runtime versions — revised App Runner build | Runtime name  | **Minor versions** | **Included packages** |
| ----------------------------------------------------- | ------------- | ------------------ | --------------------- |
| Python 3.11 (python311)                               | 3.11.14       | SQLite 3.50.2      |
| 3.11.13                                               | SQLite 3.50.2 |
| 3.11.13                                               | SQLite 3.50.1 |
| 3.11.12                                               | SQLite 3.50.0 |
| 3.11.11                                               | SQLite 3.49.1 |
| 3.11.10                                               | SQLite 3.46.1 |
| 3.11.9                                                | SQLite 3.46.1 |
| 3.11.8                                                | SQLite 3.45.2 |
| 3.11.7                                                | SQLite 3.44.2 |

###### Notes

- **Python 3.11** – We have specific recommendations for the build configuration of services that use the Python
  3.11 managed runtime. For more information, see [Callouts for specific runtime versions](service-source-code-python.md#service-source-code-python.callouts "service-source-code-python.md#service-source-code-python.callouts") in the _Python platform_ topic.
- App Runner provides a revised build process for specific major runtimes that have been released more recently. Because of this you'll see references to
  _revised App Runner build_ and _original App Runner build_ in certain sections of this document. For more information, see [Managed runtime versions and the App Runner
  build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail").

| Supported runtime versions — original App Runner build | Runtime name  | **Minor versions** | **Included packages** |
| ------------------------------------------------------ | ------------- | ------------------ | --------------------- |
| Python 3 (python3)                                     | 3.8.20        | SQLite 3.50.2      |
| 3.8.20                                                 | SQLite 3.50.1 |
| 3.8.20                                                 | SQLite 3.50.0 |
| 3.8.16                                                 | SQLite 3.46.1 |
| 3.8.15                                                 | SQLite 3.40.0 |
| 3.7.16                                                 | SQLite 3.50.2 |
| 3.7.16                                                 | SQLite 3.50.0 |
| 3.7.15                                                 | SQLite 3.40.0 |
| 3.7.10                                                 | SQLite 3.40.0 |

###### Note

App Runner provides a revised build process for specific major runtimes that have been released more recently. Because of this you'll see references to
_revised App Runner build_ and _original App Runner build_ in certain sections of this document. For more information, see [Managed runtime versions and the App Runner
build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail").
