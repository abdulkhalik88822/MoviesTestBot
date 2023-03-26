import re
import random
import asyncio
from TheHanCock.utils import get_shortlink
from config import AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, API_KEY, AUTH_GROUPS, BUTTON
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant
from TheHanCock.utils import get_filter_results, get_file_details, is_subscribed, get_poster, search_gagala
BUTTONS = {}
BOT = {}
@Client.on_message(filters.text & filters.group & filters.incoming & filters.chat(AUTH_GROUPS) if AUTH_GROUPS else filters.text & filters.group & filters.incoming)
async def group(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        sumit=BOT.get("username")
        if not sumit:
            botusername=await client.get_me()
            sumit=botusername.username
            BOT["username"]=sumit
        files = await get_filter_results(query=search)
        if files:
            btn.append(
                    [
                        InlineKeyboardButton("✅ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ✅", url=f"https://t.me/TheMoviesUpdate/4")
                    ]
                )             
            for file in files:
                file_id = file.file_id
                filename = f"{get_size(file.file_size)} ϟ {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", url=await get_shortlink(f"https://telegram.dog/{sumit}?start=subinps_-_-_-_{file_id}")),]
                )
        else:
            hancock = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton("☉ ʀᴇǫᴜᴇsᴛ", url="https://t.me/Reqstmovies"),
                     InlineKeyboardButton("☉ ʀᴇᴀᴅ", callback_data="cbrules")
                ]
            ]
        )
            rk = await message.reply_text("⭕️ ᴛʜɪs ᴍᴏᴠɪᴇ ɴᴏᴛ ғᴏᴜɴᴅ\n\n⭕️ ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ\n\n⭕️ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴀᴅᴍɪɴ ғᴏʀ ᴜᴘʟᴏᴀᴅɪɴɢ", reply_markup=hancock)
            await asyncio.sleep(30)
            await rk.delete()
            await message.delete()
            return
        if not btn:
            return

        if len(btn) > 8: 
            btns = list(split_list(btn, 8)) 
            keyword = f"{message.chat.id}-{message.id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📄 ᴘᴀɢᴇs 1/1",callback_data="pages")]
            )
            if BUTTON:
                buttons.append([InlineKeyboardButton(text="◉ ᴄʟᴏsᴇ ◉",callback_data="close")])
            poster=None
            if API_KEY:
                poster=await get_poster(search)
            if poster:
                await message.reply_photo(photo=poster, caption=f"<b>ʜᴇʀᴇ ɪs ᴡʜᴀᴛ ɪ ғᴏᴜɴᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ғᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {search} </b>", reply_markup=InlineKeyboardMarkup(buttons))
            else:
                r = await message.reply_text(f"⊚ <code>{search}</code> ᴜᴘʟᴏᴀᴅᴇᴅ\n\n⊚ ɴᴏᴛᴇ :- ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀғᴛᴇʀ 2 ᴍɪɴᴜᴛᴇ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n", reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(120)
                await r.delete()
                await message.delete()
                return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="◉ ɴᴇxᴛ ◉",callback_data=f"next_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📄 ᴘᴀɢᴇs 1/{data['total']}",callback_data="pages")]
        )
        if BUTTON:
            buttons.append([InlineKeyboardButton(text="◉ ᴄʟᴏsᴇ ◉",callback_data="close")])
        poster=None
        if API_KEY:
            poster=await get_poster(search)
        if poster:
            await message.reply_photo(photo=poster, caption=f"<b>ʜᴇʀᴇ ɪs ᴡʜᴀᴛ ɪ ғᴏᴜɴᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ғᴏʀ ǫᴜᴇʀʏ {search} ‌‎</b>", reply_markup=InlineKeyboardMarkup(buttons))
        else:
            r = await message.reply_text(f"⊚ <code>{search}</code> ᴜᴘʟᴏᴀᴅᴇᴅ\n\n⊚ ɴᴏᴛᴇ :- ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀғᴛᴇʀ 2ᴍɪɴᴜᴛᴇs ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.", reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(120)
            await r.delete()
            await message.delete()

    
def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]          



@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):

        if query.data.startswith("next"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴛʜɪs ғᴏʀ ᴏɴᴇ  ᴏғ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇ, ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ᴀɢᴀɪɴ.",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("◉ ʙᴀᴄᴋ ◉", callback_data=f"back_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📄 ᴘᴀɢᴇs {int(index)+2}/{data['total']}", callback_data="pages")]
                )
                if BUTTON:
                    buttons.append([InlineKeyboardButton(text="◉ ᴄʟᴏsᴇ ◉",callback_data="close")])

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("◉ ʙᴀᴄᴋ ◉", callback_data=f"back_{int(index)+1}_{keyword}"),InlineKeyboardButton("◉ ɴᴇxᴛ ◉", callback_data=f"next_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📄 ᴘᴀɢᴇs {int(index)+2}/{data['total']}", callback_data="pages")]
                )
                if BUTTON:
                    buttons.append([InlineKeyboardButton(text="◉ ᴄʟᴏsᴇ ◉",callback_data="close")])

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data.startswith("back"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴛʜɪs ғᴏʀ ᴏɴᴇ  ᴏғ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇ, ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ᴀɢᴀɪɴ.",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("◉ ɴᴇxᴛ ◉", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📄 ᴘᴀɢᴇs {int(index)}/{data['total']}", callback_data="pages")]
                )
                if BUTTON:
                    buttons.append([InlineKeyboardButton(text="◉ ᴄʟᴏsᴇ ◉",callback_data="close")])

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("◉ ʙᴀᴄᴋ ◉", callback_data=f"back_{int(index)-1}_{keyword}"),InlineKeyboardButton("◉ ɴᴇxᴛ ◉", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📄 ᴘᴀɢᴇs {int(index)}/{data['total']}", callback_data="pages")]
                )
                if BUTTON:
                    buttons.append([InlineKeyboardButton(text="◉ ᴄʟᴏsᴇ ◉",callback_data="close")])

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
        


        elif query.data.startswith("subinps"):
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [
                    [
                           InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url="https://t.me/TheMoviesUpdate"),
                           InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ ', url="https://t.me/TheMoviesRequests")
                    ]
                    
                    ]
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        elif query.data.startswith("checksub"):
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                await query.answer("<code>ɪ ʟɪᴋᴇ ʏᴏᴜʀ sᴍᴀʀᴛɴᴇss, ʙᴜᴛ ᴅᴏɴ'ᴛ ʙᴇ ᴏᴠᴇʀsᴍᴀʀᴛ 😒</code>",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{title}"
                buttons = [
                    [
                           InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url="https://t.me/TheMoviesUpdate"),
                           InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ ', url="https://t.me/TheMoviesRequests")
                    ]
                    
                    ]
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


        elif query.data == "pages":
            await query.answer()
        elif query.data == "close":
            try:
                await query.message.reply_to_message.delete()
                await query.message.delete()
            except:
                await query.message.delete()
                
    else:
        await query.answer("🥲 ᴊᴀᴀᴋᴇ ᴀᴘɴᴀ sᴇᴀʀᴄʜ ᴋʀᴏ 👀",show_alert=True)


async def advantage_spell_chok(msg):
    query = re.sub(
        r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e|a)?(l)*(o)*|mal(ayalam)?|t(h)?amil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(u)?(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle(s)?)",
        "", msg.text, flags=re.IGNORECASE)  # plis contribute some common words
    query = query.strip() + " movie"
    g_s = await search_gagala(query)
    g_s += await search_gagala(msg.text)
    gs_parsed = []
    if not g_s:
        k = await msg.reply("I couldn't find any movie in that name.")
        await asyncio.sleep(8)
        await k.delete()
        return
    regex = re.compile(r".*(imdb|wikipedia).*", re.IGNORECASE)  # look for imdb / wiki results
    gs = list(filter(regex.match, g_s))
    gs_parsed = [re.sub(
        r'\b(\-([a-zA-Z-\s])\-\simdb|(\-\s)?imdb|(\-\s)?wikipedia|\(|\)|\-|reviews|full|all|episode(s)?|film|movie|series)',
        '', i, flags=re.IGNORECASE) for i in gs]
    if not gs_parsed:
        reg = re.compile(r"watch(\s[a-zA-Z0-9_\s\-\(\)]*)*\|.*",
                         re.IGNORECASE)  # match something like Watch Niram | Amazon Prime
        for mv in g_s:
            match = reg.match(mv)
            if match:
                gs_parsed.append(match.group(1))
    user = msg.from_user.id if msg.from_user else 0
    movielist = []
    gs_parsed = list(dict.fromkeys(gs_parsed))  # removing duplicates https://stackoverflow.com/a/7961425
    if len(gs_parsed) > 3:
        gs_parsed = gs_parsed[:3]
    if gs_parsed:
        for mov in gs_parsed:
            imdb_s = await get_poster(mov.strip(), bulk=True)  # searching each keyword in imdb
            if imdb_s:
                movielist += [movie.get('title') for movie in imdb_s]
    movielist += [(re.sub(r'(\-|\(|\)|_)', '', i, flags=re.IGNORECASE)).strip() for i in gs_parsed]
    movielist = list(dict.fromkeys(movielist))  # removing duplicates
    if not movielist:
        k = await msg.reply("I couldn't find anything related to that. Check your spelling")
        await asyncio.sleep(8)
        await k.delete()
        return
    SPELL_CHECK[msg.id] = movielist
    btn = [[
        InlineKeyboardButton(
            text=movie.strip(),
            callback_data=f"spolling#{user}#{k}",
        )
    ] for k, movie in enumerate(movielist)]
    btn.append([InlineKeyboardButton(text="Close", callback_data=f'spolling#{user}#close_spellcheck')])
    await msg.reply("I couldn't find anything related to that\nDid you mean any one of these?",
                    reply_markup=InlineKeyboardMarkup(btn))
