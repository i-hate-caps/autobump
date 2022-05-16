import os, discum, time, random
import multiprocessing
#PLEASE DO NOT USE THIS. AUTOMATING ACCOUNTS BREAKS DISCORD TOS AND AUTOMATIC BUMPING IS AGAINST DISBOARD'S RULES. THIS IS SIMPLY A PROOF OF CONCEPT AND TEST OF DISCUM
#Use the following command to install the required discum library: python -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum
#edit the TOKEN, guildID and channelID values to match that of your userbot and account
#do not change the botID unless you intend to bump something other than disboard
#if you would like to automate a different command, change the query and s.get values
#if you would like to change the interval, check the line 13 comment
#the default interval is 2 hours and 2 minutes to avoid conflict and server lag
#special thanks to obviouslymymain123
#With love, ihatecaps
TOKEN = 'TOKEN HERE'
#change these values to adjust interval (default 2hrs2mins(7320) - 2hrs3mins(7380)), set both to the same to disable randomization()
VAL1 = 7320 #min wait
VAL2 = 7380 #max wait
def token():
	bot = discum.Client(token = TOKEN, log=False)
	from discum.utils.slash import SlashCommander
	def bump(resp, guildID, channelID, botID):
		if resp.event.ready_supplemental:
			bot.gateway.request.searchSlashCommands(guildID, limit=10, query="bump") #query slash cmds
		if resp.event.guild_application_commands_updated:
			bot.gateway.removeCommand(bump) #because 2 guild_app_cmd_update events are received...idk ask discord why
			slashCmds = resp.parsed.auto()['application_commands'] #get the slash cmds
			s = SlashCommander(slashCmds, application_id=botID) #for easy slash cmd data creation
			data = s.get(['bump'])
			bot.triggerSlashCommand(botID, channelID=channelID, guildID=guildID, data=data, sessionID=bot.gateway.session_id) #and send it off
	guildID = "832793435358363678"
	channelID = "864272353478443048"
	botID = "302050872383242240"
	bot.gateway.command(
		{
			"function": bump,
			"params": {"guildID": guildID, "channelID": channelID, "botID": botID},
		}
	)
	bot.gateway.run()
if __name__ == '__main__':
	while True:
		proc = multiprocessing.Process(target=token)
		proc.start()
		print('Bumped!')
		time.sleep(10) #LEAVE ME ALONE
		proc.terminate()
		print('Entering Rest...')
		time.sleep(random.randint(VAL1, VAL2))
