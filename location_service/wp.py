from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site_name
from wpadmin.menu import items
from wpadmin.menu.menus import Menu

class TopMenu(Menu):

    def init_with_context(self, context):

        admin_site_name = get_admin_site_name(context)

        self.children += [
            items.MenuItem(
                title='SPOTANEOUS',
                icon='fa-compass',
                css_styles='font-size: 1.5em;',
            ),
        ]


class LeftMenu(Menu):
    def init_with_context(self, context):

        admin_site_name = get_admin_site_name(context)
        user = context.get('request').user

        self.children += [
            items.MenuItem(
                    title=_('Users'),
                    url=reverse('admin:custom_users_customuser_changelist'),
                    enabled=user.has_perm('events.change_customuser'),
                    icon='fa-users'
            ),
            items.MenuItem(
                    title=_('Events'),
                    url=reverse('admin:events_event_changelist'),
                    enabled=user.has_perm('events.change_event'),
                    icon='fa-map-marker'
            ),

            items.MenuItem(
                    title=_('Interests'),
                    url=reverse('admin:interests_interest_changelist'),
                    enabled=user.has_perm('interests.change_interest'),
                    icon='fa-info-circle'
            ),
        ]