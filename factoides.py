import re

from errbot import BotPlugin, botcmd, re_botcmd


class Factoides(BotPlugin):
    """Factoid plugin"""

    factoid_store = {}
    re_learn_factoid = r'^((\w+\s??){1,3}) es (.+?)(\?+)?$'
    re_tell_factoid = r'^(que es )?((\w+\s??){1,3})\?+$'
    re_forget_factoid = r'^olvidar? ((\w+\s??){1,3})$'

    @re_botcmd(pattern=re_learn_factoid, prefixed=True, flags=re.IGNORECASE)
    def aprender_factoides(self, message, match):
        """Guardar un factoid. Example: !agua es humeda """

        factoid = match.group(1)
        content = match.group(3)
        question = match.group(4)

        if question:
            return

        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if factoid in self.factoid_store:
            return "Ya sabia sobre %s." % (factoid)

        self.factoid_store[factoid] = content
        self['FACTOID'] = self.factoid_store

        return "Perfecto, %s es %s" % (format(factoid), format(content))

    @re_botcmd(pattern=re_tell_factoid, prefixed=False, flags=re.IGNORECASE)
    def mostrar_factoid(self, message, match):
        """ Ask about a factoid (prefix not needed). Example: water?  """

        factoid = match.group(2)
        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if factoid in self.factoid_store:
            return "%s es %s" % (factoid, format(self.factoid_store[factoid]))

        else:
            return "No tengo idea de que es %s" % (factoid)

    @re_botcmd(pattern=re_forget_factoid, prefixed=True, flags=re.IGNORECASE)
    def olvidar_factoides(self, message, match):
        """ Forget a factoid.  Example: !forget water """

        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        factoid = match.group(2)

        if factoid in self.factoid_store:
            self.factoid_store.pop(factoid, None)
            self['FACTOID'] = self.factoid_store

            return "OK, me olvido de %s" % (format(factoid))

        else:
            return "No sabia sobre." % (format(factoid))

    @botcmd
    def listar_factoides(self, message, args):
        """ Lista todos los factoides """

        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if self.factoid_store:
            yield "Mi nombre es {} y conozco sobre:" .format(self.bot_config.CHATROOM_FN)
            yield ', '.join(sorted(self.factoid_store.keys()))

        else:
            yield "Todavia no aprendi nada."
