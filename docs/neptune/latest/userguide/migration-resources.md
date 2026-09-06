

# Resources for migrating from Neo4j to Neptune
<a name="migration-resources"></a>

Neptune provides several tools and resources that can assist in the migration process.

**Tools to help migrate from Neo4j to Neptune**
+ The openCypher [CheatSheet](https://github.com/aws-samples/amazon-neptune-samples/blob/master/opencypher/Cheatsheet.md).
+ [neo4j-to-neptune](https://github.com/awslabs/amazon-neptune-tools/tree/master/neo4j-to-neptune) – A command-line utility for migrating data from Neo4j to Neptune. This tool includes the ability to:
  + Export the data from a properly configured Neo4j graph.
  + Convert that data into Neptune format.
  + Bulk load that data into Neptune.
  + Perform some basic conversions of data during the conversion to Neptune format, such as renaming vertex or edge labels and generating elements.
  + Generate properties for nodes and edges using templates (for example, create an `~id` value using a template such as `Person_{personid}` for situations where you need to create the unique identifier for an element).
+ [openCypher Query Compatibility Checker](https://github.com/awslabs/amazon-neptune-tools/tree/master/opencypher-compatability-checker) – This tool takes an input of openCypher queries and will:
  + Check for compatibility with the selected version of Neptune.
  + Identify specific unsupported functions and clauses with their positions.
  + Suggest replacements if available.
  + Provide error descriptions of any other syntax errors.