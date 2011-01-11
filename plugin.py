###
# Copyright (c) 2011, Aristides Francisco Lourenco
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###
import urllib

import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Lighthouse(callbacks.Plugin):
    """Add the help for "@plugin help Lighthouse" here
    This should describe *how* to use this plugin."""
    threaded = True
    
    def tickets(self, irc, msg, args, channel):
        """[<channel>]

        Returns the link of lighouse tickets of <channel>.  <channel> is
        only necessary if the message isn't sent in the channel itself.
        """
        url = False
        projectId = conf.supybot.plugins.Lighthouse.projectId.get(channel)()
        
        if (projectId):    
            url = format('http://hunch.lighthouseapp.com/projects/%s/tickets', projectId)
        irc.reply(url or 'First you need to set a lighthouse project id for this channel using: config channel <channel> plugins.lighthouse.projectId <project id>')
    tickets = wrap(tickets, ['inChannel'])
    
    def find(self, irc, msg, args, channel, query):
        """[<channel>][<query>] 

        Returns a link to search for <query> in the lighthouse tickets of <channel>.  <channel> is
        only necessary if the message isn't sent in the channel itself.
        """
        url = False
        projectId = conf.supybot.plugins.Lighthouse.projectId.get(channel)()

        if (projectId):
            url = format('http://hunch.lighthouseapp.com/projects/%s/tickets?q=%s', projectId, urllib.quote_plus(query))
        irc.reply(url or 'First you need to set a lighthouse project id for this channel using: config channel <channel> plugins.lighthouse.projectId <project id>')
    find = wrap(find, ['inChannel', 'text'])

Class = Lighthouse


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
