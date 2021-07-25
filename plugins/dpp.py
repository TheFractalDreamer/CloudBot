import json

from cloudbot import hook

@hook.command("duckdance", autohelp=False)
def duckdance(message):
    message("https://www.youtube.com/watch?v=8An272FPO6E");

@hook.command("ricflair", autohelp=False)
def ricflair(message):
    message("WOOOO! https://media.giphy.com/media/yUI3a7RwLhOFy/giphy.gif");

@hook.command("stitchgif", autohelp=False)
def stitchgif(message):
    message("https://gifimage.net/wp-content/uploads/2018/11/spray-water-bottle-gif-2.gif");
