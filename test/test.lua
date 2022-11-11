--[[
    Testing comments

    game:FindFirstChild("Hello")
    game:GetService("Test")
]]

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ServerScriptService = game:GetService("ServerScriptService")
task.wait(3)

if ReplicatedStorage:WaitForChild("Test") ~= nil then
    print("Hello")
end
do
    ServerScriptService:WaitForChild("TestingEnd")
end

ServerScriptService:FindFirstChild("Hello")

game:GetService("ReplicatedStorage")
:FindFirstChild("SomeModule")
:Destroy()