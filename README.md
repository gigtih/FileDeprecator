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

[You can see a better example in the test folder.](https://github.com/gigtih/FileDeprecator/tree/main/test)

## Why?

For fun, there is no reason to use deprecated functions, in fact, you should avoid them.
