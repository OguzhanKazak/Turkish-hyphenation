from tkinter import *

window = Tk()
window.title = "Hecelere Ayır"
window.geometry("500x150")

label1 = Label(window,text="Heceleri ayırmak istediğin cümleyi yaz.")
label1.grid(column=0,row=0)

label2 = Label(window,text="")
label2.grid(column=0,row=2)

entry1 = Entry(window,width = 50)
entry1.grid(column=0,row=1)


vowels = {"a", "e", "ı", "i", "o", "ö", "u", "ü"}
consonants = {"b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"}

sentence = ""

def spell_onClick():
    sentence = entry1.get()
    sentence = sentence.lower()
    sentence_array = sentence.split(" ")

    spelled_sentence = make_sentence(sentence_array)
    label2.configure(text = spelled_sentence)


button1 = Button(window, text="Hecele", command=spell_onClick)
button1.grid(column=1, row=1)

def find_vowel_count(word):
    count = 0
    for letter in word:
        if(letter in vowels):
            count+=1
    return count

def spell(word):
    #kural 1: Türkçede kelime içinde iki ünlü arasındaki ünsüz, kendinden sonraki ünlüyle hece kurar
    #kural 2: Kelime içinde yan yana gelen iki ünsüzden ilki kendinden önceki ünlüyle, ikincisi kendinden sonraki ünlüyle hece kurar
    #kural 3: Kelime içinde yan yana gelen üç ünsüz harften ilk ikisi kendinden önceki ünlüyle, üçüncüsü kendinden sonraki ünlüyle hece kurar
    count = 0
    syllabels = []
    for i in range(len(word)):
        try:
            if(word[count] in vowels):
                if(word[count+1] in vowels):#birleşik kelimelerde (baba*evi)
                    syllabels.append(word[:count + 1])
                    word = word[count + 1:]
                    count = 0
                elif (word[count+2] in vowels): # kural 1
                    syllabels.append(word[:count + 1])
                    word= word[count + 1:] #kelimenin öncesini hece olarak alıp devamını yeni kelime olarak devam ettiriyoruz. Kelimenin devamı başka kurallara uyuyor olabilir
                    count = 0
                elif(word[count+3] in vowels): # kural2
                    syllabels.append(word[:count + 2])
                    word = word[count + 2:]
                    count = 0
                elif(word[count+4] in vowels): # kural 3
                    syllabels.append(word[:count + 3])
                    word = word[count + 3:]
                    count = 0

            else:
                count+=1
        except IndexError:
            continue

    if (find_vowel_count(word) == 1):
        syllabels.append(word)

    return syllabels

def make_sentence(sentence_array):
    spelled_sentence = ""
    for word in sentence_array:
        syllable_array = spell(word)
        for syllable in syllable_array:
            if(syllable_array[len(syllable_array)-1] != syllable):
                spelled_sentence += syllable + "-"
            else:
                spelled_sentence += syllable + "  "
    return spelled_sentence



window.mainloop()