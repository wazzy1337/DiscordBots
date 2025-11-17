from database import get_total_sins_by_player

def build_sin_summary_description(sinners):
    description = "```\nSinners          | Sins\n-----------------|------\n"
    for sinner in sinners:
        total_sins = get_total_sins_by_player(sinner)
        description += f"{sinner:<16} | {total_sins}\n"
    description += "```"
    return description