from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
          .format(client))

@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    if message.content.startswith('$start'):
        await message.channel.send("Event")
        def check(m):
            return m.author.id == message.author.id
        Event = await client.wait_for('message',check=check)

        await message.channel.send("Selection")
        Selection = await client.wait_for("message",check=check)

        await message.channel.send("Bookie")
        Bookie = await client.wait_for("message", check=check)

        await message.channel.send("Stake")
        Stake = await client.wait_for("message",check=check)

        await message.channel.send("Odds")
        Odds = await client.wait_for("message",check=check)
        
        await message.channel.send("Sport")
        Sport = await client.wait_for("message",check=check)

        await message.channel.send("Tags")
        Tags = await client.wait_for("message",check=check)

        web = webdriver.Chrome()
        web.get('https://bettin.gs/login')

        Email = 'shihongfoo@gmail.com'
        boxEmail = web.find_element_by_xpath('//*[@id="email"]')
        boxEmail.send_keys(Email)

        Password = "06011712Fsh"
        boxPassword = web.find_element_by_xpath('//*[@id="password"]')
        boxPassword.send_keys(Password)

        Login = web.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/p/input')
        Login.click()
        
        boxEvent = web.find_element_by_xpath('//*[@id="game"]')
        boxEvent.send_keys(Event.content)

        boxSelection = web.find_element_by_xpath('//*[@id="bet"]')
        boxSelection.send_keys(Selection.content)

        
        web.find_element_by_xpath('//*[@id="bookie"]').clear()
        boxBookie = web.find_element_by_xpath('//*[@id="bookie"]')
        boxBookie.send_keys(Bookie.content)

        boxStake = web.find_element_by_xpath('//*[@id="stake"]')
        boxStake.send_keys(Stake.content)

        boxOdds = web.find_element_by_xpath('//*[@id="odds"]')
        boxOdds.send_keys(Odds.content)
        
        boxDetails = web.find_element_by_xpath('//*[@id="quickAddForm"]/div[3]/div[1]/a')
        boxDetails.click()
        
        inputField = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[5]/form/div[4]/div[1]/div/div/input')))
                
        boxSport = web.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[5]/form/div[4]/div[1]/div/div/input')
        arr = Tags.content.split(" ")
        var = Sport.content + Keys.TAB
        for i in arr:
            var += i + Keys.ENTER
        
        boxSport.send_keys(var)
        
        addBet = web.find_element_by_xpath('//*[@id="modalboxAddForm"]/div[7]/div[1]/input')
        addBet.click()


