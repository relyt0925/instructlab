# SPDX-License-Identifier: Apache-2.0

# Third Party
from click_didyoumean import DYMGroup
import click

# Local
from .generate import generate


@click.group(cls=DYMGroup)
@click.pass_context
def data(ctx):
    """Command Group for Interacting with the Data generated by InstructLab.

    If this is your first time running ilab, it's best to start with `ilab config init` to create the environment.
    """
    ctx.obj = ctx.parent.obj
    ctx.default_map = ctx.parent.default_map


data.add_command(generate)
