# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from user import User
from permissions import Permissions
import datetime, re

class Role(object):
    """Represents a Discord role in a :class:`Server`.

    Instance attributes:

    .. attribute:: id

        The ID for the role.
    .. attribute:: name

        The name of the role.
    .. attribute:: permissions

        A :class:`Permissions` that represents the role's permissions.
    """

    def __init__(self, id, name, permissions):
        self.id = id
        self.name = name
        self.permissions = Permissions(permissions)

class Member(User):
    """Represents a Discord member to a :class:`Server`.

    This is a subclass of :class:`User` that extends more functionality
    that server members have such as roles and permissions.

    Instance attributes:

    .. attribute:: deaf

        Specifies if the member is currently deafened by the user.
    .. attribute:: mute

        Specifies if the member is currently muted by the user.
    .. attribute:: roles

        An array of :class:`Role` that the member belongs to.
    .. attribute:: joined_at

        A datetime object that specifies the date and time that the member joined the server for
        the first time.
    """

    def __init__(self, deaf, joined_at, user, roles, mute):
        super(Member, self).__init__(**user)
        self.deaf = deaf
        self.mute = mute
        self.joined_at = datetime.datetime(*map(int, re.split(r'[^\d]', joined_at.replace('+00:00', ''))))
        self.roles = roles

class Server(object):
    """Represents a Discord server.

    Instance attributes:

    .. attribute:: name

        The server name.
    .. attribute:: roles

        An array of :class:`Role` that the server has available.
    .. attribute:: region

        The region the server belongs on.
    .. attribute:: afk_timeout

        The timeout to get sent to the AFK channel.
    .. attribute:: afk_channel_id

        The channel ID for the AFK channel. None if it doesn't exist.
    .. attribute:: members

        An array of :class:`Member` that are currently on the server.
    .. attribute:: channels

        An array of :class:`Channel` that are currently on the server.
    .. attribute:: icon

        The server's icon.
    .. attribute:: id

        The server's ID.
    .. attribute:: owner_id

        The ID of the server's owner.
    """

    def __init__(self, name, roles, region, afk_timeout, afk_channel_id, members, icon, id, owner_id, **kwargs):
        self.name = name
        self.roles = roles
        self.region = region
        self.afk_timeout = afk_timeout
        self.afk_channel_id = afk_channel_id
        self.members = members
        self.icon = icon
        self.id = id
        self.owner_id = owner_id