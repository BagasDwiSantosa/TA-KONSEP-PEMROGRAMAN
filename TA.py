# Buat 2 file txt bernama score.txt dan saran.txt dalam satu folder dengan program ini.
# Copy soal-soal kuis pada file txt soal.txt yang telah diupload di github ini.

print(' '+'_'*75+' ')
print('|'+' '*75+'|')
print('|'+'='*10+'-'*8+'>'+' '*9+" PYTHON GAME QUIZ  "+' '*9+'<'+'-'*8+'='*10+'|')
print('|'+'_'*27+" ! ENJOY THE GAME ! "+'_'*28+'|')
print('|'+'_'*75+'|')


try:
    nilai = 0

    nama = input("\n Masukkan nama anda : ")
    ucapan = ("""\n Welcome {} to Python Game Quiz... 
          Belajar dan Bersenang-senang, Enjoy the Game...!!!""".format(nama))
    print(ucapan)
    print(input("\n Tekan entar untuk lanjut..."))

except ValueError:
    print("  Masukkan nama anda bukan yang lainnya.")


def menu():
    try:
        menu = ["1. Kuis Basic Pemrograman Python","2. Data Score Kuis Pemrograman Python", "3. Info kami", 
        "4. Saran dan Tanggapan ", "5. Keluar Program"]      
        print(' '+'_'*75+' ')
        print('|'+' '*75+'|')
        print('|'+'='*7+'-'*5+'>'+' '*3+" Silahkan Pilih Opsi dibawah untuk bermain "+' '*3+'<'+'-'*5+'='*7+'|')   
        print('|'+' '*18+ menu[0]+' '*25+'|')
        print('|'+' '*18+ menu[1]+' '*20+'|')
        print('|'+' '*18+ menu[2]+' '*45+'|')
        print('|'+' '*18+ menu[3]+' '*34+'|')
        print('|'+' '*18+ menu[4]+' '*40+'|')
        print('|'+'_'*75+'|')
        pilihan = int(input("\n Masukkan pilihan anda : "))
        return pilihan

    except ValueError:
        print(" Masukan pilihan anda dengan angka bukan huruf.")

def kuis_1():
    try:
        file = open ("soal.txt","r")
        kuis= file.readlines()
        file.close()
        return kuis
    except FileNotFoundError:
        print("File tidak ada")

def score():
    print(' '+'_'*75+' ')
    print('|'+' '*75+'|')
    print('|'+'='*8+'-'*8+'>'+' '*3+" Data Score Akhir Python Game Kuis "+' '*3+'<'+'-'*8+'='*8+'|')
    print('|'+'_'*75+'|')
    convert = str(nilai)
    score = open("score.txt","a+")
    semua = "  {} Score akhir = {}\n".format(nama,convert)
    score.write(semua)
    score.close()
    read = open("score.txt","r")
    print( read.read())
    read.close()
    return convert


def info_kami():
    print(' '+'_'*75+' ')
    print('|'+' '*75+'|')
    print('|'+'='*8+'-'*8+'>'+' '*5+" Tugas Akhir Konsep Pemrograman "+' '*4+'<'+'-'*8+'='*8+'|')
    print('|'+'_'*28+" Program Game QUIZ "+'_'*28+'|')
    print('|'+' '*75+'|')

    print('|'+'='*8+'-'*8+'>'+' '*4+"Ulfi Saidata Aesyi, S.Kom., M.Cs."+' '*4+'<'+'-'*8+'='*8+'|')
    print('|'+'_'*30+" Dosen Pengampu "+'_'*29+'|')
    print('|'+' '*75+'|')

    print('|'+'='*8+'-'*8+'>'+' '*11+" Bagas Dwi Santosa "+' '*11+'<'+'-'*8+'='*8+'|')
    print('|'+'_'*32+" 212103006 "+'_'*32+'|')
    print('|'+' '*75+'|')

    print('|'+'='*8+'-'*8+'>'+' '*11+" Adha Rahmatullah  "+' '*11+'<'+'-'*8+'='*8+'|')
    print('|'+'_'*32+" 212103006 "+'_'*32+'|')
    print('|'+' '*75+'|')

    print('|'+'='*8+'-'*8+'>'+' '*12+" Muhammad Roykhan "+' '*11+'<'+'-'*8+'='*8+'|')
    print('|'+'_'*32+" 212103006 "+'_'*32+'|')
    print('|'+' '*75+'|')

    print('|'+'='*8+'-'*8+'>'+' '*13+" Nurul Fatimah "+' '*13+'<'+'-'*8+'='*8+'|')
    print('|'+'_'*32+" 212103006 "+'_'*32+'|')
    print('|'+'_'*75+'|')
    
def saran():
    saran = input("\n Masukan saran dan tanggapan untuk program kami, Enter untuk mengirim\n=> ")
    saran_txt = open("saran.txt", "a")
    saran_txt.write(saran)
    saran_txt.close()
    return saran
    

pilihan = int()
kuis = kuis_1()

while pilihan < 5 :
    pilihan = menu()
    if pilihan == 1:
        print(' '+'_'*75+' ')
        print('|'+' '*75+'|')
        print('|'+'='*10+'-'*8+'>'+' '*6+" GAME QUIZ BASIC PYTHON "+' '*7+'<'+'-'*8+'='*10+'|')
        print('|'+'_'*75+'|\n')
        print("Pilih jawaban yang paling benar dan input jawaban menggunakan huruf besar!!!\n ")
        try:
            #Soal 1
            print(kuis[0])
            for i in kuis[1:6]:
                print(i)
            jawab = input("Masukkan jawaban anda : ")
            if jawab == "C" or jawab == "c":
                print("Jawaban anda Benar")
                nilai = nilai + 20
            else:
                print("Jawaban anda Salah")

            lanjut = input("Tekan enter untuk lanjut\n")

            #Soal 2
            print(kuis[7])
            for i in kuis[8:13]:
                print(i)
            jawab = input("Masukkan jawaban anda : ")
            if jawab == "D" or jawab == "d":
                print("Jawaban anda Benar")
                nilai = nilai + 20
            else:
                print("Jawaban anda Salah")

            lanjut = input("Tekan enter untuk lanjut\n")

            #Soal 3
            print(kuis[14])
            for i in kuis[15:20]:
                print(i)
            jawab = input("Masukkan jawaban anda : ")
            if jawab == "B" or jawab == "b":
                print("Jawaban anda Benar")
                nilai = nilai + 20
            else:
                print("Jawaban anda Salah")

            lanjut = input("Tekan enter untuk lanjut\n")

            #Soal 4
            print(kuis[21])
            for i in kuis[22:27]:
                print(i)
            jawab = input("Masukkan jawaban anda : ")
            if jawab == "B" or jawab == "b":
                print("Jawaban anda Benar")
                nilai = nilai + 20
            else:
                print("Jawaban anda Salah")
            total = str(nilai)

            lanjut = input("Tekan enter untuk lanjut\n")

            #Soal 5
            print(kuis[28])
            for i in kuis[29:34]:
                print(i)
            jawab = input("Masukkan jawaban anda : ")
            if jawab == "A" or jawab == "a":
                print("Jawaban anda Benar")
                nilai = nilai + 20
            else:
                print("Jawaban anda Salah")
            total_nilai = str(nilai)

            print("\nHai {} score kuis kamu adalah {}".format(nama,total_nilai))
            lanjut = input("\n Kembali ke Menu utama ? yes/no : ")
            if lanjut == "yes":
                print()

            else:
                print(' '+'_'*75+' ')
                print('|'+' '*75+'|')
                print("|"+'='*8+'-'*7+'>'+"  Terimakasih sudah mencoba Program kami   "+'<'+'-'*7+'='*8+'|')
                print('|'+'='*8+'-'*7+'>'+' '*9+" Sampai Berjumpa Kembali "+' '*9+'<'+'-'*7+'='*8+'|')
                print("|"+("_"*75)+"|")
                break

        except ValueError:
            print(" Masukan jawaban A, B, C, D dan E, bukan yang lainnya.")


    elif pilihan == 2:
        score()
        lanjut = input("\n Kembali ke Menu utama ? yes/no : ")
        if lanjut == "yes":
            print()

        else:
            print(' '+'_'*75+' ')
            print('|'+' '*75+'|')
            print("|"+'='*8+'-'*7+'>'+"  Terimakasih sudah mencoba Program kami   "+'<'+'-'*7+'='*8+'|')
            print('|'+'='*8+'-'*7+'>'+' '*9+" Sampai Berjumpa Kembali "+' '*9+'<'+'-'*7+'='*8+'|')
            print("|"+("_"*75)+"|")
            break


    elif pilihan == 3:
        info_kami()
        lanjut = input("\n Kembali ke Menu utama ? yes/no : ")
        if lanjut == "yes":
            print()
        else:
            print(' '+'_'*75+' ')
            print('|'+' '*75+'|')
            print("|"+'='*8+'-'*7+'>'+"  Terimakasih sudah mencoba Program kami   "+'<'+'-'*7+'='*8+'|')
            print('|'+'='*8+'-'*7+'>'+' '*9+" Sampai Berjumpa Kembali "+' '*9+'<'+'-'*7+'='*8+'|')
            print("|"+("_"*75)+"|")
            break


    elif pilihan == 4 :
        saran()
        print(' '+'_'*75+' ')
        print('|'+' '*75+'|')
        print("|"+'='*8+'-'*7+'>'+"  Saran dan Tanggapan anda sudah tersimpan "+'<'+'-'*7+'='*8+'|')
        print("|"+("_"*75)+"|")
        lanjut = input("\n Kembali ke Menu utama ? yes/no : ")
        if lanjut == "yes":
            print()

        else:
            print(' '+'_'*75+' ')
            print('|'+' '*75+'|')
            print("|"+'='*8+'-'*7+'>'+"  Terimakasih sudah mencoba Program kami   "+'<'+'-'*7+'='*8+'|')
            print('|'+'='*8+'-'*7+'>'+' '*9+" Sampai Berjumpa Kembali "+' '*9+'<'+'-'*7+'='*8+'|')
            print("|"+("_"*75)+"|")
            break


    else:
        print(' '+'_'*75+' ')
        print('|'+' '*75+'|')
        print("|"+'='*8+'-'*7+'>'+"  Terimakasih sudah mencoba Program kami   "+'<'+'-'*7+'='*8+'|')
        print('|'+'='*8+'-'*7+'>'+' '*9+" Sampai Berjumpa Kembali "+' '*9+'<'+'-'*7+'='*8+'|')
        print("|"+("_"*75)+"|")
        break






    

