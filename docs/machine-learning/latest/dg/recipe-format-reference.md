We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Recipe Format Reference

Amazon ML recipes contain instructions for transforming your data as a part of
the machine learning process. Recipes are defined using a JSON-like syntax, but they
have additional restrictions beyond the normal JSON restrictions.
Recipes have the following sections, which must appear in the order shown here:

- **Groups** enable grouping of multiple variables, for ease of
  applying transformations. For example, you can create a group of all variables having to do
  with free-text parts of a web page (title, body), and then perform a transformation on all
  of these parts at once.
- **Assignments** enable the
  creation of intermediate named variables that can be reused in
  processing.
- **Outputs** define which
  variables will be used in the learning process, and what
  transformations (if any) apply to these variables.

## Groups

You can define groups of variables in order to collectively transform all variables
within the groups, or to use these variables for machine learning without transforming them.
By default, Amazon ML creates the following groups for you:

**ALL_TEXT, ALL_NUMERIC, ALL_CATEGORICAL, ALL_BINARY
–**Type-specific groups based on variables defined in the datasource schema.

###### Note

You cannot create a group with `ALL_INPUTS`.

These variables can be used in the outputs section of your recipe without being defined.
You can also create custom groups by adding to or subtracting variables from existing groups,
or directly from a collection of variables. In the following example, we demonstrate all three
approaches, and the syntax for the grouping assignment:

```

"groups": {

"Custom_Group": "group(var1, var2)",
"All_Categorical_plus_one_other": "group(ALL_CATEGORICAL, var2)"

}

```

Group names need to start with an alphabetical character and can be between 1 and 64
characters long. If the group name does not start with an alphabetical character or if it
contains special characters (, ' " \t \r \n ( ) \), then the name needs to be quoted to
be included in the recipe.

## Assignments

You can assign one or more transformations to an intermediate
variable, for convenience and readability. For example, if you
have a text variable named email_subject, and you apply the
lowercase transformation to it, you can name the resulting
variable email_subject_lowercase, making it easy to keep track
of it elsewhere in the recipe. Assignments can also be chained,
enabling you to apply multiple transformations in a specified
order. The following example shows single and chained
assignments in recipe syntax:

```

"assignments": {

"email_subject_lowercase": "lowercase(email_subject)",

"email_subject_lowercase_ngram":"ngram(lowercase(email_subject), 2)"

}

```

Intermediate variable names need to start with an alphabet
character and can be between 1 and 64 characters long. If the
name does not start with an alphabet or if it contains special
characters (, ' " \t \r \n ( ) \), then the name needs to
be quoted to be included in the recipe.

## Outputs

The outputs section controls which
input variables will be used for the learning process, and which
transformations apply to them. An empty or non-existent output section is an error, because no
data will be passed to the learning process.

The simplest outputs section simply includes the predefined **ALL_INPUTS** group, instructing Amazon ML to use all of the variables defined in
the datasource for learning:

```

"outputs": [

"ALL_INPUTS"

]

```

The output section can also refer to the other predefined groups
by instructing Amazon ML to use all the variables in these
groups:

```

"outputs": [

"ALL_NUMERIC",

"ALL_CATEGORICAL"

]

```

The output section can also refer to custom groups. In the
following example, only one of the custom groups defined in the
grouping assignments section in the preceding example will be
used for machine learning. All other variables will be dropped:

```
"outputs": [

"All_Categorical_plus_one_other"

]
```

The outputs section can also refer to variable assignments defined in
the assignment section:

```
"outputs": [

"email_subject_lowercase"

]
```

And input variables or transformations can be defined directly
in the outputs section:

```

"outputs": [

"var1",

"lowercase(var2)"

]

```

Output needs to explicitly specify all variables and transformed
variables that are expected to be available to the learning
process. Say, for example, that you include in the output a
Cartesian product of var1 and var2. If you would like to include
both the raw variables var1 and var2 as well, then you need to
add the raw variables in the output section:

```

"outputs": [

"cartesian(var1,var2)",

"var1",

"var2"

]

```

Outputs can include comments for readability by adding the
comment text along with the variable:

```

"outputs": [

"quantile_bin(age, 10) //quantile bin age",

"age // explicitly include the original numeric variable along with the
binned version"

]

```

You can mix and match all of these approaches within the outputs
section.

###### Note

Comments are not allowed in the Amazon ML console when adding a recipe.

## Complete Recipe Example

The following example refers to several built-in data processors
that were introduced in preceding examples:

```

{

"groups": {

"LONGTEXT": "group_remove(ALL_TEXT, title, subject)",

"SPECIALTEXT": "group(title, subject)",

"BINCAT": "group(ALL_CATEGORICAL, ALL_BINARY)"

},

"assignments": {

"binned_age" : "quantile_bin(age,30)",

"country_gender_interaction" : "cartesian(country, gender)"

},

"outputs": [

"lowercase(no_punct(LONGTEXT))",

"ngram(lowercase(no_punct(SPECIALTEXT)),3)",

"quantile_bin(hours-per-week, 10)",

"hours-per-week // explicitly include the original numeric variable
along with the binned version",

"cartesian(binned_age, quantile_bin(hours-per-week,10)) // this one is
critical",

"country_gender_interaction",

"BINCAT"

]

}

```
