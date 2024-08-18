from random import choice, randrange


class Beast:
    def __init__(self, name: str, name_set: set):
        self.name = name
        self.name_set = name_set
        self.biter = None


class Beastiary:
    def __init__(self):
        self.zoo = (
            Beast('воробья и всех его друзей', {'воробья', 'воробья и всех его друзей', 'воробушка', 'птицу'}),
            Beast('ночницу (это литучая мыш!)', {'ночницу', 'литучую мыш', 'мыш'}),
            Beast('андатру', {'андатру', 'ондатру'}),
            Beast('чёрного хоря', {'черного хоря', 'чёрного хоря', 'хоря', 'хорька', 'черного хорька',
                                   'чёрного хорька'}),
            Beast('зайца', {'зайца', 'заица'}),
            Beast('еврапейскава леснова ката', {'кота', 'ката', 'еврапейскава леснова ката', 'леснова ката'})
        )

    def find(self, text):
        for beast in self.zoo:
            if text in beast.name_set:
                return beast
        return None

    def find_biter(self, user):
        for beast in self.zoo:
            if user == beast.biter:
                return beast
        return None

    def _bite(self, user, ans):
        beast = choice(self.zoo) if ans in ('жвотне', 'жвотнее', 'жывотне', 'жывотнее') else self.find(ans)
        if beast is None:
            return f'{user} пытаится кусат {ans}. Нет неможно это не совсем правилно!'
        if beast.biter:
            return f'{user} не кусаит {beast.name}, потому что {beast.name} уже кусаит {beast.biter}, ' \
                      'потому что так правилно. Дождитис пока кусание будет закончено!'
        else:
            if randrange(5) == 0:
                return f'{user} не может дагнать жвотне и не кусаит ево!'
            power = choice((' изовсех сил!', ', но несилно.'))
            beast.biter = user
            return f'{user} кусаит {beast.name}{power}'

    def handle(self, msg):
        message = msg.text.strip().lower()
        user = msg.from_user.first_name
        answer = ''
        beast = self.find_biter(user)
        if beast:
            beast.biter = None
            answer = f'{user} открываит рот и болше не кусаит {beast.name}.\n'
        if message.startswith('кусат '):
            return answer + self._bite(user, message[6:])
        return answer
