# Define limits in a

repeating section

You can set limits to show only a certain number of distinct dimension
values for each dimension of a repeating section. You can choose to show
between 1 and 1000 distinct values. The default limit is 50.

###### To define limits in a repeating section

1. Navigate to the section that you want to add a repeating behavior
   to and choose the **Edit repeating section**
   (triple panel).
2. In the **Edit section** that opens, choose the
   ellipsis (three dots) next to the dimension that you want to
   change.
3. For **Limit to**, enter the number of values that
   you want to limit the sorting to. You can enter a number between 1
   and 1000.
   **Considerations for limits**

The following limitations apply to limits in repeating sections.

- An _instance_ is defined as a distinct value of
  a dimention or a unique combination of values of multiple
  dimensions.
- If the number of unique instancess for a dimension in a repeating
  section exceeds 1000, the PDF report is NOT generated. If this
  occurs, try one of the following options.
  - Define a limit for your dimension.
  - Create a sheet level filter to restrict the dimension
    values.
  - Use row level security (RLS) to restrict the dimension
    values.
  - Apply dataset filters.
