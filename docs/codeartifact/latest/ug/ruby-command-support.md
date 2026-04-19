# RubyGems command support

CodeArtifact supports the `gem install` and `gem push` commands.

###### Note

The `gem install` command requires RubyGems version 3.5.18 or earlier
when used with CodeArtifact. RubyGems versions 3.5.19 and later require the Compact Index API
to resolve gems, which CodeArtifact does not currently support. If you are using RubyGems 3.5.19
or later, use Bundler to install gems instead, or downgrade RubyGems by running
`gem update --system 3.5.18`.

CodeArtifact does not support the following
`gem` commands:

- `gem fetch`
- `gem info --remote`
- `gem list --remote`
- `gem mirror`
- `gem outdated`
- `gem owner`
- `gem query`
- `gem search`
- `gem signin`
- `gem signout`
- `gem sources --add`
- `gem sources --update`
- `gem specification --remote`
- `gem update`
- `gem yank`
