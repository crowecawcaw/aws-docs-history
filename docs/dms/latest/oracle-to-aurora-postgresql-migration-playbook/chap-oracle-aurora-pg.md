# Tables of feature compatibility

AWS DMS, you can ensure compatibility between the source and target databases during migration. Feature compatibility defines the set of database engine features that AWS DMS supports for a specific source-target combination. The following tables provide legends for feature compatibility to help you plan for your specific migration scenario.

## Feature compatibility legend

| Automation level icon            | Description                                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Five star feature compatibility  | **Very high compatibility**. None or minimal low-risk and low-effort rewrites needed.                                                            |
| Four star feature compatibility  | **High compatibility**. Some low-risk rewrites needed, easy workarounds exist for incompatible features.                                         |
| Three star feature compatibility | **Medium compatibility**. More involved low-medium risk rewrites needed, some redesign may be needed for incompatible features.                  |
| Two star feature compatibility   | **Low compatibility**. Medium to high risk rewrites needed, some incompatible features require redesign and reasonable-effort workarounds exist. |
| One star feature compatibility   | **Very low compatibility**. High risk and/or high-effort rewrites needed, some features require redesign and workarounds are challenging.        |
| No compatibility                 | **Not compatible**. No practical workarounds yet, may require an application level architectural solution to work around incompatibilities.      |

## AWS SCT and AWS DMS automation level legend

| Automation level icon       | Description                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------ |
| Five star automation level  | **Full automation**. AWS SCT performs fully automatic conversion, no manual conversion needed.         |
| Four star automation level  | **High automation**. Minor, simple manual conversions may be needed.                                   |
| Three star automation level | **Medium automation**. Low-medium complexity manual conversions may be needed.                         |
| Two star automation level   | **Low automation**. Medium-high complexity manual conversions may be needed.                           |
| One star automation level   | **Very low automation**. High risk or complex manual conversions may be needed.                        |
| No automation               | **No automation**. Not currently supported by AWS SCT, manual conversion is required for this feature. |
