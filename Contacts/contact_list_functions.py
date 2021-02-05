# Ime- 
# God- 
# Adrese - list 
# Broj telefona - list 
# Email - list

def new_contact(contact_list):

    sve_adrese = []
    svi_telefoni = []
    svi_mailovi = []
    contact = {}
    contact['Ime'] = input("Unesi ime: ")
    contact['Godine'] = int(input("Unesi godine: "))

    adrese = input("Unesi adresu: ")
    sve_adrese.append(adrese)
    contact["Adresa(e)"] = sve_adrese

    telefon = input("Unesi broj telefona: ")
    svi_telefoni.append(telefon)
    contact["Telefon(i)"] = svi_telefoni

    email = input("Unesi Email: ")
    svi_mailovi.append(email)
    contact["Email(ovi)"] = svi_mailovi
    contact_list.append(contact)

def remove_contact(contact_list):
    view_contact(contact_list)
    remove = int(input("Koji kontakt bi obrisali? "))
    if 0 < remove <= len(contact_list):
        del contact_list[remove -1]
        print("Kontakt obrisan")    
    else:
        print("Error.")

def view_contact(contact_list):
    if len(contact_list) == 0:
        print("Nema kontakata")
    else:
        for i in range(len(contact_list)):
            print(i+1, contact_list[i])