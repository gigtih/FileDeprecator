# Introduction

This is a program written in python that deprecates luau files.

e.g:

```lua
-- Before deprecator
game:GetService("ReplicatedStorage")
task.wait(3)

-- After deprecator
Game:service("ReplicatedStorage")
Wait(3)
```

[You can see a better example in the deprecated file located at test/deprecated.lua or just click here.](https://github.com/gigtih/FileDeprecator/blob/main/test/deprecated.lua)

## Why?

For fun, there is no reason to use deprecated functions, in fact, you should avoid them.
