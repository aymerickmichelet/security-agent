import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot_token = 'NzU5ODc2NTU5Nzc5MTM1NTI5.G41uxj.pseMZ3nhsO3-bpsDFFev0JEvBFr4ClKyqFDl6g' # security-agent
# bot_token = 'NzcxODYxMTQ1NTM5NzA2ODgw.G9osxW.nrfcH7VDVktwc2jE3Ay_x4Aut58glKwoErYJlo' # vigile
# channel_id = '952164676815429704'
command_prefix = '!'
bot = commands.Bot(command_prefix=command_prefix, description="Security Agent", intents=intents)


def pseudo_is_unique(members, pseudo):
    is_unique = True
    for member in members:
        is_unique = False if member.nick == pseudo else is_unique
    return is_unique


@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def register(ctx):
    author = ctx.message.author
    await ctx.message.delete()

    # si la commande provient d'un étudiant non gradé
    if len(author.roles) < 2:

        # récupère l'email
        args = ctx.message.content.split(" ")
        if len(args) > 1:
            email_address = args[1]

            # si email existe en xslx,
            if True:

                # récupère le role de l'etudiant
                if len(args) > 2:
                    role = discord.utils.get(ctx.guild.roles, name=args[2].upper())
                    if role is None:
                        return
                    members = ctx.guild.members
                    pseudo = email_address.split("@")[0].lower()

                    # si le pseudo n'existe pas déjà sur le serveur
                    if pseudo_is_unique(members, pseudo):
                        # applique les modifications
                        try:
                            await ctx.author.edit(nick=pseudo)
                            await ctx.author.add_roles(role)
                        except discord.errors.Forbidden:
                            print("Error: Missing Permissions to apply changement for " + ctx.message.author.name)
                        except discord.errors.HTTPException:
                            print("Error: changement failed for " + ctx.message.author.name)


bot.run(bot_token)
