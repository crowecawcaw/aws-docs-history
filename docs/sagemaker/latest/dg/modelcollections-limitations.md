# Constraints

While using Collections, you may face issues related to tag length constraints or
rate limits for Collection operations. Review the following list of caveats so you
can avoid issues related to these limitations when you work with your
Collections.

**VPC constraints**

- Collections are not supported in VPC mode.
  **Collection operation constraints**

- You can add a maximum of 10 Model Groups to a Collection at a time.
- You can remove a maximum of 10 Model Groups from a Collection at a
  time.
- You can move a maximum of 10 Model Groups from one Collection to another
  at a time.
- You cannot delete a Collection unless it is empty.
- A Model Group can belong to multiple Collections, but a Collection can
  only belong to one Collection.
  **Tag-related constraints**

- A Model Group can belong to a maximum of 48 Collections. For more details,
  see the following section [Collection and Model Group
  tagging](#modelcollections-tagging "#modelcollections-tagging").
- A Collection’s absolute path can be a maximum of 256 characters long.
  Since Collection names are user-specified, you can control the path length.
  For more details, see the following section [Collection and Model Group
  tagging](#modelcollections-tagging "#modelcollections-tagging").

## Collection and Model Group

tagging

The SageMaker Model Registry uses tag rules and tags to internally represent your Collection
groupings and hierarchy. You can access these tag elements in the AWS Resource Access Manager, the
SageMaker SDK, and the AWS CLI, but it is important that you do not alter or delete
them.

###### Important

Do not delete or alter any tag rules or tags which belong to your
Collections or Model Groups. Doing so prevents you from performing
Collection operations!

A tag rule is a key-value pair that SageMaker AI uses to identify a Collection’s
location in the hierarchy. In short, the key is the key of the parent
Collection, and the value is the path of the Collection within the hierarchy.
SageMaker AI allows tag values to be 256 characters or less, so if you have multiple
nested hierarchies you are advised to keep your Collection names short.

###### Important

Keep your Collection names short. The absolute path to any Collection must
be 256 characters long or less.

Model Groups, on the other hand, do not have tag rules but use tags. A Model
Group’s tags include the tag rules for all the Collections which contain the
Model Group. For example, if four Collections contain _model-group-1_, _model-group-1_
has four tags. SageMaker AI allows a single AWS resource to have a maximum of 50 tags.
Since two are pre-allocated for general purposes, a Model Group can have a
maximum of 48 tags. In conclusion, a Model Group can belong to a maximum of 48
Collections.
