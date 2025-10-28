# Use magic commands

Magic commands, or _magics_, are special commands that you can run in
a notebook cell. For example, `%env` shows the environment variables in a
notebook session. Athena supports the magic functions in IPython 6.0.3.

This section shows some key magic commands in Athena for Apache Spark.

- To see a list of magic commands in Athena, run the command
  `%lsmagic` in a notebook cell.
- For information about using magics to create graphs in Athena notebooks, see [Use magics to create data graphs](notebooks-spark-magics-graphs.md "notebooks-spark-magics-graphs.md").
- For information about additional magic commands, see [Built-in
  magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html "https://ipython.readthedocs.io/en/stable/interactive/magics.html") in the IPython documentation.

###### Note

Currently, the `%pip` command fails when executed. This is a known issue.

###### Topics

- [Cell magics](notebooks-spark-magics-cell-magics.md "notebooks-spark-magics-cell-magics.md")
- [Line Magics](notebooks-spark-magics-line-magics.md "notebooks-spark-magics-line-magics.md")
- [Graph magics](notebooks-spark-magics-graphs.md "notebooks-spark-magics-graphs.md")
