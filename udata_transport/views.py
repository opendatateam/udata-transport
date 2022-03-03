from flask import Blueprint, current_app

from udata_front import theme
from udata_front.frontend import template_hook


blueprint = Blueprint('transport', __name__, template_folder='templates')


@template_hook()
def dataset_recommendations(ctx):
    return theme.render()
