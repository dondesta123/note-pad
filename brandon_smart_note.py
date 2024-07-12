""" NOTEPAD APP """

#step 1: import semua module
#karena mau bikin app -> window app
#window app modules -> pyqt5
from PyQt5.QtCore import * #core semua window app
from PyQt5.QtWidgets import * #btn, label, listwidget, dll
import json #file2nya

#step 2: bikin app & halaman utama
#app
app = QApplication([]) #([]) wajib
#halaman utama
hal_utama = QWidget()
#atur ukuran
hal_utama.resize(750,750) #width, height
hal_utama.setWindowTitle("Koala Note") #judul / nama app

#step 3: bikin panel list
#list kosong untuk nampung semua list catatan
notes = list()
#list2nya
list_notes = QListWidget()
#label
list_notes_text = QLabel("Note List:")
#btn panel list
btn_create = QPushButton("Create note")
btn_del = QPushButton("Delete note")
btn_save = QPushButton("Save note")

#step 4: bikin panel tag
#list kosong untuk simpen list tag
tags = list()
#list2nya
list_tag = QListWidget()
#label
list_tag_text = QLabel("Tag List:")

#field tag untuk mencari / menambahkan tag kpd note
field_tag = QLineEdit('')
field_tag.setPlaceholderText("Enter a tag")

#btn panel tag
btn_add_tag = QPushButton("Add a tag")
btn_untag = QPushButton("Untag")
btn_search_tag = QPushButton("Search a tag")

#step 5: bikin panel untuk edit kolom text
field_text = QTextEdit()

#step 6: bikin layout
#6.1. bikin layout utama
main_layout = QHBoxLayout() #kolom text & panel list tag
                            #samping2an

#6.2. layout kolom text
layout_field_text = QVBoxLayout() #kolom text nya mau dari atas-bawah
layout_field_text.addWidget(field_text)

#6.3. layout panel list
layout_panel_list_tag = QVBoxLayout()
#taruh dulu label text note list
layout_panel_list_tag.addWidget(list_notes_text)
#taruh lagi list widget untuk tampilin semua note
layout_panel_list_tag.addWidget(list_notes)

#6.3.1. btn panel list
#btn row 1
layout_btn_list1 = QHBoxLayout()
layout_btn_list1.addWidget(btn_create)
layout_btn_list1.addWidget(btn_del)

#btn row 2
layout_btn_list2 = QHBoxLayout()
layout_btn_list2.addWidget(btn_save)

#6.3.2. masukin btn panel list, ke dalam layout panel list
layout_panel_list_tag.addLayout(layout_btn_list1)
layout_panel_list_tag.addLayout(layout_btn_list2)

#6.4. layout panel tag
#tambahin dulu label text
layout_panel_list_tag.addWidget(list_tag_text)
#tambahin list widget untuk tampilin semua tag
layout_panel_list_tag.addWidget(list_tag)
#tambahin field tag -> masukin tag / search tag
layout_panel_list_tag.addWidget(field_tag)

#6.4.1. btn panel tag
#btn row 1
layout_btn_tag1 = QHBoxLayout()
layout_btn_tag1.addWidget(btn_add_tag)
layout_btn_tag1.addWidget(btn_untag)

#btn row 2
layout_btn_tag2 = QHBoxLayout()
layout_btn_tag2.addWidget(btn_search_tag)

#6.4.2. tambahin btn panel tag ke dalam layout panel tag
layout_panel_list_tag.addLayout(layout_btn_tag1)
layout_panel_list_tag.addLayout(layout_btn_tag2)

#6.5. taruh layout kolom text & panel list tag ke dalam
#main layout
main_layout.addLayout(layout_field_text, stretch=2)
main_layout.addLayout(layout_panel_list_tag, stretch=1)

#Step 7: buat fungsi2nya
#7.1. fungsi untuk create a note
def create_note():
    #input dialog untuk masukin judul note
    note_name, ok = QInputDialog.getText(hal_utama,"Add note", "Note name:")
    #cek jika betul input dialog sudah diisi
    #dan note name tidak kosong
    if ok and note_name != "":
        #list kosong untuk note tersebut
        note = list()
        #struktur untuk note tersebut
        note = [note_name, '', []] #[judul, isi, list tag]
        #masukin struktur note ke dalam list notes
        notes.append(note)
        #masukin note baru kedalam list note yg di layar
        list_notes.addItem(note[0])
        #masukin tag pada note baru ke dalam list tag yg di layar
        list_tag.addItems(note[2])
        #simpan ke dalam txt file
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')
        #print list notes tsb
        print(notes)

#7.2. delete note
def del_note():
    #cek note mana yg kita pilih
    #jika ada note pada list notes di layar
    #yg di pilih
    if list_notes.selectedItems():
        #cari tau dulu, judul note dari note yg kita pilih
        judul_note = list_notes.selectedItems()[0].text()
        #cek satu per satu
        #untuk setiap note pada list notes
        for note in notes:
            #cek jika ada note yg judulnya sama
            if note[0] == judul_note:
                #clear semua
                field_text.clear()
                list_tag.clear()
                field_tag.clear()
                #remove note tsb dalam list notes
                list_notes.takeItem(list_notes.currentRow())
                notes.remove(note)
        #simpan lagi ke dalam file txt
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')
        print(notes)
    #jika gak ada note yg dipilih
    else:
        #kirim alert bahwa belum ada note yg dipilih
        print("Belum ada note yg dipilih")
#7.3. save note
def save_note():
    #cek note mana yg kita pilih
    #jika ada note pada list notes di layar
    #yg di pilih
    if list_notes.selectedItems():
        #cari tau dulu, judul note dari note yg kita pilih
        judul_note = list_notes.selectedItems()[0].text()
        #butuh index / urutan untuk simpan file note txt
        index = 0
        #cek satu per satu
        #untuk setiap note pada list notes
        for note in notes:
            #cek jika ada note dgn judul yg sama
            if note[0] == judul_note:
                #simpan text pada kolom text
                note[1] = field_text.toPlainText()
                #simpan lagi ke dalam file txt
                with open(str(index)+'.txt','w') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    #simpan list tag
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index+=1
        print(notes)
    #jika tidak ada note yg dipilih
    else:
        print("Note yang ingin di save, belum dipilih")

#7.4. fungsi untuk tambah tag pada note
def add_tag():
    #cek note mana yg kita pilih
    #jika ada note pada list notes di layar
    #yg di pilih
    if list_notes.selectedItems():
        #harus tau judul note yg kita pilih
        judul_note = list_notes.selectedItems()[0].text()
        #tag nya itu ada di dalam field tag
        tag = field_tag.text()
        #cek masing2 note
        for note in notes:
            #jika ada note dgn judul note yg kita pilih
            #dan tag pada note tsb, belum ada
            if note[0] == judul_note and note[2] != tag:
                #taruh tag pada note tsb
                note[2] = tag
                #tambahin tag pada list
                list_tag.addItem(tag)
                #clear in field tag
                field_tag.clear()
        #simpan lagi ke dalam file txt
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')
        print(notes)
    #belum ada note yg dipilih
    else:
        print("Belum ada note yg dipilih")

#7.5. buat fungsi untuk cari note berdasarkan tag
def search_note_by_tag():
    #cari tau dulu apa yg kita ketik
    tag = field_tag.text()
    print(btn_search_tag.text())
    #jika betul btn yg kita klik adalah btn search
    #dan tag nya tidak kosong / True
    if btn_search_tag.text() == "Search a tag" and tag:
        #print tag
        print(tag)
        notes_filter = {} #dictionary
        #cek satu per satu note
        for note in notes:
            #cek jika ada tag tsb di dalam salah satu note
            if tag in notes[note][2]:
                #maka notes filter akan di simpan
                notes_filter[note]=notes[note]
        #ganti btn text
        btn_search_tag.setText("reset search")
        #clear in semua
        list_notes.clear()
        list_tag.clear()
        #masukin data yg baru
        list_notes.addItems(notes_filter)
        #print btn text
        print(btn_search_tag.text())
    #jika btn text = reset search
    elif btn_search_tag.text() == "reset search":
        #clear in semua
        list_notes.clear()
        list_tag.clear()
        field_tag.clear()
        #masukin lagi data baru
        list_notes.addItems(notes)
        #ganti lagi btn textnya
        btn_search_tag.setText("Search a tag")
    #kalau bukan btn search a tag / reset search
    else:
        #maka pass aja
        pass

#7.6. buat fungsi untuk delete tag
def untag():
    #cek note mana yg kita pilih
    #jika ada note pada list notes di layar
    #yg di pilih
    if list_notes.selectedItems():
        #harus tau judul note yg kita pilih
        judul_note = list_notes.selectedItems()[0].text()
        #harus tau nama tag
        tag = list_tag.selectedItems()[0].text()
        #baru remove
        for note in notes:
            #cek, jika ada note dgn judul note yg sama
            #dan isi list tag berisikan tag yg ingin kita hapus
            if note[0] == judul_note and note[2] == tag:
               # list_notes.clear()
               # field_tag.clear()
                list_tag.takeItem(list_tag.currentRow())
                notes.remove(note)
                #simpan lagi ke dalam file txt
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')
        print(notes)
    #belum ada note yg dipilih
    else:
        print("Belum ada note yg dipilih")
#step 8:
#koneksiin btn2nya
btn_create.clicked.connect(create_note)
btn_del.clicked.connect(del_note)
btn_save.clicked.connect(save_note)
btn_add_tag.clicked.connect(add_tag)
btn_untag.clicked.connect(untag)
btn_search_tag.clicked.connect(search_note_by_tag)
#step 9: set layout utama ke halaman utama
hal_utama.setLayout(main_layout)
#show halaman utama
hal_utama.show()
#jalanin app nya
app.exec()
            