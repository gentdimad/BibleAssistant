import flet as ft
from flet import Row, IconButton, icons, TextField, Text
import pandas as pd
import numpy as np
from urllib.parse import urlparse

ds = pd.read_csv("data/ASV_Bible.csv")
book = 1
chapter = 1
current = ds[ds['b'] == book]
current = current[current['c'] == chapter].reset_index()

def displayText(data, book, chapter):
        current = data[data['b'] == book]
        current = current[current['c'] == chapter].reset_index()
        otptTextText = ''
        for i in range(0, len(current['v'])):
            otptTextText = otptTextText + str(i+1) + ' ' + str(current.loc[i, 't']) + '\n'

        return otptTextText

def bookLength(data, book):
    current = data[data['b'] == book]
    length = 0
    
    for i in current['c']:
        if i != length:
            length += 1

    return length

def versNum(data, book, chapter):
    current = data[data['b'] == book]
    current = current[current['c'] == chapter].reset_index()
    length =  len(current['v'])

    return length

def main(page: ft.Page):
    global chapter
    global book
    global ds
    page.window_width = 770
    page.window_height = 500
    page.theme_mode = 'dark'
    page.title = "Bible"
    page.scroll = "adaptive"
    params = "Search"

    def bkName(book):
        match book:
            case 1: bookName = 'Genesis'
            case 2: bookName = 'Exodus'
            case 3: bookName = 'Leviticus'
            case 4: bookName = 'Numbers'
            case 5: bookName = 'Deuteronomy'
            case 6: bookName = 'Joshua'
            case 7: bookName = 'Judges'
            case 8: bookName = 'Ruth'
            case 9: bookName = '1 Samuel'
            case 10: bookName = '2 Samuel'
            case 11: bookName = '1 Kings'
            case 12: bookName = '2 Kings'
            case 13: bookName = '1 Chronicles'
            case 14: bookName = '2 Chronicles'
            case 15: bookName = 'Ezra'
            case 16: bookName = 'Nehemiah'
            case 17: bookName = 'Esther'
            case 18: bookName = 'Job'
            case 19: bookName = 'Psalms'
            case 20: bookName = 'Proverbs'
            case 21: bookName = 'Ecclesiastes'
            case 22: bookName = 'Song of Solomon'
            case 23: bookName = 'Isaiah'
            case 24: bookName = 'Jeremiah'
            case 25: bookName = 'Lamentations'
            case 26: bookName = 'Ezekiel'
            case 27: bookName = 'Daniel'
            case 28: bookName = 'Hosea'
            case 29: bookName = 'Joel'
            case 30: bookName = 'Amos'
            case 31: bookName = 'Obadiah'
            case 32: bookName = 'Jonah'
            case 33: bookName = 'Micah'
            case 34: bookName = 'Nahum'
            case 35: bookName = 'Habakkuk'
            case 36: bookName = 'Zephaniah'
            case 37: bookName = 'Haggai'
            case 38: bookName = 'Zechariah'
            case 39: bookName = 'Malachi'
            case 40: bookName = 'Matthew'
            case 41: bookName = 'Mark'
            case 42: bookName = 'Luke'
            case 43: bookName = 'John'
            case 44: bookName = 'Acts'
            case 45: bookName = 'Romans'
            case 46: bookName = '1 Corinthians'
            case 47: bookName = '2 Corinthians'
            case 48: bookName = 'Galatians'
            case 49: bookName = 'Ephesians'
            case 50: bookName = 'Philippians'
            case 51: bookName = 'Colossians'
            case 52: bookName = '1 Thessalonians'
            case 53: bookName = '2 Thessalonians'
            case 54: bookName = '1 Timothy'
            case 55: bookName = '2 Timothy'
            case 56: bookName = 'Titus'
            case 57: bookName = 'Philemon'
            case 58: bookName = 'Hebrews'
            case 59: bookName = 'James'
            case 60: bookName = '1 Peter'
            case 61: bookName = '2 Peter'
            case 62: bookName = '1 John'
            case 63: bookName = '2 John'
            case 64: bookName = '3 John'
            case 65: bookName = 'Jude'
            case 66: bookName = 'Revelations'
        
        return bookName
    
    def button_clicked(e):
        global book
        global chapter
        
        header.value = str(bkName(bookNum(bk.value)) + ' ' + str(ch.value))
        textBody.value = str(displayText(ds, bookNum(bk.value), int(ch.value)))
        chapter = int(ch.value)
        book = bookNum(bk.value)
        page.update()
    
    def testament(e):
        if bt.value == "Old Testament":
            bk.value = "Genesis"
            bk.options=[
                ft.dropdown.Option("Genesis"),
                ft.dropdown.Option("Exodus"),
                ft.dropdown.Option("Leviticus"),
                ft.dropdown.Option("Numbers"),
                ft.dropdown.Option("Deuteronomy"),
                ft.dropdown.Option("Joshua"),
                ft.dropdown.Option("Judges"),
                ft.dropdown.Option("Ruth"),
                ft.dropdown.Option("1 Samuel"),
                ft.dropdown.Option("2 Samuel"),
                ft.dropdown.Option("1 Kings"),
                ft.dropdown.Option("2 Kings"),
                ft.dropdown.Option("1 Chronicles"),
                ft.dropdown.Option("2 Chronicles"),
                ft.dropdown.Option("Ezra"),
                ft.dropdown.Option("Nehemiah"),
                ft.dropdown.Option("Esther"),
                ft.dropdown.Option("Job"),
                ft.dropdown.Option("Psalms"),
                ft.dropdown.Option("Proverbs"),
                ft.dropdown.Option("Ecclesiastes"),
                ft.dropdown.Option("Song of Solomon"),
                ft.dropdown.Option("Isaiah"),
                ft.dropdown.Option("Jeremiah"),
                ft.dropdown.Option("Lamentations"),
                ft.dropdown.Option("Ezekiel"),
                ft.dropdown.Option("Daniel"),
                ft.dropdown.Option("Hosea"),
                ft.dropdown.Option("Joel"),
                ft.dropdown.Option("Amos"),
                ft.dropdown.Option("Obadiah"),
                ft.dropdown.Option("Jonah"),
                ft.dropdown.Option("Micah"),
                ft.dropdown.Option("Nahum"),
                ft.dropdown.Option("Habakkuk"),
                ft.dropdown.Option("Zephaniah"),
                ft.dropdown.Option("Haggai"),
                ft.dropdown.Option("Zechariah"),
                ft.dropdown.Option("Malachi"),
            ]
            bk.update()

            page.update()
        else:
            bk.value = "Matthew"
            bk.options=[
                ft.dropdown.Option("Matthew"),
                ft.dropdown.Option("Mark"),
                ft.dropdown.Option("Luke"),
                ft.dropdown.Option("John"),
                ft.dropdown.Option("Acts"),
                ft.dropdown.Option("Romans"),
                ft.dropdown.Option("1 Corinthians"),
                ft.dropdown.Option("2 Corinthians"),
                ft.dropdown.Option("Galatians"),
                ft.dropdown.Option("Ephesians"),
                ft.dropdown.Option("Philippians"),
                ft.dropdown.Option("Colossians"),
                ft.dropdown.Option("1 Thessalonians"),
                ft.dropdown.Option("2 Thessalonians"),
                ft.dropdown.Option("1 Timothy"),
                ft.dropdown.Option("2 Timothy"),
                ft.dropdown.Option("Titus"),
                ft.dropdown.Option("Philemon"),
                ft.dropdown.Option("Hebrews"),
                ft.dropdown.Option("James"),
                ft.dropdown.Option("1 Peter"),
                ft.dropdown.Option("2 Peter"),
                ft.dropdown.Option("1 John"),
                ft.dropdown.Option("2 John"),
                ft.dropdown.Option("3 John"),
                ft.dropdown.Option("Jude"),
                ft.dropdown.Option("Revelation"),

            ]
            bk.update()
            page.update()

    def bookNum(name):
        match name:
            case 'Genesis':         bookNum = 1
            case 'Exodus':          bookNum = 2
            case 'Leviticus':       bookNum = 3
            case 'Numbers':         bookNum = 4
            case 'Deuteronomy':     bookNum = 5
            case 'Joshua':          bookNum = 6
            case 'Judges':          bookNum = 7
            case 'Ruth':            bookNum = 8
            case '1 Samuel':        bookNum = 9
            case '2 Samuel':        bookNum = 10
            case '1 Kings':         bookNum = 11
            case '2 Kings':         bookNum = 12
            case '1 Chronicles':    bookNum = 13
            case '2 Chronicles':    bookNum = 14
            case 'Ezra':            bookNum = 15
            case 'Nehemiah':        bookNum = 16
            case 'Esther':          bookNum = 17
            case 'Job':             bookNum = 18
            case 'Psalms':          bookNum = 19
            case 'Proverbs':        bookNum = 20
            case 'Ecclesiastes':    bookNum = 21
            case 'Song of Solomon': bookNum = 22
            case 'Isaiah':          bookNum = 23
            case 'Jeremiah':        bookNum = 24
            case 'Lamentations':    bookNum = 25
            case 'Ezekiel':         bookNum = 26
            case 'Daniel':          bookNum = 27
            case 'Hosea':           bookNum = 28
            case 'Joel':            bookNum = 29
            case 'Amos':            bookNum = 30
            case 'Obadiah':         bookNum = 31
            case 'Jonah':           bookNum = 32
            case 'Micah':           bookNum = 33
            case 'Nahum':           bookNum = 34
            case 'Habakkuk':        bookNum = 35
            case 'Zephaniah':       bookNum = 36
            case 'Haggai':          bookNum = 37
            case 'Zechariah':       bookNum = 38
            case 'Malachi':         bookNum = 39
            case 'Matthew':         bookNum = 40
            case 'Mark':            bookNum = 41
            case 'Luke':            bookNum = 42
            case 'John':            bookNum = 43
            case 'Acts':            bookNum = 44
            case 'Romans':          bookNum = 45
            case '1 Corinthians':   bookNum = 46
            case '2 Corinthians':   bookNum = 47
            case 'Galatians':       bookNum = 48
            case 'Ephesians':       bookNum = 49
            case 'Philippians':     bookNum = 50
            case 'Colossians':      bookNum = 51
            case '1 Thessalonians': bookNum = 52
            case '2 Thessalonians': bookNum = 53
            case '1 Timothy':       bookNum = 54
            case '2 Timothy':       bookNum = 55
            case 'Titus':           bookNum = 56
            case 'Philemon':        bookNum = 57
            case 'Hebrews':         bookNum = 58
            case 'James':           bookNum = 59
            case '1 Peter':         bookNum = 60
            case '2 Peter':         bookNum = 61
            case '1 John':          bookNum = 62
            case '2 John':          bookNum = 63
            case '3 John':          bookNum = 64
            case 'Jude':            bookNum = 65
            case 'Revelations':     bookNum = 66
        
        return bookNum
    
    def books(e):
        ch.value = '1'
        ch.options = []
        for i in range(0, bookLength(ds, bookNum(bk.value))): ch.options.append(ft.dropdown.Option(str(i+1)))
        ch.update()

    def verses(e):
        vr.value = '1'
        vr.options = []
        for i in range(0, versNum(ds, bookNum(bk.value), int(ch.value))):
            vr.options.append(ft.dropdown.Option(str(i+1)))
        vr.update()

    #Initializing Dropdowns (First Page)
    b = ft.ElevatedButton(text="Go", bgcolor = 'white',
                color = 'black', on_click=button_clicked)
    bt = ft.Dropdown(value = "Old Testament",
        width=170,
        options=[
            ft.dropdown.Option("Old Testament"),
            ft.dropdown.Option("New Testament"),
        ],
        on_change = testament,
    )
    bk = ft.Dropdown( 
        value = "Genesis",
        width=170,
        options=[
                ft.dropdown.Option("Genesis"),
                ft.dropdown.Option("Exodus"),
                ft.dropdown.Option("Leviticus"),
                ft.dropdown.Option("Numbers"),
                ft.dropdown.Option("Deuteronomy"),
                ft.dropdown.Option("Joshua"),
                ft.dropdown.Option("Judges"),
                ft.dropdown.Option("Ruth"),
                ft.dropdown.Option("1 Samuel"),
                ft.dropdown.Option("2 Samuel"),
                ft.dropdown.Option("1 Kings"),
                ft.dropdown.Option("2 Kings"),
                ft.dropdown.Option("1 Chronicles"),
                ft.dropdown.Option("2 Chronicles"),
                ft.dropdown.Option("Ezra"),
                ft.dropdown.Option("Nehemiah"),
                ft.dropdown.Option("Esther"),
                ft.dropdown.Option("Job"),
                ft.dropdown.Option("Psalms"),
                ft.dropdown.Option("Proverbs"),
                ft.dropdown.Option("Ecclesiastes"),
                ft.dropdown.Option("Song of Solomon"),
                ft.dropdown.Option("Isaiah"),
                ft.dropdown.Option("Jeremiah"),
                ft.dropdown.Option("Lamentations"),
                ft.dropdown.Option("Ezekiel"),
                ft.dropdown.Option("Daniel"),
                ft.dropdown.Option("Hosea"),
                ft.dropdown.Option("Joel"),
                ft.dropdown.Option("Amos"),
                ft.dropdown.Option("Obadiah"),
                ft.dropdown.Option("Jonah"),
                ft.dropdown.Option("Micah"),
                ft.dropdown.Option("Nahum"),
                ft.dropdown.Option("Habakkuk"),
                ft.dropdown.Option("Zephaniah"),
                ft.dropdown.Option("Haggai"),
                ft.dropdown.Option("Zechariah"),
                ft.dropdown.Option("Malachi"),
            ],
            on_change = books,
    )

    ch = ft.Dropdown(value = "1",
        width=60,
        options=[],
        on_change = verses,
    )
    for i in range(0, bookLength(ds, bookNum(bk.value))): ch.options.append(ft.dropdown.Option(str(i+1)))

    vr = ft.Dropdown(value = "1",
        width=60,
        options=[
        ],
    )
    for i in range(0, versNum(ds, bookNum(bk.value), int(ch.value))): vr.options.append(ft.dropdown.Option(str(i+1)))

    header = Text(value = str(bkName(book) + ' ' + str(chapter)), text_align='left')
    textBody = Text(value = str(displayText(ds, book, chapter)), width = 650, selectable = True)
    
    def back(e):
        #Header Values
        global chapter
        global book
        global displayText

        if chapter >1:
            chapter -= 1
        else:
            if book >1:
                book -= 1
            chapter = bookLength(ds, book)

        header.value = str(bkName(book) + ' ' + str(chapter))
        textBody.value = str(displayText(ds, book, chapter))
        page.update()
    
    def next(e):
        #Header Values
        global chapter
        global book
        if chapter < bookLength(ds,book):
            chapter += 1
        else:
            if book < 66:
                book += 1
            chapter = 1

        header.value = str(bkName(book) + ' ' + str(chapter))
        textBody.value = str(displayText(ds, book, chapter))
        page.update()


    #Second Page Elements
    def findClick(e):
        col.controls = []
        findList, count = search(inpField.value.strip(' ').lower())
        col.controls.append(ft.Text(f"The word/s \"{inpField.value}\" comes out {count} times.\n", color = 'black',size = 13,weight = ft.FontWeight.BOLD ))
        for bk, ch, vr, tx in findList:
            col.controls.append(ft.Text(str((tx) + '\n' + bk) + ' ' + str(ch) + ' ' + ':' + ' ' + str(vr)+'\n', color = 'black', size = 13, weight = ft.FontWeight.BOLD))
        col.update()

    def search(text):
        global ds
        count = 0
        words = text.split()
        list = []
        for i in range(0, len(ds['v'])):
            content = ds.loc[i,'t'].strip("!?','").lower()
            for word in words:
                if word in content:
                    if (bkName(ds.loc[i,'b']),ds.loc[i,'c'],ds.loc[i,'v']) not in list:
                        list.append((bkName(ds.loc[i,'b']),ds.loc[i,'c'],ds.loc[i,'v'], ds.loc[i,'t']))
                        count+= 1

        return list, count

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    dlg = ft.AlertDialog(
        title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    inpField = TextField(value = " ", width = 500, border_color= 'white', border_radius = 20)
    find = ft.ElevatedButton(text="Find", bgcolor = 'white',
                color = 'black', on_click=findClick)
    col = ft.Column(spacing = 0, controls=[], height = 600, width = 530, scroll = 'adaptive', alignment='center')

    #Routing Elements
    router = ft.ElevatedButton(
                "Search",
                on_click=lambda _: page.go(f"/page/{params}"),
                bgcolor = 'white',
                color = 'black'
                
            )
    goBack = ft.ElevatedButton(
                "Read",
                on_click=lambda _: page.go("/"),
                bgcolor = 'white',
                color = 'black'
                
            )
        

    def route_change(route):
            page.views.clear()
            page.views.append(
                ft.View(
                    "/",
				    [
                    Row([bt, bk, ch, vr, b, router], spacing = 20),
                    Row([
                    header,
                    IconButton(icons.REMOVE, on_click=back),
                    IconButton(icons.ADD, on_click=next)
                    ]),
                    textBody
                    ], scroll = "adaptive"
			    )
            )
            # GET PARAM FROM HOME PAGE
            param = page.route
            # THIS IS GET VALUE AFTER /secondpage/THIS RES HERE
            res = urlparse(param).path.split("/")[-1]
            if page.route == f"/page/{res}":
                page.views.append(
                    ft.View(
                    f"/secondpage/{res}",
                        [
                        Text("You can look up any keywords or stories that you want to read through the input field below."),
                        Row([inpField, find, goBack], spacing = 20),
                        ft.Container(col, bgcolor = 'white', border_radius = 20, padding = 20)
                        ]
                    )
                )
    page.update()

    def view_pop(view):
            page.views.pop()
            myview = page.views[-1]
            page.go(myview.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)