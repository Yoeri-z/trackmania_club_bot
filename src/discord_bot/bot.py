import discord
from math import floor
from src.config import config
from src.storage.models import RoomInfo, LeaderboardEntry

instance = discord.Bot()


_admin = instance.create_group(
    "admin", "Commands for server administrators", guild_ids=[config.GUILD_ID]
)

_campaign = _admin.create_subgroup(
    "campaign",
    "Administrator commands regarding campaigns",
    guild_ids=[config.GUILD_ID],
)

_player = _admin.create_subgroup(
    "player", "Manage what players appear on leaderboards.", guild_ids=[config.GUILD_ID]
)


def _set_persitent_footer(embed: discord.Embed):
    embed.set_footer(text="Trackmania Club bot")


@instance.event
async def on_ready():
    print(f"We have logged in as {instance.user}")


@instance.slash_command(
    description="Send the bot's latency.", guild_ids=[config.GUILD_ID]
)
async def ping(ctx: discord.ApplicationContext):
    latency_ms = floor(instance.latency * 1000)

    embed = discord.Embed(
        title="Pong!",
        description=f"The server latency is {latency_ms}ms.",
        color=discord.Color.green(),
    )

    _set_persitent_footer(embed)

    await ctx.respond(embed=embed)


@instance.slash_command(
    description="Get the leaderboard of a map on the current campaign",
    guild_ids=[config.GUILD_ID],
)
async def get_leaderboard(ctx: discord.ApplicationContext, name: str):
    await ctx.respond("This command has not been implemented yet.")


@instance.slash_command(
    description="Get show the 10 latest pbs your drove", guild_ids=[config.GUILD_ID]
)
async def get_pbs(ctx: discord.ApplicationContext):
    await ctx.respond("This command has not been implemented yet.")


@_campaign.command(
    description="Set up tracking for a new campaign", guild_ids=[config.GUILD_ID]
)
async def track(ctx: discord.ApplicationContext, campaign_uid: str, channel_id: int):
    await ctx.respond("This command has not been implemented yet.")


@_campaign.command(
    description="Remove tracking for a campaign", guild_ids=[config.GUILD_ID]
)
async def untrack(ctx: discord.ApplicationContext, channel_id: int):
    await ctx.respond("This command has not been implemented yet.")


@_player.command(description="Add a player to the blacklist")
async def blacklist(ctx: discord.ApplicationContext, in_game_name: str):
    await ctx.respond("This command has not been implemented yet.")


@_player.command(description="Remove a player from the blacklist")
async def unblacklist(ctx: discord.ApplicationContext, in_game_name: str):
    await ctx.respond("This command has not been implemented yet.")


async def send_position_update(
    channel_id: int, new_entry: LeaderboardEntry, old_entry: LeaderboardEntry | None
):
    pass


async def send_room_update(new_info: RoomInfo):
    pass


def start():
    instance.run(config.DISCORD_TOKEN)
