# Windows Instances

These are the rules to configure for your Windows parent and child domain controllers.

## Parent Domain Controller, Windows

| FROM: Parent domain controllers TO: Windows stack and shared services subnets | Source Port      | Destination Port | Protocol |
| ----------------------------------------------------------------------------- | ---------------- | ---------------- | -------- |
| 88                                                                            | 49152<br>• 65535 | TCP              |
| 389                                                                           | 49152<br>• 65535 | UDP              |

| FROM: Stack subnets, including shared services TO: Windows forest root domain controllers | Source Port | Destination Port | Protocol |
| ----------------------------------------------------------------------------------------- | ----------- | ---------------- | -------- |
| 49152<br>• 65535                                                                          | 88          | TCP              |
| 49152<br>• 65535                                                                          | 389         | UDP              |

## Child Domain Controller, Windows

| FROM: Child domain controllers TO: Windows AWS domain controllers | Source Port | Destination Port | Protocol |
| ----------------------------------------------------------------- | ----------- | ---------------- | -------- |
| 49152<br>• 65535                                                  | 53          | TCP              |
| 49152<br>• 65535                                                  | 88          | TCP              |
| 49152<br>• 65535                                                  | 389         | UDP              |

| FROM: Child domain controllers TO: Windows stack and shared services subnets | Source Port      | Destination Port | Protocol |
| ---------------------------------------------------------------------------- | ---------------- | ---------------- | -------- |
| 88                                                                           | 49152<br>• 65535 | TCP              |
| 135                                                                          | 49152<br>• 65535 | TCP              |
| 389                                                                          | 49152<br>• 65535 | TCP              |
| 389                                                                          | 49152<br>• 65535 | UDP              |
| 445                                                                          | 49152<br>• 65535 | TCP              |
| 49152<br>• 65535                                                             | 49152<br>• 65535 | TCP              |

| FROM: Stack subnets, including shared services TO: Windows child domain controllers | Source Port      | Destination Port | Protocol |
| ----------------------------------------------------------------------------------- | ---------------- | ---------------- | -------- |
| 49152<br>• 65535                                                                    | 88               | TCP              |
| 49152<br>• 65535                                                                    | 135              | TCP              |
| 49152<br>• 65535                                                                    | 389              | TCP              |
| 49152<br>• 65535                                                                    | 389              | UDP              |
| 49152<br>• 65535                                                                    | 445              | TCP              |
| 49152<br>• 65535                                                                    | 49152<br>• 65535 | TCP              |
