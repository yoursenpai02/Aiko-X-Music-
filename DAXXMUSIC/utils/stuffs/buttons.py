from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("𝗖𝗵𝗮𝘁𝗚𝗣𝗧", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣𝗦", callback_data="mplus HELP_Group"),InlineKeyboardButton("𝗦𝗧𝗜𝗖𝗞𝗘𝗥𝗦", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("𝗧𝗔𝗚-𝗔𝗟𝗟", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("𝗜𝗡𝗙𝗢", callback_data="mplus HELP_Info"),InlineKeyboardButton("𝗘𝗫𝗧𝗥𝗔", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("𝗜𝗠𝗔𝗚𝗘", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("Aᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),InlineKeyboardButton("𝗦𝗘𝗔𝗥𝗖𝗛", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("𝗙𝗢𝗡𝗧", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("𝗚𝗔𝗠𝗘𝗦", callback_data="mplus HELP_Game"),InlineKeyboardButton("Ⓣ-𝗚𝗥𝗔𝗣𝗛", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("𝗜𝗠𝗣𝗢𝗦𝗧𝗘𝗥", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("Tʀᴜᴛʜ-ᗪᴀʀᴇ", callback_data="mplus HELP_TD"),InlineKeyboardButton("𝗛𝗔𝗦𝗧𝗔𝗚", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("𝗧𝗧𝗦", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("𝗙𝗨𝗡", callback_data="mplus HELP_Fun"),InlineKeyboardButton("𝗤𝗨𝗢𝗧𝗟𝗬", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
