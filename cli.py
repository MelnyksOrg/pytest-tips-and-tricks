#!/usr/bin/env python3
import click

from mlib.mchange import change


@click.command
@click.option("--amount", prompt="Amount: ", help="This is my change calculation")
def make_change(amount):
    "Gives correct change in coins"
    result = change(float(amount))
    click.echo(click.style(f"Change for {amount}: ", fg="red"))
    for correct_change in result:
        for num, coin in correct_change.items():
            click.echo(click.style(f"{coin}: {num}", fg="green"))
