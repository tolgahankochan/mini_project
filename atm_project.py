#proje detaylarını github hesabından bulabilir ve kendiniz uygulayabilirsiniz.

#ilk olarak hesapları tanımladık
 
sadik_account = {
    'name':"Sadık Turan",
    'accountnumber':'123654789',
    'remainder': 4500,
    'additional account':2000

}

tolga_account = { 
    'name':"Tolgahan Koçhan",
    'accountnumber':'546789123',
    'remainder': 10500,
    'additional_account':4000

}

#daha sonra ise işlemi gerçekleştirecek olan fonksiyonu hesap ve çekilecek miktar girişi istenecek şekilde tanımladık.

def withdraw_money(account, amount):

    #Girilen kullanıcı hesabıyla beraber müşteriye mesaj gönderdik
    print(f"Hi, {account['name']}")

    #eğer bakiyemiz istenen miktara eşit veya ondan büyükse para çekme işlemi onaylanacak ve mesaj gönderilecek.
    if (account['remainder'] >= amount):

        #hesaptan, çekilen tutarı eksiltiyoruz.
         
        account['remainder'] -= amount

        print('You can get your money')


    #eğer değilse de ek hesaptaki miktar ile ana hesaptaki miktarın toplamına bakılacak.
    else:
        total = int(account['remainder'] + account['additional_account'])

        #eğer toplam miktar istenen miktardan büyük veya eşitse kullanıcıya ek hesapı kullanmak istemediği sorulacak.
        if (total >= amount):
            using_additional_account = input("Should I use an additional account ? (Y/N) : ")

            #eğer ek hesabı kullanmak istiyorsa para çekim işlemi gerçekleşecek. 
            if using_additional_account =='y' or using_additional_account =="Y":
                #ana hesaptan para azaltma işlemi yaptık
                account['remainder'] -= amount

                #ek hesaptan para azaltma işlemi için ne kadar miktar kullanılacağını bir değişkene atadık
                for_using_additional_account = amount - account['remainder']

                #ana hesabı sıfırladık
                account['remainder'] = 0 

                #ek hesaptan para azaltma işlemi yaptık
                account['additional_account'] -= for_using_additional_account
                print("You can get your money")

            #eğer istenmiyorsa da hesaptaki miktar hesap numarası ile birlikte kullanıcıya rapor edilecek.
            else:
                print(f"{account['accountnumber']} / your account balance : {account['remainder']} ")    

        #eğer toplam miktar istenenden küçükse yetersiz bakiye bildirimi kullanıcıya gösterilecek.
        else:
            print("Sorry, Your balance is not enough ")

    print("************************************")

#fonksiyonu çağırma işlemi yaptık

withdraw_money(tolga_account,9600)
withdraw_money(tolga_account,3200)












