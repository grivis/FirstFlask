'''
Проверка корректности выгрузки анкет в формат JSON. Берем полученный JSON, преобразуем обратно в объект Python
и производим раазличные манипуляции.
Обращаем внимание, что все нестандартные символы - т.е. все, кроме стандартной латиницы,
представлены в JSON-выводе в виде кодов.
Преобразованию подверглись русские буквы, буквы с диакритикой во французском и польском языках.
В процессе обратного преобразования они были корректно восприняты.
'''
import json
json_string = '''
{"form1118931": {"Iron": "\u05d1\u05bc\u05b7\u05e8\u05d6\u05b6\u05dc", "Coffee": "\u05de\u05db\u05d5\u05e0\u05ea \u05e7\u05e4\u05d4", "Smartphone": "\u05d8\u05dc\u05e4\u05d5\u05df \u05e0\u05d9\u05d9\u05d3", "Name": "Golda", "Lastname": "Meir", "Kettle": "\u05e7\u05d5\u05bc\u05de\u05e7\u05d5\u05bc\u05dd", "Residence": "city", "Language": "Hebrew", "Television": "\u05d8\u05dc\u05d5\u05d9\u05d6\u05d9\u05d4", "Sex": "female", "Age": "122"},
"form11161735": {"Language": "\u0444\u0435\u043d\u044f", "Coffee": "\u0432\u0430\u0440\u0438\u043b\u043e", "Name": "\u041c\u0430\u043d\u044c\u043a\u0430", "Lastname": "\u041e\u0431\u043b\u0438\u0433\u0430\u0446\u0438\u044f", "Kettle": "\u0447\u0438\u0444\u0438\u0440\u043d\u0438\u043a", "Residence": "city", "Television": "\u043a\u0438\u043d\u043e\u0448\u043a\u0430", "Sex": "female", "Age": "35"},
"form11161618": {"Language": "\u0431\u0435\u043b\u043e\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043a\u0430\u0444\u044f\u0440\u043d\u044f", "Name": "\u0412\u0430\u0441\u044f", "Lastname": "\u041f\u0443\u043f\u043a\u0438\u043d", "Kettle": "\u0447\u044f\u0439\u043d\u0438\u043a", "Residence": "city", "Television": "\u0442\u044f\u043b\u044f\u0432\u0438\u0437\u0430\u0440", "Sex": "male", "Age": "44"},
"form11171010": {"Iron": "fer \u00e0 repasser", "Language": "Francaise", "Smartphone": "t\u00e9l\u00e9phone portable", "Name": "Napoleon", "Lastname": "Bonaparte", "Kettle": "bouilloire", "Residence": "city", "Coffee": "machine \u00e0 caf\u00e9", "Television": "poste de t\u00e9l\u00e9vision", "Sex": "male", "Age": "200"},
"form11161625": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043d\u0435\u0437\u043d\u0430\u044e", "Name": "\u041c\u0430\u043a\u0441\u0438\u043c", "Lastname": "\u041f\u0435\u0440\u0435\u043f\u0435\u043b\u0438\u0446\u0430", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "village", "Television": "\u043d\u0435\u0437\u043d\u0430\u044e", "Sex": "male", "Age": "20"},
"form1117108": {"Language": "\u0430\u043d\u0433\u043b", "Iron": "\u044b", "Smartphone": "\u044b", "Name": "\u0432\u0432\u0432", "Lastname": "\u0432\u0432", "Kettle": "\u0432", "Residence": "village", "Coffee": "\u0443", "Television": "\u0432", "Sex": "male", "Age": "21"},
"form11171017": {"Iron": "prasowa\u0107", "Coffee": "Maszyna do kawy", "Smartphone": "telefon kom\u00f3rkowy", "Name": "J\u00f3zef", "Lastname": "J\u00f3zef", "Kettle": "czajnik", "Residence": "city", "Language": "polski", "Television": "telewizor", "Sex": "male", "Age": "140"},
"form11161738": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043a\u043e\u0444\u0435\u0432\u0430\u0440\u043a\u0430", "Name": "\u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440", "Lastname": "\u0428\u0430\u0440\u0430\u043f\u043e\u0432", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "city", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440\u041a\u0412\u041d", "Sex": "male", "Age": "26"},
"form11161615": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043a\u043e\u0444\u0435\u0432\u0430\u0440\u043a\u0430", "Name": "\u041c\u0430\u0448\u0430", "Lastname": "\u041f\u0435\u0440\u0435\u043a\u0438\u0434\u044b\u0448\u0438\u043d\u0441\u043a\u0430\u044f", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "village", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440", "Sex": "female", "Age": "33"},
"form1117107": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043a\u043e\u0444\u0435\u0432\u0430\u0440\u043a\u0430", "Smartphone": "\u0442\u0435\u043b\u0435\u0444\u043e\u043d", "Iron": "\u0443\u0442\u044e\u0433", "Name": "\u0410\u0439\u043d\u0430", "Lastname": "\u041a\u0430\u043c\u0438\u043b\u043e\u0432\u0430", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "city", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440", "Sex": "female", "Age": "19"},
"form11171241": {"Iron": "\u043f\u0440\u0430\u0441\u043a\u0430", "Language": "\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430", "Smartphone": "\u043c\u043e\u0431\u0456\u043b\u044c\u043d\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", "Name": "\u0422\u0430\u0440\u0430\u0441", "Lastname": "\u0428\u0435\u0432\u0447\u0435\u043d\u043a\u043e", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "village", "Coffee": "\u043a\u0430\u0432\u043e\u0432\u0430\u0440\u043a\u0430", "Television": "\u0442\u0435\u043b\u0435\u0432\u0456\u0437\u043e\u0440", "Sex": "male", "Age": "160"},
"form11161715": {"Language": "english", "Coffee": "coffe-maker", "Name": "Sherlock", "Lastname": "Holmes", "Kettle": "tea-pot", "Residence": "city", "Television": "neverseensuchthing", "Sex": "male", "Age": "46"}, "form11161636": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043d\u0435\u0437\u043d\u0430\u044e\u0442\u0430\u043a\u043e\u0433\u043e", "Name": "\u041c\u0430\u0440\u0443\u0441\u044f", "Lastname": "\u041a\u043b\u0438\u043c\u043e\u0432\u0430", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "city", "Television": "\u043d\u0435\u0432\u0438\u0434\u0435\u043b\u0430", "Sex": "female", "Age": "35"},
"form11161622": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043a\u043e\u0444\u0435\u043a\u043e\u0440\u044b\u0442\u043e", "Name": "\u041d\u0438\u043a\u043e\u043b\u0430", "Lastname": "\u041f\u0438\u0442\u0435\u0440\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "village", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440", "Sex": "male", "Age": "66"}, "form1117102": {"Language": "Deutsch", "Coffee": "Kaffeemaschine", "Iron": "Pl\u00e4tteisen", "Name": "Karl", "Lastname": "Marx", "Kettle": "Kessel", "Residence": "city", "Age": "150", "Television": "Fernsehger\u00e4t", "Sex": "male", "Smartphone": "Mobiltelefon"},
"form11161723": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Coffee": "\u043d\u0438\u043a\u043e\u0433\u0434\u0430\u0442\u0430\u043a\u043e\u0433\u043e\u043d\u0435\u0432\u0438\u0434\u0435\u043b\u0430", "Name": "\u0417\u043e\u0441\u044f", "Lastname": "\u0421\u0438\u043d\u0438\u0446\u043a\u0430\u044f", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Residence": "city", "Television": "\u043d\u0435\u0432\u0438\u0434\u0435\u043b\u0430", "Sex": "female", "Age": "20"},
"form11161616": {"Language": "", "Coffee": "", "Name": "", "Lastname": "", "Kettle": "", "Residence": "city", "Television": "", "Sex": "male", "Age": ""}, "form11161613": {"Language": "", "Coffee": "", "Name": "", "Lastname": "", "Kettle": "", "Residence": "city", "Television": "", "Sex": "male", "Age": ""}}
'''
alldict = json.loads(json_string)

print(alldict)
print('-------')
print(alldict['form11171010'])
print('-------')
print(alldict['form11171010']['Name'], alldict['form11171010']['Lastname'] )
print('-------')
for key in alldict.keys():
    print(key, end=' ')
print('-------')
for value in alldict.values():
    print(value)
print('-------')
