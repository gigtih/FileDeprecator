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

### Some problems

There are know issues with the program. For example:

```lua
game:GetService("ReplicatedStorage"):FindFirstChild("Test"):Destroy()

-- Gets deprecated like:
Game:service("ReplicatedStorage"):FindFirstChild("Test"):Destroy()
```

You can get around this bug by doing the following (yes I will fix it):

```lua
game:GetService("ReplicatedStorage")
:FindFirstChild("Test")
:Destroy() -- Same thing as game:GetService("ReplicatedStorage"):FindFirstChild("Test"):Destroy() but with new lines

-- After deprecator
Game:service("ReplicatedStorage")
:findFirstChild("Test")
:destroy()
```
