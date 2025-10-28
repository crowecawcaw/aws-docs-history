# Download the C producer library code

In this section, you download the low-level libraries. For prerequisites and other
details about this example, see [Use the C++ producer library](producer-sdk-cpp.md "producer-sdk-cpp.md").

1. Create a directory, and then clone the example source code from the GitHub
   repository.

```
git clone --recursive https://github.com/awslabs/amazon-kinesis-video-streams-producer-c.git
```

###### Note

If you miss running git clone with `--recursive`, run `git
 submodule update --init` in the
`amazon-kinesis-video-streams-producer-c/open-source`
directory. You must also install pkg-config, CMake, and a build
environment.

For more information, see the `README.md` in [https://github.com/awslabs/amazon-kinesis-video-streams-producer-c.git](https://github.com/awslabs/amazon-kinesis-video-streams-producer-c.git "https://github.com/awslabs/amazon-kinesis-video-streams-producer-c.git"). 2. Open the code in the integrated development environment (IDE) of your choice
(for example, [Eclipse](https://www.eclipse.org/ "https://www.eclipse.org/")).
