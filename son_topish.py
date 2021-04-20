import random as r
def kopyuter_uylagan_soni():
    print('men 1dan 10 gacha son o`yladim siz shuni o`ylap topingchi =>')
    kompyuter_soni=r.randint(1,10)
    urinishlar_soni_odam=0
    while True:
        men_kiritgan_son=int(input('1 dan 10gacha son kiriting: '))
        if men_kiritgan_son<kompyuter_soni:
            print('men o`ylagan son siz kiritgandan KATTA!')
            urinishlar_soni_odam+=1
        elif men_kiritgan_son>kompyuter_soni:
            print('men o`ylagan son siz kiritgandan KICHIK!')
            urinishlar_soni_odam+=1
        else:
            print('TABRIKLAYMAN TOPDINGGIZ!')
            urinishlar_soni_odam+=1
            print(f'siz {urinishlar_soni_odam} ta urinish bilan topdinggiz!')
            javob=input("yana o`ynaysizmi (y/n): ")
            if javob == 'n':
                break
            else:
                men_uylagan_son()
def men_uylagan_son():
    print('endi siz o`ylaysiz men topaman!!')
    son_uyla_va_kirit=int(input('o`ylagan soningni kirit: '))
    urnishlar_soni_komp=0
    boshlanishi=1
    oxri=10
    while True:
  
        random_uylagan_soni=r.randint(boshlanishi,oxri)
        print(f'siz o`ylagan son bundan => {random_uylagan_soni} kattami yoki kichik?|| {boshlanishi} {oxri} ||')
        y_n=input('katta bo`lsa ( + ) kichik bo`lsa ( - ) ni kiriting  to`g`ri topgan bo`lsam ( t ) ni kiriting : ')
        if y_n=='+':
            boshlanishi=random_uylagan_soni+1
            urnishlar_soni_komp+=1
        elif y_n=='-':
            oxri=random_uylagan_soni-1
            urnishlar_soni_komp+=1
        else:
            urnishlar_soni_komp+=1
            print(f'{urnishlar_soni_komp} ta urinishda to`ri topdim!!')
            print('yana o`ynaysizmi?')
            h_y=input('ha yoki yo`q (h/y): ')
            if h_y=='y':
                print("Xayr!!")
            else: 
                kopyuter_uylagan_soni()
                


    
kopyuter_uylagan_soni()