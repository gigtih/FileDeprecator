--[[ File deprecated with file deprecator by gigtih, https://github.com/gigtih/FileDeprecator Version: 0.1 ]]

--[[
    Testing comments

    game:findFirstChild("Hello")
    Game:service("Test")
]]

local ReplicatedStorage = Game:service("ReplicatedStorage")
local ServerScriptService = Game:service("ServerScriptService")
Wait(3)

if ReplicatedStorage:WaitForChild("Test") ~= nil then
    print("Hello")
end
do
    ServerScriptService:WaitForChild("TestingEnd")
end

ServerScriptService:findFirstChild("Hello")

Game:service("ReplicatedStorage")
:findFirstChild("SomeModule")
:destroy()