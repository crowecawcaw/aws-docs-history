# Supported languages for Amazon Q Developer in the IDE

You can use the following features of Amazon Q Developer in the IDE with any programming
language:

- [Chat](q-in-IDE-chat.md "q-in-IDE-chat.md")
- [Inline chat](q-in-IDE-inline-chat.md "q-in-IDE-inline-chat.md")
  The quality of outputs while using these features varies based on the popularity of the
  language.

For the remaining features of Amazon Q in the IDE, the supported languages are listed in
the following sections.

## Language support for inline

suggestions

Amazon Q supports [inline code suggestions](inline-suggestions.md "inline-suggestions.md") for multiple programming languages. The
accuracy and quality of the code generation for a programming language depends on the
size and quality of the training data.

In terms of the quality of the training data, the programming languages with the most
support are:

- C
- C++
- C#
- Dart
- Go
- Java
- JavaScript
- Kotlin
- Lua
- PHP
- PowerShell
- Python
- R
- Ruby
- Rust
- Scala
- Shell
- SQL
- Swift
- SystemVerilog
- TypeScript

The Infrastructure as Code (IaC) languages with the most support are:

- CDK (Typescript, Python)
- HCL (Terraform)
- JSON
- YAML

## Language support for transformations

The supported languages for transformation depend on the environment where you are transforming code.

In JetBrains IDEs and Visual Studio Code, Amazon Q can transform code in the following languages:

- [Java](code-transformation.md "code-transformation.md")
- [Embedded SQL conversion for Oracle to PostgreSQL
  database migration](transform-sql.md "transform-sql.md")

In Visual Studio, Amazon Q can transform code in the following languages:

- [C# in .NET applications](transform-dotnet-IDE.md "transform-dotnet-IDE.md")

For more information about supported languages and other prerequisites for
transformation, see the topic for the type of transformation you're performing.

## Language support for code reviews

Amazon Q can create [code reviews](code-reviews.md "code-reviews.md") and provide automatic code fixes for files and
projects written in the following languages:

- Java ‐ Java 17 and earlier
- JavaScript ‐ ECMAScript 2021 and earlier
- Python ‐ Python 3.11 and earlier, within the Python 3 series
- C# ‐ All versions (.NET 6.0 and later recommended)
- TypeScript ‐ All versions
- Ruby ‐ Ruby 2.7 and 3.2
- Go ‐ Go 1.18
- C ‐ C11 and earlier
- C++ ‐ C++17 and earlier
- PHP ‐ PHP 8.2 and earlier
- Kotlin ‐ Kotlin 2.0.0 and earlier
- Scala ‐ Scala 3.2.2 and earlier
- JSX ‐ React 17 and earlier
- Infrastructure as Code (IaC) languages
  - CloudFormation ‐ 2010-09-09
  - Terraform ‐ 1.6.2 and earlier
  - AWS CDK ‐ TypeScript and Python

## Language support for customizations

Amazon Q supports for the following
languages, and uses the listed file types to create customizations:

- Bash/Shell (.sh, .zsh, .bash)
- C (.c, .h)
- C# (.cs)
- C++ (.cpp, .hpp, .h)
- Dart (.dart)
- Go (.go)
- HCL (.hcl)
- HTML (.html, .htm)
- Java (.java)
- JavaScript (.js, .jsx)
- JSON (.json)
- Kotlin (.kt, .kts)
- Markdown (.md, .mdx)
- PHP (.php)
- Powershell (.ps1, .psm1, .psd1)
- Python (.py)
- reStructuredText (.rst)
- Ruby (.rb)
- Rust (.rs)
- Scala (.scala)
- Terraform (.tf, .tfvars)
- Text (.txt)
- TypeScript (.ts, .tsx)
- YAML (.yaml, .yml)
