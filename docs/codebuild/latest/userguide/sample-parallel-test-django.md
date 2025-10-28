# Configure parallel tests with Django

The following is sample of a `buildspec.yml` that shows parallel test execution
with Django on an Ubuntu platform:

```
version: 0.2

batch:
  fast-fail: false
  build-fanout:
    parallelism: 5

phases:
  install:
    commands:
      - echo 'Installing Python dependencies'
      - sudo yum install -y python3 python3-pip
      - python3 -m ensurepip --upgrade
      - python3 -m pip install django
  pre_build:
    commands:
      - echo 'Prebuild'
  build:
    commands:
      - echo 'Running Django Tests'
      - |
        codebuild-tests-run \
         --test-command 'python3 manage.py test $(echo "$CODEBUILD_CURRENT_SHARD_FILES" | sed -E "s/\//__/g; s/\.py$//; s/__/./g")' \
         --files-search "codebuild-glob-search '**/tests/*test_*.py'" \
         --sharding-strategy 'equal-distribution'
  post_build:
    commands:
      - echo 'Test execution completed'
```

The above example shows the usage of the environment variable `CODEBUILD_CURRENT_SHARD_FILES`.
Here `CODEBUILD_CURRENT_SHARD_FILES` is used to fetch dot notation file paths supported by Django. Use
`CODEBUILD_CURRENT_SHARD_FILES` inside double quotes as shown above.
