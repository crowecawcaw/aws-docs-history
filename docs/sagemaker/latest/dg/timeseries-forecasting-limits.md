# Time-series forecasting resource

limits for Autopilot

The following table lists the resource limits for time-series forecasting jobs
in Amazon SageMaker Autopilot and whether or not you can adjust each limit.

| **Resource limits**                                                                             | **Default limit** | **Adjustable** |
| ----------------------------------------------------------------------------------------------- | ----------------- | -------------- |
| Size of input dataset                                                                           | 30 GB             | Yes            |
| Size of a single Parquet file                                                                   | 2 GB              | No             |
| Maximum number of rows in a dataset                                                             | 3 billion         | Yes            |
| Maximum number of grouping columns                                                              | 5                 | No             |
| Maximum number of numerical features                                                            | 13                | No             |
| Maximum number of categorical features                                                          | 10                | No             |
| Maximum number of time-series (unique combinations of item and grouping columns)<br>per dataset | 5,000,000         | Yes            |
| Maximum Forecast horizon                                                                        | 500               | Yes            |
