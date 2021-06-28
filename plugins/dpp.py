import json

from cloudbot import hook

@hook.command("duckdance", autohelp=False)
def duckdance(message):
    message("https://www.youtube.com/watch?v=8An272FPO6E");
