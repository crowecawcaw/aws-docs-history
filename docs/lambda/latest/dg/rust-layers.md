

# Working with layers for Rust Lambda Event Functions
<a name="rust-layers"></a>

We don't recommend using [layers](chapter-layers.md) to manage dependencies for Lambda Event Functions written in Rust. This is because Rust functions compile into a single executable, which you provide to Lambda when you deploy your function. This executable contains your compiled function code, along with all of its dependencies. Using layers not only complicates this process, but also leads to increased cold start times because your functions need to manually load extra assemblies into memory during the init phase.

To use external dependencies with your Rust handlers, include them directly in your deployment package. By doing so, you simplify the deployment process and also take advantage of built-in Rust compiler optimizations. For an example of how to import and use a dependency like the AWS SDK for Rust in your function, see [Define Lambda Event Function handlers in Rust](rust-handler.md).