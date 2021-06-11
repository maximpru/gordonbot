#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import random2

da = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
      'нилко?', "ва?", 'ры Кубани?', 'рт Вейдер?', 'рт Мол?','мблдор?','вай поженимся?','мбо?','ня Милохин?', 'ёшь молодёжь?',
      'ллаский клуб покупателей?','ша Букина?', "ша Путешественница?", "мир Янов?", "рья?", "нила Козловский?", "ть дуба в округе Юба?",
      "льнобойщики?", "унтонское аббатство?", "Сковорода", "Винчи?", "ры смерти?", "чный ответ?", "нди Крокодил?", "кота Фаннинг?",
      "лай Лама?", "дли Дурсль?", "нила Багров?"]
dmitro = ["Гордон?", "Гордон!", "Ильич Гордон?"]
gordonloh = ["CAACAgIAAxkBAAECYdNgupe0hRFpdmkQENlmQkU1wy09TwACEgADdJypFjoE3jbqKm1pHwQ", "CAACAgIAAxkBAAECYd1gupf7hhyTb4jCJ9CPh1LwigQ9JwACEQADdJypFh7Zfh-1l67THwQ"]
net = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
       "фликс?", "опырь?", "маме привет", "ормози сникерсни?", "ребко?"]
jalko = ["у пчёлки?", "у тарантулика?", "у муравьишки?", "у осочки?", "у шершника?", "у скорпиончика?"]
samolet = ["ковёр-самолёт?", "самокат"]
gde = ["в Караганде", "хочется ответить, но я воздержусь", "тебе в рифму или по факту?", "лучшие тусовки?"]
norm = ["ально?", "ан Ридус?", "ан Озборн?","", "", ""]
kanal = ["Беломорканал?", "ья?", "без к"]
aga = ["", "", "", "", "", "", "та Кристи?", "та Муцениеце?", "йо?", "фон?", "Баба Яга", "пустельга", "в жопе кочерга", "х*й на рога", "в жопе нога"]
sovet = ["да любовь?", "рабочих и крестьян?", "ский союз?"]
mem = ["глух и мем?", "уары гейши?", "орандум?"]
zad = ["ница?", "орнов?", "в будущее?"]
fuf = ["lo?", "aika?"]
zakladka = ["прикоп 5 см", "ненаход"]
suk = ["", "", "","", "", "", "куб?", "ачёв?", "барсук"]
zachem = ["затем", "за шкафом"]
uzhe = ["шире", "куда уж уже!"]
ok = ["", "", "", "", "", "", "", "", "", "рошка?", "тавиус?", "симирон?", "олофутбола?", "сана Акиньшина?", "сана?", "о за око и весь мир ослепнет?", "сид азота?", "аменелость?"]
vopros = ["на размышление даётся 60 секунд", "минута пошла", "отвечает Александр Друзь", "что в чёрном ящике?"]
pasibo = ["", "", "", "спасибо на хлеб не намажешь", "всегда пожалуйста"]
bolt = ["сам ты бот", "ты бот"]
yasno  = ["", "", "", "понятно", "пасмурно"]
gordon = ["в шоколаде?", "Фриман?", "комиссар?", "Рамзи?"]
manda = ["ринка?", "вошка?", "лорец?"]
chmo = ["шник?", "ки чмоки?", "зато без гмо"]
loh = ["несское чудовище?", ""]
pidor = ["ас?", "асина?", "гнойный?"]
kofe = ["В интервью я профи", "Потанцуем?", "варка?"]
trash = ["смэш?", "ер?", "отка?"]
privet = ["медвед?", "интернет?", "госбюджет?", "облсовет?", "минет?", "ленсовет?", "женсовет?", "дармоед?", "людоед?", "пересвет?", "правовед?"]
li = ["Кей?", "зинг?", "труха?", "мпопо?", "за Кудроу?", "зер?", "ла из Футурамы?"]
hach = ["апури по-аджарски?", "апури по-мергрельски?", "апури по-гурийски?", "апури по-имеретински?", "и Старски?"]
salam = ["всем пацанам", "всем городам", "Алейкум"]
tvar = ["дрожащая?", "визжащая?"]
russkiy = ["беларусский", "тунгусский"]
volk = ["слабее льва и тигра?", "в цирке выступает", "в поросятах знает толк?"]
stalin = ["гулаг?", "Двалин", "Балин"]
bruh = ["В чём сила, bruh?", "Не bruh ты мне", "Ну, bruh, ты даёшь!", "Ты так на bruha похож", "bruh за bruha", "свах"]
chelovek = ["паук?", "муравей?", "с бульвара Капуцинов?", "это звучит гордо?"]
sdelat = ["сделай бочку"]
suka = ["", "", "", "чёв?", "даже не знает, что в её спрайте?"]
papa = ["Янгтраппа?", "Римский?", "Джонс?"]
pizda = ["", "", "", "рики?", "рулю?", "тые у меня интервью"]
ahah = ["CAACAgIAAxkBAAECZgRgvpP9VaMz2NFLLPz6zZ10sd1ROQAC7gsAAo_6OErD6vVcDVS4WB8E", "CAACAgIAAxkBAAECZgJgvpP2ZTZa4zfZk47L6IAR6eVUkQACHgADdJypFgTPskgwE3cwHwQ"]
allo = ["CAACAgIAAxkBAAECZgZgvpQPkzW95H7fGm2ndHbkjwftMAACDQADdJypFjlxXeqcLASuHwQ"]
lubov = ["Аксёнова?", "Соболь?", "морковь?", "смерть и роботы?", "Успенская?"]
zvonit1 = ["правильно, звонит, а не звонит", "звонит, а не звонит"]
zvonit = ["правильно, звонит, а не звонит", "звонит, а не звонит", "в колокол?"]
torti = ["торты, а не торты", "правильно, торты, а не торты"]
kosmos = ["из Бригады?", "его же в Бригаде убили"]
chto = ["Где? Гогда?", "такое осень - это небо?", "будет, если бросить лом в унитаз поезда?", "такое бибки?"]
ne = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "тфликс?", "стор Махно?", "грози Южному Централу, попивая сок у себя в квартале?", "забудка - мой любимый цветок?", "шнал географик?", "родись квасивой?", "лли Уварова?"]
ne1 = ["фильтрованного пшеничного?", "пора ли отдохнуть?", "пропустить ли на по рюмашке?"]
odin = ["Локи", "дома?", "в поле не воин?", "ннадцать друзей Оушена?", "очество - сволочь?", "за всех, и все за одного?", 'кирк? Боб Одинкирк? Ну, актёр, который играл в "Лучше звоните Солу". И в "Никто". Все его знают. Может, не по имени, но видели точно все.', ]
dva = ["ch?", "меча? А в штанах ты два хрена носишь?", "лин?", "дцать тысяч лье под водой?", "дцать одно? Очко, так сказать?"]
budu = ["ар императрицы?", "лай?", "щее не предопределено?", "Будду?"]
kupish = ["кукиш", "Купишь уехал в Париж"]
posmotret = ["мои интервью?", "Гордона?"]
smeshno = ["А это я ещё не шутил", "Ахах да", "Обхохочешься!"]
brat = ["сват", "bruh", "за брата - за основу взято", "в чём сила?"]
rak = ["Херак!", "амакафо?"]
koroche = ["дело к ночи?", "у кого короче, тот дома сидит", "длинее", "", ""]
pidoras = ["аль Гуль?", "Эдорас"]
shalava = ["Опять на улице облава","Вокруг тебя дурная слава"]
idinahui = ["жёстко", "грубо", "Ну, пошлём мы друг друга нахер, и чего? Обнимемся и вместе пойдём?"]
soglasen = ["Объявляю вас мужем и женой", "", ""]
tri = ["нити?", "мушкетёра?", "пер?", "цепс?", "цератопс?", "ггеред?", "ваго?", "кстер?"]
chetire = ["комнаты?", "пацана?", "лапы?", "свадьбы и одни похороны?", "народа жили в мире. Всё изменилось, когда Народ Огня развязал войну. Только Аватар, властелин всех четырёх стихий, мог остановить захватчиков. Но, когда мир нуждался в нём больше всего, он исчез. Прошло сто лет, и мы с братом нашли нового Аватара, в маге воздуха по имени Аанг. И хотя его искусство покорения воздуха было велико, ему предстояло ещё многому научиться. Но я верила, что Аанг спасёт мир?"]
pyat = ["ница?", "ница. Других шуток не могу придумать"]
guf = ["овский?", "умер?", "и? Друг Микки Мауса?"]
sem = ["гномов?", "ён Слепаков?", "енович?", "с Кевином Спейси?"]
vosem = ["шутить шутки мы не бросим", "смотреть Гордона мы не бросим"]
kent = ["с кнопкой?", "а завтра мент?", "уки фрайд чикен?", "а Барби?"]
slovo = ["о полку Игореве?", "не воробей?", "целиком? 300 очков на барабане"]
pet = ["ка и Василий Иваныч?", "Пить!"]
rovesnici = ["розимницы?", "ролетницы?", "роосенницы?"]
rovesniki = ["розимники?", "ролетники?", "роосенники?"]
raz = ["на раз или зассал?", "раз раз это хардбас?", "минка окончена. баллы за разминку:", "умовский?"]
put = ["ин?"]
cirk = ["с конями?"]
pomosh = ["скорая?"]
obidelsya = ["на обиженных воду возят", "Обижаться - это всё равно, что выпить яд в надежде, что он убьёт твоих врагов"]
ludi = ["The Люди?", "на блюде?", "верблюди?"]
pyati = ["элемент?", "пятнатый?"]
treti = ["лишний?", "тритий?"]
hui = ["ло?"]
lenin = ["Дашин", "Светин", "Олин", "Катин", "Юлин", "Поленин", "Оленин"]
chislo = ["Пи?", "Авогадро?", "Слевина?", "Фибоначчи?"]
her = ["сонес?", "увим?", "сон?", "омант?"]
bil = ["Клинтон?", "Гейтс?", "Уизли?"]
schitayu = ["деньги?", "ворон?", "овец?"]
haip = ["попыт", "симпл димпл", "сквиш", "спиннер"]
spoki = ["https://borgdotcom.files.wordpress.com/2018/08/trek-spocks.jpg?w=640", "https://www.denofgeek.com/wp-content/uploads/2019/03/star-trek-dc-fontana-on-origins-of-spocks-family-sarek-amanda-grayson.jpg"]
ukos = ["и меня пчела?", "айкос?"]
viski = ["прямые?", "косые", "выбритые?"]
piter = ["Паркер?", "Динклейдж?"]
lisiy = ["иди пописай?", "из Браззерс?"]
disco = ["Элизиум?", "графию Юрия Шатунова?"]
beloe = ["пламя, пляшущее на курганах врагов?", "солнце пустыни?"]
ohota = ["Дикая?", "на карпа?", "Крепкое?"]
slava = ["Украине?", "КПСС?", "Марлоу?"]
volya = ["Павла?"]
vera = ["Брежнева"]
nadejda = ["Бабкина?", "Кадышева?"]
nutipa = ["CAACAgIAAxkBAAECZ5tgwM788SFwn3yk98RrNq-TFTpo9wAC5A4AAk02CErROrPiGZnT7B8E", "CAACAgIAAxkBAAECZ5lgwM74xiS9gb9vzfoBNK_826Km8QACNQ0AAp89CEpcDHw8IEDODB8E", "CAACAgIAAxkBAAECZ5dgwM7y9ngBXmZo1e1h8sGcTurnDgACLQ4AAsRMCEql_kfeWavMDh8E", "CAACAgIAAxkBAAECZ0VgwCvGqANsnn8Rd9hcMbzbCRl4-AACwgADXHekE0Pv8u8c3qiRHwQ", "CAACAgIAAxkBAAECYwVgu5eCoLtckSR0TUAkg8AQ2xDsbwACrAwAAn2ZmUosaUUVbhZdGB8E"]
gosti = ["Глодать кости?", "Жарить гвозди?", "Ломать трости?", "Лежать в компосте?"]
kto = ["Дед Пехто", "Конь в пальто", "Агния Барто", "Бочонок из лото", "Французское шато", "Абстрактное ничто", "Осиное гнездо", "Спортивное авто"]
vopros = ["В каких условиях содержатся заключённые?", "Кто ваш любимый персонаж Игры Престолов?", "Какую планету вы бы хотели посетить?", "Кто вы по знаку зодиака?", "Какой напиток предпочитаете?", "Как вы думаете, что спасёт мир?", "Сколько раз в день вы обычно едите?"]
kant = ["Гегель", "Репликант?", "емир Балагов?"]
predskazuem = ["И не говори!", "Никак не ожидал, что ты это скажешь!", "На самом деле, люди очень прдесказукемы"]
kameru = ["одиночную?", "обскуру?"]
bilo = ["", "", "", "", "", "Да сплыло", "Да всплыло"]
zdorova = ["", "", "Здоровее видали", "Здоровенькi, були!"]
katz = ["товары?", "доктор Кац?"]
start = ["1. Добавьте меня в чат. \n2. Дайте мне доступ к сообщениям. \n3. Наслаждайтесь моим искромётным юмором. \nНе нужно давать никаких команд! Просто общайтесь, а я сам буду вставлять шутки, как только увижу подходящий (нет) момент.\n\nТак я работаю:"]
rublya = ["На постройку корабля?", "На покупку букваря?"]
rubley = ["На постройку кораблей?", "На покупку букварей?"]
rost = ["и Нагиев?"]
kolu = ["Что колешь?", "чую проволоку?"]
beliy = ["Саша?", "Волк?", "Анатолий?"]
serso = ["Это нерусское слово!", "А как же?", "Его можно найти в любом словаре, на обложке которого написано 'Словарь русского языка'", "Да заберите себе это очко!"]
supir = ["блиц?", "игра?", "бобровы?"]
kruk = ["Борис?", "Капитан?"]
yashik = ["Отвечает Фёдор Двинятин", "Господин Ведущий", "Принадлежности для игры в Серсо", "Выкройки", "Салат кайсо", "Там пусто!"]
breiten = ["Румпельштильцкен", "Биохакер", "Бьютиблогер", "Брайтоньбичер", "Крастибургер", "Баронбукин", "Брендонфрейзер"]
bot=telebot.TeleBot('1862894498:AAFsZOqXP68dMbrcbserspYCT7sZl2mHMU4')

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

   if message.text == "да":
      bot.send_message(message.chat.id, random2.choice(da), reply_to_message_id=message.message_id)
   elif message.text == "Да":
      bot.send_message(message.chat.id, random2.choice(da), reply_to_message_id=message.message_id)
   elif message.text.endswith (" да"):
      bot.send_message(message.chat.id, random2.choice(da), reply_to_message_id=message.message_id)
   elif message.text.endswith ("Да"):
      bot.send_message(message.chat.id, random2.choice(da), reply_to_message_id=message.message_id)

   elif message.text == "рост":
      bot.send_message(message.chat.id, random2.choice(rost), reply_to_message_id=message.message_id)
   elif message.text.endswith (" рост"):
      bot.send_message(message.chat.id, random2.choice(rost), reply_to_message_id=message.message_id)
   elif message.text.endswith ("Рост"):
      bot.send_message(message.chat.id, random2.choice(rost), reply_to_message_id=message.message_id)

   elif message.text == "Дмитро":
      bot.send_message(message.chat.id, random2.choice(dmitro), reply_to_message_id=message.message_id)
   elif message.text == "дмитро":
      bot.send_message(message.chat.id, random2.choice(dmitro), reply_to_message_id=message.message_id)
   elif message.text.endswith ("Дмитрий"):
      bot.send_message(message.chat.id, random2.choice(dmitro), reply_to_message_id=message.message_id)
   elif message.text.endswith ("дмитрий"):
      bot.send_message(message.chat.id, random2.choice(dmitro), reply_to_message_id=message.message_id)

   elif message.text.startswith("А0а0а"):
     bot.send_message(message.chat.id, "ты чего смеёшься, как робот?", reply_to_message_id=message.message_id)
   elif message.text.startswith("0а0а"):
     bot.send_message(message.chat.id, "странный у тебя смех", reply_to_message_id=message.message_id)


   elif message.text.find("гордон лох") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find('Гордон лох') != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("тупой бот") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("Тупой бот") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("Крым русский") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("Крым - Россия") !=-1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("Иди нахуй") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("Иди нахуй") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("Пошёл нахуй") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find("Пошёл нахуй") !=-1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)

   elif message.text.endswith("от накала"):
     bot.send_message(message.chat.id, "От такого", reply_to_message_id=message.message_id)
   elif message.text.endswith("От накала"):
     bot.send_message(message.chat.id, "От такого", reply_to_message_id=message.message_id)
   elif message.text == "от такого":
     bot.send_message(message.chat.id, "У него", reply_to_message_id=message.message_id)
   elif message.text.endswith(" от такого"):
     bot.send_message(message.chat.id, "У него", reply_to_message_id=message.message_id)
   elif message.text.endswith("От такого"):
     bot.send_message(message.chat.id, "у него", reply_to_message_id=message.message_id)
   elif message.text == "у него":
     bot.send_message(message.chat.id, "На полшестого", reply_to_message_id=message.message_id)
   elif message.text.endswith("такого у него"):
     bot.send_message(message.chat.id, "На полшестого", reply_to_message_id=message.message_id)
   elif message.text.endswith("У него"):
     bot.send_message(message.chat.id, "На полшестого", reply_to_message_id=message.message_id)

   elif message.text == "на полшестого":
     bot.send_message(message.chat.id, "И зовут", reply_to_message_id=message.message_id)
   elif message.text.endswith("у него на полшестого"):
     bot.send_message(message.chat.id, "И зовут", reply_to_message_id=message.message_id)
   elif message.text.endswith("На полшестого"):
     bot.send_message(message.chat.id, "И зовут", reply_to_message_id=message.message_id)

   elif message.text == "и зовут":
     bot.send_message(message.chat.id, "Его в России", reply_to_message_id=message.message_id)
   elif message.text.endswith("И зовут"):
     bot.send_message(message.chat.id, "Его в России", reply_to_message_id=message.message_id)
   elif message.text.endswith("шестого и зовут"):
     bot.send_message(message.chat.id, "Его в России", reply_to_message_id=message.message_id)
   elif message.text == "его в России":
     bot.send_message(message.chat.id, "Наш вечерний мудозвон!", reply_to_message_id=message.message_id)
   elif message.text.endswith("Его в России"):
     bot.send_message(message.chat.id, "Наш вечерний мудозвон!", reply_to_message_id=message.message_id)
   elif message.text.endswith("зовут его в России"):
     bot.send_message(message.chat.id, "Наш вечерний мудозвон!", reply_to_message_id=message.message_id)
   elif message.text == "наш вечерний":
     bot.send_message(message.chat.id, "Мудозвон!", reply_to_message_id=message.message_id)
   elif message.text.endswith("Наш вечерний"):
     bot.send_message(message.chat.id, "Мудозвон!", reply_to_message_id=message.message_id)
   elif message.text.endswith("оссии наш вечерний"):
     bot.send_message(message.chat.id, "Мудозвон!", reply_to_message_id=message.message_id)
   elif message.text.find("аш вечерний мудозвон") != -1:
     bot.send_message(message.chat.id, "Вы поёте восхитительно!", reply_to_message_id=message.message_id)
   elif message.text.find("аш Вечерний Мудозвон") != -1:
     bot.send_message(message.chat.id, "Вы поёте восхитительно!", reply_to_message_id=message.message_id)


   elif message.text.endswith("встал?"):
     bot.send_message(message.chat.id, "и не только он", reply_to_message_id=message.message_id)
   elif message.text.endswith("встал"):
     bot.send_message(message.chat.id, "и не только он", reply_to_message_id=message.message_id)

   elif message.text == ("нет"):
     bot.send_message(message.chat.id, random2.choice(net), reply_to_message_id=message.message_id)
   elif message.text.endswith(" нет"):
     bot.send_message(message.chat.id, random2.choice(net), reply_to_message_id=message.message_id)
   elif message.text.endswith("Нет"):
     bot.send_message(message.chat.id, random2.choice(net), reply_to_message_id=message.message_id)

   elif message.text.endswith("Барак"):
     bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECYyNgu6pk4tEo7nNRKV2n9JbsxVM1awACJgADdJypFt-zINE_EqsTHwQ", reply_to_message_id=message.message_id)
   elif message.text.endswith("барак"):
     bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECYyNgu6pk4tEo7nNRKV2n9JbsxVM1awACJgADdJypFt-zINE_EqsTHwQ", reply_to_message_id=message.message_id)
   elif message.text.endswith(" барак"):
     bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECYyNgu6pk4tEo7nNRKV2n9JbsxVM1awACJgADdJypFt-zINE_EqsTHwQ", reply_to_message_id=message.message_id)


   elif message.text.endswith(" муж"):
     bot.send_message(message.chat.id, "объелся груш?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Муж"):
     bot.send_message(message.chat.id, "объелся груш?", reply_to_message_id=message.message_id)

   elif message.text.endswith("жалко..."):
     bot.send_message(message.chat.id, random2.choice (jalko), reply_to_message_id=message.message_id)
   elif message.text.endswith("жалко"):
     bot.send_message(message.chat.id, random2.choice (jalko), reply_to_message_id=message.message_id)
   elif message.text.endswith("Жалко"):
     bot.send_message(message.chat.id, random2.choice (jalko), reply_to_message_id=message.message_id)
   elif message.text.endswith("жалко?"):
     bot.send_message(message.chat.id, random2.choice (jalko), reply_to_message_id=message.message_id)

   elif message.text.endswith("ходор"):
     bot.send_message(message.chat.id, "ковский?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Ходор"):
     bot.send_message(message.chat.id, "ковский?", reply_to_message_id=message.message_id)
   elif message.text.endswith("ходор?"):
     bot.send_message(message.chat.id, "ковский?", reply_to_message_id=message.message_id)

   elif message.text.find("за воротник") != -1:
     bot.send_message(message.chat.id, "Заворотнюк", reply_to_message_id=message.message_id)
   elif message.text.find("За воротник") != -1:
     bot.send_message(message.chat.id, "Заворотнюк", reply_to_message_id=message.message_id)

   elif message.text.find("задержали") != -1:
     bot.send_message(message.chat.id, "раздрожает, когда спешишь куда-нибудь, а тебя задерживают.", reply_to_message_id=message.message_id)

   elif message.text.endswith("Марс"):
      bot.send_message (message.chat.id, "сникерс", reply_to_message_id=message.message_id)
   elif message.text.endswith("Марс?"):
      bot.send_message (message.chat.id, "сникерс", reply_to_message_id=message.message_id)
   elif message.text.endswith("марс"):
      bot.send_message (message.chat.id, "сникерс", reply_to_message_id=message.message_id)
   elif message.text.endswith("марс?"):
      bot.send_message (message.chat.id, "сникерс", reply_to_message_id=message.message_id)

   elif message.text.endswith("гордон"):
      bot.send_message (message.chat.id, random2.choice (gordon), reply_to_message_id=message.message_id)
   elif message.text.endswith("Гордон"):
      bot.send_message (message.chat.id, random2.choice (gordon), reply_to_message_id=message.message_id)

   elif message.text.endswith(" прав"):
      bot.send_message (message.chat.id, "лев", reply_to_message_id=message.message_id)
   elif message.text.endswith(" лев"):
      bot.send_message (message.chat.id, "Лещенко?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Лев"):
      bot.send_message (message.chat.id, "Лещенко?", reply_to_message_id=message.message_id)
   elif message.text.find("лев") != -1:
     bot.send_sticker(message.chat.id, "Лещенко?", reply_to_message_id=message.message_id)
   elif message.text.find("прав") != -1:
     bot.send_sticker(message.chat.id, "лев", reply_to_message_id=message.message_id)

   elif message.text.endswith("амолёт"):
     bot.send_message(message.chat.id, random2.choice (samolet), reply_to_message_id=message.message_id)

   elif message.text.endswith(" где"):
      bot.send_message (message.chat.id, random2.choice (gde), reply_to_message_id=message.message_id)
   elif message.text.endswith(" где?"):
      bot.send_message (message.chat.id, random2.choice (gde), reply_to_message_id=message.message_id)
   elif message.text.endswith("Где?"):
      bot.send_message (message.chat.id, random2.choice (gde), reply_to_message_id=message.message_id)
   elif message.text.endswith("Где"):
      bot.send_message (message.chat.id, random2.choice (gde), reply_to_message_id=message.message_id)

   elif message.text.endswith("Норм"):
      bot.send_message (message.chat.id, random2.choice (norm), reply_to_message_id=message.message_id)
   elif message.text.endswith("норм"):
      bot.send_message (message.chat.id, random2.choice (norm), reply_to_message_id=message.message_id)

   elif message.text.endswith("канал"):
      bot.send_message (message.chat.id, random2.choice (kanal), reply_to_message_id=message.message_id)
   elif message.text.endswith("канал?"):
      bot.send_message (message.chat.id, random2.choice (kanal), reply_to_message_id=message.message_id)

   elif message.text.endswith(" ага"):
      bot.send_message (message.chat.id, random2.choice (aga), reply_to_message_id=message.message_id)
   elif message.text == "ага":
      bot.send_message (message.chat.id, random2.choice (aga), reply_to_message_id=message.message_id)
   elif message.text == "Ага":
      bot.send_message (message.chat.id, random2.choice (aga), reply_to_message_id=message.message_id)

   elif message.text == "ну типа":
      bot.send_sticker(message.chat.id, random2.choice (nutipa))
   elif message.text == "Ну типа":
      bot.send_sticker(message.chat.id, random2.choice (nutipa))

   elif message.text.endswith("совет"):
      bot.send_message (message.chat.id, random2.choice (sovet), reply_to_message_id=message.message_id)

   elif message.text.endswith("камеру"):
      bot.send_message (message.chat.id, random2.choice (kameru), reply_to_message_id=message.message_id)
   elif message.text.endswith("камеру?"):
      bot.send_message (message.chat.id, random2.choice (kameru), reply_to_message_id=message.message_id)

   elif message.text.find("слава Украине") != -1:
     bot.send_message(message.chat.id, "Героям слава!", reply_to_message_id=message.message_id)
   elif message.text.find("Слава Украине") != -1:
     bot.send_message(message.chat.id, "Героям слава!", reply_to_message_id=message.message_id)
   elif message.text.find("слава украине") != -1:
     bot.send_message(message.chat.id, "Героям слава!", reply_to_message_id=message.message_id)
   elif message.text.find("сало уронили") != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)
   elif message.text.find('Сало уронили') != -1:
     bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)

   elif message.text.endswith(" мем"):
     bot.send_message (message.chat.id, random2.choice (mem), reply_to_message_id=message.message_id)

   elif message.text.endswith("зад"):
      bot.send_message (message.chat.id, random2.choice (zad), reply_to_message_id=message.message_id)

   elif message.text.endswith("fuf"):
      bot.send_message (message.chat.id, random2.choice (fuf), reply_to_message_id=message.message_id)

   elif message.text.endswith("акладка"):
      bot.send_message (message.chat.id, random2.choice (zakladka), reply_to_message_id=message.message_id)

   elif message.text == "сук":
      bot.send_message (message.chat.id, random2.choice (suk), reply_to_message_id=message.message_id)
   elif message.text.endswith(" сук"):
      bot.send_message (message.chat.id, random2.choice (suk), reply_to_message_id=message.message_id)
   elif message.text.endswith("Сук"):
      bot.send_message (message.chat.id, random2.choice (suk), reply_to_message_id=message.message_id)

   elif message.text.endswith("уже"):
     bot.send_message (message.chat.id, random2.choice (uzhe), reply_to_message_id=message.message_id)

   elif message.text == "ок":
     bot.send_message(message.chat.id, random2.choice (ok), reply_to_message_id=message.message_id)
   elif message.text.endswith("Ок"):
     bot.send_message(message.chat.id, random2.choice (ok), reply_to_message_id=message.message_id)

   elif message.text.endswith("рики"):
      bot.send_message (message.chat.id, "тикки тави?", reply_to_message_id=message.message_id)

   elif message.text.endswith("вопрос"):
      bot.send_message (message.chat.id, random2.choice (vopros), reply_to_message_id=message.message_id)

   elif message.text == "папа":
      bot.send_message(message.chat.id, random2.choice (papa), reply_to_message_id=message.message_id)
   elif message.text.endswith("Папа"):
      bot.send_message(message.chat.id, random2.choice (papa), reply_to_message_id=message.message_id)
   elif message.text.endswith(" папа"):
      bot.send_message(message.chat.id, random2.choice (papa), reply_to_message_id=message.message_id)

   elif message.text.endswith("Отец"):
      bot.send_message(message.chat.id, "молодец", reply_to_message_id=message.message_id)
   elif message.text == "отец":
      bot.send_message(message.chat.id, "Крёстный?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" отец"):
      bot.send_message(message.chat.id, "молодец", reply_to_message_id=message.message_id)

   elif message.text.startswith("тупой"):
      bot.send_message (message.chat.id, "острый", reply_to_message_id=message.message_id)
   elif message.text.startswith("Тупой"):
      bot.send_message (message.chat.id, "Острый", reply_to_message_id=message.message_id)

   elif message.text.find("здорова") != -1:
      bot.send_message(message.chat.id, random2.choice (zdorova), reply_to_message_id=message.message_id)
   elif message.text.find("Здорова") != -1:
      bot.send_message(message.chat.id, random2.choice (zdorova), reply_to_message_id=message.message_id)

   elif message.text.endswith(" кац"):
      bot.send_message (message.chat.id, random2.choice (katz), reply_to_message_id=message.message_id)
   elif message.text.endswith("Кац"):
      bot.send_message (message.chat.id, random2.choice (katz), reply_to_message_id=message.message_id)

   elif message.text.endswith("Сталин"):
      bot.send_message (message.chat.id, random2.choice (stalin), reply_to_message_id=message.message_id)
   elif message.text.endswith("сталин"):
      bot.send_message (message.chat.id, random2.choice (stalin), reply_to_message_id=message.message_id)

   elif message.text.endswith("Гениально"):
      bot.send_message (message.chat.id, "Евгениально", reply_to_message_id=message.message_id)
   elif message.text.endswith(" гениально"):
      bot.send_message (message.chat.id, "Евгениально", reply_to_message_id=message.message_id)

   elif message.text.startswith("/start"):
       bot.send_message (message.chat.id, random2.choice (start), reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, "https://i.postimg.cc/ZqXxfsV0/photo-2021-06-09-22-45-49.jpg") and bot.send_photo(message.chat.id, "https://i.postimg.cc/7L5Nnr1p/photo-2021-06-09-22-45-49-2.jpg")


   elif message.text.endswith ("джеком"):
       bot.send_message (message.chat.id, "и шлюхами?", reply_to_message_id=message.message_id)

   elif message.text.endswith ("пиво"):
       bot.send_message (message.chat.id, "варов?", reply_to_message_id=message.message_id)
   elif message.text.endswith ("Пиво"):
       bot.send_message (message.chat.id, "варов?", reply_to_message_id=message.message_id)

   elif message.text.endswith ("околад"):
       bot.send_message (message.chat.id, "в Гордоне?", reply_to_message_id=message.message_id)

   elif message.text.endswith ("пасибо"):
       bot.send_message (message.chat.id, random2.choice (pasibo), reply_to_message_id=message.message_id)

   elif message.text.endswith ("бот"):
       bot.send_message (message.chat.id, random2.choice (bolt), reply_to_message_id=message.message_id)

   elif message.text.endswith ("гордонбот"):
       bot.send_message (message.chat.id, random2.choice (bolt), reply_to_message_id=message.message_id)
   elif message.text.endswith ("ГордонБот"):
       bot.send_message (message.chat.id, random2.choice (bolt), reply_to_message_id=message.message_id)

   elif message.text.startswith ("НЕТ ТЫ"):
       bot.send_message (message.chat.id, "Чё орёшь, бот?", reply_to_message_id=message.message_id)
   elif message.text.startswith ("НЕТ, ТЫ"):
       bot.send_message (message.chat.id, "Чё орёшь, бот?", reply_to_message_id=message.message_id)
   elif message.text.startswith ("Нет ты!"):
       bot.send_message (message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.startswith ("Нет, ты!"):
       bot.send_message (message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.startswith ("нет ты!"):
       bot.send_message (message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.startswith ("нет, ты!"):
       bot.send_message (message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.find(" нет, ты") != -1:
      bot.send_message(message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.find(" нет ты") != -1:
      bot.send_message(message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.find("Нет, ты") != -1:
      bot.send_message(message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.find("Нет ты") != -1:
      bot.send_message(message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text.find("НеТ тЫ") != -1:
      bot.send_message(message.chat.id, "НеТ тЫ", reply_to_message_id=message.message_id)
   elif message.text.find("нЕт тЫ") != -1:
      bot.send_message(message.chat.id, "нЕт тЫ", reply_to_message_id=message.message_id)
   elif message.text.find("HET Tbl") != -1:
      bot.send_message(message.chat.id, "нет ты", reply_to_message_id=message.message_id)
   elif message.text == "ты":
      bot.send_message(message.chat.id, "попой нюхаешь цветы?", reply_to_message_id=message.message_id)
   elif message.text == "Ты":
      bot.send_message(message.chat.id, "попой кушаешь торты?", reply_to_message_id=message.message_id)

   elif message.text.find("выпьем") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("Выпьем") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("выпить") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("Выпить") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("отметим") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("Отметим") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("отметить") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("Отметить") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("бухнём") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("Бухнём") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("бухать") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)
   elif message.text.find("Бухать") != -1:
      bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECY29gu97aYHg2lxnidTQZQQGds1jYvQACHwADdJypFi-pOnvSySiPHwQ", reply_to_message_id=message.message_id)

   elif message.text.endswith ("особо"):
       bot.send_message (message.chat.id, "опасен?", reply_to_message_id=message.message_id)

   elif message.text == "ясно":
       bot.send_message (message.chat.id, random2.choice (yasno), reply_to_message_id=message.message_id)
   elif message.text.endswith (" ясно"):
       bot.send_message (message.chat.id, random2.choice (yasno), reply_to_message_id=message.message_id)
   elif message.text.endswith ("Ясно"):
       bot.send_message (message.chat.id, random2.choice (yasno), reply_to_message_id=message.message_id)

   elif message.text.find("написать симфонию") != -1:
       bot.send_message(message.chat.id, "А ты можешь?" , reply_to_message_id=message.message_id)
   elif message.text.find("создать шедевр") != -1:
       bot.send_message(message.chat.id, "А ты можешь?" , reply_to_message_id=message.message_id)

   elif message.text.find("Гордон может отсосать") != -1:
      bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)

   elif message.text.endswith (" ту"):
       bot.send_message (message.chat.id, "ту ту, на на на, снова вместе, снова рядом?", reply_to_message_id=message.message_id)
   elif message.text.endswith ("Ту"):
       bot.send_message (message.chat.id, "ту ту, на на на, снова вместе, снова рядом?", reply_to_message_id=message.message_id)

   elif message.text.endswith("За май"):
       bot.send_message(message.chat.id, "Из Антихайпа?", reply_to_message_id=message.message_id)
   elif message.text.endswith("За Май"):
       bot.send_message(message.chat.id, "и Гнойный?", reply_to_message_id=message.message_id)
   elif message.text.endswith("за май"):
       bot.send_message(message.chat.id, "Из Антихайпа?", reply_to_message_id=message.message_id)
   elif message.text.endswith("за Май"):
       bot.send_message(message.chat.id, "и Гнойный?", reply_to_message_id=message.message_id)

   elif message.text.endswith("май"):
       bot.send_message(message.chat.id, "Абрикосов?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Май"):
       bot.send_message(message.chat.id, "Абрикосов?", reply_to_message_id=message.message_id)

   elif message.text.find("внутри червяка") != -1:
       bot.send_message(message.chat.id, "Найти там двух червяков", reply_to_message_id=message.message_id)
   elif message.text.find("там червяка") != -1:
       bot.send_message(message.chat.id, "Найти там двух червяков", reply_to_message_id=message.message_id)

   elif message.text.endswith("Пи"):
       bot.send_message(message.chat.id, "кули?", reply_to_message_id=message.message_id)
   elif message.text.endswith("пи"):
       bot.send_message(message.chat.id, "кули?", reply_to_message_id=message.message_id)

   elif message.text.endswith("Идрак"):
       bot.send_message(message.chat.id, "как?", reply_to_message_id=message.message_id)
   elif message.text.endswith("идрак"):
       bot.send_message(message.chat.id, "как?", reply_to_message_id=message.message_id)

   elif message.text.endswith("попит"):
       bot.send_message(message.chat.id, "а поест?", reply_to_message_id=message.message_id)
   elif message.text.endswith("попыт"):
       bot.send_message(message.chat.id, "а поест?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Попит"):
       bot.send_message(message.chat.id, "а поест?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Попыт"):
       bot.send_message(message.chat.id, "а поест?", reply_to_message_id=message.message_id)

   elif message.text.endswith("Ладно"):
       bot.send_message(message.chat.id, "Прохладно", reply_to_message_id=message.message_id)

   elif message.text.endswith(" вот"):
       bot.send_message(message.chat.id, "новый поворот, и мотор ревёт?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Вот"):
       bot.send_message(message.chat.id, "новый поворот?", reply_to_message_id=message.message_id)

   elif message.text.endswith("соло"):
       bot.send_message(message.chat.id, "вьёв?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Cоло"):
       bot.send_message(message.chat.id, "вьёв?", reply_to_message_id=message.message_id)

   elif message.text.endswith("гены"):
       bot.send_message(message.chat.id, "Букины?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Гены"):
       bot.send_message(message.chat.id, "Букины?", reply_to_message_id=message.message_id)

   elif message.text.endswith("мама"):
       bot.send_message(message.chat.id, "Обама", reply_to_message_id=message.message_id)
   elif message.text.endswith("Мама"):
       bot.send_message(message.chat.id, "Обама", reply_to_message_id=message.message_id)

   elif message.text.endswith("судак"):
       bot.send_message(message.chat.id, "тудак", reply_to_message_id=message.message_id)
   elif message.text.endswith("Судак"):
       bot.send_message(message.chat.id, "Тудак", reply_to_message_id=message.message_id)

   elif message.text.endswith("bruh"):
       bot.send_message(message.chat.id, random2.choice (bruh), reply_to_message_id=message.message_id)
   elif message.text.endswith("Bruh"):
       bot.send_message(message.chat.id, random2.choice (bruh), reply_to_message_id=message.message_id)

   elif message.text.endswith("кофе"):
       bot.send_message(message.chat.id, random2.choice (kofe), reply_to_message_id=message.message_id)
   elif message.text.endswith("Кофе"):
       bot.send_message(message.chat.id, random2.choice (kofe), reply_to_message_id=message.message_id)

   elif message.text.endswith("пидор"):
       bot.send_message(message.chat.id, random2.choice (pidor), reply_to_message_id=message.message_id)
   elif message.text.endswith("Пидор"):
       bot.send_message(message.chat.id, random2.choice (pidor), reply_to_message_id=message.message_id)

   elif message.text.endswith("лох"):
       bot.send_message(message.chat.id, random2.choice (loh), reply_to_message_id=message.message_id)
   elif message.text.endswith("Лох"):
       bot.send_message(message.chat.id, random2.choice (loh), reply_to_message_id=message.message_id)

   elif message.text.endswith("чмо"):
       bot.send_message(message.chat.id, random2.choice (chmo), reply_to_message_id=message.message_id)
   elif message.text.endswith("Чмо"):
       bot.send_message(message.chat.id, random2.choice (chmo), reply_to_message_id=message.message_id)

   elif message.text.endswith("трэш"):
       bot.send_message(message.chat.id, random2.choice (trash), reply_to_message_id=message.message_id)
   elif message.text.endswith("Трэш"):
       bot.send_message(message.chat.id, random2.choice (trash), reply_to_message_id=message.message_id)

   elif message.text == "манда":
       bot.send_message(message.chat.id, random2.choice (manda), reply_to_message_id=message.message_id)
   elif message.text.endswith("Манда"):
       bot.send_message(message.chat.id, random2.choice (manda), reply_to_message_id=message.message_id)
   elif message.text.endswith(" манда"):
       bot.send_message(message.chat.id, random2.choice (manda), reply_to_message_id=message.message_id)
   elif message.text.endswith(" manda"):
       bot.send_message(message.chat.id, random2.choice (manda), reply_to_message_id=message.message_id)

   elif message.text.endswith("плебей"):
       bot.send_message(message.chat.id, "плейбой?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Плебей"):
       bot.send_message(message.chat.id, "Плейбой?", reply_to_message_id=message.message_id)

   elif message.text.endswith(" ли"):
       bot.send_message(message.chat.id, random2.choice (li), reply_to_message_id=message.message_id)
   elif message.text.endswith("Ли"):
       bot.send_message(message.chat.id, random2.choice (li), reply_to_message_id=message.message_id)

   elif message.text.endswith("рехаб"):
       bot.send_message(message.chat.id, "порнхаб?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Рехаб"):
       bot.send_message(message.chat.id, "Порнхаб?", reply_to_message_id=message.message_id)

   elif message.text.endswith("хач"):
       bot.send_message(message.chat.id, random2.choice (hach), reply_to_message_id=message.message_id)
   elif message.text.endswith("Хач"):
       bot.send_message(message.chat.id, random2.choice (hach), reply_to_message_id=message.message_id)

   elif message.text.find(' на Украине') != -1:
     bot.send_message(message.chat.id, "В Украине!", reply_to_message_id=message.message_id) and bot.send_sticker(message.chat.id, random2.choice(gordonloh))
   elif message.text.find(' на украине') != -1:
     bot.send_message(message.chat.id, "В Украине!", reply_to_message_id=message.message_id) and bot.send_sticker(message.chat.id, random2.choice(gordonloh))

   elif message.text.endswith("салам"):
       bot.send_message(message.chat.id, random2.choice (salam), reply_to_message_id=message.message_id)
   elif message.text.endswith("Салам"):
       bot.send_message(message.chat.id, random2.choice (salam), reply_to_message_id=message.message_id)

   elif message.text.endswith("тварь"):
       bot.send_message(message.chat.id, random2.choice (tvar), reply_to_message_id=message.message_id)
   elif message.text.endswith("Тварь"):
       bot.send_message(message.chat.id, random2.choice (tvar), reply_to_message_id=message.message_id)

   elif message.text == "русский":
       bot.send_message(message.chat.id, random2.choice (russkiy), reply_to_message_id=message.message_id)
   elif message.text.endswith("Русский"):
       bot.send_message(message.chat.id, random2.choice (russkiy), reply_to_message_id=message.message_id)
   elif message.text.endswith(" русский"):
       bot.send_message(message.chat.id, random2.choice (russkiy), reply_to_message_id=message.message_id)
   elif message.text.endswith(" нерусский"):
       bot.send_message(message.chat.id, random2.choice (russkiy), reply_to_message_id=message.message_id)

   elif message.text == "тем не менее":
       bot.send_message(message.chat.id, "тем не более", reply_to_message_id=message.message_id)
   elif message.text.endswith("Тем не менее"):
       bot.send_message(message.chat.id, "тем не более", reply_to_message_id=message.message_id)
   elif message.text.endswith(" тем не менее"):
       bot.send_message(message.chat.id, "тем не более", reply_to_message_id=message.message_id)

   elif message.text.endswith("Твою мать"):
       bot.send_message(message.chat.id, "Мать - это святое", reply_to_message_id=message.message_id)
   elif message.text.endswith("твою мать"):
       bot.send_message(message.chat.id, "Мать - это святое", reply_to_message_id=message.message_id)

   elif message.text.endswith("Начать"):
       bot.send_message(message.chat.id, "и кончить?", reply_to_message_id=message.message_id)
   elif message.text.endswith("начать"):
       bot.send_message(message.chat.id, "и кончить?", reply_to_message_id=message.message_id)

   elif message.text.endswith("жаба"):
       bot.send_message(message.chat.id, "Аркадьевна?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Жаба"):
       bot.send_message(message.chat.id, "Аркадьевна?", reply_to_message_id=message.message_id)

   elif message.text.endswith("волк"):
       bot.send_message(message.chat.id, random2.choice (volk), reply_to_message_id=message.message_id)
   elif message.text.endswith("Волк"):
       bot.send_message(message.chat.id, random2.choice (volk), reply_to_message_id=message.message_id)

   elif message.text.endswith("человек"):
       bot.send_message(message.chat.id, random2.choice (chelovek), reply_to_message_id=message.message_id)
   elif message.text.endswith("Человек"):
       bot.send_message(message.chat.id, random2.choice (chelovek), reply_to_message_id=message.message_id)

   elif message.text.endswith("сделать"):
       bot.send_message(message.chat.id, random2.choice (sdelat), reply_to_message_id=message.message_id)
   elif message.text.endswith("Сделать"):
       bot.send_message(message.chat.id, random2.choice (sdelat), reply_to_message_id=message.message_id)

   elif message.text == "сука":
       bot.send_message(message.chat.id, random2.choice (suka), reply_to_message_id=message.message_id)
   elif message.text.endswith("Сука"):
       bot.send_message(message.chat.id, random2.choice (suka), reply_to_message_id=message.message_id)
   elif message.text.endswith(" сука"):
       bot.send_message(message.chat.id, random2.choice (suka), reply_to_message_id=message.message_id)

   elif message.text == "пизда":
       bot.send_message(message.chat.id, random2.choice (pizda), reply_to_message_id=message.message_id)
   elif message.text.endswith("Пизда"):
       bot.send_message(message.chat.id, random2.choice (pizda), reply_to_message_id=message.message_id)
   elif message.text.endswith(" пизда"):
       bot.send_message(message.chat.id, random2.choice (pizda), reply_to_message_id=message.message_id)

   elif message.text.endswith("ахахахахахахахах"):
       bot.send_sticker(message.chat.id, random2.choice (ahah))
   elif message.text.endswith("АХАХАХ"):
       bot.send_sticker(message.chat.id, random2.choice (ahah))
   elif message.text.endswith("ахахахахахахаха"):
       bot.send_sticker(message.chat.id, random2.choice (ahah))
   elif message.text.endswith("АХАХА"):
       bot.send_sticker(message.chat.id, random2.choice (ahah))

   elif message.text.endswith("Алло"):
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text.endswith(" алло"):
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text == "алло":
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text.endswith("Алё"):
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text.endswith(" алё"):
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text == "алё":
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text.endswith("Але"):
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text.endswith(" але"):
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text == "але":
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text == "ало":
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)
   elif message.text.endswith("Ало"):
       bot.send_sticker(message.chat.id, random2.choice (allo), reply_to_message_id=message.message_id)

   elif message.text.endswith("любовь"):
       bot.send_message(message.chat.id, random2.choice (lubov), reply_to_message_id=message.message_id)
   elif message.text.endswith("Любовь"):
       bot.send_message(message.chat.id, random2.choice (lubov), reply_to_message_id=message.message_id)

   elif message.text.find("елорусси") != -1:
       bot.send_message(message.chat.id, 'Беларусь, а не Белоруссия!', reply_to_message_id=message.message_id) and bot.send_sticker(message.chat.id, random2.choice(gordonloh))

   elif message.text == "звонит":
       bot.send_message(message.chat.id, random2.choice (zvonit), reply_to_message_id=message.message_id)
   elif message.text.endswith(" звонит"):
       bot.send_message(message.chat.id, random2.choice (zvonit), reply_to_message_id=message.message_id)
   elif message.text.endswith("Звонит"):
       bot.send_message(message.chat.id, random2.choice (zvonit), reply_to_message_id=message.message_id)
   elif message.text.find(" звонит ") != -1:
       bot.send_message(message.chat.id, random2.choice (zvonit1), reply_to_message_id=message.message_id)

   elif message.text == "торты":
       bot.send_message(message.chat.id, random2.choice (torti), reply_to_message_id=message.message_id)
   elif message.text.endswith(" торты"):
       bot.send_message(message.chat.id, random2.choice (torti), reply_to_message_id=message.message_id)
   elif message.text.endswith("Торты"):
       bot.send_message(message.chat.id, random2.choice (torti), reply_to_message_id=message.message_id)
   elif message.text.find(" торты ") != -1:
       bot.send_message(message.chat.id, random2.choice (torti), reply_to_message_id=message.message_id)

   elif message.text == "молоко":
       bot.send_message(message.chat.id, "птичье?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" молоко"):
       bot.send_message(message.chat.id, "птичье?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Молоко"):
       bot.send_message(message.chat.id, "птичье?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" молоко ") != -1:
       bot.send_message(message.chat.id, "птичье молоко?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text == "молока":
       bot.send_message(message.chat.id, "птичьего?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" молока"):
       bot.send_message(message.chat.id, "птичьего?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Молока"):
       bot.send_message(message.chat.id, "птичьго?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" молока ") != -1:
       bot.send_message(message.chat.id, "птичьего?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text == "молоко?":
       bot.send_message(message.chat.id, "птичье?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" молоко?"):
       bot.send_message(message.chat.id, "птичье?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Молоко?"):
       bot.send_message(message.chat.id, "птичье?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" молоко, ") != -1:
       bot.send_message(message.chat.id, "птичье молоко?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text == "молока?":
       bot.send_message(message.chat.id, "птичьего?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" молока?"):
       bot.send_message(message.chat.id, "птичьего?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Молока?"):
       bot.send_message(message.chat.id, "птичьго?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" молока, ") != -1:
       bot.send_message(message.chat.id, "птичьего?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')

   elif message.text == "торт":
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" торт"):
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Торт"):
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" торт ") != -1:
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text == "торта":
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" торта"):
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Торта"):
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" торта ") != -1:
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text == "торт?":
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" торт?"):
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Торт?"):
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" торт, ") != -1:
       bot.send_message(message.chat.id, "Гордон в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text == "торта?":
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith(" торта?"):
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.endswith("Торта?"):
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')
   elif message.text.find(" торта, ") != -1:
       bot.send_message(message.chat.id, "Гордона в шоколаде?" , reply_to_message_id=message.message_id) and bot.send_photo(message.chat.id, 'https://cdn.segodnya.ua/i/image_1200x630/media/image/607/2f6/43a/6072f643a5a01.jpg')

   elif message.text == "космоса":
       bot.send_message(message.chat.id, random2.choice (kosmos), reply_to_message_id=message.message_id)
   elif message.text.endswith(" космоса"):
       bot.send_message(message.chat.id, random2.choice (kosmos), reply_to_message_id=message.message_id)
   elif message.text.endswith("Космоса"):
       bot.send_message(message.chat.id, random2.choice (kosmos), reply_to_message_id=message.message_id)
   elif message.text.find(" космоса ") != -1:
       bot.send_message(message.chat.id, "Космоса из Бригады?", reply_to_message_id=message.message_id)
   elif message.text == "космосом":
       bot.send_message(message.chat.id, random2.choice (kosmos), reply_to_message_id=message.message_id)
   elif message.text.endswith(" космосом"):
       bot.send_message(message.chat.id, random2.choice (kosmos), reply_to_message_id=message.message_id)
   elif message.text.endswith("Космосом"):
       bot.send_message(message.chat.id, random2.choice (kosmos), reply_to_message_id=message.message_id)
   elif message.text.find(" космосом ") != -1:
       bot.send_message(message.chat.id, "Космосом из Бригады?", reply_to_message_id=message.message_id)

   elif message.text == "что":
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)
   elif message.text.endswith(" что"):
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)
   elif message.text == "что?":
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)
   elif message.text.endswith(" что?"):
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)
   elif message.text == "Что":
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)
   elif message.text.endswith(" Что"):
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)
   elif message.text == "Что?":
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)
   elif message.text.endswith(" Что?"):
       bot.send_message(message.chat.id, random2.choice (chto), reply_to_message_id=message.message_id)

   elif message.text == "не":
       bot.send_message(message.chat.id, random2.choice (ne), reply_to_message_id=message.message_id)
   elif message.text.endswith(" не"):
       bot.send_message(message.chat.id, random2.choice (ne), reply_to_message_id=message.message_id)
   elif message.text.endswith("Не"):
       bot.send_message(message.chat.id, random2.choice (ne1), reply_to_message_id=message.message_id) and bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECZgtgvrUtvb46RDLwO6IwbMkyrb46jwACHwADdJypFi-pOnvSySiPHwQ")
   elif message.text == "не?":
       bot.send_message(message.chat.id, random2.choice (ne), reply_to_message_id=message.message_id)
   elif message.text.endswith(" не?"):
       bot.send_message(message.chat.id, random2.choice (ne), reply_to_message_id=message.message_id)
   elif message.text.endswith("Не?"):
       bot.send_message(message.chat.id, random2.choice (ne1), reply_to_message_id=message.message_id) and bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECZgtgvrUtvb46RDLwO6IwbMkyrb46jwACHwADdJypFi-pOnvSySiPHwQ")

   elif message.text.find("лапидарный") != -1:
       bot.send_message(message.chat.id, "лаПИДАРный?)))" , reply_to_message_id=message.message_id)
   elif message.text.find("Лапидарный") != -1:
       bot.send_message(message.chat.id, "лаПИДАРный?)))" , reply_to_message_id=message.message_id)

   elif message.text == "буду":
       bot.send_message(message.chat.id, random2.choice (budu), reply_to_message_id=message.message_id)
   elif message.text.endswith(" буду"):
       bot.send_message(message.chat.id, random2.choice (budu), reply_to_message_id=message.message_id)
   elif message.text.endswith("Буду"):
       bot.send_message(message.chat.id, random2.choice (budu), reply_to_message_id=message.message_id)

   elif message.text == "один":
       bot.send_message(message.chat.id, random2.choice (odin), reply_to_message_id=message.message_id)
   elif message.text.endswith(" один"):
       bot.send_message(message.chat.id, random2.choice (odin), reply_to_message_id=message.message_id)
   elif message.text.endswith("Один"):
       bot.send_message(message.chat.id, random2.choice (odin), reply_to_message_id=message.message_id)

   elif message.text == "два":
       bot.send_message(message.chat.id, random2.choice (dva), reply_to_message_id=message.message_id)
   elif message.text.endswith(" два"):
       bot.send_message(message.chat.id, random2.choice (dva), reply_to_message_id=message.message_id)
   elif message.text.endswith("Два"):
       bot.send_message(message.chat.id, random2.choice (dva), reply_to_message_id=message.message_id)

   elif message.text == "купишь":
       bot.send_message(message.chat.id, random2.choice (kupish), reply_to_message_id=message.message_id)
   elif message.text.endswith(" купишь"):
       bot.send_message(message.chat.id, random2.choice (kupish), reply_to_message_id=message.message_id)
   elif message.text.endswith("Купишь"):
       bot.send_message(message.chat.id, random2.choice (kupish), reply_to_message_id=message.message_id)
   elif message.text == "купишь?":
       bot.send_message(message.chat.id, random2.choice (kupish), reply_to_message_id=message.message_id)
   elif message.text.endswith(" купишь?"):
       bot.send_message(message.chat.id, random2.choice (kupish), reply_to_message_id=message.message_id)
   elif message.text.endswith("Купишь?"):
       bot.send_message(message.chat.id, random2.choice (kupish), reply_to_message_id=message.message_id)

   elif message.text == "три":
       bot.send_message(message.chat.id, random2.choice (tri), reply_to_message_id=message.message_id)
   elif message.text.endswith(" три"):
       bot.send_message(message.chat.id, random2.choice (tri), reply_to_message_id=message.message_id)
   elif message.text.endswith("Три"):
       bot.send_message(message.chat.id, random2.choice (tri), reply_to_message_id=message.message_id)

   elif message.text == "четыре":
       bot.send_message(message.chat.id, random2.choice (chetire), reply_to_message_id=message.message_id)
   elif message.text.endswith(" четыре"):
       bot.send_message(message.chat.id, random2.choice (chetire), reply_to_message_id=message.message_id)
   elif message.text.endswith("Четыре"):
       bot.send_message(message.chat.id, random2.choice (chetire), reply_to_message_id=message.message_id)

   elif message.text == "пять":
       bot.send_message(message.chat.id, random2.choice (pyat), reply_to_message_id=message.message_id)
   elif message.text.endswith(" пять"):
       bot.send_message(message.chat.id, random2.choice (pyat), reply_to_message_id=message.message_id)
   elif message.text.endswith("Пять"):
       bot.send_message(message.chat.id, random2.choice (pyat), reply_to_message_id=message.message_id)

   elif message.text == "гуф":
       bot.send_message(message.chat.id, random2.choice (guf), reply_to_message_id=message.message_id)
   elif message.text.endswith(" гуф"):
       bot.send_message(message.chat.id, random2.choice (guf), reply_to_message_id=message.message_id)
   elif message.text.endswith("Гуф"):
       bot.send_message(message.chat.id, random2.choice (guf), reply_to_message_id=message.message_id)

   elif message.text == "семь":
       bot.send_message(message.chat.id, random2.choice (sem), reply_to_message_id=message.message_id)
   elif message.text.endswith(" семь"):
       bot.send_message(message.chat.id, random2.choice (sem), reply_to_message_id=message.message_id)
   elif message.text.endswith("Семь"):
       bot.send_message(message.chat.id, random2.choice (sem), reply_to_message_id=message.message_id)

   elif message.text == "восемь":
       bot.send_message(message.chat.id, random2.choice (vosem), reply_to_message_id=message.message_id)
   elif message.text.endswith(" восемь"):
       bot.send_message(message.chat.id, random2.choice (vosem), reply_to_message_id=message.message_id)
   elif message.text.endswith("Восемь"):
       bot.send_message(message.chat.id, random2.choice (vosem), reply_to_message_id=message.message_id)

   elif message.text == "кент":
       bot.send_message(message.chat.id, random2.choice (kent), reply_to_message_id=message.message_id)
   elif message.text.endswith(" кент"):
       bot.send_message(message.chat.id, random2.choice (kent), reply_to_message_id=message.message_id)
   elif message.text.endswith("Кент"):
       bot.send_message(message.chat.id, random2.choice (kent), reply_to_message_id=message.message_id)

   elif message.text.find("охла спросить забыли") != -1:
       bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)

   elif message.text.find("охла забыть спросили") != -1:
       bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)

   elif message.text.find("охла забыли спросить") != -1:
       bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)

   elif message.text.find("охла спросили забыть") != -1:
       bot.send_sticker(message.chat.id, random2.choice(gordonloh), reply_to_message_id=message.message_id)

   elif message.text == "гордон":
       bot.send_message(message.chat.id, random2.choice (gordon), reply_to_message_id=message.message_id)
   elif message.text.endswith(" гордон"):
       bot.send_message(message.chat.id, random2.choice (gordon), reply_to_message_id=message.message_id)

   elif message.text.endswith("идорас"):
       bot.send_message(message.chat.id, random2.choice (pidoras), reply_to_message_id=message.message_id)

   elif message.text.endswith("алава"):
       bot.send_message(message.chat.id, random2.choice (shalava), reply_to_message_id=message.message_id)

   elif message.text.endswith("ди нахуй"):
       bot.send_message(message.chat.id, random2.choice (idinahui), reply_to_message_id=message.message_id)
   elif message.text.endswith("ди нахер"):
       bot.send_message(message.chat.id, random2.choice (idinahui), reply_to_message_id=message.message_id)

   elif message.text.endswith(" рубля"):
       bot.send_message(message.chat.id, random2.choice (rublya), reply_to_message_id=message.message_id)
   elif message.text.endswith("Рубля"):
       bot.send_message(message.chat.id, random2.choice (rublya), reply_to_message_id=message.message_id)

   elif message.text.endswith(" рублей"):
       bot.send_message(message.chat.id, random2.choice (rubley), reply_to_message_id=message.message_id)
   elif message.text.endswith("Рублей"):
       bot.send_message(message.chat.id, random2.choice (rubley), reply_to_message_id=message.message_id)

   elif message.text.endswith("обильный"):
       bot.send_message(message.chat.id, "дебильный?", reply_to_message_id=message.message_id)

   elif message.text == "согласен":
       bot.send_message(message.chat.id, random2.choice (soglasen), reply_to_message_id=message.message_id)
   elif message.text == "Согласен":
       bot.send_message(message.chat.id, random2.choice (soglasen), reply_to_message_id=message.message_id)
   elif message.text == "согласна":
       bot.send_message(message.chat.id, random2.choice (soglasen), reply_to_message_id=message.message_id)
   elif message.text == "Согласна":
       bot.send_message(message.chat.id, random2.choice (soglasen), reply_to_message_id=message.message_id)

   elif message.text == "короче":
       bot.send_message(message.chat.id, random2.choice (koroche), reply_to_message_id=message.message_id)
   elif message.text.endswith(" короче"):
       bot.send_message(message.chat.id, random2.choice (koroche), reply_to_message_id=message.message_id)
   elif message.text.endswith("Короче"):
       bot.send_message(message.chat.id, random2.choice (koroche), reply_to_message_id=message.message_id)

   elif message.text == "рак":
       bot.send_message(message.chat.id, random2.choice (rak), reply_to_message_id=message.message_id)
   elif message.text.endswith(" рак"):
       bot.send_message(message.chat.id, random2.choice (rak), reply_to_message_id=message.message_id)
   elif message.text.endswith("Рак"):
       bot.send_message(message.chat.id, random2.choice (rak), reply_to_message_id=message.message_id)

   elif message.text == "брат":
       bot.send_message(message.chat.id, random2.choice (brat), reply_to_message_id=message.message_id)
   elif message.text.endswith(" брат"):
       bot.send_message(message.chat.id, random2.choice (brat), reply_to_message_id=message.message_id)
   elif message.text.endswith("Брат"):
       bot.send_message(message.chat.id, random2.choice (brat), reply_to_message_id=message.message_id)

   elif message.text == "ебануться":
       bot.send_message(message.chat.id, "Туфли гнутся?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" ебануться"):
       bot.send_message(message.chat.id, "Туфли гнутся?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Ебануться"):
       bot.send_message(message.chat.id, "Туфли гнутся?", reply_to_message_id=message.message_id)

   elif message.text == "слово":
       bot.send_message(message.chat.id, random2.choice (slovo), reply_to_message_id=message.message_id)
   elif message.text.endswith(" слово"):
       bot.send_message(message.chat.id, random2.choice (slovo), reply_to_message_id=message.message_id)
   elif message.text.endswith("Слово"):
       bot.send_message(message.chat.id, random2.choice (slovo), reply_to_message_id=message.message_id)

   elif message.text == "смешно":
       bot.send_message(message.chat.id, random2.choice (smeshno), reply_to_message_id=message.message_id)
   elif message.text.endswith("Смешно"):
       bot.send_message(message.chat.id, random2.choice (smeshno), reply_to_message_id=message.message_id)

   elif message.text == "посмотреть":
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text.endswith(" посмотреть"):
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text.endswith("Посмотреть"):
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text == "посмотрим":
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text.endswith(" посмотрим"):
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text.endswith("Посмотрим"):
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text == "посмотрю":
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text.endswith(" посмотрю"):
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)
   elif message.text.endswith("Посмотрю"):
       bot.send_message(message.chat.id, random2.choice (posmotret), reply_to_message_id=message.message_id)

   elif message.text == "хайп":
       bot.send_message(message.chat.id, random2.choice (haip), reply_to_message_id=message.message_id)
   elif message.text.endswith(" хайп"):
       bot.send_message(message.chat.id, random2.choice (haip), reply_to_message_id=message.message_id)
   elif message.text.endswith("Хайп"):
       bot.send_message(message.chat.id, random2.choice (haip), reply_to_message_id=message.message_id)

   elif message.text == "считаю":
       bot.send_message(message.chat.id, random2.choice (schitayu), reply_to_message_id=message.message_id)
   elif message.text.endswith(" считаю"):
       bot.send_message(message.chat.id, random2.choice (schitayu), reply_to_message_id=message.message_id)
   elif message.text.endswith("Считаю"):
       bot.send_message(message.chat.id, random2.choice (schitayu), reply_to_message_id=message.message_id)

   elif message.text == "бил":
       bot.send_message(message.chat.id, random2.choice (bil), reply_to_message_id=message.message_id)
   elif message.text.endswith(" бил"):
       bot.send_message(message.chat.id, random2.choice (bil), reply_to_message_id=message.message_id)
   elif message.text.endswith("Бил"):
       bot.send_message(message.chat.id, random2.choice (bil), reply_to_message_id=message.message_id)

   elif message.text == "хер":
       bot.send_message(message.chat.id, random2.choice (her), reply_to_message_id=message.message_id)
   elif message.text.endswith(" хер"):
       bot.send_message(message.chat.id, random2.choice (her), reply_to_message_id=message.message_id)
   elif message.text.endswith("Хер"):
       bot.send_message(message.chat.id, random2.choice (her), reply_to_message_id=message.message_id)

   elif message.text == "число":
       bot.send_message(message.chat.id, random2.choice (chislo), reply_to_message_id=message.message_id)
   elif message.text.endswith(" число"):
       bot.send_message(message.chat.id, random2.choice (chislo), reply_to_message_id=message.message_id)
   elif message.text.endswith("Число"):
       bot.send_message(message.chat.id, random2.choice (chislo), reply_to_message_id=message.message_id)

   elif message.text == "Ленин":
       bot.send_message(message.chat.id, random2.choice (lenin), reply_to_message_id=message.message_id)
   elif message.text.endswith("Ленин"):
       bot.send_message(message.chat.id, random2.choice (lenin), reply_to_message_id=message.message_id)

   elif message.text == "хуй":
       bot.send_message(message.chat.id, random2.choice (hui), reply_to_message_id=message.message_id)
   elif message.text.endswith(" хуй"):
       bot.send_message(message.chat.id, random2.choice (hui), reply_to_message_id=message.message_id)
   elif message.text.endswith("Хуй"):
       bot.send_message(message.chat.id, random2.choice (hui), reply_to_message_id=message.message_id)

   elif message.text.find("мысл жизни") != -1:
       bot.send_message(message.chat.id, "42", reply_to_message_id=message.message_id)

   elif message.text == "третий":
       bot.send_message(message.chat.id, random2.choice (treti), reply_to_message_id=message.message_id)
   elif message.text.endswith(" третий"):
       bot.send_message(message.chat.id, random2.choice (treti), reply_to_message_id=message.message_id)
   elif message.text.endswith("Третий"):
       bot.send_message(message.chat.id, random2.choice (treti), reply_to_message_id=message.message_id)

   elif message.text == "пятый":
       bot.send_message(message.chat.id, random2.choice (pyati), reply_to_message_id=message.message_id)
   elif message.text.endswith(" пятый"):
       bot.send_message(message.chat.id, random2.choice (pyati), reply_to_message_id=message.message_id)
   elif message.text.endswith("Пятый"):
       bot.send_message(message.chat.id, random2.choice (pyati), reply_to_message_id=message.message_id)

   elif message.text == "люди":
       bot.send_message(message.chat.id, random2.choice (ludi), reply_to_message_id=message.message_id)
   elif message.text.endswith(" люди"):
       bot.send_message(message.chat.id, random2.choice (ludi), reply_to_message_id=message.message_id)
   elif message.text.endswith("Люди"):
       bot.send_message(message.chat.id, random2.choice (ludi), reply_to_message_id=message.message_id)

   elif message.text == "обиделся":
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith(" обиделся"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith("Обиделся"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text == "обиделась":
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith(" обиделась"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith("Обиделась"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text == "обиделся?":
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith(" обиделся?"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith("Обиделся?"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text == "обиделась?":
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith(" обиделась?"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)
   elif message.text.endswith("Обиделась?"):
       bot.send_message(message.chat.id, random2.choice (obidelsya), reply_to_message_id=message.message_id)

   elif message.text == "помощь":
       bot.send_message(message.chat.id, random2.choice (pomosh), reply_to_message_id=message.message_id)
   elif message.text.endswith(" помощь"):
       bot.send_message(message.chat.id, random2.choice (pomosh), reply_to_message_id=message.message_id)
   elif message.text.endswith("Помощь"):
       bot.send_message(message.chat.id, random2.choice (pomosh), reply_to_message_id=message.message_id)

   elif message.text == "цирк":
       bot.send_message(message.chat.id, random2.choice (cirk), reply_to_message_id=message.message_id)
   elif message.text.endswith(" цирк"):
       bot.send_message(message.chat.id, random2.choice (cirk), reply_to_message_id=message.message_id)
   elif message.text.endswith("Цирк"):
       bot.send_message(message.chat.id, random2.choice (cirk), reply_to_message_id=message.message_id)

   elif message.text == "раз":
       bot.send_message(message.chat.id, random2.choice (raz), reply_to_message_id=message.message_id)
   elif message.text.endswith(" раз"):
       bot.send_message(message.chat.id, random2.choice (raz), reply_to_message_id=message.message_id)
   elif message.text.endswith("Раз"):
       bot.send_message(message.chat.id, random2.choice (raz), reply_to_message_id=message.message_id)

   elif message.text == "ровесники":
       bot.send_message(message.chat.id, random2.choice (rovesniki), reply_to_message_id=message.message_id)
   elif message.text.endswith(" ровесники"):
       bot.send_message(message.chat.id, random2.choice (rovesniki), reply_to_message_id=message.message_id)
   elif message.text.endswith("Ровесники"):
       bot.send_message(message.chat.id, random2.choice (rovesniki), reply_to_message_id=message.message_id)
   elif message.text == "ровесницы":
       bot.send_message(message.chat.id, random2.choice (rovesniсi), reply_to_message_id=message.message_id)
   elif message.text.endswith(" ровесницы"):
       bot.send_message(message.chat.id, random2.choice (rovesniсi), reply_to_message_id=message.message_id)
   elif message.text.endswith("Ровесницы"):
       bot.send_message(message.chat.id, random2.choice (rovesniсi), reply_to_message_id=message.message_id)

   elif message.text == "петь":
       bot.send_message(message.chat.id, random2.choice (pet), reply_to_message_id=message.message_id)
   elif message.text.endswith(" петь"):
       bot.send_message(message.chat.id, random2.choice (pet), reply_to_message_id=message.message_id)
   elif message.text.endswith("Петь"):
       bot.send_message(message.chat.id, random2.choice (pet), reply_to_message_id=message.message_id)
   elif message.text == "петь?":
       bot.send_message(message.chat.id, random2.choice (pet), reply_to_message_id=message.message_id)
   elif message.text.endswith(" петь?"):
       bot.send_message(message.chat.id, random2.choice (pet), reply_to_message_id=message.message_id)
   elif message.text.endswith("Петь?"):
       bot.send_message(message.chat.id, random2.choice (pet), reply_to_message_id=message.message_id)

   elif message.text == "плотина":
       bot.send_message(message.chat.id, "логи?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" плотина"):
       bot.send_message(message.chat.id, "логи?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Плотина"):
       bot.send_message(message.chat.id, "логи?", reply_to_message_id=message.message_id)

   elif message.text == "надежда":
       bot.send_message(message.chat.id, random2.choice (nadejda), reply_to_message_id=message.message_id)
   elif message.text.endswith(" надежда"):
       bot.send_message(message.chat.id, random2.choice (nadejda), reply_to_message_id=message.message_id)
   elif message.text.endswith("Надежда"):
       bot.send_message(message.chat.id, random2.choice (nadejda), reply_to_message_id=message.message_id)

   elif message.text == "надежда":
       bot.send_message(message.chat.id, random2.choice (nadejda), reply_to_message_id=message.message_id)
   elif message.text.endswith(" надежда"):
       bot.send_message(message.chat.id, random2.choice (nadejda), reply_to_message_id=message.message_id)
   elif message.text.endswith("Надежда"):
       bot.send_message(message.chat.id, random2.choice (nadejda), reply_to_message_id=message.message_id)

   elif message.text == "вера":
       bot.send_message(message.chat.id, random2.choice (vera), reply_to_message_id=message.message_id)
   elif message.text.endswith(" вера"):
       bot.send_message(message.chat.id, random2.choice (vera), reply_to_message_id=message.message_id)
   elif message.text.endswith("Вера"):
       bot.send_message(message.chat.id, random2.choice (vera), reply_to_message_id=message.message_id)

   elif message.text == "волю":
       bot.send_message(message.chat.id, random2.choice (volya), reply_to_message_id=message.message_id)
   elif message.text.endswith("волю"):
       bot.send_message(message.chat.id, random2.choice (volya), reply_to_message_id=message.message_id)
   elif message.text.endswith("Волю"):
       bot.send_message(message.chat.id, random2.choice (volya), reply_to_message_id=message.message_id)

   elif message.text == "слава":
       bot.send_message(message.chat.id, random2.choice (slava), reply_to_message_id=message.message_id)
   elif message.text.endswith(" слава"):
       bot.send_message(message.chat.id, random2.choice (slava), reply_to_message_id=message.message_id)
   elif message.text.endswith("Слава"):
       bot.send_message(message.chat.id, random2.choice (slava), reply_to_message_id=message.message_id)

   elif message.text == "Колю":
       bot.send_message(message.chat.id, random2.choice (kolu), reply_to_message_id=message.message_id)
   elif message.text.endswith(" Колю"):
       bot.send_message(message.chat.id, random2.choice (kolu), reply_to_message_id=message.message_id)
   elif message.text.endswith("Колю?"):
       bot.send_message(message.chat.id, random2.choice (kolu), reply_to_message_id=message.message_id)

   elif message.text == "лада":
       bot.send_message(message.chat.id, "Дэнс?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" лада"):
       bot.send_message(message.chat.id, "Дэнс?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Лада"):
       bot.send_message(message.chat.id, "Дэнс?", reply_to_message_id=message.message_id)

   elif message.text == "майами":
       bot.send_message(message.chat.id, "Олег?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" майами"):
       bot.send_message(message.chat.id, "Олег?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Майами"):
       bot.send_message(message.chat.id, "Олег?", reply_to_message_id=message.message_id)

   elif message.text == "охота":
       bot.send_message(message.chat.id, random2.choice (ohota), reply_to_message_id=message.message_id)
   elif message.text.endswith("охота"):
       bot.send_message(message.chat.id, random2.choice (ohota), reply_to_message_id=message.message_id)
   elif message.text.endswith("Охота"):
       bot.send_message(message.chat.id, random2.choice (ohota), reply_to_message_id=message.message_id)

   elif message.text == "белое":
       bot.send_message(message.chat.id, random2.choice (beloe), reply_to_message_id=message.message_id)
   elif message.text.endswith("белое"):
       bot.send_message(message.chat.id, random2.choice (beloe), reply_to_message_id=message.message_id)
   elif message.text.endswith("Белое"):
       bot.send_message(message.chat.id, random2.choice (beloe), reply_to_message_id=message.message_id)

   elif message.text == "диско":
       bot.send_message(message.chat.id, random2.choice (disco), reply_to_message_id=message.message_id)
   elif message.text.endswith("диско"):
       bot.send_message(message.chat.id, random2.choice (disco), reply_to_message_id=message.message_id)
   elif message.text.endswith("Диско"):
       bot.send_message(message.chat.id, random2.choice (disco), reply_to_message_id=message.message_id)

   elif message.text == "сыт":
       bot.send_message(message.chat.id, "Ссыт!", reply_to_message_id=message.message_id)
   elif message.text.endswith(" сыт"):
       bot.send_message(message.chat.id, "Ссыт!", reply_to_message_id=message.message_id)
   elif message.text.endswith("Сыт"):
       bot.send_message(message.chat.id, "Ссыт!", reply_to_message_id=message.message_id)

   elif message.text == "рис":
       bot.send_message(message.chat.id, "Уизерспун?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" рис"):
       bot.send_message(message.chat.id, "Уизерспун?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Рис"):
       bot.send_message(message.chat.id, "Уизерспун?", reply_to_message_id=message.message_id)

   elif message.text.endswith("рома"):
       bot.send_message(message.chat.id, "Зверь?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Рома"):
       bot.send_message(message.chat.id, "Зверь?", reply_to_message_id=message.message_id)

   elif message.text.endswith(" ром"):
       bot.send_message(message.chat.id, "а Зверь?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" ром"):
       bot.send_message(message.chat.id, "а Зверь?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Ром"):
       bot.send_message(message.chat.id, "а Зверь?", reply_to_message_id=message.message_id)

   elif message.text == "с нг":
       bot.send_message(message.chat.id, "Судружество Независимых Государств?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" с нг"):
       bot.send_message(message.chat.id, "Содружество Независимых Государств?", reply_to_message_id=message.message_id)
   elif message.text.endswith("С нг"):
       bot.send_message(message.chat.id, "Содружество Независимых Государств?", reply_to_message_id=message.message_id)

   elif message.text.endswith("плэй"):
       bot.send_message(message.chat.id, "бой?", reply_to_message_id=message.message_id)
   elif message.text.endswith("play"):
       bot.send_message(message.chat.id, "boy?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Плэй"):
       bot.send_message(message.chat.id, "бой?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Play"):
       bot.send_message(message.chat.id, "boy?", reply_to_message_id=message.message_id)

   elif message.text.endswith("Гааге"):
       bot.send_message(message.chat.id, "Леди?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Гаагу"):
       bot.send_message(message.chat.id, "Леди?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Гаага"):
       bot.send_message(message.chat.id, "Леди?", reply_to_message_id=message.message_id)

   elif message.text == "круг":
       bot.send_message(message.chat.id, "Михаил?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" круг"):
       bot.send_message(message.chat.id, "Михаил?", reply_to_message_id=message.message_id)

   elif message.text.endswith("алла"):
       bot.send_message(message.chat.id, "Пугачёва?", reply_to_message_id=message.message_id)

   elif message.text == "лысый":
       bot.send_message(message.chat.id, random2.choice (liliy), reply_to_message_id=message.message_id)
   elif message.text.endswith("дысый"):
       bot.send_message(message.chat.id, random2.choice (lisiy), reply_to_message_id=message.message_id)
   elif message.text.endswith("Лысый"):
       bot.send_message(message.chat.id, random2.choice (lisiy), reply_to_message_id=message.message_id)

   elif message.text.endswith("питер"):
       bot.send_message(message.chat.id, random2.choice (piter), reply_to_message_id=message.message_id)
   elif message.text.endswith("Питер"):
       bot.send_message(message.chat.id, random2.choice (piter), reply_to_message_id=message.message_id)

   elif message.text.endswith ("ЮКОС"):
       bot.send_message(message.chat.id, random2.choice (ukos), reply_to_message_id=message.message_id)
   elif message.text.endswith ("юкос"):
       bot.send_message(message.chat.id, random2.choice (ukos), reply_to_message_id=message.message_id)

   elif message.text == "виски":
       bot.send_message(message.chat.id, random2.choice (viski), reply_to_message_id=message.message_id)
   elif message.text.endswith("виски"):
       bot.send_message(message.chat.id, random2.choice (viski), reply_to_message_id=message.message_id)
   elif message.text.endswith("Виски"):
       bot.send_message(message.chat.id, random2.choice (viski), reply_to_message_id=message.message_id)

   elif message.text == "споки":
       bot.send_photo(message.chat.id, random2.choice (spoki), reply_to_message_id=message.message_id)
   elif message.text.endswith(" споки"):
       bot.send_photo(message.chat.id, random2.choice (spoki), reply_to_message_id=message.message_id)
   elif message.text.endswith("Споки"):
       bot.send_photo(message.chat.id, random2.choice (spoki), reply_to_message_id=message.message_id)
   elif message.text.find(" споки ") != -1:
       bot.send_photo(message.chat.id, random2.choice (spoki), reply_to_message_id=message.message_id)

   elif message.text == "кто?":
       bot.send_message(message.chat.id, random2.choice (kto), reply_to_message_id=message.message_id)
   elif message.text.endswith(" кто?"):
       bot.send_message(message.chat.id, random2.choice (kto), reply_to_message_id=message.message_id)
   elif message.text.endswith("Кто?"):
       bot.send_message(message.chat.id, random2.choice (kto), reply_to_message_id=message.message_id)
   elif message.text == "кто":
       bot.send_message(message.chat.id, random2.choice (kto), reply_to_message_id=message.message_id)
   elif message.text.endswith(" кто"):
       bot.send_message(message.chat.id, random2.choice (kto), reply_to_message_id=message.message_id)
   elif message.text.endswith("Кто"):
       bot.send_message(message.chat.id, random2.choice (kto), reply_to_message_id=message.message_id)

   elif message.text.endswith("в гости?"):
       bot.send_message(message.chat.id, random2.choice (gosti), reply_to_message_id=message.message_id)
   elif message.text.endswith("В гости?"):
       bot.send_message(message.chat.id, random2.choice (gosti), reply_to_message_id=message.message_id)
   elif message.text.endswith("в гости"):
       bot.send_message(message.chat.id, random2.choice (gosti), reply_to_message_id=message.message_id)
   elif message.text.endswith("В гости"):
       bot.send_message(message.chat.id, random2.choice (gosti), reply_to_message_id=message.message_id)

   elif message.text.endswith("адай вопрос"):
       bot.send_message(message.chat.id, random2.choice (vopros), reply_to_message_id=message.message_id)

   elif message.text.endswith("кант"):
       bot.send_message(message.chat.id, random2.choice (kant), reply_to_message_id=message.message_id)
   elif message.text.endswith("Кант"):
       bot.send_message(message.chat.id, random2.choice (kant), reply_to_message_id=message.message_id)

   elif message.text.find("предсказуем") != -1:
       bot.send_message(message.chat.id, random2.choice (predskazuem), reply_to_message_id=message.message_id)
   elif message.text.find("Предсказуем") != -1:
       bot.send_message(message.chat.id, random2.choice (predskazuem), reply_to_message_id=message.message_id)

   elif message.text == "шесть":
       bot.send_message(message.chat.id, "ое чувство?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" шесть"):
       bot.send_message(message.chat.id, "ое чувство?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Шесть"):
       bot.send_message(message.chat.id, "ое чувство?", reply_to_message_id=message.message_id)

   elif message.text.endswith("ерсея"):
       bot.send_message(message.chat.id, "нукович?", reply_to_message_id=message.message_id)

   elif message.text == "серсо":
       bot.send_message(message.chat.id, random2.choice (serso), reply_to_message_id=message.message_id)
   elif message.text.endswith(" серсо"):
       bot.send_message(message.chat.id, random2.choice (serso), reply_to_message_id=message.message_id)
   elif message.text.endswith("Серсо"):
       bot.send_message(message.chat.id, random2.choice (serso), reply_to_message_id=message.message_id)

   elif message.text == "супер":
       bot.send_message(message.chat.id, random2.choice (supir), reply_to_message_id=message.message_id)
   elif message.text.endswith(" супер"):
       bot.send_message(message.chat.id, random2.choice (supir), reply_to_message_id=message.message_id)
   elif message.text.endswith("супер"):
       bot.send_message(message.chat.id, random2.choice (supir), reply_to_message_id=message.message_id)

   elif message.text == "крюк":
       bot.send_message(message.chat.id, random2.choice (kruk), reply_to_message_id=message.message_id)
   elif message.text.endswith(" крюк"):
       bot.send_message(message.chat.id, random2.choice (kruk), reply_to_message_id=message.message_id)
   elif message.text.endswith("Крюк"):
       bot.send_message(message.chat.id, random2.choice (kruk), reply_to_message_id=message.message_id)

   elif message.text.endswith("рейтенбихера?"):
       bot.send_message(message.chat.id, random2.choice (breiten), reply_to_message_id=message.message_id)
   elif message.text.endswith("рейтенбихер?"):
       bot.send_message(message.chat.id, random2.choice (breiten), reply_to_message_id=message.message_id)
   elif message.text.endswith("рейтенбихера"):
       bot.send_message(message.chat.id, random2.choice (breiten), reply_to_message_id=message.message_id)
   elif message.text.endswith("рейтенбихер"):
       bot.send_message(message.chat.id, random2.choice (breiten), reply_to_message_id=message.message_id)
   elif message.text.endswith("интересов телезрителей"):
       bot.send_message(message.chat.id, random2.choice (breiten), reply_to_message_id=message.message_id)
   elif message.text.endswith("интересов телезрителей?"):
       bot.send_message(message.chat.id, random2.choice (breiten), reply_to_message_id=message.message_id)

   elif message.text.endswith("в чёрном ящике"):
       bot.send_message(message.chat.id, random2.choice (yashik), reply_to_message_id=message.message_id)
   elif message.text.endswith("в чёрном ящике?"):
       bot.send_message(message.chat.id, random2.choice (yashik), reply_to_message_id=message.message_id)

   elif message.text == "сирень":
       bot.send_message(message.chat.id, "и крыжовник?", reply_to_message_id=message.message_id)
   elif message.text.endswith(" сирень"):
       bot.send_message(message.chat.id, "и крыжовник?", reply_to_message_id=message.message_id)
   elif message.text.endswith("Сирень"):
       bot.send_message(message.chat.id, "и крыжовник?", reply_to_message_id=message.message_id)

   elif message.text == "белый":
       bot.send_message(message.chat.id, random2.choice (beliy), reply_to_message_id=message.message_id)
   elif message.text.endswith(" белый"):
       bot.send_message(message.chat.id, random2.choice (beliy), reply_to_message_id=message.message_id)
   elif message.text.endswith("Белый"):
       bot.send_message(message.chat.id, random2.choice (beliy), reply_to_message_id=message.message_id)



bot.polling(none_stop=True, interval=0)

try:
    bot.poling(none_stop=True)
except:
    pass
