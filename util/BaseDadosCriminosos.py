from random import randrange
from util.Util import to_s
import random
from model.DataSet import DataSet

def get_tipo_crimes():
    return crimes

def get_criminosos():
    return criminosos


crimes = ["Terrorismo",
          "Tráfico de drogas",
          "Tráfico de pessoas",
          "Homicídio",
          "Estupro",
          "Ofensas à integridade física graves",
          "Roubo Organizado",
          "Homicídio Qualificado",
          "Matar",
          "Extorsão",
          "Crime de Guerra",
          "Atear fogo em pessoas",
          "Roubo qualificado",
          "Assassinato",
          "Tentativa de homicídio",
          "Sequestro",
          "Exploração Sexual",
          "Pedofilia",
          "Pornografia Infantil",
          "Máfia",
          "Assalto a mão armada",
          "Fraude",
          "Homicídio por asfixia",
          "Organização Criminosa",
          "Tráfico de armas",
          "Lavagem de dinheiro",
          "Peculato",
          "Propina",
          "Corrupção Ativa",
          "Corrupção Passiva",
          "Assassino de Aluguel",
          "Grilagem"
          ]
criminosos = [
    DataSet("Matteo Denaro Messina", [
        crimes[11] ,crimes[26] ,crimes[1] ,crimes[29] , crimes[13] ,]),
    DataSet("Salah Abdeslam", [
        crimes[27] ,crimes[21] ,crimes[3] ,crimes[11] ,crimes[22] ,crimes[12] ,crimes[28] ,crimes[3] ,]),
    DataSet("Hasen Amhamed Aksema", [
        crimes[14] ,crimes[22] ,crimes[4] ,crimes[31] ,crimes[11] ,]),
    DataSet("Simon Arnamo", [
        crimes[30] ,crimes[2] ,crimes[20] ,crimes[30] ,crimes[23] ,]),
    DataSet("Issei Sagawa", [
        crimes[28] ,crimes[26] ,crimes[26] ,crimes[8] ,],),
    DataSet("David Gras", [
        crimes[24] ,crimes[19] ,crimes[24] ,],),
    DataSet("Róbert Farkas", [
        crimes[9] ,crimes[30] ,crimes[27] ,]),
    DataSet("Panayiotis Netzati", [
        crimes[1] ,crimes[14] ,crimes[6] ,crimes[7] ,crimes[10] ,crimes[29] ,]),
    DataSet(    "Giedrius Poderskis", [
        crimes[4] ,crimes[14] ,crimes[4] ,crimes[15] ,crimes[28] ,crimes[18] ,]),
    DataSet("Mohamed Guibli", [
        crimes[18] ,crimes[30] ,crimes[18] ,crimes[3] ,crimes[11] ,crimes[20] ,crimes[9] ,]),
    DataSet(    "Armen Oganesjan", [
        crimes[8] ,crimes[16] ,crimes[24] ,]),
    DataSet("Ernesto Fazzalari", [
        crimes[21] ,crimes[4] ,crimes[12] ,crimes[29] ,crimes[17] ,crimes[24] ,crimes[2] ,crimes[13] ,])          ,
    DataSet("Rafał Czerwoniec", [
        crimes[4] ,crimes[16] ,crimes[13] ,]),
    DataSet("Yoshio Kodama", [
        crimes[10], crimes[24], crimes[4], crimes[29], crimes[25], crimes[21]]),
    DataSet("Emamali Ghader Esmaeil Zadeh", [
        crimes[29], crimes[22], crimes[26], crimes[3], crimes[16], crimes[3], crimes[11], crimes[21],
        crimes[8]]),
    DataSet("Ringaila Algimantas", [
        crimes[23], crimes[4], crimes[1]]),
    DataSet("Shoko Asahara", [
        crimes[11], crimes[27], crimes[8], crimes[24], crimes[31]]),
    DataSet("Mihails Korablovs", [
        crimes[30], crimes[31], crimes[13], crimes[13], crimes[9], crimes[22], crimes[28]]),
    DataSet("Marina Cecilia Kettunen", [
        crimes[20], crimes[22], crimes[16]]),
    DataSet("Radomir Cvijanovic", [
        crimes[19], crimes[22], crimes[22]]),
    DataSet("Patrik Šnajdr", [
        crimes[28], crimes[26], crimes[3]]),
    DataSet("Róbert Nigut", [
        crimes[3], crimes[26], crimes[5], crimes[21], crimes[9], crimes[30]]),
    DataSet("Amim Boali", [
        crimes[3], crimes[15], crimes[13], crimes[25], crimes[11], crimes[19], crimes[6]]),
    DataSet("Zakaria Benaissa", [
        crimes[6], crimes[4], crimes[22], crimes[5], crimes[2], crimes[26], crimes[5], crimes[29]]),
    DataSet("Tomáš Harmaceck", [
        crimes[7], crimes[1], crimes[18], crimes[27], crimes[1], crimes[19]]),
    DataSet("Sada Abe", [
        crimes[0], crimes[13], crimes[12], crimes[7], crimes[11], crimes[8], crimes[17], crimes[28]]),
    DataSet("Sasnauskas Martynas", [
        crimes[9], crimes[1], crimes[5]]),
    DataSet("Cumali Ata", [
        crimes[12], crimes[14], crimes[17], crimes[6]]),
    DataSet("Jesovnik Darjan", [
        crimes[27], crimes[16], crimes[15], crimes[3], crimes[16], crimes[4], crimes[26], crimes[16]]),
    DataSet("Tibor Foco", [
        crimes[13], crimes[23], crimes[23], crimes[8], crimes[19], crimes[14], crimes[16], crimes[21],
        crimes[31]]),
    DataSet("Mohamed Abrini", [
        crimes[8], crimes[19], crimes[18], crimes[18], crimes[4], crimes[15]]),
    DataSet("Arunas Algirdo Garsva", [
        crimes[5], crimes[1], crimes[1], crimes[23], crimes[1], crimes[23], crimes[30], crimes[17]]),
    DataSet("Dragicevic Bojan", [
        crimes[4], crimes[20], crimes[4], crimes[30], crimes[31], crimes[10], crimes[29], crimes[5],
        crimes[17]]),
    DataSet("Ahmed Numan Isaac Rahma", [
        crimes[17], crimes[19], crimes[4], crimes[16], crimes[12], crimes[18], crimes[8], crimes[14]]),
    DataSet("Dominique Delattre", [
        crimes[13], crimes[30], crimes[22], crimes[10], crimes[1], crimes[22]]),
    DataSet("Tsutomu Miyazaki", [
        crimes[14], crimes[21], crimes[30], crimes[9], crimes[29], crimes[11], crimes[20]]),
    DataSet("Robert Veaceslav Girleanu", [
        crimes[12], crimes[18], crimes[26], crimes[9]]),
    DataSet("Zeljko Bojanic", [
        crimes[29], crimes[27], crimes[30], crimes[20], crimes[9], crimes[29], crimes[25], crimes[24]]),
    DataSet("Jean Marc Sirichai Kiesch", [
        crimes[11], crimes[6], crimes[3], crimes[31], crimes[10], crimes[11], crimes[24], crimes[16]]),
    DataSet("Gregorian Bivolaru", [
        crimes[31], crimes[30], crimes[1], crimes[19]]),
    DataSet("Hiroshi Maeue", [
        crimes[4], crimes[17], crimes[30], crimes[4], crimes[14], crimes[16], crimes[31], crimes[9]]),
    DataSet("Esteban Vacas Garcia", [
        crimes[9], crimes[18], crimes[7], crimes[5], crimes[29], crimes[30], crimes[7], crimes[31]]),
    DataSet("Jean-Claude Lacote", [
        crimes[4], crimes[6], crimes[19], crimes[23], crimes[11], crimes[30], crimes[17], crimes[5]]),
    DataSet("Derek Fergunson", [
        crimes[22], crimes[12], crimes[16], crimes[13], crimes[1], crimes[13]]),
    DataSet("Kenichi Shinoda", [
        crimes[11], crimes[9], crimes[13], crimes[27], crimes[16], crimes[10], crimes[12]]),
    DataSet("Kajetan Poznanski", [
        crimes[11], crimes[11], crimes[30], crimes[26], crimes[6], crimes[27]]),
    DataSet("Robert Hauer", [
        crimes[15], crimes[20], crimes[1], crimes[13], crimes[11]]),
    DataSet("Tibor Varjú", [
        crimes[26], crimes[2], crimes[4], crimes[28], crimes[9]]),
    DataSet("Izet Ajdinovic", [
        crimes[6], crimes[12], crimes[18], crimes[31]]),
    DataSet("Hime Lufaj", [
        crimes[26], crimes[27], crimes[24], crimes[6], crimes[8], crimes[16], crimes[28], crimes[22]]),
    DataSet("Matteo Denaro Messina", [
        crimes[11] ,crimes[26] ,crimes[1] ,crimes[29] , crimes[13] ,]),
    DataSet("Salah Abdeslam", [
        crimes[27] ,crimes[21] ,crimes[3] ,crimes[11] ,crimes[22] ,crimes[12] ,crimes[28] ,crimes[3] ,]),
    DataSet("Hasen Amhamed Aksema", [
        crimes[14] ,crimes[22] ,crimes[4] ,crimes[31] ,crimes[11] ,]),
    DataSet("Simon Arnamo", [
        crimes[30] ,crimes[2] ,crimes[20] ,crimes[30] ,crimes[23] ,]),
    DataSet("Issei Sagawa", [
        crimes[28] ,crimes[26] ,crimes[26] ,crimes[8] ,],),
    DataSet("David Gras", [
        crimes[24] ,crimes[19] ,crimes[24] ,],),
    DataSet("Róbert Farkas", [
        crimes[9] ,crimes[30] ,crimes[27] ,]),
    DataSet("Panayiotis Netzati", [
        crimes[1] ,crimes[14] ,crimes[6] ,crimes[7] ,crimes[10] ,crimes[29] ,]),
    DataSet(    "Giedrius Poderskis", [
        crimes[4] ,crimes[14] ,crimes[4] ,crimes[15] ,crimes[28] ,crimes[18] ,]),
    DataSet("Mohamed Guibli", [
        crimes[18] ,crimes[30] ,crimes[18] ,crimes[3] ,crimes[11] ,crimes[20] ,crimes[9] ,]),
    DataSet(    "Armen Oganesjan", [
        crimes[8] ,crimes[16] ,crimes[24] ,]),
    DataSet("Ernesto Fazzalari", [
        crimes[21] ,crimes[4] ,crimes[12] ,crimes[29] ,crimes[17] ,crimes[24] ,crimes[2] ,crimes[13] ,])          ,
    DataSet("Rafał Czerwoniec", [
        crimes[4] ,crimes[16] ,crimes[13] ,]),
    DataSet("Yoshio Kodama", [
        crimes[10], crimes[24], crimes[4], crimes[29], crimes[25], crimes[21]]),
    DataSet("Emamali Ghader Esmaeil Zadeh", [
        crimes[29], crimes[22], crimes[26], crimes[3], crimes[16], crimes[3], crimes[11], crimes[21],
        crimes[8]]),
    DataSet("Ringaila Algimantas", [
        crimes[23], crimes[4], crimes[1]]),
    DataSet("Shoko Asahara", [
        crimes[11], crimes[27], crimes[8], crimes[24], crimes[31]]),
    DataSet("Mihails Korablovs", [
        crimes[30], crimes[31], crimes[13], crimes[13], crimes[9], crimes[22], crimes[28]]),
    DataSet("Marina Cecilia Kettunen", [
        crimes[20], crimes[22], crimes[16]]),
    DataSet("Radomir Cvijanovic", [
        crimes[19], crimes[22], crimes[22]]),
    DataSet("Patrik Šnajdr", [
        crimes[28], crimes[26], crimes[3]]),
    DataSet("Róbert Nigut", [
        crimes[3], crimes[26], crimes[5], crimes[21], crimes[9], crimes[30]]),
    DataSet("Amim Boali", [
        crimes[3], crimes[15], crimes[13], crimes[25], crimes[11], crimes[19], crimes[6]]),
    DataSet("Zakaria Benaissa", [
        crimes[6], crimes[4], crimes[22], crimes[5], crimes[2], crimes[26], crimes[5], crimes[29]]),
    DataSet("Tomáš Harmaceck", [
        crimes[7], crimes[1], crimes[18], crimes[27], crimes[1], crimes[19]]),
    DataSet("Sada Abe", [
        crimes[0], crimes[13], crimes[12], crimes[7], crimes[11], crimes[8], crimes[17], crimes[28]]),
    DataSet("Sasnauskas Martynas", [
        crimes[9], crimes[1], crimes[5]]),
    DataSet("Cumali Ata", [
        crimes[12], crimes[14], crimes[17], crimes[6]]),
    DataSet("Jesovnik Darjan", [
        crimes[27], crimes[16], crimes[15], crimes[3], crimes[16], crimes[4], crimes[26], crimes[16]]),
    DataSet("Tibor Foco", [
        crimes[13], crimes[23], crimes[23], crimes[8], crimes[19], crimes[14], crimes[16], crimes[21],
        crimes[31]]),
    DataSet("Mohamed Abrini", [
        crimes[8], crimes[19], crimes[18], crimes[18], crimes[4], crimes[15]]),
    DataSet("Arunas Algirdo Garsva", [
        crimes[5], crimes[1], crimes[1], crimes[23], crimes[1], crimes[23], crimes[30], crimes[17]]),
    DataSet("Dragicevic Bojan", [
        crimes[4], crimes[20], crimes[4], crimes[30], crimes[31], crimes[10], crimes[29], crimes[5],
        crimes[17]]),
    DataSet("Ahmed Numan Isaac Rahma", [
        crimes[17], crimes[19], crimes[4], crimes[16], crimes[12], crimes[18], crimes[8], crimes[14]]),
    DataSet("Dominique Delattre", [
        crimes[13], crimes[30], crimes[22], crimes[10], crimes[1], crimes[22]]),
    DataSet("Tsutomu Miyazaki", [
        crimes[14], crimes[21], crimes[30], crimes[9], crimes[29], crimes[11], crimes[20]]),
    DataSet("Robert Veaceslav Girleanu", [
        crimes[12], crimes[18], crimes[26], crimes[9]]),
    DataSet("Zeljko Bojanic", [
        crimes[29], crimes[27], crimes[30], crimes[20], crimes[9], crimes[29], crimes[25], crimes[24]]),
    DataSet("Jean Marc Sirichai Kiesch", [
        crimes[11], crimes[6], crimes[3], crimes[31], crimes[10], crimes[11], crimes[24], crimes[16]]),
    DataSet("Gregorian Bivolaru", [
        crimes[31], crimes[30], crimes[1], crimes[19]]),
    DataSet("Hiroshi Maeue", [
        crimes[4], crimes[17], crimes[30], crimes[4], crimes[14], crimes[16], crimes[31], crimes[9]]),
    DataSet("Esteban Vacas Garcia", [
        crimes[9], crimes[18], crimes[7], crimes[5], crimes[29], crimes[30], crimes[7], crimes[31]]),
    DataSet("Jean-Claude Lacote", [
        crimes[4], crimes[6], crimes[19], crimes[23], crimes[11], crimes[30], crimes[17], crimes[5]]),
    DataSet("Derek Fergunson", [
        crimes[22], crimes[12], crimes[16], crimes[13], crimes[1], crimes[13]]),
    DataSet("Kenichi Shinoda", [
        crimes[11], crimes[9], crimes[13], crimes[27], crimes[16], crimes[10], crimes[12]]),
    DataSet("Kajetan Poznanski", [
        crimes[11], crimes[11], crimes[30], crimes[26], crimes[6], crimes[27]]),
    DataSet("Robert Hauer", [
        crimes[15], crimes[20], crimes[1], crimes[13], crimes[11]]),
    DataSet("Tibor Varjú", [
        crimes[26], crimes[2], crimes[4], crimes[28], crimes[9]]),
    DataSet("Izet Ajdinovic", [
        crimes[6], crimes[12], crimes[18], crimes[31]]),
    DataSet("Hime Lufaj", [
        crimes[26], crimes[27], crimes[24], crimes[6], crimes[8], crimes[16], crimes[28], crimes[22]]),
    DataSet("Matteo Denaro Messina", [
        crimes[11] ,crimes[26] ,crimes[1] ,crimes[29] , crimes[13] ,]),
    DataSet("Salah Abdeslam", [
        crimes[27] ,crimes[21] ,crimes[3] ,crimes[11] ,crimes[22] ,crimes[12] ,crimes[28] ,crimes[3] ,]),
    DataSet("Hasen Amhamed Aksema", [
        crimes[14] ,crimes[22] ,crimes[4] ,crimes[31] ,crimes[11] ,]),
    DataSet("Simon Arnamo", [
        crimes[30] ,crimes[2] ,crimes[20] ,crimes[30] ,crimes[23] ,]),
    DataSet("Issei Sagawa", [
        crimes[28] ,crimes[26] ,crimes[26] ,crimes[8] ,],),
    DataSet("David Gras", [
        crimes[24] ,crimes[19] ,crimes[24] ,],),
    DataSet("Róbert Farkas", [
        crimes[9] ,crimes[30] ,crimes[27] ,]),
    DataSet("Panayiotis Netzati", [
        crimes[1] ,crimes[14] ,crimes[6] ,crimes[7] ,crimes[10] ,crimes[29] ,]),
    DataSet(    "Giedrius Poderskis", [
        crimes[4] ,crimes[14] ,crimes[4] ,crimes[15] ,crimes[28] ,crimes[18] ,]),
    DataSet("Mohamed Guibli", [
        crimes[18] ,crimes[30] ,crimes[18] ,crimes[3] ,crimes[11] ,crimes[20] ,crimes[9] ,]),
    DataSet(    "Armen Oganesjan", [
        crimes[8] ,crimes[16] ,crimes[24] ,]),
    DataSet("Ernesto Fazzalari", [
        crimes[21] ,crimes[4] ,crimes[12] ,crimes[29] ,crimes[17] ,crimes[24] ,crimes[2] ,crimes[13] ,])          ,
    DataSet("Rafał Czerwoniec", [
        crimes[4] ,crimes[16] ,crimes[13] ,]),
    DataSet("Yoshio Kodama", [
        crimes[10], crimes[24], crimes[4], crimes[29], crimes[25], crimes[21]]),
    DataSet("Emamali Ghader Esmaeil Zadeh", [
        crimes[29], crimes[22], crimes[26], crimes[3], crimes[16], crimes[3], crimes[11], crimes[21],
        crimes[8]]),
    DataSet("Ringaila Algimantas", [
        crimes[23], crimes[4], crimes[1]]),
    DataSet("Shoko Asahara", [
        crimes[11], crimes[27], crimes[8], crimes[24], crimes[31]]),
    DataSet("Mihails Korablovs", [
        crimes[30], crimes[31], crimes[13], crimes[13], crimes[9], crimes[22], crimes[28]]),
    DataSet("Marina Cecilia Kettunen", [
        crimes[20], crimes[22], crimes[16]]),
    DataSet("Radomir Cvijanovic", [
        crimes[19], crimes[22], crimes[22]]),
    DataSet("Patrik Šnajdr", [
        crimes[28], crimes[26], crimes[3]]),
    DataSet("Róbert Nigut", [
        crimes[3], crimes[26], crimes[5], crimes[21], crimes[9], crimes[30]]),
    DataSet("Amim Boali", [
        crimes[3], crimes[15], crimes[13], crimes[25], crimes[11], crimes[19], crimes[6]]),
    DataSet("Zakaria Benaissa", [
        crimes[6], crimes[4], crimes[22], crimes[5], crimes[2], crimes[26], crimes[5], crimes[29]]),
    DataSet("Tomáš Harmaceck", [
        crimes[7], crimes[1], crimes[18], crimes[27], crimes[1], crimes[19]]),
    DataSet("Sada Abe", [
        crimes[0], crimes[13], crimes[12], crimes[7], crimes[11], crimes[8], crimes[17], crimes[28]]),
    DataSet("Sasnauskas Martynas", [
        crimes[9], crimes[1], crimes[5]]),
    DataSet("Cumali Ata", [
        crimes[12], crimes[14], crimes[17], crimes[6]]),
    DataSet("Jesovnik Darjan", [
        crimes[27], crimes[16], crimes[15], crimes[3], crimes[16], crimes[4], crimes[26], crimes[16]]),
    DataSet("Tibor Foco", [
        crimes[13], crimes[23], crimes[23], crimes[8], crimes[19], crimes[14], crimes[16], crimes[21],
        crimes[31]]),
    DataSet("Mohamed Abrini", [
        crimes[8], crimes[19], crimes[18], crimes[18], crimes[4], crimes[15]]),
    DataSet("Arunas Algirdo Garsva", [
        crimes[5], crimes[1], crimes[1], crimes[23], crimes[1], crimes[23], crimes[30], crimes[17]]),
    DataSet("Dragicevic Bojan", [
        crimes[4], crimes[20], crimes[4], crimes[30], crimes[31], crimes[10], crimes[29], crimes[5],
        crimes[17]]),
    DataSet("Ahmed Numan Isaac Rahma", [
        crimes[17], crimes[19], crimes[4], crimes[16], crimes[12], crimes[18], crimes[8], crimes[14]]),
    DataSet("Dominique Delattre", [
        crimes[13], crimes[30], crimes[22], crimes[10], crimes[1], crimes[22]]),
    DataSet("Tsutomu Miyazaki", [
        crimes[14], crimes[21], crimes[30], crimes[9], crimes[29], crimes[11], crimes[20]]),
    DataSet("Robert Veaceslav Girleanu", [
        crimes[12], crimes[18], crimes[26], crimes[9]]),
    DataSet("Zeljko Bojanic", [
        crimes[29], crimes[27], crimes[30], crimes[20], crimes[9], crimes[29], crimes[25], crimes[24]]),
    DataSet("Jean Marc Sirichai Kiesch", [
        crimes[11], crimes[6], crimes[3], crimes[31], crimes[10], crimes[11], crimes[24], crimes[16]]),
    DataSet("Gregorian Bivolaru", [
        crimes[31], crimes[30], crimes[1], crimes[19]]),
    DataSet("Hiroshi Maeue", [
        crimes[4], crimes[17], crimes[30], crimes[4], crimes[14], crimes[16], crimes[31], crimes[9]]),
    DataSet("Esteban Vacas Garcia", [
        crimes[9], crimes[18], crimes[7], crimes[5], crimes[29], crimes[30], crimes[7], crimes[31]]),
    DataSet("Jean-Claude Lacote", [
        crimes[4], crimes[6], crimes[19], crimes[23], crimes[11], crimes[30], crimes[17], crimes[5]]),
    DataSet("Derek Fergunson", [
        crimes[22], crimes[12], crimes[16], crimes[13], crimes[1], crimes[13]]),
    DataSet("Kenichi Shinoda", [
        crimes[11], crimes[9], crimes[13], crimes[27], crimes[16], crimes[10], crimes[12]]),
    DataSet("Kajetan Poznanski", [
        crimes[11], crimes[11], crimes[30], crimes[26], crimes[6], crimes[27]]),
    DataSet("Robert Hauer", [
        crimes[15], crimes[20], crimes[1], crimes[13], crimes[11]]),
    DataSet("Tibor Varjú", [
        crimes[26], crimes[2], crimes[4], crimes[28], crimes[9]]),
    DataSet("Izet Ajdinovic", [
        crimes[6], crimes[12], crimes[18], crimes[31]]),
    DataSet("Hime Lufaj", [
        crimes[26], crimes[27], crimes[24], crimes[6], crimes[8], crimes[16], crimes[28], crimes[22]]),
    DataSet("Matteo Denaro Messina", [
        crimes[11] ,crimes[26] ,crimes[1] ,crimes[29] , crimes[13] ,]),
    DataSet("Salah Abdeslam", [
        crimes[27] ,crimes[21] ,crimes[3] ,crimes[11] ,crimes[22] ,crimes[12] ,crimes[28] ,crimes[3] ,]),
    DataSet("Hasen Amhamed Aksema", [
        crimes[14] ,crimes[22] ,crimes[4] ,crimes[31] ,crimes[11] ,]),
    DataSet("Simon Arnamo", [
        crimes[30] ,crimes[2] ,crimes[20] ,crimes[30] ,crimes[23] ,]),
    DataSet("Issei Sagawa", [
        crimes[28] ,crimes[26] ,crimes[26] ,crimes[8] ,],),
    DataSet("David Gras", [
        crimes[24] ,crimes[19] ,crimes[24] ,],),
    DataSet("Róbert Farkas", [
        crimes[9] ,crimes[30] ,crimes[27] ,]),
    DataSet("Panayiotis Netzati", [
        crimes[1] ,crimes[14] ,crimes[6] ,crimes[7] ,crimes[10] ,crimes[29] ,]),
    DataSet(    "Giedrius Poderskis", [
        crimes[4] ,crimes[14] ,crimes[4] ,crimes[15] ,crimes[28] ,crimes[18] ,]),
    DataSet("Mohamed Guibli", [
        crimes[18] ,crimes[30] ,crimes[18] ,crimes[3] ,crimes[11] ,crimes[20] ,crimes[9] ,]),
    DataSet(    "Armen Oganesjan", [
        crimes[8] ,crimes[16] ,crimes[24] ,]),
    DataSet("Ernesto Fazzalari", [
        crimes[21] ,crimes[4] ,crimes[12] ,crimes[29] ,crimes[17] ,crimes[24] ,crimes[2] ,crimes[13] ,])          ,
    DataSet("Rafał Czerwoniec", [
        crimes[4] ,crimes[16] ,crimes[13] ,]),
    DataSet("Yoshio Kodama", [
        crimes[10], crimes[24], crimes[4], crimes[29], crimes[25], crimes[21]]),
    DataSet("Emamali Ghader Esmaeil Zadeh", [
        crimes[29], crimes[22], crimes[26], crimes[3], crimes[16], crimes[3], crimes[11], crimes[21],
        crimes[8]]),
    DataSet("Ringaila Algimantas", [
        crimes[23], crimes[4], crimes[1]]),
    DataSet("Shoko Asahara", [
        crimes[11], crimes[27], crimes[8], crimes[24], crimes[31]]),
    DataSet("Mihails Korablovs", [
        crimes[30], crimes[31], crimes[13], crimes[13], crimes[9], crimes[22], crimes[28]]),
    DataSet("Marina Cecilia Kettunen", [
        crimes[20], crimes[22], crimes[16]]),
    DataSet("Radomir Cvijanovic", [
        crimes[19], crimes[22], crimes[22]]),
    DataSet("Patrik Šnajdr", [
        crimes[28], crimes[26], crimes[3]]),
    DataSet("Róbert Nigut", [
        crimes[3], crimes[26], crimes[5], crimes[21], crimes[9], crimes[30]]),
    DataSet("Amim Boali", [
        crimes[3], crimes[15], crimes[13], crimes[25], crimes[11], crimes[19], crimes[6]]),
    DataSet("Zakaria Benaissa", [
        crimes[6], crimes[4], crimes[22], crimes[5], crimes[2], crimes[26], crimes[5], crimes[29]]),
    DataSet("Tomáš Harmaceck", [
        crimes[7], crimes[1], crimes[18], crimes[27], crimes[1], crimes[19]]),
    DataSet("Sada Abe", [
        crimes[0], crimes[13], crimes[12], crimes[7], crimes[11], crimes[8], crimes[17], crimes[28]]),
    DataSet("Sasnauskas Martynas", [
        crimes[9], crimes[1], crimes[5]]),
    DataSet("Cumali Ata", [
        crimes[12], crimes[14], crimes[17], crimes[6]]),
    DataSet("Jesovnik Darjan", [
        crimes[27], crimes[16], crimes[15], crimes[3], crimes[16], crimes[4], crimes[26], crimes[16]]),
    DataSet("Tibor Foco", [
        crimes[13], crimes[23], crimes[23], crimes[8], crimes[19], crimes[14], crimes[16], crimes[21],
        crimes[31]]),
    DataSet("Mohamed Abrini", [
        crimes[8], crimes[19], crimes[18], crimes[18], crimes[4], crimes[15]]),
    DataSet("Arunas Algirdo Garsva", [
        crimes[5], crimes[1], crimes[1], crimes[23], crimes[1], crimes[23], crimes[30], crimes[17]]),
    DataSet("Dragicevic Bojan", [
        crimes[4], crimes[20], crimes[4], crimes[30], crimes[31], crimes[10], crimes[29], crimes[5],
        crimes[17]]),
    DataSet("Ahmed Numan Isaac Rahma", [
        crimes[17], crimes[19], crimes[4], crimes[16], crimes[12], crimes[18], crimes[8], crimes[14]]),
    DataSet("Dominique Delattre", [
        crimes[13], crimes[30], crimes[22], crimes[10], crimes[1], crimes[22]]),
    DataSet("Tsutomu Miyazaki", [
        crimes[14], crimes[21], crimes[30], crimes[9], crimes[29], crimes[11], crimes[20]]),
    DataSet("Robert Veaceslav Girleanu", [
        crimes[12], crimes[18], crimes[26], crimes[9]]),
    DataSet("Zeljko Bojanic", [
        crimes[29], crimes[27], crimes[30], crimes[20], crimes[9], crimes[29], crimes[25], crimes[24]]),
    DataSet("Jean Marc Sirichai Kiesch", [
        crimes[11], crimes[6], crimes[3], crimes[31], crimes[10], crimes[11], crimes[24], crimes[16]]),
    DataSet("Gregorian Bivolaru", [
        crimes[31], crimes[30], crimes[1], crimes[19]]),
    DataSet("Hiroshi Maeue", [
        crimes[4], crimes[17], crimes[30], crimes[4], crimes[14], crimes[16], crimes[31], crimes[9]]),
    DataSet("Esteban Vacas Garcia", [
        crimes[9], crimes[18], crimes[7], crimes[5], crimes[29], crimes[30], crimes[7], crimes[31]]),
    DataSet("Jean-Claude Lacote", [
        crimes[4], crimes[6], crimes[19], crimes[23], crimes[11], crimes[30], crimes[17], crimes[5]]),
    DataSet("Derek Fergunson", [
        crimes[22], crimes[12], crimes[16], crimes[13], crimes[1], crimes[13]]),
    DataSet("Kenichi Shinoda", [
        crimes[11], crimes[9], crimes[13], crimes[27], crimes[16], crimes[10], crimes[12]]),
    DataSet("Kajetan Poznanski", [
        crimes[11], crimes[11], crimes[30], crimes[26], crimes[6], crimes[27]]),
    DataSet("Robert Hauer", [
        crimes[15], crimes[20], crimes[1], crimes[13], crimes[11]]),
    DataSet("Tibor Varjú", [
        crimes[26], crimes[2], crimes[4], crimes[28], crimes[9]]),
    DataSet("Izet Ajdinovic", [
        crimes[6], crimes[12], crimes[18], crimes[31]]),
    DataSet("Hime Lufaj", [
        crimes[26], crimes[27], crimes[24], crimes[6], crimes[8], crimes[16], crimes[28], crimes[22]]),
    DataSet("Ze Lezim", [
        crimes[2], crimes[10], crimes[13], crimes[31]])


]

def get_data(type="train"):
    if type=="train":
        return get_train()
    elif type=="test":
        return get_test()


def get_train():
    return criminosos[0:int(2*len(criminosos)/3)]

def get_test():
    return criminosos[int(2 * len(criminosos) / 3)+1:len(criminosos)]

def get_target(list):
    l = []
    for t in list:
        l.append(t.key)

    return l

def get_target_names():
    return get_target(criminosos)


#print(get_target_names())
def get_text_list(list):
    r = []
    for l in list:
        c="Crimes de "
        for v in l.values:
            c = c+" "+v+", "
        r.append(c)
    return r

def get_crimes(criminoso):
    for c in criminosos:
        if criminoso == c.key:
            print(c.values)
            break


print(get_crimes("Salah Abdeslam"))


