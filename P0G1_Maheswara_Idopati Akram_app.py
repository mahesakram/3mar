'''
=================================================
Graded Challenge 1

Nama  : Maheswara Idopati Akram
Batch : RMT-42

Program ini dibuat untuk melakukan pencatatan To Do List dengan ditur penambahan dan penghapusan judul dan deskripsi
dan juga fitur pengubah status keselesaian.
=================================================
'''

def welcome():
  '''
  function untuk welcoming pengguna
  '''
  print("Selamat Datang di Aplikasi To-Do List Harian!")

def menu():
  '''
  function untuk menunujukan text menu
  '''
  print()
  print("Menu:")
  print("1. Menambah Tugas")
  print("2. Hapus Tugas")
  print("3. Tampilkan Daftar Tugas")
  print("4. Tandai Tugas sebagai Selesai")
  print("5. Exit")

class Task:
  '''
  class untuk menyimpan data judul, deskripsi, dan status tugas
  '''
  def __init__(self,judul,deskripsi, status):
    self.judul = judul
    self.deskripsi = deskripsi
    self.status = status
#######################################################
'''
  class dibuat hierarchy anak (Todolist) dan parent(Task)
  agar lebih mudah penggunaannya
  '''
class TodoList(Task):
  def __init__(self,judul,deskripsi, status):
    Task.__init__(self,judul,deskripsi, status)
    self.tasks = []
  '''
  function untuk menerima input menu dari user dan menampilkan menu
  '''
  def menu_class(self):
    i=0
    welcome()
    j=0
    while i == 0: 
      menu()
      pilihan = input("Pilihan: ")
######################################################

      if pilihan == "1":
        item.add()
        i = 0
#########################################

      elif pilihan == "2":
        item.delete()
        i = 0
#############################################

      elif pilihan == "3":
        item.show_list()
        i = 0
###################################################

      elif pilihan == "4":
        item.mark_finished()
        i = 0
#############################################

      elif pilihan == "5":
        print("Terima kasih! Sampai jumpa.")
        i = 1
##############################################

      else:
        print("Maaf, input tidak sesuai dengan pilihan dalam menu")
        print("Silahkan masukan ulang input sesuai pilihan dalam menu")
        print("e.g. \"Pilihan: 1\"")
        i = 0
###########################
  '''
  function untuk menambah isi list tugas
  '''
  def add(self):
    self.judul = input("Masukkan judul tugas: ")
    self.deskripsi = input("Masukkan deskripsi: ")
    self.status = "Belum Selesai"
    item_1 = Task(self.judul, self.deskripsi, self.status)

    self.tasks.append(item_1)
    print("Tugas ", item_1.judul," berhasil ditambahkan ke daftar.")
  '''
  function untuk menghapus isi list tugas
  '''
  def delete(self):
    item_judul = input("Masukkan judul tugas: ")
    n=0
    n1=2

    if len(self.tasks) == 0:
      check = item_judul
    else:
      check = self.tasks[n].judul

    while check != item_judul:
      if n == len(self.tasks):
        check = item_judul
        n1 = 0
        n=n-1
      
      check = self.tasks[n].judul
      n = n + 1

      if n1 == 0:
        check = item_judul
        n=n+3

    if n > len(self.tasks):
      print("Judul Not Found \nplease try again")
    else:
      if n == 0:
        if len(self.tasks) == 0:
          print("Daftar Kosong")
        else:
          self.tasks.pop(n)
      else:
        self.tasks.pop(n-1)
        print("Tugas ", item_judul," berhasil dihapus dari daftar.")
  '''
  function untuk mengubah status menjadi selesai
  '''
  def mark_finished(self):
    item_judul = input("Masukkan judul tugas: ")
    n=0
    n1=2

    if len(self.tasks) == 0:
      check = item_judul
    else:
      check = self.tasks[n].judul

    while check != item_judul:
      if n == len(self.tasks):
        check = item_judul
        n1 = 0
        n=n-1
      
      check = self.tasks[n].judul
      n = n + 1

      if n1 == 0:
        check = item_judul
        n=n+3

    if n > len(self.tasks):
      print("Judul Not Found \nplease try again")
    else:
      if n == 0:
        if len(self.tasks) == 0:
          print("Daftar Kosong")
        else:
          self.tasks[n].status = "Selesai"
      else:
        self.tasks[n-1].status = "Selesai"
        print("Tugas ", item_judul," berhasil ditandai selesai.")
  '''
  function untuk menunjukan isi list tugas
  '''
  def show_list(self):
    print("Daftar Tugas: ")
    for j in range(len(self.tasks)):
      print(j+1, ". ", self.tasks[j].judul, " - ", self.tasks[j].deskripsi," ",
            "(", self.tasks[j].status,")")
    if len(self.tasks) == 0:
      print("Daftar Kosong")
################################################

item = TodoList("item_judul", "item_deskripsi","Belum Selesai")
item.menu_class()
