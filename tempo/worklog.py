import datetime
import sys

import click
import requests

from .config import load_config


@click.command()
@click.argument("arguments", nargs=-1)
def logwork(arguments):
    if len(arguments) < 2:
        click.echo("Wrong number of arguments.")
        sys.exit(1)
    issue = arguments[0].upper()
    time = arguments[1]
    desc = " ".join(arguments[2:])

    time_a = time.split(":")
    if len(time_a) > 2:
        click.echo("Wrong time format.")

    if len(time_a) < 2:
        time_a.append(0)

    seconds = (int(time_a[0] or 0) * 60 * 60) + int(time_a[1]) * 60

    click.echo(f"Saving: {issue} - {seconds}s - {desc}")

    config = load_config()
    default = getattr(config, "default", None)
    api_key = getattr(default, "API_KEY", None)
    user_id = getattr(default, "USER_ID", None)


    worklog = {
        "authorAccountId": user_id,
        "billableSeconds": None,
        "description": desc,
        "issueKey": issue,
        "remainingEstimateSeconds": None,
        "startDate": "{}".format(datetime.date.today()),
        "timeSpentSeconds": seconds,
    }

    r = requests.post(
        "https://api.tempo.io/core/3/worklogs",
        json=worklog,
        headers={"Authorization": f"Bearer {api_key}"},
    )

    if r.status_code == 200:
        click.echo("Done.")
    else:
        click.echo(r.status_code)
        click.echo(r.content)
