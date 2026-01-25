# Precedence for zonal shifts

There can be no more than one applied zonal shift at a given time. That is, only one practice run zonal shift,
customer-initiated zonal shift, autoshift, or AWS FIS experiment for the resource. When a second zonal shift is started,
ARC follows a precedence to determine which zonal shift type is in effect for a resource.

The general principle for precedence is that zonal shifts that you start as a customer take precedence over other
shift types. However, be aware that a currently-running AWS-initiated practice run prevents you from starting an
on-demand practice run.

To illustrate precedence in ARC, the following is how precedence works for example scenarios:

| Zonal shift type applied | Zonal shift type initiated | Result                                                                                                                                              |
| ------------------------ | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS FIS experiment       | Practice run               | The practice run will fail to start, as the AWS FIS experiment takes precedence.                                                                    |
| AWS FIS experiment       | Manual zonal shift         | The AWS FIS experiment will be canceled, and the manual zonal shift will be applied.                                                                |
| AWS FIS experiment       | Zonal autoshift            | The AWS FIS experiment will be canceled, and the zonal autoshift will be applied.                                                                   |
| AWS FIS experiment       | AWS FIS experiment         | The initiated AWS FIS experiment will fail to start because there is an existing<br>experiment running that triggered the AWS FIS autoshift action. |
| Practice run             | Manual zonal shift         | The practice run will be canceled and the outcome set to `INTERRUPTED`, and the zonal<br>shift will be applied.                                     |
| Practice run             | AWS FIS experiment         | The practice run will be canceled and the outcome set to `INTERRUPTED`,<br>and the AWS FIS experiment will be applied.                              |
| Practice run             | Zonal autoshift            | The practice run will be canceled and the outcome set to `INTERRUPTED`,<br>and the zonal autoshift will be applied.                                 |
| Manual zonal shift       | Practice run               | The practice run will fail to start.                                                                                                                |
| Manual zonal shift       | AWS FIS experiment         | The AWS FIS experiment will fail to start, or fail if it's already<br>in progress.                                                                  |
| Manual zonal shift       | Zonal autoshift            | The zonal autoshift will be `ACTIVE` but not `APPLIED` on the<br>resource. The manual zonal shift takes precedence.                                 |
| Zonal autoshift          | AWS FIS experiment         | The AWS FIS experiment will fail to start, or will fail if it's in<br>progress.                                                                     |
| Zonal autoshift          | Manual zonal shift         | The zonal autoshift will be `ACTIVE` but not `APPLIED` on the<br>resource. The manual zonal shift takes precedence.                                 |
| Zonal autoshift          | Practice run               | The practice run will fail to start, as the zonal autoshift<br>takes precedence.                                                                    |

The traffic shift that is currently in effect for the resource has an applied zonal shift
status set to `APPLIED`. Only one shift is set to
`APPLIED` at any time. Other shifts that are in progress are
set to `NOT_APPLIED`, but remain with `ACTIVE`
status.
