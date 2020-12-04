import json
import time

import yaml


class Timer:
    def start(self):
        start = time.time()
        return start

    def stop(self, start):
        stop = time.time() - start
        return stop


def parsingByModules(input, output):
    start = Timer().start()
    work = True
    try:
        with open(input, "r", encoding="utf-8") as fileIn:
            fileOut = json.load(fileIn)
        with open(output, "w", encoding="utf8") as fileIn:
            yaml.dump(fileOut, fileIn, default_flow_style=False, allow_unicode=True)
    except BaseException:
        work = False
    if work:
        print("parsingByModules: Парсинг прошёл успешно")
    else:
        print("parsingByModules: Во время парисинга произошла ошибка")
    parsingByModulesTime = Timer().stop(start)
    return parsingByModulesTime


def parsingByMySelf(fileIn, fileOut):
    start = Timer().start()
    work = True
    try:
        file1 = open(fileIn, "r", encoding="utf-8")
        file2 = open(fileOut, "w", encoding="utf-8")
        lessons = eval(file1.read())
        for i in range(5):
            lesson = str(lessons["lesson" + " " + str(i + 1)])
            lesson = lesson.replace("[", " ")
            lesson = lesson.replace("]", " ")
            lesson = eval(lesson)

            lessonDop1 = []
            for item in lesson:
                if item not in lessonDop1:
                    lessonDop1.append(item)
            lessonKeys = lessonDop1

            lessonDop2 = []
            for item in lesson.values():
                if item not in lessonDop2:
                    lessonDop2.append(item)
            lessonValues = lessonDop2

            file2.write("lesson" + " " + str(i + 1) + ":")
            file2.write("\n" + "-")
            for j in range(6):
                if j == 0:
                    file2.write(" " + str(lessonKeys[j]) + ": " + str(lessonValues[j]) + "\n")
                else:
                    file2.write("  " + str(lessonKeys[j]) + ": " + str(lessonValues[j]) + "\n")
        file1.close()
        file2.close()
    except BaseException:
        work = False
    if work:
        print("parsingByMySelf: Парсинг прошёл успешно")
    else:
        print("parsingByMySelf: Во время парсинга произошла ошибка")
    parsingByMySelfTime = Timer().stop(start)
    return parsingByMySelfTime


def comparison(time1, time2):
    print("\nВремя работы алгоритма с использованием специальных модулей:" + str(time1))
    print("Время работы моего алгоритма:" + str(time2))
    if time1 == time2:
        print("Мой алгоритм также эффективен, как и алгоритм с использованием специальных модулей")
    elif time1 < time2:
        print("Алгоритм с использованием специальных модулей эффективнее")
    elif time1 > time2:
        print("Мой алгоритм эффективнее")


comparison(parsingByModules("timetable.json", "timetableByModules.yaml"), parsingByMySelf("timetable.json", "timetableByMySelf.yaml"))
