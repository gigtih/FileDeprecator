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
