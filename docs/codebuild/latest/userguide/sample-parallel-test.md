# Parallel test execution for various test frameworks sample

You can use the `codebuild-tests-run` CLI command to split and run your tests
across parallel execution environments. The following section provides `buildspec.yml`
samples for various frameworks, illustrating the usage of the `codebuild-tests-run` command.

- Each example below includes a `parallelism` level of five, meaning that five identical execution
  environments will be created to split your tests across. You can choose a `parallelism` level to suit
  your project by modifying the `parallelism` value in the `build-fanout` section.
- Each example below shows configuring your tests to be split by the test file name, which is by
  default. This distributes the tests evenly across the parallel execution environments.
  Before you get started, see [Execute parallel tests in batch builds](parallel-test.md "parallel-test.md") for more information.

For a full list of options when using the `codebuild-tests-run` CLI command,
see [Use the codebuild-tests-run CLI command](parallel-test-tests-run.md "parallel-test-tests-run.md").

###### Topics

- [Configure parallel tests with Django](sample-parallel-test-django.md "sample-parallel-test-django.md")
- [Configure parallel tests with Elixir](sample-parallel-test-elixir.md "sample-parallel-test-elixir.md")
- [Configure parallel tests with Go](sample-parallel-test-go.md "sample-parallel-test-go.md")
- [Configure parallel tests with Java (Maven)](sample-parallel-test-java-maven.md "sample-parallel-test-java-maven.md")
- [Configure parallel tests with Javascript (Jest)](sample-parallel-test-javascript.md "sample-parallel-test-javascript.md")
- [Configure parallel tests with Kotlin](sample-parallel-test-kotlin.md "sample-parallel-test-kotlin.md")
- [Configure parallel tests with PHPUnit](sample-parallel-test-phpunit.md "sample-parallel-test-phpunit.md")
- [Configure parallel tests with Pytest](sample-parallel-test-python.md "sample-parallel-test-python.md")
- [Configure parallel tests with Ruby (Cucumber)](sample-parallel-test-ruby-cucumber.md "sample-parallel-test-ruby-cucumber.md")
- [Configure parallel tests with Ruby (RSpec)](sample-parallel-test-ruby.md "sample-parallel-test-ruby.md")
