# Distribution

Use the `Distribution` Analyzer to compute the frequency distribution of
values in a column. The analyzer produces different outputs depending on the column data
type:

- **Numeric columns** – Generates a binned
  histogram. The histogram divides the column's value range into equal-width intervals
  (bins) and counts the number of values in each bin.
- **String, date, and other non-numeric columns**
  – Generates a value distribution that counts the frequency of each distinct value,
  sorted in descending order by frequency. The analyzer returns only the top 20 most
  frequent values.

###### Note

You can use the `Distribution` Analyzer only in the
`Analyzers` block of your DQDL ruleset. It cannot be used as a rule.

**Syntax**

```
Distribution `<COL_NAME>`
Distribution `<COL_NAME>` with bins = `<BIN_COUNT>`
Distribution `<COL_NAME>` with bins = `<BIN_COUNT>`, rebin = `<true|false>`
```

- **COL\_NAME** – The name of the column to analyze,
  or `AllColumns` to compute distributions for all columns in the
  dataset.

**Supported column types**: Any column type

- **bins** (optional) – The number of bins
  (intervals) to use for numeric column histograms. The default value is 20. The maximum
  value is 20. This parameter has no effect on non-numeric columns.
- **rebin** (optional) – Controls automatic
  rebinning behavior. When overflow exceeds the threshold on consecutive runs, the
  analyzer rebins automatically. The default value is `true`. Set to
  `false` to keep bin edges frozen indefinitely regardless of overflow
  frequency. For more information, see
  [Automatic rebinning](dqdl.md#dqdl-analyzers-distribution-rebinning "dqdl.md#dqdl-analyzers-distribution-rebinning").
  **Example – Basic distribution for a single column**

The following example computes a frequency distribution for the `Salary`
column using the default 20 bins:

```
Analyzers = [
    Distribution "Salary"
]
```

**Example – Custom bin count**

The following example computes a histogram for the `Age` column using 10
bins:

```
Analyzers = [
    Distribution "Age" with bins = 10
]
```

**Example – Distribution for all columns**

The following example computes distributions for all columns in the dataset. Numeric
columns produce histograms with 20 bins, and non-numeric columns produce value
distributions:

```
Analyzers = [
    Distribution AllColumns
]
```

**Example – Combining with rules and other analyzers**

The following example shows a ruleset that combines rules, standard analyzers, and
the `Distribution` Analyzer:

```
Rules = [
    RowCount > 100,
    Completeness "Salary" > 0.9
]
Analyzers = [
    Mean "Salary",
    StandardDeviation "Salary",
    Distribution "Salary" with bins = 15,
    Distribution "Department"
]
```

**Output format**

When you run the `Distribution` Analyzer, it produces a statistic named
`Distribution`. Scalar statistics (such as `Mean` or
`Sum`) return a single numeric value. The `Distribution`
statistic, by contrast, returns a structured result:

- `BinEdges` – An array defining the bin boundaries (for numeric
  columns) or distinct values (for non-numeric columns).
- `Count` – An array of frequencies for each bin or value.
  You can retrieve distribution results using the `ListDataQualityStatistics`
  API or the `GetDataQualityResult` API. For more information about the Data
  Quality APIs, see
  [Data Quality APIs](aws-glue-api-data-quality.md "aws-glue-api-data-quality.md") in the
  _AWS Glue API Reference_.

**Null behavior**

The analyzer excludes rows with NULL values in the target column from the bin
calculation.

For more information about frozen bin edges, overflow observations, and automatic
rebinning, see
[Distribution Analyzer](dqdl.md#dqdl-analyzers-distribution "dqdl.md#dqdl-analyzers-distribution").
