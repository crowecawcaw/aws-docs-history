Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Testing lifecycle management for bundle outputs and merge conflicts

You can locally test your blueprint’s lifecycle management and merge conflict resolution. A series of bundles under the
`synth/` directory that represent the various phases of a lifecycle update is generated. To test the lifecycle management,
you can run the following yarn command on your blueprint:`yarn blueprint: resynth`. To learn more about resynthesis and bundles, see
[Resynthesis](custom-bp-concepts.md#resynthesis-concept "custom-bp-concepts.md#resynthesis-concept") and [Generating files with resynthesis](merge-strategies-lm.md#three-way-merge-lm "merge-strategies-lm.md#three-way-merge-lm").
