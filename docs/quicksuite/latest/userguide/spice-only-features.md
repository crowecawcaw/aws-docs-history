# SPICE-only features

Amazon Quick Sight's SPICE (Super-fast, Parallel, In-memory Calculation Engine) enables certain computationally intensive
data preparation features. These transformations are materialized in SPICE for optimal performance, rather than being
executed at query time.

**SPICE-only features**

| Steps                                                                                                                             | Other capabilities       |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>• Append <br>• Aggregate <br>• Pivot <br>• Unpivot                                                                            | <br>• Divergence         | **Features available in both SPICE and DirectQuery**                                                                                                                                                                                                                      |
| Steps                                                                                                                             | Other capabilities       |
| ---                                                                                                                               | ---                      |
| <br>• Input <br>• Add Calculated Columns <br>• Change Data Type <br>• Rename Columns <br>• Select Columns <br>• Filter <br>• Join | <br>• Composite Datasets | **Best practices** <br>• Use SPICE for workflows requiring SPICE-only features. <br>• Choose SPICE to optimize performance for complex transformations and large datasets. <br>• Consider DirectQuery for real-time data needs when SPICE-only features are not required. |
