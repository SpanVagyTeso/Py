class Music:
    def __init__(self,bot):
        self.bot = bot
        self.voice_states = []

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id]=state
        return state

    async def create_voice_client(self,channel):
        voice = await self.bot.join_voice_channel(channel);
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                        self.bot.loop.create_task(state.voice.disconnet())

            except:
                pass

    @commands.command(pass_context=True , no_pm=True)
    async def join(self, ctx, *, channel: discord.Channel):
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            await self.bot.say("Already in a voice channel :c")
